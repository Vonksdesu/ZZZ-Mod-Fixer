"""
Nicole Character Hash Commands
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
    Returns Nicole's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6847bbbd': [(log, ('1.0 -> 3.0: Nicole Hair-头发 IB Hash',)),    (update_hash, ('7dcfe907',))],
'7dcfe907': [(log, ('3.0: Nicole Hair-头发 IB Hash',)),    (add_ib_check_if_missing,)],
'5a4c1ef3': [(log, ('1.0 -> 3.0: Nicole Body-身体 IB Hash',)),    (update_hash, ('e53364dd',))],
'e53364dd': [(log, ('3.0: Nicole Body-身体 IB Hash',)),    (add_ib_check_if_missing,)],
'7435fc0e': [(log, ('1.0 - 2.8: Nicole Face-脸 IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('93b02078',))],
'93b02078': [(log, ('3.0: Nicole Face-脸 IB Hash',)), (add_ib_check_if_missing,)],
'6abd3dd3': [
        (log,                           ('1.0-1.7: Nicole HeadA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'd1e84a34': [
        (log,                           ('1.0-2.5: Nicole HeadA Diffuse 2048p Hash',)),
    ],
'6d3868f9': [
        (log,                           ('1.0-2.5: Nicole HairA Diffuse 2048p Hash',)),
    ],
'7a45adcd': [
        (log,                           ('1.0-1.7: Nicole HairA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'1dfd9e16': [
        (log,                           ('1.0-1.7: Nicole HairA LightMap 2048p Hash',)),
        (update_hash,                   ('8c9c25d5',)),
    ],
'9adc04ed': [
        (log,                           ('1.0-1.7: Nicole HairA LightMap 1024p Hash (Removed in 2.5)',)),
    ],
'8c9c25d5': [
        (log,                           ('2.5: Nicole HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        (('f3c21e41', '9adc04ed'), 'Nicole.HairA.LightMap.1024')),
    ],

'f3c21e41': [
        (log,                           ('2.5: Nicole HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        (('8c9c25d5', '1dfd9e16'), 'Nicole.HairA.LightMap.2048')),
    ],
'a05c2386': [
        (log,                           ('2.5: Nicole HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'bffb4a66': [
        (log,                           ('1.0-1.7: Nicole HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'b8db0209': [
        (log,                           ('1.0-1.7: Nicole HairA NormalMap 1024p Hash (Removed in 2.5)',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Nicole HairA, BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'f86ffe2c': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'9ee9b402': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA Diffuse 1024p Hash (Removed in 2.5)',)),
    ],
'80855e0f': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'2b5aa784': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA LightMap 1024p Hash (Removed in 2.5)',)),
    ],
'95cabef3': [
        (log,                           ('1.0-2.5: Nicole BodyA, AmillionA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'bb33129d': [
        (log,                           ('1.0-1.7: Nicole BodyA, AmillionA MaterialMap 1024p Hash (Removed in 2.5)',)),
    ],
'8cf23419': [
        (log,                           ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'580df52d': [
        (log,                           ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 1024p Hash (Removed in 2.5)',)),
    ],
'40e64ae2': [(log, ('2.5: Nicole Amillion IB Hash',)),    (add_ib_check_if_missing,)],
'f6344432': [(log, ('2.4 -> 3.01: Nicole Hair-头发 draw_vb Hash',)), (update_hash, ('d9b8d61a',))],
'd9b8d61a': [
        (log, ('3.0: Nicole Hair VB Hash',)),
        (add_section_if_missing, ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'199853eb': [(log, ('2.4 -> 3.01: Nicole Hair-头发 position_vb Hash',)), (update_hash, ('6f931ca7',))],
'6f931ca7': [
        (log, ('3.0: Nicole Hair VB Hash',)),
        (add_section_if_missing, ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'06e4fd79': [(log, ('2.4 -> 3.01: Nicole Hair-头发 texcoord_vb Hash',)), (update_hash, ('e04f4893',))],
'e04f4893': [
        (log, ('3.0: Nicole Hair VB Hash',)),
        (add_section_if_missing, ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'347e4a48': [(log, ('2.4 -> 3.01: Nicole Hair-头发 blend_vb Hash',)), (update_hash, ('8171f5c9',))],
'8171f5c9': [
        (log, ('3.0: Nicole Hair VB Hash',)),
        (add_section_if_missing, ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'4ed9a81f': [(log, ('3.0: Nicole Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'4d61e6f3': [
        (log, ('3.0: Nicole Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b408b261': [
        (log, ('3.0: Nicole Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'e6b9e50e': [
        (log, ('3.0: Nicole Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ab4b28ad': [
        (log, ('3.0: Nicole Hair Shadow VB Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'322345a6': [
        (log, ('2.8: Nicole Hair Shadow Texcoord Hash',)),
        (add_section_if_missing, ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
        (update_hash, ('e6b9e50e',)),
    ],
'8cc1262b': [(log, ('2.4 -> 3.01: Nicole Body-身体 draw_vb Hash',)), (update_hash, ('b19da99e',))],
'b19da99e': [
        (log, ('3.0: Nicole Body VB Hash',)),
        (add_section_if_missing, ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'89df5a07': [(log, ('2.4 -> 3.01: Nicole Body-身体 position_vb Hash',)), (update_hash, ('4af0a4cd',))],
'4af0a4cd': [
        (log, ('3.0: Nicole Body VB Hash',)),
        (add_section_if_missing, ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'91c1b779': [(log, ('2.4 -> 3.01: Nicole Body-身体 texcoord_vb Hash',)), (update_hash, ('ed4c47a9',))],
'ed4c47a9': [
        (log, ('3.0: Nicole Body VB Hash',)),
        (add_section_if_missing, ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'7ecda89f': [(log, ('2.4 -> 3.01: Nicole Body-身体 blend_vb Hash',)), (update_hash, ('b793c804',))],
'b793c804': [
        (log, ('3.0: Nicole Body VB Hash',)),
        (add_section_if_missing, ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
    ],
'176bf3d7': [
        (log, ('3.0: Nicole Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'077c3500': [(log, ('2.4 -> 3.01: Nicole Amillion-艾米莉安 texcoord_vb Hash',)), (update_hash, ('f9f810ed',))],
'f9f810ed': [
        (log, ('3.0: Nicole Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'4e1d9c9a': [
        (log, ('3.0: Nicole Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
'd5958556': [
        (log, ('3.0: Nicole Face VB Hash',)),
        (add_section_if_missing, ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
    ],
'292d1b1f': [
        (log, ('3.0: Nicole Face VB Hash',)),
        (add_section_if_missing, ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
    ],
'5714e5e6': [
        (log, ('2.8: Nicole Face Texcoord Hash',)),
        (add_section_if_missing, ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('d5958556',)),
    ],
'9274e401': [
        (log, ('2.8: Nicole Face VertexLimit Hash',)),
        (add_section_if_missing, ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('967c2f1c',)),
    ],
'b25ebcf6': [
        (log, ('2.8: Nicole Face Blend Hash',)),
        (add_section_if_missing, ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('292d1b1f',)),
    ],
'f9befc51': [(log, ('3.0: Nicole weapon IB Hash',)), (add_ib_check_if_missing,)],
'00c8b3c5': [
        (log, ('3.0: Nicole weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'14b0d6b6': [
        (log, ('3.0: Nicole weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'2f427bdb': [
        (log, ('3.0: Nicole weapon VB Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'a365836f': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'fda56c66': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'ad4bf30d': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'76e8ac35': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'967c2f1c': [(log, ('3.0: Nicole misc hash',)),],
'f6325378': [(log, ('3.0: Nicole misc hash',)),],
'798adba3': [
        (log, ('3.0: Nicole Hair TEX Hash',)),
        (add_section_if_missing, ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
    ],
'35951ccf': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'6d5ee825': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'0fe671cc': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'f1af36a8': [
        (log, ('3.0: Nicole weapon TEX Hash',)),
        (add_section_if_missing, ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
    ],
'bb7fffe9': [
        (log, ('3.0: Nicole Amillion VB Hash',)),
        (add_section_if_missing, ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nicole',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5', '3.0'],
}

