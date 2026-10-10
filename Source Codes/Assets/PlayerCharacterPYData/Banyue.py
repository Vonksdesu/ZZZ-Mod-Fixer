"""
Banyue Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.4 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Banyue's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Body Component ====================
        '698046e6': [
            (log,                             ('2.4 - 3.2: Banyue Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1aab74cc': [
            (log,                             ('2.4 - 3.2: Banyue Body Draw VB Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        ],
        '6fab5f8b': [
            (log,                             ('2.4 - 3.2: Banyue Body Position VB Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        ],
        '9b4cef87': [
            (log,                             ('2.4 - 3.2: Banyue Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        ],
        'dba0d45e': [
            (log,                             ('2.4 - 3.2: Banyue Body Blend VB Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        ],
        '19c3125c': [
            (log,                             ('2.4 - 3.2: Banyue BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b3b968a5', 'Banyue.BodyA.Diffuse.1024')),
        ],
        'b3b968a5': [
            (log,                             ('2.4 - 3.2: Banyue BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('19c3125c', 'Banyue.BodyA.Diffuse.2048')),
        ],
        'f44f6316': [
            (log,                             ('2.4 - 3.2: Banyue BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdecf7ef', 'Banyue.BodyA.LightMap.1024')),
        ],
        'cdecf7ef': [
            (log,                             ('2.4 - 3.2: Banyue BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f6316', 'Banyue.BodyA.LightMap.2048')),
        ],
        '7099d2dc': [
            (log,                             ('2.4 - 3.2: Banyue BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77d743f8', 'Banyue.BodyA.MaterialMap.1024')),
        ],
        '77d743f8': [
            (log,                             ('2.4 - 3.2: Banyue BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7099d2dc', 'Banyue.BodyA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.4 - 3.2: Banyue BodyA, BothArmsA, LegA, FaceA, PalmsBallA and WeaponBallA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.BothArmsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.FaceA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.PalmsBallA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Banyue.WeaponBallA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.4 - 3.2: Banyue BodyA, BothArmsA, LegA, FaceA, PalmsBallA and WeaponBallA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.BothArmsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.FaceA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.PalmsBallA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Banyue.WeaponBallA.NormalMap.2048')),
        ],

        # ==================== BothArms Component ====================
        '635709b5': [
            (log,                             ('2.4 - 3.2: Banyue BothArms IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8e08205b': [
            (log,                             ('2.4 - 3.2: Banyue BothArms Draw VB Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
        ],
        '121a1aa7': [
            (log,                             ('2.4 - 3.2: Banyue BothArms Position VB Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
        ],
        'd17bb604': [
            (log,                             ('2.4 - 3.2: Banyue BothArms Texcoord VB Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
        ],
        '0bc8c485': [
            (log,                             ('2.4 - 3.2: Banyue BothArms Blend VB Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
        ],
        'd6a9d46e': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b91ab7b9', 'Banyue.BothArmsA.Diffuse.1024')),
        ],
        'b91ab7b9': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d6a9d46e', 'Banyue.BothArmsA.Diffuse.2048')),
        ],
        '46d2edd3': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2b682d6', 'Banyue.BothArmsA.LightMap.1024')),
        ],
        'a2b682d6': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('46d2edd3', 'Banyue.BothArmsA.LightMap.2048')),
        ],
        '721a29de': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d6ac66fa', 'Banyue.BothArmsA.MaterialMap.1024')),
        ],
        'd6ac66fa': [
            (log,                             ('2.4 - 3.2: Banyue BothArmsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('721a29de', 'Banyue.BothArmsA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '5f855404': [
            (log,                             ('2.4 - 3.2: Banyue Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ae8abe08': [
            (log,                             ('2.4 - 3.2: Banyue Leg Draw VB Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
        ],
        'dc2a8ff5': [
            (log,                             ('2.4 - 3.2: Banyue Leg Position VB Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
        ],
        '132c3f5c': [
            (log,                             ('2.4 - 3.2: Banyue Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
        ],
        'edc17446': [
            (log,                             ('2.4 - 3.2: Banyue Leg Blend VB Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
        ],
        'a75cf25e': [
            (log,                             ('2.4 - 3.2: Banyue LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('950ca70a', 'Banyue.LegA.Diffuse.1024')),
        ],
        '950ca70a': [
            (log,                             ('2.4 - 3.2: Banyue LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a75cf25e', 'Banyue.LegA.Diffuse.2048')),
        ],
        '1003c4df': [
            (log,                             ('2.4 - 3.2: Banyue LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('62c9fcaa', 'Banyue.LegA.LightMap.1024')),
        ],
        '62c9fcaa': [
            (log,                             ('2.4 - 3.2: Banyue LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1003c4df', 'Banyue.LegA.LightMap.2048')),
        ],
        '1125ccff': [
            (log,                             ('2.4 - 3.2: Banyue LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b0fcc7b', 'Banyue.LegA.MaterialMap.1024')),
        ],
        '8b0fcc7b': [
            (log,                             ('2.4 - 3.2: Banyue LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1125ccff', 'Banyue.LegA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'f3b6e869': [
            (log,                             ('2.4 - 3.2: Banyue Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0a12bb17': [
            (log,                             ('2.4 - 3.2: Banyue Face Draw VB Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
        ],
        '8be7477c': [
            (log,                             ('2.4 - 3.2: Banyue Face Position VB Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
        ],
        'ec9b7916': [
            (log,                             ('2.4 - 3.2: Banyue Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
        ],
        'bafd83bb': [
            (log,                             ('2.4 - 3.2: Banyue Face Blend VB Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
        ],
        '0a1f42fb': [
            (log,                             ('2.4 - 3.2: Banyue FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fc9c6235', 'Banyue.FaceA.Diffuse.1024')),
        ],
        'fc9c6235': [
            (log,                             ('2.4 - 3.2: Banyue FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0a1f42fb', 'Banyue.FaceA.Diffuse.2048')),
        ],
        '81cd7414': [
            (log,                             ('2.4 - 3.2: Banyue FaceA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c0d6d52', 'Banyue.FaceA.LightMap.1024')),
        ],
        '6c0d6d52': [
            (log,                             ('2.4 - 3.2: Banyue FaceA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81cd7414', 'Banyue.FaceA.LightMap.2048')),
        ],
        'ef8ba12a': [
            (log,                             ('2.4 - 3.2: Banyue FaceA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca2b8ca8', 'Banyue.FaceA.MaterialMap.1024')),
        ],
        'ca2b8ca8': [
            (log,                             ('2.4 - 3.2: Banyue FaceA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef8ba12a', 'Banyue.FaceA.MaterialMap.2048')),
        ],

        # ==================== PalmsBall Component ====================
        '084eb825': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBall IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '16698b4f': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBall Draw VB Hash',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        ],
        '679f2627': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBall Position VB Hash',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        ],
        'daf0e9f9': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBall Texcoord VB Hash',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        ],
        '3a3a9a42': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBall Blend VB Hash',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
        ],
        '3b8e4eda': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d70384d8', 'Banyue.PalmsBallA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d70384d8', 'Banyue.WeaponBallA.Diffuse.1024')),
        ],
        'd70384d8': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3b8e4eda', 'Banyue.PalmsBallA.Diffuse.2048')),
            (multiply_section_if_missing,     ('3b8e4eda', 'Banyue.WeaponBallA.Diffuse.2048')),
        ],
        '4a7ef137': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1be5d33e', 'Banyue.PalmsBallA.LightMap.1024')),
            (multiply_section_if_missing,     ('1be5d33e', 'Banyue.WeaponBallA.LightMap.1024')),
        ],
        '1be5d33e': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a7ef137', 'Banyue.PalmsBallA.LightMap.2048')),
            (multiply_section_if_missing,     ('4a7ef137', 'Banyue.WeaponBallA.LightMap.2048')),
        ],
        'cc671a53': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a0df0d6c', 'Banyue.PalmsBallA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('a0df0d6c', 'Banyue.WeaponBallA.MaterialMap.1024')),
        ],
        'a0df0d6c': [
            (log,                             ('2.4 - 3.2: Banyue PalmsBallA and WeaponBallA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cc671a53', 'Banyue.PalmsBallA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('cc671a53', 'Banyue.WeaponBallA.MaterialMap.2048')),
        ],

        # ==================== WeaponBall Component ====================
        '9bb1eb14': [
            (log,                             ('2.4 - 3.2: Banyue WeaponBall IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '00f0ed60': [
            (log,                             ('2.4 - 3.2: Banyue WeaponBall Draw VB Hash',)),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
        ],
        '289bb2ef': [
            (log,                             ('2.4 - 3.2: Banyue WeaponBall Position VB Hash',)),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
        ],
        'd6d66d05': [
            (log,                             ('2.4 - 3.2: Banyue WeaponBall Texcoord VB Hash',)),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
        ],
        '48237f26': [
            (log,                             ('2.4 - 3.2: Banyue WeaponBall Blend VB Hash',)),
            (add_section_if_missing,          ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Banyue',
    'game_versions': ['2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
