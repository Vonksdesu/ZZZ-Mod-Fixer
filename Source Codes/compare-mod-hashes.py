#!/usr/bin/env python3
"""
Compare Mod Hashes Script
Compares hashes in a mod .ini file against those defined in ZZZ Mod Fixer character assets.

Usage:
    python compare-mod-hashes.py <path_to_mod.ini>
    python compare-mod-hashes.py <path_to_mod_folder>
"""

import os
import re
import sys
import argparse
import importlib
from pathlib import Path
from collections import defaultdict

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def load_all_character_hashes():
    """
    Load all hashes from character asset modules.
    Returns: dict mapping hash -> list of character names that define it
    """
    # Determine base path
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent / 'Assets'
    
    character_data_path = base_path / 'PlayerCharacterPYData'
    
    if not character_data_path.exists():
        print(f"ERROR: Character data path not found: {character_data_path}")
        return {}
    
    # Mock command classes (we only need the structure, not execution)
    def mock_command(*args, **kwargs):
        pass
    
    command_classes = {
        'log': mock_command,
        'update_hash': mock_command,
        'comment_sections': mock_command,
        'comment_commandlists': mock_command,
        'remove_section': mock_command,
        'remove_indexed_sections': mock_command,
        'capture_section': mock_command,
        'create_new_section': mock_command,
        'transfer_indexed_sections': mock_command,
        'multiply_section_if_missing': mock_command,
        'add_ib_check_if_missing': mock_command,
        'add_section_if_missing': mock_command,
        'zzz_13_remap_texcoord': mock_command,
        'zzz_12_shrink_texcoord_color': mock_command,
        'update_buffer_blend_indices': mock_command,
    }
    
    hash_to_characters = defaultdict(list)
    
    # Add to Python path
    sys.path.insert(0, str(character_data_path.parent))
    
    try:
        character_files = [f for f in character_data_path.glob('*.py') 
                        if f.name != '__init__.py']
        
        print(f"{Colors.BOLD}{Colors.CYAN}Loading character hash data from {len(character_files)} modules...{Colors.RESET}\n")
        
        for char_file in sorted(character_files):
            char_name = char_file.stem
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{char_name}')
                
                if hasattr(module, 'get_hash_commands'):
                    # Get the hash commands (which are really just hash definitions)
                    char_commands = module.get_hash_commands(**command_classes)
                    
                    # Store each hash with the character name
                    for hash_value in char_commands.keys():
                        hash_to_characters[hash_value.lower()].append(char_name)
                    
                    print(f"{Colors.GREEN}✓ Loaded {char_name}:{Colors.RESET} {len(char_commands)} {Colors.GREEN}hashes{Colors.RESET}")
                    
            except Exception as e:
                print(f"{Colors.RED}✖ Failed to load {char_name}: {e}{Colors.RESET}")
        
        print(f"\n{Colors.CYAN}Total unique hashes loaded:{Colors.RESET} {Colors.YELLOW}{len(hash_to_characters)}{Colors.RESET}")
        
    finally:
        sys.path.remove(str(character_data_path.parent))
    
    return hash_to_characters


def extract_hashes_from_ini(ini_path):
    """
    Extract all hash values from an .ini file.
    Returns: dict mapping hash -> list of line numbers where it appears
    """
    try:
        content = Path(ini_path).read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = Path(ini_path).read_text(encoding='gb2312')
    
    # Find all hash definitions (uncommented only)
    pattern = re.compile(r'^\s*hash\s*=\s*([a-f0-9]+)', flags=re.IGNORECASE | re.MULTILINE)
    
    hash_locations = defaultdict(list)
    for match in pattern.finditer(content):
        hash_value = match.group(1).lower()
        line_num = content[:match.start()].count('\n') + 1
        hash_locations[hash_value].append(line_num)
    
    return hash_locations


def find_ini_files(path):
    """
    Find all .ini files in a directory (recursively) or return single file.
    """
    path = Path(path)
    
    if path.is_file() and path.suffix.lower() == '.ini':
        return [path]
    
    elif path.is_dir():
        ini_files = []
        for root, dirs, files in os.walk(path):
            for filename in files:
                # Skip disabled backups
                if filename.upper().startswith('DISABLED'):
                    continue
                if filename.lower().endswith('.ini'):
                    ini_files.append(Path(root) / filename)
        return ini_files
    
    else:
        return []


