"""
Soukaku Character Hash Commands
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
    Returns Soukaku's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'fe70c7a3': [(log, ('1.0 - 2.5: Soukaku Hair IB Hash',)), (add_ib_check_if_missing,)],
'ced49ff8': [(log, ('1.0 - 2.5: Soukaku Body IB Hash',)), (add_ib_check_if_missing,)],
'1315178e': [(log, ('1.1 - 2.5: Soukaku Mask IB Hash',)), (add_ib_check_if_missing,)],
'020f9ac6': [(log, ('1.1 - 2.5: Soukaku Head/Face IB Hash',)), (add_ib_check_if_missing,)],
'01f7369e': [(log, ('1.0 - 1.1: Soukaku Head IB Hash',)), (update_hash, ('020f9ac6',))],
'2ceacde6': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA Diffuse 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('427b39a4', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'c20a8c82': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('17110d01', 'Soukaku.HeadA.Diffuse.2048')),
    ],
'427b39a4': [
        (log,                           ('1.0 - 2.5: Soukaku HeadA/FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2ceacde6', 'Soukaku.HeadA.Diffuse.1024')),
    ],
'17110d01': [
        (log,                           ('1.0 - 1.7: Soukaku HeadA LightMap 2048p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        (('020f9ac6', '01f7369e'), 'Soukaku.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c20a8c82', 'Soukaku.HeadA.Diffuse.1024')),
    ],
'32ea0d00': [
        (log,                           ('1.0 - 2.5: Soukaku HairA/MaskA Diffuse 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('34a3ff5b', 'Soukaku.HairA.Diffuse.1024')),
    ],
'34a3ff5b': [
        (log,                           ('1.0: Soukaku HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('32ea0d00', 'Soukaku.HairA.Diffuse.2048')),
    ],
'04654e94': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 2048p Hash',)), (update_hash, ('a70e24a2',))],
'7bbb3d02': [(log, ('1.0 - 1.7: Soukaku HairA LightMap 1024p Hash (deprecated)',))],
'a70e24a2': [
        (log,                           ('2.5: Soukaku HairA/MaskA LightMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('5966c5e3', '7bbb3d02'), 'Soukaku.HairA.LightMap.1024')),
    ],

'5966c5e3': [
        (log,                           ('2.5: Soukaku HairA/MaskA LightMap 1024p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('a70e24a2', '04654e94'), 'Soukaku.HairA.LightMap.2048')),
    ],
'd1444c52': [
        (log,                           ('1.0 - 2.5: Soukaku HairA/MaskA MaterialMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('218689cf', 'Soukaku.HairA.MaterialMap.1024')),
    ],
'218689cf': [
        (log,                           ('1.0: Soukaku HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1444c52', 'Soukaku.HairA.MaterialMap.2048')),
    ],
'8498ee4d': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'0003126a': [(log, ('1.0 - 1.7: Soukaku HairA NormalMap 1024p Hash (deprecated)',))],
'ebac056e': [
        (log,                           ('2.5: Soukaku HairA/BodyA NormalMap 2048p Hash (shared)',)),
        (add_section_if_missing,        ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'ee31954b': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6f5d31fc', 'Soukaku.BodyA.Diffuse.1024')),
    ],
'6f5d31fc': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA Diffuse 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ee31954b', 'Soukaku.BodyA.Diffuse.2048')),
    ],
'112a36a4': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c0f0bb74', 'Soukaku.BodyA.LightMap.1024')),
    ],
'c0f0bb74': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA LightMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('112a36a4', 'Soukaku.BodyA.LightMap.2048')),
    ],
'd638ddf9': [
        (log,                           ('1.0 - 2.5: Soukaku BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ec28297', 'Soukaku.BodyA.MaterialMap.1024')),
    ],
'1ec28297': [
        (log,                           ('1.0 - 1.7: Soukaku BodyA MaterialMap 1024p Hash (deprecated in 2.5)',)),
        (add_section_if_missing,        ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d638ddf9', 'Soukaku.BodyA.MaterialMap.2048')),
    ],
'363e3d70': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'77c48d32': [(log, ('1.0 - 1.7: Soukaku BodyA NormalMap 1024p Hash (deprecated)',))],
'5432bbb8': [
        (log, ('3.0: Soukaku Hair VB Hash',)),
        (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
    ],
'beac45e4': [
        (log, ('3.0: Soukaku Hair VB Hash',)),
        (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
    ],
'43fb429d': [
        (log, ('3.0: Soukaku Hair VB Hash',)),
        (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
    ],
'f65883f3': [
        (log, ('3.0: Soukaku Hair VB Hash',)),
        (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
    ],
'c0ef468f': [(log, ('3.0: Soukaku Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'4ece0220': [
        (log, ('3.0: Soukaku Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bbcd9e5a': [
        (log, ('3.0: Soukaku Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9ab82a7f': [
        (log, ('3.0: Soukaku Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd586de2b': [
        (log, ('3.0: Soukaku Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ff00994d': [
        (log, ('3.0: Soukaku Body VB Hash',)),
        (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'a426e353': [
        (log, ('3.0: Soukaku Body VB Hash',)),
        (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'176fb4d5': [
        (log, ('3.0: Soukaku Body VB Hash',)),
        (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'dbbbafef': [
        (log, ('3.0: Soukaku Body VB Hash',)),
        (add_section_if_missing, ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
    ],
'ddd3fb88': [
        (log, ('3.0: Soukaku Mask VB Hash',)),
        (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'3a6a6326': [
        (log, ('3.0: Soukaku Mask VB Hash',)),
        (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'e261ddc0': [
        (log, ('3.0: Soukaku Mask VB Hash',)),
        (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'5c5d1e7c': [
        (log, ('3.0: Soukaku Mask VB Hash',)),
        (add_section_if_missing, ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
    ],
'ea7c06ba': [
        (log, ('3.0: Soukaku Face VB Hash',)),
        (add_section_if_missing, ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
    ],
'ad41e2f6': [(log, ('1.0 - 1.1: Soukaku Head Texcoord Hash',)), (update_hash, ('c2db08f0',))],
'c2db08f0': [
        (log, ('3.0: Soukaku Face VB Hash',)),
        (add_section_if_missing, ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
    ],
'2d187d8f': [
        (log, ('3.0: Soukaku Face VB Hash',)),
        (add_section_if_missing, ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
    ],
'931476f6': [(log, ('3.0: Soukaku weapon IB Hash',)), (add_ib_check_if_missing,)],
'6b63687a': [
        (log, ('3.0: Soukaku weapon VB Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'c18afef0': [
        (log, ('3.0: Soukaku weapon VB Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'6bf775f7': [
        (log, ('3.0: Soukaku weapon VB Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'67177563': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'7c4efb96': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'd0796da7': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'66f9d07c': [(log, ('3.0: Soukaku misc hash',)),],
'd06e95fd': [(log, ('3.0: Soukaku misc hash',)),],
'798adba3': [
        (log, ('3.0: Soukaku Hair TEX Hash',)),
        (add_section_if_missing, ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
    ],
'd148b6b9': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'a9ddf03d': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
'39d92e17': [
        (log, ('3.0: Soukaku weapon TEX Hash',)),
        (add_section_if_missing, ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soukaku',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

