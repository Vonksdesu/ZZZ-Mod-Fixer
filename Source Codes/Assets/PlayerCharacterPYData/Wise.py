"""
Wise Character Hash Commands
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
    Returns Wise's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes (Current v2.5)
'd5ca0411': [(log, ('2.5: Wise Hair IB Hash',)), (add_ib_check_if_missing,)],
'b1df5d22': [(log, ('1.0 - 2.5: Wise Bag IB Hash',)),  (add_ib_check_if_missing,)],
'8d6acf4e': [(log, ('1.1 - 2.5: Wise Body IB Hash',)), (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('1.6 - 2.5: Wise Head IB Hash',)), (add_ib_check_if_missing,)],

# IB Hash Updates
'f6cac296': [(log, ('1.0 -> 2.5: Wise Hair IB Hash',)), (update_hash, ('d5ca0411',))],
'ba59bf09': [(log, ('1.0 -> 2.5: Wise Hair Draw Hash',)), (update_hash, ('ef9c0510',))],
'1273c7b0': [(log, ('1.0 -> 2.5: Wise Hair Blend Hash',)), (update_hash, ('edfd1666',))],
'6235fa7f': [(log, ('1.0 -> 2.5: Wise Hair Position Hash',)), (update_hash, ('e8df7ff3',))],
'fe89498c': [(log, ('1.0 -> 2.5: Wise Hair Texcoord Hash',)), (update_hash, ('774071dd',))],
'4894246e': [(log, ('1.5 -> 1.6: Wise Head IB Hash',)),       (update_hash, ('1fdaf388',))],
'054ea752': [(log, ('1.0 -> 1.1: Wise Body IB Hash',)),       (update_hash, ('8d6acf4e',))],
'73c48816': [(log, ('1.0 -> 1.1: Wise Body Draw Hash',)),     (update_hash, ('b581dc0a',))],
'1d55bd87': [(log, ('1.0 -> 1.1: Wise Body Blend Hash',)),    (update_hash, ('46462bd8',))],
'9581de22': [(log, ('1.0 -> 1.1: Wise Body Position Hash',)), (update_hash, ('67f21c9f',))],
'a012c752': [(log, ('1.0 -> 1.1: Wise Body Texcoord Hash',)), (update_hash, ('91fbd2fa',))],
'f6c5b9f3': [(log, ('1.5 -> 1.6: Wise Body Position Hash',)),   (update_hash, ('67f21c9f',))],
'a9d5b70d': [(log, ('1.5 -> 1.6: Wise Body Texcoord Hash',)),   (update_hash, ('f425bd04',))],
'cb22cb95': [(log, ('1.2 -> 1.3: Wise Bag Texcoord Hash',)),    (update_hash, ('8d825ff1',))],
'6c4ae8ce': [(log, ('1.0 -> 1.1: Wise HeadA Diffuse 1024p Hash',)), (update_hash, ('588d7d2d',))],
'588d7d2d': [
        (log,                           ('1.1 - 2.5: Wise HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('1fdaf388', '4894246e'), 'Wise.Head.IB', 'match_priority = 0\n')),
    ],
'8f9d78c1': [
        (log,                           ('1.0 - 2.5: Wise HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('1fdaf388', '4894246e'), 'Wise.Head.IB', 'match_priority = 0\n')),
    ],

# Face Textures (v2.5)
'5d75fddc': [
        (log,                           ('2.5: Wise FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
    ],
'28005a5b': [
        (log,                           ('1.0 - 2.5: Wise HairA, BagA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cb0d0c22', 'Wise.HairA.Diffuse.1024')),
    ],
'cb0d0c22': [
        (log,                           ('1.0 - 2.5: Wise HairA, BagA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('28005a5b', 'Wise.HairA.Diffuse.2048')),
    ],

# Hair/Bag Texture Updates (v1.0 -> v2.5)
'1f21c633': [(log, ('1.0 -> 2.5: Wise HairA, BagA LightMap 2048p Hash',)), (update_hash, ('8d8269f8',))],
'8d8269f8': [
        (log,                           ('2.5: Wise HairA, BagA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6fcc4ad4', 'Wise.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('33368e12', '6fcc4ad4'), 'Wise.HairA.LightMap.1024')),
    ],

'33368e12': [
        (log,                           ('2.5: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6fcc4ad4', 'Wise.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('8d8269f8', '1f21c633'), 'Wise.HairA.LightMap.2048')),
    ],
'6fcc4ad4': [
        (log,                           ('1.0 - 2.5: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8d8269f8', '1f21c633'), 'Wise.HairA.LightMap.2048')),
    ],

'473f816d': [(log, ('1.0 -> 2.5: Wise HairA, BagA MaterialMap 2048p Hash',)), (update_hash, ('f1b20f3d',))],
'f1b20f3d': [
        (log,                           ('2.5: Wise HairA, BagA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c8b0713', 'Wise.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('d9383a15', '7c8b0713'), 'Wise.HairA.MaterialMap.1024')),
    ],

'd9383a15': [
        (log,                           ('2.5: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7c8b0713', 'Wise.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('f1b20f3d', '473f816d'), 'Wise.HairA.MaterialMap.2048')),
    ],
'7c8b0713': [
        (log,                           ('1.0 - 2.5: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('f1b20f3d', '473f816d'), 'Wise.HairA.MaterialMap.2048')),
    ],

'3b4f22ad': [(log, ('1.0 -> 2.5: Wise HairA, BagA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('2.5: Wise Shared NormalMap Hash (Hair/Bag/Body)',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('db08bb73', 'Wise.HairA.NormalMap.1024')),
    ],
'db08bb73': [
        (log,                           ('1.0 - 2.5: Wise HairA, BagA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '3b4f22ad'), 'Wise.HairA.NormalMap.2048')),
    ],
'84529dab': [(log, ('1.0 - 1.1: Wise BodyA Diffuse 2048p Hash',)), (update_hash, ('868709f2',))],
'868709f2': [(log, ('2.6 -> 2.7: Wise BodyA Diffuse 2048p Hash',)), (update_hash, ('f2fb7a37',))],
'ef76b675': [(log, ('1.0 - 1.1: Wise BodyA Diffuse 1024p Hash',)), (update_hash, ('3d7a53b0',))],
'3d7a53b0': [(log, ('2.6 -> 2.7: Wise BodyA Diffuse 1024p Hash',)), (update_hash, ('dea7a8ca',))],
'dea7a8ca': [
        (log,                           ('2.8 -> 3.0: Wise BodyA Diffuse 1024p Hash',)),
        (update_hash,                        ('53b3623f',)),
    ],
'53b3623f': [
        (log,                           ('1.1: Wise BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('868709f2', '84529dab', 'f2fb7a37', 'a9652fa4'), 'Wise.BodyA.Diffuse.2048')),
    ],
'f2fb7a37': [
        (log,                           ('2.8 -> 3.0: Wise BodyA Diffuse 2048p Hash',)),
        (update_hash,                        ('a9652fa4',)),
    ],
'a9652fa4': [
        (log,                           ('1.1: Wise BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('3d7a53b0', 'ef76b675', 'dea7a8ca', '53b3623f'), 'Wise.BodyA.Diffuse.1024')),
    ],
'088718a9': [
        (log,                           ('1.0 - 2.5: Wise BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9f46182a', 'Wise.BodyA.LightMap.1024')),
    ],
'9f46182a': [
        (log,                           ('1.0 - 2.5: Wise BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('088718a9', 'Wise.BodyA.LightMap.2048')),
    ],
'a5fdb5e7': [
        (log,                           ('1.0 - 2.5: Wise BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('148283b7', 'Wise.BodyA.MaterialMap.1024')),
    ],
'148283b7': [
        (log,                           ('1.0 - 2.5: Wise BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a5fdb5e7', 'Wise.BodyA.MaterialMap.2048')),
    ],

# Body NormalMap now uses shared ebac056e hash in v2.5
'f43c8025': [(log, ('1.0 -> 2.5: Wise BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'6807521d': [
        (log,                           ('1.0 - 2.5: Wise BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'f43c8025'), 'Wise.BodyA.NormalMap.2048')),
    ],
'e8df7ff3': [
        (log, ('3.0: Wise Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
    ],
'774071dd': [
        (log, ('3.0: Wise Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
    ],
'edfd1666': [(log, ('2.8 -> 3.0: Wise Hair Blend Hash',)), (update_hash, ('68e4f572',))],
'68e4f572': [
        (log, ('3.0: Wise Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
    ],
'8d08b190': [(log, ('3.0: Wise Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'681651f9': [
        (log, ('3.0: Wise Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'Wise.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4af493e5': [
        (log, ('3.0: Wise Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'Wise.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ad7d7eca': [
        (log, ('3.0: Wise Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'Wise.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'795e9a7c': [
        (log, ('3.0: Wise Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'Wise.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b581dc0a': [
        (log, ('3.0: Wise Body VB Hash',)),
        (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
    ],
'67f21c9f': [
        (log, ('3.0: Wise Body VB Hash',)),
        (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
    ],
'f425bd04': [(log, ('2.0 -> 2.1: Wise Body Texcoord Hash',)), (update_hash, ('91fbd2fa',))],
'91fbd2fa': [
        (log, ('3.0: Wise Body VB Hash',)),
        (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
    ],
'46462bd8': [(log, ('2.8 -> 3.0: Wise Body Blend Hash',)), (update_hash, ('03dadd2a',))],
'03dadd2a': [
        (log, ('3.0: Wise Body VB Hash',)),
        (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
    ],
'24ca2d36': [
        (log, ('3.0: Wise Bag VB Hash',)),
        (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],
'19f96193': [
        (log, ('3.0: Wise Bag VB Hash',)),
        (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],
'2ae08ae7': [(log, ('2.0 -> 2.1: Wise Bag Texcoord Hash',)),    (update_hash, ('8d825ff1',))],
'8d825ff1': [
        (log, ('3.0: Wise Bag VB Hash',)),
        (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],
'd80dc314': [
        (log, ('3.0: Wise Bag VB Hash',)),
        (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],
'5657c1fc': [
        (log, ('3.0: Wise Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
    ],
'b300256d': [(log, ('1.7 -> 2.0: Wise Head Texcoord Hash',)), (update_hash, ('ebe9f31b',))],
'ebe9f31b': [(log, ('2.0 -> 2.1: Wise Head Texcoord Hash',)), (update_hash, ('c83b6cbf',))],
'c83b6cbf': [
        (log, ('3.0: Wise Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
    ],
'2b320847': [
        (log, ('3.1: Wise Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
    ],
'015fbf96': [
        (log, ('3.0: Wise Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
    ],
'757bc7cc': [
        (log, ('2.8: Wise Face Blend Hash',)),
        (add_section_if_missing, ('1fdaf388', 'Wise.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('015fbf96',)),
    ],
'6c4552bb': [(log, ('3.0: Wise misc hash',)),],
'ef9c0510': [
        (log, ('3.0: Wise Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Wise Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Wise',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5', '2.6', '2.7', '2.8', '3.0'],
}

