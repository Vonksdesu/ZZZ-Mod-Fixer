"""
JuFufu Character Hash Commands
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
    Returns JuFufu's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'a4fd9113': [
            (log,                             ('2.2 - 3.2: JuFufu Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '77d02cb1': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Draw VB Hash',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        ],
        'e836ec8f': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Position VB Hash',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        ],
        'fbca830d': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        ],
        'c9c19a97': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Blend VB Hash',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
        ],
        'db3bdffa': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('521f60ae', 'JuFufu.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('521f60ae', 'JuFufu.TailA.Diffuse.1024')),
        ],
        '521f60ae': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('db3bdffa', 'JuFufu.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('db3bdffa', 'JuFufu.TailA.Diffuse.2048')),
        ],
        '5c948f7b': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('29bb13b7', 'JuFufu.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('29bb13b7', 'JuFufu.TailA.LightMap.1024')),
        ],
        '29bb13b7': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5c948f7b', 'JuFufu.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('5c948f7b', 'JuFufu.TailA.LightMap.2048')),
        ],
        '9f4d4f72': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9355dcea', 'JuFufu.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('9355dcea', 'JuFufu.TailA.MaterialMap.1024')),
        ],
        '9355dcea': [
            (log,                             ('2.2 - 3.2: JuFufu HairA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f4d4f72', 'JuFufu.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9f4d4f72', 'JuFufu.TailA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: JuFufu HairA, BodyA, TailA, weapon - 左手爪, weapon - 右手爪 and weapon - 虎威 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.weapon - 左手爪.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.weapon - 右手爪.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JuFufu.weapon - 虎威.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: JuFufu HairA, BodyA, TailA, weapon - 左手爪, weapon - 右手爪 and weapon - 虎威 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a4fd9113', 'JuFufu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.weapon - 左手爪.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.weapon - 右手爪.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JuFufu.weapon - 虎威.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '095f38e8': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e636c467': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'f0e84fef': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '60d9a4fc': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b18001e6': [
            (log,                             ('2.2 - 3.2: JuFufu Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('095f38e8', 'JuFufu.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'de303163': [
            (log,                             ('2.2 - 3.2: JuFufu Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5c076ce8': [
            (log,                             ('2.2 - 3.2: JuFufu Body Draw VB Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        ],
        '00ba64ca': [
            (log,                             ('2.2 - 3.2: JuFufu Body Position VB Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        ],
        '2e086db7': [
            (log,                             ('2.2 - 3.2: JuFufu Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        ],
        'c06c0417': [
            (log,                             ('2.2 - 3.2: JuFufu Body Blend VB Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
        ],
        '16e4cac1': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3b372932', 'JuFufu.BodyA.Diffuse.1024')),
        ],
        '3b372932': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('16e4cac1', 'JuFufu.BodyA.Diffuse.2048')),
        ],
        'c952431f': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9d1ab7c4', 'JuFufu.BodyA.LightMap.1024')),
        ],
        '9d1ab7c4': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c952431f', 'JuFufu.BodyA.LightMap.2048')),
        ],
        'd555b4f8': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f72af17c', 'JuFufu.BodyA.MaterialMap.1024')),
        ],
        'f72af17c': [
            (log,                             ('2.2 - 3.2: JuFufu BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('de303163', 'JuFufu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d555b4f8', 'JuFufu.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Tail Component ====================
        'f8ab3141': [
            (log,                             ('2.2 - 3.2: JuFufu Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c84e77d4': [
            (log,                             ('2.2 - 3.2: JuFufu Tail Draw VB Hash',)),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        ],
        'c397375f': [
            (log,                             ('2.2 - 3.2: JuFufu Tail Position VB Hash',)),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        ],
        '9a198bcf': [
            (log,                             ('2.2 - 3.2: JuFufu Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        ],
        'c8fa66e3': [
            (log,                             ('2.2 - 3.2: JuFufu Tail Blend VB Hash',)),
            (add_section_if_missing,          ('f8ab3141', 'JuFufu.Tail.IB', 'match_priority = 0\n')),
        ],
        # Tail shares its Diffuse/LightMap/MaterialMap with Hair, and NormalMap with Hair; see that Component above.

        # ==================== Face Component ====================
        '321768df': [
            (log,                             ('2.2 - 3.2: JuFufu Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd7802a0b': [
            (log,                             ('2.2 - 3.2: JuFufu Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
        ],
        'ed92b94c': [
            (log,                             ('2.2 - 3.2: JuFufu Face Position VB Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
        ],
        '8267358b': [
            (log,                             ('2.2 - 3.1: JuFufu Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('768c9ec4',)),
        ],
        '768c9ec4': [
            (log,                             ('3.2: JuFufu Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '512615d6': [
            (log,                             ('2.2 - 3.2: JuFufu Face Blend VB Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
        ],
        '37b277db': [
            (log,                             ('2.2 - 3.2: JuFufu FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('134fbe43', 'JuFufu.FaceA.Diffuse.1024')),
        ],
        '134fbe43': [
            (log,                             ('2.2 - 3.2: JuFufu FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('321768df', 'JuFufu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('37b277db', 'JuFufu.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 左手爪 Component ====================
        'a27835bb': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '303b7a17': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
        ],
        '41006dfa': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 Position VB Hash',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
        ],
        'ce435978': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
        ],
        'fbb7c2a6': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 Blend VB Hash',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
        ],
        '401f92e6': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9a93726a', 'JuFufu.weapon - 左手爪.Diffuse.1024')),
            (multiply_section_if_missing,     ('9a93726a', 'JuFufu.weapon - 右手爪.Diffuse.1024')),
        ],
        '9a93726a': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('401f92e6', 'JuFufu.weapon - 左手爪.Diffuse.2048')),
            (multiply_section_if_missing,     ('401f92e6', 'JuFufu.weapon - 右手爪.Diffuse.2048')),
        ],
        '1b61ae30': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1738f744', 'JuFufu.weapon - 左手爪.LightMap.1024')),
            (multiply_section_if_missing,     ('1738f744', 'JuFufu.weapon - 右手爪.LightMap.1024')),
        ],
        '1738f744': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1b61ae30', 'JuFufu.weapon - 左手爪.LightMap.2048')),
            (multiply_section_if_missing,     ('1b61ae30', 'JuFufu.weapon - 右手爪.LightMap.2048')),
        ],
        'e62eed48': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d54f20a', 'JuFufu.weapon - 左手爪.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7d54f20a', 'JuFufu.weapon - 右手爪.MaterialMap.1024')),
        ],
        '7d54f20a': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 左手爪 and weapon - 右手爪 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a27835bb', 'JuFufu.weapon - 左手爪.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e62eed48', 'JuFufu.weapon - 左手爪.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e62eed48', 'JuFufu.weapon - 右手爪.MaterialMap.2048')),
        ],
        # weapon - 左手爪 shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Weapon - 右手爪 Component ====================
        '46e339a6': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 右手爪 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0468fc0c': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 右手爪 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
        ],
        '45b2b661': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 右手爪 Position VB Hash',)),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
        ],
        '395481f4': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 右手爪 Texcoord VB Hash',)),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
        ],
        '18a54256': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 右手爪 Blend VB Hash',)),
            (add_section_if_missing,          ('46e339a6', 'JuFufu.weapon - 右手爪.IB', 'match_priority = 0\n')),
        ],
        # weapon - 右手爪 shares its Diffuse/LightMap/MaterialMap with weapon - 左手爪, and NormalMap with Hair; see those Components above.

        # ==================== Weapon - 虎威 Component ====================
        'b51e30e5': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '03768505': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
        ],
        '245e6459': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 Position VB Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
        ],
        '1544d097': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
        ],
        '7778328f': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 Blend VB Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
        ],
        '094ac0a2': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('27928ca3', 'JuFufu.weapon - 虎威.Diffuse.1024')),
        ],
        '27928ca3': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('094ac0a2', 'JuFufu.weapon - 虎威.Diffuse.2048')),
        ],
        '4bb30541': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('87e25f7d', 'JuFufu.weapon - 虎威.LightMap.1024')),
        ],
        '87e25f7d': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4bb30541', 'JuFufu.weapon - 虎威.LightMap.2048')),
        ],
        '9db94a04': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('26d6f075', 'JuFufu.weapon - 虎威.MaterialMap.1024')),
        ],
        '26d6f075': [
            (log,                             ('2.2 - 3.2: JuFufu weapon - 虎威 MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b51e30e5', 'JuFufu.weapon - 虎威.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9db94a04', 'JuFufu.weapon - 虎威.MaterialMap.2048')),
        ],
        # weapon - 虎威 shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JuFufu',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
