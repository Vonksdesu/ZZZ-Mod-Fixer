"""
ZhuYuan Character Hash Commands
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
    Returns ZhuYuan's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6619364f': [(log, ('1.1: ZhuYuan Body IB Hash',)),         (add_ib_check_if_missing,)],
'9821017e': [(log, ('1.0: ZhuYuan Hair IB Hash',)),         (add_ib_check_if_missing,)],
'fcac8411': [(log, ('1.0: ZhuYuan Extras IB Hash',)),       (add_ib_check_if_missing,)],
'5e717358': [(log, ('1.0: ZhuYuan ShoulderAmmo IB Hash',)), (add_ib_check_if_missing,)],
'a63028ae': [(log, ('1.0: ZhuYuan HipAmmo IB Hash',)),      (add_ib_check_if_missing,)],
'f1c241b7': [(log, ('1.0: ZhuYuan Head IB Hash',)),         (add_ib_check_if_missing,)],
'a4aeb1d5': [(log, ('1.0 -> 1.1: ZhuYuan Body IB Hash',)),  (update_hash, ('6619364f',))],
'5e942526': [(log, ('1.0 -> 1.1: ZhuYuan Body Blend Hash',)), (update_hash, ('01e0c8d9',))],
'f3569f8d': [(log, ('1.0 -> 1.1: ZhuYuan Body Position Hash',)), (update_hash, ('f595d24d',))],
'160872c0': [(log, ('1.0 -> 1.1: ZhuYuan Body Texcoord Hash',)), (update_hash, ('cb885260',))],
'fdc045fc': [
        (log, ('1.1 -> 1.2: ZhuYuan Hair Texcoord Hash',)),
        (update_hash, ('f3c092c5',)),
        (log, ('+ Reverting texcoord buffer remap',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'138c7d76': [
        (log,                           ('1.0: ZhuYuan HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f1c241b7', 'ZhuYuan.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a1eabb9f', 'ZhuYuan.HeadA.Diffuse.2048')),
    ],
'a1eabb9f': [
        (log,                           ('1.0: ZhuYuan HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f1c241b7', 'ZhuYuan.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('138c7d76', 'ZhuYuan.HeadA.Diffuse.1024')),
    ],
'9b86c2f6': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('7f823598', 'ZhuYuan.HairA.Diffuse.2048')),
    ],
'6eb346b9': [(log, ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'8955095f': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d4ee59c7', 'ZhuYuan.HairA.LightMap.2048')),
    ],
'7d884663': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('12a407b1', 'ZhuYuan.HairA.MaterialMap.2048')),
    ],
'7f823598': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('9b86c2f6', 'ZhuYuan.HairA.Diffuse.1024')),
    ],
'4ac1defe': [(log, ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('1.2: ZhuYuan Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        (('9821017e', 'fcac8411', '5e717358', 'a63028ae', '6619364f'), 'ZhuYuan.Shared.NormalMap.2048', 'match_priority = 0\n')),
    ],
'd4ee59c7': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8955095f', 'ZhuYuan.HairA.LightMap.1024')),
    ],
'12a407b1': [
        (log,                           ('1.0: ZhuYuan HairA, ExtrasA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('7d884663', 'ZhuYuan.HairA.MaterialMap.1024')),
    ],
'b57a8744': [(log, ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 1024p Hash',)),     (update_hash, ('f6795718',))],
'833bafd5': [(log, ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('729ea75a',))],
'18d00ac6': [(log, ('1.0 -> 1.1: ZhuYuan BodyA LightMap 1024p Hash',)),    (update_hash, ('14b638b6',))],
'1daa379f': [(log, ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 1024p Hash',)), (update_hash, ('cd4dee2c',))],
'f6795718': [(log, ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 1024p Hash',)),     (update_hash, ('46af14f8',))],
'729ea75a': [(log, ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('d5b175bf',))],
'14b638b6': [(log, ('1.1 -> 1.2: ZhuYuan BodyA LightMap 1024p Hash',)),    (update_hash, ('fb385169',))],
'cd4dee2c': [(log, ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 1024p Hash',)), (update_hash, ('29e2ebc5',))],
'46af14f8': [
        (log,                           ('1.2: ZhuYuan BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('a271e894', '3ef82f41', 'c88e7660'), 'ZhuYuan.BodyA.Diffuse.2048')),
    ],
'd5b175bf': [(log, ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'fb385169': [
        (log,                           ('1.2: ZhuYuan BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d02bc66c', '80ebf536', '13a38449'), 'ZhuYuan.BodyA.LightMap.2048')),
    ],
'29e2ebc5': [
        (log,                           ('1.2: ZhuYuan BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3e808ef6', '10415de8', 'b4e20235'), 'ZhuYuan.BodyA.MaterialMap.2048')),
    ],
'c88e7660': [(log, ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 2048p Hash',)),     (update_hash, ('3ef82f41',))],
'a396c53a': [(log, ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('7195a311',))],
'13a38449': [(log, ('1.0 -> 1.1: ZhuYuan BodyA LightMap 2048p Hash',)),    (update_hash, ('80ebf536',))],
'b4e20235': [(log, ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 2048p Hash',)), (update_hash, ('10415de8',))],
'3ef82f41': [(log, ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 2048p Hash',)),     (update_hash, ('a271e894',))],
'7195a311': [(log, ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('d81fb56e',))],
'80ebf536': [(log, ('1.1 -> 1.2: ZhuYuan BodyA LightMap 2048p Hash',)),    (update_hash, ('d02bc66c',))],
'10415de8': [(log, ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 2048p Hash',)), (update_hash, ('3e808ef6',))],
'a271e894': [
        (log,                           ('1.2: ZhuYuan BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('46af14f8', 'f6795718', 'b57a8744'), 'ZhuYuan.BodyA.Diffuse.1024')),
    ],
'd81fb56e': [(log, ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'd02bc66c': [
        (log,                           ('1.2: ZhuYuan BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('fb385169', '14b638b6', '18d00ac6'), 'ZhuYuan.BodyA.LightMap.1024')),
    ],
'3e808ef6': [
        (log,                           ('1.2: ZhuYuan BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('a4aeb1d5', '6619364f'), 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('29e2ebc5', 'cd4dee2c', '1daa379f'), 'ZhuYuan.BodyA.MaterialMap.1024')),
    ],
'222ae5ee': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('6a33b25e', 'ZhuYuan.ExtrasB.Diffuse.2048')),
    ],
'0fda74c3': [(log, ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 1024p Hash',)),   (update_hash, ('ebac056e',))],
'790183b4': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e30f025b', 'ZhuYuan.ExtrasB.LightMap.2048')),
    ],
'84842409': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('58d5c840', 'ZhuYuan.ExtrasB.MaterialMap.2048')),
    ],
'6a33b25e': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('222ae5ee', 'ZhuYuan.ExtrasB.Diffuse.1024')),
    ],
'fb35b7e9': [(log, ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 2048p Hash',)),   (update_hash, ('ebac056e',))],
'e30f025b': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('790183b4', 'ZhuYuan.ExtrasB.LightMap.1024')),
    ],
'58d5c840': [
        (log,                           ('1.0: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('84842409', 'ZhuYuan.ExtrasB.MaterialMap.1024')),
    ],
'a3091843': [
        (log, ('3.0: ZhuYuan Hair VB Hash',)),
        (add_section_if_missing, ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
    ],
'd140d2e7': [
        (log, ('3.0: ZhuYuan Hair VB Hash',)),
        (add_section_if_missing, ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
    ],
'f3c092c5': [
        (log, ('3.0: ZhuYuan Hair VB Hash',)),
        (add_section_if_missing, ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
    ],
'9d35aee2': [
        (log, ('3.0: ZhuYuan Hair VB Hash',)),
        (add_section_if_missing, ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
    ],
'fb69fc45': [(log, ('3.0: ZhuYuan Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'72411765': [
        (log, ('3.0: ZhuYuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'35b94ea8': [
        (log, ('3.0: ZhuYuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'aecf6710': [
        (log, ('3.0: ZhuYuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'527b317a': [
        (log, ('3.0: ZhuYuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f595d24d': [
        (log, ('3.0: ZhuYuan Body VB Hash',)),
        (add_section_if_missing, ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
    ],
'cb885260': [
        (log, ('3.0: ZhuYuan Body VB Hash',)),
        (add_section_if_missing, ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
    ],
'01e0c8d9': [
        (log, ('3.0: ZhuYuan Body VB Hash',)),
        (add_section_if_missing, ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
    ],
'dd91b126': [
        (log, ('3.0: ZhuYuan ShoulderAmmo VB Hash',)),
        (add_section_if_missing, ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
    ],
'd55c7763': [
        (log, ('3.0: ZhuYuan ShoulderAmmo VB Hash',)),
        (add_section_if_missing, ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
    ],
'1c68a02f': [
        (log, ('3.0: ZhuYuan ShoulderAmmo VB Hash',)),
        (add_section_if_missing, ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
    ],
'e6fca033': [
        (log, ('3.0: ZhuYuan ShoulderAmmo VB Hash',)),
        (add_section_if_missing, ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
    ],
'52e3c65f': [
        (log, ('3.0: ZhuYuan Extras VB Hash',)),
        (add_section_if_missing, ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
    ],
'5f445c20': [
        (log, ('3.0: ZhuYuan Extras VB Hash',)),
        (add_section_if_missing, ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
    ],
'ac21fba4': [
        (log, ('3.0: ZhuYuan Extras VB Hash',)),
        (add_section_if_missing, ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
    ],
'0f5035dd': [
        (log, ('3.0: ZhuYuan Extras VB Hash',)),
        (add_section_if_missing, ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
    ],
'82889576': [
        (log, ('3.0: ZhuYuan HipAmmo VB Hash',)),
        (add_section_if_missing, ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
    ],
'45d265c0': [
        (log, ('3.0: ZhuYuan HipAmmo VB Hash',)),
        (add_section_if_missing, ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
    ],
'75c5e659': [
        (log, ('3.0: ZhuYuan HipAmmo VB Hash',)),
        (add_section_if_missing, ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
    ],
'9a268159': [
        (log, ('3.0: ZhuYuan HipAmmo VB Hash',)),
        (add_section_if_missing, ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
    ],
'09f4496a': [
        (log, ('3.0: ZhuYuan Face VB Hash',)),
        (add_section_if_missing, ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
    ],
'0c6f696b': [
        (log, ('3.0: ZhuYuan Face VB Hash',)),
        (add_section_if_missing, ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
    ],
'6c9ffbbf': [
        (log, ('3.0: ZhuYuan Face VB Hash',)),
        (add_section_if_missing, ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
    ],
'a9188e3c': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'04a00393': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'8bade376': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'9d99178a': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'1747290f': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'84de8345': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'852f5de0': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'a7f00ae5': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'49c9bbf7': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a7f00ae5', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'e03ad35f': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a7f00ae5', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'0e291903': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('a7f00ae5', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'd19a5cd0': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'53738d91': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('d19a5cd0', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'c03acfb5': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('d19a5cd0', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'8f4f2e30': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('d19a5cd0', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'db111545': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'd3630839': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('db111545', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'3ffbf9b5': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('db111545', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'32a33b84': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('db111545', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'e5a92555': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'7cab956b': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e5a92555', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'61312746': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e5a92555', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'c8e16aaf': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e5a92555', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'f8e6c967': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'e3e969f4': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('f8e6c967', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'a102d142': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('f8e6c967', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'b0cda17f': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('f8e6c967', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'e7263d9a': [(log, ('3.0: ZhuYuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'c84557c0': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e7263d9a', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'b7ad2492': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e7263d9a', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'93d2f31a': [
        (log, ('3.0: ZhuYuan weapon VB Hash',)),
        (add_section_if_missing, ('e7263d9a', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'1756495e': [(log, ('3.0: ZhuYuan misc hash',)),],
'33e6da2d': [(log, ('3.0: ZhuYuan misc hash',)),],
'3421e96d': [(log, ('3.0: ZhuYuan misc hash',)),],
'7ae1f70f': [(log, ('3.0: ZhuYuan misc hash',)),],
'7b103bdf': [(log, ('3.0: ZhuYuan misc hash',)),],
'b179d1e8': [(log, ('3.0: ZhuYuan misc hash',)),],
'd04cc3dd': [(log, ('3.0: ZhuYuan misc hash',)),],
'd853623a': [(log, ('3.0: ZhuYuan misc hash',)),],
'798adba3': [
        (log, ('3.0: ZhuYuan Hair TEX Hash',)),
        (add_section_if_missing, ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
    ],
'5ce66b3f': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'51280394': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'2a06612e': [
        (log, ('3.0: ZhuYuan weapon TEX Hash',)),
        (add_section_if_missing, ('a9188e3c', 'ZhuYuan.weapon.IB', 'match_priority = 0\n')),
    ],
'291f7f5a': [
        (log, ('3.0: ZhuYuan Body VB Hash',)),
        (add_section_if_missing, ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ZhuYuan',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
