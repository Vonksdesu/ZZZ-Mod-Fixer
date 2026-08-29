"""
WiseOathOfSkies Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseOathOfSkies's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'22fe3236': [
        (log,                           ('3.0: WiseOathOfSkies Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'8d08b190': [
        (log,                           ('3.0: WiseOathOfSkies HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'8a1ec07e': [
        (log,                           ('3.0: WiseOathOfSkies Neck IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'f21a2bac': [
        (log,                           ('3.0: WiseOathOfSkies Tie IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === WiseOathOfSkies Textures (BodyA) ===
'a0a4c84e': [
        (log,                           ('3.0: WiseOathOfSkies BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('b9dcce2e', 'WiseOathOfSkies.BodyA.Diffuse.2048')),
    ],
'b9dcce2e': [
        (log,                           ('3.0: WiseOathOfSkies BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('a0a4c84e', 'WiseOathOfSkies.BodyA.Diffuse.1024')),
    ],
'8d09dc95': [
        (log,                           ('3.0: WiseOathOfSkies BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('bd86c7c4', 'WiseOathOfSkies.BodyA.LightMap.2048')),
    ],
'bd86c7c4': [
        (log,                           ('3.0: WiseOathOfSkies BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('8d09dc95', 'WiseOathOfSkies.BodyA.LightMap.1024')),
    ],
'31707abe': [
        (log,                           ('3.0: WiseOathOfSkies BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('4d7473b1', 'WiseOathOfSkies.BodyA.MaterialMap.2048')),
    ],
'4d7473b1': [
        (log,                           ('3.0: WiseOathOfSkies BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('31707abe', 'WiseOathOfSkies.BodyA.MaterialMap.1024')),
    ],

# === WiseOathOfSkies Textures (TieA) ===
'dd08a467': [
        (log,                           ('3.0: WiseOathOfSkies TieA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('1024352b', 'WiseOathOfSkies.TieA.Diffuse.2048')),
    ],
'1024352b': [
        (log,                           ('3.0: WiseOathOfSkies TieA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('dd08a467', 'WiseOathOfSkies.TieA.Diffuse.1024')),
    ],
'4f211318': [
        (log,                           ('3.0: WiseOathOfSkies TieA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e550cd81', 'WiseOathOfSkies.TieA.LightMap.2048')),
    ],
'e550cd81': [
        (log,                           ('3.0: WiseOathOfSkies TieA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('4f211318', 'WiseOathOfSkies.TieA.LightMap.1024')),
    ],
'ba59a4d0': [
        (log,                           ('3.0: WiseOathOfSkies TieA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6649f407', 'WiseOathOfSkies.TieA.MaterialMap.2048')),
    ],
'6649f407': [
        (log,                           ('3.0: WiseOathOfSkies TieA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ba59a4d0', 'WiseOathOfSkies.TieA.MaterialMap.1024')),
    ],
'd5ca0411': [(log, ('3.0: WiseOathOfSkies Hair IB Hash',)), (add_ib_check_if_missing,)],
'ef9c0510': [
        (log, ('3.0: WiseOathOfSkies Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'e8df7ff3': [
        (log, ('3.0: WiseOathOfSkies Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'774071dd': [
        (log, ('3.0: WiseOathOfSkies Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'68e4f572': [
        (log, ('3.0: WiseOathOfSkies Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'28005a5b': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'4dcfe033': [
        (log, ('3.0: WiseOathOfSkies Body VB Hash',)),
        (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
    ],
'0c2cc3dd': [
        (log, ('3.0: WiseOathOfSkies Body VB Hash',)),
        (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
    ],
'8bab814c': [
        (log, ('3.0: WiseOathOfSkies Body VB Hash',)),
        (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
    ],
'6171b974': [
        (log, ('3.0: WiseOathOfSkies Neck VB Hash',)),
        (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'0da56abf': [
        (log, ('3.0: WiseOathOfSkies Neck VB Hash',)),
        (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'98a06e7d': [
        (log, ('3.0: WiseOathOfSkies Neck VB Hash',)),
        (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'fb0a401a': [
        (log, ('3.0: WiseOathOfSkies Tie VB Hash',)),
        (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'052d4b48': [
        (log, ('3.0: WiseOathOfSkies Tie VB Hash',)),
        (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'4b19b5b5': [
        (log, ('3.0: WiseOathOfSkies Tie VB Hash',)),
        (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'1fdaf388': [(log, ('3.0: WiseOathOfSkies Face IB Hash',)), (add_ib_check_if_missing,)],
'6c4552bb': [
        (log, ('3.0: WiseOathOfSkies Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'5657c1fc': [
        (log, ('3.0: WiseOathOfSkies Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'c83b6cbf': [
        (log, ('3.0: WiseOathOfSkies Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('2b320847',)),
    ],
'2b320847': [
        (log, ('3.1: WiseOathOfSkies Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'015fbf96': [
        (log, ('3.0: WiseOathOfSkies Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'5d75fddc': [
        (log, ('3.0: WiseOathOfSkies Face TEX Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'cb0d0c22': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'33368e12': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'd9383a15': [
        (log, ('3.0: WiseOathOfSkies Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'588d7d2d': [
        (log, ('3.0: WiseOathOfSkies Face TEX Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],
'86f21a82': [
        (log, ('3.0: WiseOathOfSkies Tie VB Hash',)),
        (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
    ],
'c4a1fb46': [
        (log, ('3.0: WiseOathOfSkies Neck VB Hash',)),
        (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
    ],
'164b2ccb': [
        (log, ('3.0: WiseOathOfSkies Body VB Hash',)),
        (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseOathOfSkies',
    'game_versions': ['3.0'],
}
