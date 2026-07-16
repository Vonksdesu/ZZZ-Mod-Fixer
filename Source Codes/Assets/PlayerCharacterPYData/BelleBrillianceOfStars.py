"""
BelleBrillianceOfStars Character Hash Commands
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
    Returns BelleBrillianceOfStars's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'a6431856': [(log, ('3.0: BelleBrillianceOfStars Neck IB Hash',)),         (add_ib_check_if_missing,)],
'403eace9': [(log, ('3.0: BelleBrillianceOfStars HairShadow IB Hash',)),    (add_ib_check_if_missing,)],
# === VB Hashes ===
# Hat
'0a877d89': [(log, ('3.0: BelleBrillianceOfStars Hat draw_vb',)),          (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'74d2da11': [(log, ('3.0: BelleBrillianceOfStars Hat position_vb',)),      (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'801cd45d': [(log, ('3.0: BelleBrillianceOfStars Hat texcoord_vb',)),      (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],
'd5070379': [(log, ('3.0: BelleBrillianceOfStars Hat blend_vb',)),         (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n'))],

# Face
'04abceb5': [(log, ('3.0: BelleBrillianceOfStars Face draw_vb',)),         (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('3.0: BelleBrillianceOfStars Face position_vb',)),     (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'd3000b22': [(log, ('3.0: BelleBrillianceOfStars Face texcoord_vb',)),     (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],
'359e4502': [(log, ('3.0: BelleBrillianceOfStars Face blend_vb',)),        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n'))],

# Neck
'0e72bdb7': [(log, ('3.0: BelleBrillianceOfStars Neck draw_vb',)),         (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'd5c6a50f': [(log, ('3.0: BelleBrillianceOfStars Neck position_vb',)),     (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'07a15f8e': [(log, ('3.0: BelleBrillianceOfStars Neck texcoord_vb',)),     (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],
'57192494': [(log, ('3.0: BelleBrillianceOfStars Neck blend_vb',)),        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n'))],

# Hair
'992d149f': [(log, ('3.0: BelleBrillianceOfStars Hair draw_vb',)),         (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'dbd537bb': [(log, ('3.0: BelleBrillianceOfStars Hair position_vb',)),     (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'0f1d7b96': [(log, ('3.0: BelleBrillianceOfStars Hair texcoord_vb',)),     (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],
'2cf18f34': [(log, ('3.0: BelleBrillianceOfStars Hair blend_vb',)),        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n'))],

# Extra
'f6ed0e7b': [(log, ('3.0: BelleBrillianceOfStars Extra draw_vb',)),        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'd9087948': [(log, ('3.0: BelleBrillianceOfStars Extra position_vb',)),    (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'1cfe1205': [(log, ('3.0: BelleBrillianceOfStars Extra texcoord_vb',)),    (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],
'82c81803': [(log, ('3.0: BelleBrillianceOfStars Extra blend_vb',)),       (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n'))],

# Tie
'c0ee97be': [(log, ('3.0: BelleBrillianceOfStars Tie draw_vb',)),          (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'6aa2848f': [(log, ('3.0: BelleBrillianceOfStars Tie position_vb',)),      (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'88e81d00': [(log, ('3.0: BelleBrillianceOfStars Tie texcoord_vb',)),      (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],
'f83e837a': [(log, ('3.0: BelleBrillianceOfStars Tie blend_vb',)),         (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n'))],

# Body
'76ceb325': [(log, ('3.0: BelleBrillianceOfStars Body draw_vb',)),         (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'df17d505': [(log, ('3.0: BelleBrillianceOfStars Body position_vb',)),     (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'3e19f179': [(log, ('3.0: BelleBrillianceOfStars Body texcoord_vb',)),     (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],
'987395ef': [(log, ('3.0: BelleBrillianceOfStars Body blend_vb',)),        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n'))],

# Earrings
'e2c8decf': [(log, ('3.0: BelleBrillianceOfStars Earrings draw_vb',)),      (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'29324995': [(log, ('3.0: BelleBrillianceOfStars Earrings position_vb',)),  (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'8da231b5': [(log, ('3.0: BelleBrillianceOfStars Earrings texcoord_vb',)),  (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],
'611f1c52': [(log, ('3.0: BelleBrillianceOfStars Earrings blend_vb',)),     (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'75ec3614': [
        (log,                           ('3.0: BelleBrillianceOfStars Face Diffuse Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
    '77eef7e8': [
        (log,                           ('3.0: BelleBrillianceOfStars Face Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('75ec3614', 'BelleBrillianceOfStars.Face.Diffuse.2048')),
    ],


# === Hair Textures ===
'1ce58567': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
    '08f04d95': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('1ce58567', 'BelleBrillianceOfStars.Hair.Diffuse.2048')),
    ],
    '7d562f53': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair LightMap 2048p Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
    'f44f330b': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('7d562f53', 'BelleBrillianceOfStars.Hair.LightMap.2048')),
    ],
    '34bdb036': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
    '7542ef4b': [
        (log,                           ('3.0: BelleBrillianceOfStars Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('34bdb036', 'BelleBrillianceOfStars.Hair.MaterialMap.2048')),
    ],


# === Legacy Hash Updates (Historical Chain v2.0 - v2.8) ===
'01b0c8b6': [(log, ('2.8 -> 3.0: BelleBrillianceOfStars Face blend_vb [Legacy]',)), (update_hash, ('f3dedb50',))],
'1de8fc08': [(log, ('2.8 -> 3.0: BelleBrillianceOfStars Face texcoord_vb [Legacy]',)), (update_hash, ('d3000b22',))],
'0c9a075b': [(log, ('2.8 -> 3.0: BelleBrillianceOfStars Face Blend Hash [Legacy]',)), (update_hash, ('359e4502',))],


# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: BelleBrillianceOfStars Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
    'd9a12c0a': [
        (log,                           ('3.0: BelleBrillianceOfStars Neck NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('ebac056e', 'BelleBrillianceOfStars.Neck.NormalMap.2048')),
    ],
'ebac056e': [
        (log,                           ('3.0: BelleBrillianceOfStars Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a318b3c6', 'BelleBrillianceOfStars.Extra.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
    '0a843a8f': [(log, ('3.0: BelleBrillianceOfStars Hat IB Hash',)), (add_ib_check_if_missing,)],
'b946c37f': [(log, ('3.0: BelleBrillianceOfStars Tie IB Hash',)), (add_ib_check_if_missing,)],
'62711f82': [(log, ('3.0: BelleBrillianceOfStars Earrings IB Hash',)), (add_ib_check_if_missing,)],
'feb1c4cd': [(log, ('3.0: BelleBrillianceOfStars Body IB Hash',)), (add_ib_check_if_missing,)],
'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Player IB Hash',)), (add_ib_check_if_missing,)],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '42310c0e': [(log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '57130f7c': [(log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '5724e531': [(log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '62711f82': [(log, ('3.0: BelleBrillianceOfStars Earrings IB Hash',)), (add_ib_check_if_missing,)],
'feb1c4cd': [(log, ('3.0: BelleBrillianceOfStars Body IB Hash',)), (add_ib_check_if_missing,)],
'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Player IB Hash',)), (add_ib_check_if_missing,)],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '8c0ea559': [(log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '9a9780a7': [(log, ('2.8: BelleTemple Face IB Hash',)),                 (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('2.8: BelleTemple Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.8: BelleTemple Legs IB Hash',)),                 (add_ib_check_if_missing,)],
'ce86946f': [(log, ('2.8: BelleTemple BackAcc IB Hash',)),              (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.8: BelleTemple Body IB Hash',)),                 (add_ib_check_if_missing,)],
'db72ceab': [(log, ('2.8: BelleTemple HairWAcc IB Hash',)),              (add_ib_check_if_missing,)],
'403eace9': [(log, ('2.8: BelleTemple Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'c2189ddf': [(log, ('2.8: BelleTemple Red Knot Rope IB Hash',)),        (add_ib_check_if_missing,)],
'2ac09c8f': [(log, ('2.8: BelleTemple Orange Green Ribbon IB Hash',)),  (add_ib_check_if_missing,)],
'c0fcc53d': [(log, ('2.8: BelleTemple Earrings1 IB Hash',)),            (add_ib_check_if_missing,)],
'e6e890a7': [(log, ('2.8: BelleTemple Earrings2 IB Hash',)),            (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: BelleTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'b28a7685': [(log, ('2.8: BelleTemple Cat Ear Accessories IB Hash',)),  (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: BelleTemple Pink Badge IB Hash',)),           (add_ib_check_if_missing,)],
'4dcc384f': [(log, ('2.8: BelleTemple Orange Green Badge IB Hash',)),   (add_ib_check_if_missing,)],
'455bcfc7': [(log, ('2.8: BelleTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],
'169e5f5d': [(log, ('3.0: BelleTemple BackRibbon IB Hash',)),            (add_ib_check_if_missing,)],
'e850777c': [(log, ('3.0: BelleTemple Earring IB Hash',)),               (add_ib_check_if_missing,)],
    'a292d07d': [(log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Player IB Hash',)), (add_ib_check_if_missing,)],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    'aa9ffb85': [(log, ('2.8: BelleTemple Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.8: BelleTemple Legs IB Hash',)),                 (add_ib_check_if_missing,)],
'ce86946f': [(log, ('2.8: BelleTemple BackAcc IB Hash',)),              (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.8: BelleTemple Body IB Hash',)),                 (add_ib_check_if_missing,)],
'db72ceab': [(log, ('2.8: BelleTemple HairWAcc IB Hash',)),              (add_ib_check_if_missing,)],
'403eace9': [(log, ('2.8: BelleTemple Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'c2189ddf': [(log, ('2.8: BelleTemple Red Knot Rope IB Hash',)),        (add_ib_check_if_missing,)],
'2ac09c8f': [(log, ('2.8: BelleTemple Orange Green Ribbon IB Hash',)),  (add_ib_check_if_missing,)],
'c0fcc53d': [(log, ('2.8: BelleTemple Earrings1 IB Hash',)),            (add_ib_check_if_missing,)],
'e6e890a7': [(log, ('2.8: BelleTemple Earrings2 IB Hash',)),            (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: BelleTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'b28a7685': [(log, ('2.8: BelleTemple Cat Ear Accessories IB Hash',)),  (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: BelleTemple Pink Badge IB Hash',)),           (add_ib_check_if_missing,)],
'4dcc384f': [(log, ('2.8: BelleTemple Orange Green Badge IB Hash',)),   (add_ib_check_if_missing,)],
'455bcfc7': [(log, ('2.8: BelleTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],
'169e5f5d': [(log, ('3.0: BelleTemple BackRibbon IB Hash',)),            (add_ib_check_if_missing,)],
'e850777c': [(log, ('3.0: BelleTemple Earring IB Hash',)),               (add_ib_check_if_missing,)],
    'b946c37f': [(log, ('3.0: BelleBrillianceOfStars Tie IB Hash',)), (add_ib_check_if_missing,)],
'62711f82': [(log, ('3.0: BelleBrillianceOfStars Earrings IB Hash',)), (add_ib_check_if_missing,)],
'feb1c4cd': [(log, ('3.0: BelleBrillianceOfStars Body IB Hash',)), (add_ib_check_if_missing,)],
'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Player IB Hash',)), (add_ib_check_if_missing,)],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    'dcb8ba2e': [(log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    'feb1c4cd': [(log, ('3.0: BelleBrillianceOfStars Body IB Hash',)), (add_ib_check_if_missing,)],
'a318b3c6': [(log, ('3.0: BelleBrillianceOfStars Player IB Hash',)), (add_ib_check_if_missing,)],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'639ad374': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),],
    '860e1558': [(log, ('2.0 -> 2.1: BelleBrillianceOfStars Body IB Hash [Legacy]',)), (update_hash, ('d509bdd4',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleBrillianceOfStars',
    'game_versions': ['2.0', '2.1', '2.4', '2.5', '2.8', '3.0'],
}