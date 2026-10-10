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
import struct
import argparse
import traceback
import functools

from dataclasses import dataclass, field
from pathlib import Path

# Extra precaution to not 'fix' 
# the same buffer multiple times
global_modified_buffers: dict[str, list[str]] = {}


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

    return True


# MARK: Ini
class Ini():
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.content  = Path(self.filepath).read_text(encoding='utf-8')
            self.encoding = 'utf-8'
        except UnicodeDecodeError:
            self.content  = Path(self.filepath).read_text(encoding='gb2312')
            self.encoding = 'gb2312'
        

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

        # Get all (uncommented) hashes in the ini
        pattern = re.compile(r'\n\s*hash\s*=\s*([a-f0-9]*)', flags=re.IGNORECASE)
        self._hashes = pattern.findall(self.content)
    
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

            self._done_hashes.add(hash)

        # Auto-detect logic for Jane Doe / Dialyn blend fixes has been moved
        # to the standalone remapper tools to avoid double-remap conflicts.
        # See: Jane.remapper.py / Dialyn.remapper.py

        return self

    def execute(self, commands, default_args):
        for command in commands:
            clss = command[0]
            args = command[1] if len(command) > 1 else {}
            instance = clss(**args) if type(args) is dict else clss(*args) 
            result: ExecutionResult = instance.execute(default_args)

            self._touched = self._touched or result.touched
            if result.failed:
                print()
                return

            if result.queue_hashes:
                # Only add the hashes that I haven't already iterated on
                self._hashes.extend(set(result.queue_hashes).difference(self._done_hashes))

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
                    
                    with open(self.filepath, 'r', encoding=self.encoding) as original_file:
                        original_content = original_file.read()
                    with open(backup_fallback_path, 'w', encoding=self.encoding) as backup_file:
                        backup_file.write(original_content)
                    print(f'Created Backup (Emergency): {backup_fallback_filename} at {backup_fallback_dir}')
                except Exception as ex:
                    print(f"✖ Failed to create emergency backup: {ex}")

            with open(self.filepath, 'w', encoding=self.encoding) as updated_ini:
                updated_ini.write(self.content)

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

            print('Updates applied')
        else:
            print('No changes applied')
        print()

    def has_hash(self, hash):
        return (
            (hash in self._hashes)
            or (hash in self._done_hashes)
        )


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
    line_pattern = re.compile(r'^\s*(run|{})\s*=\s*(.*)\s*$'.format(target), flags=re.IGNORECASE)
    resources = []

    for line in commandlist.splitlines():
        line_match = line_pattern.match(line)
        if not line_match: continue

        if line_match.group(1) == target:
            resources.append(line_match.group(2))

        # Must check the commandlists that are run within the
        # the current commandlist for the resource as well
        elif line_match.group(1) == 'run':
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
class update_hash():
    new_hash: str

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash

        pattern = re.compile(r'(\n\s*)(hash\s*=\s*{})'.format(active_hash), flags=re.IGNORECASE)
        ini.content, sub_count = pattern.subn(r'\1hash = {}\n; \2'.format(self.new_hash), ini.content)

        default_args.hash = self.new_hash

        return ExecutionResult(
            touched        = True,
            failed         = False,
            signal_break   = False,
            queue_hashes   = (self.new_hash,),
            queue_commands = (
                (log, ('+ Updating {} hash(es) to {}'.format(sub_count, self.new_hash),)),
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

        return ExecutionResult(
            touched        = True,
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

        return ExecutionResult(
            touched        = True,
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

        new_ini_content += ini.content[prev_end:]
        ini.content = new_ini_content

        if self.capture_position:
            data[self.capture_position] = str(position)

        return ExecutionResult(
            touched        = True,
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
    trg_indices: tuple[str] = None
    transfer_indexed_sections: tuple[str] = None

    def execute(self, default_args: DefaultArgs):
        ini         = default_args.ini
        active_hash = default_args.hash
        data        = default_args.data

        title = None
        p = get_section_hash_pattern(hash)
        ib_matches = p.findall(ini.content)
        indexed_ib_count = 0
        for m in ib_matches:
            if re.search(r'\n\s*match_first_index\s*=', m):
                indexed_ib_count += 1
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-1]
            else:
                if not title: title = re.match(r'^\[TextureOverride(.*?)\]', m, flags=re.IGNORECASE).group(1)[:-2]

        if indexed_ib_count == 0:
            return ExecutionResult()

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


@dataclass()
class multiply_section_if_missing():
    equiv_hashes: tuple[str] | str
    extra_title : tuple[str]

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        if (type(self.equiv_hashes) is not tuple):
            self.equiv_hashes = (self.equiv_hashes,)
        for equiv_hash in self.equiv_hashes:
            if ini.has_hash(equiv_hash):
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
            if ini.has_hash(equiv_hash):
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


@dataclass
class zzz_13_remap_texcoord():
    id: str
    old_format: tuple[str]
    new_format: tuple[str]

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
                print('{}Skipping {}: buffer of {} bytes is already a multiple of the new stride {} (ambiguous/already converted)'.format('\t'*tabs, resource, len(buffer), new_stride))
                continue
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

        return ExecutionResult(
            touched=True
        )

@dataclass
class zzz_12_shrink_texcoord_color():
    id: str

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini
        hash = default_args.hash
        tabs = default_args.tabs        

        pattern = get_section_hash_pattern(hash)
        section_match = pattern.search(ini.content)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb1')

        buffer_filenames = set()
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match: continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    modified_resource_section.append(line)
                elif line_match.group(1) == 'filename':
                    modified_resource_section.append(line)
                    buffer_filenames.add(line_match.group(2))
                elif line_match.group(1) == 'stride':
                    stride = int(line_match.group(2))
                    modified_resource_section.append('stride = {}'.format(stride - 12))
                    modified_resource_section.append(';'+line)

            modified_resource_section = '\n'.join(modified_resource_section)
            i, j = resource_section_match.span(1)
            ini.content = ini.content[:i] + modified_resource_section + ini.content[j:]

        global global_modified_buffers
        for buffer_filename in buffer_filenames:
            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in global_modified_buffers:
                global_modified_buffers[buffer_dict_key] = []
            fix_id = f'{self.id}-zzz_12_shrink_texcoord_color'
            if fix_id in global_modified_buffers[buffer_dict_key]: continue
            else: global_modified_buffers[buffer_dict_key].append(fix_id)

            if buffer_dict_key not in ini.modified_buffers:
                buffer = buffer_filepath.read_bytes()
            else:
                buffer = ini.modified_buffers[buffer_dict_key]

            vcount = len(buffer) // stride
            new_buffer = bytearray()
            for i in range(vcount):
                new_buffer.extend(struct.pack(
                        '<4B',
                        *[
                            max(0, min(255, int(f * 255))) if f == f else 0
                            for f in struct.unpack_from('<4f', buffer, i*stride + 0)
                        ]
                    ))
                new_buffer.extend(buffer[i*stride + 16: i*stride + stride])
            
            ini.modified_buffers[buffer_dict_key] = new_buffer            

        return ExecutionResult(
            touched=True
        )

@dataclass
class update_buffer_blend_indices():
    hash       : str
    old_indices: tuple[int]
    new_indices: tuple[int]

    def execute(self, default_args: DefaultArgs):
        ini  = default_args.ini

        pattern = get_section_hash_pattern(self.hash)
        section_match = pattern.search(ini.content)
        resources = process_commandlist(ini.content, section_match.group(1), 'vb2')

        buffer_filenames = set()
        line_pattern = re.compile(r'^\s*(filename|stride)\s*=\s*(.*)\s*$', flags=re.IGNORECASE)
        for resource in resources:
            pattern = get_section_title_pattern(resource)
            resource_section_match = pattern.search(ini.content)
            if not resource_section_match: continue

            modified_resource_section = []
            for line in resource_section_match.group(1).splitlines():
                line_match = line_pattern.match(line)
                if not line_match:
                    modified_resource_section.append(line)
                elif line_match.group(1) == 'filename':
                    modified_resource_section.append(line)
                    buffer_filenames.add(line_match.group(2))

        for buffer_filename in buffer_filenames:
            buffer_filepath = Path(Path(ini.filepath).parent/buffer_filename)
            buffer_dict_key = str(buffer_filepath.absolute())

            if buffer_dict_key not in ini.modified_buffers:
                buffer = buffer_filepath.read_bytes()
            else:
                buffer = ini.modified_buffers[buffer_dict_key]
    
            new_buffer = bytearray()
            blend_stride = 32
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

        return ExecutionResult(
            touched=True
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
        '''.format(hash),
        flags=re.VERBOSE|re.IGNORECASE|re.MULTILINE
    )


@functools.lru_cache(maxsize=None)
def get_section_title_pattern(title) -> re.Pattern:
    return re.compile(
        r'''
            ^(
                [ \t]*?\[{}\]
                (?:
                    (?:\n(?![ \t]*?\[).*$)*
                    (?:\n[\t ]*?[\$\w].*$)
                )?
            )\s*
        '''.format(title),
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