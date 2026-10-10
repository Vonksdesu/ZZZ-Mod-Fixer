"""
VelinaShadeOfLeisure Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns VelinaShadeOfLeisure's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '5eb66b57': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c60af8f1': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Hair Draw VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
        ],
        '53954bd7': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Hair Position VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
        ],
        '9f40d9d1': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
        ],
        'a1c210e2': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Hair Blend VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
        ],
        '5e6e492c': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('03002967', 'VelinaShadeOfLeisure.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('03002967', 'VelinaShadeOfLeisure.HairClipA.Diffuse.1024')),
        ],
        '03002967': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e6e492c', 'VelinaShadeOfLeisure.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5e6e492c', 'VelinaShadeOfLeisure.HairClipA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA, HairClipA, BodyA, BodyB, LegA, FanA and WeaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.HairClipA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.FanA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VelinaShadeOfLeisure.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA, HairClipA, BodyA, BodyB, LegA, FanA and WeaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.HairClipA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.FanA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VelinaShadeOfLeisure.WeaponA.NormalMap.2048')),
        ],
        '6b7dcb1b': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9c5d317', 'VelinaShadeOfLeisure.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('b9c5d317', 'VelinaShadeOfLeisure.HairClipA.LightMap.1024')),
        ],
        'b9c5d317': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b7dcb1b', 'VelinaShadeOfLeisure.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('6b7dcb1b', 'VelinaShadeOfLeisure.HairClipA.LightMap.2048')),
        ],
        '18018e7a': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ccf82282', 'VelinaShadeOfLeisure.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ccf82282', 'VelinaShadeOfLeisure.HairClipA.MaterialMap.1024')),
        ],
        'ccf82282': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairA and HairClipA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'VelinaShadeOfLeisure.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18018e7a', 'VelinaShadeOfLeisure.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('18018e7a', 'VelinaShadeOfLeisure.HairClipA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '6f33df95': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== HairClip Component ====================
        '73685503': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairClip IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '885c2ba8': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairClip Draw VB Hash',)),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
        ],
        'f10329bb': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairClip Position VB Hash',)),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
        ],
        'a71dc0ae': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairClip Texcoord VB Hash',)),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
        ],
        '363488a6': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure HairClip Blend VB Hash',)),
            (add_section_if_missing,          ('73685503', 'VelinaShadeOfLeisure.HairClip.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '0479bb8f': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cc427fff': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Body Draw VB Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        ],
        '6a0beedf': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Body Position VB Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        ],
        '5914c865': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        ],
        '7bdd845e': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Body Blend VB Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
        ],
        '988ded22': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f573933', 'VelinaShadeOfLeisure.BodyA.Diffuse.1024')),
        ],
        '3f573933': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('988ded22', 'VelinaShadeOfLeisure.BodyA.Diffuse.2048')),
        ],
        '48ece6e8': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22b4f8ab', 'VelinaShadeOfLeisure.BodyA.LightMap.1024')),
        ],
        '22b4f8ab': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('48ece6e8', 'VelinaShadeOfLeisure.BodyA.LightMap.2048')),
        ],
        'ed40f87e': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca53350a', 'VelinaShadeOfLeisure.BodyA.MaterialMap.1024')),
        ],
        'ca53350a': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed40f87e', 'VelinaShadeOfLeisure.BodyA.MaterialMap.2048')),
        ],
        '2ca3f765': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b3f5f0a6', 'VelinaShadeOfLeisure.BodyB.Diffuse.1024')),
        ],
        'b3f5f0a6': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2ca3f765', 'VelinaShadeOfLeisure.BodyB.Diffuse.2048')),
        ],
        '64b2da48': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a8072c81', 'VelinaShadeOfLeisure.BodyB.LightMap.1024')),
        ],
        'a8072c81': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('64b2da48', 'VelinaShadeOfLeisure.BodyB.LightMap.2048')),
        ],
        '7c2d3cdb': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('05e20bdc', 'VelinaShadeOfLeisure.BodyB.MaterialMap.1024')),
        ],
        '05e20bdc': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('0479bb8f', 'VelinaShadeOfLeisure.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7c2d3cdb', 'VelinaShadeOfLeisure.BodyB.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '2f94c7e8': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '87cd2937': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Leg Draw VB Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
        ],
        '938eb9f7': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Leg Position VB Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
        ],
        'b49b9651': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
        ],
        '112d2da2': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Leg Blend VB Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
        ],
        'f786f1ab': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6eaed274', 'VelinaShadeOfLeisure.LegA.Diffuse.1024')),
        ],
        '6eaed274': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f786f1ab', 'VelinaShadeOfLeisure.LegA.Diffuse.2048')),
        ],
        'bd0acdee': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('301301ff', 'VelinaShadeOfLeisure.LegA.LightMap.1024')),
        ],
        '301301ff': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd0acdee', 'VelinaShadeOfLeisure.LegA.LightMap.2048')),
        ],
        'ea9152d8': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('966cf15e', 'VelinaShadeOfLeisure.LegA.MaterialMap.1024')),
        ],
        '966cf15e': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2f94c7e8', 'VelinaShadeOfLeisure.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ea9152d8', 'VelinaShadeOfLeisure.LegA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        '1914d1e4': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f828e6a': [
            (log,                             ('3.0: VelinaShadeOfLeisure Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '38d54a4d': [
            (log,                             ('3.0: VelinaShadeOfLeisure Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '80e5ee4d': [
            (log,                             ('3.0: VelinaShadeOfLeisure Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f18dd23f': [
            (log,                             ('3.0: VelinaShadeOfLeisure Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '93ce2562': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e5409177', 'VelinaShadeOfLeisure.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('e5409177', 'VelinaShadeOfLeisure.FaceA.Diffuse.1024')),
        ],
        'e5409177': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1914d1e4', 'VelinaShadeOfLeisure.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93ce2562', 'VelinaShadeOfLeisure.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('93ce2562', 'VelinaShadeOfLeisure.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '6cfb2498': [
            (log,                             ('3.0 -> 3.1: VelinaShadeOfLeisure Face IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('2414f4b9',)),
        ],
        '2414f4b9': [
            (log,                             ('3.1: VelinaShadeOfLeisure Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '19ead1b7': [
            (log,                             ('3.0 -> 3.1: VelinaShadeOfLeisure Face Draw Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bfa3b361',)),
        ],
        'bfa3b361': [
            (log,                             ('3.1: VelinaShadeOfLeisure Face Draw VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
        ],
        '23f842f0': [
            (log,                             ('3.0 -> 3.1: VelinaShadeOfLeisure Face Position Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('85b12026',)),
        ],
        '85b12026': [
            (log,                             ('3.1: VelinaShadeOfLeisure Face Position VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
        ],
        '641bedfb': [
            (log,                             ('3.0 -> 3.1: VelinaShadeOfLeisure Face Texcoord Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('69304ff6',)),
        ],
        '69304ff6': [
            (log,                             ('3.1: VelinaShadeOfLeisure Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
        ],
        '98ecf569': [
            (log,                             ('3.0 -> 3.1: VelinaShadeOfLeisure Face Blend Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('76fe8eed',)),
        ],
        '76fe8eed': [
            (log,                             ('3.1: VelinaShadeOfLeisure Face Blend VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'VelinaShadeOfLeisure.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Fan Component ====================
        '9fbf4911': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Fan IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f496de0': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Fan Draw VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
        ],
        '738fb0b1': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Fan Position VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
        ],
        'f8e38f88': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Fan Texcoord VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
        ],
        '055b892d': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Fan Blend VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
        ],
        '185d733b': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5c55318', 'VelinaShadeOfLeisure.FanA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d5c55318', 'VelinaShadeOfLeisure.WeaponA.Diffuse.1024')),
        ],
        'd5c55318': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('185d733b', 'VelinaShadeOfLeisure.FanA.Diffuse.2048')),
            (multiply_section_if_missing,     ('185d733b', 'VelinaShadeOfLeisure.WeaponA.Diffuse.2048')),
        ],
        'e0e44e38': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5f7363aa', 'VelinaShadeOfLeisure.FanA.LightMap.1024')),
            (multiply_section_if_missing,     ('5f7363aa', 'VelinaShadeOfLeisure.WeaponA.LightMap.1024')),
        ],
        '5f7363aa': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e0e44e38', 'VelinaShadeOfLeisure.FanA.LightMap.2048')),
            (multiply_section_if_missing,     ('e0e44e38', 'VelinaShadeOfLeisure.WeaponA.LightMap.2048')),
        ],
        'b45cdc1a': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('edb1276e', 'VelinaShadeOfLeisure.FanA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('edb1276e', 'VelinaShadeOfLeisure.WeaponA.MaterialMap.1024')),
        ],
        'edb1276e': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure FanA and WeaponA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9fbf4911', 'VelinaShadeOfLeisure.Fan.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b45cdc1a', 'VelinaShadeOfLeisure.FanA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b45cdc1a', 'VelinaShadeOfLeisure.WeaponA.MaterialMap.2048')),
        ],

        # ==================== Weapon Component ====================
        '8ac40392': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1d3db60d': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4f3ab614': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Weapon Position VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
        ],
        '1b43f126': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4ba016b1': [
            (log,                             ('3.0 - 3.2: VelinaShadeOfLeisure Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'VelinaShadeOfLeisure.Weapon.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VelinaShadeOfLeisure',
    'game_versions': ['3.0', '3.1', '3.2'],
}
