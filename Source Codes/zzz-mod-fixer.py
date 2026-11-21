# Originally written by petrascyll
# Thanks to Leotorrez, CaveRabbit, and SilentNightSound for help
# Join AGMG: discord.gg/agmg

# 1.6 Hashes updated by HammyCatte
# 1.7 Hashes updated by shaojiang

# 2.5 update with dyanmic character data overhaul by ConfoundedHermit

# Last Updated: 2026-06-22
# Game Version at time of update: 3.0

import os
import re
import time
import json
import struct
import hashlib
import argparse
import traceback
import functools

from dataclasses import dataclass, field
from pathlib import Path

# Extra precaution to not 'fix' 
# the same buffer multiple times
global_modified_buffers: dict[str, list[str]] = {}


# MARK: Buffer state guard
# A .buf file cannot carry a marker of its own (every byte is vertex data) and the marker we
# write into the .ini disappears as soon as the user restores that .ini from a backup - which
# is exactly the case where a second pass used to corrupt the buffer.  The ledger below closes
# that gap: next to each buffer we record the SHA1 of the content we PRODUCED for a given fix.
# A guard may only skip when the bytes on disk hash to a recorded result, so a stale entry can
# never block a repair that is still needed - the content simply will not match.
FIXER_STATE_NAME = '.zzz-fixer-state.json'
_global_fixer_state: dict[str, dict] = {}


def sha1_of(data) -> str:
    return hashlib.sha1(bytes(data)).hexdigest()


def fixer_state_path(folder) -> Path:
    return Path(folder) / FIXER_STATE_NAME


def fixer_state(folder) -> dict:
    r"""Ledger of one folder (lazy, cached per process - buffers live next to their mod)."""
    key = str(Path(folder).resolve())
    if key not in _global_fixer_state:
        state = {}
        try:
            loaded = json.loads(fixer_state_path(folder).read_text(encoding='utf-8'))
            if isinstance(loaded, dict) and isinstance(loaded.get('buffers'), dict):
                state = loaded
        except Exception:
            state = {}          # missing/unreadable/corrupt ledger: nothing is recorded
        _global_fixer_state[key] = state
    return _global_fixer_state[key]


def recorded_buffer(buffer_filepath, data, prefix) -> dict | None:
    """Entry describing `data` as a result WE produced for this buffer family, else None.

    Matching is by content hash, so the answer is about the bytes that are actually there.
    """
    buffer_filepath = Path(buffer_filepath)
    entries = fixer_state(buffer_filepath.parent).get('buffers', {})
    for fix_id, entry in entries.get(buffer_filepath.name, {}).items():
        if not fix_id.startswith(prefix) or not isinstance(entry, dict):
            continue
        if entry.get('sha1') == sha1_of(data):
            return dict(entry, fix_id=fix_id)
    return None


def record_buffer(buffer_filepath, fix_id, data, stride=None):
    """Remember that `data` is the result of `fix_id` for this buffer (written by `save`)."""
    buffer_filepath = Path(buffer_filepath)
    state = fixer_state(buffer_filepath.parent)
    state.setdefault('buffers', {}).setdefault(buffer_filepath.name, {})[fix_id] = {
        'sha1': sha1_of(data),
        'size': len(data),
        'stride': stride,
    }


def flush_fixer_state(folder):
    """Write one folder's ledger; called once the buffers of that folder are on disk."""
    key = str(Path(folder).resolve())
    if key not in _global_fixer_state:
        return
    try:
        fixer_state_path(folder).write_text(
            json.dumps(_global_fixer_state[key], indent=1, sort_keys=True) + '\n',
            encoding='utf-8')
    except Exception as e:
        print('\t\u26a0  Could not write {}: {}'.format(FIXER_STATE_NAME, e))


def read_stride_marker(section_text) -> int | None:
    r"""The `;stride = N` line we leave behind in a resource section (None if absent)."""
    match = re.search(r'^[ \t]*;[ \t]*stride[ \t]*=[ \t]*(\d+)[ \t]*$', section_text,
                      flags=re.MULTILINE | re.IGNORECASE)
    return int(match.group(1)) if match else None


def read_blend_marker(section_text) -> str | None:
    """The `;blend_indices = remapped(<id>)` line we leave behind (None if absent)."""
    match = re.search(r'^[ \t]*;[ \t]*blend_indices[ \t]*=[ \t]*remapped\([ \t]*([0-9a-fA-F]+)[ \t]*\)[ \t]*$',
                      section_text, flags=re.MULTILINE | re.IGNORECASE)
    return match.group(1) if match else None


def blend_fix_id(old_indices, new_indices) -> str:
    """Short stable id of one blend-index mapping (used by both the marker and the ledger)."""
    seed = repr((tuple(old_indices), tuple(new_indices))).encode('utf-8')
    return hashlib.sha1(seed).hexdigest()[:12]


def buffer_state(declared_stride, buffer_size, marker_stride, recorded_result):
    r"""Decide what to do with a buffer whose stride shrinks by 12 bytes (`zzz_12`).

    Returns `(verdict, new_stride)`.  The decision is based on FILE STATE only
    (our ledger, our own `;stride` marker, the size of the buffer and the stride the .ini
    declares), never on an in-memory dedup set:

      `fresh`     the buffer is already converted; at most a stale `stride` line needs fixing
      `legacy`    still the legacy layout with the declared stride - safe to shrink
      `uncertain` cannot tell (the declaration does not fit the buffer) - touch nothing
    """
    new_stride = declared_stride - 12
    if recorded_result:
        return 'fresh', recorded_result.get('stride') or new_stride
    if marker_stride is not None and new_stride > 0 \
            and buffer_size % new_stride == 0 and buffer_size % declared_stride != 0:
        return 'fresh', new_stride
    if declared_stride > 0 and buffer_size % declared_stride == 0:
        return 'legacy', new_stride
    return 'uncertain', new_stride


def main():
    parser = argparse.ArgumentParser(
        prog="ZZZ Fix 3.0 by ConfoundedHermit",
        description=('')
    )

    parser.add_argument('ini_filepath', nargs='?', default=None, type=str)
    args = parser.parse_args()

    if args.ini_filepath:
        if args.ini_filepath.endswith('.ini'):
            print('Passed .ini file:', args.ini_filepath)
            upgrade_ini(args.ini_filepath)
        else:
            raise Exception('Passed file is not an Ini')

    else:
        # Change the CWD to the directory this script is in
        # Nuitka: "Onefile: Finding files" in https://nuitka.net/doc/user-manual.pdf 
        # I'm not using Nuitka anymore but this distinction (probably) also applies for pyinstaller
        print('CWD: {}'.format(os.path.abspath('.')))
        process_folder('.')

    print('Done!')


# SHAMELESSLY (mostly) ripped from genshin fix script
def process_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.upper().startswith('DISABLED') and filename.lower().endswith('.ini'):
            continue
        if filename.upper().startswith('DESKTOP'):
            continue

        filepath = os.path.join(folder_path, filename)
        if os.path.isdir(filepath):
            process_folder(filepath)
        elif filename.endswith('.ini'):
            print('Found .ini file:', filepath)
            upgrade_ini(filepath)


def report_skipped_unfixable(ini):
    """End-of-file summary of the parts `skip_unfixable_update` left untouched.

    Printed for every ini that hit at least one class A/C/D hash, so the CLI and
    the GUI CLI-output both show it without extra plumbing (the GUI redirects
    `sys.stdout` while running the engine).
    """
    skipped = getattr(ini, 'skipped_unfixable', None)
    if not skipped:
        return
    print()
    print('! {} part(s) were left untouched: the model changed in a newer game '
          'version,'.format(len(skipped)))
    print('! so a hash replacement there would reuse old geometry and corrupt the mod.')
    print('! This is deliberate - see AIWorks/transisi_tidak_dapat_diperbaiki.json.')
    for hash, component, era in skipped:
        print('    - {:8} {}{}'.format(hash, component,
                                    ' (changed in %s)' % era if era else ''))
    print()


def report_failed_parts(ini):
    """End-of-file summary of the parts whose chain stopped on a failed command.

    `ExecutionResult.failed` used to be a silent stop: the remaining commands of that part were
    skipped, yet the file was saved and reported as fixed. Same style as
    `report_skipped_unfixable`, so the CLI and the GUI CLI panel both show it.
    """
    failed = getattr(ini, 'failed_hashes', None)
    if not failed:
        return
    print()
    print('! {} part(s) could not be repaired: the command chain stopped there,'.format(len(failed)))
    print('! so the rest of that part was left as it was.')
    for hash, command in failed:
        print('    - {:8} {}'.format(hash, command))
    print()


def upgrade_ini(filepath):
    try:
        # Errors occuring here is fine as no write operations to the ini nor any buffers are performed
        ini = Ini(filepath).upgrade()
    except Exception as x:
        print('Error occurred: {}'.format(x))
        print('No changes have been applied to {}!'.format(filepath))
        print()
        print(traceback.format_exc())
        print()
        return False

    try:
        # Content of the ini and any modified buffers get written to disk in this function
        # Since the code for this function is more concise and predictable, the chance of it failing
        # is low, but it can happen if Windows doesn't want to cooperate and write for whatever reason.
        ini.save()
    except Exception as X:
        print('Fatal error occurred while saving changes for {}!'.format(filepath))
        print('Its likely that your mod has been corrupted. You must redownload it from the source before attempting to fix it again.')
        print()
        print(traceback.format_exc())
        print()
        return False

    report_skipped_unfixable(ini)
    report_failed_parts(ini)
    return True


