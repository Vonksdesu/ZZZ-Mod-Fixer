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
    'd823ac80': [
        (log,                           ('3.0: JaneNocturne Face Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('3b75aa2c', 'JaneNocturne.HeadA.Diffuse.2048')),
    ],

# === Hair Textures ===
'f7ef1a53': [
        (log,                           ('3.0: JaneNocturne Hair Diffuse Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],
    'b33a9770': [
        (log,                           ('3.0: JaneNocturne Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('f7ef1a53', 'JaneNocturne.HairA.Diffuse.2048')),
    ],
    '9ec4cd4f': [
        (log,                           ('3.0: JaneNocturne Hair LightMap Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],
    '5e12acc1': [
        (log,                           ('3.0: JaneNocturne Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('9ec4cd4f', 'JaneNocturne.HairA.LightMap.2048')),
    ],
    '5e34e275': [
        (log,                           ('3.0: JaneNocturne Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('3275b812', 'JaneNocturne.Hair.IB', 'match_priority = 0\n')),
    ],
    '40fca454': [
        (log,                           ('3.0: JaneNocturne Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('5e34e275', 'JaneNocturne.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'a47bf333': [
        (log,                           ('2.8 -> 3.0: JaneNocturne Body Diffuse Hash [Legacy]',)),
        (update_hash,                   ('a47bf989',)),
    ],
'a47bf989': [
        (log,                           ('3.0: JaneNocturne Body Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],
'dd1b5520': [
        (log,                           ('3.0: JaneNocturne Body LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],
'389d9c67': [
        (log,                           ('3.0: JaneNocturne Body MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ac900322', 'JaneNocturne.Body.IB', 'match_priority = 0\n')),
    ],

# === Leg Ring Gemstone Textures ===
'e108fa5b': [
        (log,                           ('3.0: JaneNocturne Leg Ring Gemstone Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ca887a07', 'JaneNocturne.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],

# === Hand Knife Textures ===
'59c18114': [
        (log,                           ('3.0: JaneNocturne Hand Knife Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
    '0158a68f': [
        (log,                           ('3.0: JaneNocturne Hand Knife Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('59c18114', 'JaneNocturne.HandKnife.Diffuse.2048')),
    ],
    '76cda993': [
        (log,                           ('3.0: JaneNocturne Hand Knife LightMap 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
    '655a0c17': [
        (log,                           ('3.0: JaneNocturne Hand Knife LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('76cda993', 'JaneNocturne.HandKnife.LightMap.2048')),
    ],
    'd83ad325': [
        (log,                           ('3.0: JaneNocturne Hand Knife MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'JaneNocturne.HandKnife.IB', 'match_priority = 0\n')),
    ],
    'f9f30a0e': [
        (log,                           ('3.0: JaneNocturne Hand Knife MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d83ad325', 'JaneNocturne.HandKnife.MaterialMap.2048')),
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
        (multiply_section_if_missing,   ('be442045', 'JaneDoeNocturneOfLight.BodyA.Diffuse.1024')),
    ],
    'be442045': [
        (log,                           ('1.1: JaneSkin BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a47bf989', 'JaneDoeNocturneOfLight.BodyA.Diffuse.2048')),
    ],
    'dd1b5520': [
        (log,                           ('1.1: JaneSkin BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('f655d62e', 'JaneDoeNocturneOfLight.BodyA.LightMap.1024')),
    ],
    'f655d62e': [
        (log,                           ('1.1: JaneSkin BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('dd1b5520', 'JaneDoeNocturneOfLight.BodyA.LightMap.2048')),
    ],
    '389d9c67': [
        (log,                           ('1.1: JaneSkin BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('13eafbbd', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.1024')),
    ],
    '13eafbbd': [
        (log,                           ('1.1: JaneSkin BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('389d9c67', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.2048')),
    ],

# === Legacy Hash Updates ===
'9268a5af': [(log, ('2.4 -> 2.5: JaneNocturne Hair IB Hash [Legacy]',)), (update_hash, ('3275b812',))],
'2d06e785': [(log, ('2.4 -> 2.5: JaneNocturne Hair Draw Hash [Legacy]',)), (update_hash, ('74bc0b7f',))],
'e7a3b7dc': [(log, ('2.4 -> 2.5: JaneNocturne Hair Position Hash [Legacy]',)), (update_hash, ('33a09cfe',))],
'acec29f8': [(log, ('2.4 -> 2.5: JaneNocturne Hair Texcoord Hash [Legacy]',)), (update_hash, ('fa617c9a',))],
'8721477f': [(log, ('2.4 -> 2.5: JaneNocturne Hair Blend Hash [Legacy]',)), (update_hash, ('e42171df',))],
'9f2f7c53': [(log, ('2.4 -> 2.5: JaneNocturne Head Texcoord Hash [Legacy]',)), (update_hash, ('1fa404c1',))],
'850d4cbf': [(log, ('2.1 -> 2.2: JaneNocturne Face Position Hash [Legacy]',)), (update_hash, ('eace2dfa',))],
'eace2dfa': [(log, ('2.2: JaneNocturne Face Position Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
'7fd655de': [(log, ('2.1 -> 2.2: JaneNocturne Face Texcoord Hash [Legacy]',)), (update_hash, ('535e2453',))],
'535e2453': [(log, ('2.2: JaneNocturne Face Texcoord Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
'a14461d9': [(log, ('2.1 -> 2.2: JaneNocturne Face Blend Hash [Legacy]',)), (update_hash, ('7310ad6a',))],
'7310ad6a': [(log, ('2.2: JaneNocturne Face Blend Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoeNocturneOfLight',
    'game_versions': ['2.8', '3.0'],
}