"""
Velina Character Hash Commands
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
    Returns Velina's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '5eb66b57': [
            (log,                             ('3.0 - 3.2: Velina Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c60af8f1': [
            (log,                             ('3.0 - 3.2: Velina Hair Draw VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
        ],
        '53954bd7': [
            (log,                             ('3.0 - 3.2: Velina Hair Position VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
        ],
        '9f40d9d1': [
            (log,                             ('3.0 - 3.2: Velina Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
        ],
        'a1c210e2': [
            (log,                             ('3.0 - 3.2: Velina Hair Blend VB Hash',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
        ],
        'dc6853c3': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('673e5da6', 'Velina.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('673e5da6', 'Velina.HairClipA.Diffuse.1024')),
        ],
        '673e5da6': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc6853c3', 'Velina.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('dc6853c3', 'Velina.HairClipA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.0 - 3.2: Velina HairA, HairClipA, BodyA, LegA, WeaponA and FanA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.HairClipA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Velina.FanA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.0 - 3.2: Velina HairA, HairClipA, BodyA, LegA, WeaponA and FanA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.HairClipA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Velina.FanA.NormalMap.2048')),
        ],
        'f06d3a26': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54fc678e', 'Velina.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('54fc678e', 'Velina.HairClipA.LightMap.1024')),
        ],
        '54fc678e': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f06d3a26', 'Velina.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('f06d3a26', 'Velina.HairClipA.LightMap.2048')),
        ],
        '4951b2a2': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ccbcd045', 'Velina.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ccbcd045', 'Velina.HairClipA.MaterialMap.1024')),
        ],
        'ccbcd045': [
            (log,                             ('3.0 - 3.2: Velina HairA and HairClipA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4951b2a2', 'Velina.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4951b2a2', 'Velina.HairClipA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '6f33df95': [
            (log,                             ('3.0 - 3.2: Velina HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== HairClip Component ====================
        '6c0b932e': [
            (log,                             ('3.0 - 3.2: Velina HairClip IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a364c911': [
            (log,                             ('3.0 - 3.2: Velina HairClip Draw VB Hash',)),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
        ],
        'cb6147f9': [
            (log,                             ('3.0 - 3.2: Velina HairClip Position VB Hash',)),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
        ],
        '4b702182': [
            (log,                             ('3.0 - 3.2: Velina HairClip Texcoord VB Hash',)),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
        ],
        'bd043a8e': [
            (log,                             ('3.0 - 3.2: Velina HairClip Blend VB Hash',)),
            (add_section_if_missing,          ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '1300e048': [
            (log,                             ('3.0 - 3.2: Velina Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f62f81f': [
            (log,                             ('3.0 - 3.2: Velina Body Draw VB Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
        ],
        '0b4b3a1f': [
            (log,                             ('3.0 - 3.2: Velina Body Position VB Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
        ],
        '1f1c042b': [
            (log,                             ('3.0 - 3.2: Velina Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
        ],
        '2c2ccd38': [
            (log,                             ('3.0 - 3.2: Velina Body Blend VB Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
        ],
        '93c61891': [
            (log,                             ('3.0 - 3.2: Velina BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9a8e3ba', 'Velina.BodyA.Diffuse.1024')),
        ],
        'f9a8e3ba': [
            (log,                             ('3.0 - 3.2: Velina BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93c61891', 'Velina.BodyA.Diffuse.2048')),
        ],
        '9a16d70e': [
            (log,                             ('3.0 - 3.2: Velina BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5562351c', 'Velina.BodyA.LightMap.1024')),
        ],
        '5562351c': [
            (log,                             ('3.0 - 3.2: Velina BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9a16d70e', 'Velina.BodyA.LightMap.2048')),
        ],
        'bb1d0172': [
            (log,                             ('3.0 - 3.2: Velina BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('531320a5', 'Velina.BodyA.MaterialMap.1024')),
        ],
        '531320a5': [
            (log,                             ('3.0 - 3.2: Velina BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb1d0172', 'Velina.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '6b25e6d8': [
            (log,                             ('3.0 - 3.2: Velina Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '10675a0f': [
            (log,                             ('3.0 - 3.2: Velina Leg Draw VB Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
        ],
        'adba03f3': [
            (log,                             ('3.0 - 3.2: Velina Leg Position VB Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
        ],
        'd4019bfa': [
            (log,                             ('3.0 - 3.2: Velina Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
        ],
        '231b06ea': [
            (log,                             ('3.0 - 3.2: Velina Leg Blend VB Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
        ],
        'febbf3b1': [
            (log,                             ('3.0 - 3.2: Velina LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('afa5c7de', 'Velina.LegA.Diffuse.1024')),
        ],
        'afa5c7de': [
            (log,                             ('3.0 - 3.2: Velina LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('febbf3b1', 'Velina.LegA.Diffuse.2048')),
        ],
        '5908c0bf': [
            (log,                             ('3.0 - 3.2: Velina LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9fb90ca', 'Velina.LegA.LightMap.1024')),
        ],
        'b9fb90ca': [
            (log,                             ('3.0 - 3.2: Velina LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5908c0bf', 'Velina.LegA.LightMap.2048')),
        ],
        '6b291f4d': [
            (log,                             ('3.0 - 3.2: Velina LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ba191269', 'Velina.LegA.MaterialMap.1024')),
        ],
        'ba191269': [
            (log,                             ('3.0 - 3.2: Velina LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b291f4d', 'Velina.LegA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        '1914d1e4': [
            (log,                             ('3.0 - 3.2: Velina Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f828e6a': [
            (log,                             ('3.0: Velina Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '38d54a4d': [
            (log,                             ('3.0: Velina Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '80e5ee4d': [
            (log,                             ('3.0: Velina Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f18dd23f': [
            (log,                             ('3.0: Velina Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '93ce2562': [
            (log,                             ('3.0 - 3.2: Velina EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e5409177', 'Velina.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('e5409177', 'Velina.FaceA.Diffuse.1024')),
        ],
        'e5409177': [
            (log,                             ('3.0 - 3.2: Velina EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93ce2562', 'Velina.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('93ce2562', 'Velina.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '6cfb2498': [
            (log,                             ('3.0 -> 3.1: Velina Face IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('2414f4b9',)),
        ],
        '2414f4b9': [
            (log,                             ('3.1: Velina Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '19ead1b7': [
            (log,                             ('3.0 -> 3.1: Velina Face Draw Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bfa3b361',)),
        ],
        'bfa3b361': [
            (log,                             ('3.1: Velina Face Draw VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
        ],
        '23f842f0': [
            (log,                             ('3.0 -> 3.1: Velina Face Position Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('85b12026',)),
        ],
        '85b12026': [
            (log,                             ('3.1: Velina Face Position VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
        ],
        '641bedfb': [
            (log,                             ('3.0 -> 3.1: Velina Face Texcoord Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('69304ff6',)),
        ],
        '69304ff6': [
            (log,                             ('3.1: Velina Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
        ],
        '98ecf569': [
            (log,                             ('3.0 -> 3.1: Velina Face Blend Hash',)),
            (add_section_if_missing,          ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('76fe8eed',)),
        ],
        '76fe8eed': [
            (log,                             ('3.1: Velina Face Blend VB Hash',)),
            (add_section_if_missing,          ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon Component ====================
        '8ac40392': [
            (log,                             ('3.0 - 3.2: Velina Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1d3db60d': [
            (log,                             ('3.0 - 3.2: Velina Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4f3ab614': [
            (log,                             ('3.0 - 3.2: Velina Weapon Position VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
        ],
        '1b43f126': [
            (log,                             ('3.0 - 3.2: Velina Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4ba016b1': [
            (log,                             ('3.0 - 3.2: Velina Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
        ],
        '185d733b': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5c55318', 'Velina.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d5c55318', 'Velina.FanA.Diffuse.1024')),
        ],
        'd5c55318': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('185d733b', 'Velina.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('185d733b', 'Velina.FanA.Diffuse.2048')),
        ],
        'e0e44e38': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5f7363aa', 'Velina.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('5f7363aa', 'Velina.FanA.LightMap.1024')),
        ],
        '5f7363aa': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e0e44e38', 'Velina.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('e0e44e38', 'Velina.FanA.LightMap.2048')),
        ],
        'b45cdc1a': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('edb1276e', 'Velina.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('edb1276e', 'Velina.FanA.MaterialMap.1024')),
        ],
        'edb1276e': [
            (log,                             ('3.0 - 3.2: Velina WeaponA and FanA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b45cdc1a', 'Velina.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b45cdc1a', 'Velina.FanA.MaterialMap.2048')),
        ],

        # ==================== Fan Component ====================
        '9fbf4911': [
            (log,                             ('3.0 - 3.2: Velina Fan IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f496de0': [
            (log,                             ('3.0 - 3.2: Velina Fan Draw VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
        ],
        '738fb0b1': [
            (log,                             ('3.0 - 3.2: Velina Fan Position VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
        ],
        'f8e38f88': [
            (log,                             ('3.0 - 3.2: Velina Fan Texcoord VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
        ],
        '055b892d': [
            (log,                             ('3.0 - 3.2: Velina Fan Blend VB Hash',)),
            (add_section_if_missing,          ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Velina',
    'game_versions': ['3.0', '3.1', '3.2'],
}
