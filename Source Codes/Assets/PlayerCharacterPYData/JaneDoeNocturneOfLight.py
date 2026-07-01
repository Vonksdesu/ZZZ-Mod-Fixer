"""
JaneDoeNocturneOfLight Character Hash Commands
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
    Returns JaneDoeNocturneOfLight's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'3275b812': [(log, ('3.0: JaneNocturne Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'27805144': [(log, ('3.0: JaneNocturne HairShadow IB Hash',)),            (add_ib_check_if_missing,)],
'ac900322': [(log, ('3.0: JaneNocturne Body IB Hash',)),                  (add_ib_check_if_missing,)],
'ca887a07': [(log, ('3.0: JaneNocturne LegRingGemstone IB Hash',)),       (add_ib_check_if_missing,)],
'ef86fc9f': [(log, ('3.0: JaneNocturne Face IB Hash',)),                  (add_ib_check_if_missing,)],
'602c545a': [(log, ('3.0: JaneNocturne HandKnife IB Hash',)),             (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'74bc0b7f': [(log, ('3.0: JaneNocturne Hair draw_vb',)),                  (add_section_if_missing, ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n'))],
'33a09cfe': [(log, ('3.0: JaneNocturne Hair position_vb',)),              (add_section_if_missing, ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n'))],
'fa617c9a': [(log, ('3.0: JaneNocturne Hair texcoord_vb',)),              (add_section_if_missing, ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n'))],
'e42171df': [
        (log,                           ('3.0: JaneNocturne Hair blend_vb',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
        (log,                           ('+ Remapping hair blend indices (Jane 2.5+ bone fix)',)),
        (update_buffer_blend_indices,   (
            'e42171df',
            (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126),
            (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 18, 22, 23, 24, 25, 26, 27, 28, 21, 29, 30, 31, 33, 34, 32, 36, 37, 35, 38, 39, 40, 41, 42, 44, 45, 46, 48, 47, 43, 49, 52, 53, 54, 55, 50, 51, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68),
        )),
    ],

# Hair Shadow
'759a4b9f': [(log, ('3.0: JaneNocturne HairShadow draw_vb',)),            (add_section_if_missing, ('27805144', 'JaneNocturne.HairShadow.IB', 'match_priority = 0\n'))],
'7c08cd53': [(log, ('3.0: JaneNocturne HairShadow position_vb',)),        (add_section_if_missing, ('27805144', 'JaneNocturne.HairShadow.IB', 'match_priority = 0\n'))],
'93c5b49a': [(log, ('3.0: JaneNocturne HairShadow texcoord_vb',)),        (add_section_if_missing, ('27805144', 'JaneNocturne.HairShadow.IB', 'match_priority = 0\n'))],
'6af472f5': [(log, ('3.0: JaneNocturne HairShadow blend_vb',)),           (add_section_if_missing, ('27805144', 'JaneNocturne.HairShadow.IB', 'match_priority = 0\n'))],

# Body
'3f009560': [(log, ('3.0: JaneNocturne Body draw_vb',)),                  (add_section_if_missing, ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n'))],
'4544dca7': [(log, ('3.0: JaneNocturne Body position_vb',)),              (add_section_if_missing, ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n'))],
'6845e991': [(log, ('3.0: JaneNocturne Body texcoord_vb',)),              (add_section_if_missing, ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n'))],
'44071a5e': [(log, ('3.0: JaneNocturne Body blend_vb',)),                 (add_section_if_missing, ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n'))],

# Leg Ring Gemstone
'65c0f994': [(log, ('3.0: JaneNocturne LegRingGemstone draw_vb',)),       (add_section_if_missing, ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n'))],
'ad125746': [(log, ('3.0: JaneNocturne LegRingGemstone position_vb',)),   (add_section_if_missing, ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n'))],
'7c6a8591': [(log, ('3.0: JaneNocturne LegRingGemstone texcoord_vb',)),   (add_section_if_missing, ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n'))],
'370c397a': [(log, ('3.0: JaneNocturne LegRingGemstone blend_vb',)),      (add_section_if_missing, ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n'))],

# Face
'5661afc3': [(log, ('3.0: JaneNocturne Face VertexLimit',)),              (add_section_if_missing, ('ef86fc9f', 'JaneNocturne.Face.IB', 'match_priority = 0\n'))],
'6c733c84': [(log, ('3.0: JaneNocturne Face position_vb',)),              (add_section_if_missing, ('ef86fc9f', 'JaneNocturne.Face.IB', 'match_priority = 0\n'))],
'1fa404c1': [(log, ('3.0: JaneNocturne Face texcoord_vb',)),              (add_section_if_missing, ('ef86fc9f', 'JaneNocturne.Face.IB', 'match_priority = 0\n'))],
'91846a84': [(log, ('3.0: JaneNocturne Face blend_vb',)),                 (add_section_if_missing, ('ef86fc9f', 'JaneNocturne.Face.IB', 'match_priority = 0\n'))],

# Hand Knife
'be378e74': [(log, ('3.0: JaneNocturne Hand Knife VertexLimit',)),        (add_section_if_missing, ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'3b75aa2c': [
        (log,                           ('3.0: JaneNocturne Face Diffuse Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'JaneNocturne.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'f7ef1a53': [
        (log,                           ('3.0: JaneNocturne Hair Diffuse Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],
'9ec4cd4f': [
        (log,                           ('3.0: JaneNocturne Hair LightMap Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],
'5e34e275': [
        (log,                           ('3.0: JaneNocturne Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'a47bf333': [
        (log,                           ('2.8 -> 3.0: JaneNocturne Body Diffuse Hash [Legacy]',)),
        (update_hash,                   ('a47bf989',)),
    ],
'a47bf989': [
        (log,                           ('3.0: JaneNocturne Body Diffuse Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],
'dd1b5520': [
        (log,                           ('3.0: JaneNocturne Body LightMap Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],
'389d9c67': [
        (log,                           ('3.0: JaneNocturne Body MaterialMap Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],

# === Leg Ring Gemstone Textures ===
'e108fa5b': [
        (log,                           ('3.0: JaneNocturne Leg Ring Gemstone Diffuse Hash',)),
        (add_section_if_missing,        ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],

# === Hand Knife Textures ===
'59c18114': [
        (log,                           ('3.0: JaneNocturne Hand Knife Diffuse Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
'76cda993': [
        (log,                           ('3.0: JaneNocturne Hand Knife LightMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
'd83ad325': [
        (log,                           ('3.0: JaneNocturne Hand Knife MaterialMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: JaneNocturne Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
    'ebac056e': [
        (log,                           ('3.0: JaneNocturne Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],

# === Legacy BodyA Textures ===
    'a47bf989': [
        (log,                           ('1.1: JaneSkin BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('be442045', 'JaneSkin.BodyA.Diffuse.1024')),
    ],
    'be442045': [
        (log,                           ('1.1: JaneSkin BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a47bf989', 'JaneSkin.BodyA.Diffuse.2048')),
    ],
    'dd1b5520': [
        (log,                           ('1.1: JaneSkin BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('f655d62e', 'JaneSkin.BodyA.LightMap.1024')),
    ],
    'f655d62e': [
        (log,                           ('1.1: JaneSkin BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dd1b5520', 'JaneSkin.BodyA.LightMap.2048')),
    ],
    '389d9c67': [
        (log,                           ('1.1: JaneSkin BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('13eafbbd', 'JaneSkin.BodyA.MaterialMap.1024')),
    ],
    '13eafbbd': [
        (log,                           ('1.1: JaneSkin BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('389d9c67', 'JaneSkin.BodyA.MaterialMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoeNocturneOfLight',
    'game_versions': ['2.8', '3.0'],
}