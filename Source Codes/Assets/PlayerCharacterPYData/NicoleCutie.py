"""
NicoleCutie Character Hash Commands
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
    Returns NicoleCutie's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'776f5703': [(log, ('2.5: NicoleCutie Hair IB Hash',)), (add_ib_check_if_missing,)],
'52842f31': [(log, ('2.5: NicoleCutie Body IB Hash',)), (add_ib_check_if_missing,)],
'262c96ff': [(log, ('2.5: NicoleCutie Phone IB Hash',)), (add_ib_check_if_missing,)],
'40e64ae2': [(log, ('2.5: NicoleCutie Amillion IB Hash',)), (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('2.5: NicoleCutie Face-脸 IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('93b02078',))],
'93b02078': [(log, ('3.0: NicoleCutie Face-脸 IB Hash',)), (add_ib_check_if_missing,)],
'd1e84a34': [
        (log,                           ('2.5: NicoleCutie FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'cdaa9ab5': [
        (log,                           ('2.5: NicoleCutie HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0e55f39d', 'NicoleCutie.HairA.Diffuse.1024')),
    ],

'0e55f39d': [
        (log,                           ('2.5: NicoleCutie HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('cdaa9ab5', 'NicoleCutie.HairA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: NicoleCutie HairA, BodyA, PhoneA, AmillionA NormalMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'4c8b0bce': [
        (log,                           ('2.5: NicoleCutie HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b3ef7388', 'NicoleCutie.HairA.LightMap.1024')),
    ],

'b3ef7388': [
        (log,                           ('2.5: NicoleCutie HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4c8b0bce', 'NicoleCutie.HairA.LightMap.2048')),
    ],
'a05c2386': [
        (log,                           ('2.5: NicoleCutie HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'4af0010c': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b2bd144b', 'NicoleCutie.BodyA.Diffuse.1024')),
    ],

'b2bd144b': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4af0010c', 'NicoleCutie.BodyA.Diffuse.2048')),
    ],
'c45a93a3': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5fcde3a6', 'NicoleCutie.BodyA.LightMap.1024')),
    ],

'5fcde3a6': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c45a93a3', 'NicoleCutie.BodyA.LightMap.2048')),
    ],
'592cee08': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('76774ee7', 'NicoleCutie.BodyA.MaterialMap.1024')),
    ],

'76774ee7': [
        (log,                           ('2.5: NicoleCutie BodyA, AmillionA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('592cee08', 'NicoleCutie.BodyA.MaterialMap.2048')),
    ],
'6986beb1': [
        (log,                           ('2.5: NicoleCutie PhoneA Diffuse Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4ae94b82': [
        (log,                           ('2.5: NicoleCutie PhoneA LightMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'4bbaadb9': [
        (log,                           ('2.5: NicoleCutie PhoneA MaterialMap Hash',)),
        (add_section_if_missing,        ('262c96ff', 'NicoleCutie.Phone.IB', 'match_priority = 0\n')),
    ],
'7b4b4f06': [
        (log, ('3.0: NicoleCutie Hair VB Hash',)),
        (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'a09489fa': [
        (log, ('3.0: NicoleCutie Hair VB Hash',)),
        (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'0df63fc6': [
        (log, ('3.0: NicoleCutie Hair VB Hash',)),
        (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'4ed9a81f': [(log, ('3.0: NicoleCutie Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'4d61e6f3': [
        (log, ('3.0: NicoleCutie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b408b261': [
        (log, ('3.0: NicoleCutie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'879a6522': [
        (log, ('3.0: NicoleCutie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'720296ff': [
        (log, ('3.0: NicoleCutie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4151c6c6': [
        (log, ('3.0: NicoleCutie Body VB Hash',)),
        (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
    ],
'dfab3761': [
        (log, ('3.0: NicoleCutie Body VB Hash',)),
        (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
    ],
'fa58977c': [
        (log, ('3.0: NicoleCutie Body VB Hash',)),
        (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
    ],
'f9fb2aa0': [
        (log, ('3.0: NicoleCutie Body VB Hash',)),
        (add_section_if_missing, ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
    ],
'bb7fffe9': [
        (log, ('3.0: NicoleCutie Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'176bf3d7': [
        (log, ('3.0: NicoleCutie Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'f9f810ed': [
        (log, ('3.0: NicoleCutie Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'4e1d9c9a': [
        (log, ('3.0: NicoleCutie Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
    ],
'ac6ebc5b': [
        (log, ('3.0: NicoleCutie Face VB Hash',)),
        (add_section_if_missing, ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'd5958556': [
        (log, ('3.0: NicoleCutie Face VB Hash',)),
        (add_section_if_missing, ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'292d1b1f': [
        (log, ('3.0: NicoleCutie Face VB Hash',)),
        (add_section_if_missing, ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'a8667746': [
        (log, ('2.8: NicoleCutie Face Position Hash',)),
        (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('ac6ebc5b',)),
    ],
'5714e5e6': [
        (log, ('2.8: NicoleCutie Face Texcoord Hash',)),
        (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('d5958556',)),
    ],
'9274e401': [
        (log, ('2.8: NicoleCutie Face VertexLimit Hash',)),
        (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('967c2f1c',)),
    ],
'b25ebcf6': [
        (log, ('2.8: NicoleCutie Face Blend Hash',)),
        (add_section_if_missing, ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('292d1b1f',)),
    ],
'f9befc51': [(log, ('3.0: NicoleCutie weapon IB Hash',)), (add_ib_check_if_missing,)],
'00c8b3c5': [
        (log, ('3.0: NicoleCutie weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'14b0d6b6': [
        (log, ('3.0: NicoleCutie weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'2f427bdb': [
        (log, ('3.0: NicoleCutie weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'67f0bd9c': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'28d0438d': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'f1304abf': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'7672fb0c': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'c03d03de': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'028c6ebf': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'63d1bd6f': [
        (log, ('3.0: NicoleCutie mobile phone VB Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'ef68beba': [
        (log, ('3.0: NicoleCutie mobile phone VB Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'8424f0ec': [
        (log, ('3.0: NicoleCutie mobile phone VB Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'cbce3456': [
        (log, ('3.0: NicoleCutie mobile phone VB Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'967c2f1c': [(log, ('3.0: NicoleCutie misc hash',)),],
'f6325378': [(log, ('3.0: NicoleCutie misc hash',)),],
'bafa609a': [
        (log, ('3.0: NicoleCutie Hair VB Hash',)),
        (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: NicoleCutie Hair TEX Hash',)),
        (add_section_if_missing, ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
    ],
'6abd3dd3': [
        (log, ('3.0: NicoleCutie Face TEX Hash',)),
        (add_section_if_missing, ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
    ],
'89699adb': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'b89dc4e4': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'48f45547': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'b6f0f975': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'df7b84ed': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'5c298267': [
        (log, ('3.0: NicoleCutie weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
    ],
'd484bf22': [
        (log, ('3.0: NicoleCutie mobile phone TEX Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'8d3aca36': [
        (log, ('3.0: NicoleCutie mobile phone TEX Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
'f8db9ea5': [
        (log, ('3.0: NicoleCutie mobile phone TEX Hash',)),
        (add_section_if_missing, ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NicoleCutie',
    'game_versions': ['2.5', '3.0'],
}
