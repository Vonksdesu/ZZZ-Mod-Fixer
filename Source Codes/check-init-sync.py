#!/usr/bin/env python3
import re
from pathlib import Path

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def check_registration():
    base_path = Path('.')
    py_folder = base_path / 'Assets' / 'PlayerCharacterPYData'
    init_file = py_folder / '__init__.py'

    if not py_folder.exists() or not init_file.exists():
        print(f"{Colors.RED}✖ Error: Folder 'Assets/PlayerCharacterPYData' or '__init__.py' not found!{Colors.RESET}")
        print("Ensure you run this script from the root folder of your project.")
        return

    physical_files = {f.stem for f in py_folder.glob("*.py") if f.name != "__init__.py"}

    try:
        content = init_file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = init_file.read_text(encoding='gb2312')

    characters_match = re.search(r'CHARACTERS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not characters_match:
        print(f"{Colors.RED}✖ Error: 'CHARACTERS = [...]' block not found in __init__.py!{Colors.RESET}")
        return

    characters_block = characters_match.group(1)
    registered_chars = set(re.findall(r"['\"](.*?)['\"]", characters_block))

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}    ZZZ Mod Fixer - __init__ Registration Verification{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"Total physical files (.py) found       : {Colors.BLUE}{len(physical_files)}{Colors.RESET}")
    print(f"Total characters registered in __init__   : {Colors.BLUE}{len(registered_chars)}{Colors.RESET}")
    print(f"{Colors.CYAN}--------------------------------------------------{Colors.RESET}")

    missing_in_init = physical_files - registered_chars
    redundant_in_init = registered_chars - physical_files

    has_issue = False

    if missing_in_init:
        has_issue = True
        print(f"\n{Colors.YELLOW}⚠   [NOT REGISTERED] Physical file exists, but has not been added to __init__.py:{Colors.RESET}")
        for char in sorted(missing_in_init):
            print(f"   - {Colors.YELLOW}{char}.py{Colors.RESET}")

    if redundant_in_init:
        has_issue = True
        print(f"\n{Colors.RED}✖ [FILE MISSING] Listed in __init__.py, but physical file does not exist:{Colors.RESET}")
        for char in sorted(redundant_in_init):
            print(f"   - {Colors.RED}{char}{Colors.RESET}")

    if not has_issue:
        print(f"\n{Colors.BOLD}{Colors.GREEN}✓ SYNCHRONIZATION SUCCESSFUL!{Colors.RESET}")
        print(f"{Colors.GREEN}All physical Python files are correctly registered in __init__.py.{Colors.RESET}")
        print(f"{Colors.GREEN}There are no missing or redundantly registered files.{Colors.RESET}")
    else:
        print(f"\n{Colors.BOLD}{Colors.RED}✖ VERIFICATION FAILED: Please fix the mismatches listed above.{Colors.RESET}")

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")

if __name__ == '__main__':
    check_registration()