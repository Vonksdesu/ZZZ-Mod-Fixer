"""
Zhao Character Hash Commands
ZZZ Mod Fixer v2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Zhao's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ===== IB Hashes (Current v2.5) =====
'2d519056': [(log, ('2.5: Zhao Hair IB Hash',)), (add_ib_check_if_missing,)],
'43c3c5a0': [(log, ('2.5: Zhao Face IB Hash',)), (add_ib_check_if_missing,)],
'6a57d06b': [(log, ('2.5: Zhao Body IB Hash',)), (add_ib_check_if_missing,)],

# ===== Buffer Hashes (Current v2.5) =====
'9bfc82f2': [(log, ('2.5: Zhao Hair Draw Hash',))],
'f86dba12': [(log, ('2.5: Zhao Hair Position Hash',))],
'4b9ea40c': [(log, ('2.5: Zhao Hair Blend Hash',))],
'e1fe5e10': [(log, ('2.5: Zhao Hair Texcoord Hash',))],
'b26f9258': [(log, ('2.5: Zhao Face Draw Hash',))],
'887d011f': [(log, ('2.5: Zhao Face Position Hash',))],
'd3c0fe17': [(log, ('2.5: Zhao Face Blend Hash',))],
'76c4a041': [(log, ('2.5: Zhao Face Texcoord Hash',))],
'a08c7b83': [(log, ('2.5: Zhao Body Draw Hash',))],
'ac4490da': [(log, ('2.5: Zhao Body Position Hash',))],
'06ce2ca1': [(log, ('2.5: Zhao Body Blend Hash',))],
'834b607a': [(log, ('2.5: Zhao Body Texcoord Hash',))],

# ===== Texture Hashes (Current v2.5) =====
'3400d1fc': [
        (log,                           ('2.5: Zhao HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('738b6ad0', 'Zhao.HairA.Diffuse.1024')),
    ],

'738b6ad0': [
        (log,                           ('2.5: Zhao HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3400d1fc', 'Zhao.HairA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Zhao Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
    ],
'4c988418': [
        (log,                           ('2.5: Zhao HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('39dab7f4', 'Zhao.HairA.LightMap.1024')),
    ],

'39dab7f4': [
        (log,                           ('2.5: Zhao HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4c988418', 'Zhao.HairA.LightMap.2048')),
    ],
'bdc3666d': [
        (log,                           ('2.5: Zhao HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('06b8c2ae', 'Zhao.HairA.MaterialMap.1024')),
    ],

'06b8c2ae': [
        (log,                           ('2.5: Zhao HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bdc3666d', 'Zhao.HairA.MaterialMap.2048')),
    ],
'6f06cdfa': [
        (log,                           ('2.5: Zhao FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b9f4efa3', 'Zhao.FaceA.Diffuse.2048')),
    ],

'b9f4efa3': [
        (log,                           ('2.5: Zhao FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6f06cdfa', 'Zhao.FaceA.Diffuse.1024')),
    ],
'e98b7e9e': [
        (log,                           ('2.5: Zhao Shared MaterialMap 2048p Hash (Face/Body)',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('04383cb9', 'Zhao.BodyA.MaterialMap.1024')),
    ],

'04383cb9': [
        (log,                           ('2.5: Zhao Shared MaterialMap 1024p Hash (Face/Body)',)),
        (add_section_if_missing,        ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e98b7e9e', 'Zhao.BodyA.MaterialMap.2048')),
    ],
'77dc1746': [
        (log,                           ('2.5: Zhao BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bebe4176', 'Zhao.BodyA.Diffuse.1024')),
    ],

'bebe4176': [
        (log,                           ('2.5: Zhao BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('77dc1746', 'Zhao.BodyA.Diffuse.2048')),
    ],
'5ed57658': [
        (log,                           ('2.5: Zhao BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('dd6cfe48', 'Zhao.BodyA.LightMap.1024')),
    ],

'dd6cfe48': [
        (log,                           ('2.5: Zhao BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5ed57658', 'Zhao.BodyA.LightMap.2048')),
    ],
'75cf4c8a': [(log, ('3.0: Zhao Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'302715ad': [
        (log, ('3.0: Zhao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9d33a619': [
        (log, ('3.0: Zhao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f4afa896': [
        (log, ('3.0: Zhao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f1c99dcc': [
        (log, ('3.0: Zhao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4141c5ee': [(log, ('3.0: Zhao Knife IB Hash',)), (add_ib_check_if_missing,)],
'fa03bb15': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'c8892598': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'36b0a2b1': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'b61f8d2c': [
        (log, ('3.0: Zhao Knife VB Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'0a4341f5': [
        (log, ('3.0: Zhao Knife VB Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'1acc9c40': [(log, ('3.0: Zhao misc hash',)),],
'798adba3': [
        (log, ('3.0: Zhao Hair TEX Hash',)),
        (add_section_if_missing, ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
    ],
'61730662': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'c3cad120': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'b900c202': [
        (log, ('3.0: Zhao Knife TEX Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
'6caf1e01': [
        (log, ('3.0: Zhao Knife VB Hash',)),
        (add_section_if_missing, ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Zhao',
    'game_versions': ['2.5'],
}
