"""
WiseSoaringSoaringCrane Outfit Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseSoaringSoaringCrane Outfit's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# =============================================================================
# Hash Updates (Old → New)
# =============================================================================
'6acc1eb8': [(log, ('2.5: WiseSoaringCrane Body IB Hash → WiseSoaringCrane Body IB Hash',)), (update_hash, ('1eca2097',))],
'a83ada4e': [(log, ('2.5: WiseSoaringCrane Body Texcoord → WiseSoaringCrane Body Texcoord',)), (update_hash, ('b39870e1',))],
'177ad7e8': [(log, ('2.5: WiseSoaringCrane Body Blend → WiseSoaringCrane Body Blend',)), (update_hash, ('8612559a',))],
'ae59eabb': [(log, ('2.5: WiseSoaringCrane Body Position → WiseSoaringCrane Body Position',)), (update_hash, ('a388eb6b',))],
'4fa228f9': [(log, ('2.5: WiseSoaringCrane Body Draw → WiseSoaringCrane Body Draw',)), (update_hash, ('ca02f614',))],

# =============================================================================
# WiseSoaringCrane IB Hashes
# =============================================================================
'01c42a1d': [(log, ('2.5: WiseSoaringCrane Neck IB Hash',)), (add_ib_check_if_missing,)],
'1eca2097': [(log, ('2.5: WiseSoaringCrane Body IB Hash',)), (add_ib_check_if_missing,)],
'1fdaf388': [(log, ('2.5: WiseSoaringCrane Face IB Hash',)), (add_ib_check_if_missing,)],
'd5ca0411': [(log, ('2.5: WiseSoaringCrane Hair IB Hash',)), (add_ib_check_if_missing,)],
'e7f527ea': [(log, ('2.5: WiseSoaringCrane DiskPlayer IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# WiseSoaringCrane Body Buffer Hashes
# =============================================================================
'b39870e1': [(log, ('2.5: WiseSoaringCrane Body Texcoord Buffer Hash',))],
'8612559a': [(log, ('2.8 -> 3.0: WiseSoaringCrane Body Blend Hash',)), (update_hash, ('f28a6363',))],
'a388eb6b': [(log, ('2.5: WiseSoaringCrane Body Position Buffer Hash',))],
'ca02f614': [(log, ('2.5: WiseSoaringCrane Body Draw Buffer Hash',))],

# =============================================================================
# WiseSoaringCrane Face Textures
# =============================================================================
'5d75fddc': [
        (log,                           ('2.5: WiseSoaringCrane Face Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],

'a15aa6b3': [
        (log,                           ('2.5: WiseSoaringCrane Face/DiskPlayer MaterialMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseSoaringCrane.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# WiseSoaringCrane Hair Textures
# =============================================================================
'28005a5b': [
        (log,                           ('2.5: WiseSoaringCrane Hair Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],

'8d8269f8': [
        (log,                           ('2.5: WiseSoaringCrane Hair LightMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],

'f1b20f3d': [
        (log,                           ('2.5: WiseSoaringCrane Hair MaterialMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# WiseSoaringCrane Body/Neck Shared Textures
# =============================================================================
'81406abe': [
        (log,                           ('2.8 -> 3.0: WiseSoaringCrane BodyA Diffuse 2048p Hash',)),
        (update_hash,                        ('669191ec',)),
    ],
'669191ec': [
        (log,                           ('3.0: WiseSoaringCrane BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('9fc3646e', '23876240'), 'WiseSoaringCrane.BodyA.Diffuse.1024')),
    ],

'9fc3646e': [
        (log,                           ('2.8 -> 3.0: WiseSoaringCrane BodyA Diffuse 1024p Hash',)),
        (update_hash,                        ('23876240',)),
    ],
'23876240': [
        (log,                           ('3.0: WiseSoaringCrane BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('81406abe', '669191ec'), 'WiseSoaringCrane.BodyA.Diffuse.2048')),
    ],

'05b25d35': [
        (log,                           ('2.5: WiseSoaringCrane Body/Neck LightMap 2048p Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('dd79b44b', 'WiseSoaringCrane.BodyA.LightMap.1024')),
    ],

'dd79b44b': [
        (log,                           ('2.5: WiseSoaringCrane Body/Neck LightMap 1024p Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('05b25d35', 'WiseSoaringCrane.BodyA.LightMap.2048')),
    ],

'24af1f48': [
        (log,                           ('2.5: WiseSoaringCrane Body/Neck MaterialMap 2048p Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('aa712fb9', 'WiseSoaringCrane.BodyA.MaterialMap.1024')),
    ],

'aa712fb9': [
        (log,                           ('2.5: WiseSoaringCrane Body/Neck MaterialMap 1024p Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('24af1f48', 'WiseSoaringCrane.BodyA.MaterialMap.2048')),
    ],

# =============================================================================
# WiseSoaringCrane DiskPlayer Textures
# =============================================================================
'3fef0e14': [
        (log,                           ('2.5: WiseSoaringCrane DiskPlayer Diffuse Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseSoaringCrane.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

'08b27f4a': [
        (log,                           ('2.5: WiseSoaringCrane DiskPlayer LightMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('e7f527ea', 'WiseSoaringCrane.DiskPlayer.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# Shared NormalMap (Hair/Body/Neck/DiskPlayer)
# =============================================================================
'ebac056e': [
        (log,                           ('2.5: WiseSoaringCrane Shared NormalMap Hash (No alternate resolution)',)),
        (add_section_if_missing,        ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e7f527ea', 'WiseSoaringCrane.DiskPlayer.IB', 'match_priority = 0\n')),
    ],
'ef9c0510': [
        (log, ('3.0: WiseSoaringCrane Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'e8df7ff3': [
        (log, ('3.0: WiseSoaringCrane Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'774071dd': [
        (log, ('3.0: WiseSoaringCrane Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'68e4f572': [
        (log, ('3.0: WiseSoaringCrane Hair VB Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'8d08b190': [(log, ('3.0: WiseSoaringCrane Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'681651f9': [
        (log, ('3.0: WiseSoaringCrane Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4af493e5': [
        (log, ('3.0: WiseSoaringCrane Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ad7d7eca': [
        (log, ('3.0: WiseSoaringCrane Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'795e9a7c': [
        (log, ('3.0: WiseSoaringCrane Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'276e1373': [
        (log, ('3.0: WiseSoaringCrane Neck VB Hash',)),
        (add_section_if_missing, ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
    ],
'd8ad824b': [
        (log, ('3.0: WiseSoaringCrane Neck VB Hash',)),
        (add_section_if_missing, ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
    ],
'39a1dfe3': [
        (log, ('3.0: WiseSoaringCrane Neck VB Hash',)),
        (add_section_if_missing, ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
    ],
'458bbde3': [(log, ('2.8 -> 3.0: Wise Neck Blend Hash',)), (update_hash, ('e0b1e734',))],
'e0b1e734': [
        (log, ('3.0: WiseSoaringCrane Neck VB Hash',)),
        (add_section_if_missing, ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
    ],
'f28a6363': [
        (log, ('3.0: WiseSoaringCrane Body VB Hash',)),
        (add_section_if_missing, ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
    ],
'0c1c9bf3': [
        (log, ('3.0: WiseSoaringCrane Waist accessories VB Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'1e5cafee': [
        (log, ('3.0: WiseSoaringCrane Waist accessories VB Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'06f42a6f': [
        (log, ('3.0: WiseSoaringCrane Waist accessories VB Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'0a0aa1a8': [
        (log, ('3.0: WiseSoaringCrane Waist accessories VB Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'5657c1fc': [
        (log, ('3.0: WiseSoaringCrane Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],
'c83b6cbf': [
        (log, ('3.0: WiseSoaringCrane Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],
'2b320847': [
        (log, ('3.1: WiseSoaringCrane Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],
'015fbf96': [
        (log, ('3.0: WiseSoaringCrane Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],
'6c4552bb': [(log, ('3.0: WiseSoaringCrane misc hash',)),],
'cb0d0c22': [
        (log, ('3.0: WiseSoaringCrane Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: WiseSoaringCrane Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'33368e12': [
        (log, ('3.0: WiseSoaringCrane Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'd9383a15': [
        (log, ('3.0: WiseSoaringCrane Hair TEX Hash',)),
        (add_section_if_missing, ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
    ],
'e590e6be': [
        (log, ('3.0: WiseSoaringCrane Waist accessories TEX Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'a78880dc': [
        (log, ('3.0: WiseSoaringCrane Waist accessories TEX Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'4a0b4014': [
        (log, ('3.0: WiseSoaringCrane Waist accessories TEX Hash',)),
        (add_section_if_missing, ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
    ],
'588d7d2d': [
        (log, ('3.0: WiseSoaringCrane Face TEX Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
    ],
# =============================================================================
# WiseSoaringCrane 2.8 WiseSkin Accessory IBs (2.8-only, no 3.0)
# =============================================================================
'd0e278fc': [(log, ('2.8: WiseSoaringCrane Cat Ear Accessories IB Hash',)), (add_ib_check_if_missing,)],
'b856d397': [(log, ('2.8: WiseSoaringCrane Earrings IB Hash',)), (add_ib_check_if_missing,)],
'bfce3c18': [(log, ('2.8: WiseSoaringCrane glasses IB Hash',)), (add_ib_check_if_missing,)],
'ac3a0dec': [(log, ('2.8: WiseSoaringCrane Panda headgear IB Hash',)), (add_ib_check_if_missing,)],
'e5f8b021': [(log, ('2.8: WiseSoaringCrane Black orange ribbon IB Hash',)), (add_ib_check_if_missing,)],
'e5f269f4': [(log, ('2.8: WiseSoaringCrane Orange green ribbon IB Hash',)), (add_ib_check_if_missing,)],
'eeabff55': [(log, ('2.8: WiseSoaringCrane Orange green badge IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# WiseSoaringCrane 2.8 WiseSkin Accessory VB Hashes (2.8-only, no 3.0)
# =============================================================================
'0f705b4a': [
        (log, ('2.8: WiseSoaringCrane Black orange ribbon texcoord_vb Hash',)),
        (add_section_if_missing, ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
    ],
'139c0e20': [
        (log, ('2.8: WiseSoaringCrane Black orange ribbon position_vb Hash',)),
        (add_section_if_missing, ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
    ],
'2efc0d70': [
        (log, ('2.8: WiseSoaringCrane Orange green ribbon draw_vb Hash',)),
        (add_section_if_missing, ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
    ],
'3280491f': [
        (log, ('2.8: WiseSoaringCrane Cat Ear Accessories texcoord_vb Hash',)),
        (add_section_if_missing, ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
    ],
'4851307e': [
        (log, ('2.8: WiseSoaringCrane Orange green ribbon blend_vb Hash',)),
        (add_section_if_missing, ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
    ],
'49a9bab4': [
        (log, ('2.8: WiseSoaringCrane Earrings position_vb Hash',)),
        (add_section_if_missing, ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
    ],
'53b4170f': [
        (log, ('2.8: WiseSoaringCrane Cat Ear Accessories position_vb Hash',)),
        (add_section_if_missing, ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
    ],
'5a617015': [
        (log, ('2.8: WiseSoaringCrane Earrings draw_vb Hash',)),
        (add_section_if_missing, ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
    ],
'603fdb26': [
        (log, ('2.8: WiseSoaringCrane Cat Ear Accessories blend_vb Hash',)),
        (add_section_if_missing, ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
    ],
'66cabdf9': [
        (log, ('2.8: WiseSoaringCrane glasses position_vb Hash',)),
        (add_section_if_missing, ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
    ],
'686847cc': [
        (log, ('2.8: WiseSoaringCrane Earrings blend_vb Hash',)),
        (add_section_if_missing, ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
    ],
'757bc7cc': [
        (log, ('2.8: WiseSoaringCrane Face Blend Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('015fbf96',)),
    ],
'a60b2098': [
        (log, ('2.8: WiseSoaringCrane Black orange ribbon blend_vb Hash',)),
        (add_section_if_missing, ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
    ],
'a8620018': [
        (log, ('2.8: WiseSoaringCrane glasses blend_vb Hash',)),
        (add_section_if_missing, ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
    ],
'a9b9bf40': [
        (log, ('2.8: WiseSoaringCrane Earrings texcoord_vb Hash',)),
        (add_section_if_missing, ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
    ],
'aad48132': [
        (log, ('2.8: WiseSoaringCrane Black orange ribbon draw_vb Hash',)),
        (add_section_if_missing, ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
    ],
'ac329cd7': [
        (log, ('2.8: WiseSoaringCrane glasses texcoord_vb Hash',)),
        (add_section_if_missing, ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
    ],
'ad73aefc': [
        (log, ('2.8: WiseSoaringCrane Cat Ear Accessories draw_vb Hash',)),
        (add_section_if_missing, ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
    ],
'b6108302': [
        (log, ('2.8: WiseSoaringCrane Orange green badge texcoord_vb Hash',)),
        (add_section_if_missing, ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'ba8bde72': [
        (log, ('2.8: WiseSoaringCrane glasses draw_vb Hash',)),
        (add_section_if_missing, ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
    ],
'bc87900c': [
        (log, ('2.8: WiseSoaringCrane Orange green ribbon texcoord_vb Hash',)),
        (add_section_if_missing, ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
    ],
'c8a749b1': [
        (log, ('2.8: WiseSoaringCrane Panda headgear position_vb Hash',)),
        (add_section_if_missing, ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'd9691e6b': [
        (log, ('2.8: WiseSoaringCrane Orange green badge blend_vb Hash',)),
        (add_section_if_missing, ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'e0931b87': [
        (log, ('2.8: WiseSoaringCrane Orange green badge draw_vb Hash',)),
        (add_section_if_missing, ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'e7d550d0': [
        (log, ('2.8: WiseSoaringCrane Panda headgear draw_vb Hash',)),
        (add_section_if_missing, ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'e801def3': [
        (log, ('2.8: WiseSoaringCrane Orange green ribbon position_vb Hash',)),
        (add_section_if_missing, ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
    ],
'e938a289': [
        (log, ('2.8: WiseSoaringCrane Panda headgear texcoord_vb Hash',)),
        (add_section_if_missing, ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'ece854ad': [
        (log, ('2.8: WiseSoaringCrane Panda headgear blend_vb Hash',)),
        (add_section_if_missing, ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'fe8e2ff8': [
        (log, ('2.8: WiseSoaringCrane Orange green badge position_vb Hash',)),
        (add_section_if_missing, ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseSoaringCrane',
    'game_versions': ['2.5', '3.0'],
}

