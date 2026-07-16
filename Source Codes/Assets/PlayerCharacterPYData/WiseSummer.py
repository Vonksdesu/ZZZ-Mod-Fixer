"""
WiseSummer Character Hash Commands
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
    Returns WiseSummer's hash commands dictionary.
    """
    return {

# === IB Hashes ===
'1fdaf388': [(log, ('2.8: WiseSummer Face IB Hash (shared with Wise)',)), (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'0ec31440': [(log, ('3.0: WiseSummer Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'19a3f02e': [(log, ('3.0: WiseSummer Body IB Hash',)),                  (add_ib_check_if_missing,)],
'8d08b190': [(log, ('3.0: WiseSummer HairShadow IB Hash',)),            (add_ib_check_if_missing,)],

# === IB Hashes (WiseSkin v2.0 Historical) ===

# === VB Hashes ===
# Hair

# Hair Shadow

# Body


# Face

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs

# HairShadow VBs

# Body VBs

# Face VBs

# === Face Textures ===
'5d75fddc': [
        (log,                           ('2.8: WiseSummer Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'd476035d': [
        (log,                           ('2.8: WiseSummer BodyA Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'0fa8f99c': [
        (log,                           ('2.8: WiseSummer BodyA LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],
'c2c8606e': [
        (log,                           ('2.8: WiseSummer FaceA, BodyA MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSummer.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === WiseSkin Body Textures (v2.0 Historical) ===

# === Hair Textures ===
'28005a5b': [
        (log,                           ('2.8: WiseSummer HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.8: WiseSummer HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.8: WiseSummer HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('cb272754', 'f6cac296'), 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'ebac056e': [
        (log,                           ('2.8: WiseSummer BodyA, HairA NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('4fe696c8', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cb272754', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('19a3f02e', 'WiseSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ec31440', 'WiseSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8d08b190', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n')),
    ],
    '4af493e5': [(log, ('2.8: WiseTemple HairShadow position_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
    '681651f9': [(log, ('2.8: WiseTemple HairShadow draw_vb',)),            (add_section_if_missing, ('8d08b190', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
    '795e9a7c': [(log, ('2.8: WiseTemple HairShadow blend_vb',)),           (add_section_if_missing, ('8d08b190', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
    'ad7d7eca': [(log, ('2.8: WiseTemple HairShadow texcoord_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseSummer.HairShadow.IB', 'match_priority = 0\n'))],
    '16c55ecc': [(log, ('3.0: WiseSummer Hair blend_vb',)), (add_section_if_missing, ('16c55ecc', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '1a6be2b0': [(log, ('3.0: WiseSummer Hair position_vb',)), (add_section_if_missing, ('1a6be2b0', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '20f40e82': [(log, ('3.0: WiseSummer Hair draw_vb',)), (add_section_if_missing, ('20f40e82', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '31d424fc': [(log, ('3.0: WiseSummer Body texcoord_vb',)), (add_section_if_missing, ('31d424fc', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '44accf08': [(log, ('3.0: WiseSummer Body draw_vb',)), (add_section_if_missing, ('44accf08', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '71a703c7': [(log, ('3.0: WiseSummer Body position_vb',)), (add_section_if_missing, ('71a703c7', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '951a90bf': [(log, ('3.0: WiseSummer Hair texcoord_vb',)), (add_section_if_missing, ('951a90bf', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '9ab40475': [(log, ('3.0: WiseSummer Body blend_vb',)), (add_section_if_missing, ('9ab40475', 'WiseSummer.Unknown.IB', 'match_priority = 0\n'))],
    '4fe696c8': [(log, ('2.1 -> 2.2: WiseSummer Body IB Hash [Legacy]',)), (update_hash, ('19a3f02e',))],
    'cb272754': [(log, ('2.1 -> 2.2: WiseSummer Hair IB Hash [Legacy]',)), (update_hash, ('0ec31440',))],
    '1a438b0d': [(log, ('2.7 -> 2.8: WiseSummer HairShadow position_vb Hash [Legacy]',)), (update_hash, ('4af493e5',))],
    '3f771e63': [(log, ('2.8 -> 3.0: WiseSummer HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
    '52bd07dd': [(log, ('2.7 -> 2.8: WiseSummer HairShadow blend_vb Hash [Legacy]',)), (update_hash, ('795e9a7c',))],
    '7b7957fa': [(log, ('2.7 -> 2.8: WiseSummer HairShadow texcoord_vb Hash [Legacy]',)), (update_hash, ('ad7d7eca',))],
    '83e07a1b': [(log, ('2.7 -> 2.8: WiseSummer HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
    'af5fc216': [(log, ('2.7 -> 2.8: WiseSummer HairShadow draw_vb Hash [Legacy]',)), (update_hash, ('681651f9',))],
    '14fff21a': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('14fff21a', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '16ac44f6': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('16ac44f6', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '18e704a8': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('18e704a8', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '49d81f9a': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('49d81f9a', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '5c5bde90': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('5c5bde90', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '77045a80': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('77045a80', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '82396952': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('82396952', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '8e9a12c7': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('8e9a12c7', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'a2c79f8d': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('a2c79f8d', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'acfe9fe4': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('acfe9fe4', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'd4147320': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('d4147320', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'd6c86c1e': [(log, ('3.0: WiseSummer Unknown Component Hash',)), (add_section_if_missing, ('d6c86c1e', 'WiseSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '33368e12': [(log,                           ('2.0: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8d8269f8', '1f21c633'), 'Wise.HairA.LightMap.2048')),],
    '588d7d2d': [(log,                           ('1.1: Wise HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4894246e', 'Wise.Head.IB', 'match_priority = 0\n')),],
    '5907afda': [(log,                           ('2.0: WiseSummer BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('d476035d', 'WiseSummer.BodyA.Diffuse.2048')),],
    '798adba3': [(log,                           ('1.0: Billy HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'Billy.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('27185819', 'Billy.HairA.NormalMap.1024')),],
    '7a142a7d': [(log,                           ('2.0: WiseSummer BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('0fa8f99c', 'WiseSummer.BodyA.LightMap.2048')),],
    'cb0d0c22': [(log,                           ('1.0: Wise HairA, BagA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('28005a5b', 'Wise.HairA.Diffuse.2048')),],
    'd6996446': [(log,                           ('2.0: WiseSummer BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('c2c8606e', 'WiseSummer.BodyA.MaterialMap.2048')),],
    'd9383a15': [(log,                           ('2.0: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('f1b20f3d', '473f816d'), 'Wise.HairA.MaterialMap.2048')),],
    '9741e2f0': [(log, ('2.1 -> 2.2: WiseSummer Body Blend Hash',)), (update_hash, ('d4147320',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseSummer',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}