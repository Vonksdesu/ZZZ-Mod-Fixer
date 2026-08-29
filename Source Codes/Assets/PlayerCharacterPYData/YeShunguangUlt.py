"""
YeShunguangUlt Character Hash Commands
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
    Returns YeShunguangUlt's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Body Textures (BodyA) ===
'34097193': [
        (log,                           ('2.5: YeShunguangUlt BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('43ca3d50', 'YeShunguangUlt.BodyA.Diffuse.2048')),
    ],
'43ca3d50': [
        (log,                           ('2.5: YeShunguangUlt BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('34097193', 'YeShunguangUlt.BodyA.Diffuse.1024')),
    ],
'1fb42fdf': [
        (log,                           ('2.5: YeShunguangUlt BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('369a2106', 'YeShunguangUlt.BodyA.LightMap.2048')),
    ],
'369a2106': [
        (log,                           ('2.5: YeShunguangUlt BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('1fb42fdf', 'YeShunguangUlt.BodyA.LightMap.1024')),
    ],
'0e921a23': [
        (log,                           ('2.5: YeShunguangUlt BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e41b12be', 'YeShunguangUlt.BodyA.MaterialMap.2048')),
    ],
'e41b12be': [
        (log,                           ('2.5: YeShunguangUlt BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('0e921a23', 'YeShunguangUlt.BodyA.MaterialMap.1024')),
    ],

# === Hair Textures (HairA) ===
'b79da949': [
        (log,                           ('2.5: YeShunguangUlt HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('e8a8ac0b', 'YeShunguangUlt.HairA.Diffuse.2048')),
    ],
'e8a8ac0b': [
        (log,                           ('2.5: YeShunguangUlt HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('b79da949', 'YeShunguangUlt.HairA.Diffuse.1024')),
    ],
'd8ce86a1': [
        (log,                           ('2.5: YeShunguangUlt HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('9f7defbc', 'YeShunguangUlt.HairA.LightMap.2048')),
    ],
'9f7defbc': [
        (log,                           ('2.5: YeShunguangUlt HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d8ce86a1', 'YeShunguangUlt.HairA.LightMap.1024')),
    ],
'd864cc64': [
        (log,                           ('2.5: YeShunguangUlt HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c74f9710', 'YeShunguangUlt.HairA.MaterialMap.2048')),
    ],
'c74f9710': [
        (log,                           ('2.5: YeShunguangUlt HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d864cc64', 'YeShunguangUlt.HairA.MaterialMap.1024')),
    ],

# === Hair Textures (HairB) ===
'22ad0434': [
        (log,                           ('2.5: YeShunguangUlt HairB Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('652e15a3', 'YeShunguangUlt.HairB.Diffuse.2048')),
    ],
'652e15a3': [
        (log,                           ('2.5: YeShunguangUlt HairB Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('22ad0434', 'YeShunguangUlt.HairB.Diffuse.1024')),
    ],

# === Leg Textures (LegA) ===
'60aa1cca': [
        (log,                           ('2.5: YeShunguangUlt LegA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('0b7c1487', 'YeShunguangUlt.LegA.Diffuse.2048')),
    ],
'0b7c1487': [
        (log,                           ('2.5: YeShunguangUlt LegA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('60aa1cca', 'YeShunguangUlt.LegA.Diffuse.1024')),
    ],
'2cd88b0d': [
        (log,                           ('2.5: YeShunguangUlt LegA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('afbdd8a1', 'YeShunguangUlt.LegA.LightMap.2048')),
    ],
'afbdd8a1': [
        (log,                           ('2.5: YeShunguangUlt LegA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('2cd88b0d', 'YeShunguangUlt.LegA.LightMap.1024')),
    ],
'6261eabc': [
        (log,                           ('2.5: YeShunguangUlt LegA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('263992f5', 'YeShunguangUlt.LegA.MaterialMap.2048')),
    ],
'263992f5': [
        (log,                           ('2.5: YeShunguangUlt LegA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('6261eabc', 'YeShunguangUlt.LegA.MaterialMap.1024')),
    ],
'2d72a119': [(log, ('3.0: YeShunguangUlt ArmsRibbons IB Hash',)), (add_ib_check_if_missing,)],
'49a95c22': [
        (log, ('3.0: YeShunguangUlt ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'4c1e777e': [
        (log, ('3.0: YeShunguangUlt ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'649a0ed6': [
        (log, ('3.0: YeShunguangUlt ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'ebdbb8db': [
        (log, ('3.0: YeShunguangUlt ArmsRibbons VB Hash',)),
        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: YeShunguangUlt ArmsRibbons Texture Hash',)),
        (add_section_if_missing, ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
    ],
'7e5fb476': [
        (log, ('3.0: YeShunguangUlt BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'a93cc204': [
        (log, ('3.0: YeShunguangUlt BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'cad13a53': [
        (log, ('3.0: YeShunguangUlt BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'f9b50292': [
        (log, ('3.0: YeShunguangUlt BackDecoration VB Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'0d70f7cd': [
        (log, ('3.0: YeShunguangUlt BackDecoration Texture Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'7bf83964': [
        (log, ('3.0: YeShunguangUlt BackDecoration Texture Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'6beec4cb': [
        (log, ('3.0: YeShunguangUlt BackDecoration Texture Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'fc76ef5b': [
        (log, ('3.0: YeShunguangUlt BackDecoration Texture Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'0afd6ddf': [
        (log, ('3.0: YeShunguangUlt BackDecoration Texture Hash',)),
        (add_section_if_missing, ('0534b536', 'YeShunguangUlt.BackDecoration.IB', 'match_priority = 0\n')),
    ],
'3239124c': [
        (log, ('3.0: YeShunguangUlt Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
    ],
'79c7949c': [
        (log, ('3.0: YeShunguangUlt Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
    ],
'dbb027eb': [
        (log, ('3.0: YeShunguangUlt Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
    ],
'f201bd10': [
        (log, ('3.0: YeShunguangUlt Body VB Hash',)),
        (add_section_if_missing, ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
    ],
'ac8c7ca2': [
        (log, ('3.0: YeShunguangUlt Eyebrow Texture Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f3d6be85': [
        (log, ('3.0: YeShunguangUlt Eyebrow Texture Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'153d04c7': [
        (log, ('3.0: YeShunguangUlt Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],
'2f2f9780': [
        (log, ('3.0: YeShunguangUlt Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],
'a1353cc8': [
        (log, ('3.0: YeShunguangUlt Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],
'fa261a46': [
        (log, ('3.0: YeShunguangUlt Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
    ],
'be28e18b': [(log, ('3.0: YeShunguangUlt FrontHair IB Hash',)), (add_ib_check_if_missing,)],
'0041e5e3': [
        (log, ('3.0: YeShunguangUlt FrontHair VB Hash',)),
        (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
    ],
'13343914': [
        (log, ('3.0: YeShunguangUlt FrontHair VB Hash',)),
        (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
    ],
'2f030baf': [
        (log, ('3.0: YeShunguangUlt FrontHair VB Hash',)),
        (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
    ],
'5234bbcb': [
        (log, ('3.0: YeShunguangUlt FrontHair VB Hash',)),
        (add_section_if_missing, ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
    ],
'afe311e8': [
        (log, ('3.0: YeShunguangUlt Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'bd9b6102': [
        (log, ('3.0: YeShunguangUlt Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'e841684d': [
        (log, ('3.0: YeShunguangUlt Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'f84ce9bf': [
        (log, ('3.0: YeShunguangUlt Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
    ],
'a9c76fcf': [(log, ('3.0: YeShunguangUlt HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'0818885d': [
        (log, ('3.0: YeShunguangUlt HairShadow VB Hash',)),
        (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
    ],
'4654a675': [
        (log, ('3.0: YeShunguangUlt HairShadow VB Hash',)),
        (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
    ],
'53b4c9f3': [
        (log, ('3.0: YeShunguangUlt HairShadow VB Hash',)),
        (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
    ],
'ac4f1cc8': [
        (log, ('3.0: YeShunguangUlt HairShadow VB Hash',)),
        (add_section_if_missing, ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
    ],
'093ff56e': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'1e3923d1': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'682c1e3c': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'7ccb6725': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'47e62e43': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'504a82ea': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'852eedf5': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'a6f3e58f': [
        (log, ('3.0: YeShunguangUlt Headwear VB Hash',)),
        (add_section_if_missing, ('ae840e72', 'YeShunguangUlt.Headwear.IB', 'match_priority = 0\n')),
    ],
'25033e92': [
        (log, ('3.0: YeShunguangUlt Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
    ],
'514dc7f3': [
        (log, ('3.0: YeShunguangUlt Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
    ],
'5d7f073e': [
        (log, ('3.0: YeShunguangUlt Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
    ],
'fb37e9f8': [
        (log, ('3.0: YeShunguangUlt Legs VB Hash',)),
        (add_section_if_missing, ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
    ],
'3fe83226': [
        (log, ('3.0: YeShunguangUlt Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
    ],
'690ba2b1': [
        (log, ('3.0: YeShunguangUlt Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
    ],
'9a2dfc61': [
        (log, ('3.0: YeShunguangUlt Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
    ],
'cb4b7cc7': [
        (log, ('3.0: YeShunguangUlt Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
    ],
'441f1cf2': [
        (log, ('3.0: YeShunguangUlt TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'5bc3d9ca': [
        (log, ('3.0: YeShunguangUlt TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'67a50546': [
        (log, ('3.0: YeShunguangUlt TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'ae7d7235': [
        (log, ('3.0: YeShunguangUlt TransparentCloth VB Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'dd1adbe8': [
        (log, ('3.0: YeShunguangUlt TransparentCloth Texture Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'b4a2abbc': [
        (log, ('3.0: YeShunguangUlt TransparentCloth Texture Hash',)),
        (add_section_if_missing, ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangUlt',
    'game_versions': ['2.5'],
}
