"""
Ellen Character Hash Commands
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
    Returns Ellen's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd44a8015': [
            (log,                             ('2.2 - 3.2: Ellen Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7f89a2b3': [
            (log,                             ('1.0 -> 1.1: Ellen Hair IB Hash',)),
            (update_hash,                     ('d44a8015',)),
        ],
        '77ac5f85': [
            (log,                             ('2.2 - 3.2: Ellen Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        ],
        'd59a5fec': [
            (log,                             ('1.0 -> 1.1: Ellen Hair Draw Hash',)),
            (update_hash,                     ('77ac5f85',)),
        ],
        'ba0fe600': [
            (log,                             ('2.2 - 3.2: Ellen Hair Position VB Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        ],
        'a5448398': [
            (log,                             ('1.0 -> 1.1: Ellen Hair Position Hash',)),
            (update_hash,                     ('ba0fe600',)),
        ],
        'a27a8e1a': [
            (log,                             ('2.2 - 3.2: Ellen Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        ],
        '9cddb082': [
            (log,                             ('1.0 -> 1.1: Ellen Hair Texcoord Hash',)),
            (update_hash,                     ('5c33833e',)),
            (log,                             ('+ Remapping texcoord buffer from stride 24 to 36',)),
            (zzz_13_remap_texcoord,           ('11_Ellen_Hair', ('4B', '2e', '2f', '2e', '2e'), ('4f', '2e', '2f', '2e', '2e'))),
        ],
        '5c33833e': [
            (log,                             ('1.1 -> 1.2: Ellen Hair Texcoord Hash',)),
            (update_hash,                     ('a27a8e1a',)),
            (log,                             ('+ Remapping texcoord buffer from stride 36 to 24',)),
            (zzz_12_shrink_texcoord_color,    ('1.2',)),
        ],
        'e91c93e0': [
            (log,                             ('2.2 - 3.2: Ellen Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        ],
        '2f9df031': [
            (log,                             ('1.2 -> 1.3: Ellen Hair Blend Hash',)),
            (update_hash,                     ('52188576',)),
        ],
        '52188576': [
            (log,                             ('1.3 -> 1.4: Ellen Hair Blend Remap',)),
            (update_buffer_blend_indices,     (
                '52188576',
                (34, 35, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50),
                (39, 34, 40, 35, 38, 42, 43, 44, 45, 46, 47, 41, 50, 49),
            )),
            (update_hash,                     ('e91c93e0',)),
        ],
        '81ccd2e2': [
            (log,                             ('2.2 - 3.2: Ellen HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1440e534', 'Ellen.HairA.Diffuse.1024')),
        ],
        '1440e534': [
            (log,                             ('2.2 - 3.2: Ellen HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81ccd2e2', 'Ellen.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Ellen HairA, BodyA, weapon - 镰刀 and weapon - 镰刀 - 弹簧 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', 'd6715e09'), 'Ellen.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '590880e5'), 'Ellen.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Ellen.weapon - 镰刀.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Ellen.weapon - 镰刀 - 弹簧.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Ellen HairA, BodyA, weapon - 镰刀 and weapon - 镰刀 - 弹簧 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', 'aaadca31'), 'Ellen.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '798c3a51'), 'Ellen.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Ellen.weapon - 镰刀.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Ellen.weapon - 镰刀 - 弹簧.NormalMap.2048')),
        ],
        'aaadca31': [
            (log,                             ('1.0 -> 2.5: Ellen HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'd6715e09': [
            (log,                             ('1.0: Ellen HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
        ],
        'dc9d8b6e': [
            (log,                             ('2.2 - 3.2: Ellen HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8c835faa', 'Ellen.HairA.LightMap.1024')),
        ],
        '8c835faa': [
            (log,                             ('2.2 - 3.2: Ellen HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc9d8b6e', 'Ellen.HairA.LightMap.2048')),
        ],
        '01bb8189': [
            (log,                             ('2.2 - 3.2: Ellen HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b21b8370', 'Ellen.HairA.MaterialMap.1024')),
        ],
        'b21b8370': [
            (log,                             ('2.2 - 3.2: Ellen HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d44a8015', 'Ellen.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01bb8189', 'Ellen.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '7b54b96f': [
            (log,                             ('2.2 - 3.2: Ellen Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3d83f929': [
            (log,                             ('2.2 - 3.2: Ellen Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '58dacb05': [
            (log,                             ('2.2 - 3.2: Ellen Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'fcfafc18': [
            (log,                             ('2.2 - 3.2: Ellen Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '01033838': [
            (log,                             ('2.2 - 3.2: Ellen Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'Ellen.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'e30fae03': [
            (log,                             ('2.2 - 3.2: Ellen Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a72cfb34': [
            (log,                             ('1.0 -> 1.1: Ellen Body IB Hash',)),
            (update_hash,                     ('e30fae03',)),
        ],
        'cdce1fc2': [
            (log,                             ('2.2 - 3.2: Ellen Body Draw VB Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        ],
        '7bd3f8c2': [
            (log,                             ('1.0 -> 1.1: Ellen Body Draw Hash',)),
            (update_hash,                     ('cdce1fc2',)),
        ],
        'b78f3616': [
            (log,                             ('2.2 - 3.2: Ellen Body Position VB Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        ],
        '89d5fba4': [
            (log,                             ('1.0 -> 1.1: Ellen Body Position Hash',)),
            (update_hash,                     ('b78f3616',)),
        ],
        '5ac6d5ee': [
            (log,                             ('2.2 - 3.2: Ellen Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        ],
        '26966844': [
            (log,                             ('1.0 -> 1.1: Ellen Body Texcoord Hash',)),
            (update_hash,                     ('5ac6d5ee',)),
        ],
        'ed9cb852': [
            (log,                             ('2.2 - 3.2: Ellen Body Blend VB Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        ],
        '4f4a54f0': [
            (log,                             ('1.0 -> 1.1: Ellen Body Blend Hash',)),
            (update_hash,                     ('89589539',)),
        ],
        '89589539': [
            (log,                             ('1.5 -> 1.6: Ellen Body Blend Hash',)),
            (update_hash,                     ('ed9cb852',)),
        ],
        '163e2559': [
            (log,                             ('2.2 - 3.2: Ellen BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22fa0cd6', 'Ellen.BodyA.Diffuse.1024')),
        ],
        'cf5f5fed': [
            (log,                             ('1.0: -> 1.1: Ellen BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('163e2559',)),
        ],
        '22fa0cd6': [
            (log,                             ('2.2 - 3.2: Ellen BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('163e2559', 'Ellen.BodyA.Diffuse.2048')),
        ],
        '94c15986': [
            (log,                             ('1.0: -> 1.1: Ellen BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('22fa0cd6',)),
        ],
        '798c3a51': [
            (log,                             ('1.0 -> 2.5: Ellen BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '590880e5': [
            (log,                             ('1.0: Ellen BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
        ],
        'ff26fb83': [
            (log,                             ('2.2 - 3.2: Ellen BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cea7516a', 'Ellen.BodyA.LightMap.1024')),
        ],
        'cea7516a': [
            (log,                             ('2.2 - 3.2: Ellen BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ff26fb83', 'Ellen.BodyA.LightMap.2048')),
        ],
        'f4487235': [
            (log,                             ('2.2 - 3.2: Ellen BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('30dc14d7', 'Ellen.BodyA.MaterialMap.1024')),
        ],
        '30dc14d7': [
            (log,                             ('2.2 - 3.2: Ellen BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('e30fae03', 'Ellen.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f4487235', 'Ellen.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'f6ef8f3a': [
            (log,                             ('2.2 - 3.2: Ellen Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9c7fac5a': [
            (log,                             ('1.0 -> 1.1: Ellen Face IB Hash',)),
            (update_hash,                     ('f6ef8f3a',)),
        ],
        '96baf0ee': [
            (log,                             ('2.2 - 3.2: Ellen Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
        ],
        'aca863a9': [
            (log,                             ('2.2 - 3.2: Ellen Face Position VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
        ],
        '158fa3f3': [
            (log,                             ('2.2 - 3.1: Ellen Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ac48fc8a',)),
        ],
        'ac48fc8a': [
            (log,                             ('3.2: Ellen Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '83dfd744': [
            (log,                             ('1.0 -> 1.1: Ellen Face Texcoord Hash',)),
            (update_hash,                     ('8744badf',)),
        ],
        'e015297d': [
            (log,                             ('2.2 - 3.2: Ellen Face Blend VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
        ],
        '465a66eb': [
            (log,                             ('2.2 - 3.2: Ellen FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('4808d050', 'e6b27e31'), 'Ellen.FaceA.Diffuse.1024')),
        ],
        '09d55bce': [
            (log,                             ('1.0 -> 1.1: Ellen FaceA Diffuse 2048p Hash',)),
            (update_hash,                     ('465a66eb',)),
        ],
        '4808d050': [
            (log,                             ('2.2 - 3.2: Ellen FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'Ellen.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('465a66eb', '09d55bce'), 'Ellen.FaceA.Diffuse.2048')),
        ],
        'e6b27e31': [
            (log,                             ('1.0 -> 1.1: Ellen FaceA Diffuse 1024p Hash',)),
            (update_hash,                     ('4808d050',)),
        ],

        # ==================== Weapon - 镰刀 Component ====================
        '569f47ac': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '14ee18a1': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '0e6ed776': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 Position VB Hash',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        'ad548430': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '6500eb53': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 Blend VB Hash',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        'e9e610cd': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b06f7cb9', 'Ellen.weapon - 镰刀.Diffuse.1024')),
            (multiply_section_if_missing,     ('b06f7cb9', 'Ellen.weapon - 镰刀 - 弹簧.Diffuse.1024')),
        ],
        'b06f7cb9': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e9e610cd', 'Ellen.weapon - 镰刀.Diffuse.2048')),
            (multiply_section_if_missing,     ('e9e610cd', 'Ellen.weapon - 镰刀 - 弹簧.Diffuse.2048')),
        ],
        '1721ed1a': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0567bc4e', 'Ellen.weapon - 镰刀.LightMap.1024')),
            (multiply_section_if_missing,     ('0567bc4e', 'Ellen.weapon - 镰刀 - 弹簧.LightMap.1024')),
        ],
        '0567bc4e': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1721ed1a', 'Ellen.weapon - 镰刀.LightMap.2048')),
            (multiply_section_if_missing,     ('1721ed1a', 'Ellen.weapon - 镰刀 - 弹簧.LightMap.2048')),
        ],
        '9aaa6b4b': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4c2adaa', 'Ellen.weapon - 镰刀.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d4c2adaa', 'Ellen.weapon - 镰刀 - 弹簧.MaterialMap.1024')),
        ],
        'd4c2adaa': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 and weapon - 镰刀 - 弹簧 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('569f47ac', 'Ellen.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9aaa6b4b', 'Ellen.weapon - 镰刀.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9aaa6b4b', 'Ellen.weapon - 镰刀 - 弹簧.MaterialMap.2048')),
        ],

        # ==================== Weapon - 镰刀 - 弹簧 Component ====================
        '2747bdd1': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 - 弹簧 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a063d963': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 - 弹簧 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        '4b5ecba8': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 - 弹簧 Position VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        'c75b2bfe': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 - 弹簧 Texcoord VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        '4afdcca5': [
            (log,                             ('2.2 - 3.2: Ellen weapon - 镰刀 - 弹簧 Blend VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'Ellen.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        # weapon - 镰刀 - 弹簧 shares all texture hashes with weapon - 镰刀; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ellen',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
