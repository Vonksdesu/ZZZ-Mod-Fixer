#!/usr/bin/env python3
"""
Jane Doe Blend Remapper
Translated from Jane.remapper.cs by Satan1c
https://github.com/Satan1c/ZZMI_tools/releases/tag/2.5

Remaps blend bone indices for Jane Doe character mods to match
the updated 3D model structure in ZZZ 3.0+.
"""
import os
import re
import time
import struct
import shutil
from pathlib import Path


# Remapping dictionaries derived from Satan1c's C# source
HAIR_MAPPINGS = {
    26: 4, 27: 5, 28: 6, 29: 7, 30: 8, 31: 9, 32: 10, 33: 11, 34: 12, 35: 13,
    36: 14, 37: 15, 38: 16, 39: 17, 40: 19, 41: 20, 42: 18, 43: 22, 44: 23,
    45: 24, 46: 25, 47: 26, 48: 27, 49: 28, 50: 21, 51: 29, 52: 30, 53: 31,
    90: 33, 91: 34, 92: 32, 93: 36, 94: 37, 95: 35, 96: 38, 97: 39, 98: 40,
    99: 41, 100: 42, 101: 44, 102: 45, 103: 46, 104: 48, 105: 47, 106: 43,
    107: 49, 108: 52, 109: 53, 110: 54, 111: 55, 112: 50, 113: 51, 114: 56,
    115: 57, 116: 58, 117: 59, 118: 60, 119: 61, 120: 62, 121: 63, 122: 64,
    123: 65, 124: 66, 125: 67, 126: 68
}

HAND_MAPPINGS = {
    4: 0, 5: 1, 6: 2, 7: 3, 8: 4, 9: 5, 10: 6, 11: 7, 12: 8, 13: 9, 14: 10,
    15: 11, 16: 12, 17: 13, 18: 14, 19: 15, 20: 16, 21: 17, 22: 18, 23: 19,
    24: 20, 25: 21,
    54: 22, 55: 23, 56: 24, 57: 25, 58: 26, 59: 27, 60: 28, 61: 29, 62: 30,
    63: 31, 64: 32, 65: 33, 66: 34, 67: 35, 68: 36, 69: 37, 70: 38, 71: 39,
    72: 40, 73: 41, 74: 42, 75: 43, 76: 44, 77: 45, 78: 46, 79: 47, 80: 48,
    81: 49, 82: 50, 83: 51, 84: 52, 85: 53, 86: 54, 87: 55, 88: 56, 89: 57,
    127: 58, 128: 59, 129: 60
}

POSITION_TO_BLEND = {
    "33a09cfe": "e42171df",
    "82e7c056": "d06a9206"
}

# Stride size (32 bytes per vertex)
STRIDE = 32

def clean_and_get_lines(ini_path):
    """
    Reads the .ini file, removes carriage returns, trims whitespace,
    and ignores empty lines or lines starting with semicolons.
    """
    try:
        content = ini_path.read_text(encoding='utf-8')
    except Exception:
        try:
            content = ini_path.read_text(encoding='gbk', errors='ignore')
        except Exception as e:
            print(f"Failed to read {ini_path.name}: {e}")
            return "", []

    lines_raw = content.replace('\r\n', '\n').split('\n')
    separate_lines = []
    for line in lines_raw:
        trimmed = line.strip()
        if trimmed and not trimmed.startswith(';'):
            separate_lines.append(trimmed)
            
    ini_content_cleaned = "\n".join(separate_lines)
    return ini_content_cleaned, separate_lines

