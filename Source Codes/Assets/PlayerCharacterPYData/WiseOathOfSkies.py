"""
WiseOathOfSkies Character Hash Commands
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
    Returns WiseOathOfSkies's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'1fdaf388': [(log, ('3.0: WiseOathOfSkies Face IB Hash',)),                 (add_ib_check_if_missing,)],
# === IB Hashes (Wiseswimwear v2.0 Historical) ===

# === VB Hashes ===
# Body
'164b2ccb': [(log, ('3.0: WiseOathOfSkies Body draw_vb',)),                 (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'4dcfe033': [(log, ('3.0: WiseOathOfSkies Body position_vb',)),             (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'0c2cc3dd': [(log, ('3.0: WiseOathOfSkies Body texcoord_vb',)),             (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],
'8bab814c': [(log, ('3.0: WiseOathOfSkies Body blend_vb',)),                (add_section_if_missing, ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n'))],

# Neck
'c4a1fb46': [(log, ('3.0: WiseOathOfSkies Neck draw_vb',)),                 (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'6171b974': [(log, ('3.0: WiseOathOfSkies Neck position_vb',)),             (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'0da56abf': [(log, ('3.0: WiseOathOfSkies Neck texcoord_vb',)),             (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],
'98a06e7d': [(log, ('3.0: WiseOathOfSkies Neck blend_vb',)),                (add_section_if_missing, ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n'))],

# Tie
'86f21a82': [(log, ('3.0: WiseOathOfSkies Tie draw_vb',)),                  (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'fb0a401a': [(log, ('3.0: WiseOathOfSkies Tie position_vb',)),              (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'052d4b48': [(log, ('3.0: WiseOathOfSkies Tie texcoord_vb',)),              (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],
'4b19b5b5': [(log, ('3.0: WiseOathOfSkies Tie blend_vb',)),                 (add_section_if_missing, ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n'))],

# Hair
'ef9c0510': [(log, ('3.0: WiseOathOfSkies Hair draw_vb',)),                 (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'e8df7ff3': [(log, ('3.0: WiseOathOfSkies Hair position_vb',)),             (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'774071dd': [(log, ('3.0: WiseOathOfSkies Hair texcoord_vb',)),             (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],
'68e4f572': [(log, ('3.0: WiseOathOfSkies Hair blend_vb',)),                (add_section_if_missing, ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n'))],

# Face
'6c4552bb': [(log, ('3.0: WiseOathOfSkies Face VertexLimit',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('3.0: WiseOathOfSkies Face position_vb',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('3.0: WiseOathOfSkies Face texcoord_vb',)),             (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],
'015fbf96': [(log, ('3.0: WiseOathOfSkies Face blend_vb',)),                (add_section_if_missing, ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n'))],

# === Face Textures ===
'5d75fddc': [
        (log,                           ('3.0: WiseOathOfSkies Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
    ],


# === Hair Textures ===
'28005a5b': [
        (log,                           ('3.0: WiseOathOfSkies Hair Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('3.0: WiseOathOfSkies Hair LightMap 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('3.0: WiseOathOfSkies Hair MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
    ],


# === Legacy 2.0-2.8 Hash Updates ===
'f6cac296': [(log, ('2.0 -> 2.8: WiseOathOfSkies IB Hash [Legacy]',)), (update_hash, ('d5ca0411',))],
'ba59bf09': [(log, ('2.0 -> 2.8: Wise Hair draw_vb Hash [Legacy]',)), (update_hash, ('ef9c0510',))],
'6235fa7f': [(log, ('2.0 -> 2.8: Wise Hair position_vb Hash [Legacy]',)), (update_hash, ('e8df7ff3',))],
'fe89498c': [(log, ('2.0 -> 2.8: Wise Hair texcoord_vb Hash [Legacy]',)), (update_hash, ('774071dd',))],
'1273c7b0': [(log, ('2.0 -> 2.8: Wise Hair blend_vb Hash [Legacy]',)), (update_hash, ('edfd1666',))],
'83e07a1b': [(log, ('2.7 -> 2.8: Wise HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'af5fc216': [(log, ('2.7 -> 2.8: Wise HairShadow draw_vb Hash [Legacy]',)), (update_hash, ('681651f9',))],
'1a438b0d': [(log, ('2.7 -> 2.8: Wise HairShadow position_vb Hash [Legacy]',)), (update_hash, ('4af493e5',))],
'7b7957fa': [(log, ('2.7 -> 2.8: Wise HairShadow texcoord_vb Hash [Legacy]',)), (update_hash, ('ad7d7eca',))],
'52bd07dd': [(log, ('2.7 -> 2.8: Wise HairShadow blend_vb Hash [Legacy]',)), (update_hash, ('795e9a7c',))],
'edfd1666': [(log, ('2.7 -> 2.8: Wise Hair blend_vb Hash [Legacy]',)), (update_hash, ('68e4f572',))],
'757bc7cc': [(log, ('2.7 -> 2.8: Wise Face blend_vb Hash [Legacy]',)), (update_hash, ('015fbf96',))],
'3f771e63': [(log, ('2.8 -> 3.0: WiseSwimwear HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'ebe9f31b': [(log, ('2.0 -> 2.1: Wise Head Texcoord Hash [Legacy]',)), (update_hash, ('c83b6cbf',))],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: WiseOathOfSkies Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8d08b190', 'WiseOathOfSkies.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: WiseOathOfSkies Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8d08b190', 'WiseOathOfSkies.HairShadow.IB', 'match_priority = 0\n')),
    ],
    '8d08b190': [(log, ('2.8: WiseTemple HairShadow IB Hash',)),            (add_ib_check_if_missing,)],
'eeabff55': [(log, ('2.8: WiseTemple Torso Ribbon IB Hash',)),          (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: WiseTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'e5f8b021': [(log, ('2.8: WiseTemple Black Orange Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'e5f269f4': [(log, ('2.8: WiseTemple Orange Green Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'bfce3c18': [(log, ('2.8: WiseTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],
'b856d397': [(log, ('2.8: WiseTemple Earrings IB Hash',)),               (add_ib_check_if_missing,)],
'd0e278fc': [(log, ('2.8: WiseTemple CatEar IB Hash',)),                 (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: WiseTemple TorsoAcc IB Hash',)),               (add_ib_check_if_missing,)],
    'd5ca0411': [(log, ('2.8: WiseTemple Hair IB Hash',)),                  (add_ib_check_if_missing,)],
'e7f527ea': [(log, ('2.8: WiseTemple DiskPlayer IB Hash',)),             (add_ib_check_if_missing,)],
'8d08b190': [(log, ('2.8: WiseTemple HairShadow IB Hash',)),            (add_ib_check_if_missing,)],
'eeabff55': [(log, ('2.8: WiseTemple Torso Ribbon IB Hash',)),          (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: WiseTemple Panda Headgear IB Hash',)),        (add_ib_check_if_missing,)],
'e5f8b021': [(log, ('2.8: WiseTemple Black Orange Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'e5f269f4': [(log, ('2.8: WiseTemple Orange Green Ribbon IB Hash',)),   (add_ib_check_if_missing,)],
'bfce3c18': [(log, ('2.8: WiseTemple Glasses IB Hash',)),               (add_ib_check_if_missing,)],
'b856d397': [(log, ('2.8: WiseTemple Earrings IB Hash',)),               (add_ib_check_if_missing,)],
'd0e278fc': [(log, ('2.8: WiseTemple CatEar IB Hash',)),                 (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.8: WiseTemple TorsoAcc IB Hash',)),               (add_ib_check_if_missing,)],
    '1024352b': [(log,                           ('3.0: WiseOathOfSkies TieA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('dd08a467', 'WiseSchoolUniform.TieA.Diffuse.1024')),],
    '22fe3236': [(log, ('3.0: WiseOathOfSkies Body IB Hash',)), (add_ib_check_if_missing,)],
    '4d7473b1': [(log,                           ('3.0: WiseOathOfSkies BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('31707abe', 'WiseSchoolUniform.BodyA.MaterialMap.1024')),],
    '6649f407': [(log,                           ('3.0: WiseOathOfSkies TieA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('ba59a4d0', 'WiseSchoolUniform.TieA.MaterialMap.1024')),],
    '8a1ec07e': [(log, ('3.0: WiseOathOfSkies Neck IB Hash',)), (add_ib_check_if_missing,)],
    'b9dcce2e': [(log,                           ('3.0: WiseOathOfSkies BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('a0a4c84e', 'WiseSchoolUniform.BodyA.Diffuse.1024')),],
    'bd86c7c4': [(log,                           ('3.0: WiseOathOfSkies BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8d09dc95', 'WiseSchoolUniform.BodyA.LightMap.1024')),],
    'e550cd81': [(log,                           ('3.0: WiseOathOfSkies TieA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('4f211318', 'WiseSchoolUniform.TieA.LightMap.1024')),],
    'f21a2bac': [(log, ('3.0: WiseOathOfSkies Tie IB Hash',)), (add_ib_check_if_missing,)],
    '31707abe': [(log,                           ('3.0: WiseOathOfSkies BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('4d7473b1', 'WiseSchoolUniform.BodyA.MaterialMap.2048')),],
    '33368e12': [(log,                           ('2.0: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8d8269f8', '1f21c633'), 'WiseOathOfSkies.HairA.LightMap.2048')),],
    '4f211318': [(log,                           ('3.0: WiseOathOfSkies TieA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e550cd81', 'WiseSchoolUniform.TieA.LightMap.2048')),],
    '588d7d2d': [(log,                           ('1.1: Wise HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4894246e', 'WiseOathOfSkies.Head.IB', 'match_priority = 0\n')),],
    '8d09dc95': [(log,                           ('3.0: WiseOathOfSkies BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('bd86c7c4', 'WiseSchoolUniform.BodyA.LightMap.2048')),],
    'a0a4c84e': [(log,                           ('3.0: WiseOathOfSkies BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('b9dcce2e', 'WiseSchoolUniform.BodyA.Diffuse.2048')),],
    'ba59a4d0': [(log,                           ('3.0: WiseOathOfSkies TieA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('6649f407', 'WiseSchoolUniform.TieA.MaterialMap.2048')),],
    'cb0d0c22': [(log,                           ('1.0: Wise HairA, BagA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'WiseOathOfSkies.Bag.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('28005a5b', 'WiseOathOfSkies.HairA.Diffuse.2048')),],
    'd9383a15': [(log,                           ('2.0: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('f1b20f3d', '473f816d'), 'WiseOathOfSkies.HairA.MaterialMap.2048')),],
    'dd08a467': [(log,                           ('3.0: WiseOathOfSkies TieA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('1024352b', 'WiseSchoolUniform.TieA.Diffuse.2048')),],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseOathOfSkies',
    'game_versions': ['3.0'],
}