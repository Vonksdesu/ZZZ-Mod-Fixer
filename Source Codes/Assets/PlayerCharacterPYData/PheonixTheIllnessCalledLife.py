"""
PheonixTheIllnessCalledLife Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.3
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      skip_unfixable_update, check_indexed_sections,
                      **kwargs):
    """
    Returns PheonixTheIllnessCalledLife's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ad90e710': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '672c5dc6': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
        ],
        '3632149d': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Hair Position VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
        ],
        'e982ac3d': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
        ],
        'efc69729': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
        ],
        'f44f89de': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('616fa2d3', 'PheonixTheIllnessCalledLife.HairA.Diffuse.1024')),
        ],
        '616fa2d3': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f89de', 'PheonixTheIllnessCalledLife.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.BodyC.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixTheIllnessCalledLife.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.BodyC.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixTheIllnessCalledLife.weaponA.NormalMap.2048')),
        ],
        'dd2a6e00': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8650b8ea', 'PheonixTheIllnessCalledLife.HairA.LightMap.1024')),
        ],
        '8650b8ea': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd2a6e00', 'PheonixTheIllnessCalledLife.HairA.LightMap.2048')),
        ],
        'ab3560a0': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a308f19', 'PheonixTheIllnessCalledLife.HairA.MaterialMap.1024')),
        ],
        '8a308f19': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixTheIllnessCalledLife.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab3560a0', 'PheonixTheIllnessCalledLife.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '35f435d6': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ae826f3b': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixTheIllnessCalledLife.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '8e0fef21': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixTheIllnessCalledLife.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '6819ce1f': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixTheIllnessCalledLife.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '0c3af952': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixTheIllnessCalledLife.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear Component ====================
        'f16189da': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'db462a2f': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
        ],
        'e38f480e': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Headwear Position VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
        ],
        '704504ea': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
        ],
        '527c0b23': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
        ],
        '048d2a12': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45b3179b', 'PheonixTheIllnessCalledLife.HeadwearA.Diffuse.1024')),
            (multiply_section_if_missing,     ('45b3179b', 'PheonixTheIllnessCalledLife.BodyB.Diffuse.1024')),
        ],
        '45b3179b': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('048d2a12', 'PheonixTheIllnessCalledLife.HeadwearA.Diffuse.2048')),
            (multiply_section_if_missing,     ('048d2a12', 'PheonixTheIllnessCalledLife.BodyB.Diffuse.2048')),
        ],
        'f50f67d0': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c40edaaf', 'PheonixTheIllnessCalledLife.HeadwearA.LightMap.1024')),
            (multiply_section_if_missing,     ('c40edaaf', 'PheonixTheIllnessCalledLife.BodyB.LightMap.1024')),
        ],
        'c40edaaf': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f50f67d0', 'PheonixTheIllnessCalledLife.HeadwearA.LightMap.2048')),
            (multiply_section_if_missing,     ('f50f67d0', 'PheonixTheIllnessCalledLife.BodyB.LightMap.2048')),
        ],
        '2b2b0797': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed0ed12a', 'PheonixTheIllnessCalledLife.HeadwearA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ed0ed12a', 'PheonixTheIllnessCalledLife.BodyB.MaterialMap.1024')),
        ],
        'ed0ed12a': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife HeadwearA and BodyB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixTheIllnessCalledLife.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2b2b0797', 'PheonixTheIllnessCalledLife.HeadwearA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2b2b0797', 'PheonixTheIllnessCalledLife.BodyB.MaterialMap.2048')),
        ],

        # ==================== Diamond Component ====================
        '0e8484c2': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Diamond IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6f4c7514': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Diamond Draw VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
        ],
        'a62cf7aa': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Diamond Position VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
        ],
        'ba28e264': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Diamond Texcoord VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
        ],
        'b1748278': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Diamond Blend VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
        ],
        '482bd07a': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e5817878', 'PheonixTheIllnessCalledLife.DiamondA.Diffuse.1024')),
            (multiply_section_if_missing,     ('e5817878', 'PheonixTheIllnessCalledLife.BodyC.Diffuse.1024')),
        ],
        'e5817878': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('482bd07a', 'PheonixTheIllnessCalledLife.DiamondA.Diffuse.2048')),
            (multiply_section_if_missing,     ('482bd07a', 'PheonixTheIllnessCalledLife.BodyC.Diffuse.2048')),
        ],
        '0645411f': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf46cf2b', 'PheonixTheIllnessCalledLife.DiamondA.LightMap.1024')),
            (multiply_section_if_missing,     ('cf46cf2b', 'PheonixTheIllnessCalledLife.BodyC.LightMap.1024')),
        ],
        'cf46cf2b': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0645411f', 'PheonixTheIllnessCalledLife.DiamondA.LightMap.2048')),
            (multiply_section_if_missing,     ('0645411f', 'PheonixTheIllnessCalledLife.BodyC.LightMap.2048')),
        ],
        '1ac02006': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fe34ddb', 'PheonixTheIllnessCalledLife.DiamondA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('1fe34ddb', 'PheonixTheIllnessCalledLife.BodyC.MaterialMap.1024')),
        ],
        '1fe34ddb': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife DiamondA and BodyC MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixTheIllnessCalledLife.Diamond.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ac02006', 'PheonixTheIllnessCalledLife.DiamondA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1ac02006', 'PheonixTheIllnessCalledLife.BodyC.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'a78033b2': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c128a12b': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Body Draw VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
        ],
        'a685de5f': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Body Position VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
        ],
        '2047c603': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
        ],
        'b011756a': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Body Blend VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
        ],
        '8fa734cb': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf4ce589', 'PheonixTheIllnessCalledLife.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf4ce589', 'PheonixTheIllnessCalledLife.weaponA.Diffuse.1024')),
        ],
        'bf4ce589': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8fa734cb', 'PheonixTheIllnessCalledLife.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8fa734cb', 'PheonixTheIllnessCalledLife.weaponA.Diffuse.2048')),
        ],
        'f19ad816': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dcd83bf8', 'PheonixTheIllnessCalledLife.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('dcd83bf8', 'PheonixTheIllnessCalledLife.weaponA.LightMap.1024')),
        ],
        'dcd83bf8': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f19ad816', 'PheonixTheIllnessCalledLife.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('f19ad816', 'PheonixTheIllnessCalledLife.weaponA.LightMap.2048')),
        ],
        '0f4f608f': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('efe69785', 'PheonixTheIllnessCalledLife.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('efe69785', 'PheonixTheIllnessCalledLife.weaponA.MaterialMap.1024')),
        ],
        'efe69785': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife BodyA and weaponA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixTheIllnessCalledLife.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0f4f608f', 'PheonixTheIllnessCalledLife.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0f4f608f', 'PheonixTheIllnessCalledLife.weaponA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'dbbf0aee': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ca9f101d': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f08d835a': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f92a4f69': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '79c94799': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f15548c2': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9868612e', 'PheonixTheIllnessCalledLife.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9868612e', 'PheonixTheIllnessCalledLife.FaceA.Diffuse.1024')),
        ],
        '9868612e': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixTheIllnessCalledLife.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f15548c2', 'PheonixTheIllnessCalledLife.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f15548c2', 'PheonixTheIllnessCalledLife.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd58b6350': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd134a629': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Face Draw VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
        ],
        'eb26356e': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Face Position VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
        ],
        '5e60d462': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
        ],
        'b9429bd4': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife Face Blend VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixTheIllnessCalledLife.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        '0bcb1cb4': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8bf0357a': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife weapon Draw VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
        ],
        'e211cd2e': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife weapon Position VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
        ],
        '467f7bd4': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
        ],
        '05d7f849': [
            (log,                             ('3.3: PheonixTheIllnessCalledLife weapon Blend VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixTheIllnessCalledLife.weapon.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PheonixTheIllnessCalledLife',
    'game_versions': ['3.3'],
}
