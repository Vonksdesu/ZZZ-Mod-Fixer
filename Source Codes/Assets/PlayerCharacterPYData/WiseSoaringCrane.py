"""
WiseSoaringCrane Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseSoaringCrane's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd5ca0411': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ef9c0510': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
        ],
        'e8df7ff3': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Position VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
        ],
        '774071dd': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
        ],
        'edfd1666': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane Hair Blend Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('68e4f572',)),
        ],
        '68e4f572': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
        ],
        '28005a5b': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cb0d0c22', 'WiseSoaringCrane.HairA.Diffuse.1024')),
        ],
        'cb0d0c22': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28005a5b', 'WiseSoaringCrane.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA, NeckA, BodyA, Waist accessoriesA, EarringsA, Cat Ear AccessoriesA, white badgeA, Orange green badgeA, Panda headgearA, Black orange ribbonA, Orange green ribbonA and glassesA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'WiseSoaringCrane.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseSoaringCrane.NeckA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseSoaringCrane.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseSoaringCrane.Waist accessoriesA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA, NeckA, BodyA and Waist accessoriesA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseSoaringCrane.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseSoaringCrane.NeckA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseSoaringCrane.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseSoaringCrane.Waist accessoriesA.NormalMap.2048')),
        ],
        '8d8269f8': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33368e12', 'WiseSoaringCrane.HairA.LightMap.1024')),
        ],
        '33368e12': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d8269f8', 'WiseSoaringCrane.HairA.LightMap.2048')),
        ],
        'f1b20f3d': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d9383a15', 'WiseSoaringCrane.HairA.MaterialMap.1024')),
        ],
        'd9383a15': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseSoaringCrane.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1b20f3d', 'WiseSoaringCrane.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '83e07a1b': [
            (log,                             ('2.0 -> 2.1: WiseSoaringCrane Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('8d08b190',)),
        ],
        '8d08b190': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'af5fc216': [
            (log,                             ('2.0 -> 2.1: WiseSoaringCrane Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('83e07a1b', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('681651f9',)),
        ],
        '681651f9': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '1a438b0d': [
            (log,                             ('2.0 -> 2.1: WiseSoaringCrane Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('83e07a1b', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('4af493e5',)),
        ],
        '4af493e5': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '7b7957fa': [
            (log,                             ('2.0 -> 2.1: WiseSoaringCrane Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('83e07a1b', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ad7d7eca',)),
        ],
        'ad7d7eca': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '52bd07dd': [
            (log,                             ('2.0 -> 2.1: WiseSoaringCrane Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('83e07a1b', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('795e9a7c',)),
        ],
        '795e9a7c': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WiseSoaringCrane.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Neck Component ====================
        '01c42a1d': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Neck IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '276e1373': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Neck Draw VB Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        ],
        'd8ad824b': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Neck Position VB Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        ],
        '39a1dfe3': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Neck Texcoord VB Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        ],
        '458bbde3': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane Neck Blend Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e0b1e734',)),
        ],
        'e0b1e734': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane Neck Blend VB Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
        ],
        '81406abe': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane NeckA, BodyA, white badgeA and Black orange ribbonA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('669191ec',)),
        ],
        '669191ec': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane NeckA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('23876240', '9fc3646e'), 'WiseSoaringCrane.NeckA.Diffuse.1024')),
            (multiply_section_if_missing,     (('23876240', '9fc3646e'), 'WiseSoaringCrane.BodyA.Diffuse.1024')),
        ],
        '9fc3646e': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane NeckA and BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('23876240',)),
        ],
        '23876240': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane NeckA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('669191ec', '81406abe'), 'WiseSoaringCrane.NeckA.Diffuse.2048')),
            (multiply_section_if_missing,     (('669191ec', '81406abe'), 'WiseSoaringCrane.BodyA.Diffuse.2048')),
        ],
        '05b25d35': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane NeckA, BodyA, white badgeA and Black orange ribbonA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd79b44b', 'WiseSoaringCrane.NeckA.LightMap.1024')),
            (multiply_section_if_missing,     ('dd79b44b', 'WiseSoaringCrane.BodyA.LightMap.1024')),
        ],
        'dd79b44b': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane NeckA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('05b25d35', 'WiseSoaringCrane.NeckA.LightMap.2048')),
            (multiply_section_if_missing,     ('05b25d35', 'WiseSoaringCrane.BodyA.LightMap.2048')),
        ],
        '24af1f48': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane NeckA, BodyA, white badgeA and Black orange ribbonA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa712fb9', 'WiseSoaringCrane.NeckA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('aa712fb9', 'WiseSoaringCrane.BodyA.MaterialMap.1024')),
        ],
        'aa712fb9': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane NeckA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('01c42a1d', 'WiseSoaringCrane.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('24af1f48', 'WiseSoaringCrane.NeckA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('24af1f48', 'WiseSoaringCrane.BodyA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        '6acc1eb8': [
            (log,                             ('2.4 -> 2.5: WiseSoaringCrane Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('1eca2097',)),
        ],
        '1eca2097': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4fa228f9': [
            (log,                             ('2.4 -> 2.5: WiseSoaringCrane Body Draw Hash',)),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ca02f614',)),
        ],
        'ca02f614': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Body Draw VB Hash',)),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        ],
        'ae59eabb': [
            (log,                             ('2.4 -> 2.5: WiseSoaringCrane Body Position Hash',)),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('a388eb6b',)),
        ],
        'a388eb6b': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Body Position VB Hash',)),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        ],
        'a83ada4e': [
            (log,                             ('2.4 -> 2.5: WiseSoaringCrane Body Texcoord Hash',)),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b39870e1',)),
        ],
        'b39870e1': [
            (log,                             ('2.5 - 3.2: WiseSoaringCrane Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        ],
        '177ad7e8': [
            (log,                             ('2.4 -> 2.5: WiseSoaringCrane Body Blend Hash',)),
            (add_section_if_missing,          ('6acc1eb8', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('8612559a',)),
        ],
        '8612559a': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane Body Blend Hash',)),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f28a6363',)),
        ],
        'f28a6363': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane Body Blend VB Hash',)),
            (add_section_if_missing,          ('1eca2097', 'WiseSoaringCrane.Body.IB', 'match_priority = 0\n')),
        ],

        # ==================== Waist accessories Component ====================
        'e7f527ea': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0c1c9bf3': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessories Draw VB Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
        ],
        '1e5cafee': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessories Position VB Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
        ],
        '06f42a6f': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
        ],
        '0a0aa1a8': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessories Blend VB Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
        ],
        '3fef0e14': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e590e6be', 'WiseSoaringCrane.Waist accessoriesA.Diffuse.1024')),
        ],
        'e590e6be': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3fef0e14', 'WiseSoaringCrane.Waist accessoriesA.Diffuse.2048')),
        ],
        '08b27f4a': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a78880dc', 'WiseSoaringCrane.Waist accessoriesA.LightMap.1024')),
        ],
        'a78880dc': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08b27f4a', 'WiseSoaringCrane.Waist accessoriesA.LightMap.2048')),
        ],
        'a15aa6b3': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a0b4014', 'WiseSoaringCrane.Waist accessoriesA.MaterialMap.1024')),
        ],
        '4a0b4014': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Waist accessoriesA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('e7f527ea', 'WiseSoaringCrane.Waist accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a15aa6b3', 'WiseSoaringCrane.Waist accessoriesA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '1fdaf388': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c4552bb': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        ],
        '5657c1fc': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane Face Position VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        ],
        'c83b6cbf': [
            (log,                             ('3.0 -> 3.1: WiseSoaringCrane Face Texcoord Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2b320847',)),
        ],
        '2b320847': [
            (log,                             ('3.1: WiseSoaringCrane Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        ],
        '757bc7cc': [
            (log,                             ('2.8 -> 3.0: WiseSoaringCrane Face Blend Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('015fbf96',)),
        ],
        '015fbf96': [
            (log,                             ('3.0 - 3.2: WiseSoaringCrane Face Blend VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
        ],
        '5d75fddc': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('588d7d2d', 'WiseSoaringCrane.FaceA.Diffuse.1024')),
        ],
        '588d7d2d': [
            (log,                             ('2.2 - 3.2: WiseSoaringCrane FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseSoaringCrane.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5d75fddc', 'WiseSoaringCrane.FaceA.Diffuse.2048')),
        ],

        # ==================== Earrings Component ====================
        'b856d397': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Earrings IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5a617015': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Earrings Draw VB Hash',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
        ],
        '49a9bab4': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Earrings Position VB Hash',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
        ],
        'a9b9bf40': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Earrings Texcoord VB Hash',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
        ],
        '686847cc': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Earrings Blend VB Hash',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
        ],
        'ed1a5b7f': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane EarringsA, Cat Ear AccessoriesA and glassesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
        'f5dc4198': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane EarringsA, Cat Ear AccessoriesA and glassesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
        '5346205a': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane EarringsA, Cat Ear AccessoriesA and glassesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b856d397', 'WiseSoaringCrane.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],

        # ==================== Cat Ear Accessories Component ====================
        'd0e278fc': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Cat Ear Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ad73aefc': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Cat Ear Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        '53b4170f': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Cat Ear Accessories Position VB Hash',)),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        '3280491f': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Cat Ear Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        '603fdb26': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Cat Ear Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('d0e278fc', 'WiseSoaringCrane.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],

        # ==================== white badge Component ====================
        '4e8b2454': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane white badge IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0406d75f': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane white badge Draw VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
        ],
        '13e791fa': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane white badge Position VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
        ],
        'fd95b568': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane white badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
        ],
        'e147258a': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane white badge Blend VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'WiseSoaringCrane.white badge.IB', 'match_priority = 0\n')),
        ],

        # ==================== Orange green badge Component ====================
        'eeabff55': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badge IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e0931b87': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badge Draw VB Hash',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        'fe8e2ff8': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badge Position VB Hash',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        'b6108302': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        'd9691e6b': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badge Blend VB Hash',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        '96ad58d4': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badgeA and Orange green ribbonA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        '8839d1fc': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badgeA and Orange green ribbonA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        'cd075caa': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green badgeA and Orange green ribbonA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('eeabff55', 'WiseSoaringCrane.Orange green badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== Panda headgear Component ====================
        'ac3a0dec': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e7d550d0': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgear Draw VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'c8a749b1': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgear Position VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'e938a289': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgear Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'ece854ad': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgear Blend VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'a2f096fc': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgearA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        '78c2d1dd': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgearA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        '2a7548a9': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Panda headgearA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'WiseSoaringCrane.Panda headgear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Black orange ribbon Component ====================
        'e5f8b021': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Black orange ribbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'aad48132': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Black orange ribbon Draw VB Hash',)),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
        ],
        '139c0e20': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Black orange ribbon Position VB Hash',)),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
        ],
        '0f705b4a': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Black orange ribbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
        ],
        'a60b2098': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Black orange ribbon Blend VB Hash',)),
            (add_section_if_missing,          ('e5f8b021', 'WiseSoaringCrane.Black orange ribbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== Orange green ribbon Component ====================
        'e5f269f4': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green ribbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2efc0d70': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green ribbon Draw VB Hash',)),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        'e801def3': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green ribbon Position VB Hash',)),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        'bc87900c': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green ribbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        '4851307e': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane Orange green ribbon Blend VB Hash',)),
            (add_section_if_missing,          ('e5f269f4', 'WiseSoaringCrane.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],

        # ==================== glasses Component ====================
        'bfce3c18': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane glasses IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ba8bde72': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane glasses Draw VB Hash',)),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
        '66cabdf9': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane glasses Position VB Hash',)),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
        'ac329cd7': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane glasses Texcoord VB Hash',)),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
        'a8620018': [
            (log,                             ('2.2 - 2.8: WiseSoaringCrane glasses Blend VB Hash',)),
            (add_section_if_missing,          ('bfce3c18', 'WiseSoaringCrane.glasses.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseSoaringCrane',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
