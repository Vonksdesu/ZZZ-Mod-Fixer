"""
Vivian Character Hash Commands
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
    Returns Vivian's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'c4eb6168': [(log, ('2.5: Vivian Hair IB Hash',)), (add_ib_check_if_missing,)],
'cd609d98': [(log, ('2.5: Vivian Body IB Hash',)), (add_ib_check_if_missing,)],
'14602a61': [(log, ('2.5: Vivian Gem IB Hash',)), (add_ib_check_if_missing,)],
'39944f20': [(log, ('2.5: Vivian Face IB Hash',)), (add_ib_check_if_missing,)],
'7b262ab6': [
        (log,                           ('2.5: Vivian FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('66b5da8e', 'Vivian.FaceA.Diffuse.1024')),
    ],
'66b5da8e': [
        (log,                           ('2.5: Vivian FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7b262ab6', 'Vivian.FaceA.Diffuse.2048')),
    ],
'a84d933f': [
        (log,                           ('2.5: Vivian HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2df6f7b5', 'Vivian.HairA.Diffuse.1024')),
    ],
'2df6f7b5': [
        (log,                           ('2.5: Vivian HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a84d933f', 'Vivian.HairA.Diffuse.2048')),
    ],
'8e3a20ea': [
        (log,                           ('2.5: Vivian HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('36b80366', 'Vivian.HairA.LightMap.1024')),
    ],
'36b80366': [
        (log,                           ('2.5: Vivian HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8e3a20ea', 'Vivian.HairA.LightMap.2048')),
    ],
'2af66072': [
        (log,                           ('2.5: Vivian HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2d5b1412', 'Vivian.HairA.MaterialMap.1024')),
    ],
'2d5b1412': [
        (log,                           ('2.5: Vivian HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2af66072', 'Vivian.HairA.MaterialMap.2048')),
    ],
'0635e2dd': [
        (log,                           ('2.5: Vivian BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da41fbd6', 'Vivian.BodyA.Diffuse.1024')),
    ],
'da41fbd6': [
        (log,                           ('2.5: Vivian BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0635e2dd', 'Vivian.BodyA.Diffuse.2048')),
    ],
'e21c3a6b': [
        (log,                           ('2.5: Vivian BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a86e169', 'Vivian.BodyA.LightMap.1024')),
    ],
'4a86e169': [
        (log,                           ('2.5: Vivian BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e21c3a6b', 'Vivian.BodyA.LightMap.2048')),
    ],
'81f7d37c': [
        (log,                           ('2.5: Vivian BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fa650e6c', 'Vivian.BodyA.MaterialMap.1024')),
    ],
'fa650e6c': [
        (log,                           ('2.5: Vivian BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('81f7d37c', 'Vivian.BodyA.MaterialMap.2048')),
    ],
'71d0dfd9': [
        (log, ('3.0: Vivian Hair VB Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'406beb54': [
        (log, ('3.0: Vivian Hair VB Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'ef4a8bb6': [
        (log, ('3.0: Vivian Hair VB Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Vivian Hair TEX Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'548f7dff': [(log, ('3.0: Vivian Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'b1bf0e1a': [
        (log, ('3.0: Vivian Hair Shadow VB Hash',)),
        (add_section_if_missing, ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a544d14e': [
        (log, ('3.0: Vivian Hair Shadow VB Hash',)),
        (add_section_if_missing, ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4a5054ba': [
        (log, ('3.0: Vivian Hair Shadow VB Hash',)),
        (add_section_if_missing, ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'2376d129': [
        (log, ('3.0: Vivian Hair Shadow VB Hash',)),
        (add_section_if_missing, ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'5c34690a': [
        (log, ('3.0: Vivian Body VB Hash',)),
        (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
    ],
'64a6b06d': [
        (log, ('3.0: Vivian Body VB Hash',)),
        (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
    ],
'55dae493': [
        (log, ('3.0: Vivian Body VB Hash',)),
        (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
    ],
'e7122fe8': [
        (log, ('3.0: Vivian Body VB Hash',)),
        (add_section_if_missing, ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
    ],
'8a6fd2f9': [
        (log, ('3.0: Vivian Gem VB Hash',)),
        (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
    ],
'3c32547b': [
        (log, ('3.0: Vivian Gem VB Hash',)),
        (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
    ],
'45c0ac67': [
        (log, ('3.0: Vivian Gem VB Hash',)),
        (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
    ],
'a23da1ce': [
        (log, ('3.0: Vivian Gem VB Hash',)),
        (add_section_if_missing, ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
    ],
'c6e5dc87': [
        (log, ('3.0: Vivian Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
    ],
'0afe5a44': [
        (log, ('3.0: Vivian Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
    ],
'ef07b6f6': [
        (log, ('3.0: Vivian Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
    ],
'1b843cb1': [(log, ('3.0: Vivian weapon IB Hash',)), (add_ib_check_if_missing,)],
'7c80f1d8': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'79ee2ea7': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'5d4a63ca': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'e2327fb8': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'9277a2c1': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'dd8a1851': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'7232ac6f': [(log, ('3.0: Vivian weapon IB Hash',)), (add_ib_check_if_missing,)],
'd06d75e0': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('7232ac6f', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'2e01f6e0': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('7232ac6f', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'b24f5c99': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('7232ac6f', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'28f8090e': [(log, ('3.0: Vivian weapon IB Hash',)), (add_ib_check_if_missing,)],
'b586b07e': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('28f8090e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'2809e5db': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('28f8090e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'd97d4c96': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('28f8090e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'a031575e': [(log, ('3.0: Vivian weapon IB Hash',)), (add_ib_check_if_missing,)],
'cb21ccdf': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('a031575e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'af180e46': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('a031575e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'12f34479': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('a031575e', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'e69dfc8c': [(log, ('3.0: Vivian weapon IB Hash',)), (add_ib_check_if_missing,)],
'30e3560c': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('e69dfc8c', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'c8ede4d4': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('e69dfc8c', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'15002e84': [
        (log, ('3.0: Vivian weapon VB Hash',)),
        (add_section_if_missing, ('e69dfc8c', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'56ccb629': [(log, ('3.0: Vivian misc hash',)),],
'66cc3370': [(log, ('3.0: Vivian misc hash',)),],
'8413730c': [(log, ('3.0: Vivian misc hash',)),],
'cc2d7ad1': [(log, ('3.0: Vivian misc hash',)),],
'd175e722': [(log, ('3.0: Vivian misc hash',)),],
'fcf74fc0': [(log, ('3.0: Vivian misc hash',)),],
'2e01f7f7': [
        (log, ('3.0: Vivian Hair VB Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Vivian Hair TEX Hash',)),
        (add_section_if_missing, ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
    ],
'bf6a1304': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'a33edccd': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
'ab4cde14': [
        (log, ('3.0: Vivian weapon TEX Hash',)),
        (add_section_if_missing, ('1b843cb1', 'Vivian.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Vivian',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
