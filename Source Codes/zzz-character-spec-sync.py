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

def check_spec_registration():
    base_path = Path('.')
    py_folder = base_path / 'Assets' / 'PlayerCharacterPYData'
    spec_file = base_path / 'zzz-mod-fixer.spec'

    if not py_folder.exists() or not spec_file.exists():
        print(f"{Colors.RED}✖ Error: 'Assets/PlayerCharacterPYData' folder or 'zzz-mod-fixer.spec' not found!{Colors.RESET}")
        print("Ensure you run this script from the root folder of your project.")
        return

    physical_files = {f.stem for f in py_folder.glob("*.py") if f.name != "__init__.py"}

    try:
        content = spec_file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = spec_file.read_text(encoding='gb2312')

    spec_match = re.search(r'character_modules\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not spec_match:
        print(f"{Colors.RED}✖ Error: 'character_modules = [...]' block not found in zzz-mod-fixer.spec!{Colors.RESET}")
        return

    spec_block = spec_match.group(1)
    raw_registered = re.findall(r"['\"](.*?)['\"]", spec_block)
    
    registered_chars = {char.split('.')[-1] for char in raw_registered if char}

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}    ZZZ Mod Fixer - Spec Registration Verification{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"Total physical files (.py) found       : {Colors.BLUE}{len(physical_files)}{Colors.RESET}")
    print(f"Total characters registered in Spec       : {Colors.BLUE}{len(registered_chars)}{Colors.RESET}")
    print(f"{Colors.CYAN}--------------------------------------------------{Colors.RESET}")

    missing_in_spec = physical_files - registered_chars
    redundant_in_spec = registered_chars - physical_files

    has_issue = False

    if missing_in_spec:
        has_issue = True
        print(f"\n{Colors.YELLOW}⚠   [NOT REGISTERED] Physical file exists, but has not been added to zzz-mod-fixer.spec:{Colors.RESET}")
        for char in sorted(missing_in_spec):
            print(f"   - {Colors.YELLOW}{char}.py (Add: 'PlayerCharacterPYData.{char}'){Colors.RESET}")

    if redundant_in_spec:
        has_issue = True
        print(f"\n{Colors.RED}✖ [FILE MISSING] Listed in zzz-mod-fixer.spec, but physical file does not exist:{Colors.RESET}")
        for char in sorted(redundant_in_spec):
            print(f"   - {Colors.RED}PlayerCharacterPYData.{char}{Colors.RESET}")

    if not has_issue:
        print(f"\n{Colors.BOLD}{Colors.GREEN}✓ SYNCHRONIZATION SUCCESSFUL!{Colors.RESET}")
        print(f"{Colors.GREEN}All physical Python files are correctly registered in zzz-mod-fixer.spec.{Colors.RESET}")
        print(f"{Colors.GREEN}There are no missing or redundantly registered files.{Colors.RESET}")
    else:
        print(f"\n{Colors.BOLD}{Colors.RED}✖ VERIFICATION FAILED: Please fix the mismatches listed above.{Colors.RESET}")

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")

if __name__ == '__main__':
    check_spec_registration()