"""
Claret Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Claret's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '13596d7b': [
            (log,                             ('3.2: Claret Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'afd59133': [
            (log,                             ('3.2: Claret Hair Draw VB Hash',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
        ],
        'a15b4977': [
            (log,                             ('3.2: Claret Hair Position VB Hash',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
        ],
        '3323e267': [
            (log,                             ('3.2: Claret Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
        ],
        '8b8a3aee': [
            (log,                             ('3.2: Claret Hair Blend VB Hash',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
        ],
        '27ff9425': [
            (log,                             ('3.2: Claret HairA and HeadwearA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('539c1df5', 'Claret.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('539c1df5', 'Claret.HeadwearA.Diffuse.1024')),
        ],
        '539c1df5': [
            (log,                             ('3.2: Claret HairA and HeadwearA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('27ff9425', 'Claret.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('27ff9425', 'Claret.HeadwearA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.2: Claret HairA, HeadwearA, BodyA, LegA and weapon - 主体A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Claret.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Claret.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Claret.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Claret.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Claret.weapon - 主体A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.2: Claret HairA, HeadwearA, BodyA, LegA and weapon - 主体A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Claret.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Claret.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Claret.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Claret.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Claret.weapon - 主体A.NormalMap.2048')),
        ],
        '54af7ec2': [
            (log,                             ('3.2: Claret HairA and HeadwearA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ad8c918e', 'Claret.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('ad8c918e', 'Claret.HeadwearA.LightMap.1024')),
        ],
        'ad8c918e': [
            (log,                             ('3.2: Claret HairA and HeadwearA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54af7ec2', 'Claret.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('54af7ec2', 'Claret.HeadwearA.LightMap.2048')),
        ],
        'f328bcde': [
            (log,                             ('3.2: Claret HairA and HeadwearA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d32fb365', 'Claret.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d32fb365', 'Claret.HeadwearA.MaterialMap.1024')),
        ],
        'd32fb365': [
            (log,                             ('3.2: Claret HairA and HeadwearA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('13596d7b', 'Claret.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f328bcde', 'Claret.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f328bcde', 'Claret.HeadwearA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '55d7b71a': [
            (log,                             ('3.2: Claret HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Headwear Component ====================
        '480eeade': [
            (log,                             ('3.2: Claret Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3633bc1d': [
            (log,                             ('3.2: Claret Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
        ],
        '39f0a7d8': [
            (log,                             ('3.2: Claret Headwear Position VB Hash',)),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
        ],
        '8bdb2003': [
            (log,                             ('3.2: Claret Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
        ],
        'f3e22ccc': [
            (log,                             ('3.2: Claret Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('480eeade', 'Claret.Headwear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'd942b3a7': [
            (log,                             ('3.2: Claret Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd2c8aa32': [
            (log,                             ('3.2: Claret Body Draw VB Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
        ],
        'a71005c1': [
            (log,                             ('3.2: Claret Body Position VB Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
        ],
        '774b873a': [
            (log,                             ('3.2: Claret Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
        ],
        '9e4b673e': [
            (log,                             ('3.2: Claret Body Blend VB Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
        ],
        '49f33d8f': [
            (log,                             ('3.2: Claret BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e2cd795e', 'Claret.BodyA.Diffuse.1024')),
        ],
        'e2cd795e': [
            (log,                             ('3.2: Claret BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('49f33d8f', 'Claret.BodyA.Diffuse.2048')),
        ],
        '3327e83f': [
            (log,                             ('3.2: Claret BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6411f51e', 'Claret.BodyA.LightMap.1024')),
        ],
        '6411f51e': [
            (log,                             ('3.2: Claret BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3327e83f', 'Claret.BodyA.LightMap.2048')),
        ],
        '875e4282': [
            (log,                             ('3.2: Claret BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('38cb42d1', 'Claret.BodyA.MaterialMap.1024')),
        ],
        '38cb42d1': [
            (log,                             ('3.2: Claret BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d942b3a7', 'Claret.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('875e4282', 'Claret.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '98ece166': [
            (log,                             ('3.2: Claret Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4e0b27d3': [
            (log,                             ('3.2: Claret Leg Draw VB Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
        ],
        '5db64c7a': [
            (log,                             ('3.2: Claret Leg Position VB Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
        ],
        'ea4c2d82': [
            (log,                             ('3.2: Claret Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
        ],
        '350e55b3': [
            (log,                             ('3.2: Claret Leg Blend VB Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
        ],
        '54b5a00b': [
            (log,                             ('3.2: Claret LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76b905e9', 'Claret.LegA.Diffuse.1024')),
        ],
        '76b905e9': [
            (log,                             ('3.2: Claret LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54b5a00b', 'Claret.LegA.Diffuse.2048')),
        ],
        '83d81888': [
            (log,                             ('3.2: Claret LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7a3a0d91', 'Claret.LegA.LightMap.1024')),
        ],
        '7a3a0d91': [
            (log,                             ('3.2: Claret LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('83d81888', 'Claret.LegA.LightMap.2048')),
        ],
        '6c63f8ce': [
            (log,                             ('3.2: Claret LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('55d77a3a', 'Claret.LegA.MaterialMap.1024')),
        ],
        '55d77a3a': [
            (log,                             ('3.2: Claret LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('98ece166', 'Claret.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c63f8ce', 'Claret.LegA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'a56d773c': [
            (log,                             ('3.2: Claret Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '05b25205': [
            (log,                             ('3.2: Claret EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a56d773c', 'Claret.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3caf81d7', 'Claret.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('3caf81d7', 'Claret.FaceA.Diffuse.1024')),
        ],
        '3caf81d7': [
            (log,                             ('3.2: Claret EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a56d773c', 'Claret.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('05b25205', 'Claret.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('05b25205', 'Claret.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '6467d6c6': [
            (log,                             ('3.2: Claret Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '66804e03': [
            (log,                             ('3.2: Claret Face Draw VB Hash',)),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
        ],
        '5c92dd44': [
            (log,                             ('3.2: Claret Face Position VB Hash',)),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
        ],
        'bf09259d': [
            (log,                             ('3.2: Claret Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
        ],
        'c21ac1a5': [
            (log,                             ('3.2: Claret Face Blend VB Hash',)),
            (add_section_if_missing,          ('6467d6c6', 'Claret.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 主体 Component ====================
        '7e1354ab': [
            (log,                             ('3.2: Claret weapon - 主体 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '80d5b6d0': [
            (log,                             ('3.2: Claret weapon - 主体 Draw VB Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
        ],
        'f4b0040c': [
            (log,                             ('3.2: Claret weapon - 主体 Position VB Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
        ],
        'ec033fcd': [
            (log,                             ('3.2: Claret weapon - 主体 Texcoord VB Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
        ],
        'e20c6992': [
            (log,                             ('3.2: Claret weapon - 主体 Blend VB Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
        ],
        '9ff6afae': [
            (log,                             ('3.2: Claret weapon - 主体A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('98c65984', 'Claret.weapon - 主体A.Diffuse.1024')),
        ],
        '98c65984': [
            (log,                             ('3.2: Claret weapon - 主体A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ff6afae', 'Claret.weapon - 主体A.Diffuse.2048')),
        ],
        'a3fe0a37': [
            (log,                             ('3.2: Claret weapon - 主体A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d6dd0d4e', 'Claret.weapon - 主体A.LightMap.1024')),
        ],
        'd6dd0d4e': [
            (log,                             ('3.2: Claret weapon - 主体A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a3fe0a37', 'Claret.weapon - 主体A.LightMap.2048')),
        ],
        '7786fad6': [
            (log,                             ('3.2: Claret weapon - 主体A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a8aebda0', 'Claret.weapon - 主体A.MaterialMap.1024')),
        ],
        'a8aebda0': [
            (log,                             ('3.2: Claret weapon - 主体A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7e1354ab', 'Claret.weapon - 主体.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7786fad6', 'Claret.weapon - 主体A.MaterialMap.2048')),
        ],

        # ==================== weapon - 斧刃 Component ====================
        '0415192c': [
            (log,                             ('3.2: Claret weapon - 斧刃 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bac994dc': [
            (log,                             ('3.2: Claret weapon - 斧刃 Draw VB Hash',)),
            (add_section_if_missing,          ('0415192c', 'Claret.weapon - 斧刃.IB', 'match_priority = 0\n')),
        ],
        '25e25099': [
            (log,                             ('3.2: Claret weapon - 斧刃 Position VB Hash',)),
            (add_section_if_missing,          ('0415192c', 'Claret.weapon - 斧刃.IB', 'match_priority = 0\n')),
        ],
        '92faa9b5': [
            (log,                             ('3.2: Claret weapon - 斧刃 Texcoord VB Hash',)),
            (add_section_if_missing,          ('0415192c', 'Claret.weapon - 斧刃.IB', 'match_priority = 0\n')),
        ],
        'e4164046': [
            (log,                             ('3.2: Claret weapon - 斧刃 Blend VB Hash',)),
            (add_section_if_missing,          ('0415192c', 'Claret.weapon - 斧刃.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Claret',
    'game_versions': ['3.2'],
}
