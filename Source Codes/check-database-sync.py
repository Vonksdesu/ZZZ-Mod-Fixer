#!/usr/bin/env python3
import os
import re
import json
import importlib
import sys
from pathlib import Path
from collections import Counter

# ==============================================================================
# KONFIGURASI VERSI DATABASE (Ganti bagian ini untuk versi masa depan)
# ==============================================================================
DATABASE_VERSION = "2.8"
# ==============================================================================

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

def parse_json_structure(json_path):
    ib_hashes = set()
    other_hashes = set()
    hex_pattern = re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE)
    
    def walk(d):
        if isinstance(d, dict):
            for k, v in d.items():
                if k.lower() == 'ib' and isinstance(v, str) and hex_pattern.match(v):
                    ib_hashes.add(v.lower())
                elif isinstance(v, str) and hex_pattern.match(v):
                    other_hashes.add(v.lower())
                else:
                    walk(v)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, str) and hex_pattern.match(item):
                    other_hashes.add(item.lower())
                else:
                    walk(item)
                    
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            walk(data)
    except Exception as e:
        print(f"{Colors.RED}Gagal membaca {json_path}: {e}{Colors.RESET}")
    return ib_hashes, other_hashes

def parse_txt_transitions(txt_path):
    transitions = []
    try:
        content = txt_path.read_text(encoding='utf-8')
    except Exception:
        try:
            content = txt_path.read_text(encoding='gb2312')
        except Exception:
            return []
            
    lines = content.splitlines()
    current_char = ""
    for line in lines:
        char_match = re.match(r'^\s*([^,:\s]+)', line)
        if char_match:
            potential_char = char_match.group(1)
            # Menghindari kata kunci penjelas struktural
            if not any(word in potential_char for word in ["以下", "新增", "头发", "NormalMap", "Diffuse", "LightMap", "MaterialMap", "Position", "Texcoord", "Blend"]):
                current_char = potential_char
        
        matches = re.findall(r'([a-f0-9]{8})\s*->\s*([a-f0-9]{8})', line, re.IGNORECASE)
        for old_h, new_h in matches:
            transitions.append({
                'char_hint': current_char,
                'old': old_h.lower(),
                'new': new_h.lower(),
                'line': line.strip()
            })
    return transitions

