"""
JuFufu Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from RawAssets/PlayerCharacterData/JuFufu/hash.json
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns JuFufu's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'a4fd9113': [(log, ('2.5: JuFufu Hair IB Hash',)), (add_ib_check_if_missing,)],
'de303163': [(log, ('2.5: JuFufu Body IB Hash',)), (add_ib_check_if_missing,)],
'f8ab3141': [(log, ('2.5: JuFufu Tail IB Hash',)), (add_ib_check_if_missing,)],
'321768df': [(log, ('2.5: JuFufu Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'37b277db': [
        (log,                           ('2.5: JuFufu FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('134fbe43', 'JuFufu.FaceA.Diffuse.1024')),
    ],

'134fbe43': [
        (log,                           ('2.5: JuFufu FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('37b277db', 'JuFufu.FaceA.Diffuse.2048')),
    ],

# Shared NormalMap (Hair, Body, Tail)
'ebac056e': [
        (log,                           ('2.5: JuFufu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],

# Hair and Tail Shared Textures
'db3bdffa': [
        (log,                           ('2.5: JuFufu HairA, TailA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('521f60ae', 'JuFufu.HairA.Diffuse.1024')),
    ],

'521f60ae': [
        (log,                           ('2.5: JuFufu HairA, TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('db3bdffa', 'JuFufu.HairA.Diffuse.2048')),
    ],
'5c948f7b': [
        (log,                           ('2.5: JuFufu HairA, TailA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('29bb13b7', 'JuFufu.HairA.LightMap.1024')),
    ],

'29bb13b7': [
        (log,                           ('2.5: JuFufu HairA, TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5c948f7b', 'JuFufu.HairA.LightMap.2048')),
    ],
'9f4d4f72': [
        (log,                           ('2.5: JuFufu HairA, TailA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9355dcea', 'JuFufu.HairA.MaterialMap.1024')),
    ],

'9355dcea': [
        (log,                           ('2.5: JuFufu HairA, TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9f4d4f72', 'JuFufu.HairA.MaterialMap.2048')),
    ],

# Body Textures
'16e4cac1': [
        (log,                           ('2.5: JuFufu BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3b372932', 'JuFufu.BodyA.Diffuse.1024')),
    ],

'3b372932': [
        (log,                           ('2.5: JuFufu BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('16e4cac1', 'JuFufu.BodyA.Diffuse.2048')),
    ],
'c952431f': [
        (log,                           ('2.5: JuFufu BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9d1ab7c4', 'JuFufu.BodyA.LightMap.1024')),
    ],

'9d1ab7c4': [
        (log,                           ('2.5: JuFufu BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c952431f', 'JuFufu.BodyA.LightMap.2048')),
    ],
'd555b4f8': [
        (log,                           ('2.5: JuFufu BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f72af17c', 'JuFufu.BodyA.MaterialMap.1024')),
    ],

'f72af17c': [
        (log,                           ('2.5: JuFufu BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d555b4f8', 'JuFufu.BodyA.MaterialMap.2048')),
    ],
'e836ec8f': [
        (log, ('3.0: JuFufu Hair VB Hash',)),
        (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
    ],
'fbca830d': [
        (log, ('3.0: JuFufu Hair VB Hash',)),
        (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
    ],
'c9c19a97': [
        (log, ('3.0: JuFufu Hair VB Hash',)),
        (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
    ],
'095f38e8': [(log, ('3.0: JuFufu Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'e636c467': [
        (log, ('3.0: JuFufu Hair Shadow VB Hash',)),
        (add_section_if_missing, ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f0e84fef': [
        (log, ('3.0: JuFufu Hair Shadow VB Hash',)),
        (add_section_if_missing, ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'60d9a4fc': [
        (log, ('3.0: JuFufu Hair Shadow VB Hash',)),
        (add_section_if_missing, ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b18001e6': [
        (log, ('3.0: JuFufu Hair Shadow VB Hash',)),
        (add_section_if_missing, ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'5c076ce8': [
        (log, ('3.0: JuFufu Body VB Hash',)),
        (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'00ba64ca': [
        (log, ('3.0: JuFufu Body VB Hash',)),
        (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'2e086db7': [
        (log, ('3.0: JuFufu Body VB Hash',)),
        (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'c06c0417': [
        (log, ('3.0: JuFufu Body VB Hash',)),
        (add_section_if_missing, ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
    ],
'c84e77d4': [
        (log, ('3.0: JuFufu Tail VB Hash',)),
        (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'c397375f': [
        (log, ('3.0: JuFufu Tail VB Hash',)),
        (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'9a198bcf': [
        (log, ('3.0: JuFufu Tail VB Hash',)),
        (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'c8fa66e3': [
        (log, ('3.0: JuFufu Tail VB Hash',)),
        (add_section_if_missing, ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
    ],
'ed92b94c': [
        (log, ('3.0: JuFufu Face VB Hash',)),
        (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],
'8267358b': [
        (log, ('3.0: JuFufu Face VB Hash',)),
        (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],
'512615d6': [
        (log, ('3.0: JuFufu Face VB Hash',)),
        (add_section_if_missing, ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
    ],
'a27835bb': [(log, ('3.0: JuFufu weapon IB Hash',)), (add_ib_check_if_missing,)],
'41006dfa': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'ce435978': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'fbb7c2a6': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'401f92e6': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'1b61ae30': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'e62eed48': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'46e339a6': [(log, ('3.0: JuFufu weapon IB Hash',)), (add_ib_check_if_missing,)],
'45b2b661': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('46e339a6', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'395481f4': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('46e339a6', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'18a54256': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('46e339a6', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'b51e30e5': [(log, ('3.0: JuFufu weapon IB Hash',)), (add_ib_check_if_missing,)],
'245e6459': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'1544d097': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'7778328f': [
        (log, ('3.0: JuFufu weapon VB Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'094ac0a2': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'4bb30541': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'9db94a04': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'03768505': [(log, ('3.0: JuFufu misc hash',)),],
'0468fc0c': [(log, ('3.0: JuFufu misc hash',)),],
'303b7a17': [(log, ('3.0: JuFufu misc hash',)),],
'd7802a0b': [(log, ('3.0: JuFufu misc hash',)),],
'77d02cb1': [
        (log, ('3.0: JuFufu Hair VB Hash',)),
        (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: JuFufu Hair TEX Hash',)),
        (add_section_if_missing, ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
    ],
'9a93726a': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'1738f744': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'7d54f20a': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('a27835bb', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'27928ca3': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'87e25f7d': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
'26d6f075': [
        (log, ('3.0: JuFufu weapon TEX Hash',)),
        (add_section_if_missing, ('b51e30e5', 'JuFufu.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JuFufu',
    'game_versions': ['2.5'],
}
