"""
MiyabiDignifiedBlossom Character Hash Commands
ZZZ Mod Fixer v2.8
Game Version: 2.8
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns MiyabiDignifiedBlossom's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'a913e9a9': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fbb18630': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Clothes IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'ecaf558f': [
        (log,                           ('2.8: MiyabiDignifiedBlossom Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === MiyabiDignifiedBlossom Textures (BodyA) ===
'7d420160': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('18299e4d', 'MiyabiDignifiedBlossom.BodyA.Diffuse.2048')),
    ],
'18299e4d': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('7d420160', 'MiyabiDignifiedBlossom.BodyA.Diffuse.1024')),
    ],
'd8ad1898': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6b59bc2d', 'MiyabiDignifiedBlossom.BodyA.LightMap.2048')),
    ],
'6b59bc2d': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d8ad1898', 'MiyabiDignifiedBlossom.BodyA.LightMap.1024')),
    ],
'417337f2': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('93d7173c', 'MiyabiDignifiedBlossom.BodyA.MaterialMap.2048')),
    ],
'93d7173c': [
        (log,                           ('2.8: MiyabiDignifiedBlossom BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('417337f2', 'MiyabiDignifiedBlossom.BodyA.MaterialMap.1024')),
    ],

# === MiyabiDignifiedBlossom Textures (ClothesA) ===
'88e357af': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA Diffuse 1024p Hash',)),
        (update_hash,                        ('7d80f565',)),
    ],
'7d80f565': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('66724f5a', '4e6c90bd'), 'MiyabiDignifiedBlossom.ClothesA.Diffuse.2048')),
    ],
'66724f5a': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA Diffuse 2048p Hash',)),
        (update_hash,                        ('4e6c90bd',)),
    ],
'4e6c90bd': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('88e357af', '7d80f565'), 'MiyabiDignifiedBlossom.ClothesA.Diffuse.1024')),
    ],
'93b264d9': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('7b8eb437', 'MiyabiDignifiedBlossom.ClothesA.LightMap.2048')),
    ],
'7b8eb437': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('93b264d9', 'MiyabiDignifiedBlossom.ClothesA.LightMap.1024')),
    ],
'85aad660': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA MaterialMap 1024p Hash',)),
        (update_hash,                        ('2fbabf2e',)),
    ],
'2fbabf2e': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        (('1e1485e7', '30590865'), 'MiyabiDignifiedBlossom.ClothesA.MaterialMap.2048')),
    ],
'1e1485e7': [
        (log,                           ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA MaterialMap 2048p Hash',)),
        (update_hash,                        ('30590865',)),
    ],
'30590865': [
        (log,                           ('2.8: MiyabiDignifiedBlossom ClothesA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        (('85aad660', '2fbabf2e'), 'MiyabiDignifiedBlossom.ClothesA.MaterialMap.1024')),
    ],
'e49def56': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair VB Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'b8cb383f': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair VB Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'28a01b2c': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair VB Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'012e84e9': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'a6ea6d83': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'd5462e37': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'244eb75a': [(log, ('3.0: MiyabiDignifiedBlossom HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'a4a705f6': [
        (log, ('3.0: MiyabiDignifiedBlossom Body VB Hash',)),
        (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'6567066b': [
        (log, ('3.0: MiyabiDignifiedBlossom Body VB Hash',)),
        (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'01c36f40': [
        (log, ('3.0: MiyabiDignifiedBlossom Body VB Hash',)),
        (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'f2f19cb2': [(log, ('2.8 -> 2.81: MiyabiSkin Body Blend Hash',)),   (update_hash, ('5121459b',)),],
'5121459b': [
        (log, ('3.0: MiyabiDignifiedBlossom Body VB Hash',)),
        (add_section_if_missing, ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
    ],
'c2b0eca3': [
        (log, ('3.0: MiyabiDignifiedBlossom Clothes VB Hash',)),
        (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'6eb82b02': [
        (log, ('3.0: MiyabiDignifiedBlossom Clothes VB Hash',)),
        (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'958db681': [
        (log, ('3.0: MiyabiDignifiedBlossom Clothes VB Hash',)),
        (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'dbd59d30': [(log, ('3.0: MiyabiDignifiedBlossom Face IB Hash',)), (add_ib_check_if_missing,)],
'0dbd45ea': [
        (log, ('3.0: MiyabiDignifiedBlossom Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'37afd6ad': [
        (log, ('3.0: MiyabiDignifiedBlossom Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'7a476f86': [
        (log, ('3.0: MiyabiDignifiedBlossom Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'd7781c46': [
        (log, ('3.0: MiyabiDignifiedBlossom Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'1d487fd5': [
        (log, ('3.0: MiyabiDignifiedBlossom Face TEX Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'0275d39f': [(log, ('3.0: MiyabiDignifiedBlossom Sword IB Hash',)), (add_ib_check_if_missing,)],
'9d6f441f': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'81a99d68': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'aeb95d61': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'8bc72b94': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'e1215530': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'9d2adcc5': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'4659445f': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'562b2030': [(log, ('3.0: MiyabiDignifiedBlossom SwordSheath IB Hash',)), (add_ib_check_if_missing,)],
'e3590e91': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordSheath VB Hash',)),
        (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
    ],
'fc93f762': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordSheath VB Hash',)),
        (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
    ],
'a9ac3439': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordSheath VB Hash',)),
        (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
    ],
'38c91cb1': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordSheath VB Hash',)),
        (add_section_if_missing, ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
    ],
'1a82a439': [(log, ('3.0: MiyabiDignifiedBlossom SwordHandle IB Hash',)), (add_ib_check_if_missing,)],
'5e1e12aa': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordHandle VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'10545b04': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordHandle VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'51af1803': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordHandle VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'c55927b0': [
        (log, ('3.0: MiyabiDignifiedBlossom SwordHandle VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
    ],
'ed6b94f7': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'8b5708f4': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'a84d9003': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair TEX Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
'92599e94': [
        (log, ('3.0: MiyabiDignifiedBlossom Face TEX Hash',)),
        (add_section_if_missing, ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
    ],
'f9ec3ac8': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'0f21a6c9': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'e6eab72f': [
        (log, ('3.0: MiyabiDignifiedBlossom Sword TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
    ],
'467f402c': [
        (log, ('3.0: MiyabiDignifiedBlossom Clothes VB Hash',)),
        (add_section_if_missing, ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
    ],
'd011ed6c': [
        (log, ('3.0: MiyabiDignifiedBlossom Hair VB Hash',)),
        (add_section_if_missing, ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'MiyabiDignifiedBlossom',
    'game_versions': ['2.8', '3.0'],
}

