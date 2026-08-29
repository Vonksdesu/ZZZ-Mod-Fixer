#!/usr/bin/env python3
"""
ZZZ Mod Fixer — Rollback Core
File: zzz-mod-fixer-rollback.py

Manages automatic hidden backup of INI and BUF files during every tool run,
and provides restore / delete operations for the Rolling Back UI section.

All backups are stored in:
    %LOCALAPPDATA%\\Hash_ZZZ_Caches\\
        Hash Character Mods Updater\\
            (.ini) Caches\\
                2026-04-15_10-12-58\\     <- one folder = one tool run session
                    session.json           <- metadata + original paths
                    charA.txt              <- INI backed up as .txt
                    charB.txt
            (.buf) Backup\\
                2026-04-15_10-12-58\\
                    session.json
                    charA.buf
        Jane Doe Remapper\\
            (.buf) JaneDoe Backup\\
                2026-04-15_10-12-58\\
                    session.json
                    jane_hair.buf
        Dialyn Remapper\\
            (.buf) Dialyn Backup\\
                2026-04-15_10-12-58\\
                    session.json
                    dialyn_body.buf

This module is completely independent from the checkbox-based user-visible
backup system. It always runs silently in the background whenever files are
actually modified by any of the three tools.

GUI integration points (zzz-mod-fixer-gui.py):

  1. Import via importlib at application startup (same pattern as other tools).

  2. In each tool worker, BEFORE tool starts:
         session_ctx = rollback.begin_session("Hash Character Mods Updater")

  3. Inside patched save / remap_binary, BEFORE file is overwritten:
         rollback.backup_ini_file(original_ini_path, session_ctx)
         rollback.backup_buf_file(original_buf_path, session_ctx)

  4. In each tool worker, AFTER tool finishes:
         rollback.finalize_session(session_ctx)

  5. Rolling Back UI - populate session cards (panel kiri):
         sessions = rollback.list_sessions(section, file_type)

  6. Rolling Back UI - populate file rows (panel kanan, after Sync click):
         files = rollback.load_session_files(session_dir)

  7. Rolling Back UI - button actions:
         rollback.restore_file(session_dir, file_entry)
         rollback.delete_file(session_dir, file_entry)
         rollback.restore_all(session_dir)
         rollback.delete_all(session_dir)
"""

import os
import json
import shutil
import datetime
from pathlib import Path


# -----------------------------------------------------------------------------
#  CONSTANTS
# -----------------------------------------------------------------------------

BASE_CACHE_FOLDER = "Hash_ZZZ_Caches"
SESSION_MANIFEST  = "session.json"

# File types supported by each sidebar section
SECTION_FILE_TYPES = {
    "Hash Character Mods Updater": ["ini", "buf"],
    "Jane Doe Remapper":           ["buf"],
    "Dialyn Remapper":             ["buf"],
}

# Subfolder name inside each section directory, keyed by file type
TYPE_SUBFOLDERS = {
    "Hash Character Mods Updater": {
        "ini": "(.ini) Caches",
        "buf": "(.buf) Backup",
    },
    "Jane Doe Remapper": {
        "buf": "(.buf) JaneDoe Backup",
    },
    "Dialyn Remapper": {
        "buf": "(.buf) Dialyn Backup",
    },
}


# -----------------------------------------------------------------------------
#  PATH RESOLUTION
# -----------------------------------------------------------------------------

def get_base_cache_dir():
    """
    Returns the base cache root:
        %LOCALAPPDATA%\\Hash_ZZZ_Caches

    Raises EnvironmentError if LOCALAPPDATA is unavailable.
    """
    local_appdata = os.environ.get("LOCALAPPDATA")
    if not local_appdata:
        raise EnvironmentError(
            "LOCALAPPDATA environment variable is not available. "
            "Rollback cache cannot be located on this system."
        )
    return Path(local_appdata) / BASE_CACHE_FOLDER


