"""
BelleSummerSkies Character Hash Commands
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
    Returns BelleSummerSkies's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ea055cac': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('a7683988',)),
        ],
        'a7683988': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ff8f2723': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        'f0740488': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Position VB Hash',)),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        'af566e38': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '8823a09a': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '898f40fc': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Draw VB Hash',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        'd440bcc9': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Position VB Hash',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        'b536d9e6': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '4bb8fccc': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Blend VB Hash',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '20954729': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('afe23695', 'BelleSummerSkies.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('afe23695', 'BelleSummerSkies.TshirtA.Diffuse.1024')),
            (multiply_section_if_missing,     ('afe23695', 'BelleSummerSkies.HatA.Diffuse.1024')),
            (multiply_section_if_missing,     ('afe23695', 'BelleSummerSkies.BodyA.Diffuse.1024')),
        ],
        'afe23695': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('20954729', 'BelleSummerSkies.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('20954729', 'BelleSummerSkies.TshirtA.Diffuse.2048')),
            (multiply_section_if_missing,     ('20954729', 'BelleSummerSkies.HatA.Diffuse.2048')),
            (multiply_section_if_missing,     ('20954729', 'BelleSummerSkies.BodyA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA, BodyB, BodyC, EarPendantA and HairPinA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.TshirtA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.HatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.BodyC.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.EarPendantA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleSummerSkies.HairPinA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA, BodyB, BodyC, EarPendantA and HairPinA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.TshirtA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.HatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.BodyC.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.EarPendantA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleSummerSkies.HairPinA.NormalMap.2048')),
        ],
        'e0a86379': [
            (log,                             ('2.8 -> 3.0: BelleSummerSkies BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('60250d24',)),
        ],
        '60250d24': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('5978a2ca', 'a189eccd'), 'BelleSummerSkies.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('5978a2ca', 'a189eccd'), 'BelleSummerSkies.TshirtA.LightMap.1024')),
            (multiply_section_if_missing,     (('5978a2ca', 'a189eccd'), 'BelleSummerSkies.HatA.LightMap.1024')),
            (multiply_section_if_missing,     (('5978a2ca', 'a189eccd'), 'BelleSummerSkies.BodyA.LightMap.1024')),
        ],
        'a189eccd': [
            (log,                             ('2.8 -> 3.0: BelleSummerSkies BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('5978a2ca',)),
        ],
        '5978a2ca': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('60250d24', 'e0a86379'), 'BelleSummerSkies.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('60250d24', 'e0a86379'), 'BelleSummerSkies.TshirtA.LightMap.2048')),
            (multiply_section_if_missing,     (('60250d24', 'e0a86379'), 'BelleSummerSkies.HatA.LightMap.2048')),
            (multiply_section_if_missing,     (('60250d24', 'e0a86379'), 'BelleSummerSkies.BodyA.LightMap.2048')),
        ],
        '0298fba2': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fbaaeb92', 'BelleSummerSkies.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('fbaaeb92', 'BelleSummerSkies.TshirtA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('fbaaeb92', 'BelleSummerSkies.HatA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('fbaaeb92', 'BelleSummerSkies.BodyA.MaterialMap.1024')),
        ],
        'fbaaeb92': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies HairA, TshirtA, HatA, BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0298fba2', 'BelleSummerSkies.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0298fba2', 'BelleSummerSkies.TshirtA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0298fba2', 'BelleSummerSkies.HatA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0298fba2', 'BelleSummerSkies.BodyA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'fba5908c': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '403eace9': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8c70a1df': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'f98fb7ca': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ddf97ec8': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '0fba192e': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd077170c': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'f2298f2e': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '43f15315': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '288df448': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hat Component ====================
        '93f38bdd': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd2cf1bc': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hat Draw VB Hash',)),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        ],
        'c6b1cd55': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hat Position VB Hash',)),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        ],
        'a8b3bbab': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hat Texcoord VB Hash',)),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        ],
        'b7061769': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Hat Blend VB Hash',)),
            (add_section_if_missing,          ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '43ed3c22': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('619c5c94',)),
        ],
        '619c5c94': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2ceb44ef': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Body Draw VB Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '537d9b9b': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Body Position VB Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        'f5e62ded': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '6af00597': [
            (log,                             ('2.1 -> 2.2: BelleSummerSkies Body Blend Hash',)),
            (update_hash,                     ('4f3ddd5c',)),
        ],
        '4f3ddd5c': [
            (log,                             ('2.2 - 2.8: BelleSummerSkies Body Blend VB Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '051d5424': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Body Draw VB Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        'b95ddd01': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Body Position VB Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '91cdde70': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        'b36f6834': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Body Blend VB Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '24639b77': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9c7f71b', 'BelleSummerSkies.BodyB.Diffuse.1024')),
        ],
        'b9c7f71b': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('24639b77', 'BelleSummerSkies.BodyB.Diffuse.2048')),
        ],
        '7947679c': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a4d3687d', 'BelleSummerSkies.BodyB.LightMap.1024')),
        ],
        'a4d3687d': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7947679c', 'BelleSummerSkies.BodyB.LightMap.2048')),
        ],
        '33f28c6d': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b1abe877', 'BelleSummerSkies.BodyB.MaterialMap.1024')),
        ],
        'b1abe877': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33f28c6d', 'BelleSummerSkies.BodyB.MaterialMap.2048')),
        ],
        '1ce58567': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleSummerSkies.BodyC.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleSummerSkies.EarPendantA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleSummerSkies.HairPinA.Diffuse.1024')),
        ],
        '08f04d95': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleSummerSkies.BodyC.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleSummerSkies.EarPendantA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleSummerSkies.HairPinA.Diffuse.2048')),
        ],
        '7d562f53': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleSummerSkies.BodyC.LightMap.1024')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleSummerSkies.EarPendantA.LightMap.1024')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleSummerSkies.HairPinA.LightMap.1024')),
        ],
        'f44f330b': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleSummerSkies.BodyC.LightMap.2048')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleSummerSkies.EarPendantA.LightMap.2048')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleSummerSkies.HairPinA.LightMap.2048')),
        ],
        '34bdb036': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleSummerSkies.BodyC.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleSummerSkies.EarPendantA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleSummerSkies.HairPinA.MaterialMap.1024')),
        ],
        '7542ef4b': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies BodyC, EarPendantA and HairPinA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleSummerSkies.BodyC.MaterialMap.2048')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleSummerSkies.EarPendantA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleSummerSkies.HairPinA.MaterialMap.2048')),
        ],

        # ==================== Tshirt Component ====================
        '69148073': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Tshirt IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a1de68c0': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Tshirt Draw VB Hash',)),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
        ],
        '324d9d21': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Tshirt Position VB Hash',)),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
        ],
        '881514bf': [
            (log,                             ('2.8 -> 3.0: BelleSummerSkies Tshirt Texcoord Hash',)),
            (update_hash,                     ('325b4a1c',)),
        ],
        '325b4a1c': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Tshirt Texcoord VB Hash',)),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
        ],
        '65481194': [
            (log,                             ('2.1 -> 2.2: BelleSummerSkies Tshirt Blend Hash',)),
            (update_hash,                     ('0139f7e8',)),
        ],
        '0139f7e8': [
            (log,                             ('2.8 -> 3.0: BelleSummerSkies Tshirt Blend Hash',)),
            (update_hash,                     ('0a00d846',)),
        ],
        '0a00d846': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Tshirt Blend VB Hash',)),
            (add_section_if_missing,          ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '9a9780a7': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Face IB Hash (Shared with Belle)',)),
            (add_ib_check_if_missing,),
        ],
        '04abceb5': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Face Draw VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '3eb95df2': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies Face Position VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        ],
        'ccc76aea': [
            (log,                             ('2.2 -> 2.6: BelleSummerSkies Face Texcoord Hash',)),
            (update_hash,                     ('bcfc3326',)),
        ],
        'bcfc3326': [
            (log,                             ('2.6 - 2.7: BelleSummerSkies Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '0c9a075b': [
            (log,                             ('2.2 -> 3.0: BelleSummerSkies Face Blend Hash',)),
            (update_hash,                     ('359e4502',)),
        ],
        '359e4502': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies Face Blend VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '75ec3614': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies FaceA Diffuse 2048p Hash (Shared with Belle)',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77eef7e8', 'BelleSummerSkies.FaceA.Diffuse.1024')),
        ],
        '77eef7e8': [
            (log,                             ('2.2 - 3.2: BelleSummerSkies FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('75ec3614', 'BelleSummerSkies.FaceA.Diffuse.2048')),
        ],

        # ==================== EarPendant Component ====================
        '07920753': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies EarPendant IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c4e3b1e8': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies EarPendant Draw VB Hash',)),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
        ],
        '66a4bab6': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies EarPendant Position VB Hash',)),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
        ],
        'a2ee3518': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies EarPendant Texcoord VB Hash',)),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
        ],
        '28720ee7': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies EarPendant Blend VB Hash',)),
            (add_section_if_missing,          ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
        ],

        # ==================== HairPin Component ====================
        '3acf9aea': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairPin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '84a9dfca': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairPin Draw VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
        ],
        'a678dff4': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairPin Position VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
        ],
        '1196668a': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairPin Texcoord VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
        ],
        '6e583c52': [
            (log,                             ('3.0 - 3.2: BelleSummerSkies HairPin Blend VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleSummerSkies',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}

