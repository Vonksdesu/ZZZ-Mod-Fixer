"""
NangongYu Character Hash Commands
ZZZ Mod Fixer v2.7
Game Version: 2.7
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns NangongYu's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'4586e530': [
        (log,                           ('2.7: NangongYu Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd643e19a': [
        (log,                           ('2.7: NangongYu Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'969152d4': [
        (log,                           ('2.7: NangongYu Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === NangongYu Textures (FaceA) ===
'b6e87aef': [
        (log,                           ('2.7: NangongYu FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,    ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1fd77103', 'NangongYu.FaceA.Diffuse.2048')),
    ],
'1fd77103': [
        (log,                           ('2.7: NangongYu FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,    ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b6e87aef', 'NangongYu.FaceA.Diffuse.1024')),
    ],

# === NangongYu Textures (HairA) ===
'd2e23730': [
        (log,                           ('2.7: NangongYu HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('df39b77c', 'NangongYu.HairA.Diffuse.2048')),
    ],
'df39b77c': [
        (log,                           ('2.7: NangongYu HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('d2e23730', 'NangongYu.HairA.Diffuse.1024')),
    ],
'e3573bc8': [
        (log,                           ('2.7: NangongYu HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d94a0c41', 'NangongYu.HairA.LightMap.2048')),
    ],
'd94a0c41': [
        (log,                           ('2.7: NangongYu HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('e3573bc8', 'NangongYu.HairA.LightMap.1024')),
    ],
'687f57b8': [
        (log,                           ('2.7: NangongYu HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('a458a615', 'NangongYu.HairA.MaterialMap.2048')),
    ],
'a458a615': [
        (log,                           ('2.7: NangongYu HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('687f57b8', 'NangongYu.HairA.MaterialMap.1024')),
    ],

# === NangongYu Textures (BodyA) ===
'fe06152c': [
        (log,                           ('2.7 -> 2.8: NangongYu BodyA Diffuse 1024p Hash',)),
        (update_hash,                        ('dc41fbbf',)),
    ],
'dc41fbbf': [
        (log,                           ('2.7: NangongYu BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('2d290490', '11254966'), 'NangongYu.BodyA.Diffuse.2048')),
    ],
'2d290490': [
        (log,                           ('2.7 -> 2.8: NangongYu BodyA Diffuse 2048p Hash',)),
        (update_hash,                        ('11254966',)),
    ],
'11254966': [
        (log,                           ('2.7: NangongYu BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('fe06152c', 'dc41fbbf'), 'NangongYu.BodyA.Diffuse.1024')),
    ],
'ab51539c': [
        (log,                           ('2.7: NangongYu BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('fee3d533', 'NangongYu.BodyA.LightMap.2048')),
    ],
'fee3d533': [
        (log,                           ('2.7: NangongYu BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ab51539c', 'NangongYu.BodyA.LightMap.1024')),
    ],
'958e389e': [
        (log,                           ('2.7: NangongYu BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('beb11b78', 'NangongYu.BodyA.MaterialMap.2048')),
    ],
'beb11b78': [
        (log,                           ('2.7: NangongYu BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('958e389e', 'NangongYu.BodyA.MaterialMap.1024')),
    ],
'd1a15d0e': [
        (log, ('3.0: NangongYu Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'e67f6a3c': [
        (log, ('3.0: NangongYu Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'56699a62': [
        (log, ('3.0: NangongYu Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: NangongYu Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'17438fa9': [(log, ('3.0: NangongYu Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'cd884c0a': [(log, ('3.0: NangongYu Headband IB Hash',)), (add_ib_check_if_missing,)],
'5aac7571': [
        (log, ('3.0: NangongYu Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
    ],
'74cbadea': [
        (log, ('3.0: NangongYu Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
    ],
'00cbd7a8': [
        (log, ('3.0: NangongYu Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
    ],
'82509f4f': [
        (log, ('3.0: NangongYu Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
    ],
'3b4190ce': [(log, ('3.0: NangongYu wing IB Hash',)), (add_ib_check_if_missing,)],
'6ab572d9': [
        (log, ('3.0: NangongYu wing VB Hash',)),
        (add_section_if_missing, ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
    ],
'b90d042a': [
        (log, ('3.0: NangongYu wing VB Hash',)),
        (add_section_if_missing, ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
    ],
'e062b6fc': [
        (log, ('3.0: NangongYu wing VB Hash',)),
        (add_section_if_missing, ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
    ],
'4d677fbd': [
        (log, ('3.0: NangongYu wing VB Hash',)),
        (add_section_if_missing, ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
    ],
'd4908293': [
        (log, ('3.0: NangongYu Body VB Hash',)),
        (add_section_if_missing, ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
    ],
'5ebf2446': [
        (log, ('3.0: NangongYu Body VB Hash',)),
        (add_section_if_missing, ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
    ],
'f43a1dba': [
        (log, ('3.0: NangongYu Body VB Hash',)),
        (add_section_if_missing, ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
    ],
'ba598cf9': [(log, ('3.0: NangongYu Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'ed1df686': [
        (log, ('3.0: NangongYu Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
    ],
'45910aef': [
        (log, ('3.0: NangongYu Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
    ],
'93c1ec0c': [
        (log, ('3.0: NangongYu Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
    ],
'dcd7242e': [(log, ('3.0: NangongYu Weapon IB Hash',)), (add_ib_check_if_missing,)],
'acea6f2f': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'5e50a4f2': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'766f3fca': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: NangongYu Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'fcc325af': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'a64be703': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'd70f65c1': [
        (log, ('3.0: NangongYu Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
    ],
'5b0185fc': [
        (log, ('3.0: NangongYu Body VB Hash',)),
        (add_section_if_missing, ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
    ],
'536345c3': [
        (log, ('3.0: NangongYu Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
    ],
'84246d50': [
        (log, ('3.0: NangongYu Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'8252253e': [
        (log, ('2.8: NangongYu Weapon draw_vb Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'fe68de06': [
        (log, ('2.8: NangongYu Weapon position_vb Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'06639b26': [
        (log, ('2.8: NangongYu Weapon texcoord_vb Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
'4115d67b': [
        (log, ('2.8: NangongYu Weapon blend_vb Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYu',
    'game_versions': ['2.7', '2.8'],
}
