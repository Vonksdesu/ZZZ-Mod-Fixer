"""
WiseTemple Character Hash Commands
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
    Returns WiseTemple's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01c42a1d': [(log, ('2.8: WiseTemple Neck IB Hash',)),                  (add_ib_check_if_missing,)],
'1eca2097': [(log, ('2.8: WiseTemple Body IB Hash',)),                  (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('2.8: WiseTemple Face IB Hash',)),                  (add_ib_check_if_missing,)],
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

# === VB Hashes ===
# Hair
'ef9c0510': [(log, ('2.8: WiseTemple Hair draw_vb',)),                  (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'e8df7ff3': [(log, ('2.8: WiseTemple Hair position_vb',)),              (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'774071dd': [(log, ('2.8: WiseTemple Hair texcoord_vb',)),              (add_section_if_missing, ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n'))],
'edfd1666': [(log, ('2.8 -> 3.0: WiseTemple Hair blend_vb Hash [Legacy]',)), (update_hash, ('68e4f572',))],

# Hair Shadow
'681651f9': [(log, ('2.8: WiseTemple HairShadow draw_vb',)),            (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'4af493e5': [(log, ('2.8: WiseTemple HairShadow position_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'ad7d7eca': [(log, ('2.8: WiseTemple HairShadow texcoord_vb',)),        (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],
'795e9a7c': [(log, ('2.8: WiseTemple HairShadow blend_vb',)),           (add_section_if_missing, ('8d08b190', 'WiseTemple.HairShadow.IB', 'match_priority = 0\n'))],

# Neck
'276e1373': [(log, ('2.8: WiseTemple Neck draw_vb',)),                  (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'd8ad824b': [(log, ('2.8: WiseTemple Neck position_vb',)),              (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'39a1dfe3': [(log, ('2.8: WiseTemple Neck texcoord_vb',)),              (add_section_if_missing, ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n'))],
'458bbde3': [(log, ('2.8 -> 3.0: WiseTemple Neck blend_vb Hash [Legacy]',)), (update_hash, ('e0b1e734',))],

# Body (WiseTemple Outfit)
'ca02f614': [(log, ('2.8: WiseTemple Body draw_vb',)),                  (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'a388eb6b': [(log, ('2.8: WiseTemple Body position_vb',)),              (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'b39870e1': [(log, ('2.8: WiseTemple Body texcoord_vb',)),              (add_section_if_missing, ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n'))],
'8612559a': [(log, ('2.8 -> 3.0: WiseTemple Body blend_vb Hash [Legacy]',)), (update_hash, ('f28a6363',))],

# WaistAccessories (DiskPlayer Acc)
'0c1c9bf3': [(log, ('2.8: WiseTemple WaistAccessories draw_vb',)),       (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'1e5cafee': [(log, ('2.8: WiseTemple WaistAccessories position_vb',)),   (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'06f42a6f': [(log, ('2.8: WiseTemple WaistAccessories texcoord_vb',)),   (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],
'0a0aa1a8': [(log, ('2.8: WiseTemple WaistAccessories blend_vb',)),      (add_section_if_missing, ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n'))],

# Face VBs & Limits
'6c4552bb': [(log, ('2.8: WiseTemple Face VertexLimit',)),              (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'5657c1fc': [(log, ('2.8: WiseTemple Face Position',)),                 (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'c83b6cbf': [(log, ('2.8: WiseTemple Face Texcoord',)),                 (add_section_if_missing, ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n'))],
'757bc7cc': [(log, ('2.8 -> 3.0: WiseTemple Face blend_vb Hash [Legacy]',)), (update_hash, ('015fbf96',))],

# Torso Ribbon VBs
'e0931b87': [(log, ('2.8: WiseTemple Torso Ribbon draw_vb',)),          (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'fe8e2ff8': [(log, ('2.8: WiseTemple Torso Ribbon position_vb',)),      (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'b6108302': [(log, ('2.8: WiseTemple Torso Ribbon texcoord_vb',)),      (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],
'd9691e6b': [(log, ('2.8: WiseTemple Torso Ribbon blend_vb',)),          (add_section_if_missing, ('eeabff55', 'WiseTemple.Ribbon.IB', 'match_priority = 0\n'))],

# Panda Headgear VBs
'e7d550d0': [(log, ('2.8: WiseTemple Panda Headgear draw_vb',)),        (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'c8a749b1': [(log, ('2.8: WiseTemple Panda Headgear position_vb',)),    (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'e938a289': [(log, ('2.8: WiseTemple Panda Headgear texcoord_vb',)),    (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],
'ece854ad': [(log, ('2.8: WiseTemple Panda Headgear blend_vb',)),       (add_section_if_missing, ('ac3a0dec', 'WiseTemple.PandaHeadgear.IB', 'match_priority = 0\n'))],

# Black Orange Ribbon VBs
'aad48132': [(log, ('2.8: WiseTemple Black Orange Ribbon draw_vb',)),   (add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'139c0e20': [(log, ('2.8: WiseTemple Black Orange Ribbon position_vb',)),(add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'0f705b4a': [(log, ('2.8: WiseTemple Black Orange Ribbon texcoord_vb',)),(add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],
'a60b2098': [(log, ('2.8: WiseTemple Black Orange Ribbon blend_vb',)),   (add_section_if_missing, ('e5f8b021', 'WiseTemple.BlackOrangeRibbon.IB', 'match_priority = 0\n'))],

# Orange Green Ribbon VBs
'2efc0d70': [(log, ('2.8: WiseTemple Orange Green Ribbon draw_vb',)),   (add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'e801def3': [(log, ('2.8: WiseTemple Orange Green Ribbon position_vb',)),(add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'bc87900c': [(log, ('2.8: WiseTemple Orange Green Ribbon texcoord_vb',)),(add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],
'4851307e': [(log, ('2.8: WiseTemple Orange Green Ribbon blend_vb',)),   (add_section_if_missing, ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n'))],

# Glasses VBs
'ba8bde72': [(log, ('2.8: WiseTemple Glasses draw_vb',)),               (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'66cabdf9': [(log, ('2.8: WiseTemple Glasses position_vb',)),           (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'ac329cd7': [(log, ('2.8: WiseTemple Glasses texcoord_vb',)),           (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],
'a8620018': [(log, ('2.8: WiseTemple Glasses blend_vb',)),              (add_section_if_missing, ('bfce3c18', 'WiseTemple.Glasses.IB', 'match_priority = 0\n'))],

# Earrings VBs
'5a617015': [(log, ('2.8: WiseTemple Earrings draw_vb',)),               (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'49a9bab4': [(log, ('2.8: WiseTemple Earrings position_vb',)),           (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'a9b9bf40': [(log, ('2.8: WiseTemple Earrings texcoord_vb',)),           (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],
'686847cc': [(log, ('2.8: WiseTemple Earrings blend_vb',)),              (add_section_if_missing, ('b856d397', 'WiseTemple.Earrings.IB', 'match_priority = 0\n'))],

# CatEar VBs
'ad73aefc': [(log, ('2.8: WiseTemple CatEar draw_vb',)),                 (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'53b4170f': [(log, ('2.8: WiseTemple CatEar position_vb',)),             (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'3280491f': [(log, ('2.8: WiseTemple CatEar texcoord_vb',)),             (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],
'603fdb26': [(log, ('2.8: WiseTemple CatEar blend_vb',)),                (add_section_if_missing, ('d0e278fc', 'WiseTemple.CatEar.IB', 'match_priority = 0\n'))],

# TorsoAcc VBs
'0406d75f': [(log, ('2.8: WiseTemple TorsoAcc draw_vb',)),             (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'13e791fa': [(log, ('2.8: WiseTemple TorsoAcc position_vb',)),         (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'fd95b568': [(log, ('2.8: WiseTemple TorsoAcc texcoord_vb',)),         (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],
'e147258a': [(log, ('2.8: WiseTemple TorsoAcc blend_vb',)),            (add_section_if_missing, ('4e8b2454', 'WiseTemple.TorsoAcc.IB', 'match_priority = 0\n'))],

# === Legacy / Version Updates ===
'6acc1eb8': [(log, ('2.5 -> 2.8: WiseTemple Body IB [Legacy]',)),       (update_hash, ('1eca2097',))],
'ae59eabb': [(log, ('2.5 -> 2.8: WiseTemple Body Position [Legacy]',)), (update_hash, ('a388eb6b',))],
'a83ada4e': [(log, ('2.5 -> 2.8: WiseTemple Body Texcoord [Legacy]',)), (update_hash, ('b39870e1',))],
'177ad7e8': [(log, ('2.5 -> 2.8: WiseTemple Body Blend [Legacy]',)),    (update_hash, ('8612559a',))],
'4fa228f9': [(log, ('2.5 -> 2.8: WiseTemple Body Draw [Legacy]',)),     (update_hash, ('ca02f614',))],

'5d75fddc': [
        (log,                           ('2.8: WiseTemple Face Diffuse Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
    ],
'015fbf96': [
        (log,                           ('3.0: WiseTemple Face blend_vb Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.8: WiseTemple Hair LightMap 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'28005a5b': [
        (log,                           ('2.8: WiseTemple Hair Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.8: WiseTemple Hair MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'68e4f572': [
        (log,                           ('3.0: WiseTemple Hair blend_vb Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
    ],
'669191ec': [
        (log,                           ('3.0: WiseTemple Neck, Body Diffuse Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'05b25d35': [
        (log,                           ('3.0: WiseTemple Neck, Body LightMap 1024p Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'08b27f4a': [
        (log,                           ('3.0: WiseTemple WaistAccessories LightMap 2048p Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'3fef0e14': [
        (log,                           ('3.0: WiseTemple WaistAccessories Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'aa712fb9': [
        (log,                           ('3.0: WiseTemple Neck, Body MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('24af1f48', 'WiseTemple.Neck.Body.MaterialMap.2048')),
    ],
'e590e6be': [
        (log,                           ('3.0: WiseTemple WaistAccessories Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'a78880dc': [
        (log,                           ('3.0: WiseTemple WaistAccessories LightMap 1024p Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'4a0b4014': [
        (log,                           ('3.0: WiseTemple WaistAccessories MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'24af1f48': [
        (log,                           ('3.0: WiseTemple Neck, Body MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],
'a15aa6b3': [
        (log,                           ('3.0: WiseTemple Face/DiskPlayer MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseTemple.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'e0b1e734': [
        (log,                           ('3.0: WiseTemple Neck blend_vb Hash',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
    ],
'f28a6363': [
        (log,                           ('3.0: WiseTemple Body blend_vb Hash',)),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
    ],

# === Broken References Fix (v2.8) ===
'f425bd04': [(log, ('2.8: Wise Body Texcoord Hash [Legacy] 2.0',)),     (update_hash, ('91fbd2fa',))],
'84529dab': [(log, ('2.8: Wise BodyA Diffuse 2048p Hash [Legacy] Old',)), (update_hash, ('f2fb7a37',))],
'ef76b675': [(log, ('2.8: Wise BodyA Diffuse 1024p Hash [Legacy] Old',)), (update_hash, ('3d7a53b0',))],

# === 2.8 Sync Updates ===
'868709f2': [(log, ('2.7 -> 2.8: Wise BodyA Diffuse [Legacy]',)), (update_hash, ('f2fb7a37',))],

# === Legacy 2.0-2.8 Hash Updates ===
'f6cac296': [(log, ('2.0 -> 2.8: WiseTemple IB Hash [Legacy]',)), (update_hash, ('d5ca0411',))],
'ba59bf09': [(log, ('2.0 -> 2.8: Wise Hair draw_vb Hash [Legacy]',)), (update_hash, ('ef9c0510',))],
'6235fa7f': [(log, ('2.0 -> 2.8: Wise Hair position_vb Hash [Legacy]',)), (update_hash, ('e8df7ff3',))],
'fe89498c': [(log, ('2.0 -> 2.8: Wise Hair texcoord_vb Hash [Legacy]',)), (update_hash, ('774071dd',))],
'1273c7b0': [(log, ('2.0 -> 2.8: Wise Hair blend_vb Hash [Legacy]',)), (update_hash, ('edfd1666',))],
'83e07a1b': [(log, ('2.7 -> 2.8: Wise HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'af5fc216': [(log, ('2.7 -> 2.8: Wise HairShadow draw_vb Hash [Legacy]',)), (update_hash, ('681651f9',))],
'1a438b0d': [(log, ('2.7 -> 2.8: Wise HairShadow position_vb Hash [Legacy]',)), (update_hash, ('4af493e5',))],
'7b7957fa': [(log, ('2.7 -> 2.8: Wise HairShadow texcoord_vb Hash [Legacy]',)), (update_hash, ('ad7d7eca',))],
'52bd07dd': [(log, ('2.7 -> 2.8: Wise HairShadow blend_vb Hash [Legacy]',)), (update_hash, ('795e9a7c',))],
'81406abe': [(log, ('2.8 -> 3.0: WiseTemple BodyA Diffuse 2048p Hash [Legacy]',)), (update_hash, ('669191ec',))],
'3f771e63': [(log, ('2.8 -> 3.0: WiseSwimwear HairShadow IB Hash [Legacy]',)), (update_hash, ('8d08b190',))],
'ebe9f31b': [(log, ('2.0 -> 2.1: Wise Head Texcoord Hash [Legacy]',)), (update_hash, ('c83b6cbf',))],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('2.8: WiseTemple Shared NormalMap Hash',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseTemple.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseTemple.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('01c42a1d', 'WiseTemple.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseTemple.DiskPlayer.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e5f269f4', 'WiseTemple.OrangeGreenRibbon.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: WiseTemple Shared NormalMap Hash [Legacy]',)),
        (update_hash,                   ('798adba3',)),
    ],

# === Legacy 3.0 Texture Hashes ===
    '1024352b': [
        (log,                           ('3.0: WiseTemple TieA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('dd08a467', 'WiseSchoolUniform.TieA.Diffuse.1024')),
    ],
    '22fe3236': [(log, ('3.0: WiseTemple Body IB Hash',)), (add_ib_check_if_missing,)],
    '31707abe': [
        (log,                           ('3.0: WiseTemple BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('4d7473b1', 'WiseSchoolUniform.BodyA.MaterialMap.2048')),
    ],
    '4d7473b1': [
        (log,                           ('3.0: WiseTemple BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('31707abe', 'WiseSchoolUniform.BodyA.MaterialMap.1024')),
    ],
    '4f211318': [
        (log,                           ('3.0: WiseTemple TieA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e550cd81', 'WiseSchoolUniform.TieA.LightMap.2048')),
    ],
    '6649f407': [
        (log,                           ('3.0: WiseTemple TieA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('ba59a4d0', 'WiseSchoolUniform.TieA.MaterialMap.1024')),
    ],
    '8a1ec07e': [(log, ('3.0: WiseTemple Neck IB Hash',)), (add_ib_check_if_missing,)],
    '8d09dc95': [
        (log,                           ('3.0: WiseTemple BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('bd86c7c4', 'WiseSchoolUniform.BodyA.LightMap.1024')),
    ],
    'a0a4c84e': [
        (log,                           ('3.0: WiseTemple BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('b9dcce2e', 'WiseSchoolUniform.BodyA.Diffuse.1024')),
    ],
    'b9dcce2e': [
        (log,                           ('3.0: WiseTemple BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('a0a4c84e', 'WiseSchoolUniform.BodyA.Diffuse.1024')),
    ],
    'ba59a4d0': [
        (log,                           ('3.0: WiseTemple TieA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('6649f407', 'WiseSchoolUniform.TieA.MaterialMap.2048')),
    ],
    'bd86c7c4': [
        (log,                           ('3.0: WiseTemple BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8d09dc95', 'WiseSchoolUniform.BodyA.LightMap.1024')),
    ],
    'dd08a467': [
        (log,                           ('3.0: WiseTemple TieA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('1024352b', 'WiseSchoolUniform.TieA.Diffuse.2048')),
    ],
    'e550cd81': [
        (log,                           ('3.0: WiseTemple TieA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('4f211318', 'WiseSchoolUniform.TieA.LightMap.1024')),
    ],
    'f21a2bac': [(log, ('3.0: WiseTemple Tie IB Hash',)), (add_ib_check_if_missing,)],
    '2a7548a9': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('2a7548a9', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    '5346205a': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('5346205a', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    '78c2d1dd': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('78c2d1dd', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    '8839d1fc': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('8839d1fc', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    '96ad58d4': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('96ad58d4', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    'a2f096fc': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('a2f096fc', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    'cd075caa': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('cd075caa', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    'ed1a5b7f': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('ed1a5b7f', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    'f5dc4198': [(log, ('3.0: WiseTemple Unknown Component Hash',)), (add_section_if_missing, ('f5dc4198', 'WiseTemple.py.Unknown.IB', 'match_priority = 0\n'))],
    '23876240': [(log,                           ('3.0: WiseTemple BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('81406abe','669191ec'), 'WiseSkin.BodyA.Diffuse.2048')),],
    '33368e12': [(log,                           ('2.0: Wise HairA, BagA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8d8269f8', '1f21c633'), 'Wise.HairA.LightMap.2048')),],
    '588d7d2d': [(log,                           ('1.1: Wise HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4894246e', 'Wise.Head.IB', 'match_priority = 0\n')),],
    'cb0d0c22': [(log,                           ('1.0: Wise HairA, BagA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b1df5d22', 'Wise.Bag.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('28005a5b', 'Wise.HairA.Diffuse.2048')),],
    'd9383a15': [(log,                           ('2.0: Wise HairA, BagA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f6cac296', 'Wise.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('f1b20f3d', '473f816d'), 'Wise.HairA.MaterialMap.2048')),],
    'dd79b44b': [(log,                           ('2.0: WiseTemple BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('6acc1eb8', 'WiseSkin.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('05b25d35', 'WiseSkin.BodyA.LightMap.2048')),],
    '9fc3646e': [(log, ('Transition legacy entry for 9fc3646e',)), (update_hash, ('23876240',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseTemple',
    'game_versions': ['2.8', '3.0'],
}