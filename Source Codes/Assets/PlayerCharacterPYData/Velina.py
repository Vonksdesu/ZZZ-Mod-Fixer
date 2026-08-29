"""
Velina Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0
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
# === IB Hashes ===
'1300e048': [
        (log,                           ('3.0: Velina Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6cfb2498': [
        (log,                           ('3.0 -> 3.1: Velina Face IB Hash',)),
        (add_ib_check_if_missing,),
        (update_hash,                        ('2414f4b9',)),
    ],
'9fbf4911': [
        (log,                           ('3.0: Velina Fan IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'5eb66b57': [
        (log,                           ('3.0: Velina Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6c0b932e': [
        (log,                           ('3.0: Velina HairClip IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6b25e6d8': [
        (log,                           ('3.0: Velina Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Velina Textures (FaceA) ===
'e5409177': [
        (log,                           ('3.0: Velina FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('93ce2562', 'Velina.FaceA.Diffuse.2048')),
    ],
'93ce2562': [
        (log,                           ('3.0: Velina FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('e5409177', 'Velina.FaceA.Diffuse.1024')),
    ],

# === Velina Textures (HairA) ===
'673e5da6': [
        (log,                           ('3.0: Velina HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('dc6853c3', 'Velina.HairA.Diffuse.2048')),
    ],
'dc6853c3': [
        (log,                           ('3.0: Velina HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('673e5da6', 'Velina.HairA.Diffuse.1024')),
    ],
'54fc678e': [
        (log,                           ('3.0: Velina HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('f06d3a26', 'Velina.HairA.LightMap.2048')),
    ],
'f06d3a26': [
        (log,                           ('3.0: Velina HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('54fc678e', 'Velina.HairA.LightMap.1024')),
    ],
'ccbcd045': [
        (log,                           ('3.0: Velina HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('4951b2a2', 'Velina.HairA.MaterialMap.2048')),
    ],
'4951b2a2': [
        (log,                           ('3.0: Velina HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ccbcd045', 'Velina.HairA.MaterialMap.1024')),
    ],

# === Velina Textures (BodyA) ===
'f9a8e3ba': [
        (log,                           ('3.0: Velina BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('93c61891', 'Velina.BodyA.Diffuse.2048')),
    ],
'93c61891': [
        (log,                           ('3.0: Velina BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('f9a8e3ba', 'Velina.BodyA.Diffuse.1024')),
    ],
'5562351c': [
        (log,                           ('3.0: Velina BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('9a16d70e', 'Velina.BodyA.LightMap.2048')),
    ],
'9a16d70e': [
        (log,                           ('3.0: Velina BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('5562351c', 'Velina.BodyA.LightMap.1024')),
    ],
'531320a5': [
        (log,                           ('3.0: Velina BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('bb1d0172', 'Velina.BodyA.MaterialMap.2048')),
    ],
'bb1d0172': [
        (log,                           ('3.0: Velina BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('531320a5', 'Velina.BodyA.MaterialMap.1024')),
    ],

# === Velina Textures (LegA) ===
'afa5c7de': [
        (log,                           ('3.0: Velina LegA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('febbf3b1', 'Velina.LegA.Diffuse.2048')),
    ],
'febbf3b1': [
        (log,                           ('3.0: Velina LegA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('afa5c7de', 'Velina.LegA.Diffuse.1024')),
    ],
'b9fb90ca': [
        (log,                           ('3.0: Velina LegA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('5908c0bf', 'Velina.LegA.LightMap.2048')),
    ],
'5908c0bf': [
        (log,                           ('3.0: Velina LegA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('b9fb90ca', 'Velina.LegA.LightMap.1024')),
    ],
'ba191269': [
        (log,                           ('3.0: Velina LegA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6b291f4d', 'Velina.LegA.MaterialMap.2048')),
    ],
'6b291f4d': [
        (log,                           ('3.0: Velina LegA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ba191269', 'Velina.LegA.MaterialMap.1024')),
    ],
'53954bd7': [
        (log, ('3.0: Velina Hair VB Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
'9f40d9d1': [
        (log, ('3.0: Velina Hair VB Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
'a1c210e2': [
        (log, ('3.0: Velina Hair VB Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Velina Hair TEX Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
'6f33df95': [(log, ('3.0: Velina HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'a364c911': [
        (log, ('3.0: Velina HairClip VB Hash',)),
        (add_section_if_missing, ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
    ],
'cb6147f9': [
        (log, ('3.0: Velina HairClip VB Hash',)),
        (add_section_if_missing, ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
    ],
'4b702182': [
        (log, ('3.0: Velina HairClip VB Hash',)),
        (add_section_if_missing, ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
    ],
'bd043a8e': [
        (log, ('3.0: Velina HairClip VB Hash',)),
        (add_section_if_missing, ('6c0b932e', 'Velina.HairClip.IB', 'match_priority = 0\n')),
    ],
'0b4b3a1f': [
        (log, ('3.0: Velina Body VB Hash',)),
        (add_section_if_missing, ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
    ],
'1f1c042b': [
        (log, ('3.0: Velina Body VB Hash',)),
        (add_section_if_missing, ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
    ],
'2c2ccd38': [
        (log, ('3.0: Velina Body VB Hash',)),
        (add_section_if_missing, ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
    ],
'adba03f3': [
        (log, ('3.0: Velina Leg VB Hash',)),
        (add_section_if_missing, ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
    ],
'd4019bfa': [
        (log, ('3.0: Velina Leg VB Hash',)),
        (add_section_if_missing, ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
    ],
'231b06ea': [
        (log, ('3.0: Velina Leg VB Hash',)),
        (add_section_if_missing, ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
    ],
'1914d1e4': [(log, ('3.0: Velina Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'2f828e6a': [
        (log, ('3.0: Velina Eyebrow VB Hash',)),
        (add_section_if_missing, ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'38d54a4d': [
        (log, ('3.0: Velina Eyebrow VB Hash',)),
        (add_section_if_missing, ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'80e5ee4d': [
        (log, ('3.0: Velina Eyebrow VB Hash',)),
        (add_section_if_missing, ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f18dd23f': [
        (log, ('3.0: Velina Eyebrow VB Hash',)),
        (add_section_if_missing, ('1914d1e4', 'Velina.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'23f842f0': [
        (log, ('3.0: Velina Face VB Hash',)),
        (add_section_if_missing, ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
    ],
'641bedfb': [
        (log,                           ('3.0 -> 3.1: Velina Face VB Hash',)),
        (add_section_if_missing, ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
        (update_hash,                        ('69304ff6',)),
    ],
'98ecf569': [
        (log,                           ('3.0 -> 3.1: Velina Face VB Hash',)),
        (add_section_if_missing, ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
        (update_hash,                        ('76fe8eed',)),
    ],
# === Velina Face (3.1) ===
'2414f4b9': [(log, ('3.1: Velina Face IB Hash',)), (add_ib_check_if_missing,)],
'85b12026': [
        (log, ('3.1: Velina Face VB Hash',)),
        (add_section_if_missing, ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
    ],
'69304ff6': [
        (log, ('3.1: Velina Face VB Hash',)),
        (add_section_if_missing, ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
    ],
'76fe8eed': [
        (log, ('3.1: Velina Face VB Hash',)),
        (add_section_if_missing, ('2414f4b9', 'Velina.Face.IB', 'match_priority = 0\n')),
    ],
'8ac40392': [(log, ('3.0: Velina Weapon IB Hash',)), (add_ib_check_if_missing,)],
'1d3db60d': [
        (log, ('3.0: Velina Weapon VB Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'4f3ab614': [
        (log, ('3.0: Velina Weapon VB Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'1b43f126': [
        (log, ('3.0: Velina Weapon VB Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'4ba016b1': [
        (log, ('3.0: Velina Weapon VB Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'185d733b': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'e0e44e38': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'b45cdc1a': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'738fb0b1': [
        (log, ('3.0: Velina Fan VB Hash',)),
        (add_section_if_missing, ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
    ],
'f8e38f88': [
        (log, ('3.0: Velina Fan VB Hash',)),
        (add_section_if_missing, ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
    ],
'055b892d': [
        (log, ('3.0: Velina Fan VB Hash',)),
        (add_section_if_missing, ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Velina Hair TEX Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
'd5c55318': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'5f7363aa': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'edb1276e': [
        (log, ('3.0: Velina Weapon TEX Hash',)),
        (add_section_if_missing, ('8ac40392', 'Velina.Weapon.IB', 'match_priority = 0\n')),
    ],
'2f496de0': [
        (log, ('3.0: Velina Fan VB Hash',)),
        (add_section_if_missing, ('9fbf4911', 'Velina.Fan.IB', 'match_priority = 0\n')),
    ],
'19ead1b7': [
        (log, ('3.0: Velina Face VB Hash',)),
        (add_section_if_missing, ('6cfb2498', 'Velina.Face.IB', 'match_priority = 0\n')),
    ],
'10675a0f': [
        (log, ('3.0: Velina Leg VB Hash',)),
        (add_section_if_missing, ('6b25e6d8', 'Velina.Leg.IB', 'match_priority = 0\n')),
    ],
'2f62f81f': [
        (log, ('3.0: Velina Body VB Hash',)),
        (add_section_if_missing, ('1300e048', 'Velina.Body.IB', 'match_priority = 0\n')),
    ],
'c60af8f1': [
        (log, ('3.0: Velina Hair VB Hash',)),
        (add_section_if_missing, ('5eb66b57', 'Velina.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Velina',
    'game_versions': ['3.0'],
}
