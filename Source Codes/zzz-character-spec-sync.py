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
    # Menentukan path ke folder karakter dan file zzz-mod-fixer.spec
    base_path = Path('.')
    py_folder = base_path / 'Assets' / 'PlayerCharacterPYData'
    spec_file = base_path / 'zzz-mod-fixer.spec'

    if not py_folder.exists() or not spec_file.exists():
        print(f"{Colors.RED}✖ Error: Folder 'Assets/PlayerCharacterPYData' atau 'zzz-mod-fixer.spec' tidak ditemukan!{Colors.RESET}")
        print("Pastikan Anda menjalankan script ini dari folder utama proyek Anda.")
        return

    # 1. Membaca file Python fisik yang ada di folder (selain __init__.py)
    physical_files = {f.stem for f in py_folder.glob("*.py") if f.name != "__init__.py"}

    # 2. Membaca isi file zzz-mod-fixer.spec dan mengekstrak daftar character_modules
    try:
        content = spec_file.read_text(encoding='utf-8')
    except UnicodeDecodeError:
        content = spec_file.read_text(encoding='gb2312')

    # Mencari blok character_modules = [ ... ]
    spec_match = re.search(r'character_modules\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not spec_match:
        print(f"{Colors.RED}✖ Error: Blok 'character_modules = [...]' tidak ditemukan di dalam zzz-mod-fixer.spec!{Colors.RESET}")
        return

    spec_block = spec_match.group(1)
    # Mengekstrak semua nama modul di dalam tanda kutip di dalam blok tersebut
    raw_registered = re.findall(r"['\"](.*?)['\"]", spec_block)
    
    # Mengambil nama karakternya saja setelah tanda titik (misal 'PlayerCharacterPYData.Alice' -> 'Alice')
    registered_chars = {char.split('.')[-1] for char in raw_registered if char}

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}    ZZZ Mod Fixer - Verifikasi Registrasi Spec{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")
    print(f"Total file fisik (.py) ditemukan       : {Colors.BLUE}{len(physical_files)}{Colors.RESET}")
    print(f"Total karakter terdaftar di Spec       : {Colors.BLUE}{len(registered_chars)}{Colors.RESET}")
    print(f"{Colors.CYAN}--------------------------------------------------{Colors.RESET}")

    # 3. Membandingkan daftar
    missing_in_spec = physical_files - registered_chars
    redundant_in_spec = registered_chars - physical_files

    has_issue = False

    # Deteksi file fisik yang belum tertulis di zzz-mod-fixer.spec
    if missing_in_spec:
        has_issue = True
        print(f"\n{Colors.YELLOW}⚠   [BELUM TERDAFTAR] File fisik ada, tapi belum ditulis di zzz-mod-fixer.spec:{Colors.RESET}")
        for char in sorted(missing_in_spec):
            print(f"   - {Colors.YELLOW}{char}.py (Tambahkan: 'PlayerCharacterPYData.{char}'){Colors.RESET}")

    # Deteksi nama di zzz-mod-fixer.spec yang file fisiknya sudah dihapus/tidak ada
    if redundant_in_spec:
        has_issue = True
        print(f"\n{Colors.RED}✖ [FILE TIDAK ADA] Ditulis di zzz-mod-fixer.spec, tapi file fisiknya tidak ada:{Colors.RESET}")
        for char in sorted(redundant_in_spec):
            print(f"   - {Colors.RED}PlayerCharacterPYData.{char}{Colors.RESET}")

    # Kesimpulan
    if not has_issue:
        print(f"\n{Colors.BOLD}{Colors.GREEN}✓ SINKRONISASI SUKSES!{Colors.RESET}")
        print(f"{Colors.GREEN}Semua file Python fisik telah terdaftar dengan benar di dalam zzz-mod-fixer.spec.{Colors.RESET}")
        print(f"{Colors.GREEN}Tidak ada file yang kurang atau terdaftar secara redundan.{Colors.RESET}")
    else:
        print(f"\n{Colors.BOLD}{Colors.RED}✖ VERIFIKASI GAGAL: Silakan perbaiki ketidakcocokan di atas.{Colors.RESET}")

    print(f"{Colors.BOLD}{Colors.CYAN}=================================================={Colors.RESET}")

if __name__ == '__main__':
    check_spec_registration()