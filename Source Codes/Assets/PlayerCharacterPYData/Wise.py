"""
Wise Character Hash Commands
ZZZ Mod Fixer v3.0
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
    """
    return {
# === IB Hashes ===
'b1df5d22': [(log, ('2.8: Wise Bag IB Hash',)),                         (add_ib_check_if_missing,)],
'8d6acf4e': [(log, ('2.8: Wise Body IB Hash',)),                        (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'ef9c0510': [(log, ('2.8: Wise Hair draw_vb',)),                        (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n'))],
'e8df7ff3': [(log, ('2.8: Wise Hair position_vb',)),                    (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n'))],
'774071dd': [(log, ('2.8: Wise Hair texcoord_vb',)),                    (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n'))],
'edfd1666': [(log, ('2.8 -> 3.0: Wise Hair blend_vb Hash [Legacy]',)),   (update_hash, ('68e4f572',))],

# Hair Shadow
'681651f9': [(log, ('2.8: Wise Hair Shadow draw_vb',)),                 (add_section_if_missing, ('8d08b190', 'Wise.HairShadow.IB', 'match_priority = 0\n'))],
'4af493e5': [(log, ('2.8: Wise Hair Shadow position_vb',)),             (add_section_if_missing, ('8d08b190', 'Wise.HairShadow.IB', 'match_priority = 0\n'))],
'ad7d7eca': [(log, ('2.8: Wise Hair Shadow texcoord_vb',)),             (add_section_if_missing, ('8d08b190', 'Wise.HairShadow.IB', 'match_priority = 0\n'))],
'795e9a7c': [(log, ('2.8: Wise Hair Shadow blend_vb',)),                (add_section_if_missing, ('8d08b190', 'Wise.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'b581dc0a': [(log, ('2.8: Wise Body draw_vb Hash',)),                   (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n'))],
'67f21c9f': [(log, ('2.8: Wise Body position_vb Hash',)),               (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n'))],
'91fbd2fa': [(log, ('2.8: Wise Body texcoord_vb Hash',)),               (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n'))],
'46462bd8': [(log, ('2.8 -> 3.0: Wise Body blend_vb Hash [Legacy]',)),   (update_hash, ('03dadd2a',))],

# Bag
'24ca2d36': [(log, ('2.8: Wise Bag draw_vb Hash',)),                     (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n'))],
'19f96193': [(log, ('2.8: Wise Bag position_vb Hash',)),                 (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n'))],
'8d825ff1': [(log, ('2.8: Wise Bag texcoord_vb Hash',)),                 (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n'))],
'd80dc314': [(log, ('2.8: Wise Bag blend_vb Hash',)),                    (add_section_if_missing, ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n'))],

# Face
'6c4552bb': [(log, ('2.8: Wise Face VertexLimit Hash',)),                (add_section_if_missing, ('1fdaf388', 'Wise.Head.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('2.8: Wise Face position_vb Hash',)),                (add_section_if_missing, ('1fdaf388', 'Wise.Head.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('2.8: Wise Face texcoord_vb Hash',)),                (add_section_if_missing, ('1fdaf388', 'Wise.Head.IB', 'match_priority = 0\n'))],
'757bc7cc': [(log, ('2.8 -> 3.0: Wise Face blend_vb Hash [Legacy]',)),   (update_hash, ('015fbf96',))],

# === Legacy Hash Updates ===
'f6cac296': [(log, ('2.8: Wise Hair IB Hash [Legacy]',)),               (update_hash, ('d5ca0411',))],
'ba59bf09': [(log, ('2.8: Wise Hair Draw Hash [Legacy]',)),             (update_hash, ('ef9c0510',))],
'1273c7b0': [(log, ('2.8: Wise Hair Blend Hash [Legacy]',)),            (update_hash, ('edfd1666',))],
'6235fa7f': [(log, ('2.8: Wise Hair Position Hash [Legacy]',)),         (update_hash, ('e8df7ff3',))],
'fe89498c': [(log, ('2.8: Wise Hair Texcoord Hash [Legacy]',)),         (update_hash, ('774071dd',))],
'4894246e': [(log, ('2.8: Wise Head IB Hash [Legacy]',)),               (update_hash, ('1fdaf388',))],
'054ea752': [(log, ('2.8: Wise Body IB Hash [Legacy]',)),               (update_hash, ('8d6acf4e',))],
'73c48816': [(log, ('2.8: Wise Body Draw Hash [Legacy]',)),             (update_hash, ('b581dc0a',))],
'1d55bd87': [(log, ('2.8: Wise Body Blend Hash [Legacy]',)),            (update_hash, ('46462bd8',))],
'9581de22': [(log, ('2.8: Wise Body Position Hash [Legacy]',)),         (update_hash, ('67f21c9f',))],
'a012c752': [(log, ('2.8: Wise Body Texcoord Hash [Legacy]',)),         (update_hash, ('91fbd2fa',))],
'f6c5b9f3': [(log, ('2.8: Wise Body Position Hash [Legacy] 1.6',)),     (update_hash, ('67f21c9f',))],
'a9d5b70d': [(log, ('2.8: Wise Body Texcoord Hash [Legacy] 1.6',)),     (update_hash, ('f425bd04',))],
'cb22cb95': [(log, ('2.8: Wise Bag Texcoord Hash [Legacy]',)),          (update_hash, ('8d825ff1',))],
'6c4ae8ce': [(log, ('2.8: Wise HeadA Diffuse 1024p Hash [Legacy]',)),   (update_hash, ('588d7d2d',))],
'1f21c633': [(log, ('2.8: Wise HairA, BagA LightMap 2048p Hash [Legacy]',)), (update_hash, ('8d8269f8',))],
'473f816d': [(log, ('2.8: Wise HairA, BagA MaterialMap 2048p Hash [Legacy]',)), (update_hash, ('f1b20f3d',))],
'3b4f22ad': [(log, ('2.8: Wise HairA, BagA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'f43c8025': [(log, ('2.8: Wise BodyA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'2ae08ae7': [(log, ('2.0 -> 2.1: Wise Bag Texcoord Hash',)),    (update_hash, ('8d825ff1',))],
'b300256d': [(log, ('1.7 -> 2.0: Wise Head Texcoord Hash',)), (update_hash, ('ebe9f31b',))],
'ebe9f31b': [(log, ('2.0 -> 2.1: Wise Head Texcoord Hash',)), (update_hash, ('c83b6cbf',))],
'83e07a1b': [(log, ('2.7 -> 2.8: Wise HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'af5fc216': [(log, ('2.7 -> 2.8: Wise HairShadow draw_vb Hash [Legacy]',)), (update_hash, ('681651f9',))],
'1a438b0d': [(log, ('2.7 -> 2.8: Wise HairShadow position_vb Hash [Legacy]',)), (update_hash, ('4af493e5',))],
'7b7957fa': [(log, ('2.7 -> 2.8: Wise HairShadow texcoord_vb Hash [Legacy]',)), (update_hash, ('ad7d7eca',))],
'52bd07dd': [(log, ('2.7 -> 2.8: Wise HairShadow blend_vb Hash [Legacy]',)), (update_hash, ('795e9a7c',))],
'3f771e63': [(log, ('2.8 -> 3.0: WiseSwimwear HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'6c4ae8ce': [(log, ('2.8: Wise HeadA Diffuse 1024p Hash [Legacy]',)),   (update_hash, ('588d7d2d',))],
'1f21c633': [(log, ('2.8: Wise HairA, BagA LightMap 2048p Hash [Legacy]',)), (update_hash, ('8d8269f8',))],
'473f816d': [(log, ('2.8: Wise HairA, BagA MaterialMap 2048p Hash [Legacy]',)), (update_hash, ('f1b20f3d',))],
'3b4f22ad': [(log, ('2.8: Wise HairA, BagA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],
'f43c8025': [(log, ('2.8: Wise BodyA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('ebac056e',))],

# === Broken References Fix (v2.8) ===
'f425bd04': [(log, ('2.8: Wise Body Texcoord Hash [Legacy] 2.0',)),     (update_hash, ('91fbd2fa',))],
'84529dab': [(log, ('2.8: Wise BodyA Diffuse 2048p Hash [Legacy] Old',)), (update_hash, ('f2fb7a37',))], # Update to f2fb7a37
'ef76b675': [(log, ('2.8: Wise BodyA Diffuse 1024p Hash [Legacy] Old',)), (update_hash, ('3d7a53b0',))],

# === 2.8 Sync Updates ===
'868709f2': [(log, ('2.7 -> 2.8: Wise BodyA Diffuse [Legacy]',)), (update_hash, ('f2fb7a37',))],

# === 3.0 Database Updates (Strict Sync) ===
# Body VBs
'03dadd2a': [(log, ('3.0: Wise Body blend_vb Hash',)),                  (add_section_if_missing, ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n'))],

# Hair VBs
'68e4f572': [(log, ('3.0: Wise Hair blend_vb Hash',)),                  (add_section_if_missing, ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n'))],

# Face VBs
'015fbf96': [(log, ('3.0: Wise Face blend_vb Hash',)),                  (add_section_if_missing, ('1fdaf388', 'Wise.Head.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'588d7d2d': [
        (log,                           ('2.8: Wise HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('1fdaf388', '4894246e'), 'Wise.Head.IB', 'match_priority = 0\n')),
    ],
'8f9d78c1': [
        (log,                           ('2.8: Wise HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('1fdaf388', '4894246e'), 'Wise.Head.IB', 'match_priority = 0\n')),
    ],

# === Hair & Bag Textures ===
'cb0d0c22': [
        (log,                           ('2.8: Wise HairA, BagA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('28005a5b', 'Wise.HairA.Diffuse.2048')),
    ],
'6fcc4ad4': [
        (log,                           ('2.8: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8d8269f8', '1f21c633'), 'Wise.HairA.LightMap.2048')),
    ],
'33368e12': [
        (log,                           ('2.8: Wise Hair/Bag LightMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],
'7c8b0713': [
        (log,                           ('2.8: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('f1b20f3d', '473f816d'), 'Wise.HairA.MaterialMap.2048')),
    ],
'd9383a15': [
        (log,                           ('2.8: Wise Hair/Bag MaterialMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'a9652fa4': [
        (log,                           ('3.0: Wise Body Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3d7a53b0', 'ef76b675'), 'Wise.BodyA.Diffuse.1024')),
    ],
'f2fb7a37': [
        (log,                           ('2.8 -> 3.0: Wise BodyA Diffuse 2048p Hash [Legacy]',)),
        (update_hash,                   ('a9652fa4',)),
    ],
'3d7a53b0': [
        (log,                           ('2.8: Wise BodyA Diffuse 1024p Hash [Legacy]',)),
        (update_hash,                   ('dea7a8ca',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a9652fa4', 'f2fb7a37'), 'Wise.BodyA.Diffuse.2048')),
    ],
'dea7a8ca': [
        (log,                           ('2.8 -> 3.0: Wise Body Diffuse1024 Hash [Legacy]',)),
        (update_hash,                   ('53b3623f',)),
    ],
'53b3623f': [
        (log,                           ('3.0: Wise Body Diffuse1024 Hash',)),
        (add_section_if_missing,        ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a9652fa4', 'f2fb7a37'), 'Wise.BodyA.Diffuse.2048')),
    ],
'088718a9': [
        (log,                           ('2.8: Wise BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9f46182a', 'Wise.BodyA.LightMap.1024')),
    ],
'9f46182a': [
        (log,                           ('2.8: Wise BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('088718a9', 'Wise.BodyA.LightMap.2048')),
    ],
'a5fdb5e7': [
        (log,                           ('2.8: Wise BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('148283b7', 'Wise.BodyA.MaterialMap.1024')),
    ],
'148283b7': [
        (log,                           ('2.8: Wise BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a5fdb5e7', 'Wise.BodyA.MaterialMap.2048')),
    ],
'6807521d': [
        (log,                           ('2.8: Wise BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('8d6acf4e', '054ea752'), 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'f43c8025'), 'Wise.BodyA.NormalMap.2048')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: Wise Shared NormalMap Hash (v2.8 Target)',)),
        (add_section_if_missing,        ('d5ca0411', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8d6acf4e', 'Wise.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8d08b190', 'Wise.HairShadow.IB', 'match_priority = 0\n')),
    ],
'db08bb73': [
        (log,                           ('2.8: Wise Shared NormalMap 1024p Hash [Legacy]',)),
        (add_section_if_missing,        (('d5ca0411', 'f6cac296'), 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '3b4f22ad'), 'Wise.HairA.NormalMap.2048')),
    ],
    '177ad7e8': [(log, ('2.4 -> 2.5: Wise Body Blend Hash',)), (update_hash, ('8612559a',))],
    '23876240': [(log,                           ('3.0: Wise BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('81406abe','669191ec'), 'Wise.BodyA.Diffuse.2048')),],
    '458bbde3': [(log, ('2.8 -> 3.0: Wise Neck Blend Hash',)), (update_hash, ('e0b1e734',))],

    # Body
    '81406abe': [(log, ('2.8 -> 3.0: Wise BodyA Diffuse 2048p Hash',)), (update_hash, ('669191ec',))],
    '4fa228f9': [(log, ('2.4 -> 2.5: Wise Body Draw Hash',)),     (update_hash, ('ca02f614',))],
    '6acc1eb8': [(log, ('2.4 -> 2.5: Wise Body IB Hash',)),       (update_hash, ('1eca2097',))],
    '8612559a': [(log, ('2.8 -> 3.0: Wise Body Blend Hash',)), (update_hash, ('f28a6363',))],
    '9fc3646e': [(log, ('2.8 -> 3.0: Wise BodyA Diffuse 1024p Hash',)), (update_hash, ('23876240',))],
    'a83ada4e': [(log, ('2.4 -> 2.5: Wise Body Texcoord Hash',)), (update_hash, ('b39870e1',))],
    'aa712fb9': [(log,                           ('2.0: Wise BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('24af1f48', 'Wise.BodyA.MaterialMap.2048')),],
    'ae59eabb': [(log, ('2.4 -> 2.5: Wise Body Position Hash',)), (update_hash, ('a388eb6b',))],
    'dd79b44b': [(log,                           ('2.0: Wise BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('05b25d35', 'Wise.BodyA.LightMap.2048')),],
    '28005a5b': [(log,                           ('1.0: Wise HairA, BagA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cb0d0c22', 'Wise.HairA.Diffuse.1024')),],
    '5d75fddc': [(log,                           ('2.0: WiseSummer FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('6c4ae8ce', '588d7d2d'), 'WiseSummer.FaceA.Diffuse.1024')),],
    '8d8269f8': [(log,                           ('1.0: Wise HairA, BagA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6fcc4ad4', 'Wise.HairA.LightMap.1024')),],
    'ebac056e': [(log,                           ('2.0: Wise BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('de303163', 'Wise.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9d1ab7c4', 'Wise.BodyA.LightMap.1024')),],
    'f1b20f3d': [(log,                           ('1.0: Wise HairA, BagA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c8b0713', 'Wise.HairA.MaterialMap.1024')),],
    '1fdaf388': [(log, ('1.6: Wise Head IB Hash',)), (add_ib_check_if_missing,)],
    '8d08b190': [(log, ('3.0: Wise HairShadow IB Hash',)), (add_ib_check_if_missing,)],
    'd5ca0411': [(log, ('2.1: Wise Hair IB Hash',)), (add_ib_check_if_missing,)],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Wise',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}