# MARK: Ini
class Ini():
    def __init__(self, filepath):
        self.filepath = filepath
        # Read the RAW bytes so the original line ending survives: `Path.read_text()` translates
        # `\r\n` to `\n`, and `save()` used to translate it back to `\r\n` on Windows, so every
        # LF mod became a CRLF one just because the tool touched it.
        raw = Path(self.filepath).read_bytes()
        try:
            text = raw.decode('utf-8')
            self.encoding = 'utf-8'
        except UnicodeDecodeError:
            text = raw.decode('gb2312')
            self.encoding = 'gb2312'

        # A file that uses CRLF everywhere is written back with CRLF; anything else (all LF, or a
        # mixture of both) is written with LF - the form `self.content` is kept in.
        self.line_ending = ('\r\n' if text.count('\r\n') and
                            text.count('\n') == text.count('\r\n') else '\n')
        self.content = text.replace('\r\n', '\n')
        

        # The random ordering of sets is annoying
        # Use a list for the hashes that will be iterated on
        # and a set for the hashes I already iterated on
        self._hashes = []
        self._touched = False
        self._done_hashes = set()

        # Only write the modified buffers at the very end after the ini is saved, since
        # the ini can be backed up, while backing up buffers is not not reasonable.
        # Buffer with multiple fixes: will be read from the mod directory for the first
        # fix, and from this dict in memory for subsequent fixes 
        self.modified_buffers = {
            # buffer_filepath: buffer_data
        }

        # Parts that `skip_unfixable_update` refused to rewrite (model changed in a
        # newer version). Filled while the blocks run, printed once per file by
        # `report_skipped_unfixable`. Per-ini (not module-global) so repeated runs
        # from the GUI never accumulate each other's entries.
        self.skipped_unfixable = []

        # Parts whose command chain stopped on a failed command (`create_new_section` with an
        # unresolved placeholder, ...). Printed once per file by `report_failed_parts`, so a
        # half-fixed file can never be reported as a clean success.
        self.failed_hashes = []

        # Get all (uncommented) hashes in the ini.
        # `(?:^|\n)` so a `hash =` line at offset 0 (first line of the file) is found too -
        # without it that line stayed invisible and its block never ran. Values are lowered
        # because every key of `hash_commands` is lowercase, so a mod that writes its hashes
        # in uppercase used to be skipped with "No tasks available".
        pattern = re.compile(r'(?:^|\n)\s*hash\s*=\s*([a-f0-9]*)', flags=re.IGNORECASE)
        self._hashes = [h.lower() for h in pattern.findall(self.content)]
    
    def upgrade(self):
        while len(self._hashes) > 0:
            hash = self._hashes.pop()
            if hash not in self._done_hashes:
                if hash in hash_commands:
                    print(f'\tProcessing {hash}:')
                    default_args = DefaultArgs(hash=hash, ini=self, data={}, tabs=2)
                    self.execute(hash_commands[hash], default_args)
                else:
                    print(f'\tSkipping {hash}: No tasks available')
            else:
                print(f'\tSkipping {hash}: Already Checked/Processed')

            self._done_hashes.add(str(hash).lower())

        # Auto-detect logic for Jane Doe / Dialyn blend fixes has been moved
        # to the standalone remapper tools to avoid double-remap conflicts.
        # See: Jane.remapper.py / Dialyn.remapper.py

        return self

    def execute(self, commands, default_args):
        for command in commands:
            clss = command[0]
            args = command[1] if len(command) > 1 else {}
            instance = clss(**args) if isinstance(args, dict) else clss(*args) 
            result: ExecutionResult = instance.execute(default_args)

            self._touched = self._touched or result.touched
            if result.failed:
                # The chain stops here, but the rest of the file is still saved - so the failure
                # has to stay visible (`report_failed_parts`).
                self.failed_hashes.append((default_args.hash, getattr(clss, '__name__', '?')))
                print()
                return

            if result.queue_hashes:
                # Only add the hashes that I haven't already iterated on. Keys are lowercase,
                # so queued values are normalized the same way (`str()` keeps a non-string
                # argument from turning into an AttributeError that aborts the whole file).
                self._hashes.extend(set(str(h).lower() for h in result.queue_hashes)
                                    .difference(self._done_hashes))

            if result.queue_commands:
                self.execute(result.queue_commands, default_args)

            if result.signal_break:
                return

        return default_args

    def save(self):
        if self._touched:
            basename = os.path.basename(self.filepath).split('.ini')[0]
            
            backup_dir = None
            
            # --- START HEURISTIC AV FIX ---
            # Implemented a safe upward relative traversal to locate the root ZZMI cache directory.
            # This completely eliminates the need for aggressive A-Z drive enumeration,
            # which is commonly flagged by Antivirus heuristic engines as Ransomware/Spyware behavior.
            current_path = Path(self.filepath).parent.resolve()
            for parent in [current_path] + list(current_path.parents):
                test_path = parent / 'Data' / 'ZZMI'
                if test_path.is_dir():
                    backup_dir = test_path / '(.ini) Caches'
                    break
                if parent.name.upper() == 'ZZMI':
                    backup_dir = parent / '(.ini) Caches'
                    break
                test_path_direct = parent / 'ZZMI'
                if test_path_direct.is_dir():
                    backup_dir = test_path_direct / '(.ini) Caches'
                    break
            
            if backup_dir:
                backup_dir = str(backup_dir.absolute())
            else:
                # Safe fallback: Defaulting to the local mod directory.
                backup_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
            # --- END HEURISTIC AV FIX ---
            
            try:
                os.makedirs(backup_dir, exist_ok=True)
            except Exception as e:
                print(f"⚠  Failed to create external backup folder at '{backup_dir}': {e}")
                backup_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
            
            backup_filename = f'DISABLED_BACKUP_{int(time.time())}_{basename}.txt'
            backup_fullpath = os.path.join(backup_dir, backup_filename)

            try:
                import shutil
                shutil.move(self.filepath, backup_fullpath)
                print(f'Created Backup: {backup_filename} at {backup_dir}')
            except Exception as e:
                print(f"⚠  Failed to relocate backup externally (Different Drive/Access): {e}")
                
                try:
                    backup_fallback_filename = f'DISABLED_BACKUP_{int(time.time())}.{basename}.txt'
                    backup_fallback_dir = os.path.abspath(self.filepath.split(basename+'.ini')[0])
                    backup_fallback_path = os.path.join(backup_fallback_dir, backup_fallback_filename)
                    
                    # Byte copy: the emergency backup must be IDENTICAL to the original, so it
                    # must not be re-encoded nor re-ended by the text layer.
                    with open(self.filepath, 'rb') as original_file:
                        original_content = original_file.read()
                    with open(backup_fallback_path, 'wb') as backup_file:
                        backup_file.write(original_content)
                    print(f'Created Backup (Emergency): {backup_fallback_filename} at {backup_fallback_dir}')
                except Exception as ex:
                    print(f"✖ Failed to create emergency backup: {ex}")

            # `newline=''` stops Python from translating on top of `self.line_ending`, so an LF
            # mod stays LF and a CRLF mod stays CRLF.
            with open(self.filepath, 'w', encoding=self.encoding, newline='') as updated_ini:
                updated_ini.write(self.content.replace('\r\n', '\n')
                                  .replace('\n', self.line_ending))

            if len(self.modified_buffers) > 0:
                print('Writing updated buffers')
                
                # --- START HEURISTIC AV FIX (.BUF) ---
                # Safe upward relative traversal for .buf backup folder.
                buf_backup_dir = None
                current_path = Path(self.filepath).parent.resolve()
                for parent in [current_path] + list(current_path.parents):
                    test_path = parent / 'Data' / 'ZZMI'
                    if test_path.is_dir():
                        buf_backup_dir = test_path / '(.buf) Backup'
                        break
                    if parent.name.upper() == 'ZZMI':
                        buf_backup_dir = parent / '(.buf) Backup'
                        break
                    test_path_direct = parent / 'ZZMI'
                    if test_path_direct.is_dir():
                        buf_backup_dir = test_path_direct / '(.buf) Backup'
                        break
                # --- END HEURISTIC AV FIX (.BUF) ---
                
                for filepath, data in self.modified_buffers.items():
                    # Backup original file before overwriting
                    original_path = Path(filepath)
                    if original_path.exists():
                        # Determine backup filepath gracefully
                        if buf_backup_dir:
                            try:
                                relative = original_path.relative_to(Path(self.filepath).parent)
                                backup_file = Path(str(buf_backup_dir)) / relative
                            except ValueError:
                                backup_file = Path(str(buf_backup_dir)) / original_path.name
                        else:
                            # Fallback: Safe local assignment within the same mod directory
                            backup_file = original_path.parent / f'DISABLED_BACKUP_{int(time.time())}_{original_path.name}'
                        
                        try:
                            os.makedirs(str(backup_file.parent), exist_ok=True)
                            import shutil
                            shutil.copy2(str(original_path), str(backup_file))
                            print(f'\tBacked up: {original_path.name} -> {backup_file}')
                        except Exception as be:
                            print(f"\t⚠  Failed to backup {original_path.name}: {be}")
                    
                    # Write the new buffer
                    with open(filepath, 'wb') as f:
                        f.write(data)
                    print('\tSaved: {}'.format(filepath))

                # Only now are the bytes on disk, so this is the moment to persist the ledger
                # that lets the next pass tell "already fixed" from "still to fix".
                for folder in {str(Path(filepath).parent) for filepath in self.modified_buffers}:
                    flush_fixer_state(folder)

            print('Updates applied')
        else:
            print('No changes applied')
        print()

    def has_hash(self, hash):
        # Hashes are lowercase everywhere (`hash_commands` keys, `Ini._hashes`), so compare in
        # that form: an uppercase hash in a mod names the same part.
        hash = str(hash).lower()
        return (
            (hash in self._hashes)
            or (hash in self._done_hashes)
        )

    def section_blocks(self, title):
        r"""Body of every `[TextureOverride<title>]` section (all copies).

        `(?:^|\n)` is used so that a section which is the FIRST line of the file
        is detected as well (without it, `\n\[` never matches at offset 0 -
        proven by the provider-file patcher test, 12 Oct 2026).
        """
        blocks = []
        pattern = re.compile(r'(?:^|\n)\[TextureOverride%s\]' % re.escape(title))
        for match in pattern.finditer(self.content):
            following = re.compile(r'\n\[').search(self.content, match.end())
            blocks.append(
                self.content[match.end():following.start() if following else len(self.content)]
            )
        return blocks

    def has_hash_in_section(self, hash, title):
        r"""Whether `[TextureOverride<title>]` already carries that hash - either as
        an ACTIVE line or as the legacy comment (`; hash = x`) written by `update_hash`.

        `has_hash` only looks at active lines, so a section whose hash was just moved
        is left behind as `; hash = <old>`; `add_section_if_missing` then treats that
        section as missing and adds a NEW COPY on every run (measured 12 Oct 2026:
        active hashes of a synthetic mod went 122 -> 123 -> 124 -> 125, i.e.
        `[TextureOverrideNicole.Hair.IB]` grew by one section per run).
        """
        if self.has_hash(hash):
            return True
        if not title or not isinstance(title, str):
            return False
        pattern = re.compile(r'^\s*;?\s*hash\s*=\s*%s\s*$' % re.escape(hash),
                             flags=re.IGNORECASE | re.MULTILINE)
        return any(pattern.search(block) for block in self.section_blocks(title))


