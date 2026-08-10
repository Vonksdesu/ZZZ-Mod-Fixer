"""
Ellen Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Ellen's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'd44a8015': [(log, ('1.1: Ellen Hair IB Hash',)), (add_ib_check_if_missing,)],
'e30fae03': [(log, ('1.1: Ellen Body IB Hash',)), (add_ib_check_if_missing,)],
'f6ef8f3a': [(log, ('1.1: Ellen Head IB Hash',)), (add_ib_check_if_missing,)],
'9c7fac5a': [(log, ('1.0 -> 1.1: Ellen Head IB Hash',)),       (update_hash, ('f6ef8f3a',))],
'7f89a2b3': [(log, ('1.0 -> 1.1: Ellen Hair IB Hash',)),       (update_hash, ('d44a8015',))],
'a72cfb34': [(log, ('1.0 -> 1.1: Ellen Body IB Hash',)),       (update_hash, ('e30fae03',))],
'4f4a54f0': [(log, ('1.0 -> 1.1: Ellen Body Blend Hash',)),    (update_hash, ('89589539',))],
'83dfd744': [(log, ('1.0 -> 1.1: Ellen Head Texcoord Hash',)), (update_hash, ('8744badf',))],
'd59a5fec': [(log, ('1.0 -> 1.1: Ellen Hair Draw Hash',)),     (update_hash, ('77ac5f85',))],
'a5448398': [(log, ('1.0 -> 1.1: Ellen Hair Position Hash',)), (update_hash, ('ba0fe600',))],
'9cddb082': [
        (log, ('1.0 -> 1.1: Ellen Hair Texcoord Hash',)),
        (update_hash, ('5c33833e',)),
        (log, ('+ Remapping texcoord buffer from stride 24 to 36',)),
        (zzz_13_remap_texcoord, ('11_Ellen_Hair', ('4B', '2e', '2f', '2e', '2e'), ('4f', '2e', '2f', '2e', '2e'))), # attention
    ],
'5c33833e': [
        (log, ('1.1 -> 1.2: Ellen Hair Texcoord Hash',)),
        (update_hash, ('a27a8e1a',)),
        (log, ('+ Remapping texcoord buffer from stride 36 to 24',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'2f9df031': [(log, ('1.2 -> 1.3: Ellen Hair Blend Hash',)),    (update_hash, ('52188576',))],
'52188576': [
        (log,                         ('1.3 -> 1.4: Ellen Hair Blend Remap',)),
        (update_buffer_blend_indices, (
            '52188576',
            (34, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50),
            (39, 34, 40, 35, 38, 42, 43, 44, 45, 46, 47, 41, 50, 49),
        )),
        (update_hash,                 ('e91c93e0',)),
    ],
'7bd3f8c2': [(log, ('1.0 -> 1.1: Ellen Body Draw Hash',)),     (update_hash, ('cdce1fc2',))],
'89d5fba4': [(log, ('1.0 -> 1.1: Ellen Body Position Hash',)), (update_hash, ('b78f3616',))],
'26966844': [(log, ('1.0 -> 1.1: Ellen Body Texcoord Hash',)), (update_hash, ('5ac6d5ee',))],
'89589539': [(log, ('1.5 -> 1.6: Ellen Body Blend Hash',)),    (update_hash, ('ed9cb852',))],
'09d55bce': [(log, ('1.0 -> 1.1: Ellen HeadA Diffuse 2048p Hash',)), (update_hash, ('465a66eb',))],
'465a66eb': [
        (log,                           ('1.1: Ellen HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('f6ef8f3a', '9c7fac5a'), 'Ellen.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('4808d050', 'e6b27e31'), 'Ellen.HeadA.Diffuse.1024')),
    ],
'e6b27e31': [(log, ('1.0 -> 1.1: Ellen HeadA Diffuse 1024p Hash',)), (update_hash, ('4808d050',))],
'4808d050': [
        (log,                           ('1.1: Ellen HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('f6ef8f3a', '9c7fac5a'), 'Ellen.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('465a66eb', '09d55bce'), 'Ellen.HeadA.Diffuse.2048')),
    ],
'81ccd2e2': [
        (log,                           ('1.0: Ellen HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1440e534', 'Ellen.HairA.Diffuse.1024')),
    ],
'1440e534': [
        (log,                           ('1.0: Ellen HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('81ccd2e2', 'Ellen.HairA.Diffuse.2048')),
    ],
'dc9d8b6e': [
        (log,                           ('1.0: Ellen HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8c835faa', 'Ellen.HairA.LightMap.1024')),
    ],
'8c835faa': [
        (log,                           ('1.0: Ellen HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc9d8b6e', 'Ellen.HairA.LightMap.2048')),
    ],
'01bb8189': [
        (log,                           ('1.0: Ellen HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b21b8370', 'Ellen.HairA.MaterialMap.1024')),
    ],
'b21b8370': [
        (log,                           ('1.0: Ellen HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('01bb8189', 'Ellen.HairA.MaterialMap.2048')),
    ],
'aaadca31': [
        (log,                           ('1.0 -> 2.5: Ellen HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'd6715e09': [
        (log,                           ('1.0: Ellen HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', 'aaadca31'), 'Ellen.HairA.NormalMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Ellen HairA and BodyA NormalMap 2048p Hash (shared)',)),
        (add_section_if_missing,        (('d44a8015', '7f89a2b3'), 'Ellen.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d6715e09', 'Ellen.HairA.NormalMap.1024')),
        (multiply_section_if_missing,   ('590880e5', 'Ellen.BodyA.NormalMap.1024')),
    ],
'cf5f5fed': [
        (log,                           ('1.0: -> 1.1: Ellen BodyA Diffuse 2048p Hash',)),
        (update_hash,                   ('163e2559',)),
    ],
'163e2559': [
        (log,                           ('1.1: Ellen BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('22fa0cd6', '94c15986'), 'Ellen.BodyA.Diffuse.1024')),
    ],
'94c15986': [
        (log,                           ('1.0: -> 1.1: Ellen BodyA Diffuse 1024p Hash',)),
        (update_hash,                   ('22fa0cd6',)),
    ],
'22fa0cd6': [
        (log,                           ('1.1: Ellen BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('163e2559', 'cf5f5fed'), 'Ellen.BodyA.Diffuse.2048')),
    ],
'ff26fb83': [
        (log,                           ('1.0: Ellen BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cea7516a', 'Ellen.BodyA.LightMap.1024')),
    ],
'cea7516a': [
        (log,                           ('1.0: Ellen BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff26fb83', 'Ellen.BodyA.LightMap.2048')),
    ],
'f4487235': [
        (log,                           ('1.0: Ellen BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('30dc14d7', 'Ellen.BodyA.MaterialMap.1024')),
    ],
'30dc14d7': [
        (log,                           ('1.0: Ellen BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f4487235', 'Ellen.BodyA.MaterialMap.2048')),
    ],
'798c3a51': [
        (log,                           ('1.0 -> 2.5: Ellen BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'590880e5': [
        (log,                           ('1.0: Ellen BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('e30fae03', 'a72cfb34'), 'Ellen.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '798c3a51'), 'Ellen.BodyA.NormalMap.2048')),
    ],
'ba0fe600': [
        (log, ('3.0: Ellen Hair VB Hash',)),
        (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
    ],
'a27a8e1a': [
        (log, ('3.0: Ellen Hair VB Hash',)),
        (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
    ],
'e91c93e0': [
        (log, ('3.0: Ellen Hair VB Hash',)),
        (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
    ],
'7b54b96f': [(log, ('3.0: Ellen Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'3d83f929': [
        (log, ('3.0: Ellen Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'58dacb05': [
        (log, ('3.0: Ellen Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'fcfafc18': [
        (log, ('3.0: Ellen Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'01033838': [
        (log, ('3.0: Ellen Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'cdce1fc2': [
        (log, ('3.0: Ellen Body VB Hash',)),
        (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
    ],
'b78f3616': [
        (log, ('3.0: Ellen Body VB Hash',)),
        (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
    ],
'5ac6d5ee': [
        (log, ('3.0: Ellen Body VB Hash',)),
        (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
    ],
'ed9cb852': [
        (log, ('3.0: Ellen Body VB Hash',)),
        (add_section_if_missing, ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
    ],
'aca863a9': [
        (log, ('3.0: Ellen Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
    ],
'158fa3f3': [
        (log, ('3.0: Ellen Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
    ],
'e015297d': [
        (log, ('3.0: Ellen Face VB Hash',)),
        (add_section_if_missing, ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
    ],
'569f47ac': [(log, ('3.0: Ellen weapon IB Hash',)), (add_ib_check_if_missing,)],
'0e6ed776': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'ad548430': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'6500eb53': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'e9e610cd': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'1721ed1a': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'9aaa6b4b': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'2747bdd1': [(log, ('3.0: Ellen weapon IB Hash',)), (add_ib_check_if_missing,)],
'4b5ecba8': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'c75b2bfe': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'4afdcca5': [
        (log, ('3.0: Ellen weapon VB Hash',)),
        (add_section_if_missing, ('2747bdd1', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'14ee18a1': [(log, ('3.0: Ellen misc hash',)),],
'96baf0ee': [(log, ('3.0: Ellen misc hash',)),],
'a063d963': [(log, ('3.0: Ellen misc hash',)),],
'77ac5f85': [
        (log, ('3.0: Ellen Hair VB Hash',)),
        (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Ellen Hair TEX Hash',)),
        (add_section_if_missing, ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
    ],
'b06f7cb9': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'0567bc4e': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
'd4c2adaa': [
        (log, ('3.0: Ellen weapon TEX Hash',)),
        (add_section_if_missing, ('569f47ac', 'Ellen.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ellen',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