def get_resource_names(separate_lines):
    """
    Parses clean lines to identify targeted hashes and their linked VB2 blend resources.
    Falls back to broad scan if no recognized blend hashes are found.
    """
    resource_names_map = {}
    hash_pattern = re.compile(r'^hash\s*=\s*([a-f0-9]{8})$', re.IGNORECASE)
    blend_res_name_pattern = re.compile(r'^vb2\s*=\s*Resource([a-zA-Z0-9_]+)$', re.IGNORECASE)
    
    i = 0
    while i < len(separate_lines):
        line = separate_lines[i]
        if line.startswith('['):
            i += 1
            continue
            
        hash_match = hash_pattern.match(line)
        if hash_match:
            raw_hash = hash_match.group(1).lower()
            target_hash = raw_hash
            
            # Map position hashes to blend hashes if necessary
            if target_hash not in ('e42171df', 'd06a9206'):
                if target_hash in POSITION_TO_BLEND:
                    target_hash = POSITION_TO_BLEND[target_hash]
                else:
                    i += 1
                    continue
            
            # Scan downwards until we hit another section header to find the vb2 binding
            j = i + 1
            resource_names = []
            while j < len(separate_lines):
                next_line = separate_lines[j]
                if next_line.startswith('['):
                    break
                
                res_match = blend_res_name_pattern.match(next_line)
                if res_match:
                    resource_names.append(res_match.group(1))
                    break  # Found the slot binding, stop searching the block
                j += 1
            
            if resource_names:
                if target_hash not in resource_names_map:
                    resource_names_map[target_hash] = []
                resource_names_map[target_hash].extend(resource_names)
                i = j
            else:
                i += 1
        else:
            i += 1
            
    return resource_names_map


def broad_scan_vb2_resources(separate_lines, ini_content_cleaned):
    """
    Fallback scanner: finds ALL vb2 resources bound to stride-32 buffers,
    regardless of whether their hashes are recognized.
    Returns resource_names_map keyed by heuristic category: 'hair' or 'hand'.
    """
    resource_names_map = {}
    
    # First pass: collect all vb2 bindings from all sections
    vb2_pattern = re.compile(r'^vb2\s*=\s*Resource([a-zA-Z0-9_]+)$', re.IGNORECASE)
    all_vb2_resources = []
    
    i = 0
    while i < len(separate_lines):
        line = separate_lines[i]
        if line.startswith('['):
            i += 1
            continue
        res_match = vb2_pattern.match(line)
        if res_match:
            all_vb2_resources.append(res_match.group(1))
        i += 1
    
    # Deduplicate while preserving order
    seen = set()
    unique_vb2 = []
    for name in all_vb2_resources:
        if name not in seen:
            seen.add(name)
            unique_vb2.append(name)
    
    # Second pass: match against Resource sections with stride = 32
    resource_pattern = re.compile(
        r'^\[Resource([a-zA-Z0-9_]+)\]\s*\n'
        r'type\s*=\s*Buffer\s*\n'
        r'stride\s*=\s*32\s*\n'
        r'filename\s*=\s*(.+)$',
        re.IGNORECASE | re.MULTILINE
    )
    matches = resource_pattern.findall(ini_content_cleaned)
    stride32_names = {name for name, _ in matches}
    
    for res_name in unique_vb2:
        if res_name not in stride32_names:
            continue
        
        # Heuristic categorization by filename
        name_lower = res_name.lower()
        if 'hair' in name_lower or 'head' in name_lower:
            category = 'hair'
        elif 'hand' in name_lower or 'finger' in name_lower or 'accessor' in name_lower or 'knife' in name_lower:
            category = 'hand'
        else:
            category = 'unknown'
        
        if category not in resource_names_map:
            resource_names_map[category] = []
        resource_names_map[category].append(res_name)
    
    return resource_names_map

def get_resource_files(names_map, ini_content_cleaned, ini_dir):
    """
    Finds exact .buf filenames corresponding to the matched VB2 resources.
    Supports both hash-driven keys (e42171df, d06a9206) and broad-scan
    category keys ('hair', 'hand', 'unknown').
    """
    resource_files_map = {}
    resource_pattern = re.compile(
        r'^\[Resource([a-zA-Z0-9_]+)\]\s*\n'
        r'type\s*=\s*Buffer\s*\n'
        r'stride\s*=\s*32\s*\n'
        r'filename\s*=\s*(.+)$',
        re.IGNORECASE | re.MULTILINE
    )
    
    matches = resource_pattern.findall(ini_content_cleaned)
    
    for target_hash, names in names_map.items():
        files_list = []
        for name, filename in matches:
            if name in names:
                resolved_path = Path(ini_dir) / filename.strip()
                if resolved_path.exists():
                    files_list.append(resolved_path)
        if files_list:
            resource_files_map[target_hash] = files_list
            
    return resource_files_map