# MARK: Commands

def get_critical_content(section):
    hash = None
    match_first_index = None
    critical_lines = []
    pattern = re.compile(r'^\s*(.*?)\s*=\s*(.*?)\s*$', flags=re.IGNORECASE)

    for line in section.splitlines():
        line_match = pattern.match(line)
        
        if line.strip().startswith('['):
            continue
        elif line_match and line_match.group(1).lower() == 'hash':
            hash = line_match.group(2)
        elif line_match and line_match.group(1).lower() == 'match_first_index':
            match_first_index = line_match.group(2)
        else:
            critical_lines.append(line)

    return '\n'.join(critical_lines), hash, match_first_index


# Returns all resources used by a commandlist
# Hardcoded to only return vb1 i.e. texcoord resources for now
# (TextureOverride sections are special commandlists)
def process_commandlist(ini_content: str, commandlist: str, target: str):
    # The captured field name is compared case-insensitively: the pattern below is
    # IGNORECASE, so `VB1 =`/`RUN =` must behave like `vb1 =`/`run =`. The target is
    # escaped as well because it is interpolated into the pattern.
    target = target.lower()
    line_pattern = re.compile(r'^\s*(run|{})\s*=\s*(.*)\s*$'.format(re.escape(target)), flags=re.IGNORECASE)
    resources = []

    for line in commandlist.splitlines():
        line_match = line_pattern.match(line)
        if not line_match: continue

        if line_match.group(1).lower() == target:
            resources.append(line_match.group(2))

        # Must check the commandlists that are run within the
        # the current commandlist for the resource as well
        elif line_match.group(1).lower() == 'run':
            commandlist_title = line_match.group(2)
            pattern = get_section_title_pattern(commandlist_title)
            commandlist_match = pattern.search(ini_content + '\n[')
            if commandlist_match:
                sub_resources = process_commandlist(ini_content, commandlist_match.group(1), target)
                resources.extend(sub_resources)

    return resources


@dataclass
class DefaultArgs():
    hash : str
    ini  : Ini
    tabs : int
    data : dict[str, str]


@dataclass
class ExecutionResult():
    touched        : bool = False
    failed         : bool = False
    signal_break   : bool = False
    queue_hashes   : tuple[str] = None
    queue_commands : tuple[str] = None


@dataclass(init=False)
class log():
    text: tuple[str]

    def __init__(self, *text):
        self.text = text

    def execute(self, default_args: DefaultArgs):
        tabs        = default_args.tabs

        info  = self.text[0]
        hash  = self.text[1] if len(self.text) > 1 else ''
        title = self.text[2] if len(self.text) > 2 else ''
        rest  = self.text[3:] if len(self.text) > 3 else []

        s = '{}{:34}'.format('\t'*tabs, info)
        if hash  : s += ' - {:8}'.format(hash)
        if title : s += ' - {}'.format(title) 
        if rest  : s += ' - '.join(rest)

        print(s)

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass
class skip_unfixable_update():
    r"""A transition whose model changed. Writes NOTHING - only reports.

    For these hashes (class A/C/D in AIWorks/transisi_tidak_dapat_diperbaiki.json)
    a hash replacement is what BREAKS the mod: the old mesh/weights get renamed to
    the new hash, so the game renders old geometry as if it were the new model.
    The provider file comments them out (取消更新) and the DB transition log marks
    them 不可修复 (not repairable), so the correct action is to leave the part as
    it is and TELL the user, instead of writing `; hash = <old>` as if it worked.

    Registered per component-era group (1 IB + 4 VB) in the character modules, so
    a mod of that era gets one warning per skipped part plus an end-of-file summary
    (`report_skipped_unfixable`).
    """
    component : str = ''
    era       : str = ''

    def execute(self, default_args: DefaultArgs):
        tabs = default_args.tabs
        hash = default_args.hash
        pad  = '\t' * tabs

        head = '{}{:34}'.format(pad, '! Skipped (model changed):')
        head += ' {:8}'.format(hash)
        if self.component:
            head += ' - {}'.format(self.component)
        print(head)
        print('{}\t   old geometry/weights cannot be reused in {} - part left untouched'
              .format(pad, self.era or 'a newer version'))

        skipped = getattr(default_args.ini, 'skipped_unfixable', None)
        if skipped is not None:
            skipped.append((hash, self.component, self.era))

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass
class update_hash():
    new_hash: str

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash

        # `(?:^|\n)` so a `hash =` line at offset 0 is replaced as well; at offset 0 the
        # captured prefix is empty, so the output simply starts with the new hash line.
        # `(?![0-9A-Fa-f])` closes the value: without it a shorter hash also rewrote a longer hash
        # that merely starts with it (`cafebabe` cut `hash = cafebabe11` into `cafebabe99` + `11`).
        pattern = re.compile(r'((?:^|\n)\s*)(hash\s*=\s*{})(?![0-9A-Fa-f])'.format(active_hash),
                             flags=re.IGNORECASE)
        ini.content, sub_count = pattern.subn(r'\1hash = {}\n; \2'.format(self.new_hash), ini.content)

        default_args.hash = self.new_hash

        # `touched` follows the provider file (3.2H): only a real substitution is a change, so a
        # part that is already up to date no longer prints "Updates applied" and no longer makes
        # a backup for a file that ends up byte-identical.
        note = ('+ Updating {} hash(es) to {}'.format(sub_count, self.new_hash) if sub_count else
                '+ hash = {} is already the latest'.format(active_hash))

        return ExecutionResult(
            touched        = sub_count > 0,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (self.new_hash,),
            queue_commands = (
                (log, (note,)),
            )
        )


@dataclass
class comment_sections():

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash

        pattern = get_section_hash_pattern(hash)
        new_ini_content = ''

        prev_j = 0
        commented_count = 0
        section_matches = pattern.finditer(ini.content)
        for section_match in section_matches:
            i, j = section_match.span(1)
            commented_section = '\n'.join(['; ' + line for line in section_match.group(1).splitlines()])
            commented_count  += 1

            new_ini_content += ini.content[prev_j:i] + commented_section
            prev_j = j

        new_ini_content += ini.content[prev_j:]
        
        ini.content = new_ini_content

        # 0 sections commented = nothing changed: no "Updates applied", no backup.
        return ExecutionResult(
            touched        = commented_count > 0,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (log, ('- Commented {} relevant section(s)'.format(commented_count),)),
            )
        )


