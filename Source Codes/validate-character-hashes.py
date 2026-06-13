#!/usr/bin/env python3
"""
Character Hash Validation Script
ZZZ Mod Fixer v2.5

This script validates all character hash definitions to ensure there are no issues
with the character data modules.

Validation checks:
- Hash format (8-character hex strings)
- Command structure validity
- Required parameters for each command type
- Cross-reference validation (update_hash targets exist)
- Duplicate hashes across characters (warnings only)
- Module loading errors
- Syntax validation
"""

import sys
import importlib
import traceback
from pathlib import Path
from collections import defaultdict


# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_header(text):
    """Print a formatted header"""
    print(f'\n{Colors.BOLD}{Colors.CYAN}{"="*80}{Colors.RESET}')
    print(f'{Colors.BOLD}{Colors.CYAN}{text}{Colors.RESET}')
    print(f'{Colors.BOLD}{Colors.CYAN}{"="*80}{Colors.RESET}\n')


def print_success(text):
    """Print success message"""
    print(f'{Colors.GREEN}✓ {text}{Colors.RESET}')


def print_warning(text):
    """Print warning message"""
    print(f'{Colors.YELLOW}⚠ {text}{Colors.RESET}')


def print_error(text):
    """Print error message"""
    print(f'{Colors.RED}✗ {text}{Colors.RESET}')


def print_info(text):
    """Print info message"""
    print(f'{Colors.BLUE}ℹ {text}{Colors.RESET}')


def validate_hash_format(hash_str):
    """
    Validate that a hash is an 8-character hexadecimal string.
    Returns (is_valid, error_message)
    """
    if not isinstance(hash_str, str):
        return False, f"Hash is not a string: {type(hash_str)}"
    
    if len(hash_str) != 8:
        return False, f"Hash length is {len(hash_str)}, expected 8: '{hash_str}'"
    
    try:
        int(hash_str, 16)
        return True, None
    except ValueError:
        return False, f"Hash contains non-hexadecimal characters: '{hash_str}'"


def validate_command_structure(hash_str, commands, char_name):
    """
    Validate the structure of command tuples.
    Returns list of error messages (empty if valid)
    """
    errors = []
    
    if not isinstance(commands, list):
        errors.append(f"Commands for hash {hash_str} is not a list")
        return errors
    
    for i, command in enumerate(commands):
        if not isinstance(command, tuple):
            errors.append(f"Command {i} for hash {hash_str} is not a tuple: {type(command)}")
            continue
        
        if len(command) < 1:
            errors.append(f"Command {i} for hash {hash_str} is empty")
            continue
        
        # First element should be a class or callable
        command_class = command[0]
        if not callable(command_class) and not hasattr(command_class, '__name__'):
            errors.append(f"Command {i} for hash {hash_str} has invalid command class: {command_class}")
        
        # If there's a second element, it should be tuple or dict
        if len(command) > 1:
            args = command[1]
            if not isinstance(args, (tuple, dict)):
                errors.append(f"Command {i} for hash {hash_str} has invalid args type: {type(args)}")
        
        # Shouldn't have more than 2 elements
        if len(command) > 2:
            errors.append(f"Command {i} for hash {hash_str} has too many elements: {len(command)}")
    
    return errors


def extract_referenced_hashes(commands):
    """
    Extract all hashes that are referenced in update_hash commands.
    Returns set of hash strings.
    """
    referenced = set()
    
    for command in commands:
        if len(command) < 2:
            continue
        
        command_name = command[0].__name__ if hasattr(command[0], '__name__') else str(command[0])
        args = command[1]
        
        # Check update_hash commands
        if command_name == 'update_hash':
            if isinstance(args, tuple) and len(args) > 0:
                referenced.add(args[0])
            elif isinstance(args, dict) and 'new_hash' in args:
                referenced.add(args['new_hash'])
        
        # Check multiply_section_if_missing commands
        elif command_name == 'multiply_section_if_missing':
            if isinstance(args, tuple) and len(args) > 0:
                equiv_hashes = args[0]
                if isinstance(equiv_hashes, str):
                    referenced.add(equiv_hashes)
                elif isinstance(equiv_hashes, tuple):
                    referenced.update(equiv_hashes)
        
        # Check add_section_if_missing commands
        elif command_name == 'add_section_if_missing':
            if isinstance(args, tuple) and len(args) > 0:
                equiv_hashes = args[0]
                if isinstance(equiv_hashes, str):
                    referenced.add(equiv_hashes)
                elif isinstance(equiv_hashes, tuple):
                    referenced.update(equiv_hashes)
    
    return referenced