def get_type_dir(section, file_type):
    """
    Returns the directory that holds all session folders for a given
    section + file_type combination.

    Example:
        get_type_dir("Hash Character Mods Updater", "ini")
        -> ...\\Hash_ZZZ_Caches\\Hash Character Mods Updater\\(.ini) Caches

    Raises ValueError for unknown section or file_type.
    """
    if section not in TYPE_SUBFOLDERS:
        raise ValueError(f"Unknown section: '{section}'")
    type_map = TYPE_SUBFOLDERS[section]
    if file_type not in type_map:
        raise ValueError(
            f"Section '{section}' does not support file type '{file_type}'. "
            f"Supported: {list(type_map.keys())}"
        )
    return get_base_cache_dir() / section / type_map[file_type]


def get_supported_types(section):
    """Returns the list of file types a section supports, e.g. ['ini', 'buf']."""
    return SECTION_FILE_TYPES.get(section, [])


def is_available():
    """
    Returns True if the rollback system can locate its cache directory.
    The GUI calls this on startup to decide whether to enable Rolling Back.
    """
    try:
        get_base_cache_dir()
        return True
    except EnvironmentError:
        return False


# -----------------------------------------------------------------------------
#  SESSION CREATION  (called by GUI workers before/during tool execution)
# -----------------------------------------------------------------------------

def begin_session(section):
    """
    Creates and returns a session context for one complete tool run.
    Must be called BEFORE the tool begins modifying any files.

    The returned dict is passed to backup_ini_file() / backup_buf_file()
    as files are processed, and finally to finalize_session() when the
    tool finishes.

    Session context structure:
    {
        "session_id": "2026-04-15_10-12-58",
        "timestamp":  1745310778,
        "datetime":   "2026-04-15 10:12:58",
        "section":    "Hash Character Mods Updater",
        "types": {
            "ini": {
                "session_dir": Path(...\\.(.ini) Caches\\2026-04-15_10-12-58),
                "files":       []   <- populated by backup_ini_file()
            },
            "buf": {
                "session_dir": Path(...\\(.buf) Backup\\2026-04-15_10-12-58),
                "files":       []   <- populated by backup_buf_file()
            }
        }
    }
    """
    now        = datetime.datetime.now()
    session_id = now.strftime("%Y-%m-%d_%H-%M-%S")
    timestamp  = int(now.timestamp())
    dt_str     = now.strftime("%Y-%m-%d %H:%M:%S")

    ctx = {
        "session_id": session_id,
        "timestamp":  timestamp,
        "datetime":   dt_str,
        "section":    section,
        "types":      {},
    }

    for ft in get_supported_types(section):
        type_dir    = get_type_dir(section, ft)
        session_dir = type_dir / session_id
        ctx["types"][ft] = {
            "session_dir": session_dir,
            "files":       [],
        }

    return ctx


def backup_ini_file(original_path, session_ctx):
    """
    Copies an INI file into the session's (.ini) Caches folder as a .txt backup.

    IMPORTANT: Call this BEFORE the original file is moved or overwritten
    by the tool. The original_path must still exist on disk.

    Naming: original_path.stem + ".txt"
            e.g. "charA.ini" is backed up as "charA.txt"
    Name collisions (two INIs with the same stem) are resolved:
            "charA_1.txt", "charA_2.txt", ...

    Updates session_ctx["types"]["ini"]["files"] in-place.
    Returns True on success, False on failure.
    """
    ini_ctx = session_ctx["types"].get("ini")
    if ini_ctx is None:
        return False  # This section does not back up INI files

    original_path = Path(original_path)
    if not original_path.exists():
        return False

    session_dir = Path(ini_ctx["session_dir"])
    session_dir.mkdir(parents=True, exist_ok=True)

    backup_name = original_path.stem + ".txt"
    backup_path = session_dir / backup_name

    counter = 1
    while backup_path.exists():
        backup_name = f"{original_path.stem}_{counter}.txt"
        backup_path = session_dir / backup_name
        counter += 1

    try:
        shutil.copy2(str(original_path), str(backup_path))
        ini_ctx["files"].append({
            "backup_name":   backup_name,
            "original_path": str(original_path.resolve()),
            "original_type": "ini",
        })
        return True
    except Exception as e:
        return False