@dataclass
class comment_commandlists():
    commandlist_title: str

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        pattern = get_section_title_pattern(self.commandlist_title)
        new_ini_content = ''

        prev_j = 0
        commented_count = 0
        commandlist_matches = pattern.finditer(ini.content)
        for commandlist_match in commandlist_matches:
            i, j = commandlist_match.span(1)
            commented_commandlist = '\n'.join(['; ' + line for line in commandlist_match.group(1).splitlines()])
            commented_count  += 1

            new_ini_content += ini.content[prev_j:i] + commented_commandlist
            prev_j = j

        new_ini_content += ini.content[prev_j:]
        
        ini.content = new_ini_content

        # 0 commandlists commented = nothing changed: no "Updates applied", no backup.
        return ExecutionResult(
            touched        = commented_count > 0,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (log, ('- Commented {} relevant commandlist(s)'.format(commented_count),)),
            )
        )


@dataclass(kw_only=True)
class remove_section():
    capture_content : str = None
    capture_position: str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        pattern = get_section_hash_pattern(active_hash)
        section_match = pattern.search(ini.content)
        if not section_match: raise Exception('Bad regex')
        start, end = section_match.span(1)

        if self.capture_content:
            data[self.capture_content] = get_critical_content(section_match.group(1))[0]
        if self.capture_position:
            data[self.capture_position] = str(start)

        ini.content = ini.content[:start] + ini.content[end:]

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class remove_indexed_sections():
    capture_content         : str = None
    capture_indexed_content : str = None
    capture_position        : str = None

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        data = default_args.data
        
        pattern = get_section_hash_pattern(hash)
        new_ini_content = ''   # ini with ib sections removed
        position        = -1   # First Occurence Deletion Start Position
        prev_end         = 0
        removed_count    = 0   # 0 = nothing matched, so nothing may claim a change

        section_matches = pattern.finditer(ini.content)
        for section_match in section_matches:
            if re.search(r'\n\s*match_first_index\s*=', section_match.group(1), flags=re.IGNORECASE):
                if self.capture_indexed_content:
                    critical_content, _, match_first_index = get_critical_content(section_match.group(1))
                    placeholder = '{}{}{}'.format(self.capture_indexed_content, match_first_index, self.capture_indexed_content)
                    data[placeholder] = critical_content
            else:
                if self.capture_content:
                    critical_content = get_critical_content(section_match.group(1))[0]
                    placeholder = self.capture_content
                    data[placeholder] = critical_content

            start, end = section_match.span()
            if position == -1:
                position = start

            new_ini_content += ini.content[prev_end:start]
            prev_end = end
            removed_count += 1

        new_ini_content += ini.content[prev_end:]
        ini.content = new_ini_content

        if self.capture_position:
            # Never -1: `create_new_section` inserts with content[:pos] + new + content[pos:],
            # so -1 would drop the new section INSIDE the last line of the file (proven by the
            # no-trailing-newline fixture).  With no matching section the new content simply
            # belongs at the end of the file.
            data[self.capture_position] = str(position if position >= 0 else len(ini.content))

        return ExecutionResult(
            touched        = removed_count > 0,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class capture_section():
    capture_content  : str = None
    capture_position : str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        pattern = get_section_hash_pattern(active_hash)
        section_match = pattern.search(ini.content)
        if not section_match: raise Exception('Bad regex')
        _, end = section_match.span(1)

        if self.capture_content:
            data[self.capture_content] = get_critical_content(section_match.group(1))[0]
        if self.capture_position:
            data[self.capture_position] = str(end + 1)

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class create_new_section():
    section_content  : str
    saved_position   : str = None
    capture_position : str = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        data        = default_args.data

        pos = -1
        if self.saved_position and self.saved_position in data:
            pos = int(data[self.saved_position])

        for placeholder, value in data.items():
            if placeholder.startswith('_'):
                continue
            self.section_content = self.section_content.replace(placeholder, value)

        for emoji in ['🍰', '🌲', '🤍']:
            if emoji in self.section_content:
                print('Section substitution failed')
                print(self.section_content)
                return ExecutionResult(
                    touched        = False,
                    failed         = True,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = None
                )
  
        if self.capture_position:
            data[self.capture_position] = str(len(self.section_content) + pos)

        ini.content = ini.content[:pos] + self.section_content + ini.content[pos:]

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = None
        )


@dataclass(kw_only=True)
class transfer_indexed_sections():
    # The field must stay `src_indices`: execute() reads self.src_indices and every
    # caller (Grace.py, Lucy.py) passes src_indices=... .  Any other name makes those
    # modules raise TypeError, which aborts the whole mod file (found 13 Oct 2026).
    trg_indices: tuple[str] = None
    src_indices: tuple[str] = None
    # A module writes ONE index map and hands the same dict to this command and to the
    # attached `check_indexed_sections` (see `register_index_checks`): the transfer ignores
    # these two, the check repairs a stale `match_index_count` with them.  Without the
    # fields here the shared map would raise TypeError.
    trg_counts : tuple[str] = None
    fix        : bool = False

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        # The local name deliberately shadows the builtin `hash`: every expression
        # below needs default_args.hash.  Referring to the builtin by accident built
        # a pattern that matched nothing, so the command returned as a silent no-op
        # (also found 13 Oct 2026).
        hash = default_args.hash
        data = default_args.data

        title = None
        p = get_section_hash_pattern(hash)
        ib_matches = p.findall(ini.content)
        indexed_ib_count = 0
        current_indices = set()
        for m in ib_matches:
            first = re.search(r'\n\s*match_first_index\s*=\s*([0-9]+)', m)
            if first:
                indexed_ib_count += 1
                current_indices.add(first.group(1))
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-1]
            else:
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-2]

        if indexed_ib_count == 0:
            return ExecutionResult()

        # A hash that did NOT change (Orphie 2.2 -> 3.3) is visited on every pass, so the
        # transfer must recognise the state it already produced: without this the second
        # pass captured nothing, `remove_indexed_sections` deleted every section and
        # `create_new_section` then failed on the leftover `\U0001f90d<index>\U0001f90d`
        # placeholder, leaving the file with the deletion.
        src_needed = {str(index) for index in self.src_indices if str(index) != '-1'}
        trg_needed = {str(index) for index in self.trg_indices if str(index) != '-1'}
        if current_indices == trg_needed:
            return ExecutionResult()

        # Every source index is copied into the rebuilt section, so a source that is already
        # gone cannot be captured again: refuse instead of deleting sections whose
        # placeholder would then stay unresolved, and stop the chain visibly.
        missing = src_needed - current_indices
        if missing:
            print('Indexed transfer refused: source indices {} are missing, so the '
                  'sections cannot be rebuilt.'.format(', '.join(sorted(missing))))
            return ExecutionResult(failed=True)

        unindexed_ib_content = '\n'.join([
            f'[TextureOverride{title}IB]',
            f'hash = {hash}',
            '🍰',
            '',
            ''
        ])

        alpha = [
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
        content = ''
        for i, (trg_index, src_index) in enumerate(zip(self.trg_indices, self.src_indices)):
            content += '\n'.join([
                f'[TextureOverride{title}{alpha[i]}]',
                f'hash = {hash}',
                f'match_first_index = {trg_index}',
                f'🤍{src_index}🤍' if src_index != '-1' else 'ib = null',
                '',
                ''
            ])

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = (
                (remove_indexed_sections, {'capture_content': '🍰', 'capture_indexed_content': '🤍', 'capture_position': '🌲'}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': content}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': unindexed_ib_content}),
            ) if indexed_ib_count < len(ib_matches) else (
                (remove_indexed_sections, {'capture_indexed_content': '🤍', 'capture_position': '🌲'}),
                (create_new_section,      {'saved_position': '🌲', 'section_content': content}),
            ),
        )


def indexed_segments(indices, counts):
    """`[(start, count|None)]` for an index map, deriving missing counts.

    `counts` may list only the last segment: every other count is the difference
    to the next segment start (the same rule the transfer entry relies on).  A
    count is left as None when it cannot be derived, so callers never invent one.
    """
    starts = [str(i) for i in (indices or ())]
    given  = [str(c) for c in (counts or ())]
    out = []
    for pos, start in enumerate(starts):
        count = given[pos] if pos < len(given) and given[pos] not in ('', 'None') else None
        out.append((start, count))
    for pos in range(len(out) - 1):
        start, count = out[pos]
        nxt = out[pos + 1][0]
        if count is None and start.lstrip('-').isdigit() and nxt.lstrip('-').isdigit():
            out[pos] = (start, str(int(nxt) - int(start)))
    return out


