"""
YeShunguang Character Hash Commands
ZZZ Mod Fixer v2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguang's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.5: YeShunguang Ears IB Hash',)),         (add_ib_check_if_missing,)],
'3b1b73fe': [(log, ('2.5: YeShunguang Strip IB Hash',)),        (add_ib_check_if_missing,)],
'4a178546': [(log, ('2.5: YeShunguang Legs IB Hash',)),         (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.5: YeShunguang Tail IB Hash',)),         (add_ib_check_if_missing,)],
'8c8de427': [(log, ('2.5: YeShunguang Clips IB Hash',)),        (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.5: YeShunguang Hair IB Hash',)),         (add_ib_check_if_missing,)],
'ae840e72': [(log, ('2.5: YeShunguang Antenna IB Hash',)),      (add_ib_check_if_missing,)],
'c209c22b': [(log, ('2.5: YeShunguang Torso IB Hash',)),        (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.5: YeShunguang Face IB Hash',)),         (add_ib_check_if_missing,)],
'f9ce7b07': [(log, ('2.5: YeShunguang ArmTassels IB Hash',)),   (add_ib_check_if_missing,)],
'0534b536': [(log, ('2.5: YeShunguang BackTassel IB Hash',)),   (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.5: YeShunguang BraidStrips IB Hash',)),  (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.5: YeShunguang Bow IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.5: YeShunguang Brows IB Hash',)),        (add_ib_check_if_missing,)],

# === VB Hashes ===
'd1ffd339': [(log, ('2.5: YeShunguang TexCoord VB Hash',)),     (update_hash, ('dbb027eb',))],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguang Shared NormalMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '3b1b73fe', '4a178546', '869976a3', '8c8de427', '999bff94', 'ae840e72', 'c209c22b', 'f9ce7b07', '0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face Textures ===
'6ed0c951': [
        (log,                           ('2.5: YeShunguang FaceA, BrowsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguang.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('50f2ead2', 'YeShunguang.FaceA.Diffuse.1024')),
    ],

'50f2ead2': [
        (log,                           ('2.5: YeShunguang FaceA, BrowsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguang.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6ed0c951', 'YeShunguang.FaceA.Diffuse.2048')),
    ],

# === Ears, Clips, Hair, Antenna Textures (Shared Set 1) ===
'79f6acd7': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3359b263', 'YeShunguang.HairA.Diffuse.1024')),
    ],

'3359b263': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('79f6acd7', 'YeShunguang.HairA.Diffuse.2048')),
    ],
'88269532': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3c140ab4', 'YeShunguang.HairA.LightMap.1024')),
    ],

'3c140ab4': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('88269532', 'YeShunguang.HairA.LightMap.2048')),
    ],
'825fbf26': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c009d7c9', 'YeShunguang.HairA.MaterialMap.1024')),
    ],

'c009d7c9': [
        (log,                           ('2.5: YeShunguang EarsA, ClipsA, HairA, AntennaA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('01ef4403', '8c8de427', '999bff94', 'ae840e72'), 'YeShunguang.EarsHairSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('825fbf26', 'YeShunguang.HairA.MaterialMap.2048')),
    ],

# === Strip, Torso, ArmTassels Textures (Shared Set 2) ===
'5bd7d31b': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9758a5db', 'YeShunguang.BodyA.Diffuse.1024')),
    ],

'9758a5db': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5bd7d31b', 'YeShunguang.BodyA.Diffuse.2048')),
    ],
'369a2106': [
        (log,                           ('2.5: YeShunguang StripA LightMap Hash',)),
        (add_section_if_missing,        ('3b1b73fe', 'YeShunguang.Strip.IB', 'match_priority = 0\n')),
    ],
'72c1cf72': [
        (log,                           ('2.5: YeShunguang TorsoA, ArmTasselsA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoArmSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b35315ee', 'YeShunguang.BodyA.LightMap.1024')),
    ],

'b35315ee': [
        (log,                           ('2.5: YeShunguang TorsoA, ArmTasselsA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoArmSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('72c1cf72', 'YeShunguang.BodyA.LightMap.2048')),
    ],
'a5872c6e': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('96fc91f0', 'YeShunguang.BodyA.MaterialMap.1024')),
    ],

'96fc91f0': [
        (log,                           ('2.5: YeShunguang StripA, TorsoA, ArmTasselsA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('3b1b73fe', 'c209c22b', 'f9ce7b07'), 'YeShunguang.TorsoSet.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a5872c6e', 'YeShunguang.BodyA.MaterialMap.2048')),
    ],

# === Legs, Tail Textures (Shared Set 3) ===
'727d3454': [
        (log,                           ('2.5: YeShunguang LegsA, TailA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('40985c98', 'YeShunguang.LegA.Diffuse.1024')),
    ],

'40985c98': [
        (log,                           ('2.5: YeShunguang LegsA, TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('727d3454', 'YeShunguang.LegA.Diffuse.2048')),
    ],
'4eb5aae2': [
        (log,                           ('2.5: YeShunguang LegsA, TailA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7d5bc57f', 'YeShunguang.LegA.LightMap.1024')),
    ],

'7d5bc57f': [
        (log,                           ('2.5: YeShunguang LegsA, TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4eb5aae2', 'YeShunguang.LegA.LightMap.2048')),
    ],
'7f5f0193': [
        (log,                           ('2.5: YeShunguang LegsA, TailA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1d6a9266', 'YeShunguang.LegA.MaterialMap.1024')),
    ],

'1d6a9266': [
        (log,                           ('2.5: YeShunguang LegsA, TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('4a178546', '869976a3'), 'YeShunguang.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7f5f0193', 'YeShunguang.LegA.MaterialMap.2048')),
    ],

# === BackTassel, BraidStrips, Bow Textures (Shared Set 4) ===
'804099eb': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA Diffuse Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'5ca93726': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA LightMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'1ba6bebf': [
        (log,                           ('2.5: YeShunguang BackTasselA, BraidStripsA, BowA MaterialMap Hash',)),
        (add_section_if_missing,        (('0534b536', '38b3bd13', '9258d5f8'), 'YeShunguang.TasselSet.IB', 'match_priority = 0\n')),
    ],
'f84ce9bf': [
        (log, ('3.0: YeShunguang Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
    ],
'afe311e8': [
        (log, ('3.0: YeShunguang Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
    ],
'e841684d': [
        (log, ('3.0: YeShunguang Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
    ],
'bdf6d0eb': [(log, ('3.0: YeShunguang HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'9e743bd7': [
        (log, ('3.0: YeShunguang HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
    ],
'520b7f22': [
        (log, ('3.0: YeShunguang HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
    ],
'af0e2b6e': [
        (log, ('3.0: YeShunguang HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
    ],
'1e57173e': [
        (log, ('3.0: YeShunguang HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
    ],
'01d5a625': [
        (log, ('3.0: YeShunguang FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
    ],
'bba40575': [
        (log, ('3.0: YeShunguang FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
    ],
'bea60077': [
        (log, ('3.0: YeShunguang FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
    ],
'4ca25eef': [
        (log, ('3.0: YeShunguang FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
    ],
'e05bf3a8': [
        (log, ('3.0: YeShunguang Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'b871ef41': [
        (log, ('3.0: YeShunguang Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'd7d41552': [
        (log, ('3.0: YeShunguang Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'06e29dd2': [
        (log, ('3.0: YeShunguang Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'f201bd10': [
        (log, ('3.0: YeShunguang Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
    ],
'3239124c': [
        (log, ('3.0: YeShunguang Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
    ],
'dbb027eb': [
        (log, ('3.0: YeShunguang Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
    ],
'79c7949c': [
        (log, ('3.0: YeShunguang Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
    ],
'25033e92': [
        (log, ('3.0: YeShunguang Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
    ],
'514dc7f3': [
        (log, ('3.0: YeShunguang Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
    ],
'5d7f073e': [
        (log, ('3.0: YeShunguang Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
    ],
'fb37e9f8': [
        (log, ('3.0: YeShunguang Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
    ],
'3fe83226': [
        (log, ('3.0: YeShunguang Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
    ],
'9a2dfc61': [
        (log, ('3.0: YeShunguang Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
    ],
'cb4b7cc7': [
        (log, ('3.0: YeShunguang Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
    ],
'690ba2b1': [
        (log, ('3.0: YeShunguang Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
    ],
'3a1f0236': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('8c8de427', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'd89bbbfa': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('8c8de427', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'a4a4ad17': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('8c8de427', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'd60923e0': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('8c8de427', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'7ccb6725': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'682c1e3c': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'1e3923d1': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'093ff56e': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'a6f3e58f': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'47e62e43': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'504a82ea': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'852eedf5': [
        (log, ('3.0: YeShunguang Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguang.Headwear.IB', 'match_priority = 0\n')),
    ],
'19c6b04a': [
        (log, ('3.0: YeShunguang ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'0a74e427': [
        (log, ('3.0: YeShunguang ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'fc246482': [
        (log, ('3.0: YeShunguang ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'd7558cdf': [
        (log, ('3.0: YeShunguang ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'67a50546': [
        (log, ('3.0: YeShunguang TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'5bc3d9ca': [
        (log, ('3.0: YeShunguang TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'441f1cf2': [
        (log, ('3.0: YeShunguang TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'ae7d7235': [
        (log, ('3.0: YeShunguang TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'a93cc204': [
        (log, ('3.0: YeShunguang BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguang.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'cad13a53': [
        (log, ('3.0: YeShunguang BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguang.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'7e5fb476': [
        (log, ('3.0: YeShunguang BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguang.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'f9b50292': [
        (log, ('3.0: YeShunguang BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguang.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'9f0ab8cd': [
        (log, ('3.0: YeShunguang Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'a5182b8a': [
        (log, ('3.0: YeShunguang Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'287c161c': [
        (log, ('3.0: YeShunguang Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f5daa764': [
        (log, ('3.0: YeShunguang Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'2f2f9780': [
        (log, ('3.0: YeShunguang Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],
'153d04c7': [
        (log, ('3.0: YeShunguang Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],
'a1353cc8': [
        (log, ('3.0: YeShunguang Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],
'fa261a46': [
        (log, ('3.0: YeShunguang Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
    ],
'93c3c2b7': [(log, ('3.0: YeShunguang Sword IB Hash',)), (add_ib_check_if_missing,)],
'f927c4bb': [
        (log, ('3.0: YeShunguang Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'4dc4764e': [
        (log, ('3.0: YeShunguang Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'c8702180': [
        (log, ('3.0: YeShunguang Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'5783614d': [
        (log, ('3.0: YeShunguang Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'7eb1ca38': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'90250152': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'a355e13d': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'd15c8cd9': [(log, ('3.0: YeShunguang SwordBox IB Hash',)), (add_ib_check_if_missing,)],
'd0bc0522': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'b7b9a03a': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'5b63465a': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'aff24453': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'f65635ed': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'426d4871': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'ae41d045': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'5d842a9d': [(log, ('3.0: YeShunguang SwordBox IB Hash',)), (add_ib_check_if_missing,)],
'0da4c71b': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'eaf14596': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'eaa601b5': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'c1713762': [
        (log, ('3.0: YeShunguang SwordBox VB Hash',)),
        (add_section_if_missing, ('5d842a9d', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: YeShunguang Hair TEX Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
    ],
'6beec4cb': [
        (log, ('3.0: YeShunguang Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'caa0726f': [
        (log, ('3.0: YeShunguang Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'0031ac91': [
        (log, ('3.0: YeShunguang Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
    ],
'1fb42fdf': [
        (log, ('3.0: YeShunguang TransparentCloth TEX Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'f5e4bed0': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'c2c54664': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'ef4c4385': [
        (log, ('3.0: YeShunguang Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
    ],
'c7f8046f': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'4ba72780': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'745fb007': [
        (log, ('3.0: YeShunguang SwordBox TEX Hash',)),
        (add_section_if_missing, ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
    ],
'bd9b6102': [
        (log, ('3.0: YeShunguang Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguang',
    'game_versions': ['2.5'],
}