def backup_buf_file(original_path, session_ctx):
    """
    Copies a BUF file into the session's (.buf) folder.

    IMPORTANT: Call this BEFORE the original file is overwritten by the tool.

    Name collisions resolved: "charA_1.buf", "charA_2.buf", ...

    Updates session_ctx["types"]["buf"]["files"] in-place.
    Returns True on success, False on failure.
    """
    buf_ctx = session_ctx["types"].get("buf")
    if buf_ctx is None:
        return False

    original_path = Path(original_path)
    if not original_path.exists():
        return False

    session_dir = Path(buf_ctx["session_dir"])
    session_dir.mkdir(parents=True, exist_ok=True)

    backup_name = original_path.name
    backup_path = session_dir / backup_name

    counter = 1
    while backup_path.exists():
        backup_name = f"{original_path.stem}_{counter}{original_path.suffix}"
        backup_path = session_dir / backup_name
        counter += 1

    try:
        shutil.copy2(str(original_path), str(backup_path))
        buf_ctx["files"].append({
            "backup_name":   backup_name,
            "original_path": str(original_path.resolve()),
            "original_type": "buf",
        })
        return True
    except Exception as e:
        return False


def finalize_session(session_ctx):
    """
    Called AFTER the tool worker finishes. For each file type:

    - If files were backed up:
        writes session.json and keeps the session folder.
        This session will appear as a card in the Rolling Back history.

    - If no files were backed up (tool ran but nothing actually changed):
        removes the session folder if it was created, does NOT create
        a history entry. Satisfies: "no real change = no session".

    Returns a summary of how many files were saved per type:
        {"ini": 3, "buf": 5}    (0 = no session created for that type)
    """
    summary = {}

    for ft, type_ctx in session_ctx["types"].items():
        session_dir = Path(type_ctx["session_dir"])
        files       = type_ctx["files"]

        if not files:
            if session_dir.exists():
                try:
                    shutil.rmtree(str(session_dir))
                except Exception:
                    pass
            summary[ft] = 0
            continue

        manifest = {
            "session_id": session_ctx["session_id"],
            "timestamp":  session_ctx["timestamp"],
            "datetime":   session_ctx["datetime"],
            "section":    session_ctx["section"],
            "type":       ft,
            "files":      files,
        }

        manifest_path = session_dir / SESSION_MANIFEST
        try:
            with open(str(manifest_path), "w", encoding="utf-8") as f:
                json.dump(manifest, f, indent=2, ensure_ascii=False)
            summary[ft] = len(files)
            print(
                f"— {len(files)} {ft.upper()} file(s)."
            )
        except Exception as e:
            summary[ft] = 0

    return summary


# -----------------------------------------------------------------------------
#  SESSION LISTING  (called by Rolling Back UI to build session cards)
# -----------------------------------------------------------------------------

def list_sessions(section, file_type):
    """
    Returns all valid sessions for a given section + file_type, newest first.

    Each entry in the returned list:
    {
        "session_id":  "2026-04-15_10-12-58",
        "timestamp":   1745310778,
        "datetime":    "2026-04-15 10:12:58",
        "section":     "Hash Character Mods Updater",
        "type":        "ini",
        "session_dir": Path(...),
        "file_count":  3,
    }

    A folder without a readable session.json is silently skipped.
    Returns [] if the type directory does not exist or has no valid sessions.
    """
    try:
        type_dir = get_type_dir(section, file_type)
    except ValueError:
        return []

    if not type_dir.exists():
        return []

    sessions = []
    for item in type_dir.iterdir():
        if not item.is_dir():
            continue
        manifest_path = item / SESSION_MANIFEST
        if not manifest_path.exists():
            continue
        try:
            with open(str(manifest_path), "r", encoding="utf-8") as f:
                manifest = json.load(f)
            sessions.append({
                "session_id":  manifest.get("session_id",  item.name),
                "timestamp":   manifest.get("timestamp",   0),
                "datetime":    manifest.get("datetime",    item.name),
                "section":     manifest.get("section",     section),
                "type":        manifest.get("type",        file_type),
                "session_dir": item,
                "file_count":  len(manifest.get("files", [])),
            })
        except Exception:
            continue  # Corrupt session.json — skip silently

    sessions.sort(key=lambda s: s["timestamp"], reverse=True)
    return sessions