@dataclass()
class check_indexed_sections():
    r"""Consistency self-check for indexed sections that already carry the NEW hash.

    `update_hash` entries are keyed by the OLD hash, so once a file was processed
    by an older build and already carries the new hash, those entries never run
    again: a stale `match_index_count`, a duplicate section, or an index that
    disappeared from the new segmentation can no longer be noticed.  This command
    is attached to the NEW hash (see `register_index_checks`) and re-checks the
    indexed sections against the same index map as the transfer.

    Report-only by default: it prints one line per problem and writes NOTHING.
    `fix=True` rewrites stale `match_index_count` values and comments out
    sections whose index no longer exists.  A missing `ib = null` section is
    only reported - creating it stays the transfer entry's job on purpose, so a
    report-only run can never change the ini.
    """
    src_indices : tuple[str] = None
    src_counts  : tuple[str] = None
    trg_indices : tuple[str] = None
    trg_counts  : tuple[str] = None
    drop_indices: tuple[str] = None
    fix         : bool = False

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash

        expected = {start: count for start, count in
                    indexed_segments(self.trg_indices, self.trg_counts) if count is not None}
        legacy   = {count for _start, count in
                    indexed_segments(self.src_indices, self.src_counts) if count is not None}
        trg_set  = {str(i) for i in (self.trg_indices or ()) if str(i) != '-1'}
        drop_set = {str(i) for i in (self.drop_indices or ())}

        sections = []
        for section in get_section_hash_pattern(hash).finditer(ini.content):
            block = section.group(1)
            first = re.search(r'\nmatch_first_index\s*=\s*([0-9]+)', block)
            if not first:
                continue
            count = re.search(r'\nmatch_index_count\s*=\s*([0-9]+)', block)
            sections.append((section.start(1), section.end(1), block,
                             first.group(1), count.group(1) if count else None))
        if not sections:
            return ExecutionResult()

        notes   = []
        changed = 0
        content = ini.content
        present = set()
        seen    = set()
        # Descending order keeps the earlier match offsets valid while rewriting.
        for start, end, block, index, count in reversed(sections):
            found = re.match(r'\s*\[(?:Texture|Shader)Override([^\]]*)\]', block)
            title = found.group(1) if found else ''
            if index in seen:
                notes.append('! {}: duplicate section for index {}'.format(title, index))
            seen.add(index)
            present.add(index)
            if index in drop_set:
                notes.append('! {}: index {} no longer exists in the new segments '
                             '(section should be commented)'.format(title, index))
                if self.fix:
                    commented = '\n'.join('; ' + line for line in block.splitlines())
                    content = content[:start] + commented + content[end:]
                    changed += 1
                continue
            # A section without `match_index_count` is a valid state (the transfer writes
            # indexed sections without counts); only an existing, wrong value is repaired.
            want = expected.get(index)
            if want is not None and count is not None and count != want:
                why = 'stale legacy count' if count in legacy else 'mismatch'
                notes.append('! {}: match_index_count = {} -> {} ({})'.format(
                    title, count, want, why))
                if self.fix:
                    fixed = re.sub(r'(\nmatch_index_count\s*=\s*)[0-9]+',
                                   r'\g<1>{}'.format(want), block, count=1)
                    content = content[:start] + fixed + content[end:]
                    changed += 1
            elif index not in trg_set:
                notes.append('! {}: index {} is outside the index map '
                             '(left untouched)'.format(title, index))
            # A target segment whose count cannot be derived (the last one) is a
            # valid state: only membership is checked, never an invented count.

        # The sections were visited bottom-up so that the earlier match offsets stay valid
        # while rewriting; put the report back into reading order.
        notes.reverse()

        for src_index, trg_index in zip(self.src_indices or (), self.trg_indices or ()):
            if str(src_index) == '-1' and str(trg_index) != '-1' \
                    and str(trg_index) not in present:
                notes.append('! missing section for index {} (ib = null)'.format(trg_index))

        if changed:
            ini.content = content

        return ExecutionResult(
            touched        = changed > 0,
            failed         = False,
            signal_break   = False,
            queue_hashes   = None,
            queue_commands = tuple((log, (note,)) for note in notes),
        )


def register_index_checks(commands_table):
    r"""Attach `check_indexed_sections` to the NEW hash of every indexed transfer.

    The check is derived from the very same index map, so a module declares its
    segmentation once.  Report-only is the default; a module opts into the repair
    by declaring `'fix': True` in that same index map (the gate proves the report
    first, so the repair is a deliberate decision per module).
    """
    added = 0
    for key, commands in list(commands_table.items()):
        index_map = next((command[1] for command in commands
                          if command[0] is transfer_indexed_sections
                          and isinstance(command[1], dict)), None)
        if not index_map:
            continue
        # The check belongs on the hash the sections end up carrying: the NEW hash when the
        # entry renames the part, otherwise the very same key (a hash that did not change
        # still has its sections rebuilt on every pass, stale `match_index_count` included).
        rename = next((command[1] for command in commands if command[0] is update_hash), None)
        new_hash = key if rename is None else (
            rename['new_hash'] if isinstance(rename, dict) else (
                rename[0] if isinstance(rename, (tuple, list)) else rename))
        target = commands_table.setdefault(new_hash, [])
        if any(item[0] is check_indexed_sections for item in target):
            continue
        # Only the fields this command declares: a module may grow extra keys in its
        # transfer entry, and passing one through would raise TypeError at run time.
        # `fix` stays report-only by default (see check_indexed_sections).
        target.append((check_indexed_sections, {
            field: index_map[field] for field in (
                'src_indices', 'src_counts', 'trg_indices', 'trg_counts', 'drop_indices', 'fix')
            if field in index_map}))
        added += 1
    return added


@dataclass()
class multiply_section_if_missing():
    equiv_hashes: tuple[str] | str
    extra_title : tuple[str]

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        if (type(self.equiv_hashes) is not tuple):
            self.equiv_hashes = (self.equiv_hashes,)
        for equiv_hash in self.equiv_hashes:
            if ini.has_hash(equiv_hash) or ini.has_hash_in_section(equiv_hash, self.extra_title):
                return ExecutionResult(
                    touched        = False,
                    failed         = False,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = (
                        (log, ('/ Skipping Section Multiplication',  f'{equiv_hash}', f'[...{self.extra_title}]',)),
                    ),
                )
        equiv_hash = self.equiv_hashes[0]

        content = '\n'.join([
            '',
            f'[TextureOverride{self.extra_title}]',
            f'hash = {equiv_hash}',
            '🍰',
            '',
        ])

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (equiv_hash,),
            queue_commands = (
                (log,                ('+ Multiplying Section', f'{equiv_hash}', f'[...{self.extra_title}]')),
                (capture_section,    {'capture_content': '🍰', 'capture_position': '🌲'}),
                (create_new_section, {'saved_position': '🌲', 'section_content': content}),
            ),
        )


@dataclass()
class add_ib_check_if_missing():

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        
        pattern         = get_section_hash_pattern(hash)
        
        section_matches = list(pattern.finditer(ini.content))

        needs_check       = False
        new_sections      = ''
        
        injected_commands = []

        # --- PRE-SCAN TO DETECT GLOBAL HASH THEME ---
        global_inject_command = r"CommandListSkinTexture" # Default to legacy method
        for m in section_matches:
            st = m.group(1)
            # Check if ZZMI footprint is found anywhere in this Hash group
            if re.search(r'\n\s*Resource\\ZZMI\\[a-zA-Z]+\s*=\s*ref', st, flags=re.IGNORECASE) or \
               re.search(r'\n\s*run\s*=\s*CommandList\\ZZMI', st, flags=re.IGNORECASE):
                global_inject_command = r"CommandList\ZZMI\SetTextures"
                break
            # Check if RabbitFX footprint is found anywhere in this Hash group
            elif re.search(r'\n\s*(?:\$|Resource)\\RabbitFX\\[a-zA-Z]+\s*=', st, flags=re.IGNORECASE) or \
                 re.search(r'\n\s*run\s*=\s*CommandList\\RabbitFX', st, flags=re.IGNORECASE):
                global_inject_command = r"CommandList\RabbitFX\SetTextures"
                break

        for section_match in section_matches:
            section_text = section_match.group(1)
            
            has_any_command = re.search(r'\n\s*run\s*=\s*(?:CommandList|CustomShader)', section_text, flags=re.IGNORECASE)
            has_old = re.search(r'\n\s*run\s*=\s*CommandListSkinTexture', section_text, flags=re.IGNORECASE)
            has_zzmi = re.search(r'\n\s*run\s*=\s*CommandList\\ZZMI\\SetTextures', section_text, flags=re.IGNORECASE)
            has_rabbitfx = re.search(r'\n\s*run\s*=\s*CommandList\\RabbitFX', section_text, flags=re.IGNORECASE)

            is_commented_any_commands = re.search(r'\n\s*;\s*run\s*=\s*(?:CommandList|CustomShader)', section_text, flags=re.IGNORECASE)
            is_commented_old = re.search(r'\n\s*;\s*run\s*=\s*CommandListSkinTexture', section_text, flags=re.IGNORECASE)
            is_commented_zzmi = re.search(r'\n\s*;\s*run\s*=\s*CommandList\\ZZMI\\SetTextures', section_text, flags=re.IGNORECASE)
            is_commented_rabbit = re.search(r'\n\s*;\s*run\s*=\s*CommandList\\RabbitFX', section_text, flags=re.IGNORECASE)
            
            is_disabled_by_if = re.search(r'if\s+0\s*==\s*1\s*\n\s*run\s*=', section_text, flags=re.IGNORECASE)
            
            if has_any_command or has_old or has_zzmi or has_rabbitfx or is_commented_any_commands or is_commented_old or is_commented_zzmi or is_commented_rabbit or is_disabled_by_if:
                new_sections += section_match.group()
                continue

            if not re.search(r'\n\s*match_first_index\s*=', section_text, flags=re.IGNORECASE):
                new_sections += section_match.group()
                continue

            needs_check = True
            
            command_to_inject = global_inject_command
            
            if command_to_inject not in injected_commands:
                injected_commands.append(command_to_inject)

            new_sections += re.sub(
                r'\n\s*match_first_index\s*=.*?\n',
                lambda m: f"{m.group(0)}run = {command_to_inject}\n",
                section_match.group(),
                flags=re.IGNORECASE, count=1
            )

        log_messages = []
        if needs_check:
            for cmd in injected_commands:
                log_messages.append((log, (f'+ Adding `run = {cmd}` to indexed mesh',)))
            
            return ExecutionResult(
                touched        = False,
                failed         = False,
                signal_break   = False,
                queue_hashes   = None,
                queue_commands = tuple(log_messages) + (
                    (remove_indexed_sections, {'capture_position': '🌲'}),
                    (create_new_section,      {'saved_position': '🌲', 'section_content': new_sections}),
                )
            )
        else:
            return ExecutionResult(
                touched        = False,
                failed         = False,
                signal_break   = False,
                queue_hashes   = None,
                queue_commands = (
                    (log, ('/ Skipping CommandList Addition',)),
                ),
            )


