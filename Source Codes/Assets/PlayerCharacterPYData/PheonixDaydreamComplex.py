"""
PheonixDaydreamComplex Character Hash Commands
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
    Returns PheonixDaydreamComplex's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ad90e710': [
            (log,                             ('3.3: PheonixDaydreamComplex Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '672c5dc6': [
            (log,                             ('3.3: PheonixDaydreamComplex Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
        ],
        '3632149d': [
            (log,                             ('3.3: PheonixDaydreamComplex Hair Position VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
        ],
        'e982ac3d': [
            (log,                             ('3.3: PheonixDaydreamComplex Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
        ],
        'efc69729': [
            (log,                             ('3.3: PheonixDaydreamComplex Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
        ],
        'f44f89de': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('616fa2d3', 'PheonixDaydreamComplex.HairA.Diffuse.1024')),
        ],
        '616fa2d3': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f89de', 'PheonixDaydreamComplex.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.BodyC.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PheonixDaydreamComplex.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.BodyC.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PheonixDaydreamComplex.weaponA.NormalMap.2048')),
        ],
        'dd2a6e00': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8650b8ea', 'PheonixDaydreamComplex.HairA.LightMap.1024')),
        ],
        '8650b8ea': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd2a6e00', 'PheonixDaydreamComplex.HairA.LightMap.2048')),
        ],
        'ab3560a0': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a308f19', 'PheonixDaydreamComplex.HairA.MaterialMap.1024')),
        ],
        '8a308f19': [
            (log,                             ('3.3: PheonixDaydreamComplex HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ad90e710', 'PheonixDaydreamComplex.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab3560a0', 'PheonixDaydreamComplex.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '35f435d6': [
            (log,                             ('3.3: PheonixDaydreamComplex HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ae826f3b': [
            (log,                             ('3.3: PheonixDaydreamComplex HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixDaydreamComplex.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '8e0fef21': [
            (log,                             ('3.3: PheonixDaydreamComplex HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixDaydreamComplex.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '6819ce1f': [
            (log,                             ('3.3: PheonixDaydreamComplex HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixDaydreamComplex.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '0c3af952': [
            (log,                             ('3.3: PheonixDaydreamComplex HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'PheonixDaydreamComplex.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headwear Component ====================
        'f16189da': [
            (log,                             ('3.3: PheonixDaydreamComplex Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'db462a2f': [
            (log,                             ('3.3: PheonixDaydreamComplex Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
        ],
        'e38f480e': [
            (log,                             ('3.3: PheonixDaydreamComplex Headwear Position VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
        ],
        '704504ea': [
            (log,                             ('3.3: PheonixDaydreamComplex Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
        ],
        '527c0b23': [
            (log,                             ('3.3: PheonixDaydreamComplex Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
        ],
        '048d2a12': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45b3179b', 'PheonixDaydreamComplex.HeadwearA.Diffuse.1024')),
            (multiply_section_if_missing,     ('45b3179b', 'PheonixDaydreamComplex.BodyB.Diffuse.1024')),
        ],
        '45b3179b': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('048d2a12', 'PheonixDaydreamComplex.HeadwearA.Diffuse.2048')),
            (multiply_section_if_missing,     ('048d2a12', 'PheonixDaydreamComplex.BodyB.Diffuse.2048')),
        ],
        'f50f67d0': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c40edaaf', 'PheonixDaydreamComplex.HeadwearA.LightMap.1024')),
            (multiply_section_if_missing,     ('c40edaaf', 'PheonixDaydreamComplex.BodyB.LightMap.1024')),
        ],
        'c40edaaf': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f50f67d0', 'PheonixDaydreamComplex.HeadwearA.LightMap.2048')),
            (multiply_section_if_missing,     ('f50f67d0', 'PheonixDaydreamComplex.BodyB.LightMap.2048')),
        ],
        '2b2b0797': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed0ed12a', 'PheonixDaydreamComplex.HeadwearA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ed0ed12a', 'PheonixDaydreamComplex.BodyB.MaterialMap.1024')),
        ],
        'ed0ed12a': [
            (log,                             ('3.3: PheonixDaydreamComplex HeadwearA and BodyB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f16189da', 'PheonixDaydreamComplex.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2b2b0797', 'PheonixDaydreamComplex.HeadwearA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2b2b0797', 'PheonixDaydreamComplex.BodyB.MaterialMap.2048')),
        ],

        # ==================== Diamond Component ====================
        '0e8484c2': [
            (log,                             ('3.3: PheonixDaydreamComplex Diamond IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6f4c7514': [
            (log,                             ('3.3: PheonixDaydreamComplex Diamond Draw VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
        ],
        'a62cf7aa': [
            (log,                             ('3.3: PheonixDaydreamComplex Diamond Position VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
        ],
        'ba28e264': [
            (log,                             ('3.3: PheonixDaydreamComplex Diamond Texcoord VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
        ],
        'b1748278': [
            (log,                             ('3.3: PheonixDaydreamComplex Diamond Blend VB Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
        ],
        '482bd07a': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e5817878', 'PheonixDaydreamComplex.DiamondA.Diffuse.1024')),
        ],
        'e5817878': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('482bd07a', 'PheonixDaydreamComplex.DiamondA.Diffuse.2048')),
        ],
        '0645411f': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf46cf2b', 'PheonixDaydreamComplex.DiamondA.LightMap.1024')),
        ],
        'cf46cf2b': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0645411f', 'PheonixDaydreamComplex.DiamondA.LightMap.2048')),
        ],
        '1ac02006': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fe34ddb', 'PheonixDaydreamComplex.DiamondA.MaterialMap.1024')),
        ],
        '1fe34ddb': [
            (log,                             ('3.3: PheonixDaydreamComplex DiamondA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('0e8484c2', 'PheonixDaydreamComplex.Diamond.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ac02006', 'PheonixDaydreamComplex.DiamondA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'a78033b2': [
            (log,                             ('3.3: PheonixDaydreamComplex Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c128a12b': [
            (log,                             ('3.3: PheonixDaydreamComplex Body Draw VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
        ],
        'a685de5f': [
            (log,                             ('3.3: PheonixDaydreamComplex Body Position VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
        ],
        '2047c603': [
            (log,                             ('3.3: PheonixDaydreamComplex Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
        ],
        'b011756a': [
            (log,                             ('3.3: PheonixDaydreamComplex Body Blend VB Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
        ],
        '8fa734cb': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf4ce589', 'PheonixDaydreamComplex.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf4ce589', 'PheonixDaydreamComplex.weaponA.Diffuse.1024')),
        ],
        'bf4ce589': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8fa734cb', 'PheonixDaydreamComplex.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8fa734cb', 'PheonixDaydreamComplex.weaponA.Diffuse.2048')),
        ],
        'f19ad816': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dcd83bf8', 'PheonixDaydreamComplex.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('dcd83bf8', 'PheonixDaydreamComplex.weaponA.LightMap.1024')),
        ],
        'dcd83bf8': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f19ad816', 'PheonixDaydreamComplex.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('f19ad816', 'PheonixDaydreamComplex.weaponA.LightMap.2048')),
        ],
        '0f4f608f': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('efe69785', 'PheonixDaydreamComplex.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('efe69785', 'PheonixDaydreamComplex.weaponA.MaterialMap.1024')),
        ],
        'efe69785': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyA and weaponA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0f4f608f', 'PheonixDaydreamComplex.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0f4f608f', 'PheonixDaydreamComplex.weaponA.MaterialMap.2048')),
        ],
        'f0e47142': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('839cd515', 'PheonixDaydreamComplex.BodyC.Diffuse.1024')),
        ],
        '839cd515': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0e47142', 'PheonixDaydreamComplex.BodyC.Diffuse.2048')),
        ],
        '614574e6': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22faf629', 'PheonixDaydreamComplex.BodyC.LightMap.1024')),
        ],
        '22faf629': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('614574e6', 'PheonixDaydreamComplex.BodyC.LightMap.2048')),
        ],
        '20f3bb14': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4d3ab7b2', 'PheonixDaydreamComplex.BodyC.MaterialMap.1024')),
        ],
        '4d3ab7b2': [
            (log,                             ('3.3: PheonixDaydreamComplex BodyC MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a78033b2', 'PheonixDaydreamComplex.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('20f3bb14', 'PheonixDaydreamComplex.BodyC.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'dbbf0aee': [
            (log,                             ('3.3: PheonixDaydreamComplex Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ca9f101d': [
            (log,                             ('3.3: PheonixDaydreamComplex Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f08d835a': [
            (log,                             ('3.3: PheonixDaydreamComplex Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f92a4f69': [
            (log,                             ('3.3: PheonixDaydreamComplex Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '79c94799': [
            (log,                             ('3.3: PheonixDaydreamComplex Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f15548c2': [
            (log,                             ('3.3: PheonixDaydreamComplex EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9868612e', 'PheonixDaydreamComplex.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9868612e', 'PheonixDaydreamComplex.FaceA.Diffuse.1024')),
        ],
        '9868612e': [
            (log,                             ('3.3: PheonixDaydreamComplex EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'PheonixDaydreamComplex.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f15548c2', 'PheonixDaydreamComplex.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f15548c2', 'PheonixDaydreamComplex.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd58b6350': [
            (log,                             ('3.3: PheonixDaydreamComplex Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd134a629': [
            (log,                             ('3.3: PheonixDaydreamComplex Face Draw VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
        ],
        'eb26356e': [
            (log,                             ('3.3: PheonixDaydreamComplex Face Position VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
        ],
        '5e60d462': [
            (log,                             ('3.3: PheonixDaydreamComplex Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
        ],
        'b9429bd4': [
            (log,                             ('3.3: PheonixDaydreamComplex Face Blend VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'PheonixDaydreamComplex.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        '0bcb1cb4': [
            (log,                             ('3.3: PheonixDaydreamComplex weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8bf0357a': [
            (log,                             ('3.3: PheonixDaydreamComplex weapon Draw VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
        ],
        'e211cd2e': [
            (log,                             ('3.3: PheonixDaydreamComplex weapon Position VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
        ],
        '467f7bd4': [
            (log,                             ('3.3: PheonixDaydreamComplex weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
        ],
        '05d7f849': [
            (log,                             ('3.3: PheonixDaydreamComplex weapon Blend VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'PheonixDaydreamComplex.weapon.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PheonixDaydreamComplex',
    'game_versions': ['3.3'],
}
