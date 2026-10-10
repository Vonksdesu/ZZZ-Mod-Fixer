"""
YeShunguangUlt Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5 - 3.2
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

        # ==================== Hair Component ====================
        '01ef4403': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd9b6102': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Hair Draw VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
        ],
        'f84ce9bf': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Hair Position VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
        ],
        'afe311e8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
        ],
        'e841684d': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Hair Blend VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
        ],
        'e8a8ac0b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, FrontHairB and Headwear-ShortRibbonA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b79da949', 'YeShunguangUlt.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b79da949', 'YeShunguangUlt.FrontHairB.Diffuse.1024')),
            (multiply_section_if_missing,     ('b79da949', 'YeShunguangUlt.Headwear-ShortRibbonA.Diffuse.1024')),
        ],
        '652e15a3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairB and FrontHairA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22ad0434', 'YeShunguangUlt.HairB.Diffuse.1024')),
            (multiply_section_if_missing,     ('22ad0434', 'YeShunguangUlt.FrontHairA.Diffuse.1024')),
        ],
        'b79da949': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, FrontHairB and Headwear-ShortRibbonA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8a8ac0b', 'YeShunguangUlt.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('e8a8ac0b', 'YeShunguangUlt.FrontHairB.Diffuse.2048')),
            (multiply_section_if_missing,     ('e8a8ac0b', 'YeShunguangUlt.Headwear-ShortRibbonA.Diffuse.2048')),
        ],
        '22ad0434': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairB and FrontHairA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('652e15a3', 'YeShunguangUlt.HairB.Diffuse.2048')),
            (multiply_section_if_missing,     ('652e15a3', 'YeShunguangUlt.FrontHairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB, BodyA, LegsA, TailA, Headwear-LongRibbonA, Headwear-ShortRibbonA, ArmsRibbonsA, TransparentClothA and BackDecoration-TasselHeadA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.HairB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.FrontHairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.FrontHairB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.Headwear-LongRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.Headwear-ShortRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.ArmsRibbonsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.TransparentClothA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangUlt.BackDecoration-TasselHeadA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB, BodyA, LegsA, TailA, Headwear-LongRibbonA, Headwear-ShortRibbonA, ArmsRibbonsA, TransparentClothA and BackDecoration-TasselHeadA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.HairB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.FrontHairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.FrontHairB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.Headwear-LongRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.Headwear-ShortRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.ArmsRibbonsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.TransparentClothA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangUlt.BackDecoration-TasselHeadA.NormalMap.2048')),
        ],
        '9f7defbc': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB and Headwear-ShortRibbonA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d8ce86a1', 'YeShunguangUlt.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('d8ce86a1', 'YeShunguangUlt.HairB.LightMap.1024')),
            (multiply_section_if_missing,     ('d8ce86a1', 'YeShunguangUlt.FrontHairA.LightMap.1024')),
            (multiply_section_if_missing,     ('d8ce86a1', 'YeShunguangUlt.FrontHairB.LightMap.1024')),
            (multiply_section_if_missing,     ('d8ce86a1', 'YeShunguangUlt.Headwear-ShortRibbonA.LightMap.1024')),
        ],
        'd8ce86a1': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB and Headwear-ShortRibbonA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f7defbc', 'YeShunguangUlt.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('9f7defbc', 'YeShunguangUlt.HairB.LightMap.2048')),
            (multiply_section_if_missing,     ('9f7defbc', 'YeShunguangUlt.FrontHairA.LightMap.2048')),
            (multiply_section_if_missing,     ('9f7defbc', 'YeShunguangUlt.FrontHairB.LightMap.2048')),
            (multiply_section_if_missing,     ('9f7defbc', 'YeShunguangUlt.Headwear-ShortRibbonA.LightMap.2048')),
        ],
        'c74f9710': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB and Headwear-ShortRibbonA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d864cc64', 'YeShunguangUlt.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d864cc64', 'YeShunguangUlt.HairB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d864cc64', 'YeShunguangUlt.FrontHairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d864cc64', 'YeShunguangUlt.FrontHairB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d864cc64', 'YeShunguangUlt.Headwear-ShortRibbonA.MaterialMap.1024')),
        ],
        'd864cc64': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairA, HairB, FrontHairA, FrontHairB and Headwear-ShortRibbonA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangUlt.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c74f9710', 'YeShunguangUlt.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c74f9710', 'YeShunguangUlt.HairB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c74f9710', 'YeShunguangUlt.FrontHairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c74f9710', 'YeShunguangUlt.FrontHairB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c74f9710', 'YeShunguangUlt.Headwear-ShortRibbonA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        'a9c76fcf': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '53b4c9f3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'ac4f1cc8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '0818885d': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '4654a675': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('a9c76fcf', 'YeShunguangUlt.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== FrontHair Component ====================
        'be28e18b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FrontHair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5234bbcb': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FrontHair Draw VB Hash',)),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
        ],
        '2f030baf': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FrontHair Position VB Hash',)),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
        ],
        '13343914': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FrontHair Texcoord VB Hash',)),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
        ],
        '0041e5e3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FrontHair Blend VB Hash',)),
            (add_section_if_missing,          ('be28e18b', 'YeShunguangUlt.FrontHair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'c209c22b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f201bd10': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Body Draw VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
        ],
        '3239124c': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Body Position VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
        ],
        'dbb027eb': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
        ],
        '79c7949c': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Body Blend VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
        ],
        '43ca3d50': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34097193', 'YeShunguangUlt.BodyA.Diffuse.1024')),
        ],
        '34097193': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('43ca3d50', 'YeShunguangUlt.BodyA.Diffuse.2048')),
        ],
        '369a2106': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA and TransparentClothA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fb42fdf', 'YeShunguangUlt.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('1fb42fdf', 'YeShunguangUlt.TransparentClothA.LightMap.1024')),
        ],
        '1fb42fdf': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA and TransparentClothA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('369a2106', 'YeShunguangUlt.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('369a2106', 'YeShunguangUlt.TransparentClothA.LightMap.2048')),
        ],
        'e41b12be': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e921a23', 'YeShunguangUlt.BodyA.MaterialMap.1024')),
        ],
        '0e921a23': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguangUlt.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e41b12be', 'YeShunguangUlt.BodyA.MaterialMap.2048')),
        ],

        # ==================== Legs Component ====================
        '4a178546': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '25033e92': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Legs Draw VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
        ],
        '514dc7f3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Legs Position VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
        ],
        '5d7f073e': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
        ],
        'fb37e9f8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Legs Blend VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
        ],
        '0b7c1487': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('60aa1cca', 'YeShunguangUlt.LegsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('60aa1cca', 'YeShunguangUlt.TailA.Diffuse.1024')),
        ],
        '60aa1cca': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0b7c1487', 'YeShunguangUlt.LegsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('0b7c1487', 'YeShunguangUlt.TailA.Diffuse.2048')),
        ],
        'afbdd8a1': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2cd88b0d', 'YeShunguangUlt.LegsA.LightMap.1024')),
            (multiply_section_if_missing,     ('2cd88b0d', 'YeShunguangUlt.TailA.LightMap.1024')),
        ],
        '2cd88b0d': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('afbdd8a1', 'YeShunguangUlt.LegsA.LightMap.2048')),
            (multiply_section_if_missing,     ('afbdd8a1', 'YeShunguangUlt.TailA.LightMap.2048')),
        ],
        '263992f5': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6261eabc', 'YeShunguangUlt.LegsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('6261eabc', 'YeShunguangUlt.TailA.MaterialMap.1024')),
        ],
        '6261eabc': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt LegsA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguangUlt.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('263992f5', 'YeShunguangUlt.LegsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('263992f5', 'YeShunguangUlt.TailA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '869976a3': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3fe83226': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Tail Draw VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
        ],
        '9a2dfc61': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Tail Position VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
        ],
        'cb4b7cc7': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
        ],
        '690ba2b1': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Tail Blend VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangUlt.Tail.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-LongRibbon Component ====================
        '9258d5f8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7ccb6725': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '682c1e3c': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbon Position VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '1e3923d1': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '093ff56e': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '804099eb': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6beec4cb', 'YeShunguangUlt.Headwear-LongRibbonA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6beec4cb', 'YeShunguangUlt.BackDecoration-TasselHeadA.Diffuse.1024')),
        ],
        '6beec4cb': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('804099eb', 'YeShunguangUlt.Headwear-LongRibbonA.Diffuse.2048')),
            (multiply_section_if_missing,     ('804099eb', 'YeShunguangUlt.BackDecoration-TasselHeadA.Diffuse.2048')),
        ],
        '0d70f7cd': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fc76ef5b', 'YeShunguangUlt.Headwear-LongRibbonA.LightMap.1024')),
            (multiply_section_if_missing,     ('fc76ef5b', 'YeShunguangUlt.BackDecoration-TasselHeadA.LightMap.1024')),
        ],
        'fc76ef5b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0d70f7cd', 'YeShunguangUlt.Headwear-LongRibbonA.LightMap.2048')),
            (multiply_section_if_missing,     ('0d70f7cd', 'YeShunguangUlt.BackDecoration-TasselHeadA.LightMap.2048')),
        ],
        '7bf83964': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0afd6ddf', 'YeShunguangUlt.Headwear-LongRibbonA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('0afd6ddf', 'YeShunguangUlt.BackDecoration-TasselHeadA.MaterialMap.1024')),
        ],
        '0afd6ddf': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-LongRibbonA and BackDecoration-TasselHeadA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangUlt.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7bf83964', 'YeShunguangUlt.Headwear-LongRibbonA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('7bf83964', 'YeShunguangUlt.BackDecoration-TasselHeadA.MaterialMap.2048')),
        ],

        # ==================== Headwear-ShortRibbon Component ====================
        'ae840e72': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-ShortRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a6f3e58f': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-ShortRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '47e62e43': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-ShortRibbon Position VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '504a82ea': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-ShortRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '852eedf5': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Headwear-ShortRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguangUlt.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== ArmsRibbons Component ====================
        '2d72a119': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbons IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ebdbb8db': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbons Draw VB Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        '4c1e777e': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbons Position VB Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        '49a95c22': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbons Texcoord VB Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        '649a0ed6': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbons Blend VB Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        '5bd7d31b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA and TransparentClothA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9758a5db', 'YeShunguangUlt.ArmsRibbonsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9758a5db', 'YeShunguangUlt.TransparentClothA.Diffuse.1024')),
        ],
        '9758a5db': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA and TransparentClothA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5bd7d31b', 'YeShunguangUlt.ArmsRibbonsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5bd7d31b', 'YeShunguangUlt.TransparentClothA.Diffuse.2048')),
        ],
        '72c1cf72': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b35315ee', 'YeShunguangUlt.ArmsRibbonsA.LightMap.1024')),
        ],
        'b35315ee': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('72c1cf72', 'YeShunguangUlt.ArmsRibbonsA.LightMap.2048')),
        ],
        'a5872c6e': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96fc91f0', 'YeShunguangUlt.ArmsRibbonsA.MaterialMap.1024')),
        ],
        '96fc91f0': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt ArmsRibbonsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2d72a119', 'YeShunguangUlt.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a5872c6e', 'YeShunguangUlt.ArmsRibbonsA.MaterialMap.2048')),
        ],

        # ==================== TransparentCloth Component ====================
        '3b1b73fe': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentCloth IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '67a50546': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentCloth Draw VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '5bc3d9ca': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentCloth Position VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '441f1cf2': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentCloth Texcoord VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        'ae7d7235': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentCloth Blend VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        'dd1adbe8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentClothA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b4a2abbc', 'YeShunguangUlt.TransparentClothA.MaterialMap.1024')),
        ],
        'b4a2abbc': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt TransparentClothA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguangUlt.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd1adbe8', 'YeShunguangUlt.TransparentClothA.MaterialMap.2048')),
        ],

        # ==================== BackDecoration-TasselHead Component ====================
        '0534b536': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BackDecoration-TasselHead IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a93cc204': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BackDecoration-TasselHead Draw VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        'cad13a53': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BackDecoration-TasselHead Position VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        '7e5fb476': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BackDecoration-TasselHead Texcoord VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        'f9b50292': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt BackDecoration-TasselHead Blend VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguangUlt.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '611df76d': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f0ab8cd': [
            (log,                             ('2.5 - 2.6: YeShunguangUlt Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '287c161c': [
            (log,                             ('2.5 - 2.6: YeShunguangUlt Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('014159dd',)),
        ],
        'f5daa764': [
            (log,                             ('2.5 - 2.6: YeShunguangUlt Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'ac8c7ca2': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt EyebrowA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f3d6be85', 'YeShunguangUlt.EyebrowA.Diffuse.1024')),
        ],
        'f3d6be85': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt EyebrowA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangUlt.Eyebrow.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac8c7ca2', 'YeShunguangUlt.EyebrowA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'c28e6303': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f2f9780': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Face Draw VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
        ],
        '153d04c7': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Face Position VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
        ],
        'a1353cc8': [
            (log,                             ('2.5 - 3.1: YeShunguangUlt Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bf705014',)),
        ],
        'bf705014': [
            (log,                             ('3.2: YeShunguangUlt Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'fa261a46': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Face Blend VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
        ],
        '6ed0c951': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('50f2ead2', 'YeShunguangUlt.FaceA.Diffuse.1024')),
        ],
        '50f2ead2': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangUlt.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ed0c951', 'YeShunguangUlt.FaceA.Diffuse.2048')),
        ],

        # ==================== Sword Component ====================
        'dd46b065': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3a44ca69': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Sword Draw VB Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
        ],
        '724d29ad': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Sword Position VB Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
        ],
        '2c36b1a8': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
        ],
        '2e3a5c01': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt Sword Blend VB Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
        ],
        '512d9f71': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb70b320', 'YeShunguangUlt.SwordA.Diffuse.1024')),
        ],
        'bb70b320': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('512d9f71', 'YeShunguangUlt.SwordA.Diffuse.2048')),
        ],
        '8842671b': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca8bd1e1', 'YeShunguangUlt.SwordA.NormalMap.1024')),
        ],
        'ca8bd1e1': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8842671b', 'YeShunguangUlt.SwordA.NormalMap.2048')),
        ],
        'd87a1e13': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8182cc59', 'YeShunguangUlt.SwordA.LightMap.1024')),
        ],
        '8182cc59': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d87a1e13', 'YeShunguangUlt.SwordA.LightMap.2048')),
        ],
        'ce96ea2f': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7b8275f5', 'YeShunguangUlt.SwordA.MaterialMap.1024')),
        ],
        '7b8275f5': [
            (log,                             ('2.5 - 3.2: YeShunguangUlt SwordA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('dd46b065', 'YeShunguangUlt.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ce96ea2f', 'YeShunguangUlt.SwordA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangUlt',
    'game_versions': ['2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
