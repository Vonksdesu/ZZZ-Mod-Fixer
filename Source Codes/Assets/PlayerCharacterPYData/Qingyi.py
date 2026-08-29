"""
Qingyi Character Hash Commands
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
    Returns Qingyi's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'f6e96452': [(log, ('1.1: Qingyi Head IB Hash',)), (add_ib_check_if_missing,)],
'3cacba0a': [(log, ('1.1: Qingyi Hair IB Hash',)), (add_ib_check_if_missing,)],
'195857d8': [(log, ('1.1: Qingyi Body IB Hash',)), (add_ib_check_if_missing,)],
'8e8426df': [(log, ('2.5: Qingyi Bottle IB Hash',)), (add_ib_check_if_missing,)],
'd915de65': [
        (log, ('1 -> 1.1: Qingyi Body IB Hash',)),
        (update_hash, ('195857d8',)),
    ],
'0287b8fb': [
        (log, ('1 -> 1.1: Qingyi Body Blend Hash',)),
        (update_hash, ('88a6f633',)),
    ],
'dd421c3a': [
        (log, ('1 -> 1.1: Qingyi Body Position Hash',)),
        (update_hash, ('ac54012f',)),
    ],
'00487185': [
        (log, ('1 -> 1.1: Qingyi Body Texcoord Hash',)),
        (update_hash, ('4cbe7fbe',)),
    ],
'b1f382cd': [
        (log, ('1 -> 1.1: Qingyi Body Draw Hash',)),
        (update_hash, ('7be61bce',)),
    ],
'33f6d1f2': [
        (log, ('2 -> 1.1: Qingyi Hair IB Hash',)),
        (update_hash, ('3cacba0a',)),
    ],
'd196bd5c': [
        (log, ('2 -> 1.1: Qingyi Hair Blend Hash',)),
        (update_hash, ('6e7650bc',)),
    ],
'b6e5374d': [
        (log, ('2 -> 1.1: Qingyi Hair Position Hash',)),
        (update_hash, ('dd08951b',)),
    ],
'dae0117f': [
        (log, ('2 -> 1.1: Qingyi Hair Texcoord Hash',)),
        (update_hash, ('0643440c',)),
    ],
'6a52010a': [
        (log, ('2 -> 1.1: Qingyi Hair Draw Hash',)),
        (update_hash, ('7b43d317',)),
    ],
'0b75cd32': [
        (log,                           ('1.1: Qingyi HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f6e96452', 'Qingyi.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a58b5444', 'Qingyi.HeadA.Diffuse.1024')),
    ],
'a58b5444': [
        (log,                           ('1.1: Qingyi HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f6e96452', 'Qingyi.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0b75cd32', 'Qingyi.HeadA.Diffuse.2048')),
    ],
'0643440c': [
        (log, ('1.1 -> 1.2: Qingyi Hair Texcoord Hash',)),
        (update_hash, ('53a2b66e',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'3212a0ca': [
        (log,                           ('1.1: Qingyi HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a472db9a', 'Qingyi.HairA.Diffuse.1024')),
    ],
'2910fbd0': [
        (log,                           ('1.1 -> 2.5: Qingyi HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Qingyi Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
    ],
'6e3ac847': [
        (log,                           ('1.1: Qingyi HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('683414c1', 'Qingyi.HairA.LightMap.1024')),
    ],
'4a77fd3b': [
        (log,                           ('1.1: Qingyi HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bfefa200', 'Qingyi.HairA.MaterialMap.1024')),
    ],
'a472db9a': [
        (log,                           ('1.1: Qingyi HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3212a0ca', 'Qingyi.HairA.Diffuse.2048')),
    ],
'fc1847a9': [
        (log,                           ('1.1: Qingyi HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2910fbd0', 'Qingyi.HairA.NormalMap.2048')),
    ],
'683414c1': [
        (log,                           ('1.1: Qingyi HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6e3ac847', 'Qingyi.HairA.LightMap.2048')),
    ],
'bfefa200': [
        (log,                           ('1.1: Qingyi HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a77fd3b', 'Qingyi.HairA.MaterialMap.2048')),
    ],
'1fa7e18e': [
        (log,                           ('1.1: Qingyi BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('aa3c1147', 'Qingyi.BodyA.Diffuse.1024')),
    ],
'542c6b04': [
        (log,                           ('1.1 -> 2.5: Qingyi BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'35c2a022': [
        (log,                           ('1.1: Qingyi BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4a484257', 'Qingyi.BodyA.LightMap.1024')),
    ],
'41054bb6': [
        (log,                           ('1.1: Qingyi BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e8426df', 'Qingyi.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4e561ee5', 'Qingyi.BodyA.MaterialMap.1024')),
    ],
'aa3c1147': [
        (log,                           ('1.1: Qingyi BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1fa7e18e', 'Qingyi.BodyA.Diffuse.2048')),
    ],
'4fbf05be': [
        (log,                           ('1.1: Qingyi BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('542c6b04', 'Qingyi.BodyA.NormalMap.2048')),
    ],
'4a484257': [
        (log,                           ('1.1: Qingyi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('35c2a022', 'Qingyi.BodyA.LightMap.2048')),
    ],
'4e561ee5': [
        (log,                           ('1.1: Qingyi BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('41054bb6', 'Qingyi.BodyA.MaterialMap.2048')),
    ],
'7b43d317': [
        (log, ('3.0: Qingyi Hair VB Hash',)),
        (add_section_if_missing, ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
    ],
'dd08951b': [
        (log, ('3.0: Qingyi Hair VB Hash',)),
        (add_section_if_missing, ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
    ],
'53a2b66e': [
        (log, ('3.0: Qingyi Hair VB Hash',)),
        (add_section_if_missing, ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
    ],
'6e7650bc': [
        (log, ('3.0: Qingyi Hair VB Hash',)),
        (add_section_if_missing, ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
    ],
'0a94bfd8': [(log, ('3.0: Qingyi Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'472bb581': [
        (log, ('3.0: Qingyi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'0971a397': [
        (log, ('3.0: Qingyi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ee99ded9': [
        (log, ('3.0: Qingyi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b7ce94d8': [
        (log, ('3.0: Qingyi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'7be61bce': [
        (log, ('3.0: Qingyi Body VB Hash',)),
        (add_section_if_missing, ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
    ],
'ac54012f': [
        (log, ('3.0: Qingyi Body VB Hash',)),
        (add_section_if_missing, ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
    ],
'4cbe7fbe': [
        (log, ('3.0: Qingyi Body VB Hash',)),
        (add_section_if_missing, ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
    ],
'88a6f633': [
        (log, ('3.0: Qingyi Body VB Hash',)),
        (add_section_if_missing, ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
    ],
'fca2b042': [
        (log, ('3.0: Qingyi kettle VB Hash',)),
        (add_section_if_missing, ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
    ],
'24282218': [
        (log, ('3.0: Qingyi kettle VB Hash',)),
        (add_section_if_missing, ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
    ],
'1707933f': [
        (log, ('3.0: Qingyi kettle VB Hash',)),
        (add_section_if_missing, ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
    ],
'807eb474': [
        (log, ('3.0: Qingyi kettle VB Hash',)),
        (add_section_if_missing, ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
    ],
'6a492df0': [
        (log, ('3.0: Qingyi Face VB Hash',)),
        (add_section_if_missing, ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('db1f2dfa',)),
    ],
'db1f2dfa': [
        (log, ('3.1: Qingyi Face VB Hash',)),
        (add_section_if_missing, ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
    ],
'57c9f0a3': [
        (log, ('3.0: Qingyi Face VB Hash',)),
        (add_section_if_missing, ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
    ],
'6b62986f': [(log, ('3.0: Qingyi weapon IB Hash',)), (add_ib_check_if_missing,)],
'fb916456': [
        (log, ('3.0: Qingyi weapon VB Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'8658ef62': [
        (log, ('3.0: Qingyi weapon VB Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'f75514db': [
        (log, ('3.0: Qingyi weapon VB Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'330dfe54': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'2d703fde': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'8d6da65b': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'9f6aa443': [(log, ('3.0: Qingyi misc hash',)),],
'e5a4128b': [(log, ('3.0: Qingyi misc hash',)),],
'798adba3': [
        (log, ('3.0: Qingyi Hair TEX Hash',)),
        (add_section_if_missing, ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
    ],
'46406a81': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'22b43462': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'39e8fda1': [
        (log, ('3.0: Qingyi weapon TEX Hash',)),
        (add_section_if_missing, ('6b62986f', 'Qingyi.weapon.IB', 'match_priority = 0\n')),
    ],
'a5783704': [
        (log, ('3.0: Qingyi Face VB Hash',)),
        (add_section_if_missing, ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Qingyi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
