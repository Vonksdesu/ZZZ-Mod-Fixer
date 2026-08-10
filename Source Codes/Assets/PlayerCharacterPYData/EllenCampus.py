"""
EllenCampus Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns EllenCampus's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    
    Note: EllenCampus reuses Ellen's face (IB: f6ef8f3a, Diffuse: 465a66eb)
    and shares NormalMap hash ebac056e across all components.
    """
    return {
# Hair Component
'f601f643': [(log, ('2.5: EllenCampus Hair IB Hash',)), (add_ib_check_if_missing,)],

'6e15911b': [
        (log,                           ('2.5: EllenCampus HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9a5c0d42', 'EllenCampus.HairA.Diffuse.1024')),
        (multiply_section_if_missing,        ('37eefb17', 'EllenCampus.HairA.Diffuse.1024')),
    ],

'37eefb17': [
        (log,                           ('2.5: EllenCampus HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9a5c0d42', 'EllenCampus.HairA.Diffuse.1024')),
        (multiply_section_if_missing,        ('6e15911b', 'EllenCampus.HairA.Diffuse.2048')),
    ],
'9a5c0d42': [
        (log,                           ('2.5: EllenCampus HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6e15911b', 'EllenCampus.HairA.Diffuse.2048')),
    ],

'48fd827b': [
        (log,                           ('2.5: EllenCampus HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('72e65ade', 'EllenCampus.HairA.LightMap.1024')),
        (multiply_section_if_missing,        ('aa77b3ff', 'EllenCampus.HairA.LightMap.1024')),
    ],

'aa77b3ff': [
        (log,                           ('2.5: EllenCampus HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('72e65ade', 'EllenCampus.HairA.LightMap.1024')),
        (multiply_section_if_missing,        ('48fd827b', 'EllenCampus.HairA.LightMap.2048')),
    ],
'72e65ade': [
        (log,                           ('2.5: EllenCampus HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('48fd827b', 'EllenCampus.HairA.LightMap.2048')),
    ],

'0de025b4': [(log, ('1.7 -> 2.0: EllenSkin HairA MaterialMap 2048p Hash',)), (update_hash, ('8740602f',))],
'8740602f': [
        (log,                           ('2.5: EllenCampus HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d69b5a86', 'EllenCampus.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('0ab940d8', '0cf3cd79'), 'EllenCampus.HairA.MaterialMap.1024')),
    ],

'0cf3cd79': [(log, ('1.5 -> 2.0: EllenSkin HairA MaterialMap 1024p Hash',)), (update_hash, ('0ab940d8',))],
'0ab940d8': [
        (log,                           ('2.5: EllenCampus HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d69b5a86', 'EllenCampus.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('8740602f', '0de025b4'), 'EllenCampus.HairA.MaterialMap.2048')),
    ],
'd69b5a86': [
        (log,                           ('2.5: EllenCampus HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8740602f', 'EllenCampus.HairA.MaterialMap.2048')),
    ],

# Body Component
'4a938c0a': [(log, ('2.5: EllenCampus Body IB Hash',)), (add_ib_check_if_missing,)],

'76f42184': [
        (log,                           ('2.5: EllenCampus BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fec9bbf8', 'EllenCampus.BodyA.Diffuse.1024')),
        (multiply_section_if_missing,        ('61beec5c', 'EllenCampus.BodyA.Diffuse.1024')),
    ],

'61beec5c': [
        (log,                           ('2.5: EllenCampus BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fec9bbf8', 'EllenCampus.BodyA.Diffuse.1024')),
        (multiply_section_if_missing,        ('76f42184', 'EllenCampus.BodyA.Diffuse.2048')),
    ],
'fec9bbf8': [
        (log,                           ('2.5: EllenCampus BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('76f42184', 'EllenCampus.BodyA.Diffuse.2048')),
    ],

'e6c9a6e1': [
        (log,                           ('2.5: EllenCampus BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('82a31ce3', 'EllenCampus.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        ('d13c6700', 'EllenCampus.BodyA.LightMap.1024')),
    ],

'd13c6700': [
        (log,                           ('2.5: EllenCampus BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('82a31ce3', 'EllenCampus.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        ('e6c9a6e1', 'EllenCampus.BodyA.LightMap.2048')),
    ],
'82a31ce3': [
        (log,                           ('2.5: EllenCampus BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e6c9a6e1', 'EllenCampus.BodyA.LightMap.2048')),
    ],

'd08f1a54': [(log, ('1.7 -> 2.0: EllenSkin BodyA MaterialMap 2048p Hash',)), (update_hash, ('1d7b458d',))],
'1d7b458d': [
        (log,                           ('2.5: EllenCampus BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('30427c9e', 'EllenCampus.BodyA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('ae919d9f', 'a4b66af3'), 'EllenCampus.BodyA.MaterialMap.1024')),
    ],

'a4b66af3': [(log, ('1.5 -> 2.0: EllenSkin BodyA MaterialMap 1024p Hash',)), (update_hash, ('ae919d9f',))],
'ae919d9f': [
        (log,                           ('2.5: EllenCampus BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('30427c9e', 'EllenCampus.BodyA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('1d7b458d', 'd08f1a54'), 'EllenCampus.BodyA.MaterialMap.2048')),
    ],
'30427c9e': [
        (log,                           ('2.5: EllenCampus BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d7b458d', 'EllenCampus.BodyA.MaterialMap.2048')),
    ],

# Tail Component
'fafcfe36': [(log, ('2.5: EllenCampus Tail IB Hash',)), (add_ib_check_if_missing,)],

'0e474202': [
        (log,                           ('2.5: EllenCampus TailA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e0c36e7e', 'EllenCampus.TailA.Diffuse.1024')),
        (multiply_section_if_missing,        ('8df52d2a', 'EllenCampus.TailA.Diffuse.1024')),
    ],

'8df52d2a': [
        (log,                           ('2.5: EllenCampus TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e0c36e7e', 'EllenCampus.TailA.Diffuse.1024')),
        (multiply_section_if_missing,        ('0e474202', 'EllenCampus.TailA.Diffuse.2048')),
    ],
'e0c36e7e': [
        (log,                           ('2.5: EllenCampus TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0e474202', 'EllenCampus.TailA.Diffuse.2048')),
    ],

'8f2cb44d': [
        (log,                           ('2.5: EllenCampus TailA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f21e3fa3', 'EllenCampus.TailA.LightMap.1024')),
        (multiply_section_if_missing,        ('a2f7a7db', 'EllenCampus.TailA.LightMap.1024')),
    ],

'a2f7a7db': [
        (log,                           ('2.5: EllenCampus TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f21e3fa3', 'EllenCampus.TailA.LightMap.1024')),
        (multiply_section_if_missing,        ('8f2cb44d', 'EllenCampus.TailA.LightMap.2048')),
    ],
'f21e3fa3': [
        (log,                           ('2.5: EllenCampus TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8f2cb44d', 'EllenCampus.TailA.LightMap.2048')),
    ],

'abb51170': [(log, ('1.7 -> 2.0: EllenSkin TailA MaterialMap 2048p Hash',)), (update_hash, ('51cc39d5',))],
'51cc39d5': [
        (log,                           ('2.5: EllenCampus TailA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('78e70ba9', 'EllenCampus.TailA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('cf37068c', 'beb3f207'), 'EllenCampus.TailA.MaterialMap.1024')),
    ],

'beb3f207': [(log, ('1.5 -> 2.0: EllenSkin TailA MaterialMap 1024p Hash',)), (update_hash, ('cf37068c',))],
'cf37068c': [
        (log,                           ('2.5: EllenCampus TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('78e70ba9', 'EllenCampus.TailA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('51cc39d5', 'abb51170'), 'EllenCampus.TailA.MaterialMap.2048')),
    ],
'78e70ba9': [
        (log,                           ('2.5: EllenCampus TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('51cc39d5', 'EllenCampus.TailA.MaterialMap.2048')),
    ],

# Shared NormalMap (used by Hair, Body, and Tail - same as Ellen's)
# Note: This hash is already defined in Ellen.py and shared across multiple components
# Adding references here for EllenCampus components
'ebac056e': [
        (log,                           ('2.5: EllenCampus Shared NormalMap 2048p Hash (Hair/Body/Tail)',)),
        (add_section_if_missing,        ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d6715e09', 'EllenCampus.Shared.NormalMap.1024')),
    ],

# Face Component (Reuses Ellen's face)
# IB: f6ef8f3a and Diffuse: 465a66eb are already defined in Ellen.py
# No additional hash commands needed as EllenCampus uses Ellen's face directly,
'9e8e3811': [
        (log, ('3.0: EllenCampus Hair VB Hash',)),
        (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'887a6214': [
        (log, ('3.0: EllenCampus Hair VB Hash',)),
        (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'e246fbec': [
        (log, ('3.0: EllenCampus Hair VB Hash',)),
        (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'7b54b96f': [(log, ('3.0: EllenCampus Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'3d83f929': [
        (log, ('3.0: EllenCampus Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9702c71e': [
        (log, ('3.0: EllenCampus Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'fc566cba': [
        (log, ('3.0: EllenCampus Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'42b50496': [
        (log, ('3.0: EllenCampus Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a1566c40': [
        (log, ('3.0: EllenCampus Body VB Hash',)),
        (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'fc0d07a3': [
        (log, ('3.0: EllenCampus Body VB Hash',)),
        (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'f6f9cc24': [
        (log, ('3.0: EllenCampus Body VB Hash',)),
        (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
'e053cbbd': [
        (log, ('3.0: EllenCampus Tail VB Hash',)),
        (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'54db15a2': [
        (log, ('3.0: EllenCampus Tail VB Hash',)),
        (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'f2c0c20f': [
        (log, ('3.0: EllenCampus Tail VB Hash',)),
        (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'f6ef8f3a': [(log, ('3.0: EllenCampus Face IB Hash',)), (add_ib_check_if_missing,)],
'aca863a9': [
        (log, ('3.0: EllenCampus Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],
'f87ddcae': [
        (log, ('3.0: EllenCampus Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],
'9cc30b79': [
        (log, ('3.0: EllenCampus Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],
'465a66eb': [
        (log, ('3.0: EllenCampus Face TEX Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],
'4ce3a865': [(log, ('3.0: EllenCampus weapon IB Hash',)), (add_ib_check_if_missing,)],
'4140d1e3': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'64df6d71': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'12c97a8a': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'e9e610cd': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'1721ed1a': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'9aaa6b4b': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'2747bdd1': [(log, ('3.0: EllenCampus weapon IB Hash',)), (add_ib_check_if_missing,)],
'4b5ecba8': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'21b31add': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'4afdcca5': [
        (log, ('3.0: EllenCampus weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'14ee18a1': [(log, ('3.0: EllenCampus misc hash',)),],
'96baf0ee': [(log, ('3.0: EllenCampus misc hash',)),],
'a063d963': [(log, ('3.0: EllenCampus misc hash',)),],
'a93fc9a1': [
        (log, ('3.0: EllenCampus Hair VB Hash',)),
        (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: EllenCampus Hair TEX Hash',)),
        (add_section_if_missing, ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
    ],
'4808d050': [
        (log, ('3.0: EllenCampus Face TEX Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
    ],
'b06f7cb9': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'0567bc4e': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'd4c2adaa': [
        (log, ('3.0: EllenCampus weapon TEX Hash',)),
        (add_section_if_missing, ('4ce3a865', 'EllenCampus.weapon.IB', 'match_priority = 0\n')),
    ],
'bfa3b361': [
        (log, ('3.0: EllenCampus Tail VB Hash',)),
        (add_section_if_missing, ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
    ],
'a31d576e': [
        (log, ('3.0: EllenCampus Body VB Hash',)),
        (add_section_if_missing, ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'EllenCampus',
    'full_name': 'Ellen (Campus Outfit)',
    'game_versions': ['2.5'],
    'notes': 'Reuses Ellen\'s face (IB: f6ef8f3a, Diffuse: 465a66eb). Shares NormalMap (ebac056e) across Hair/Body/Tail.',
}

