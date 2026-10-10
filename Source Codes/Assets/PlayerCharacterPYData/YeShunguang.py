"""
YeShunguang Character Hash Commands
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
    Returns YeShunguang's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '01ef4403': [
            (log,                             ('2.5 - 3.2: YeShunguang Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd9b6102': [
            (log,                             ('2.5 - 3.2: YeShunguang Hair Draw VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
        ],
        'f84ce9bf': [
            (log,                             ('2.5 - 3.2: YeShunguang Hair Position VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
        ],
        'afe311e8': [
            (log,                             ('2.5 - 3.2: YeShunguang Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
        ],
        'e841684d': [
            (log,                             ('2.5 - 3.2: YeShunguang Hair Blend VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
        ],
        '79f6acd7': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguang.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguang.FrontHairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguang.Headwear-FlowerA.Diffuse.1024')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguang.Headwear-ShortRibbonA.Diffuse.1024')),
        ],
        '3359b263': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguang.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguang.FrontHairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguang.Headwear-FlowerA.Diffuse.2048')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguang.Headwear-ShortRibbonA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, BraidA, BodyA, LegsA, TailA, Headwear-FlowerA, Headwear-LongRibbonA, Headwear-ShortRibbonA, ArmsRibbonsA, TransparentClothA, BackDecoration-TasselHeadA, SwordA, SwordBoxA and SwordBox-BallA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.FrontHairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.BraidA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.Headwear-FlowerA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.Headwear-LongRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.Headwear-ShortRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.ArmsRibbonsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.TransparentClothA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.BackDecoration-TasselHeadA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.SwordA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.SwordBoxA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguang.SwordBox-BallA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, BraidA, BodyA, LegsA, TailA, Headwear-FlowerA, Headwear-LongRibbonA, Headwear-ShortRibbonA, ArmsRibbonsA, TransparentClothA, BackDecoration-TasselHeadA, SwordA, SwordBoxA and SwordBox-BallA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.FrontHairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.BraidA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.Headwear-FlowerA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.Headwear-LongRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.Headwear-ShortRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.ArmsRibbonsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.TransparentClothA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.BackDecoration-TasselHeadA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.SwordA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.SwordBoxA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguang.SwordBox-BallA.NormalMap.2048')),
        ],
        '88269532': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguang.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguang.FrontHairA.LightMap.1024')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguang.Headwear-FlowerA.LightMap.1024')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguang.Headwear-ShortRibbonA.LightMap.1024')),
        ],
        '3c140ab4': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguang.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguang.FrontHairA.LightMap.2048')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguang.Headwear-FlowerA.LightMap.2048')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguang.Headwear-ShortRibbonA.LightMap.2048')),
        ],
        '825fbf26': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguang.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguang.FrontHairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguang.Headwear-FlowerA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguang.Headwear-ShortRibbonA.MaterialMap.1024')),
        ],
        'c009d7c9': [
            (log,                             ('2.5 - 3.2: YeShunguang HairA, FrontHairA, Headwear-FlowerA and Headwear-ShortRibbonA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguang.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguang.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguang.FrontHairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguang.Headwear-FlowerA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguang.Headwear-ShortRibbonA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        'bdf6d0eb': [
            (log,                             ('2.5 - 3.2: YeShunguang HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9e743bd7': [
            (log,                             ('2.5 - 3.2: YeShunguang HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '520b7f22': [
            (log,                             ('2.5 - 3.2: YeShunguang HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'af0e2b6e': [
            (log,                             ('2.5 - 3.2: YeShunguang HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '1e57173e': [
            (log,                             ('2.5 - 3.2: YeShunguang HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguang.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== FrontHair Component ====================
        '999bff94': [
            (log,                             ('2.5 - 3.2: YeShunguang FrontHair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '01d5a625': [
            (log,                             ('2.5 - 3.2: YeShunguang FrontHair Draw VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
        ],
        'bba40575': [
            (log,                             ('2.5 - 3.2: YeShunguang FrontHair Position VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
        ],
        'bea60077': [
            (log,                             ('2.5 - 3.2: YeShunguang FrontHair Texcoord VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
        ],
        '4ca25eef': [
            (log,                             ('2.5 - 3.2: YeShunguang FrontHair Blend VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguang.FrontHair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Braid Component ====================
        '38b3bd13': [
            (log,                             ('2.5 - 3.2: YeShunguang Braid IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e05bf3a8': [
            (log,                             ('2.5 - 3.2: YeShunguang Braid Draw VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
        ],
        'b871ef41': [
            (log,                             ('2.5 - 3.2: YeShunguang Braid Position VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
        ],
        'd7d41552': [
            (log,                             ('2.5 - 3.2: YeShunguang Braid Texcoord VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
        ],
        '06e29dd2': [
            (log,                             ('2.5 - 3.2: YeShunguang Braid Blend VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
        ],
        '804099eb': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6beec4cb', 'YeShunguang.BraidA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6beec4cb', 'YeShunguang.Headwear-LongRibbonA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6beec4cb', 'YeShunguang.BackDecoration-TasselHeadA.Diffuse.1024')),
        ],
        '6beec4cb': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('804099eb', 'YeShunguang.BraidA.Diffuse.2048')),
            (multiply_section_if_missing,     ('804099eb', 'YeShunguang.Headwear-LongRibbonA.Diffuse.2048')),
            (multiply_section_if_missing,     ('804099eb', 'YeShunguang.BackDecoration-TasselHeadA.Diffuse.2048')),
        ],
        '5ca93726': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('caa0726f', 'YeShunguang.BraidA.LightMap.1024')),
            (multiply_section_if_missing,     ('caa0726f', 'YeShunguang.Headwear-LongRibbonA.LightMap.1024')),
            (multiply_section_if_missing,     ('caa0726f', 'YeShunguang.BackDecoration-TasselHeadA.LightMap.1024')),
        ],
        'caa0726f': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ca93726', 'YeShunguang.BraidA.LightMap.2048')),
            (multiply_section_if_missing,     ('5ca93726', 'YeShunguang.Headwear-LongRibbonA.LightMap.2048')),
            (multiply_section_if_missing,     ('5ca93726', 'YeShunguang.BackDecoration-TasselHeadA.LightMap.2048')),
        ],
        '1ba6bebf': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0031ac91', 'YeShunguang.BraidA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('0031ac91', 'YeShunguang.Headwear-LongRibbonA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('0031ac91', 'YeShunguang.BackDecoration-TasselHeadA.MaterialMap.1024')),
        ],
        '0031ac91': [
            (log,                             ('2.5 - 3.2: YeShunguang BraidA, Headwear-LongRibbonA and BackDecoration-TasselHeadA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguang.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ba6bebf', 'YeShunguang.BraidA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1ba6bebf', 'YeShunguang.Headwear-LongRibbonA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1ba6bebf', 'YeShunguang.BackDecoration-TasselHeadA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'c209c22b': [
            (log,                             ('2.5 - 3.2: YeShunguang Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f201bd10': [
            (log,                             ('2.5 - 3.2: YeShunguang Body Draw VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
        ],
        '3239124c': [
            (log,                             ('2.5 - 3.2: YeShunguang Body Position VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
        ],
        'dbb027eb': [
            (log,                             ('2.5 - 3.2: YeShunguang Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
        ],
        'd1ffd339': [
            (log,                             ('2.5: YeShunguang TexCoord VB Hash',)),
            (update_hash,                     ('dbb027eb',)),
        ],
        '79c7949c': [
            (log,                             ('2.5 - 3.2: YeShunguang Body Blend VB Hash',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
        ],
        '5bd7d31b': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA, ArmsRibbonsA and TransparentClothA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9758a5db', 'YeShunguang.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9758a5db', 'YeShunguang.ArmsRibbonsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9758a5db', 'YeShunguang.TransparentClothA.Diffuse.1024')),
        ],
        '9758a5db': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA, ArmsRibbonsA and TransparentClothA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5bd7d31b', 'YeShunguang.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5bd7d31b', 'YeShunguang.ArmsRibbonsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5bd7d31b', 'YeShunguang.TransparentClothA.Diffuse.2048')),
        ],
        '72c1cf72': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA and ArmsRibbonsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b35315ee', 'YeShunguang.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('b35315ee', 'YeShunguang.ArmsRibbonsA.LightMap.1024')),
        ],
        'b35315ee': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA and ArmsRibbonsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('72c1cf72', 'YeShunguang.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('72c1cf72', 'YeShunguang.ArmsRibbonsA.LightMap.2048')),
        ],
        'a5872c6e': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA, ArmsRibbonsA and TransparentClothA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96fc91f0', 'YeShunguang.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('96fc91f0', 'YeShunguang.ArmsRibbonsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('96fc91f0', 'YeShunguang.TransparentClothA.MaterialMap.1024')),
        ],
        '96fc91f0': [
            (log,                             ('2.5 - 3.2: YeShunguang BodyA, ArmsRibbonsA and TransparentClothA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c209c22b', 'YeShunguang.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a5872c6e', 'YeShunguang.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a5872c6e', 'YeShunguang.ArmsRibbonsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a5872c6e', 'YeShunguang.TransparentClothA.MaterialMap.2048')),
        ],

        # ==================== Legs Component ====================
        '4a178546': [
            (log,                             ('2.5 - 3.2: YeShunguang Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '25033e92': [
            (log,                             ('2.5 - 3.2: YeShunguang Legs Draw VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
        ],
        '514dc7f3': [
            (log,                             ('2.5 - 3.2: YeShunguang Legs Position VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
        ],
        '5d7f073e': [
            (log,                             ('2.5 - 3.2: YeShunguang Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
        ],
        'fb37e9f8': [
            (log,                             ('2.5 - 3.2: YeShunguang Legs Blend VB Hash',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
        ],
        '727d3454': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('40985c98', 'YeShunguang.LegsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('40985c98', 'YeShunguang.TailA.Diffuse.1024')),
        ],
        '40985c98': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('727d3454', 'YeShunguang.LegsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('727d3454', 'YeShunguang.TailA.Diffuse.2048')),
        ],
        '4eb5aae2': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d5bc57f', 'YeShunguang.LegsA.LightMap.1024')),
            (multiply_section_if_missing,     ('7d5bc57f', 'YeShunguang.TailA.LightMap.1024')),
        ],
        '7d5bc57f': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4eb5aae2', 'YeShunguang.LegsA.LightMap.2048')),
            (multiply_section_if_missing,     ('4eb5aae2', 'YeShunguang.TailA.LightMap.2048')),
        ],
        '7f5f0193': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d6a9266', 'YeShunguang.LegsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('1d6a9266', 'YeShunguang.TailA.MaterialMap.1024')),
        ],
        '1d6a9266': [
            (log,                             ('2.5 - 3.2: YeShunguang LegsA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4a178546', 'YeShunguang.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f5f0193', 'YeShunguang.LegsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('7f5f0193', 'YeShunguang.TailA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '869976a3': [
            (log,                             ('2.5 - 3.2: YeShunguang Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3fe83226': [
            (log,                             ('2.5 - 3.2: YeShunguang Tail Draw VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
        ],
        '9a2dfc61': [
            (log,                             ('2.5 - 3.2: YeShunguang Tail Position VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
        ],
        'cb4b7cc7': [
            (log,                             ('2.5 - 3.2: YeShunguang Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
        ],
        '690ba2b1': [
            (log,                             ('2.5 - 3.2: YeShunguang Tail Blend VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguang.Tail.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-Flower Component ====================
        '8c8de427': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-Flower IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3a1f0236': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-Flower Draw VB Hash',)),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        'd89bbbfa': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-Flower Position VB Hash',)),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        'a4a4ad17': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-Flower Texcoord VB Hash',)),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        'd60923e0': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-Flower Blend VB Hash',)),
            (add_section_if_missing,          ('8c8de427', 'YeShunguang.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-LongRibbon Component ====================
        '9258d5f8': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-LongRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7ccb6725': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-LongRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '682c1e3c': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-LongRibbon Position VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '1e3923d1': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-LongRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '093ff56e': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-LongRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguang.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-ShortRibbon Component ====================
        'ae840e72': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-ShortRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a6f3e58f': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-ShortRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '47e62e43': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-ShortRibbon Position VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '504a82ea': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-ShortRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '852eedf5': [
            (log,                             ('2.5 - 3.2: YeShunguang Headwear-ShortRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('ae840e72', 'YeShunguang.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== ArmsRibbons Component ====================
        'f9ce7b07': [
            (log,                             ('2.5 - 3.2: YeShunguang ArmsRibbons IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '19c6b04a': [
            (log,                             ('2.5 - 3.2: YeShunguang ArmsRibbons Draw VB Hash',)),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        '0a74e427': [
            (log,                             ('2.5 - 3.2: YeShunguang ArmsRibbons Position VB Hash',)),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        'fc246482': [
            (log,                             ('2.5 - 3.2: YeShunguang ArmsRibbons Texcoord VB Hash',)),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],
        'd7558cdf': [
            (log,                             ('2.5 - 3.2: YeShunguang ArmsRibbons Blend VB Hash',)),
            (add_section_if_missing,          ('f9ce7b07', 'YeShunguang.ArmsRibbons.IB', 'match_priority = 0\n')),
        ],

        # ==================== TransparentCloth Component ====================
        '3b1b73fe': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentCloth IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '67a50546': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentCloth Draw VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '5bc3d9ca': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentCloth Position VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '441f1cf2': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentCloth Texcoord VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        'ae7d7235': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentCloth Blend VB Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '369a2106': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentClothA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fb42fdf', 'YeShunguang.TransparentClothA.LightMap.1024')),
        ],
        '1fb42fdf': [
            (log,                             ('2.5 - 3.2: YeShunguang TransparentClothA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3b1b73fe', 'YeShunguang.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('369a2106', 'YeShunguang.TransparentClothA.LightMap.2048')),
        ],

        # ==================== BackDecoration-TasselHead Component ====================
        '0534b536': [
            (log,                             ('2.5 - 3.2: YeShunguang BackDecoration-TasselHead IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a93cc204': [
            (log,                             ('2.5 - 3.2: YeShunguang BackDecoration-TasselHead Draw VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        'cad13a53': [
            (log,                             ('2.5 - 3.2: YeShunguang BackDecoration-TasselHead Position VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        '7e5fb476': [
            (log,                             ('2.5 - 3.2: YeShunguang BackDecoration-TasselHead Texcoord VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],
        'f9b50292': [
            (log,                             ('2.5 - 3.2: YeShunguang BackDecoration-TasselHead Blend VB Hash',)),
            (add_section_if_missing,          ('0534b536', 'YeShunguang.BackDecoration-TasselHead.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '611df76d': [
            (log,                             ('2.5 - 3.2: YeShunguang Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f0ab8cd': [
            (log,                             ('2.5 - 3.0: YeShunguang Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'a5182b8a': [
            (log,                             ('2.5 - 3.0: YeShunguang Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '287c161c': [
            (log,                             ('2.5 - 3.0: YeShunguang Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('014159dd',)),
        ],
        'f5daa764': [
            (log,                             ('2.5 - 3.0: YeShunguang Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '6ed0c951': [
            (log,                             ('2.5 - 3.2: YeShunguang EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('50f2ead2', 'YeShunguang.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('50f2ead2', 'YeShunguang.FaceA.Diffuse.1024')),
        ],
        '50f2ead2': [
            (log,                             ('2.5 - 3.2: YeShunguang EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguang.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ed0c951', 'YeShunguang.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6ed0c951', 'YeShunguang.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'c28e6303': [
            (log,                             ('2.5 - 3.2: YeShunguang Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f2f9780': [
            (log,                             ('2.5 - 3.2: YeShunguang Face Draw VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
        ],
        '153d04c7': [
            (log,                             ('2.5 - 3.2: YeShunguang Face Position VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
        ],
        'a1353cc8': [
            (log,                             ('2.5 - 3.1: YeShunguang Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bf705014',)),
        ],
        'bf705014': [
            (log,                             ('3.2: YeShunguang Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'fa261a46': [
            (log,                             ('2.5 - 3.2: YeShunguang Face Blend VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguang.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Sword Component ====================
        '93c3c2b7': [
            (log,                             ('2.5 - 3.2: YeShunguang Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f927c4bb': [
            (log,                             ('2.5 - 3.2: YeShunguang Sword Draw VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
        ],
        '4dc4764e': [
            (log,                             ('2.5 - 3.2: YeShunguang Sword Position VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
        ],
        'c8702180': [
            (log,                             ('2.5 - 3.2: YeShunguang Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
        ],
        '5783614d': [
            (log,                             ('2.5 - 3.2: YeShunguang Sword Blend VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
        ],
        '7eb1ca38': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f5e4bed0', 'YeShunguang.SwordA.Diffuse.1024')),
            (multiply_section_if_missing,     ('f5e4bed0', 'YeShunguang.SwordBox-BallA.Diffuse.1024')),
        ],
        'f5e4bed0': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7eb1ca38', 'YeShunguang.SwordA.Diffuse.2048')),
            (multiply_section_if_missing,     ('7eb1ca38', 'YeShunguang.SwordBox-BallA.Diffuse.2048')),
        ],
        '90250152': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c2c54664', 'YeShunguang.SwordA.LightMap.1024')),
            (multiply_section_if_missing,     ('c2c54664', 'YeShunguang.SwordBox-BallA.LightMap.1024')),
        ],
        'c2c54664': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('90250152', 'YeShunguang.SwordA.LightMap.2048')),
            (multiply_section_if_missing,     ('90250152', 'YeShunguang.SwordBox-BallA.LightMap.2048')),
        ],
        'a355e13d': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef4c4385', 'YeShunguang.SwordA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ef4c4385', 'YeShunguang.SwordBox-BallA.MaterialMap.1024')),
        ],
        'ef4c4385': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordA and SwordBox-BallA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguang.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a355e13d', 'YeShunguang.SwordA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a355e13d', 'YeShunguang.SwordBox-BallA.MaterialMap.2048')),
        ],

        # ==================== SwordBox Component ====================
        'd15c8cd9': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd0bc0522': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox Draw VB Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
        ],
        'b7b9a03a': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox Position VB Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
        ],
        '5b63465a': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox Texcoord VB Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
        ],
        'aff24453': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox Blend VB Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
        ],
        'f65635ed': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7f8046f', 'YeShunguang.SwordBoxA.Diffuse.1024')),
        ],
        'c7f8046f': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f65635ed', 'YeShunguang.SwordBoxA.Diffuse.2048')),
        ],
        '426d4871': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ba72780', 'YeShunguang.SwordBoxA.LightMap.1024')),
        ],
        '4ba72780': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('426d4871', 'YeShunguang.SwordBoxA.LightMap.2048')),
        ],
        'ae41d045': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('745fb007', 'YeShunguang.SwordBoxA.MaterialMap.1024')),
        ],
        '745fb007': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBoxA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d15c8cd9', 'YeShunguang.SwordBox.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ae41d045', 'YeShunguang.SwordBoxA.MaterialMap.2048')),
        ],

        # ==================== SwordBox-Ball Component ====================
        '5d842a9d': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox-Ball IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0da4c71b': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox-Ball Draw VB Hash',)),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
        ],
        'eaf14596': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox-Ball Position VB Hash',)),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
        ],
        'eaa601b5': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox-Ball Texcoord VB Hash',)),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
        ],
        'c1713762': [
            (log,                             ('2.5 - 3.2: YeShunguang SwordBox-Ball Blend VB Hash',)),
            (add_section_if_missing,          ('5d842a9d', 'YeShunguang.SwordBox-Ball.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguang',
    'game_versions': ['2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}