def remap_binary(target_hash, file_path, timestamp):
    """
    Performs vertex remapping inside the .buf file by modifying weight indices.
    
    target_hash can be:
    - Specific hash: 'e42171df' (hair) or 'd06a9206' (hand)
    - Broad-scan category: 'hair', 'hand', or 'unknown'
    """
    try:
        byte_data = file_path.read_bytes()
    except Exception as e:
        print(f"Failed to read file {file_path.name}: {e}")
        return
        
    num_vertices = len(byte_data) // STRIDE
    if num_vertices == 0:
        return
        
    output_bytes = bytearray(len(byte_data))
    
    # Select mapping based on hash or broad-scan category
    if target_hash == 'e42171df':
        mapping = HAIR_MAPPINGS
    elif target_hash == 'd06a9206':
        mapping = HAND_MAPPINGS
    elif target_hash == 'hair':
        mapping = HAIR_MAPPINGS
    elif target_hash == 'hand':
        mapping = HAND_MAPPINGS
    else:
        # 'unknown' or unrecognized hash: skip to avoid corrupting non-blend buffers
        print(f"  Skipping {file_path.name}: unknown blend category '{target_hash}'")
        return
    
    for x in range(num_vertices):
        group = x * STRIDE
        
        # 1. Copy weights unmodified (first 16 bytes)
        weights = byte_data[group : group + 16]
        
        # 2. Remap indices (next 16 bytes: 4 uint32 integers)
        indices = struct.unpack('<4I', byte_data[group + 16 : group + 32])
        mapped_indices = [mapping.get(idx, idx) for idx in indices]
        mapped_bytes = struct.pack('<4I', *mapped_indices)
        
        # Write packed values into output buffer
        output_bytes[group : group + 16] = weights
        output_bytes[group + 16 : group + 32] = mapped_bytes
        
    # Create backup
    backup_name = f"remap_backup_{timestamp}-{file_path.name}"
    backup_path = file_path.parent / backup_name
    try:
        shutil.copy2(file_path, backup_path)
    except Exception as e:
        print(f"Warning: Failed to create backup of {file_path.name}: {e}")
        
    try:
        file_path.write_bytes(output_bytes)
        print(f"-> Remapped: {file_path.name} (Backed up to: {backup_name})")
    except Exception as e:
        print(f"✖ Error: Failed to write remapped file {file_path.name}: {e}")

def main():
    current_dir = Path.cwd()
    start_time = Stopwatch_GetTimestamp()
    
    inis = []
    for root, dirs, files in os.walk(current_path := str(base_path := Path('.'))):
        for file in files:
            if file.lower().endswith(".ini") and not file.lower().startswith("disabled"):
                inis.append(Path(root) / file)
                
    if not inis:
        print("No .ini files found in current directory and subdirectories.")
        print("Press any key to exit...")
        try:
            input()
        except EOFError:
            pass
        return

    print(f"Found {len(inis)} active .ini files. Analyzing...")

    timestamp = int(System_GetTimestamp())
    files_processed = 0

    for ini_file in inis:
        try:
            content, separate_lines = GetIniLines_py(ini_file)
            names_map = get_resource_names(separate_lines)
            
            # Fallback: if no recognized blend hashes found, broad-scan all vb2 stride-32 buffers
            if not names_map:
                names_map = broad_scan_vb2_resources(separate_lines, content)
            
            if not names_map:
                continue
                
            resource_files = get_resource_files(names_map, content, ini_file.parent)
            
            unique_files = {}
            for target_hash, files in resource_files.items():
                for f in files:
                    if f not in unique_files:
                        unique_files[f] = target_hash
            
            for f, target_hash in unique_files.items():
                remap_binary(target_hash, f, timestamp)
                files_processed += 1
        except Exception as e:
            print(f"Failed to process {ini_file.name}: {e}")

    print(f"\nExecution finished. Processed {files_processed} buffer files.")
    print(f"Total time elapsed: {Stopwatch_GetElapsedTime_py(start_time):.4f} seconds")
    print("\nPress Enter to exit...")
    try:
        input()
    except EOFError:
        pass

# Simulation helpers of C#'s Stopwatch and Timestamp
def Stopwatch_GetTimestamp():
    return time.perf_counter()

def Stopwatch_GetElapsedTime_py(start_time):
    return time.perf_counter() - start_time

def System_GetTimestamp():
    return int(time.time() * 1000)

def GetIniLines_py(file_path):
    return clean_and_get_lines(file_path)

if __name__ == '__main__':
    main()