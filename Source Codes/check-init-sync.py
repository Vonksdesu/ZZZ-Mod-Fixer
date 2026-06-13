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
    # Menentukan path ke folder dan file __init__.py
    base_path = Path('.')
    py_folder = base_path / 'Assets' / 'PlayerCharacterPYData'
    init_file = py_folder / '__init__.py'

    if not py_folder.exists() or not init_file.exists():
        print(f"{Colors.RED}✖ Error: Folder 'Assets/PlayerCharacterPYData' atau '__init__.py' tidak ditemukan!{Colors.RESET}")
        print("Pastikan Anda menjalankan script ini dari folder utama proyek Anda.")
        return

    # 1. Membaca file Python fisik yang ada di folder (selain __init__.py)
    physical_files = {f.stem for f in py_folder.glob("*.py") if f.name != "__init__.py"}

    # 2. Membaca isi file __init__.py dan mengekstrak daftar CHARACTERS
    try:
        content = init_file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = init_file.read_text(encoding='gb2312')

    # Mencari blok CHARACTERS = [ ... ]
    characters_match = re.search(r'CHARACTERS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not characters_match:
        print(f"{Colors.RED}✖ Error: Blok 'CHARACTERS = [...]' tidak ditemukan di dalam __init__.py!{Colors.RESET}")
        return

    characters_block = characters_match.group(1)
    # Mengekstrak semua nama karakter di dalam tanda kutip di dalam blok tersebut
    registered_chars = set(re.findall(r"['\"](.*?)['\"]", characters_block))

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}    ZZZ Mod Fixer - Verifikasi Registrasi __init__{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"Total file fisik (.py) ditemukan       : {Colors.BLUE}{len(physical_files)}{Colors.RESET}")
    print(f"Total karakter terdaftar di __init__   : {Colors.BLUE}{len(registered_chars)}{Colors.RESET}")
    print(f"{Colors.CYAN}--------------------------------------------------{Colors.RESET}")

    # 3. Membandingkan daftar
    missing_in_init = physical_files - registered_chars
    redundant_in_init = registered_chars - physical_files

    has_issue = False

    # Deteksi file fisik yang belum tertulis di __init__.py
    if missing_in_init:
        has_issue = True
        print(f"\n{Colors.YELLOW}⚠   [BELUM TERDAFTAR] File fisik ada, tapi belum ditulis di __init__.py:{Colors.RESET}")
        for char in sorted(missing_in_init):
            print(f"   - {Colors.YELLOW}{char}.py{Colors.RESET}")

    # Deteksi nama di __init__.py yang file fisiknya sudah dihapus/tidak ada
    if redundant_in_init:
        has_issue = True
        print(f"\n{Colors.RED}✖ [FILE TIDAK ADA] Ditulis di __init__.py, tapi file fisiknya tidak ada:{Colors.RESET}")
        for char in sorted(redundant_in_init):
            print(f"   - {Colors.RED}{char}{Colors.RESET}")

    # Kesimpulan
    if not has_issue:
        print(f"\n{Colors.BOLD}{Colors.GREEN}✓ SINKRONISASI SUKSES!{Colors.RESET}")
        print(f"{Colors.GREEN}Semua file Python fisik telah terdaftar dengan benar di dalam __init__.py.{Colors.RESET}")
        print(f"{Colors.GREEN}Tidak ada file yang kurang atau terdaftar secara redundan.{Colors.RESET}")
    else:
        print(f"\n{Colors.BOLD}{Colors.RED}✖ VERIFIKASI GAGAL: Silakan perbaiki ketidakcocokan di atas.{Colors.RESET}")

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")

if __name__ == '__main__':
    check_registration()