def compare_hashes(ini_path, character_hashes):
    """
    Compare hashes from an .ini file against character hash database.
    """
    print(f"\n{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}")
    print(f"Analyzing: {Colors.YELLOW}{ini_path}{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}{'='*80}{Colors.RESET}\n")
    
    mod_hashes = extract_hashes_from_ini(ini_path)
    
    if not mod_hashes:
        print(f"{Colors.YELLOW}⚠ No hashes found in this file\n{Colors.RESET}")
        return
    
    print(f"{Colors.GREEN}Found{Colors.RESET} {len(mod_hashes)} {Colors.GREEN}unique hash(es) in mod file:{Colors.RESET}\n")
    
    found_hashes = []
    missing_hashes = []
    
    for hash_value, line_numbers in sorted(mod_hashes.items()):
        lines_str = ', '.join([f"line {ln}" for ln in line_numbers])
        
        if hash_value in character_hashes:
            characters = ', '.join(character_hashes[hash_value])
            found_hashes.append((hash_value, lines_str, characters))
        else:
            missing_hashes.append((hash_value, lines_str))
    
    # Report found hashes
    if found_hashes:
        print(f"{Colors.BOLD}{Colors.GREEN}✓ FOUND IN CHARACTER ASSETS ({Colors.RESET}{len(found_hashes)} {Colors.BOLD}{Colors.GREEN}hash(es)):{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.GREEN}-{Colors.RESET}" * 80)
        for hash_val, lines, chars in found_hashes:
            print(f"{Colors.YELLOW}  {hash_val}  {Colors.RESET}{Colors.BOLD}{Colors.GREEN}|{Colors.RESET}  {lines:20s}  {Colors.BOLD}{Colors.GREEN}|{Colors.RESET}  Characters: {Colors.YELLOW}{chars}{Colors.RESET}")
        print()
    
    # Report missing hashes
    if missing_hashes:
        print(f"{Colors.BOLD}{Colors.RED}✖ NOT FOUND IN CHARACTER ASSETS ({Colors.RESET}{len(missing_hashes)} {Colors.BOLD}{Colors.RED}hash(es)):{Colors.RESET}")
        print(f"{Colors.BOLD}{Colors.RED}-{Colors.RESET}" * 80)
        for hash_val, lines in missing_hashes:
            print(f"  {Colors.RED}{hash_val}{Colors.RESET}  {Colors.BOLD}{Colors.RED}|{Colors.RESET}  {lines}")
        print()
    
    # Summary
    total = len(mod_hashes)
    found = len(found_hashes)
    missing = len(missing_hashes)
    coverage = (found / total * 100) if total > 0 else 0
    
    print(f"{Colors.BOLD}{Colors.CYAN}SUMMARY:{Colors.RESET}")
    print(f"  {Colors.GREEN}Total hashes:{Colors.RESET} {total}")
    print(f"  {Colors.GREEN}Found:{Colors.RESET} {found} ({coverage:.1f}%)")
    print(f"  {Colors.RED}Missing:{Colors.RESET} {missing} ({100-coverage:.1f}%)")
    print()


def main():
    parser = argparse.ArgumentParser(
        description='Compare mod .ini hashes against ZZZ Mod Fixer character hash database',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compare-mod-hashes.py my_mod.ini
  python compare-mod-hashes.py C:\\Path\\To\\Mods\\Folder
        """
    )
    
    parser.add_argument(
        'path',
        help='Path to mod .ini file or folder containing .ini files'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show verbose output'
    )
    
    args = parser.parse_args()
    
    # Validate path
    if not os.path.exists(args.path):
        print(f"ERROR: Path does not exist: {args.path}")
        return 1
    
    # Load character hash database
    character_hashes = load_all_character_hashes()
    
    if not character_hashes:
        print(f"\n{Colors.RED}ERROR: Failed to load character hash data!{Colors.RESET}")
        print(f"{Colors.YELLOW}Ensure the ZZZ-Mod-Fixer/Assets/PlayerCharacterPYData directory exists.{Colors.RESET}")
        return 1
    
    # Find .ini files to process
    ini_files = find_ini_files(args.path)
    
    if not ini_files:
        print(f"\n{Colors.RED}No .ini files found at:{Colors.RESET} {args.path}")
        return 1
    
    print(f"\n{Colors.GREEN}Found{Colors.RESET} {len(ini_files)} {Colors.GREEN}.ini file(s) to analyze{Colors.RESET}\n")
    
    # Process each file
    for ini_file in ini_files:
        try:
            compare_hashes(ini_file, character_hashes)
        except Exception as e:
            print(f"\n{Colors.RED}✖ Error processing{Colors.RESET} {ini_file}{Colors.RED}:{Colors.RESET} {e}\n")
            if args.verbose:
                import traceback
                traceback.print_exc()
    
    return 0


if __name__ == '__main__':
    try:
        exit_code = main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.YELLOW}Interrupted by user{Colors.RESET}")
        exit_code = 130
    except Exception as e:
        print(f"\n{Colors.RED}FATAL ERROR:{Colors.RESET} {e}")
        import traceback
        traceback.print_exc()
        exit_code = 1
    
    sys.exit(exit_code)
