"""
Billy Character Hash Commands
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
    Returns Billy's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'21e98aeb': [(log, ('1.0: Billy Hair IB Hash',)), (add_ib_check_if_missing,)],
'3371580a': [(log, ('1.0: Billy Body IB Hash',)), (add_ib_check_if_missing,)],
'dc7978f3': [(log, ('1.0: Billy Head IB Hash',)), (add_ib_check_if_missing,)],
'a1d68c9e': [
        (log,                           ('1.0: Billy HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f8a9cdb', 'Billy.HeadA.Diffuse.2048')),
    ],
'eed0cd5f': [
        (log,                           ('1.0: Billy HeadA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.HeadA.NormalMap.2048')),
    ],
'877e1a0d': [
        (log,                           ('1.0: Billy HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cf4769ce', 'Billy.HeadA.LightMap.2048')),
    ],
'dc2f2dd2': [
        (log,                           ('1.0: Billy HeadA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3a7d88a1', 'Billy.HeadA.MaterialMap.2048')),
    ],
'6f8a9cdb': [
        (log,                           ('1.0: Billy HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a1d68c9e', 'Billy.HeadA.Diffuse.1024')),
    ],
'e5f2fc35': [
        (log,                           ('1.0->2.5: Billy HeadA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'9f02ef2b': [
        (log,                           ('1.0->2.5: Billy HeadA LightMap 2048p Hash',)),
        (update_hash,                   ('cf4769ce',)),
    ],
'cf4769ce': [
        (log,                           ('2.5: Billy HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('877e1a0d', 'Billy.HeadA.LightMap.1024')),
        (multiply_section_if_missing,        (('f5a507da', '877e1a0d'), 'Billy.HeadA.LightMap.1024')),
    ],

'f5a507da': [
        (log,                           ('2.5: Billy HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('877e1a0d', 'Billy.HeadA.LightMap.1024')),
        (multiply_section_if_missing,        (('cf4769ce', '9f02ef2b'), 'Billy.HeadA.LightMap.2048')),
    ],
'd166c3e5': [
        (log,                           ('1.0->2.5: Billy HeadA MaterialMap 2048p Hash',)),
        (update_hash,                   ('3a7d88a1',)),
    ],
'3a7d88a1': [
        (log,                           ('2.5: Billy HeadA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc2f2dd2', 'Billy.HeadA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('e534abc0', 'dc2f2dd2'), 'Billy.HeadA.MaterialMap.1024')),
    ],

'e534abc0': [
        (log,                           ('2.5: Billy HeadA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('dc7978f3', 'Billy.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('dc2f2dd2', 'Billy.HeadA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('3a7d88a1', 'd166c3e5'), 'Billy.HeadA.MaterialMap.2048')),
    ],
'0475db07': [
        (log,                           ('1.0->2.5: Billy HairA Diffuse 2048p Hash',)),
        (update_hash,                   ('ff939fb7',)),
    ],
'ff939fb7': [
        (log,                           ('2.5: Billy HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0360c81', 'Billy.HairA.Diffuse.1024')),
        (multiply_section_if_missing,        (('c0360c81', '6a6a1c79'), 'Billy.HairA.Diffuse.1024')),
    ],

'6a6a1c79': [
        (log,                           ('2.5: Billy HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c0360c81', 'Billy.HairA.Diffuse.1024')),
        (multiply_section_if_missing,        (('ff939fb7', '0475db07'), 'Billy.HairA.Diffuse.2048')),
    ],
'c0360c81': [
        (log,                           ('1.0: Billy HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff939fb7', 'Billy.HairA.Diffuse.2048')),
    ],
'4817b1bc': [
        (log,                           ('1.0->2.5: Billy HairA LightMap 2048p Hash',)),
        (update_hash,                   ('b6e1da4b',)),
    ],
'b6e1da4b': [
        (log,                           ('2.5: Billy HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d269a0a1', 'Billy.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('2edbc842', 'f6749665', 'd269a0a1'), 'Billy.HairA.LightMap.1024')),
    ],

'f6749665': [(log, ('1.7 -> 2.0: Billy HairA LightMap 1024p Hash',)), (update_hash, ('2edbc842',))],
'2edbc842': [
        (log,                           ('2.5: Billy HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d269a0a1', 'Billy.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('b6e1da4b', '4817b1bc'), 'Billy.HairA.LightMap.2048')),
    ],
'd269a0a1': [
        (log,                           ('1.0: Billy HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b6e1da4b', 'Billy.HairA.LightMap.2048')),
    ],
'47bbe297': [
        (log,                           ('1.0->2.5: Billy HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('798adba3',)),
    ],
'798adba3': [
        (log,                           ('2.5: Billy HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('27185819', 'Billy.HairA.NormalMap.1024')),
    ],
'27185819': [
        (log,                           ('1.0: Billy HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('798adba3', 'Billy.HairA.NormalMap.2048')),
    ],
'058d85b5': [
        (log,                           ('2.5: Billy HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'399d9865': [
        (log,                           ('1.0: Billy BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('af07a583', 'Billy.BodyA.Diffuse.1024')),
    ],
'af07a583': [
        (log,                           ('1.0: Billy BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('399d9865', 'Billy.BodyA.Diffuse.2048')),
    ],
'789b054e': [
        (log,                           ('1.0->2.5: Billy BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('6305a7f4',)),
    ],
'6305a7f4': [
        (log,                           ('2.5: Billy BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0d5d374f', 'Billy.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('adc2ec7c', '0d5d374f'), 'Billy.BodyA.LightMap.1024')),
    ],

'adc2ec7c': [
        (log,                           ('2.5: Billy BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0d5d374f', 'Billy.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('6305a7f4', '789b054e'), 'Billy.BodyA.LightMap.2048')),
    ],
'0d5d374f': [
        (log,                           ('1.0: Billy BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6305a7f4', 'Billy.BodyA.LightMap.2048')),
    ],
'9cb20fa9': [
        (log,                           ('1.0: Billy BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b3cabf65', 'Billy.BodyA.MaterialMap.1024')),
    ],
'b3cabf65': [
        (log,                           ('1.0: Billy BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9cb20fa9', 'Billy.BodyA.MaterialMap.2048')),
    ],
'56b5953e': [
        (log,                           ('1.0->2.5: Billy BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Billy BodyA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('71d95d5d', 'Billy.BodyA.NormalMap.1024')),
    ],
'71d95d5d': [
        (log,                           ('1.0: Billy BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Billy.BodyA.NormalMap.2048')),
    ],
'5783253e': [
        (log, ('3.0: Billy Hair VB Hash',)),
        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'5d6b7415': [
        (log, ('3.0: Billy Hair VB Hash',)),
        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'cc5695a9': [
        (log, ('3.0: Billy Hair VB Hash',)),
        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'2e9d0312': [
        (log, ('3.0: Billy Body VB Hash',)),
        (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
    ],
'36a0392d': [
        (log, ('3.0: Billy Body VB Hash',)),
        (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
    ],
'89eeb1af': [
        (log, ('3.0: Billy Body VB Hash',)),
        (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
    ],
'771fdae9': [
        (log, ('3.0: Billy Body VB Hash',)),
        (add_section_if_missing, ('3371580a', 'Billy.Body.IB', 'match_priority = 0\n')),
    ],
'ed6468f9': [
        (log, ('3.0: Billy Face VB Hash',)),
        (add_section_if_missing, ('dc7978f3', 'Billy.Face.IB', 'match_priority = 0\n')),
    ],
'b19e644f': [
        (log, ('3.0: Billy Face VB Hash',)),
        (add_section_if_missing, ('dc7978f3', 'Billy.Face.IB', 'match_priority = 0\n')),
    ],
'26b0deb9': [
        (log, ('3.0: Billy Face VB Hash',)),
        (add_section_if_missing, ('dc7978f3', 'Billy.Face.IB', 'match_priority = 0\n')),
    ],
'9f671d6b': [(log, ('3.0: Billy weapon IB Hash',)), (add_ib_check_if_missing,)],
'3541c183': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],
'6f6aad09': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],
'11af0644': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],
'1fd6dbf3': [(log, ('3.0: Billy weapon IB Hash',)), (add_ib_check_if_missing,)],
'd776fbbe': [(log, ('3.0: Billy misc hash',)),],
'3e4c0174': [
        (log, ('3.0: Billy Hair VB Hash',)),
        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log, ('3.0: Billy Hair TEX Hash',)),
        (add_section_if_missing, ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
    ],
'4b0a8224': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],
'49782d36': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],

'3a1ee1d7': [
        (log, ('3.0: Billy weapon TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'Billy.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Billy',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

