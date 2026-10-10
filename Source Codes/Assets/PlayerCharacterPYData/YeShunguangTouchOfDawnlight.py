"""
YeShunguangTouchOfDawnlight Character Hash Commands
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
    Returns YeShunguangTouchOfDawnlight's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '01ef4403': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd9b6102': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Hair Draw VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'f84ce9bf': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Hair Position VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'afe311e8': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'e841684d': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Hair Blend VB Hash',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
        ],
        '79f6acd7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguangTouchOfDawnlight.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('3359b263', 'YeShunguangTouchOfDawnlight.FrontHairA.Diffuse.1024')),
        ],
        '3359b263': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguangTouchOfDawnlight.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('79f6acd7', 'YeShunguangTouchOfDawnlight.FrontHairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA, FrontHairA, BraidA, BodyA, LegA, SkirtA, TailA, Headwear-FlowerA, Headwear-LongRibbonA, Headwear-ShortRibbonA, RibbonFlowerA, TransparentClothA and SwordA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.FrontHairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.BraidA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.SkirtA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.TransparentClothA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YeShunguangTouchOfDawnlight.SwordA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA, FrontHairA, BraidA, BodyA, LegA, SkirtA, TailA, Headwear-FlowerA, Headwear-LongRibbonA, Headwear-ShortRibbonA, RibbonFlowerA, TransparentClothA and SwordA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.FrontHairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.BraidA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.SkirtA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.TransparentClothA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'YeShunguangTouchOfDawnlight.SwordA.NormalMap.2048')),
        ],
        '88269532': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguangTouchOfDawnlight.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('3c140ab4', 'YeShunguangTouchOfDawnlight.FrontHairA.LightMap.1024')),
        ],
        '3c140ab4': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguangTouchOfDawnlight.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('88269532', 'YeShunguangTouchOfDawnlight.FrontHairA.LightMap.2048')),
        ],
        '825fbf26': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguangTouchOfDawnlight.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c009d7c9', 'YeShunguangTouchOfDawnlight.FrontHairA.MaterialMap.1024')),
        ],
        'c009d7c9': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairA and FrontHairA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguangTouchOfDawnlight.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('825fbf26', 'YeShunguangTouchOfDawnlight.FrontHairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        'bdf6d0eb': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9e743bd7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '520b7f22': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'af0e2b6e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '1e57173e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== FrontHair Component ====================
        '999bff94': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight FrontHair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '01d5a625': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight FrontHair Draw VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
        ],
        'bba40575': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight FrontHair Position VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
        ],
        'bea60077': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight FrontHair Texcoord VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
        ],
        '4ca25eef': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight FrontHair Blend VB Hash',)),
            (add_section_if_missing,          ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Braid Component ====================
        '38b3bd13': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Braid IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e05bf3a8': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Braid Draw VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
        ],
        'b871ef41': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Braid Position VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
        ],
        'd7d41552': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Braid Texcoord VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
        ],
        '06e29dd2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Braid Blend VB Hash',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
        ],
        '8d400443': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('019fb20a', 'YeShunguangTouchOfDawnlight.BraidA.Diffuse.1024')),
            (multiply_section_if_missing,     ('019fb20a', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.Diffuse.1024')),
            (multiply_section_if_missing,     ('019fb20a', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.Diffuse.1024')),
        ],
        '019fb20a': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d400443', 'YeShunguangTouchOfDawnlight.BraidA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8d400443', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8d400443', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.Diffuse.2048')),
        ],
        '68e162a7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('656d2415', 'YeShunguangTouchOfDawnlight.BraidA.LightMap.1024')),
            (multiply_section_if_missing,     ('656d2415', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.LightMap.1024')),
            (multiply_section_if_missing,     ('656d2415', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.LightMap.1024')),
        ],
        '656d2415': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('68e162a7', 'YeShunguangTouchOfDawnlight.BraidA.LightMap.2048')),
            (multiply_section_if_missing,     ('68e162a7', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.LightMap.2048')),
            (multiply_section_if_missing,     ('68e162a7', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.LightMap.2048')),
        ],
        'fdd44e2a': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('926bffd5', 'YeShunguangTouchOfDawnlight.BraidA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('926bffd5', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('926bffd5', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.MaterialMap.1024')),
        ],
        '926bffd5': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BraidA, Headwear-LongRibbonA and RibbonFlowerA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fdd44e2a', 'YeShunguangTouchOfDawnlight.BraidA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('fdd44e2a', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbonA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('fdd44e2a', 'YeShunguangTouchOfDawnlight.RibbonFlowerA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        '8e7f72d5': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '506b7080': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Body Draw VB Hash',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
        ],
        '22213b25': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Body Position VB Hash',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
        ],
        '2a98d810': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
        ],
        'b827643b': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Body Blend VB Hash',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
        ],
        '956bcfbd': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cc360f56', 'YeShunguangTouchOfDawnlight.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc360f56', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc360f56', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc360f56', 'YeShunguangTouchOfDawnlight.TransparentClothA.Diffuse.1024')),
        ],
        'cc360f56': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('956bcfbd', 'YeShunguangTouchOfDawnlight.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('956bcfbd', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.Diffuse.2048')),
            (multiply_section_if_missing,     ('956bcfbd', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.Diffuse.2048')),
            (multiply_section_if_missing,     ('956bcfbd', 'YeShunguangTouchOfDawnlight.TransparentClothA.Diffuse.2048')),
        ],
        '8e815da2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8617f478', 'YeShunguangTouchOfDawnlight.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('8617f478', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.LightMap.1024')),
            (multiply_section_if_missing,     ('8617f478', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.LightMap.1024')),
            (multiply_section_if_missing,     ('8617f478', 'YeShunguangTouchOfDawnlight.TransparentClothA.LightMap.1024')),
        ],
        '8617f478': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8e815da2', 'YeShunguangTouchOfDawnlight.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('8e815da2', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.LightMap.2048')),
            (multiply_section_if_missing,     ('8e815da2', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.LightMap.2048')),
            (multiply_section_if_missing,     ('8e815da2', 'YeShunguangTouchOfDawnlight.TransparentClothA.LightMap.2048')),
        ],
        '2f2c27b5': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b2efbac8', 'YeShunguangTouchOfDawnlight.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('b2efbac8', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('b2efbac8', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('b2efbac8', 'YeShunguangTouchOfDawnlight.TransparentClothA.MaterialMap.1024')),
        ],
        'b2efbac8': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight BodyA, Headwear-FlowerA, Headwear-ShortRibbonA and TransparentClothA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2f2c27b5', 'YeShunguangTouchOfDawnlight.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2f2c27b5', 'YeShunguangTouchOfDawnlight.Headwear-FlowerA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2f2c27b5', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbonA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2f2c27b5', 'YeShunguangTouchOfDawnlight.TransparentClothA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '4df52aae': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b117fabb': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Leg Draw VB Hash',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
        ],
        '38b4c4e8': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Leg Position VB Hash',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
        ],
        'ea5a39d1': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
        ],
        '352c95b2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Leg Blend VB Hash',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
        ],
        '37c5aae5': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('03ed5c91', 'YeShunguangTouchOfDawnlight.LegA.Diffuse.1024')),
            (multiply_section_if_missing,     ('03ed5c91', 'YeShunguangTouchOfDawnlight.TailA.Diffuse.1024')),
        ],
        '03ed5c91': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('37c5aae5', 'YeShunguangTouchOfDawnlight.LegA.Diffuse.2048')),
            (multiply_section_if_missing,     ('37c5aae5', 'YeShunguangTouchOfDawnlight.TailA.Diffuse.2048')),
        ],
        '01e54e40': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4de697cf', 'YeShunguangTouchOfDawnlight.LegA.LightMap.1024')),
            (multiply_section_if_missing,     ('4de697cf', 'YeShunguangTouchOfDawnlight.TailA.LightMap.1024')),
        ],
        '4de697cf': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01e54e40', 'YeShunguangTouchOfDawnlight.LegA.LightMap.2048')),
            (multiply_section_if_missing,     ('01e54e40', 'YeShunguangTouchOfDawnlight.TailA.LightMap.2048')),
        ],
        '18370cad': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a7140533', 'YeShunguangTouchOfDawnlight.LegA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('a7140533', 'YeShunguangTouchOfDawnlight.TailA.MaterialMap.1024')),
        ],
        'a7140533': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight LegA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18370cad', 'YeShunguangTouchOfDawnlight.LegA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('18370cad', 'YeShunguangTouchOfDawnlight.TailA.MaterialMap.2048')),
        ],

        # ==================== Skirt Component ====================
        'bafd232d': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Skirt IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ff96a5d2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Skirt Draw VB Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
        ],
        '43eb20a0': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Skirt Position VB Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
        ],
        '1f27ab54': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Skirt Texcoord VB Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
        ],
        '6468f592': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Skirt Blend VB Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
        ],
        'f6d35967': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c87c6d8a', 'YeShunguangTouchOfDawnlight.SkirtA.Diffuse.1024')),
        ],
        'c87c6d8a': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f6d35967', 'YeShunguangTouchOfDawnlight.SkirtA.Diffuse.2048')),
        ],
        '405fa4b6': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('043b86d0', 'YeShunguangTouchOfDawnlight.SkirtA.LightMap.1024')),
        ],
        '043b86d0': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('405fa4b6', 'YeShunguangTouchOfDawnlight.SkirtA.LightMap.2048')),
        ],
        'e67e5577': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2ae050f', 'YeShunguangTouchOfDawnlight.SkirtA.MaterialMap.1024')),
        ],
        'a2ae050f': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SkirtA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e67e5577', 'YeShunguangTouchOfDawnlight.SkirtA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '869976a3': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3fe83226': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Tail Draw VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
        ],
        '9a2dfc61': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Tail Position VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
        ],
        'cb4b7cc7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
        ],
        '690ba2b1': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Tail Blend VB Hash',)),
            (add_section_if_missing,          ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-Flower Component ====================
        '6dc6c880': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-Flower IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0e30f719': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-Flower Draw VB Hash',)),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        '7fd64a5b': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-Flower Position VB Hash',)),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        '7105bdbb': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-Flower Texcoord VB Hash',)),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],
        '16a21c01': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-Flower Blend VB Hash',)),
            (add_section_if_missing,          ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear-Flower.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-LongRibbon Component ====================
        '9258d5f8': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-LongRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7ccb6725': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-LongRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '682c1e3c': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-LongRibbon Position VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '1e3923d1': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-LongRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],
        '093ff56e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-LongRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear-LongRibbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear-ShortRibbon Component ====================
        'f383537b': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-ShortRibbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3874c939': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-ShortRibbon Draw VB Hash',)),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        '1b410367': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-ShortRibbon Position VB Hash',)),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        'e71ea768': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-ShortRibbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],
        'ae7cced6': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Headwear-ShortRibbon Blend VB Hash',)),
            (add_section_if_missing,          ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear-ShortRibbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== RibbonFlower Component ====================
        '85d52cb7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight RibbonFlower IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a203c8fa': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight RibbonFlower Draw VB Hash',)),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
        ],
        '4c1d8708': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight RibbonFlower Position VB Hash',)),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
        ],
        'b8e7470f': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight RibbonFlower Texcoord VB Hash',)),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
        ],
        '917a4c3e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight RibbonFlower Blend VB Hash',)),
            (add_section_if_missing,          ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
        ],

        # ==================== TransparentCloth Component ====================
        'ba7164f5': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight TransparentCloth IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b040f517': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight TransparentCloth Draw VB Hash',)),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        'd98395a9': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight TransparentCloth Position VB Hash',)),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '0925ae65': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight TransparentCloth Texcoord VB Hash',)),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
        ],
        '651d14a2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight TransparentCloth Blend VB Hash',)),
            (add_section_if_missing,          ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '611df76d': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f0ab8cd': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'a5182b8a': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '287c161c': [
            (log,                             ('2.5 - 3.1: YeShunguangTouchOfDawnlight Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('014159dd',)),
        ],
        '014159dd': [
            (log,                             ('3.2: YeShunguangTouchOfDawnlight Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'f5daa764': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '6ed0c951': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('50f2ead2', 'YeShunguangTouchOfDawnlight.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('50f2ead2', 'YeShunguangTouchOfDawnlight.FaceA.Diffuse.1024')),
        ],
        '50f2ead2': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ed0c951', 'YeShunguangTouchOfDawnlight.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6ed0c951', 'YeShunguangTouchOfDawnlight.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'c28e6303': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f2f9780': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Face Draw VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
        ],
        '153d04c7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Face Position VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
        ],
        'a1353cc8': [
            (log,                             ('2.5 - 3.1: YeShunguangTouchOfDawnlight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bf705014',)),
        ],
        'bf705014': [
            (log,                             ('3.2: YeShunguangTouchOfDawnlight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'fa261a46': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Face Blend VB Hash',)),
            (add_section_if_missing,          ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Sword Component ====================
        '93c3c2b7': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f927c4bb': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Sword Draw VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
        ],
        '4dc4764e': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Sword Position VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
        ],
        'c8702180': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
        ],
        '5783614d': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight Sword Blend VB Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
        ],
        '7eb1ca38': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f5e4bed0', 'YeShunguangTouchOfDawnlight.SwordA.Diffuse.1024')),
        ],
        'f5e4bed0': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7eb1ca38', 'YeShunguangTouchOfDawnlight.SwordA.Diffuse.2048')),
        ],
        '90250152': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c2c54664', 'YeShunguangTouchOfDawnlight.SwordA.LightMap.1024')),
        ],
        'c2c54664': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('90250152', 'YeShunguangTouchOfDawnlight.SwordA.LightMap.2048')),
        ],
        'a355e13d': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef4c4385', 'YeShunguangTouchOfDawnlight.SwordA.MaterialMap.1024')),
        ],
        'ef4c4385': [
            (log,                             ('2.5 - 3.2: YeShunguangTouchOfDawnlight SwordA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a355e13d', 'YeShunguangTouchOfDawnlight.SwordA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangTouchOfDawnlight',
    'game_versions': ['2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
