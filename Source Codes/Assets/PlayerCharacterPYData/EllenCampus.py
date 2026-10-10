"""
EllenCampus Character Hash Commands
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
    Returns EllenCampus's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'f601f643': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a93fc9a1': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Draw VB Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        '9e8e3811': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Position VB Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        '887a6214': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        'e246fbec': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Blend VB Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        '6e15911b': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('37eefb17', '9a5c0d42'), 'EllenCampus.HairA.Diffuse.1024')),
        ],
        '37eefb17': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6e15911b', 'EllenCampus.HairA.Diffuse.2048')),
        ],
        '9a5c0d42': [
            (log,                             ('2.5: EllenCampus HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA, BodyA, TailA, weapon - 镰刀 and weapon - 镰刀 - 弹簧 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'EllenCampus.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'EllenCampus.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'EllenCampus.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'EllenCampus.weapon - 镰刀.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'EllenCampus.weapon - 镰刀 - 弹簧.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA, BodyA, TailA, weapon - 镰刀 and weapon - 镰刀 - 弹簧 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'EllenCampus.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'EllenCampus.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'EllenCampus.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'EllenCampus.weapon - 镰刀.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'EllenCampus.weapon - 镰刀 - 弹簧.NormalMap.2048')),
        ],
        '48fd827b': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('aa77b3ff', '72e65ade'), 'EllenCampus.HairA.LightMap.1024')),
        ],
        'aa77b3ff': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('48fd827b', 'EllenCampus.HairA.LightMap.2048')),
        ],
        '72e65ade': [
            (log,                             ('2.5: EllenCampus HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        '8740602f': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0ab940d8', 'd69b5a86', '0cf3cd79'), 'EllenCampus.HairA.MaterialMap.1024')),
        ],
        '0ab940d8': [
            (log,                             ('2.2 - 3.2: EllenCampus HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8740602f', '0de025b4'), 'EllenCampus.HairA.MaterialMap.2048')),
        ],
        'd69b5a86': [
            (log,                             ('2.5: EllenCampus HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f601f643', 'EllenCampus.Hair.IB', 'match_priority = 0\n')),
        ],
        '0de025b4': [
            (log,                             ('1.7 -> 2.0: EllenSkin HairA MaterialMap 2048p Hash',)),
            (update_hash,                     ('8740602f',)),
        ],
        '0cf3cd79': [
            (log,                             ('1.5 -> 2.0: EllenSkin HairA MaterialMap 1024p Hash',)),
            (update_hash,                     ('0ab940d8',)),
        ],

        # ==================== Hair Shadow Component ====================
        '7b54b96f': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3d83f929': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9702c71e': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'fc566cba': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '42b50496': [
            (log,                             ('2.2 - 3.2: EllenCampus Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('7b54b96f', 'EllenCampus.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '4a938c0a': [
            (log,                             ('2.2 - 3.2: EllenCampus Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a31d576e': [
            (log,                             ('2.2 - 3.2: EllenCampus Body Draw VB Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        'a1566c40': [
            (log,                             ('2.2 - 3.2: EllenCampus Body Position VB Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        'fc0d07a3': [
            (log,                             ('2.2 - 3.2: EllenCampus Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        'f6f9cc24': [
            (log,                             ('2.2 - 3.2: EllenCampus Body Blend VB Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        '76f42184': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('61beec5c', 'fec9bbf8'), 'EllenCampus.BodyA.Diffuse.1024')),
        ],
        '61beec5c': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76f42184', 'EllenCampus.BodyA.Diffuse.2048')),
        ],
        'fec9bbf8': [
            (log,                             ('2.5: EllenCampus BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        'e6c9a6e1': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d13c6700', '82a31ce3'), 'EllenCampus.BodyA.LightMap.1024')),
        ],
        'd13c6700': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e6c9a6e1', 'EllenCampus.BodyA.LightMap.2048')),
        ],
        '82a31ce3': [
            (log,                             ('2.5: EllenCampus BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        '1d7b458d': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ae919d9f', '30427c9e', 'a4b66af3'), 'EllenCampus.BodyA.MaterialMap.1024')),
        ],
        'ae919d9f': [
            (log,                             ('2.2 - 3.2: EllenCampus BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('1d7b458d', 'd08f1a54'), 'EllenCampus.BodyA.MaterialMap.2048')),
        ],
        '30427c9e': [
            (log,                             ('2.5: EllenCampus BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4a938c0a', 'EllenCampus.Body.IB', 'match_priority = 0\n')),
        ],
        'd08f1a54': [
            (log,                             ('1.7 -> 2.0: EllenSkin BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('1d7b458d',)),
        ],
        'a4b66af3': [
            (log,                             ('1.5 -> 2.0: EllenSkin BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('ae919d9f',)),
        ],

        # ==================== Tail Component ====================
        'fafcfe36': [
            (log,                             ('2.2 - 3.2: EllenCampus Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bfa3b361': [
            (log,                             ('2.2 - 3.2: EllenCampus Tail Draw VB Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        'e053cbbd': [
            (log,                             ('2.2 - 3.2: EllenCampus Tail Position VB Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        '54db15a2': [
            (log,                             ('2.2 - 3.2: EllenCampus Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        'f2c0c20f': [
            (log,                             ('2.2 - 3.2: EllenCampus Tail Blend VB Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        '0e474202': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8df52d2a', 'e0c36e7e'), 'EllenCampus.TailA.Diffuse.1024')),
        ],
        '8df52d2a': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e474202', 'EllenCampus.TailA.Diffuse.2048')),
        ],
        'e0c36e7e': [
            (log,                             ('2.5: EllenCampus TailA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        '8f2cb44d': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a2f7a7db', 'f21e3fa3'), 'EllenCampus.TailA.LightMap.1024')),
        ],
        'a2f7a7db': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8f2cb44d', 'EllenCampus.TailA.LightMap.2048')),
        ],
        'f21e3fa3': [
            (log,                             ('2.5: EllenCampus TailA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        '51cc39d5': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cf37068c', '78e70ba9', 'beb3f207'), 'EllenCampus.TailA.MaterialMap.1024')),
        ],
        'cf37068c': [
            (log,                             ('2.2 - 3.2: EllenCampus TailA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('51cc39d5', 'abb51170'), 'EllenCampus.TailA.MaterialMap.2048')),
        ],
        '78e70ba9': [
            (log,                             ('2.5: EllenCampus TailA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fafcfe36', 'EllenCampus.Tail.IB', 'match_priority = 0\n')),
        ],
        'abb51170': [
            (log,                             ('1.7 -> 2.0: EllenSkin TailA MaterialMap 2048p Hash',)),
            (update_hash,                     ('51cc39d5',)),
        ],
        'beb3f207': [
            (log,                             ('1.5 -> 2.0: EllenSkin TailA MaterialMap 1024p Hash',)),
            (update_hash,                     ('cf37068c',)),
        ],

        # ==================== Face Component ====================
        'f6ef8f3a': [
            (log,                             ('2.2 - 3.2: EllenCampus Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '96baf0ee': [
            (log,                             ('2.2 - 3.2: EllenCampus Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
        ],
        'aca863a9': [
            (log,                             ('2.2 - 3.2: EllenCampus Face Position VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
        ],
        'f87ddcae': [
            (log,                             ('2.2 - 3.1: EllenCampus Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e56b3fdf',)),
        ],
        'e56b3fdf': [
            (log,                             ('3.2: EllenCampus Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '9cc30b79': [
            (log,                             ('2.2 - 3.2: EllenCampus Face Blend VB Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
        ],
        '465a66eb': [
            (log,                             ('2.2 - 3.2: EllenCampus FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4808d050', 'EllenCampus.FaceA.Diffuse.1024')),
        ],
        '4808d050': [
            (log,                             ('2.2 - 3.2: EllenCampus FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f6ef8f3a', 'EllenCampus.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('465a66eb', 'EllenCampus.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 镰刀 Component ====================
        '4ce3a865': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '14ee18a1': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '4140d1e3': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 Position VB Hash',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '64df6d71': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '12c97a8a': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 Blend VB Hash',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        'e9e610cd': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b06f7cb9', 'EllenCampus.weapon - 镰刀.Diffuse.1024')),
            (multiply_section_if_missing,     ('b06f7cb9', 'EllenCampus.weapon - 镰刀 - 弹簧.Diffuse.1024')),
        ],
        'b06f7cb9': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e9e610cd', 'EllenCampus.weapon - 镰刀.Diffuse.2048')),
            (multiply_section_if_missing,     ('e9e610cd', 'EllenCampus.weapon - 镰刀 - 弹簧.Diffuse.2048')),
        ],
        '1721ed1a': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0567bc4e', 'EllenCampus.weapon - 镰刀.LightMap.1024')),
            (multiply_section_if_missing,     ('0567bc4e', 'EllenCampus.weapon - 镰刀 - 弹簧.LightMap.1024')),
        ],
        '0567bc4e': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1721ed1a', 'EllenCampus.weapon - 镰刀.LightMap.2048')),
            (multiply_section_if_missing,     ('1721ed1a', 'EllenCampus.weapon - 镰刀 - 弹簧.LightMap.2048')),
        ],
        '9aaa6b4b': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4c2adaa', 'EllenCampus.weapon - 镰刀.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d4c2adaa', 'EllenCampus.weapon - 镰刀 - 弹簧.MaterialMap.1024')),
        ],
        'd4c2adaa': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 and weapon - 镰刀 - 弹簧 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4ce3a865', 'EllenCampus.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9aaa6b4b', 'EllenCampus.weapon - 镰刀.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9aaa6b4b', 'EllenCampus.weapon - 镰刀 - 弹簧.MaterialMap.2048')),
        ],

        # ==================== Weapon - 镰刀 - 弹簧 Component ====================
        '2747bdd1': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 - 弹簧 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a063d963': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 - 弹簧 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        '4b5ecba8': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 - 弹簧 Position VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        '21b31add': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 - 弹簧 Texcoord VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        '4afdcca5': [
            (log,                             ('2.2 - 3.2: EllenCampus weapon - 镰刀 - 弹簧 Blend VB Hash',)),
            (add_section_if_missing,          ('2747bdd1', 'EllenCampus.weapon - 镰刀 - 弹簧.IB', 'match_priority = 0\n')),
        ],
        # weapon - 镰刀 - 弹簧 shares all hashes with weapon - 镰刀; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'EllenCampus',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
