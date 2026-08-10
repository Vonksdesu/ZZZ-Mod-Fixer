"""
AstraYao Character Hash Commands
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
    Returns AstraYao's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'53cdac6c': [(log, ('1.5 - 2.5: AstraYao Hair IB Hash',)), (add_ib_check_if_missing,)],
'7a110804': [(log, ('1.5 - 2.5: AstraYao Body IB Hash',)), (add_ib_check_if_missing,)],
'92f33156': [(log, ('1.5 - 2.5: AstraYao Legs IB Hash',)), (add_ib_check_if_missing,)],
'51831437': [(log, ('1.5 - 2.5: AstraYao Face IB Hash',)), (add_ib_check_if_missing,)],
'ee3c305a': [(log, ('2.5: AstraYao Hair Position VB Hash',))],
'c3c08f85': [(log, ('2.5: AstraYao Hair Blend VB Hash',))],
'8ba0b335': [(log, ('2.5: AstraYao Hair Texcoord VB Hash',))],
'f8b92870': [(log, ('1.5 -> 1.6: AstraYao Hair Texcoord Hash',)), (update_hash, ('8ba0b335',)),],
'9b17301d': [(log, ('2.5: AstraYao Body Position VB Hash',))],
'9d35c352': [(log, ('2.5: AstraYao Body Blend VB Hash',))],
'240d8c83': [(log, ('2.5: AstraYao Body Texcoord VB Hash',))],
'3cd13d03': [(log, ('1.5 -> 1.6: AstraYao Body Blend Hash',)),    (update_hash, ('9d35c352',)),],
'97cef448': [(log, ('2.5: AstraYao Legs Position VB Hash',))],
'bc4d6455': [(log, ('2.5: AstraYao Legs Blend VB Hash',))],
'1433ee78': [(log, ('2.5: AstraYao Legs Texcoord VB Hash',))],
'da86a32e': [(log, ('1.5 -> 1.6: AstraYao Legs Texcoord Hash',)), (update_hash, ('1433ee78',)),],
'77670042': [(log, ('1.5 -> 1.6: AstraYao Face Diffuse 1024p Hash',)), (update_hash, ('3283b8be',))],
'3283b8be': [
        (log,                           ('1.6 - 2.5: AstraYao FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('c41341b2', '3a8d0dfc'), 'AstraYao.FaceA.Diffuse.2048')),
    ],
'3a8d0dfc': [(log, ('1.5 -> 1.6: AstraYao Face Diffuse 2048p Hash',)), (update_hash, ('c41341b2',))],
'c41341b2': [
        (log,                           ('1.6 - 2.5: AstraYao FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3283b8be', '77670042'), 'AstraYao.FaceA.Diffuse.1024')),
    ],
'da673df0': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 2048p Hash',)), (update_hash, ('2daa2443',))],
'2daa2443': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 2048p Hash',)),   (update_hash, ('e634238a',))],
'e634238a': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('56c71ea2', '4b1c1b47', '7a507e4a'), 'AstraYao.HairA.Diffuse.1024')),
    ],
'34aad3b4': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 2048p Hash',)), (update_hash, ('b085765e',))],
'b085765e': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 2048p Hash',)),   (update_hash, ('34f0706c',))],
'34f0706c': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   (('fd3ca2a6', 'c47a524a', 'e4a4f975'), 'AstraYao.HairA.LightMap.1024')),
    ],
'b53b2e12': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 2048p Hash',)), (update_hash, ('883a578f',))],
'883a578f': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   (('759c15e0', '0be99d44'), 'AstraYao.HairA.MaterialMap.1024')),
    ],
'7a507e4a': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA Diffuse 1024p Hash',)), (update_hash, ('4b1c1b47',))],
'4b1c1b47': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA Diffuse 1024p Hash',)),   (update_hash, ('56c71ea2',))],
'56c71ea2': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('e634238a', '2daa2443', 'da673df0'), 'AstraYao.HairA.Diffuse.2048')),
    ],
'e4a4f975': [(log, ('1.5A -> 1.5B: AstraYao HairA, LegsA LightMap 1024p Hash',)), (update_hash, ('c47a524a',))],
'c47a524a': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA LightMap 1024p Hash',)),   (update_hash, ('fd3ca2a6',))],
'fd3ca2a6': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   (('34f0706c', 'b085765e', '34aad3b4'), 'AstraYao.HairA.LightMap.2048')),
    ],
'0be99d44': [(log, ('1.5 -> 1.6: AstraYao HairA, LegsA MaterialMap 1024p Hash',)), (update_hash, ('759c15e0',))],
'759c15e0': [
        (log,                           ('1.6 - 2.5: AstraYao HairA, LegsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   (('883a578f', 'b53b2e12'), 'AstraYao.HairA.MaterialMap.2048')),
    ],
'd7f1c157': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e523eb0f', 'AstraYao.BodyA.Diffuse.1024')),
    ],
'dba7d767': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3f9f0d8a', 'AstraYao.BodyA.LightMap.1024')),
    ],
'21d5f5e3': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c4248e2d', 'AstraYao.BodyA.MaterialMap.1024')),
    ],
'e523eb0f': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d7f1c157', 'AstraYao.BodyA.Diffuse.2048')),
    ],
'3f9f0d8a': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dba7d767', 'AstraYao.BodyA.LightMap.2048')),
    ],
'c4248e2d': [
        (log,                           ('1.5 - 2.5: AstraYao BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7a110804', 'AstraYao.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('21d5f5e3', 'AstraYao.BodyA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log, ('3.0: AstraYao Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
    ],
'93d55a49': [(log, ('3.0: AstraYao Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'5e1e12aa': [
        (log, ('3.0: AstraYao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a378328a': [
        (log, ('3.0: AstraYao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'c4456161': [
        (log, ('3.0: AstraYao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'81ef699b': [
        (log, ('3.0: AstraYao Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYao.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'13a07361': [
        (log, ('3.0: AstraYao Torso VB Hash',)),
        (add_section_if_missing, ('7a110804', 'AstraYao.Torso.IB', 'match_priority = 0\n')),
    ],
'8a8dbdc5': [
        (log, ('3.0: AstraYao Legs VB Hash',)),
        (add_section_if_missing, ('92f33156', 'AstraYao.Legs.IB', 'match_priority = 0\n')),
    ],
'66451cc2': [
        (log, ('3.0: AstraYao Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
    ],
'ffac76ac': [
        (log, ('3.0: AstraYao Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
    ],
'7e05c11a': [
        (log, ('3.0: AstraYao Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYao.Face.IB', 'match_priority = 0\n')),
    ],
'702b018e': [(log, ('3.0: AstraYao weapon IB Hash',)), (add_ib_check_if_missing,)],
'9879faf3': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'b3e27d5f': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'4a4fb44e': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'b5a20274': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'57c44e60': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'fdb82c44': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'f4f5348d': [(log, ('3.0: AstraYao weapon IB Hash',)), (add_ib_check_if_missing,)],
'b8a9ba2e': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'd6d5743e': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'cb9405e1': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'9bb42122': [(log, ('3.0: AstraYao weapon IB Hash',)), (add_ib_check_if_missing,)],
'ced4a85d': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'401e9639': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'8a2319f4': [
        (log, ('3.0: AstraYao weapon VB Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'7503323d': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'7e5fe2c6': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'87687182': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'5c578f85': [(log, ('3.0: AstraYao misc hash',)),],
'6c67049b': [(log, ('3.0: AstraYao misc hash',)),],
'7ed93255': [(log, ('3.0: AstraYao misc hash',)),],
'ca16b939': [(log, ('3.0: AstraYao misc hash',)),],
'd3c951b9': [
        (log, ('3.0: AstraYao Hair VB Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: AstraYao Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYao.Hair.IB', 'match_priority = 0\n')),
    ],
'd652aa31': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'91c63955': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'98e011bc': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'9a9e8842': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'364023c4': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
'fc68cf7d': [
        (log, ('3.0: AstraYao weapon TEX Hash',)),
        (add_section_if_missing, ('9bb42122', 'AstraYao.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AstraYao',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