def build_py_hash_index(py_data_path, mock_command_classes):
    init_file = py_data_path / '__init__.py'
    if not init_file.exists():
        return {}, {}, {}
        
    try:
        content = init_file.read_text(encoding='utf-8')
    except Exception:
        content = init_file.read_text(encoding='gb2312')
        
    characters_match = re.search(r'CHARACTERS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not characters_match:
        return {}, {}, {}
        
    registered_chars = re.findall(r"['\"](.*?)['\"]", characters_match.group(1))
    
    hash_to_module = {}
    module_to_hashes = {}
    module_to_char_info = {}
    
    sys.path.insert(0, str(py_data_path.parent))
    try:
        for character_name in registered_chars:
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                py_commands = module.get_hash_commands(**mock_command_classes)
                py_hashes = {h.lower() for h in py_commands.keys()}
                
                module_to_hashes[character_name] = py_hashes
                for h in py_hashes:
                    if h not in hash_to_module:
                        hash_to_module[h] = []
                    hash_to_module[h].append(character_name)
                    
                # Ekstrak data CHARACTER_INFO jika ada di dalam modul
                char_info = getattr(module, 'CHARACTER_INFO', None)
                if char_info and isinstance(char_info, dict):
                    module_to_char_info[character_name] = char_info
                else:
                    module_to_char_info[character_name] = {}
            except Exception:
                # Saran 1: Tetap daftarkan modul yang bermasalah/kosong sebagai objek kosong agar terdeteksi di Pengecekan 1
                module_to_hashes[character_name] = set()
                module_to_char_info[character_name] = {}
                continue
    finally:
        sys.path.remove(str(py_data_path.parent))
        
    return hash_to_module, module_to_hashes, module_to_char_info

def clean_name(name):
    name_no_ext = Path(name).stem
    # Diperketat: Ambil huruf dan angka Latin (A-Z, a-z, 0-9) guna membedakan berkas seperti Soldier11 dan Soldier0
    latin_and_digits = "".join(re.findall(r'[a-zA-Z0-9]+', name_no_ext))
    # Diperluas: Menambahkan filter untuk 'write', 'ult', dan 'sword' agar YeShunguangUlt, YeShunguangSword, dsb. dapat bersatu di rumpun yang sama
    for stop_word in ['skin', 'summer', 'swimwear', 'temple', 'chandelier', 'campus', 'outfit', 'pose', 'write', 'ult', 'sword']:
        latin_and_digits = re.sub(stop_word, '', latin_and_digits, flags=re.IGNORECASE)
    return latin_and_digits.lower()

def find_associated_modules(json_filename, json_ib_hashes, json_all_hashes, hash_to_module, module_to_hashes):
    associated = set()
    methods = []
    
    # 1. Pencocokan Berdasarkan IB Hash (Akurasi Tertinggi)
    ib_matches = set()
    for h in json_ib_hashes:
        if h in hash_to_module:
            ib_matches.update(hash_to_module[h])
    if ib_matches:
        associated.update(ib_matches)
        methods.append("Jejak IB Hash (Sangat Akurat)")
    
    # 2. Pencocokan Kemiripan Nama File (Pendekatan Utama)
    clean_json = clean_name(json_filename)
    name_matches = set()
    if clean_json:
        for character_name in module_to_hashes.keys():
            clean_mod = clean_name(character_name)
            if clean_json in clean_mod or clean_mod in clean_json:
                name_matches.add(character_name)
    if name_matches:
        associated.update(name_matches)
        methods.append("Kemiripan Nama (Akurat)")
        
    # 3. Pencocokan Berdasarkan Komponen Hash (Hanya jika tahap 1 & 2 kosong, guna mencegah hijack normal-map shared)
    if not associated:
        component_matches = set()
        for h in json_all_hashes:
            if h in hash_to_module:
                # Saran 2: Batasi pencocokan hash komponen standar bersama (misal: normal map umum yang dipakai banyak modul)
                if len(hash_to_module[h]) <= 2:
                    component_matches.update(hash_to_module[h])
        if component_matches:
            associated.update(component_matches)
            methods.append("Jejak Hash Komponen (Akurat)")
            
    # 4. Penyaringan Rumpun Ketat (Strict Family Filter)
    # Jika terdeteksi beberapa file modul, saring secara ketat agar hanya yang serumpun dengan nama file database yang masuk
    if len(associated) > 1 and clean_json:
        strict_associated = set()
        for mod_name in associated:
            clean_mod = clean_name(mod_name)
            # Karakter harus berada dalam satu rumpun penamaan (saling mengandung substring nama)
            if clean_json in clean_mod or clean_mod in clean_json:
                strict_associated.add(mod_name)
        if strict_associated:
            associated = strict_associated
            
    return list(associated), " + ".join(methods) if methods else "Tidak Teridentifikasi"

def check_sync():
    base_path = Path('.')
    py_data_path = base_path / 'Assets' / 'PlayerCharacterPYData'
    json_folder = base_path / 'ZZZHashIDCharactersDatabase' / f'Database_{DATABASE_VERSION}'
    
    if not json_folder.exists():
        print(f"{Colors.RED}✖ Error: Folder database tidak ditemukan di: {json_folder.resolve()}{Colors.RESET}")
        return
        
    # Fungsi Mock yang dinamai sesuai dengan implementasi aslinya
    def log(*args, **kwargs): pass
    def update_hash(*args, **kwargs): pass
    def comment_sections(*args, **kwargs): pass
    def comment_commandlists(*args, **kwargs): pass
    def remove_section(*args, **kwargs): pass
    def remove_indexed_sections(*args, **kwargs): pass
    def capture_section(*args, **kwargs): pass
    def create_new_section(*args, **kwargs): pass
    def transfer_indexed_sections(*args, **kwargs): pass
    def multiply_section_if_missing(*args, **kwargs): pass
    def add_ib_check_if_missing(*args, **kwargs): pass
    def add_section_if_missing(*args, **kwargs): pass
    def zzz_13_remap_texcoord(*args, **kwargs): pass
    def zzz_12_shrink_texcoord_color(*args, **kwargs): pass
    def update_buffer_blend_indices(*args, **kwargs): pass
    
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
        'update_buffer_blend_indices': update_buffer_blend_indices
    }

    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Analisis Sinkronisasi Database {DATABASE_VERSION} (FLEXIBLE){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    
    hash_to_module, module_to_hashes, module_to_char_info = build_py_hash_index(py_data_path, command_classes)
    
    critical_errors = 0
    serious_errors = 0
    missing_hashes_count = 0
    flagged_swapped_modules = set()  # Set pelacak untuk menghindari pencetakan berulang
    
    # --------------------------------------------------------------------------
    # BAGIAN 1: VERIFIKASI FILE .JSON (DATABASE STRUKTUR MODEL)
    # --------------------------------------------------------------------------
    for json_file in sorted(json_folder.glob('*.json')):
        filename = json_file.name
        
        ib_hashes, other_hashes = parse_json_structure(json_file)
        all_json_hashes = ib_hashes | other_hashes
        
        # Deteksi seluruh modul terkait secara otomatis, dinamis, dan fleksibel
        associated_modules, method = find_associated_modules(filename, ib_hashes, all_json_hashes, hash_to_module, module_to_hashes)
        
        # [PENGECEKAN 1]: VERIFIKASI MODUL FISIK ATAU APABILA FILE KOSONG
        is_missing_or_empty = False
        if not associated_modules:
            is_missing_or_empty = True
        else:
            # Periksa apakah total hash yang berhasil diekstrak dari modul kelompok bernilai 0 (kosong)
            total_hashes = sum(len(module_to_hashes.get(mod, set())) for mod in associated_modules)
            if total_hashes == 0:
                is_missing_or_empty = True

        if is_missing_or_empty:
            critical_errors += 1
            print(f"{Colors.RED}[✖ MODUL HILANG ATAU FILE PYTHON KARAKTER KOSONG] File database: '{filename}'{Colors.RESET}")
            print(f"{Colors.YELLOW}                                                     Tidak ada file Python fisik yang cocok atau file Python kosong di proyek Anda!\n{Colors.RESET}")
            continue
            
        # [PENGECEKAN 2]: VERIFIKASI APAKAH ISI FILE TERSEBUT TERTUKAR DENGAN KARAKTER LAIN (KECIL/BESAR DIABAIKAN)
        swapped_modules_in_group = set()
        safe_modules_in_group = []
        
        for mod in associated_modules:
            char_info = module_to_char_info.get(mod, {})
            declared_name = char_info.get('name')
            is_this_swapped = False
            
            if declared_name:
                # Perbandingan case-insensitive antara nama modul fisik dan nama yang tertulis di CHARACTER_INFO
                if mod.lower() != declared_name.lower():
                    is_this_swapped = True
                    swapped_modules_in_group.add(mod)
                    # Cetak dan hitung error hanya jika modul belum pernah ditandai sebelumnya
                    if mod not in flagged_swapped_modules:
                        flagged_swapped_modules.add(mod)
                        serious_errors += 1
                        print(f"{Colors.RED}[✖ ISI HASH FILE KARAKTER INI TERTUKAR DENGAN HASH KARAKTER LAIN] Modul: {mod}.py{Colors.RESET}")
                        print(f"                                                                Nama di file: '{mod}'")
                        print(f"                                                                Nama di CHARACTER_INFO: '{declared_name}'")
                        print(f"{Colors.YELLOW}                                                                Harap perbaiki isi file Python Anda terlebih dahulu!\n{Colors.RESET}")
                    break
            
            # Jika file aman (tidak tertukar), masukkan ke dalam daftar grup aman
            if not is_this_swapped:
                safe_modules_in_group.append(mod)
        
        # Jika semua modul dalam kelompok ternyata tertukar (tidak ada modul aman tersisa),
        # hentikan sisa pengecekan untuk berkas JSON ini.
        if not safe_modules_in_group:
            continue

        # [PENGECEKAN 3]: VERIFIKASI PERBEDAAN HASH (HASH TIDAK SINKRON)
        # Menggabungkan seluruh set hash dari kelompok modul Python terkait yang AMAN saja
        combined_py_hashes = set()
        for mod in safe_modules_in_group:
            if mod in module_to_hashes:
                combined_py_hashes.update(module_to_hashes[mod])
                
        # Validasi strict terhadap gabungan kelompok modul Python yang aman
        missing_hashes = all_json_hashes - combined_py_hashes
        if missing_hashes:
            missing_hashes_count += 1
            modules_display = ", ".join([f"{m}.py" for m in sorted(safe_modules_in_group)])
            
            # Klasifikasi jenis modul: Modul Kelompok jika ada lebih dari 1 file aman, Modul Individu jika hanya ada 1 file aman
            if len(safe_modules_in_group) > 1:
                module_type_label = "Modul Kelompok"
            else:
                module_type_label = "Modul Individu"
                
            print(f"{Colors.RED}[✖ HASH TIDAK SINKRON] {module_type_label}: {modules_display}{Colors.RESET}")
            print(f"                        Cocok dengan: {filename} via {Colors.BLUE}{method}{Colors.RESET}")
            print(f"                        Ditemukan {Colors.YELLOW}{len(missing_hashes)}{Colors.RESET} hash yang absen dari kelompok file Python Anda:")
            for h in sorted(missing_hashes):
                print(f"                        - {Colors.YELLOW}{h}{Colors.RESET}")
            print()
            
    # Saran 3: Dipindahkan ke luar perulangan agar hanya tercetak sekali ketika verifikasi JSON selesai
    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] VERIFIKASI JSON SUKSES: Semua database model .json sinkron dan aman dengan file Python Anda!\n{Colors.RESET}")

    # --------------------------------------------------------------------------
    # BAGIAN 2: VERIFIKASI FILE .TXT (CATATAN TRANSISI PERUBAHAN HASH)
    # --------------------------------------------------------------------------
    print(f"\n{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Analisis Sinkronisasi Catatan Perubahan (.txt){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")
    
    txt_errors = 0
    for txt_file in sorted(json_folder.parent.glob('*.txt')):
        # Lewati file petunjuk atau readme yang bukan merupakan log hash transisi
        if "说明" in txt_file.name or "readme" in txt_file.name.lower():
            continue
            
        transitions = parse_txt_transitions(txt_file)
        if not transitions:
            continue
            
        print(f"\nMenganalisis catatan transisi: {Colors.BLUE}'{txt_file.name}'{Colors.RESET} ({Colors.BOLD}{len(transitions)}{Colors.RESET} transisi ditemukan)")
        
        for trans in transitions:
            old_h = trans['old']
            new_h = trans['new']
            
            # Cari modul Python yang bersangkutan dengan hash tersebut
            target_mods = set()
            if new_h in hash_to_module:
                target_mods.update(hash_to_module[new_h])
            if old_h in hash_to_module:
                target_mods.update(hash_to_module[old_h])
                
            # Fallback ke petunjuk karakter dari teks jika tidak ada modul yang terindeks
            if not target_mods and trans['char_hint']:
                clean_hint = clean_name(trans['char_hint'])
                for character_name in module_to_hashes.keys():
                    clean_mod = clean_name(character_name)
                    if clean_hint in clean_mod or clean_mod in clean_hint:
                        target_mods.add(character_name)
                        
            if not target_mods:
                continue
                
            # Validasi transisi di dalam modul target
            for character_name in target_mods:
                try:
                    sys.path.insert(0, str(py_data_path.parent))
                    module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                    py_commands = module.get_hash_commands(**command_classes)
                    sys.path.remove(str(py_data_path.parent))
                    
                    # Verifikasi apakah old_h terdaftar di dalam Python
                    if old_h not in py_commands:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ TRANSISI ABSEN] Modul: {character_name}.py{Colors.RESET}")
                        print(f"                     Hash lama '{Colors.YELLOW}{old_h}{Colors.RESET}' tidak ditemukan di file Python!")
                        print(f"                     Catatan: {trans['line']}")
                        continue
                        
                    # Verifikasi apakah old_h memiliki fungsi update_hash ke target yang benar (new_h)
                    commands_list = py_commands[old_h]
                    has_update_call = False
                    correct_target = False
                    actual_target = None
                    
                    for cmd in commands_list:
                        if isinstance(cmd, tuple) and len(cmd) >= 1:
                            func = cmd[0]
                            if hasattr(func, '__name__') and func.__name__ == 'update_hash':
                                has_update_call = True
                                if len(cmd) >= 2 and isinstance(cmd[1], tuple) and len(cmd[1]) >= 1:
                                    actual_target = cmd[1][0].lower()
                                    if actual_target == new_h:
                                        correct_target = True
                                        break
                                        
                    if not has_update_call:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ TRANSISI SALAH] Modul: {character_name}.py{Colors.RESET}")
                        print(f"                     Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' terdaftar, tapi tidak memiliki perintah 'update_hash'!")
                        print(f"                     Catatan: {trans['line']}")
                    elif not correct_target:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ TARGET SALAH] Modul: {character_name}.py{Colors.RESET}")
                        print(f"                   Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' meng-update ke '{Colors.RED}{actual_target}{Colors.RESET}',")
                        print(f"                   seharusnya menuju '{Colors.GREEN}{new_h}{Colors.RESET}' sesuai catatan!")
                        print(f"                   Catatan: {trans['line']}")
                        
                except Exception as e:
                    print(f"{Colors.RED}[✖] Gagal menganalisis modul {character_name} untuk transisi: {e}{Colors.RESET}")
                    
    # Mencetak pesan sukses khusus untuk berkas transisi .txt
    if txt_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] VERIFIKASI TXT SUKSES: Semua catatan transisi .txt tervalidasi dengan aman di file Python Anda!\n{Colors.RESET}")

    print(f"\n{Colors.BOLD}{Colors.CYAN}=========================== KESIMPULAN ==========================={Colors.RESET}")
    # Logika diperbarui agar serious_errors ikut menentukan kegagalan sinkronisasi
    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0 and txt_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] SINKRONISASI SUKSES: Seluruh modul Python Anda sinkron sempurna terhadap JSON & log .txt!{Colors.RESET}")
    else:
        print(f"{Colors.BOLD}{Colors.RED}[✖] SINKRONISASI GAGAL:{Colors.RESET}")
        if critical_errors > 0:
            print(f"    - Ditemukan {Colors.RED}{critical_errors}{Colors.RESET} kasus Modul Hilang atau isi file Python Kosong.")
        if serious_errors > 0:
            print(f"    - Ditemukan {Colors.RED}{serious_errors}{Colors.RESET} kasus isi HASH file tertukar dengan HASH file Python karakter lain.")
        if missing_hashes_count > 0:
            print(f"    - Ditemukan {Colors.RED}{missing_hashes_count}{Colors.RESET} kelompok modul Python yang memiliki hash tidak sinkron dengan JSON database.")
        if txt_errors > 0:
            print(f"    - Ditemukan {Colors.RED}{txt_errors}{Colors.RESET} kesalahan sinkronisasi transisi pada log .txt.")
        print(f"\n    {Colors.YELLOW}Silakan perbaiki ketidakcocokan di atas agar sinkronisasi sukses.{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")

if __name__ == '__main__':
    check_sync()