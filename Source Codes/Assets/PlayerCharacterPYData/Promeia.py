"""
Promeia Character Hash Commands
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
    Returns Promeia's hash commands dictionary.
    """
    return {
# === IB Hashes ===
    '6cca89ab': [(log, ('2.8 -> 2.81: Promeia Boots Texcoord Hash',)), (update_hash, ('31178971',))],
'31178971': [(log, ('2.8: Promeia Hair IB Hash',)),            (add_ib_check_if_missing,)],
    'de6eb63b': [(log, ('2.8 -> 2.81: Promeia Cloak LightMap Hash',)), (update_hash, ('ff223b2c',))],
'ff223b2c': [(log, ('2.8: Promeia HairShadow IB Hash',)),      (add_ib_check_if_missing,)],
    'cb9d17fc': [(log, ('2.8 -> 2.81: Promeia Back Hair MaterialMap Hash',)), (update_hash, ('e032287a',))],
'e032287a': [(log, ('2.8: Promeia Eyebrow IB Hash',)),         (add_ib_check_if_missing,)],
    '5ea47a32': [(log, ('2.8 -> 2.81: Promeia Cloak Texcoord Hash',)), (update_hash, ('ef3c4506',))],
'ef3c4506': [(log, ('2.8: Promeia Face IB Hash',)),            (add_ib_check_if_missing,)],
    '947ceb88': [(log, ('2.8 -> 2.81: Promeia Boots LightMap Hash',)), (update_hash, ('8995db58',))],
'8995db58': [(log, ('2.8: Promeia Weapon IB Hash',)),          (add_ib_check_if_missing,)],

# === IB Hashes (2.8 -> 3.0 Transition) ===
    'a633d5b7': [(log, ('2.8 -> 2.81: Promeia Back Hair Blend Hash',)), (update_hash, ('36e794ea',))],
'36e794ea': [(log, ('2.8 -> 3.0: Promeia BodyPinioned IB Hash [Legacy]',)), (update_hash, ('b386901d',))],
    '6abaa60a': [(log, ('2.8 -> 2.81: Promeia Back Hair Texcoord Hash',)), (update_hash, ('62a6b4bd',))],
'62a6b4bd': [(log, ('2.8 -> 3.0: Promeia BodyNormal IB Hash [Legacy]',)),   (update_hash, ('10c77d62',))],
    '68f34958': [(log, ('2.8 -> 2.81: Promeia Leg IB Hash',)), (update_hash, ('93f1f568',))],
'93f1f568': [(log, ('2.8 -> 3.0: Promeia Clothes IB Hash [Legacy]',)),      (update_hash, ('0ae14c24',))],
    '21871660': [(log, ('2.8 -> 2.81: Promeia Leg IB Hash',)), (update_hash, ('fd054d1d',))],
'fd054d1d': [(log, ('2.8 -> 3.0: Promeia Leg IB Hash [Legacy]',)),          (update_hash, ('ec003379',))],

# === IB Hashes (v3.0 Target) ===
'b386901d': [(log, ('3.0: Promeia CloakChest IB Hash',)),            (add_ib_check_if_missing,)],
'10c77d62': [(log, ('3.0: Promeia Chest IB Hash',)),                 (add_ib_check_if_missing,)],
'0ae14c24': [(log, ('3.0: Promeia Cloak IB Hash',)),                 (add_ib_check_if_missing,)],
'ec003379': [(log, ('3.0: Promeia Legs IB Hash',)),                  (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'2d4c7c18': [(log, ('2.8: Promeia Hair draw_vb Hash',)),                 (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
    '35096cb6': [(log, ('2.8 -> 2.81: Promeia Cloak Position Hash',)), (update_hash, ('681aceaa',))],
'681aceaa': [(log, ('2.8: Promeia Hair position_vb Hash',)),             (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
    '9c0aad96': [(log, ('2.8 -> 2.81: Promeia Leg MaterialMap Hash',)), (update_hash, ('84d40d91',))],
'84d40d91': [(log, ('2.8: Promeia Hair texcoord_vb Hash',)),             (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],
    '5a263750': [(log, ('2.8 -> 2.81: Promeia Cloak Blend Hash',)), (update_hash, ('3d4a4881',))],
'3d4a4881': [(log, ('2.8: Promeia Hair blend_vb Hash',)),                (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n'))],

# Body - Pinioned State (BodyPinioned) -> CloakChest (3.0)
'19ad87f6': [(log, ('2.8 -> 3.0: Promeia BodyPinioned draw_vb Hash [Legacy]',)),     (update_hash, ('dd86f5ae',))],
    'a7769c93': [(log, ('2.8 -> 2.81: Promeia Boots Blend Hash',)), (update_hash, ('ffaa183a',))],
'ffaa183a': [(log, ('2.8 -> 3.0: Promeia BodyPinioned position_vb Hash [Legacy]',)), (update_hash, ('68e2baef',))],
    'bfcfb2f7': [(log, ('2.8 -> 2.81: Promeia Leg Blend Hash',)), (update_hash, ('2a9842a1',))],
'2a9842a1': [(log, ('2.8 -> 3.0: Promeia BodyPinioned texcoord_vb Hash [Legacy]',)), (update_hash, ('6fe5f8c1',))],
    '61c399b6': [(log, ('2.8 -> 2.81: Promeia Weapon IB Hash',)), (update_hash, ('dae4abd0',))],
'dae4abd0': [(log, ('2.8 -> 3.0: Promeia BodyPinioned blend_vb Hash [Legacy]',)),    (update_hash, ('112582ea',))],

# Body - Normal State (BodyNormal) -> Chest (3.0)
'9cce6ba2': [
        (log,                           ('2.8 -> 3.0: Promeia BodyNormal / Chest draw_vb Hash',)),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
    ],
'bf938187': [(log, ('2.8 -> 3.0: Promeia BodyNormal position_vb Hash [Legacy]',)),   (update_hash, ('2dbfe8c9',))],
    'b1ec331c': [(log, ('2.8 -> 2.81: Promeia Back Hair IB Hash',)), (update_hash, ('d99d21e0',))],
'd99d21e0': [(log, ('2.8 -> 3.0: Promeia BodyNormal texcoord_vb Hash [Legacy]',)),   (update_hash, ('1fc95f5b',))],
    'bca960d0': [(log, ('2.8 -> 2.81: Promeia Back Hair LightMap Hash',)), (update_hash, ('575d8b1b',))],
'575d8b1b': [(log, ('2.8 -> 3.0: Promeia BodyNormal blend_vb Hash [Legacy]',)),      (update_hash, ('ee35cc06',))],

# Clothes -> Cloak (3.0)
'947f29ae': [
        (log,                           ('2.8 -> 3.0: Promeia Clothes / Cloak draw_vb Hash',)),
        (add_section_if_missing,        ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
    'd43597aa': [(log, ('2.8 -> 2.81: Promeia Boots IB Hash',)), (update_hash, ('1d63183b',))],
'1d63183b': [(log, ('2.8 -> 3.0: Promeia Clothes position_vb Hash [Legacy]',)),      (update_hash, ('f6cc27b6',))],
    '9f083955': [(log, ('2.8 -> 2.81: Promeia Boots MaterialMap Hash',)), (update_hash, ('826446a7',))],
'826446a7': [(log, ('2.8 -> 3.0: Promeia Clothes texcoord_vb Hash [Legacy]',)),      (update_hash, ('bf00cc95',))],
    '870f56b5': [(log, ('2.8 -> 2.81: Promeia Weapon LightMap Hash',)), (update_hash, ('58f42be3',))],
'58f42be3': [(log, ('2.8 -> 3.0: Promeia Clothes blend_vb Hash [Legacy]',)),         (update_hash, ('4b0d6867',))],

# Leg -> Legs (3.0)
'dfb01010': [
        (log,                           ('2.8 -> 3.0: Promeia Leg / Legs draw_vb Hash',)),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
    '595bd76e': [(log, ('2.8 -> 2.81: Promeia Leg Position Hash',)), (update_hash, ('0b822797',))],
'0b822797': [(log, ('2.8 -> 3.0: Promeia Leg position_vb Hash [Legacy]',)),          (update_hash, ('4c1d0a70',))],
    '2918714e': [(log, ('2.8 -> 2.81: Promeia Leg Texcoord Hash',)), (update_hash, ('f5fd0e92',))],
'f5fd0e92': [(log, ('2.8 -> 3.0: Promeia Leg texcoord_vb Hash [Legacy]',)),          (update_hash, ('03d6f933',))],
    'fd3c3d9f': [(log, ('2.8 -> 2.81: Promeia Leg LightMap Hash',)), (update_hash, ('9839b071',))],
'9839b071': [(log, ('2.8 -> 3.0: Promeia Leg blend_vb Hash [Legacy]',)),             (update_hash, ('65bba179',))],

# Eyebrow
'a1d5b256': [(log, ('2.8: Promeia Eyebrow draw_vb Hash',)),              (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
'9bc72111': [(log, ('2.8: Promeia Eyebrow position_vb Hash',)),          (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
    '3a00aa76': [(log, ('2.8 -> 2.81: Promeia Cloak Draw Hash',)), (update_hash, ('d3d65ca5',))],
'd3d65ca5': [(log, ('2.8: Promeia Eyebrow texcoord_vb Hash',)),          (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],
'42594132': [(log, ('2.8: Promeia Eyebrow blend_vb Hash',)),             (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'32a38de6': [(log, ('2.8: Promeia Face draw_vb Hash',)),                 (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
'08b11ea1': [(log, ('2.8: Promeia Face position_vb Hash',)),             (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
    'b7a6479f': [(log, ('2.8 -> 2.81: Promeia Cloak IB Hash',)), (update_hash, ('dcd61276',))],
'dcd61276': [(log, ('2.8: Promeia Face texcoord_vb Hash',)),             (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],
    '5ff41c34': [(log, ('2.8 -> 2.81: Promeia Back Hair Position Hash',)), (update_hash, ('bf5b785d',))],
'bf5b785d': [(log, ('2.8: Promeia Face blend_vb Hash',)),                (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n'))],

# Weapon - Ring Blade
    '7d76d686': [(log, ('2.8 -> 2.81: Promeia Cloak MaterialMap Hash',)), (update_hash, ('0a06059e',))],
'0a06059e': [(log, ('2.8: Promeia Weapon draw_vb Hash',)),               (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
'35ecba91': [(log, ('3.0: Promeia Weapon position_vb',)),             (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
    '2f3a560d': [(log, ('2.8 -> 2.81: Promeia Weapon Position Hash',)), (update_hash, ('d242b77a',))],
'd242b77a': [(log, ('2.8 -> 3.0: Promeia Weapon position_vb Hash [Legacy]',)), (update_hash, ('35ecba91',))],
'064658e2': [(log, ('3.0: Promeia Weapon texcoord_vb',)),             (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],
    '23587131': [(log, ('2.8 -> 2.81: Promeia Weapon Texcoord Hash',)), (update_hash, ('f2f5bd28',))],
'f2f5bd28': [(log, ('2.8 -> 3.0: Promeia Weapon texcoord_vb Hash [Legacy]',)), (update_hash, ('064658e2',))],
    '21ac80fa': [(log, ('2.8 -> 2.81: Promeia Weapon Blend Hash',)), (update_hash, ('a864dc82',))],
'a864dc82': [(log, ('2.8: Promeia Weapon blend_vb Hash',)),              (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n'))],

# === Legacy Hash Updates (2.0 -> 2.8) ===
'328fa0cf': [(log, ('2.0 -> 2.8: Promeia Face/Eyebrow Diffuse [Legacy]',)), (update_hash, ('9b293811',))],
'a0add414': [(log, ('2.0 -> 2.8: Promeia Hair Diffuse [Legacy]',)),        (update_hash, ('c96de436',))],
'5c509f54': [(log, ('2.0 -> 2.8: Promeia Hair LightMap [Legacy]',)),       (update_hash, ('e34356a6',))],
'1f96c5d7': [(log, ('2.0 -> 2.8: Promeia Hair MaterialMap [Legacy]',)),    (update_hash, ('6bed1450',))],
'7d2d3a9e': [(log, ('2.0 -> 2.8: Promeia Body/Leg Diffuse [Legacy]',)),    (update_hash, ('ae109401',))],
'70ca6de8': [(log, ('2.0 -> 2.8: Promeia Body/Leg LightMap [Legacy]',)),   (update_hash, ('3864f20c',))],
'af976ad8': [(log, ('2.0 -> 2.8: Promeia Body/Leg MaterialMap [Legacy]',)), (update_hash, ('d57df6aa',))],

# === Texture Transitions: 1024p (2.0 -> 2.8 -> 3.0) — FIXED: now targets 1024p, not 2048p ===
# Clothes Textures 1024p
'406b1373': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Clothes Diffuse1024 Hash [Legacy]',)), (update_hash, ('47d294f4',))],
'044d2d39': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Clothes LightMap1024 Hash [Legacy]',)), (update_hash, ('562616d5',))],
'01a5ba27': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Clothes MaterialMap1024 Hash [Legacy]',)), (update_hash, ('73aaae54',))],

# Weapon Textures 1024p
'138bcaa1': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Weapon Diffuse1024 Hash [Legacy]',)), (update_hash, ('7750fc88',))],
'5e59380e': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Weapon LightMap1024 Hash [Legacy]',)), (update_hash, ('a1988612',))],
'09271c02': [(log, ('2.0 -> 2.8 -> 3.0: Promeia Weapon MaterialMap1024 Hash [Legacy]',)), (update_hash, ('7559d574',))],

# === Texture Transitions: 2048p (2.8 -> 3.0) ===
# Clothes Textures 2048p
'b9367016': [(log, ('2.8 -> 3.0: Promeia Clothes Diffuse2048 Hash [Legacy]',)), (update_hash, ('e1492a53',))],
'd743acd0': [(log, ('2.8 -> 3.0: Promeia Clothes LightMap2048 Hash [Legacy]',)), (update_hash, ('9bf7f5cc',))],
'31d7cbad': [(log, ('2.8 -> 3.0: Promeia Clothes MaterialMap2048 Hash [Legacy]',)), (update_hash, ('d37b40a9',))],

# === Shared Normal Map ===
'ebac056e': [(log, ('2.8: Promeia Shared NormalMap [Legacy]',)),           (update_hash, ('798adba3',))],
'798adba3': [
        (log,                           ('2.8 -> 3.0: Promeia Shared NormalMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],

# === 3.0 Database Updates (Strict Sync) ===
# CloakChest VBs (from BodyPinioned)
'dd86f5ae': [(log, ('3.0: Promeia CloakChest draw_vb',)),            (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'68e2baef': [(log, ('3.0: Promeia CloakChest position_vb',)),        (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'6fe5f8c1': [(log, ('3.0: Promeia CloakChest texcoord_vb',)),        (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],
'112582ea': [(log, ('3.0: Promeia CloakChest blend_vb',)),           (add_section_if_missing, ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n'))],

# Chest VBs (from BodyNormal)
'2dbfe8c9': [(log, ('3.0: Promeia Chest position_vb',)),             (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],
'1fc95f5b': [(log, ('3.0: Promeia Chest texcoord_vb',)),             (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],
'ee35cc06': [(log, ('3.0: Promeia Chest blend_vb',)),                (add_section_if_missing, ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n'))],

# Cloak VBs (from Clothes)
'f6cc27b6': [(log, ('3.0: Promeia Cloak position_vb',)),             (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],
'bf00cc95': [(log, ('3.0: Promeia Cloak texcoord_vb',)),             (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],
'4b0d6867': [(log, ('3.0: Promeia Cloak blend_vb',)),                (add_section_if_missing, ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n'))],

# Legs VBs (from Leg)
'4c1d0a70': [(log, ('3.0: Promeia Legs position_vb',)),             (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],
'03d6f933': [(log, ('3.0: Promeia Legs texcoord_vb',)),             (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],
'65bba179': [(log, ('3.0: Promeia Legs blend_vb',)),                (add_section_if_missing, ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n'))],

# === Face & Eyebrow Textures (v2.8 Target) ===
'9b293811': [
        (log,                           ('2.8: Promeia FaceA, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures (v2.8 Target) ===
'c96de436': [
        (log,                           ('2.8: Promeia HairA Diffuse Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'e34356a6': [
        (log,                           ('2.8: Promeia HairA LightMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'6bed1450': [
        (log,                           ('2.8: Promeia HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body (Pinioned & Normal) & Leg Shared Textures (v2.8 Target) ===
'ae109401': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg Diffuse Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
'3864f20c': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg LightMap Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],
'd57df6aa': [
        (log,                           ('2.8 -> 3.0: Promeia Body, Leg MaterialMap Hash',)),
        (add_section_if_missing,        ('36e794ea', 'Promeia.BodyPinioned.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('62a6b4bd', 'Promeia.BodyNormal.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b386901d', 'Promeia.CloakChest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('10c77d62', 'Promeia.Chest.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec003379', 'Promeia.Legs.IB', 'match_priority = 0\n')),
    ],

# === Cloak Textures (v3.0 Target from Clothes 2048p) ===
'e1492a53': [
        (log,                           ('3.0: Promeia Cloak Diffuse Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
'9bf7f5cc': [
        (log,                           ('3.0: Promeia Cloak LightMap Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],
'd37b40a9': [
        (log,                           ('3.0: Promeia Cloak MaterialMap Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
    ],

# === Clothes 1024p Textures (v3.0 Target) ===
'47d294f4': [
        (log,                           ('3.0: Promeia Cloak Diffuse1024 Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('e1492a53', 'b9367016'), 'Promeia.CloakA.Diffuse.2048')),
    ],
'562616d5': [
        (log,                           ('3.0: Promeia Cloak LightMap1024 Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('9bf7f5cc', 'd743acd0'), 'Promeia.CloakA.LightMap.2048')),
    ],
'73aaae54': [
        (log,                           ('3.0: Promeia Cloak MaterialMap1024 Hash',)),
        (add_section_if_missing,        ('0ae14c24', 'Promeia.Cloak.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d37b40a9', '31d7cbad'), 'Promeia.CloakA.MaterialMap.2048')),
    ],

# === Weapon Textures (v2.8 Target) ===
'328135c5': [
        (log,                           ('3.0: Promeia Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'd1399215': [
        (log,                           ('2.8 -> 3.0: Promeia Weapon Diffuse Hash [Legacy]',)),
        (update_hash,                   ('328135c5',)),
    ],
'82f4146a': [
        (log,                           ('3.0: Promeia Weapon LightMap Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'369f0efd': [
        (log,                           ('2.8 -> 3.0: Promeia Weapon LightMap Hash [Legacy]',)),
        (update_hash,                   ('82f4146a',)),
    ],
'd672b87c': [
        (log,                           ('3.0: Promeia Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'a179a69c': [
        (log,                           ('2.8 -> 3.0: Promeia Weapon MaterialMap Hash [Legacy]',)),
        (update_hash,                   ('d672b87c',)),
    ],

# === Weapon 1024p Textures (v3.0 Target) ===
'7750fc88': [
        (log,                           ('3.0: Promeia Weapon Diffuse1024 Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('328135c5', 'd1399215'), 'Promeia.WeaponA.Diffuse.2048')),
    ],
'a1988612': [
        (log,                           ('3.0: Promeia Weapon LightMap1024 Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('82f4146a', '369f0efd'), 'Promeia.WeaponA.LightMap.2048')),
    ],
'7559d574': [
        (log,                           ('3.0: Promeia Weapon MaterialMap1024 Hash',)),
        (add_section_if_missing,        ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d672b87c', 'a179a69c'), 'Promeia.WeaponA.MaterialMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Promeia',
    'game_versions': ['2.0', '2.8', '3.0'],
}