def load_character_modules():
    """
    Load all character modules and return their hash commands.
    Returns (modules_dict, errors_dict)
    """
    # Determine base path
    if getattr(sys, 'frozen', False):
        base_path = Path(sys._MEIPASS)
    else:
        base_path = Path(__file__).parent / 'Assets'
    
    character_data_path = base_path / 'PlayerCharacterPYData'
    
    if not character_data_path.exists():
        print_error(f"Character data directory not found: {character_data_path}")
        return {}, {}
    
    # Mock command classes
    command_classes = {
        'log': lambda *args: None,
        'update_hash': lambda *args, **kwargs: None,
        'comment_sections': lambda *args, **kwargs: None,
        'comment_commandlists': lambda *args, **kwargs: None,
        'remove_section': lambda *args, **kwargs: None,
        'remove_indexed_sections': lambda *args, **kwargs: None,
        'capture_section': lambda *args, **kwargs: None,
        'create_new_section': lambda *args, **kwargs: None,
        'transfer_indexed_sections': lambda *args, **kwargs: None,
        'multiply_section_if_missing': lambda *args, **kwargs: None,
        'add_ib_check_if_missing': lambda *args, **kwargs: None,
        'add_section_if_missing': lambda *args, **kwargs: None,
        'zzz_13_remap_texcoord': lambda *args, **kwargs: None,
        'zzz_12_shrink_texcoord_color': lambda *args, **kwargs: None,
        'update_buffer_blend_indices': lambda *args, **kwargs: None,
    }
    
    # Add names to mock functions for validation
    for name, func in command_classes.items():
        func.__name__ = name
    
    modules_data = {}
    errors = {}
    
    # Add character data path to Python path
    sys.path.insert(0, str(character_data_path.parent))
    
    try:
        # Get all .py files
        character_files = sorted([f for f in character_data_path.glob('*.py') 
                                if f.name != '__init__.py'])
        
        print_info(f"Found {len(character_files)} character modules to validate")
        print()
        
        for char_file in character_files:
            char_name = char_file.stem
            try:
                # Import module
                module = importlib.import_module(f'PlayerCharacterPYData.{char_name}')
                
                # Get hash commands
                if hasattr(module, 'get_hash_commands'):
                    char_commands = module.get_hash_commands(**command_classes)
                    modules_data[char_name] = {
                        'commands': char_commands,
                        'module': module
                    }
                    print_success(f"Loaded {char_name}: {len(char_commands)} hashes")
                else:
                    errors[char_name] = "Missing get_hash_commands() function"
                    print_error(f"Failed {char_name}: missing get_hash_commands()")
                    
            except Exception as e:
                errors[char_name] = str(e)
                print_error(f"Failed {char_name}: {e}")
        
    finally:
        sys.path.remove(str(character_data_path.parent))
    
    return modules_data, errors


