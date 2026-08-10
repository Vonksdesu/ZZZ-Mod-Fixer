"""
VivianIrisOfTheShore Character Hash Commands
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
    Returns VivianIrisOfTheShore's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'4108c0da': [(log, ('2.5: VivianIrisOfTheShore Hair IB Hash',)), (add_ib_check_if_missing,)],
'3060793b': [(log, ('2.5: VivianIrisOfTheShore Body IB Hash',)), (add_ib_check_if_missing,)],
'ec7b047c': [(log, ('2.5: VivianIrisOfTheShore Gem IB Hash',)), (add_ib_check_if_missing,)],
'39944f20': [(log, ('2.5: VivianIrisOfTheShore Face IB Hash (shared with Vivian)',)), (add_ib_check_if_missing,)],
'7b262ab6': [
        (log,                           ('2.5: VivianIrisOfTheShore FaceA Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
    ],
'15dcce65': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('427be7bd', 'VivianIrisOfTheShore.HairA.Diffuse.1024')),
    ],

'427be7bd': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('15dcce65', 'VivianIrisOfTheShore.HairA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyA, GemA NormalMap Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
    ],
'8a82d289': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('45b67c0b', 'VivianIrisOfTheShore.HairA.LightMap.1024')),
    ],

'45b67c0b': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8a82d289', 'VivianIrisOfTheShore.HairA.LightMap.2048')),
    ],
'c23ddbea': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('cdb06288', 'VivianIrisOfTheShore.HairA.MaterialMap.1024')),
    ],

'cdb06288': [
        (log,                           ('2.5: VivianIrisOfTheShore HairA, BodyC, BodyD, GemA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c23ddbea', 'VivianIrisOfTheShore.HairA.MaterialMap.2048')),
    ],
'a84d933f': [
        (log,                           ('2.5: VivianIrisOfTheShore HairB, HairC Diffuse Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'8e3a20ea': [
        (log,                           ('2.5: VivianIrisOfTheShore HairB, HairC LightMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'2af66072': [
        (log,                           ('2.5: VivianIrisOfTheShore HairB, HairC MaterialMap Hash (shared with Vivian)',)),
        (add_section_if_missing,        ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'136b3e29': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1ea05046', 'VivianIrisOfTheShore.BodyA.Diffuse.1024')),
    ],

'1ea05046': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('136b3e29', 'VivianIrisOfTheShore.BodyA.Diffuse.2048')),
    ],
'69a6a15f': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e8bb6a0f', 'VivianIrisOfTheShore.BodyA.LightMap.1024')),
    ],

'e8bb6a0f': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('69a6a15f', 'VivianIrisOfTheShore.BodyA.LightMap.2048')),
    ],
'527c3676': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('909ea74d', 'VivianIrisOfTheShore.BodyA.MaterialMap.1024')),
    ],

'909ea74d': [
        (log,                           ('2.5: VivianIrisOfTheShore BodyA, BodyB MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('527c3676', 'VivianIrisOfTheShore.BodyA.MaterialMap.2048')),
    ],
'bec9acb0': [
        (log, ('3.0: VivianIrisOfTheShore Hair VB Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'128d277f': [
        (log, ('3.0: VivianIrisOfTheShore Hair VB Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'5b569848': [
        (log, ('3.0: VivianIrisOfTheShore Hair VB Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'b79903af': [(log, ('3.0: VivianIrisOfTheShore Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'9898740f': [
        (log, ('3.0: VivianIrisOfTheShore Hair Shadow VB Hash',)),
        (add_section_if_missing, ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bbb7d4b1': [
        (log, ('3.0: VivianIrisOfTheShore Hair Shadow VB Hash',)),
        (add_section_if_missing, ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'fa9735df': [
        (log, ('3.0: VivianIrisOfTheShore Hair Shadow VB Hash',)),
        (add_section_if_missing, ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'1853b047': [
        (log, ('3.0: VivianIrisOfTheShore Hair Shadow VB Hash',)),
        (add_section_if_missing, ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd96480bc': [
        (log, ('3.0: VivianIrisOfTheShore Body VB Hash',)),
        (add_section_if_missing, ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
    ],
'5e46216b': [
        (log, ('3.0: VivianIrisOfTheShore Body VB Hash',)),
        (add_section_if_missing, ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
    ],
'fb44f88a': [
        (log, ('3.0: VivianIrisOfTheShore Body VB Hash',)),
        (add_section_if_missing, ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
    ],
'f32eec8a': [(log, ('2.3 -> 2.4: VivianSkin Body Blend Hash',)), (update_hash, ('723bccec',))],
'723bccec': [
        (log, ('3.0: VivianIrisOfTheShore Body VB Hash',)),
        (add_section_if_missing, ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
    ],
'9829025f': [
        (log, ('3.0: VivianIrisOfTheShore Gem VB Hash',)),
        (add_section_if_missing, ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
    ],
'3c88ea03': [
        (log, ('3.0: VivianIrisOfTheShore Gem VB Hash',)),
        (add_section_if_missing, ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
    ],
'a55d2f46': [
        (log, ('3.0: VivianIrisOfTheShore Gem VB Hash',)),
        (add_section_if_missing, ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
    ],
'53a21868': [
        (log, ('3.0: VivianIrisOfTheShore Gem VB Hash',)),
        (add_section_if_missing, ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
    ],
'c6e5dc87': [
        (log, ('3.0: VivianIrisOfTheShore Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
    ],
'0afe5a44': [
        (log, ('3.0: VivianIrisOfTheShore Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
    ],
'ef07b6f6': [
        (log, ('3.0: VivianIrisOfTheShore Face VB Hash',)),
        (add_section_if_missing, ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
    ],
'4adf1f7a': [(log, ('3.0: VivianIrisOfTheShore weapon IB Hash',)), (add_ib_check_if_missing,)],
'117996c2': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'fa34947b': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'ee28f6c2': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'1dbeec1f': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'7270dab3': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'6ecc2389': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'15c97ffc': [(log, ('3.0: VivianIrisOfTheShore weapon IB Hash',)), (add_ib_check_if_missing,)],
'd4bb64cc': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('15c97ffc', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'bd66871a': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('15c97ffc', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'431b0b24': [
        (log, ('3.0: VivianIrisOfTheShore weapon VB Hash',)),
        (add_section_if_missing, ('15c97ffc', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'7f5aba6c': [(log, ('3.0: VivianIrisOfTheShore misc hash',)),],
'bd5b581e': [(log, ('3.0: VivianIrisOfTheShore misc hash',)),],
'fcf74fc0': [(log, ('3.0: VivianIrisOfTheShore misc hash',)),],
'713a8587': [
        (log, ('3.0: VivianIrisOfTheShore Hair VB Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: VivianIrisOfTheShore Hair TEX Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'2df6f7b5': [
        (log, ('3.0: VivianIrisOfTheShore Hair TEX Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'36b80366': [
        (log, ('3.0: VivianIrisOfTheShore Hair TEX Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'2d5b1412': [
        (log, ('3.0: VivianIrisOfTheShore Hair TEX Hash',)),
        (add_section_if_missing, ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
    ],
'66b5da8e': [
        (log, ('3.0: VivianIrisOfTheShore Face TEX Hash',)),
        (add_section_if_missing, ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
    ],
'756ebf6b': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'd96fe324': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
'6af50aef': [
        (log, ('3.0: VivianIrisOfTheShore weapon TEX Hash',)),
        (add_section_if_missing, ('4adf1f7a', 'VivianIrisOfTheShore.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VivianIrisOfTheShore',
    'game_versions': ['2.5'],
}