@dataclass
class add_section_if_missing():
    equiv_hashes    : tuple[str] | str
    section_title   : str = None
    section_content : str = field(default='')

    def execute(self, default_args: DefaultArgs):
        ini = default_args.ini

        if (type(self.equiv_hashes) is not tuple):
            self.equiv_hashes = (self.equiv_hashes,)
        for equiv_hash in self.equiv_hashes:
            if ini.has_hash(equiv_hash) or ini.has_hash_in_section(equiv_hash, self.section_title):
                return ExecutionResult(
                    touched        = False,
                    failed         = False,
                    signal_break   = False,
                    queue_hashes   = None,
                    queue_commands = (
                        (log, ('/ Skipping Section Addition', equiv_hash, f'[...{self.section_title}]',)),
                    ),
                )
        equiv_hash = self.equiv_hashes[0]

        section = '\n[TextureOverride{}]\n'.format(self.section_title)
        section += 'hash = {}\n'.format(equiv_hash)
        section += self.section_content

        return ExecutionResult(
            touched        = False,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (equiv_hash,),
            queue_commands = (
                (log,                ('+ Adding Section', equiv_hash, f'[...{self.section_title}]',)),
                (capture_section,    {'capture_position': '🌲'}),
                (create_new_section, {'saved_position': '🌲', 'section_content': section}),
            ),
        )


BLEND_STRIDE = 32   # blend buffer layout: 4 weights (4f) + 4 indices (4I)


def blend_vertex_count(ini, blend_hash, buffer_filepath):
    r"""Vertex count of the same mesh, read from its Blend buffer (`32 bytes/vertex`).

    A texcoord buffer whose length is a multiple of BOTH strides (36 and 48) cannot
    be told apart by size alone.  The Blend buffer of the same mesh never changes
    length here (only its indices are remapped), so its vertex count settles it.
    `blend_hash` is the Blend section's own hash and finds the buffer regardless of
    the file name; without it the name is derived from the texcoord buffer name.

    Returns `(vertex_count, source)` or `(None, reason)`; a caller must touch nothing
    when no count can be established.
    """
    path = None
    source = None

    if blend_hash:
        section = get_section_hash_pattern(blend_hash).search(ini.content)
        if section:
            for resource in process_commandlist(ini.content, section.group(1), 'vb2'):
                match = get_section_title_pattern(resource).search(ini.content)
                if not match:
                    continue
                found = re.search(r'^\s*filename\s*=\s*(.*)\s*$', match.group(1),
                                  flags=re.IGNORECASE | re.MULTILINE)
                if not found:
                    continue
                candidate = Path(Path(ini.filepath).parent/found.group(1).strip())
                if candidate.exists():
                    path, source = candidate, 'Blend hash {}'.format(blend_hash)
                    break

    if path is None:
        candidate = Path(re.sub(r'texcoord', 'Blend', str(buffer_filepath), count=1,
                                flags=re.IGNORECASE))
        if candidate != buffer_filepath and candidate.exists():
            path, source = candidate, 'the Blend buffer of the same name'

    if path is None:
        return None, 'no Blend buffer of this mesh was found'
    try:
        size = path.stat().st_size
    except OSError as error:
        return None, 'Blend buffer {} is unreadable ({})'.format(path.name, error)
    if size <= 0 or size % BLEND_STRIDE != 0:
        return None, 'Blend buffer {} ({} bytes) is not a multiple of the {} byte stride'.format(
            path.name, size, BLEND_STRIDE)
    return size // BLEND_STRIDE, source


@dataclass
class zzz_13_remap_texcoord():
    id: str
    old_format: tuple[str]
    new_format: tuple[str]
    # Optional: the hash of this mesh's Blend section.  It is only consulted when a
    # buffer's length fits BOTH strides (see `blend_vertex_count`); without it the
    # Blend buffer is looked up by file name, and a buffer that stays undecidable is
    # left untouched.
    blend_hash: str = None

    def execute(self, default_args: DefaultArgs):
        # GUARD-FACE32: decide first, write later. Every decision is based on
        # FILE STATE (buffer size + the ;stride marker we wrote ourselves),
        # never on an in-memory global dedup set that is lost when the tool is
        # run again. Without the guard, a second run corrupts the buffer.
        ini  = default_args.ini
        hash = default_args.hash
        tabs = default_args.tabs

        if (len(self.old_format) != len(self.new_format)): raise Exception()
        old_stride = struct.calcsize('<' + ''.join(self.old_format))
        new_stride = struct.calcsize('<' + ''.join(self.new_format))

        offset = 0
        offsets = [0]
        for format_chunk in self.old_format:
            offset += struct.calcsize(f'<{format_chunk}')
            offsets.append(offset)

        pattern = get_section_hash_pattern(hash)
        section_match = pattern.search(ini.content)
        if not section_match:
            print('{}Skipping texcoord remap {}: no [Texture|Shader]Override section with this hash'.format('\t'*tabs, hash))
            return ExecutionResult(touched=False)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb1')

        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        marker_pattern = re.compile(r'^\s*;\s*stride\s*=\s*(\d+)\s*$', flags=re.IGNORECASE)

        # 1) collect candidates -- not a single byte has been modified yet
        candidates = []
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match:
                continue

            declared_stride = None
            buffer_filename = None
            marker_stride = None
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if line_match:
                    if line_match.group(1).lower() == 'filename':
                        if buffer_filename is None:
                            buffer_filename = line_match.group(2)
                    else:
                        try:
                            declared_stride = int(line_match.group(2))
                        except ValueError:
                            declared_stride = None
                    continue
                marker_match = marker_pattern.match(line)
                if marker_match:
                    marker_stride = int(marker_match.group(1))
            candidates.append((resource, resource_section_match, declared_stride,
                             buffer_filename, marker_stride))

        # 2) decide per buffer (guard based on file state)
        plan = []
        for resource, resource_section_match, declared_stride, buffer_filename, marker_stride in candidates:
            if not buffer_filename:
                print('{}Skipping {}: resource section has no filename line'.format('\t'*tabs, resource))
                continue
            if declared_stride is None:
                print('{}Skipping {}: resource section has no stride line'.format('\t'*tabs, resource))
                continue

            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())
            if buffer_dict_key in ini.modified_buffers:
                buffer = ini.modified_buffers[buffer_dict_key]
            elif buffer_filepath.exists():
                buffer = buffer_filepath.read_bytes()
            else:
                print('{}Skipping {}: buffer {} not found'.format('\t'*tabs, resource, buffer_filename))
                continue

            if marker_stride is not None and declared_stride == new_stride:
                print('{}Skipping {}: already converted (stride = {} + ;stride marker = {})'.format('\t'*tabs, resource, new_stride, marker_stride))
                continue
            if len(buffer) % old_stride != 0:
                print('{}Skipping {}: buffer of {} bytes is not a multiple of the old stride {} (not the legacy format, or already 48)'.format('\t'*tabs, resource, len(buffer), old_stride))
                continue
            if len(buffer) % new_stride == 0:
                # Both strides divide the buffer, so its length alone cannot tell the two
                # formats apart.  The Blend buffer of the same mesh can: it keeps its 32
                # byte stride, so its vertex count times a stride must equal this length.
                vertex_count, source = blend_vertex_count(ini, self.blend_hash, buffer_filepath)
                if vertex_count and vertex_count * new_stride == len(buffer):
                    print('{}Skipping {}: already converted ({} vertices x {} bytes, from {})'.format(
                        '\t'*tabs, resource, vertex_count, new_stride, source))
                    continue
                if not (vertex_count and vertex_count * old_stride == len(buffer)):
                    why = source if vertex_count is None else \
                        'those vertices ({}) fit neither stride'.format(vertex_count)
                    print('{}Skipping {}: buffer of {} bytes is ambiguous (fits both the old stride {} '
                          'and the new stride {}) and {}'.format(
                              '\t'*tabs, resource, len(buffer), old_stride, new_stride, why))
                    continue
                print('{}[V] {}: ambiguous size confirmed as the legacy format by {} '
                      '({} vertices x {} bytes)'.format(
                          '\t'*tabs, resource, source, vertex_count, old_stride))
            if declared_stride != old_stride:
                print('{}[X] WARNING [{}]! Expected buffer stride {} but got {} instead. Overriding and continuing.'.format('\t'*tabs, resource, old_stride, declared_stride))
            plan.append((resource, resource_section_match, buffer_dict_key, buffer_filename))

        if not plan:
            return ExecutionResult(touched=False)

        # 3) only now are they modified; from the last span backwards so the other spans stay valid
        for resource, resource_section_match, buffer_dict_key, buffer_filename in sorted(
                plan, key=lambda item: item[1].start(1), reverse=True):
            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if line_match and line_match.group(1).lower() == 'stride':
                    modified_resource_section.append('stride = {}'.format(new_stride))
                    modified_resource_section.append(';'+line)
                else:
                    modified_resource_section.append(line)

            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

        # 4) repack the buffer (vcount uses old_stride -> always integral because of the guard)
        global global_modified_buffers
        for resource, resource_section_match, buffer_dict_key, buffer_filename in plan:
            if buffer_dict_key not in global_modified_buffers:
                global_modified_buffers[buffer_dict_key] = []
            fix_id = f'{self.id}-texcoord_remap'
            if fix_id in global_modified_buffers[buffer_dict_key]: continue
            else: global_modified_buffers[buffer_dict_key].append(fix_id)

            if buffer_dict_key in ini.modified_buffers:
                buffer = ini.modified_buffers[buffer_dict_key]
            else:
                buffer = Path(buffer_dict_key).read_bytes()

            vcount = len(buffer) // old_stride
            new_buffer = bytearray()
            for i in range(vcount):
                for j, (old_chunk, new_chunk) in enumerate(zip(self.old_format, self.new_format)):
                    if offsets[j] < old_stride and offsets[j+1] <= old_stride:
                        if old_chunk != new_chunk:
                            if (j == 0 and old_chunk == '4B' and new_chunk == '4f'):
                                new_buffer.extend(struct.pack('<4f', *[b/255 for b in struct.unpack_from('<4B', buffer, i*old_stride + 0)]))
                            elif (j == 0 and old_chunk == '4f' and new_chunk == '4B'):
                                new_buffer.extend(struct.pack('<4B', *[max(0, min(255, int(b * 255))) if b == b else 0 for b in struct.unpack_from('<4f', buffer, i*old_stride + 0)]))
                            else:
                                new_buffer.extend(struct.pack(f'<{new_chunk}', *struct.unpack_from(f'<{old_chunk}', buffer, i*old_stride+offsets[j])))
                        else:
                            new_buffer.extend(buffer[i*old_stride + offsets[j]: i*old_stride + offsets[j+1]])
                    else:
                        new_buffer.extend(struct.pack(f'<{new_chunk}', *([0] * int(new_chunk[0]))))

            ini.modified_buffers[buffer_dict_key] = new_buffer

        # Every `plan` entry rewrote its resource section above, so a non-empty plan IS a change
        # (an empty plan returned earlier).
        return ExecutionResult(
            touched=bool(plan)
        )

