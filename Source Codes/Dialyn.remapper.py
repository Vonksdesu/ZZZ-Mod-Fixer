#!/usr/bin/env python3
"""
Dialyn Blend Remapper
Translated from Dialyn.remapper.cs by Satan1c
https://github.com/Satan1c/ZZMI_tools/releases/tag/2.5

Remaps blend bone indices for Dialyn character mods to match
the updated 3D model structure in ZZZ 3.0+.
"""
import os
import re
import time
import struct
import shutil
from pathlib import Path

# ============================================================================
# Remapping dictionaries derived from Dialyn.remapper.cs
# ============================================================================

# Main blend mapping for hash 3d7e53cf
# Format: old_index -> new_index
BLEND_MAPPING = {
    18: 20, 19: 18, 20: 19,
    54: 62, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59, 61: 60, 62: 61,
    69: 71, 70: 72, 71: 70, 72: 69,
    91: 98, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97,
    113: 114, 114: 113,
    128: 129, 129: 128, 130: 132, 131: 130, 132: 131,
    188: 189, 189: 188,
}

# Position hash to blend hash mapping
POSITION_TO_BLEND = {
    "ff36809b": "3d7e53cf",
}

# Stride size (32 bytes per vertex)
STRIDE = 32

# Compiled regex patterns
HASH_REGEX = re.compile(r'^hash\s*=\s*([a-f0-9]{8})\s*$', re.IGNORECASE | re.MULTILINE)
BLEND_RESOURCE_REGEX = re.compile(r'^vb2\s*=\s*Resource([a-zA-Z0-9_]+)\s*$', re.IGNORECASE | re.MULTILINE)
RESOURCE_SECTION_REGEX = re.compile(
    r'^\[Resource([a-zA-Z0-9_]+)\]\s*\n'
    r'type\s*=\s*Buffer\s*\n'
    r'stride\s*=\s*32\s*\n'
    r'filename\s*=\s*(.+)$',
    re.IGNORECASE | re.MULTILINE
)

VALID_BLEND_HASHES = {'3d7e53cf'}

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
    Only processes hashes that are in BLEND_MAPPING or POSITION_TO_BLEND.
    """
    resource_names_map = {}
    
    i = 0
    while i < len(separate_lines):
        line = separate_lines[i]
        if line.startswith('['):
            i += 1
            continue
            
        hash_match = HASH_REGEX.match(line)
        if hash_match:
            raw_hash = hash_match.group(1).lower()
            target_hash = raw_hash
            
            # Map position hashes to blend hashes if necessary
            if target_hash not in VALID_BLEND_HASHES:
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
                    
                res_match = BLEND_RESOURCE_REGEX.match(next_line)
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


def get_resource_files(names_map, ini_content_cleaned, ini_dir):
    """
    Finds exact .buf filenames corresponding to the matched VB2 resources.
    """
    resource_files_map = {}
    
    for target_hash, names in names_map.items():
        files_list = []
        for name, filename in RESOURCE_SECTION_REGEX.findall(ini_content_cleaned):
            if name in names:
                resolved_path = Path(ini_dir) / filename.strip()
                if resolved_path.exists():
                    files_list.append(resolved_path)
        if files_list:
            resource_files_map[target_hash] = files_list
            
    return resource_files_map


def broad_scan_vb2_resources(separate_lines, ini_content_cleaned):
    """
    Fallback scanner: finds ALL vb2 resources bound to stride-32 buffers,
    regardless of whether their hashes are recognized.
    Returns resource_names_map keyed by 'broad_scan'.
    """
    resource_names_map = {}
    
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
    
    seen = set()
    unique_vb2 = []
    for name in all_vb2_resources:
        if name not in seen:
            seen.add(name)
            unique_vb2.append(name)
    
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
        if 'broad_scan' not in resource_names_map:
            resource_names_map['broad_scan'] = []
        resource_names_map['broad_scan'].append(res_name)
    
    return resource_names_map


def remap_binary(target_hash, file_path, timestamp):
    """
    Remaps blend indices in the .buf file for Dialyn.
    Creates a backup before modifying.
    """
    try:
        byte_data = file_path.read_bytes()
    except Exception as e:
        print(f"Failed to read {file_path.name}: {e}")
        return

    num_vertices = len(byte_data) // STRIDE
    if num_vertices == 0:
        return
    
    output_bytes = bytearray(len(byte_data))
    mapping = BLEND_MAPPING
    
    for v in range(num_vertices):
        offset = v * STRIDE
        
        # 1. Copy weights unmodified (first 16 bytes = 4 floats)
        output_bytes[offset:offset+16] = byte_data[offset:offset+16]
        
        # 2. Remap indices (next 16 bytes = 4 uint32)
        indices = struct.unpack_from('<4I', byte_data, offset + 16)
        mapped_indices = [mapping.get(idx, idx) for idx in indices]
        output_bytes[offset + 16:offset + 32] = struct.pack('<4I', *mapped_indices)

    # Create backup
    backup_name = f"remap_backup_{file_path.name}_{timestamp}"
    backup_path = file_path.parent / backup_name
    try:
        shutil.copy2(file_path, backup_path)
    except Exception as e:
        print(f"Warning: Failed to create backup of {file_path.name}: {e}")
        
    try:
        file_path.write_bytes(output_bytes)
        print(f"-> Remapped: {file_path.name} (Backed up to: {backup_name})")
    except Exception as e:
        print(f"Error: Failed to write remapped file {file_path.name}: {e}")


def main():
    current_dir = Path.cwd()
    start_time = time.perf_counter()
    
    inis = []
    for root, _, files in os.walk('.'):
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

    resource_names_list = []
    ini_dirs = []
    ini_contents = []
    
    for ini_file in inis:
        try:
            content, separate_lines = clean_and_get_lines(ini_file)
            res_names = get_resource_names(separate_lines)
            
            if not res_names:
                res_names = broad_scan_vb2_resources(separate_lines, content)
            
            resource_names_list.append(res_names)
            ini_dirs.append(ini_file.parent)
            ini_contents.append(content)
        except Exception as e:
            print(f"Failed to process {ini_file.name}: {e}")
            resource_names_list.append({})
            ini_dirs.append(ini_file.parent)
            ini_contents.append("")

    # Get resource files
    resource_files_list = []
    for res_names, ini_dir, content in zip(resource_names_list, ini_dirs, ini_contents):
        try:
            res_files = get_resource_files(res_names, content, ini_dir)
            resource_files_list.append(res_files)
        except Exception as e:
            print(f"Failed to get resource files: {e}")
            resource_files_list.append({})

    timestamp = int(time.time() * 1000)
    files_processed = 0

    for res_files in resource_files_list:
        unique_files = {}
        for target_hash, files in res_files.items():
            for f in files:
                if f not in unique_files:
                    unique_files[f] = target_hash
        
        for f, target_hash in unique_files.items():
            remap_binary(target_hash, f, timestamp)
            files_processed += 1

    elapsed = time.perf_counter() - start_time
    print(f"\nExecution finished. Processed {files_processed} buffer files.")
    print(f"Total time elapsed: {elapsed:.4f} seconds")
    print("\nPress Enter to exit...")
    try:
        input()
    except EOFError:
        pass

if __name__ == '__main__':
    main()