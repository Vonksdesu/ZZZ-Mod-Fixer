"""
Pulchra Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Pulchra's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'bd385763': [(log, ('2.5: Pulchra Body (Hair) IB Hash',)), (add_ib_check_if_missing,)],
'5b30f4da': [(log, ('2.5: Pulchra Mask IB Hash',)), (add_ib_check_if_missing,)],
'62de5837': [(log, ('2.5: Pulchra Face IB Hash',)), (add_ib_check_if_missing,)],

# === Face Textures ===
'1626aafe': [
        (log,                           ('2.5: Pulchra FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32f923f1', 'Pulchra.FaceA.Diffuse.1024')),
    ],
'32f923f1': [
        (log,                           ('2.5: Pulchra FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1626aafe', 'Pulchra.FaceA.Diffuse.2048')),
    ],

# === Hair Textures (BodyB) ===
'57be79d6': [
        (log,                           ('2.5: Pulchra HairB Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fb0a816a', 'Pulchra.HairB.Diffuse.1024')),
    ],
'fb0a816a': [
        (log,                           ('2.5: Pulchra HairB Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('57be79d6', 'Pulchra.HairB.Diffuse.2048')),
    ],
'12c44063': [
        (log,                           ('2.5: Pulchra HairB LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f475e822', 'Pulchra.HairB.LightMap.1024')),
    ],
'f475e822': [
        (log,                           ('2.5: Pulchra HairB LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('12c44063', 'Pulchra.HairB.LightMap.2048')),
    ],
'a553df20': [
        (log,                           ('2.5: Pulchra HairB MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('64d75415', 'Pulchra.HairB.MaterialMap.1024')),
    ],
'64d75415': [
        (log,                           ('2.5: Pulchra HairB MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a553df20', 'Pulchra.HairB.MaterialMap.2048')),
    ],

# === Body Textures (BodyA) ===
'7fc03353': [
        (log,                           ('2.5: Pulchra BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf7eba0f', 'Pulchra.BodyA.Diffuse.1024')),
    ],
'bf7eba0f': [
        (log,                           ('2.5: Pulchra BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fc03353', 'Pulchra.BodyA.Diffuse.2048')),
    ],
'd8462af0': [
        (log,                           ('2.5: Pulchra BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('47040200', 'Pulchra.BodyA.LightMap.1024')),
    ],
'47040200': [
        (log,                           ('2.5: Pulchra BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d8462af0', 'Pulchra.BodyA.LightMap.2048')),
    ],
'd404b789': [
        (log,                           ('2.5: Pulchra BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a66a11d0', 'Pulchra.BodyA.MaterialMap.1024')),
    ],
'a66a11d0': [
        (log,                           ('2.5: Pulchra BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d404b789', 'Pulchra.BodyA.MaterialMap.2048')),
    ],

# === Mask Textures (MaskA) ===
'46bab365': [
        (log,                           ('2.5: Pulchra MaskA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'03d28ecd': [
        (log,                           ('2.5: Pulchra MaskA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'320a1179': [
        (log,                           ('2.5: Pulchra MaskA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],

# Resolusi tambahan (1024p/2048p)

'820ded20': [(log, ('1.7 -> 2.0: Pulchra MaskA MaterialMap 1024p Hash',)), (update_hash, ('f1ee6734',))],
'f1ee6734': [
        (log,                           ('2.5: Pulchra MaskA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        (('320a1179', '6b141146'), 'Pulchra.MaskA.MaterialMap.2048')),
    ],

'6b141146': [
        (log,                           ('2.5: Pulchra MaskA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        (('820ded20', 'f1ee6734'), 'Pulchra.MaskA.MaterialMap.1024')),
    ],
'243cdff6': [(log, ('3.0: Pulchra Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'096ad3f4': [
        (log, ('3.0: Pulchra Hair Shadow VB Hash',)),
        (add_section_if_missing, ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'3dba047b': [
        (log, ('3.0: Pulchra Hair Shadow VB Hash',)),
        (add_section_if_missing, ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'09fcf321': [
        (log, ('3.0: Pulchra Hair Shadow VB Hash',)),
        (add_section_if_missing, ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'6b643cdd': [
        (log, ('3.0: Pulchra Hair Shadow VB Hash',)),
        (add_section_if_missing, ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'992028e7': [
        (log, ('3.0: Pulchra Mask VB Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'eed9f960': [
        (log, ('3.0: Pulchra Mask VB Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'0e117b28': [
        (log, ('3.0: Pulchra Mask VB Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'0db288cb': [
        (log, ('3.0: Pulchra Mask VB Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Pulchra Mask TEX Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'a74c8d89': [
        (log, ('3.0: Pulchra Body VB Hash',)),
        (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
    ],
'5204f58d': [
        (log, ('3.0: Pulchra Body VB Hash',)),
        (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
    ],
'9381fa0b': [
        (log, ('3.0: Pulchra Body VB Hash',)),
        (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
    ],
'425a7565': [(log, ('3.0: Pulchra Waist supply IB Hash',)), (add_ib_check_if_missing,)],
'ec497419': [
        (log, ('3.0: Pulchra Waist supply VB Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'5391a870': [
        (log, ('3.0: Pulchra Waist supply VB Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'ebd6c100': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'6f17d782': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'b8e1e3f6': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'96cb7dc9': [(log, ('3.0: Pulchra Wrist supply IB Hash',)), (add_ib_check_if_missing,)],
'29a6299d': [
        (log, ('3.0: Pulchra Wrist supply VB Hash',)),
        (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
    ],
'8329562b': [
        (log, ('3.0: Pulchra Wrist supply VB Hash',)),
        (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
    ],
'caa1f21c': [
        (log, ('3.0: Pulchra Wrist supply VB Hash',)),
        (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
    ],
'55119041': [
        (log, ('3.0: Pulchra Wrist supply VB Hash',)),
        (add_section_if_missing, ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
    ],
'ed162c10': [
        (log, ('3.0: Pulchra Face VB Hash',)),
        (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
    ],
'2a29bb4e': [
        (log, ('3.0: Pulchra Face VB Hash',)),
        (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
    ],
'7e443147': [
        (log, ('3.0: Pulchra Face VB Hash',)),
        (add_section_if_missing, ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
    ],
'5b644956': [(log, ('3.0: Pulchra weapon IB Hash',)), (add_ib_check_if_missing,)],
'bfc94dff': [(log, ('3.0: Pulchra weapon IB Hash',)), (add_ib_check_if_missing,)],
'd704bf57': [(log, ('3.0: Pulchra misc hash',)),],
'128c8f2e': [
        (log, ('3.0: Pulchra Mask TEX Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'e522177c': [
        (log, ('3.0: Pulchra Mask TEX Hash',)),
        (add_section_if_missing, ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
    ],
'cae1373a': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'f23d32e1': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],
'9ea60b10': [
        (log, ('3.0: Pulchra Waist supply TEX Hash',)),
        (add_section_if_missing, ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
    ],

'2be39a26': [
        (log, ('3.0: Pulchra Body VB Hash',)),
        (add_section_if_missing, ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pulchra',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