@dataclass
class zzz_12_shrink_texcoord_color():
    id: str

    def execute(self, default_args: DefaultArgs):
        # GUARD (Fase 4): the texcoord colour buffer shrinks by 12 bytes per vertex
        # (4f -> 4B).  Every decision below is taken from FILE STATE - our ledger, our own
        # `;stride` marker, the buffer size and the stride the .ini declares - and nothing is
        # written before all decisions are in.  Without the guard a second pass (for example
        # after the user restored the .ini from a backup) shrank the buffer AGAIN, corrupting
        # it, while an ini that was already updated kept a stale `stride` line forever.
        ini  = default_args.ini
        hash = default_args.hash
        tabs = default_args.tabs

        pattern = get_section_hash_pattern(hash)
        section_match = pattern.search(ini.content)
        if not section_match:
            print('{}Skipping texcoord colour shrink: no [Texture|Shader]Override section with this hash'.format('\t'*tabs))
            return ExecutionResult(touched=False)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb1')

        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)

        # 1) collect candidates and decide per buffer -- not a single byte has been modified yet
        decisions  = {}          # buffer_dict_key -> (verdict, new_stride, declared, name, bytes)
        candidates = []          # (resource, section_match, declared_stride, buffer_dict_key)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match:
                continue

            declared_stride = None
            buffer_filename = None
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    continue
                if line_match.group(1).lower() == 'filename':
                    if buffer_filename is None:
                        buffer_filename = line_match.group(2)
                else:
                    try:
                        declared_stride = int(line_match.group(2))
                    except ValueError:
                        declared_stride = None

            if not buffer_filename:
                print('{}Skipping {}: resource section has no filename line'.format('\t'*tabs, resource))
                continue
            if declared_stride is None or declared_stride <= 12:
                print('{}Skipping {}: resource section has no usable stride line'.format('\t'*tabs, resource))
                continue

            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in decisions:
                if buffer_dict_key in ini.modified_buffers:
                    buffer = ini.modified_buffers[buffer_dict_key]
                elif buffer_filepath.exists():
                    buffer = buffer_filepath.read_bytes()
                else:
                    print('{}Skipping {}: buffer {} not found'.format('\t'*tabs, resource, buffer_filename))
                    continue

                verdict, new_stride = buffer_state(
                    declared_stride, len(buffer),
                    read_stride_marker(resource_section_match.group(1)),
                    recorded_buffer(buffer_filepath, buffer, 'zzz_12_shrink:'))
                if verdict == 'uncertain':
                    print('{}[X] WARNING [{}]! {} bytes do not fit the stride {} this section declares '
                          '(converted buffers are {} bytes/vertex), so nothing was written for it.'
                          .format('\t'*tabs, resource, len(buffer), declared_stride, new_stride))
                    continue
                decisions[buffer_dict_key] = (verdict, new_stride, declared_stride,
                                              buffer_filename, buffer)

            verdict, new_stride, _declared, buffer_filename, _buffer = decisions[buffer_dict_key]
            candidates.append((resource, resource_section_match, declared_stride, buffer_dict_key))

        if not candidates:
            return ExecutionResult(touched=False)

        # 2) only now do we write: the stride line, and for legacy buffers the repacked bytes.
        # `changed` stays False when every candidate was already converted, so a no-op pass is
        # not reported as an update (and makes no backup).
        changed = False
        for resource, resource_section_match, declared_stride, buffer_dict_key in sorted(
                candidates, key=lambda item: item[1].start(1), reverse=True):
            verdict, new_stride, _declared, buffer_filename, _buffer = decisions[buffer_dict_key]
            if declared_stride == new_stride:
                print('{}Skipping {}: already converted (stride = {})'.format('\t'*tabs, resource, new_stride))
                continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if line_match and line_match.group(1).lower() == 'stride':
                    modified_resource_section.append('stride = {}'.format(new_stride))
                    if verdict == 'legacy':
                        modified_resource_section.append(';'+line)
                else:
                    modified_resource_section.append(line)

            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

            changed = True
            if verdict == 'legacy':
                print('{}Shrinking texcoord colour buffer {}: stride {} -> {}'.format(
                    '\t'*tabs, buffer_filename, declared_stride, new_stride))
            else:
                print('{}Fixing stale stride of {}: {} -> {} (buffer already converted, bytes left alone)'
                      .format('\t'*tabs, buffer_filename, declared_stride, new_stride))

        # 3) repack every legacy buffer exactly once (the in-process set is a second net only)
        global global_modified_buffers
        for buffer_dict_key, (verdict, new_stride, declared, buffer_name, buffer) in decisions.items():
            if verdict != 'legacy':
                continue
            fix_id = f'{self.id}-zzz_12_shrink_texcoord_color'
            if buffer_dict_key not in global_modified_buffers:
                global_modified_buffers[buffer_dict_key] = []
            if fix_id in global_modified_buffers[buffer_dict_key]:
                print('{}Skipping {}: already repacked in this run'.format('\t'*tabs, buffer_name))
                continue
            global_modified_buffers[buffer_dict_key].append(fix_id)

            vcount = len(buffer) // declared
            new_buffer = bytearray()
            for i in range(vcount):
                new_buffer.extend(struct.pack(
                        '<4B',
                        *[
                            max(0, min(255, int(f * 255))) if f == f else 0
                            for f in struct.unpack_from('<4f', buffer, i*declared + 0)
                        ]
                    ))
                new_buffer.extend(buffer[i*declared + 16: i*declared + declared])

            ini.modified_buffers[buffer_dict_key] = new_buffer
            record_buffer(Path(buffer_dict_key), 'zzz_12_shrink:{}'.format(new_stride),
                        new_buffer, new_stride)
            changed = True

        return ExecutionResult(
            touched=changed
        )