def load_session_files(session_dir):
    """
    Reads and returns the file list from a session's session.json.
    Used by the Rolling Back UI to populate the file rows in the right
    panel after the user clicks a session's Sync button.

    Each file entry:
    {
        "backup_name":   "charA.txt",
        "original_path": "D:\\ZZMI\\Mods\\CharA\\charA.ini",
        "original_type": "ini",
    }

    Returns [] if session.json is missing or unreadable.
    """
    manifest_path = Path(session_dir) / SESSION_MANIFEST
    if not manifest_path.exists():
        return []
    try:
        with open(str(manifest_path), "r", encoding="utf-8") as f:
            manifest = json.load(f)
        return manifest.get("files", [])
    except Exception:
        return []


# -----------------------------------------------------------------------------
#  INTERNAL HELPERS
# -----------------------------------------------------------------------------

def _write_session_manifest(session_dir, updated_files):
    """
    Overwrites the 'files' list in session.json while preserving all
    other metadata fields (session_id, datetime, section, type, ...).
    Returns True on success.
    """
    manifest_path = Path(session_dir) / SESSION_MANIFEST
    if not manifest_path.exists():
        return False
    try:
        with open(str(manifest_path), "r", encoding="utf-8") as f:
            manifest = json.load(f)
        manifest["files"] = updated_files
        with open(str(manifest_path), "w", encoding="utf-8") as f:
            json.dump(manifest, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        return False


def _has_backup_files(session_dir):
    """
    Returns True if at least one actual backup file remains in the session
    folder (session.json itself is not counted as a backup file).
    """
    session_dir = Path(session_dir)
    if not session_dir.exists():
        return False
    return any(
        True for f in session_dir.iterdir()
        if f.is_file() and f.name != SESSION_MANIFEST
    )


def _remove_session(session_dir):
    """Removes an entire session folder including session.json."""
    session_dir = Path(session_dir)
    if session_dir.exists():
        try:
            shutil.rmtree(str(session_dir))
        except Exception as e:
            pass


def _remove_entry_and_cleanup(session_dir, backup_name):
    """
    Removes a single file entry from session.json by backup_name.
    If no backup files remain after removal, deletes the session folder entirely.
    """
    session_dir = Path(session_dir)
    files   = load_session_files(session_dir)
    updated = [f for f in files if f.get("backup_name") != backup_name]

    if updated:
        _write_session_manifest(session_dir, updated)
        # Also remove folder if physical backups are all gone
        if not _has_backup_files(session_dir):
            _remove_session(session_dir)
    else:
        # Last entry removed — session is done
        _remove_session(session_dir)


# -----------------------------------------------------------------------------
#  RESTORE / DELETE  (called by Rolling Back UI button handlers)
# -----------------------------------------------------------------------------

def restore_file(session_dir, file_entry):
    """
    Restores a single backup file to its original location.

    INI -> copies .txt backup back to the original .ini path
    BUF -> copies .buf backup back to the original .buf path

    After a successful copy:
        - backup file is deleted from session folder
        - session.json is updated
        - session folder is removed if it has become empty

    Returns (success: bool, message: str).
    """
    session_dir   = Path(session_dir)
    backup_name   = file_entry.get("backup_name", "")
    original_path = file_entry.get("original_path", "")
    original_type = file_entry.get("original_type", "")

    if not backup_name:
        return False, "Invalid entry: 'backup_name' is missing."

    if not str(original_path).strip():
        return False, f"Invalid entry: 'original_path' is empty for {backup_name}."

    original_path = Path(original_path)
    backup_path   = session_dir / backup_name

    if not backup_path.exists():
        # Physical file already gone — still clean the manifest
        _remove_entry_and_cleanup(session_dir, backup_name)
        return False, f"Backup file not found on disk: {backup_name}"

    try:
        original_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(str(backup_path), str(original_path))
        backup_path.unlink()
        _remove_entry_and_cleanup(session_dir, backup_name)
        label = "INI" if original_type == "ini" else "BUF"
        return True, f"[{label}] Restored: {backup_name} -> {original_path.name}"
    except Exception as e:
        return False, f"Failed to restore {backup_name}: {e}"


def delete_file(session_dir, file_entry):
    """
    Permanently deletes a single backup file from the session (no restore).
    Updates session.json and removes the session folder if now empty.

    Returns (success: bool, message: str).
    """
    session_dir = Path(session_dir)
    backup_name = file_entry.get("backup_name", "")

    if not backup_name:
        return False, "Invalid entry: 'backup_name' is missing."

    backup_path = session_dir / backup_name

    try:
        if backup_path.exists():
            backup_path.unlink()
        _remove_entry_and_cleanup(session_dir, backup_name)
        return True, f"Deleted backup: {backup_name}"
    except Exception as e:
        return False, f"Failed to delete {backup_name}: {e}"


def restore_all(session_dir):
    """
    Restores every backup file in a session to its original location.

    Full success  -> session folder removed entirely.
    Partial fail  -> session.json updated with only failed entries;
                     their physical backups remain for a future retry.

    Returns (success_count: int, fail_count: int, messages: list[str]).
    """
    session_dir = Path(session_dir)
    files       = load_session_files(session_dir)
    ok          = 0
    fail        = 0
    msgs        = []
    failed      = []

    for entry in files:
        backup_name   = entry.get("backup_name", "")
        original_path = entry.get("original_path", "")
        original_type = entry.get("original_type", "")
        backup_path   = session_dir / backup_name

        if not backup_path.exists():
            fail += 1
            msgs.append(f"Not found: {backup_name}")
            failed.append(entry)
            continue

        if not str(original_path).strip():
            fail += 1
            msgs.append(f"Empty original path for: {backup_name}")
            failed.append(entry)
            continue

        try:
            dest = Path(original_path)
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(str(backup_path), str(dest))
            backup_path.unlink()
            ok += 1
            label = "INI" if original_type == "ini" else "BUF"
            msgs.append(f"[{label}] Restored: {backup_name}")
        except Exception as e:
            fail += 1
            msgs.append(f"Failed: {backup_name} — {e}")
            failed.append(entry)

    if failed:
        _write_session_manifest(session_dir, failed)
        if not _has_backup_files(session_dir):
            _remove_session(session_dir)
    else:
        _remove_session(session_dir)

    return ok, fail, msgs


def delete_all(session_dir):
    """
    Permanently deletes all backup files in a session (no restore).
    The session folder is always removed when this finishes,
    even if some individual deletions fail.

    Returns (success_count: int, fail_count: int, messages: list[str]).
    """
    session_dir = Path(session_dir)
    files       = load_session_files(session_dir)
    ok          = 0
    fail        = 0
    msgs        = []

    for entry in files:
        backup_name = entry.get("backup_name", "")
        backup_path = session_dir / backup_name
        try:
            if backup_path.exists():
                backup_path.unlink()
            ok += 1
            msgs.append(f"Deleted: {backup_name}")
        except Exception as e:
            fail += 1
            msgs.append(f"Failed to delete {backup_name}: {e}")

    # Always remove the session folder after delete_all
    _remove_session(session_dir)

    return ok, fail, msgs