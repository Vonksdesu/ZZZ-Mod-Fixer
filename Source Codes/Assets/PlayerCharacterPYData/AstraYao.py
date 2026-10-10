"""
AstraYao Character Hash Commands
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
    Returns AstraYao's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '53cdac6c': [
            (log,                             ('1.5: AstraYao Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ee3c305a': [
            (log,                             ('2.2: AstraYao Hair Position VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
        ],
        'c3c08f85': [
            (log,                             ('2.2: AstraYao Hair Blend VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
        ],
        'f8b92870': [
            (log,                             ('1.5 -> 1.6: AstraYao Hair Texcoord Hash',)),
            (update_hash,                     ('8ba0b335',)),
        ],
        '8ba0b335': [
            (log,                             ('1.6: AstraYao Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
        ],
        'd3c951b9': [
            (log,                             ('2.2: AstraYao Hair Draw VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2: AstraYao HairA, TorsoA, LegsA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.TorsoA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.WeaponB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYao.WeaponC.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2: AstraYao HairA, TorsoA, LegsA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.TorsoA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.WeaponB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYao.WeaponC.NormalMap.2048')),
        ],
        'da673df0': [
            (log,                             ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 2048p Hash',)),
            (update_hash,                     ('2daa2443',)),
        ],
        '2daa2443': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 2048p Hash',)),
            (update_hash,                     ('e634238a',)),
        ],
        'e634238a': [
            (log,                             ('1.6: AstraYao HairA and LegsA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('56c71ea2', '4b1c1b47', '7a507e4a'), 'AstraYao.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('56c71ea2', '4b1c1b47', '7a507e4a'), 'AstraYao.LegsA.Diffuse.1024')),
        ],
        '34aad3b4': [
            (log,                             ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 2048p Hash',)),
            (update_hash,                     ('b085765e',)),
        ],
        'b085765e': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 2048p Hash',)),
            (update_hash,                     ('34f0706c',)),
        ],
        '34f0706c': [
            (log,                             ('1.6: AstraYao HairA and LegsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fd3ca2a6', 'c47a524a', 'e4a4f975'), 'AstraYao.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('fd3ca2a6', 'c47a524a', 'e4a4f975'), 'AstraYao.LegsA.LightMap.1024')),
        ],
        'b53b2e12': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 2048p Hash',)),
            (update_hash,                     ('883a578f',)),
        ],
        '883a578f': [
            (log,                             ('1.6: AstraYao HairA and LegsA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('759c15e0', '0be99d44'), 'AstraYao.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('759c15e0', '0be99d44'), 'AstraYao.LegsA.MaterialMap.1024')),
        ],
        '7a507e4a': [
            (log,                             ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 1024p Hash',)),
            (update_hash,                     ('4b1c1b47',)),
        ],
        '4b1c1b47': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 1024p Hash',)),
            (update_hash,                     ('56c71ea2',)),
        ],
        '56c71ea2': [
            (log,                             ('1.6: AstraYao HairA and LegsA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('e634238a', '2daa2443', 'da673df0'), 'AstraYao.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('e634238a', '2daa2443', 'da673df0'), 'AstraYao.LegsA.Diffuse.2048')),
        ],
        'e4a4f975': [
            (log,                             ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 1024p Hash',)),
            (update_hash,                     ('c47a524a',)),
        ],
        'c47a524a': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 1024p Hash',)),
            (update_hash,                     ('fd3ca2a6',)),
        ],
        'fd3ca2a6': [
            (log,                             ('1.6: AstraYao HairA and LegsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('34f0706c', 'b085765e', '34aad3b4'), 'AstraYao.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('34f0706c', 'b085765e', '34aad3b4'), 'AstraYao.LegsA.LightMap.2048')),
        ],
        '0be99d44': [
            (log,                             ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 1024p Hash',)),
            (update_hash,                     ('759c15e0',)),
        ],
        '759c15e0': [
            (log,                             ('1.6: AstraYao HairA and LegsA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('883a578f', 'b53b2e12'), 'AstraYao.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('883a578f', 'b53b2e12'), 'AstraYao.LegsA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '93d55a49': [
            (log,                             ('2.2: AstraYao Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5e1e12aa': [
            (log,                             ('2.2: AstraYao Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a378328a': [
            (log,                             ('2.2: AstraYao Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'c4456161': [
            (log,                             ('2.2: AstraYao Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '81ef699b': [
            (log,                             ('2.2: AstraYao Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Torso Component ====================
        '7a110804': [
            (log,                             ('1.5: AstraYao Torso IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9b17301d': [
            (log,                             ('2.2: AstraYao Torso Position VB Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
        ],
        '3cd13d03': [
            (log,                             ('1.5 -> 1.6: AstraYao Torso Blend Hash',)),
            (update_hash,                     ('9d35c352',)),
        ],
        '9d35c352': [
            (log,                             ('1.6: AstraYao Torso Blend VB Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
        ],
        '240d8c83': [
            (log,                             ('2.2: AstraYao Torso Texcoord VB Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
        ],
        '13a07361': [
            (log,                             ('2.2: AstraYao Torso Draw VB Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
        ],
        'd7f1c157': [
            (log,                             ('1.5: AstraYao TorsoA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e523eb0f', 'AstraYao.TorsoA.Diffuse.1024')),
        ],
        'dba7d767': [
            (log,                             ('1.5: AstraYao TorsoA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f9f0d8a', 'AstraYao.TorsoA.LightMap.1024')),
        ],
        '21d5f5e3': [
            (log,                             ('1.5: AstraYao TorsoA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c4248e2d', 'AstraYao.TorsoA.MaterialMap.1024')),
        ],
        'e523eb0f': [
            (log,                             ('1.5: AstraYao TorsoA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d7f1c157', 'AstraYao.TorsoA.Diffuse.2048')),
        ],
        '3f9f0d8a': [
            (log,                             ('1.5: AstraYao TorsoA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dba7d767', 'AstraYao.TorsoA.LightMap.2048')),
        ],
        'c4248e2d': [
            (log,                             ('1.5: AstraYao TorsoA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('21d5f5e3', 'AstraYao.TorsoA.MaterialMap.2048')),
        ],

        # ==================== Legs Component ====================
        '92f33156': [
            (log,                             ('1.5: AstraYao Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '97cef448': [
            (log,                             ('2.2: AstraYao Legs Position VB Hash',)),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
        ],
        'bc4d6455': [
            (log,                             ('2.2: AstraYao Legs Blend VB Hash',)),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
        ],
        'da86a32e': [
            (log,                             ('1.5 -> 1.6: AstraYao Legs Texcoord Hash',)),
            (update_hash,                     ('1433ee78',)),
        ],
        '1433ee78': [
            (log,                             ('1.6: AstraYao Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
        ],
        '8a8dbdc5': [
            (log,                             ('2.2: AstraYao Legs Draw VB Hash',)),
            (add_section_if_missing,          ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '51831437': [
            (log,                             ('1.5: AstraYao Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '66451cc2': [
            (log,                             ('2.2: AstraYao Face Position VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        ],
        'ffac76ac': [
            (log,                             ('2.2: AstraYao Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('01b43c04',)),
        ],
        '01b43c04': [
            (log,                             ('3.2: AstraYao Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7e05c11a': [
            (log,                             ('2.2: AstraYao Face Blend VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        ],
        '5c578f85': [
            (log,                             ('2.2: AstraYao Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        ],
        '3a8d0dfc': [
            (log,                             ('1.5 -> 1.6: AstraYao Face Diffuse 2048p Hash',)),
            (update_hash,                     ('c41341b2',)),
        ],
        'c41341b2': [
            (log,                             ('1.6: AstraYao FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('3283b8be', '77670042'), 'AstraYao.FaceA.Diffuse.1024')),
        ],
        '77670042': [
            (log,                             ('1.5 -> 1.6: AstraYao Face Diffuse 1024p Hash',)),
            (update_hash,                     ('3283b8be',)),
        ],
        '3283b8be': [
            (log,                             ('1.6: AstraYao FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('c41341b2', '3a8d0dfc'), 'AstraYao.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 本体 Component ====================
        '702b018e': [
            (log,                             ('2.2: AstraYao weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9879faf3': [
            (log,                             ('2.2: AstraYao weapon Position VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        'b3e27d5f': [
            (log,                             ('2.2: AstraYao weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '4a4fb44e': [
            (log,                             ('2.2: AstraYao weapon Blend VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        'ca16b939': [
            (log,                             ('2.2: AstraYao weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        'b5a20274': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d652aa31', 'AstraYao.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d652aa31', 'AstraYao.WeaponB.Diffuse.1024')),
        ],
        '57c44e60': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91c63955', 'AstraYao.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('91c63955', 'AstraYao.WeaponB.LightMap.1024')),
        ],
        'fdb82c44': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('98e011bc', 'AstraYao.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('98e011bc', 'AstraYao.WeaponB.MaterialMap.1024')),
        ],
        'd652aa31': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5a20274', 'AstraYao.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('b5a20274', 'AstraYao.WeaponB.Diffuse.2048')),
        ],
        '91c63955': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57c44e60', 'AstraYao.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('57c44e60', 'AstraYao.WeaponB.LightMap.2048')),
        ],
        '98e011bc': [
            (log,                             ('2.2: AstraYao WeaponA and WeaponB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fdb82c44', 'AstraYao.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('fdb82c44', 'AstraYao.WeaponB.MaterialMap.2048')),
        ],

        # ==================== Weapon - 唱片 Component ====================
        'f4f5348d': [
            (log,                             ('2.2: AstraYao weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b8a9ba2e': [
            (log,                             ('2.2: AstraYao weapon Position VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        'd6d5743e': [
            (log,                             ('2.2: AstraYao weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        'cb9405e1': [
            (log,                             ('2.2: AstraYao weapon Blend VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '7ed93255': [
            (log,                             ('2.2: AstraYao weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon - 唱片-技能唱歌状态 Component ====================
        '9bb42122': [
            (log,                             ('2.2: AstraYao weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ced4a85d': [
            (log,                             ('2.2: AstraYao weapon Position VB Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '401e9639': [
            (log,                             ('2.2: AstraYao weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '8a2319f4': [
            (log,                             ('2.2: AstraYao weapon Blend VB Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '6c67049b': [
            (log,                             ('2.2: AstraYao weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
        ],
        '7503323d': [
            (log,                             ('2.2: AstraYao WeaponC Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9a9e8842', 'AstraYao.WeaponC.Diffuse.1024')),
        ],
        '484c92d6': [
            (log,                             ('1.7 -> 2.0: AstraYao WeaponC LightMap 2048p Hash',)),
            (update_hash,                     ('7e5fe2c6',)),
        ],
        '7e5fe2c6': [
            (log,                             ('2.0: AstraYao WeaponC LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('364023c4', 'AstraYao.WeaponC.LightMap.1024')),
        ],
        'd1d0d241': [
            (log,                             ('1.7 -> 2.0: AstraYao WeaponC MaterialMap 2048p Hash',)),
            (update_hash,                     ('87687182',)),
        ],
        '87687182': [
            (log,                             ('2.0: AstraYao WeaponC MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fc68cf7d', 'AstraYao.WeaponC.MaterialMap.1024')),
        ],
        '9a9e8842': [
            (log,                             ('2.2: AstraYao WeaponC Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7503323d', 'AstraYao.WeaponC.Diffuse.2048')),
        ],
        '364023c4': [
            (log,                             ('2.2: AstraYao WeaponC LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7e5fe2c6', 'AstraYao.WeaponC.LightMap.2048')),
        ],
        'fc68cf7d': [
            (log,                             ('2.2: AstraYao WeaponC MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('87687182', 'AstraYao.WeaponC.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AstraYao',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}