@dataclass
class update_buffer_blend_indices():
    hash       : str
    old_indices: tuple[int]
    new_indices: tuple[int]

    def execute(self, default_args: DefaultArgs):
        # GUARD (Fase 4): blend indices may be remapped ONCE - a second pass maps the already
        # mapped values again (34 -> 39 -> 35) and silently breaks the geometry.  There is no
        # size change to look at here, so the guard uses the `;blend_indices` marker we leave in
        # the .ini plus the content ledger, both of which survive a restored .ini and a shared
        # buffer.  Nothing is written before every decision is in.
        ini  = default_args.ini
        tabs = default_args.tabs
        fix_id = blend_fix_id(self.old_indices, self.new_indices)
        blend_stride = 32

        pattern = get_section_hash_pattern(self.hash)
        section_match = pattern.search(ini.content)
        if not section_match:
            print('{}Skipping blend index remap: no [Texture|Shader]Override section with this hash'.format('\t'*tabs))
            return ExecutionResult(touched=False)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb2')

        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)

        # 1) collect candidates and decide per buffer -- nothing has been modified yet
        decisions  = {}          # buffer_dict_key -> (bytes, name, filepath)
        candidates = []          # (resource, section_match, buffer_dict_key)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match:
                continue

            buffer_filename = None
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if line_match and line_match.group(1).lower() == 'filename':
                    if buffer_filename is None:
                        buffer_filename = line_match.group(2)

            if not buffer_filename:
                print('{}Skipping {}: resource section has no filename line'.format('\t'*tabs, resource))
                continue

            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in decisions:
                if buffer_dict_key in ini.modified_buffers:
                    buffer = ini.modified_buffers[buffer_dict_key]
                elif buffer_filepath.exists():
                    buffer = buffer_filepath.read_bytes()
                else:
                    print('{}Skipping {}: buffer {} not found'.format('\t'*tabs, resource, buffer_filename))
                    continue

                if len(buffer) % blend_stride != 0:
                    print('{}[X] WARNING [{}]! buffer {} of {} bytes is not a multiple of the '
                          '{} byte blend stride, so nothing was written for it.'
                          .format('\t'*tabs, resource, buffer_filename, len(buffer), blend_stride))
                    continue
                marker = read_blend_marker(resource_section_match.group(1))
                if marker and marker.lower() == fix_id:
                    print('{}Skipping {}: already remapped by this mapping (marker {})'
                          .format('\t'*tabs, resource, fix_id))
                    continue
                if recorded_buffer(buffer_filepath, buffer, 'blend_remap:'):
                    print('{}Skipping {}: buffer {} already carries the result of a recorded remap'
                          .format('\t'*tabs, resource, buffer_filename))
                    continue
                decisions[buffer_dict_key] = (buffer, buffer_filename, buffer_filepath)

            candidates.append((resource, resource_section_match, buffer_dict_key))

        if not candidates:
            return ExecutionResult(touched=False)

        # 2) only now do we write: the marker in the resource section, then the mapped bytes.
        # `changed` stays False when every candidate was skipped, so a no-op pass is not reported
        # as an update (and makes no backup).
        changed = False
        handled = set()
        for resource, resource_section_match, buffer_dict_key in sorted(
                candidates, key=lambda item: item[1].start(1), reverse=True):
            buffer, buffer_filename, buffer_filepath = decisions[buffer_dict_key]
            if buffer_dict_key in handled:
                print('{}Skipping {}: buffer {} is already handled by another section'
                      .format('\t'*tabs, resource, buffer_filename))
                continue
            handled.add(buffer_dict_key)

            modified_resource_section = list(resource_section_match.group(1).splitlines())
            modified_resource_section.append(';blend_indices = remapped({})'.format(fix_id))
            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

            new_buffer = bytearray()
            vertex_count = len(buffer)//blend_stride
            for i in range(vertex_count):
                blend_weights  = struct.unpack_from('<4f', buffer, i*blend_stride + 0)
                blend_indices  = struct.unpack_from('<4I', buffer, i*blend_stride + 16)

                new_buffer.extend(struct.pack('<4f4I', *blend_weights, *[
                    vgx if vgx not in self.old_indices
                    else self.new_indices[self.old_indices.index(vgx)]
                    for vgx in blend_indices
                ]))

            ini.modified_buffers[buffer_dict_key] = new_buffer
            record_buffer(buffer_filepath, 'blend_remap:' + fix_id, new_buffer, blend_stride)
            changed = True
            print('{}Remapping {} blend indices of {} (mapping {})'.format(
                '\t'*tabs, vertex_count, buffer_filename, fix_id))

        return ExecutionResult(
            touched=changed
        )

# MARK: Character Data Loader
def load_character_modules():
    """
    Dynamically loads all character modules from PlayerCharacterPYData folder.
    Returns merged hash_commands dictionary.
    """
    import importlib
    import sys
    from pathlib import Path
    
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS) / 'Assets'
    else:
        base_path = Path(__file__).parent / 'Assets'
    
    character_data_path = base_path / 'PlayerCharacterPYData'
    
    command_classes = {
        'log': log,
        'update_hash': update_hash,
        'comment_sections': comment_sections,
        'comment_commandlists': comment_commandlists,
        'remove_section': remove_section,
        'remove_indexed_sections': remove_indexed_sections,
        'capture_section': capture_section,
        'create_new_section': create_new_section,
        'transfer_indexed_sections': transfer_indexed_sections,
        'multiply_section_if_missing': multiply_section_if_missing,
        'add_ib_check_if_missing': add_ib_check_if_missing,
        'add_section_if_missing': add_section_if_missing,
        'zzz_13_remap_texcoord': zzz_13_remap_texcoord,
        'zzz_12_shrink_texcoord_color': zzz_12_shrink_texcoord_color,
        'update_buffer_blend_indices': update_buffer_blend_indices,
        'skip_unfixable_update': skip_unfixable_update,
        'check_indexed_sections': check_indexed_sections,
    }
    
    merged_commands = {}
    
    sys.path.insert(0, str(character_data_path.parent))
    
    try:
        character_files = [f for f in character_data_path.glob('*.py') 
                          if f.name != '__init__.py']
        
        print(f'Loading {len(character_files)} character modules...')
        
        for char_file in sorted(character_files):
            char_name = char_file.stem
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{char_name}')
                
                if hasattr(module, 'get_hash_commands'):
                    char_commands = module.get_hash_commands(**command_classes)
                    
                    collisions = set(merged_commands.keys()) & set(char_commands.keys())
                    if collisions:
                        print(f'  Warning: {char_name} has hash collisions: {collisions}')
                    
                    merged_commands.update(char_commands)
                    print(f'  [V] Loaded {char_name}: {len(char_commands)} hashes')
                else:
                    print(f'  [X] Skipped {char_name}: missing get_hash_commands()')
                    
            except Exception as e:
                print(f'  [X] Failed to load {char_name}: {e}')
        
        checks = register_index_checks(merged_commands)
        if checks:
            print(f'[V] Indexed section checks attached: {checks}')

        print(f'Total hashes loaded: {len(merged_commands)}\n')
        
    finally:
        sys.path.remove(str(character_data_path.parent))
    
    return merged_commands


try:
    hash_commands = load_character_modules()
except Exception as e:
    print(f'\nFATAL ERROR: Failed to load character modules!')
    print(f'Error: {e}')
    print('\nAll character data must be loaded from individual module files.')
    print('Please ensure the Assets/PlayerCharacterPYData directory exists and contains valid character modules.')
    print(traceback.format_exc())
    input('\nPress "Enter" to quit...\n')
    raise SystemExit(1)


# MARK: Regex
@functools.lru_cache(maxsize=None)
def get_section_hash_pattern(hash) -> re.Pattern:
    # `re.escape` keeps a hash/title that contains regex metacharacters from being read as a
    # pattern: an unescaped `CommandList\RabbitFX\...` raised `re.error: bad escape \R` and
    # aborted the whole file, while `\Z` in `CommandList\ZZMI\...` silently matched nothing.
    # `str()` keeps the old behaviour for a non-string argument (the pattern simply never
    # matches) instead of turning it into a TypeError that aborts the whole file.
    return re.compile(
        r'''
            ^(
                [ \t]*?\[(?:Texture|Shader)Override.*\][ \t]*
                (?:\n
                    (?![ \t]*?(?:\[|hash\s*=))
                    .*$
                )*?
                (?:\n\s*hash\s*=\s*{}[ \t]*)
                (?:
                    (?:\n(?![ \t]*?\[).*$)*
                    (?:\n[\t ]*?[\$\w].*$)
                )?
            )\s*
        '''.format(re.escape(str(hash))),
        flags=re.VERBOSE|re.IGNORECASE|re.MULTILINE
    )


@functools.lru_cache(maxsize=None)
def get_section_title_pattern(title) -> re.Pattern:
    # Section titles are literal text (`CommandList\ZZMI\SetTextures`, `Belle.Hair.IB`),
    # never patterns: see AIWorks/_audit_engine/fase_1_census_judul.txt. `str()` for the same
    # reason as in `get_section_hash_pattern`.
    return re.compile(
        r'''
            ^(
                [ \t]*?\[{}\]
                (?:
                    (?:\n(?![ \t]*?\[).*$)*
                    (?:\n[\t ]*?[\$\w].*$)
                )?
            )\s*
        '''.format(re.escape(str(title))),
        flags=re.VERBOSE|re.IGNORECASE|re.MULTILINE
    )

# MARK: RUN
if __name__ == '__main__':
    try: main()
    except Exception as x:
        print('\nError Occurred: {}\n'.format(x))
        print(traceback.format_exc())
    finally:
        input('\nPress "Enter" to quit...\n')