"""
Miyabi Character Hash Commands
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
    Returns Miyabi's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'4faabaac': [(log, ('1.4: Miyabi Hair IB Hash',)),   (add_ib_check_if_missing,)],
'981c1a1e': [(log, ('1.4: Miyabi Body IB Hash',)),   (add_ib_check_if_missing,)],
'd8003df3': [(log, ('1.4: Miyabi Legs IB Hash',)),   (add_ib_check_if_missing,)],
'dbd59d30': [(log, ('1.4: Miyabi Face IB Hash',)),   (add_ib_check_if_missing,)],
'1d487fd5': [
        (log,                           ('1.4: Miyabi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('92599e94', 'Miyabi.FaceA.Diffuse.1024')),
    ],
'92599e94': [
        (log,                           ('1.4: Miyabi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1d487fd5', 'Miyabi.FaceA.Diffuse.2048')),
    ],
'012e84e9': [
        (log,                           ('1.4: Miyabi HairA, LegsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('ed6b94f7', 'Miyabi.HairA.Diffuse.1024')),
    ],
'a6ea6d83': [
        (log,                           ('1.4: Miyabi HairA, LegsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8b5708f4', 'Miyabi.HairA.LightMap.1024')),
    ],
'd5462e37': [
        (log,                           ('1.4: Miyabi HairA, LegsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a84d9003', 'Miyabi.HairA.MaterialMap.1024')),
    ],
'ed6b94f7': [
        (log,                           ('1.4: Miyabi HairA, LegsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('012e84e9', 'Miyabi.HairA.Diffuse.2048')),
    ],
'8b5708f4': [
        (log,                           ('1.4: Miyabi HairA, LegsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('a6ea6d83', 'Miyabi.HairA.LightMap.2048')),
    ],
'a84d9003': [
        (log,                           ('1.4: Miyabi HairA, LegsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d5462e37', 'Miyabi.HairA.MaterialMap.2048')),
    ],
'09a2bbd1': [
        (log,                           ('1.4: Miyabi BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('1a3644e7', 'Miyabi.BodyA.Diffuse.1024')),
    ],
'fd289380': [
        (log,                           ('1.4: Miyabi BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('0492f64a', 'Miyabi.BodyA.LightMap.1024')),
    ],
'450770fd': [
        (log,                           ('1.4: Miyabi BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('168b1df9', 'Miyabi.BodyA.MaterialMap.1024')),
    ],
'1a3644e7': [
        (log,                           ('1.4: Miyabi BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('09a2bbd1', 'Miyabi.BodyA.Diffuse.2048')),
    ],
'0492f64a': [
        (log,                           ('1.4: Miyabi BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('fd289380', 'Miyabi.BodyA.LightMap.2048')),
    ],
'168b1df9': [
        (log,                           ('1.4: Miyabi BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('450770fd', 'Miyabi.BodyA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Miyabi HairA, BodyA & LegsA NormalMap Hash',)),
        (add_section_if_missing,        ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ],
'f9b9b064': [
        (log, ('3.0: Miyabi Hair VB Hash',)),
        (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
    ],
'b6530b86': [
        (log, ('3.0: Miyabi Hair VB Hash',)),
        (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
    ],
'8b2eeb77': [
        (log, ('3.0: Miyabi Hair VB Hash',)),
        (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
    ],
'acff032e': [(log, ('3.0: Miyabi Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'e8082f3c': [
        (log, ('3.0: Miyabi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a10b08d2': [
        (log, ('3.0: Miyabi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'70717c93': [
        (log, ('3.0: Miyabi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9c3d5e1f': [
        (log, ('3.0: Miyabi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'02e62d7e': [(log, ('3.0: Miyabi Hairpin IB Hash',)), (add_ib_check_if_missing,)],
'bbce89b9': [
        (log, ('3.0: Miyabi Hairpin VB Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'e7041a99': [
        (log, ('3.0: Miyabi Hairpin VB Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'750d2a46': [
        (log, ('3.0: Miyabi Hairpin VB Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'7ed40a2f': [
        (log, ('3.0: Miyabi Hairpin VB Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'e24bfe0e': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'9e1067e9': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'f4d343b2': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'0c26a38b': [(log, ('3.0: Miyabi Hairpin ribbon IB Hash',)), (add_ib_check_if_missing,)],
'3421e96d': [
        (log, ('3.0: Miyabi Hairpin ribbon VB Hash',)),
        (add_section_if_missing, ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
    ],
'be288799': [
        (log, ('3.0: Miyabi Hairpin ribbon VB Hash',)),
        (add_section_if_missing, ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
    ],
'fcc57f25': [
        (log, ('3.0: Miyabi Hairpin ribbon VB Hash',)),
        (add_section_if_missing, ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
    ],
'827f5947': [
        (log, ('3.0: Miyabi Hairpin ribbon VB Hash',)),
        (add_section_if_missing, ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
    ],
'6201dd9e': [
        (log, ('3.0: Miyabi Body VB Hash',)),
        (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
    ],
'8ecb10b3': [
        (log, ('3.0: Miyabi Body VB Hash',)),
        (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
    ],
'303fb1b6': [
        (log, ('3.0: Miyabi Body VB Hash',)),
        (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
    ],
'9a4227c8': [
        (log, ('3.0: Miyabi Body VB Hash',)),
        (add_section_if_missing, ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
    ],
'8336ded4': [
        (log, ('3.0: Miyabi Legs VB Hash',)),
        (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ],
'e71bbd08': [
        (log, ('3.0: Miyabi Legs VB Hash',)),
        (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ],
'fb94d66c': [
        (log, ('3.0: Miyabi Legs VB Hash',)),
        (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ],
'bc586fd9': [
        (log, ('3.0: Miyabi Legs VB Hash',)),
        (add_section_if_missing, ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
    ],
'37afd6ad': [
        (log, ('3.0: Miyabi Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
    ],
'7a476f86': [
        (log, ('3.0: Miyabi Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
    ],
'd7781c46': [
        (log, ('3.0: Miyabi Face VB Hash',)),
        (add_section_if_missing, ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
    ],
'0275d39f': [(log, ('3.0: Miyabi weapon IB Hash',)), (add_ib_check_if_missing,)],
'81a99d68': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'aeb95d61': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'8bc72b94': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'718d7915': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'b73ed7e7': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'e1603ca5': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'1a82a439': [(log, ('3.0: Miyabi weapon IB Hash',)), (add_ib_check_if_missing,)],
'10545b04': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'51af1803': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'c55927b0': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('1a82a439', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'562b2030': [(log, ('3.0: Miyabi weapon IB Hash',)), (add_ib_check_if_missing,)],
'fc93f762': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('562b2030', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'38c91cb1': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('562b2030', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'a9ac3439': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('562b2030', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'12739125': [(log, ('3.0: Miyabi weapon IB Hash',)), (add_ib_check_if_missing,)],
'e106fdc0': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('12739125', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'd6ea3283': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('12739125', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'51a4604d': [
        (log, ('3.0: Miyabi weapon VB Hash',)),
        (add_section_if_missing, ('12739125', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'0dbd45ea': [(log, ('3.0: Miyabi misc hash',)),],
'5e1e12aa': [(log, ('3.0: Miyabi misc hash',)),],
'79bd2f22': [(log, ('3.0: Miyabi misc hash',)),],
'9d6f441f': [(log, ('3.0: Miyabi misc hash',)),],
'e3590e91': [(log, ('3.0: Miyabi misc hash',)),],
'4e752f58': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'e10040c7': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'3af946eb': [
        (log, ('3.0: Miyabi Hairpin TEX Hash',)),
        (add_section_if_missing, ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
    ],
'ac7673da': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'f33cdee7': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'8931b1ec': [
        (log, ('3.0: Miyabi weapon TEX Hash',)),
        (add_section_if_missing, ('0275d39f', 'Miyabi.weapon.IB', 'match_priority = 0\n')),
    ],
'5a8d28f4': [
        (log, ('3.0: Miyabi Hair VB Hash',)),
        (add_section_if_missing, ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Miyabi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
