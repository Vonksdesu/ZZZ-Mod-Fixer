"""
Pheonix Character Hash Commands
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
    Returns Pheonix's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ad90e710': [
            (log,                             ('3.3: Pheonix Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '672c5dc6': [
            (log,                             ('3.3: Pheonix Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
        ],
        '3632149d': [
            (log,                             ('3.3: Pheonix Hair Position VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
        ],
        'e982ac3d': [
            (log,                             ('3.3: Pheonix Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
        ],
        'efc69729': [
            (log,                             ('3.3: Pheonix Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
        ],
        'f44f89de': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('616fa2d3', 'Pheonix.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('616fa2d3', 'Pheonix.HeadwearA.Diffuse.1024')),
            (multiply_section_if_missing,     ('616fa2d3', 'Pheonix.BodyB.Diffuse.1024')),
        ],
        '616fa2d3': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f89de', 'Pheonix.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f44f89de', 'Pheonix.HeadwearA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f44f89de', 'Pheonix.BodyB.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.BodyC.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pheonix.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA, BodyA, BodyB, BodyC and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.BodyC.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pheonix.weaponA.NormalMap.2048')),
        ],
        'dd2a6e00': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8650b8ea', 'Pheonix.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('8650b8ea', 'Pheonix.HeadwearA.LightMap.1024')),
            (multiply_section_if_missing,     ('8650b8ea', 'Pheonix.BodyB.LightMap.1024')),
        ],
        '8650b8ea': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd2a6e00', 'Pheonix.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('dd2a6e00', 'Pheonix.HeadwearA.LightMap.2048')),
            (multiply_section_if_missing,     ('dd2a6e00', 'Pheonix.BodyB.LightMap.2048')),
        ],
        'ab3560a0': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a308f19', 'Pheonix.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('8a308f19', 'Pheonix.HeadwearA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('8a308f19', 'Pheonix.BodyB.MaterialMap.1024')),
        ],
        '8a308f19': [
            (log,                             ('3.3: Pheonix HairA, HeadwearA and BodyB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ad90e710', 'Pheonix.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab3560a0', 'Pheonix.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('ab3560a0', 'Pheonix.HeadwearA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('ab3560a0', 'Pheonix.BodyB.MaterialMap.2048')),
        ],

        # ==================== Headwear Component ====================
        'b11ff137': [
            (log,                             ('3.3: Pheonix Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '202db56f': [
            (log,                             ('3.3: Pheonix Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
        ],
        'c235beff': [
            (log,                             ('3.3: Pheonix Headwear Position VB Hash',)),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
        ],
        '68b29826': [
            (log,                             ('3.3: Pheonix Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
        ],
        'fe38014f': [
            (log,                             ('3.3: Pheonix Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('b11ff137', 'Pheonix.Headwear.IB', 'match_priority = 0\n')),
        ],

        # ==================== HairShadow Component ====================
        '35f435d6': [
            (log,                             ('3.3: Pheonix HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ae826f3b': [
            (log,                             ('3.3: Pheonix HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'Pheonix.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '8e0fef21': [
            (log,                             ('3.3: Pheonix HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'Pheonix.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '6819ce1f': [
            (log,                             ('3.3: Pheonix HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'Pheonix.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '0c3af952': [
            (log,                             ('3.3: Pheonix HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('35f435d6', 'Pheonix.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '9040e2c4': [
            (log,                             ('3.3: Pheonix Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4ac4d074': [
            (log,                             ('3.3: Pheonix Body Draw VB Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
        ],
        '66456501': [
            (log,                             ('3.3: Pheonix Body Position VB Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
        ],
        '5174be85': [
            (log,                             ('3.3: Pheonix Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
        ],
        '0fc8027f': [
            (log,                             ('3.3: Pheonix Body Blend VB Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
        ],
        '7951a137': [
            (log,                             ('3.3: Pheonix BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5c50ef9', 'Pheonix.BodyA.Diffuse.1024')),
        ],
        'd5c50ef9': [
            (log,                             ('3.3: Pheonix BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7951a137', 'Pheonix.BodyA.Diffuse.2048')),
        ],
        '8c794d9d': [
            (log,                             ('3.3: Pheonix BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3755c2f4', 'Pheonix.BodyA.LightMap.1024')),
        ],
        '3755c2f4': [
            (log,                             ('3.3: Pheonix BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8c794d9d', 'Pheonix.BodyA.LightMap.2048')),
        ],
        'abc0f706': [
            (log,                             ('3.3: Pheonix BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0c37438', 'Pheonix.BodyA.MaterialMap.1024')),
        ],
        'f0c37438': [
            (log,                             ('3.3: Pheonix BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('abc0f706', 'Pheonix.BodyA.MaterialMap.2048')),
        ],
        '8fa734cb': [
            (log,                             ('3.3: Pheonix BodyC and weaponA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf4ce589', 'Pheonix.BodyC.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf4ce589', 'Pheonix.weaponA.Diffuse.1024')),
        ],
        'bf4ce589': [
            (log,                             ('3.3: Pheonix BodyC and weaponA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8fa734cb', 'Pheonix.BodyC.Diffuse.2048')),
            (multiply_section_if_missing,     ('8fa734cb', 'Pheonix.weaponA.Diffuse.2048')),
        ],
        'f19ad816': [
            (log,                             ('3.3: Pheonix BodyC and weaponA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dcd83bf8', 'Pheonix.BodyC.LightMap.1024')),
            (multiply_section_if_missing,     ('dcd83bf8', 'Pheonix.weaponA.LightMap.1024')),
        ],
        'dcd83bf8': [
            (log,                             ('3.3: Pheonix BodyC and weaponA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f19ad816', 'Pheonix.BodyC.LightMap.2048')),
            (multiply_section_if_missing,     ('f19ad816', 'Pheonix.weaponA.LightMap.2048')),
        ],
        '0f4f608f': [
            (log,                             ('3.3: Pheonix BodyC and weaponA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('efe69785', 'Pheonix.BodyC.MaterialMap.1024')),
            (multiply_section_if_missing,     ('efe69785', 'Pheonix.weaponA.MaterialMap.1024')),
        ],
        'efe69785': [
            (log,                             ('3.3: Pheonix BodyC and weaponA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9040e2c4', 'Pheonix.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0f4f608f', 'Pheonix.BodyC.MaterialMap.2048')),
            (multiply_section_if_missing,     ('0f4f608f', 'Pheonix.weaponA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'dbbf0aee': [
            (log,                             ('3.3: Pheonix Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ca9f101d': [
            (log,                             ('3.3: Pheonix Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f08d835a': [
            (log,                             ('3.3: Pheonix Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f92a4f69': [
            (log,                             ('3.3: Pheonix Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '79c94799': [
            (log,                             ('3.3: Pheonix Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f15548c2': [
            (log,                             ('3.3: Pheonix EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9868612e', 'Pheonix.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9868612e', 'Pheonix.FaceA.Diffuse.1024')),
        ],
        '9868612e': [
            (log,                             ('3.3: Pheonix EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('dbbf0aee', 'Pheonix.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f15548c2', 'Pheonix.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f15548c2', 'Pheonix.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd58b6350': [
            (log,                             ('3.3: Pheonix Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd134a629': [
            (log,                             ('3.3: Pheonix Face Draw VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
        ],
        'eb26356e': [
            (log,                             ('3.3: Pheonix Face Position VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
        ],
        '5e60d462': [
            (log,                             ('3.3: Pheonix Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
        ],
        'b9429bd4': [
            (log,                             ('3.3: Pheonix Face Blend VB Hash',)),
            (add_section_if_missing,          ('d58b6350', 'Pheonix.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        '0bcb1cb4': [
            (log,                             ('3.3: Pheonix weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8bf0357a': [
            (log,                             ('3.3: Pheonix weapon Draw VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
        ],
        'e211cd2e': [
            (log,                             ('3.3: Pheonix weapon Position VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
        ],
        '467f7bd4': [
            (log,                             ('3.3: Pheonix weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
        ],
        '05d7f849': [
            (log,                             ('3.3: Pheonix weapon Blend VB Hash',)),
            (add_section_if_missing,          ('0bcb1cb4', 'Pheonix.weapon.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pheonix',
    'game_versions': ['3.3'],
}