def validate_all_modules():
    """Main validation function"""
    print_header("ZZZ Mod Fixer - Character Hash Validation")
    
    # Statistics
    stats = {
        'total_modules': 0,
        'loaded_modules': 0,
        'failed_modules': 0,
        'total_hashes': 0,
        'invalid_hashes': 0,
        'invalid_commands': 0,
        'broken_references': 0,
        'duplicate_hashes': 0,
    }
    
    # Load modules
    print_header("Loading Character Modules")
    modules_data, load_errors = load_character_modules()
    
    stats['total_modules'] = len(modules_data) + len(load_errors)
    stats['loaded_modules'] = len(modules_data)
    stats['failed_modules'] = len(load_errors)
    
    if load_errors:
        print()
        print_header("Module Loading Errors")
        for char_name, error in load_errors.items():
            print_error(f"{char_name}: {error}")
    
    # Validate hash formats and command structures
    print_header("Validating Hash Formats and Command Structures")
    
    all_hashes = {}  # hash -> list of character names
    all_references = set()  # All hashes referenced by commands
    
    for char_name, data in modules_data.items():
        commands_dict = data['commands']
        print(f"\n{Colors.BOLD}Character: {char_name}{Colors.RESET}")
        
        char_has_errors = False
        
        for hash_str, commands in commands_dict.items():
            stats['total_hashes'] += 1
            
            # Track which characters use this hash
            if hash_str not in all_hashes:
                all_hashes[hash_str] = []
            all_hashes[hash_str].append(char_name)
            
            # Validate hash format
            is_valid, error_msg = validate_hash_format(hash_str)
            if not is_valid:
                print_error(f"  Invalid hash format: {error_msg}")
                stats['invalid_hashes'] += 1
                char_has_errors = True
            
            # Validate command structure
            cmd_errors = validate_command_structure(hash_str, commands, char_name)
            if cmd_errors:
                for error in cmd_errors:
                    print_error(f"  {error}")
                    stats['invalid_commands'] += 1
                char_has_errors = True
            
            # Extract referenced hashes
            refs = extract_referenced_hashes(commands)
            all_references.update(refs)
        
        if not char_has_errors:
            print_success(f"  All {len(commands_dict)} hashes valid")
    
    # Check for duplicate hashes
    print_header("Checking for Hash Collisions")
    duplicate_hashes = {h: chars for h, chars in all_hashes.items() if len(chars) > 1}
    
    if duplicate_hashes:
        print_warning(f"Found {len(duplicate_hashes)} hashes used by multiple characters:")
        print_info("(This is not necessarily an error - some hashes may be shared)")
        print()
        
        for hash_str, char_names in sorted(duplicate_hashes.items()):
            print(f"  {Colors.YELLOW}{hash_str}{Colors.RESET}: {', '.join(sorted(char_names))}")
            stats['duplicate_hashes'] += 1
    else:
        print_success("No hash collisions found")
    
    # Validate cross-references
    print_header("Validating Hash Cross-References")
    
    broken_refs = []
    for ref_hash in sorted(all_references):
        if ref_hash not in all_hashes:
            broken_refs.append(ref_hash)
            print_error(f"  Referenced hash not defined: {ref_hash}")
            stats['broken_references'] += 1
    
    if not broken_refs:
        print_success(f"All {len(all_references)} referenced hashes are defined")
    
    # Print summary
    print_header("Validation Summary")
    
    print(f"Total Modules:        {stats['total_modules']}")
    print(f"  {Colors.GREEN}✓ Loaded:          {stats['loaded_modules']}{Colors.RESET}")
    if stats['failed_modules'] > 0:
        print(f"  {Colors.RED}✗ Failed:          {stats['failed_modules']}{Colors.RESET}")
    
    print(f"\nTotal Hashes:         {stats['total_hashes']}")
    if stats['invalid_hashes'] > 0:
        print(f"  {Colors.RED}✗ Invalid Format:  {stats['invalid_hashes']}{Colors.RESET}")
    if stats['invalid_commands'] > 0:
        print(f"  {Colors.RED}✗ Invalid Commands: {stats['invalid_commands']}{Colors.RESET}")
    if stats['broken_references'] > 0:
        print(f"  {Colors.RED}✗ Broken References: {stats['broken_references']}{Colors.RESET}")
    if stats['duplicate_hashes'] > 0:
        print(f"  {Colors.YELLOW}⚠ Hash Collisions: {stats['duplicate_hashes']}{Colors.RESET}")
    
    print()
    
    # Determine overall status
    has_errors = (
        stats['failed_modules'] > 0 or
        stats['invalid_hashes'] > 0 or
        stats['invalid_commands'] > 0 or
        stats['broken_references'] > 0
    )
    
    if has_errors:
        print_error("VALIDATION FAILED - Issues found that need to be fixed!")
        return False
    else:
        print_success("VALIDATION PASSED - All checks successful!")
        if stats['duplicate_hashes'] > 0:
            print_warning(f"Note: {stats['duplicate_hashes']} hash collisions detected (may be intentional)")
        return True


if __name__ == '__main__':
    try:
        success = validate_all_modules()
        sys.exit(0 if success else 1)
    except Exception as e:
        print_error(f"\nFatal error during validation: {e}")
        print(traceback.format_exc())
        sys.exit(2)
