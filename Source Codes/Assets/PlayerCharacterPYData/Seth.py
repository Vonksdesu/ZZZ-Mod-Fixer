"""
Seth Character Hash Commands
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
    Returns Seth's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'35cf83ad': [(log, ('1.1: Seth Hair IB Hash',)), (add_ib_check_if_missing,)],
'00172ec3': [(log, ('1.1: Seth Body IB Hash',)), (add_ib_check_if_missing,)],
'52f5aa74': [(log, ('1.1: Seth Head IB Hash',)), (add_ib_check_if_missing,)],
'a72f760f': [
        (log,            ('1.3 -> 1.4: Seth Hair Texcoord Hash',)),
        (update_hash,    ('a91eeef2',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '14_Seth_Hair',
            ('4f','2e','2f','2e'),
            ('4B','2e','2f','2e')
        )),
    ],
'fe5b7534': [
        (log,                           ('1.1: Seth HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('09981aff', 'Seth.HeadA.Diffuse.2048')),
    ],
'09981aff': [
        (log,                           ('1.1: Seth HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('52f5aa74', 'Seth.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fe5b7534', 'Seth.HeadA.Diffuse.1024')),
    ],
'dc8e244d': [
        (log,                           ('1.1: Seth HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d3756c37', 'Seth.HairA.Diffuse.1024')),
    ],
'd3756c37': [
        (log,                           ('1.1: Seth HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dc8e244d', 'Seth.HairA.Diffuse.2048')),
    ],
'd4de9ec1': [
        (log,                           ('1.1 -> 2.5: Seth HairA LightMap 2048p Hash',)),
        (update_hash,                   ('a855884d',)),
    ],
'c01dbf6c': [
        (log,                           ('1.1 -> 2.5: Seth HairA LightMap 1024p Hash',)),
        (update_hash,                   ('a855884d',)),
    ],
'3c256565': [
        (log,                           ('1.1: Seth HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('833e9405', 'Seth.HairA.MaterialMap.1024')),
    ],
'833e9405': [
        (log,                           ('1.1: Seth HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3c256565', 'Seth.HairA.MaterialMap.2048')),
    ],
'3376b58c': [
        (log,                           ('1.1 -> 2.5: Seth HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'24d52dd8': [
        (log,                           ('1.1 -> 2.5: Seth HairA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'7f8416ab': [
        (log,                           ('1.1: Seth BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dbc90150', 'Seth.BodyA.Diffuse.1024')),
    ],
'dbc90150': [
        (log,                           ('1.1: Seth BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7f8416ab', 'Seth.BodyA.Diffuse.2048')),
    ],
'3d97c2ef': [
        (log,                           ('1.1 -> 2.5: Seth BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('5b205468',)),
    ],
'9436aa83': [
        (log,                           ('1.1 -> 2.5: Seth BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('5b205468',)),
    ],
'732d3f81': [
        (log,                           ('1.1: Seth BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('56775fcb', 'Seth.BodyA.MaterialMap.1024')),
    ],
'56775fcb': [
        (log,                           ('1.1: Seth BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('732d3f81', 'Seth.BodyA.MaterialMap.2048')),
    ],
'dde45d3d': [
        (log,                           ('1.1 -> 2.5: Seth BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'62b047c5': [
        (log,                           ('1.1 -> 2.5: Seth BodyA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Seth Shared NormalMap Hash (Hair & Body)',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'a855884d': [
        (log,                           ('2.5: Seth HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('ca070fa7', 'c01dbf6c'), 'Seth.HairA.LightMap.1024')),
    ],

'ca070fa7': [
        (log,                           ('2.5: Seth HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('a855884d', 'd4de9ec1'), 'Seth.HairA.LightMap.2048')),
    ],
'5b205468': [
        (log,                           ('2.5: Seth BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('57cf813c', '9436aa83'), 'Seth.BodyA.LightMap.1024')),
    ],

'57cf813c': [
        (log,                           ('2.5: Seth BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('5b205468', '3d97c2ef'), 'Seth.BodyA.LightMap.2048')),
    ],
'9b358a6b': [
        (log, ('3.0: Seth Hair VB Hash',)),
        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'a91eeef2': [
        (log, ('3.0: Seth Hair VB Hash',)),
        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'df779976': [
        (log, ('3.0: Seth Hair VB Hash',)),
        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'52930334': [(log, ('3.0: Seth Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'2719bad1': [
        (log, ('3.0: Seth Hair Shadow VB Hash',)),
        (add_section_if_missing, ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ab8a95a3': [
        (log, ('3.0: Seth Hair Shadow VB Hash',)),
        (add_section_if_missing, ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ca884fde': [
        (log, ('3.0: Seth Hair Shadow VB Hash',)),
        (add_section_if_missing, ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'85cb63a9': [
        (log, ('3.0: Seth Hair Shadow VB Hash',)),
        (add_section_if_missing, ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'2e990d11': [
        (log, ('3.0: Seth Body VB Hash',)),
        (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'c5e25439': [
        (log, ('3.0: Seth Body VB Hash',)),
        (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'd4837e60': [
        (log, ('3.0: Seth Body VB Hash',)),
        (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'b758d72f': [
        (log, ('3.0: Seth Body VB Hash',)),
        (add_section_if_missing, ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
    ],
'016a909a': [
        (log, ('3.0: Seth Face VB Hash',)),
        (add_section_if_missing, ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
    ],
'bff3e0b3': [
        (log, ('3.0: Seth Face VB Hash',)),
        (add_section_if_missing, ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
    ],
'b3f6842f': [
        (log, ('3.1: Seth Face VB Hash',)),
        (add_section_if_missing, ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
    ],
'9dad4eb7': [
        (log, ('3.0: Seth Face VB Hash',)),
        (add_section_if_missing, ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
    ],
'd15922eb': [(log, ('3.0: Seth weapon IB Hash',)), (add_ib_check_if_missing,)],
'c17c87ba': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'bb5022ce': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'08a86fef': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'c5f5e59c': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'47016fd0': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'4e10eb19': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'713b2a30': [(log, ('3.0: Seth weapon IB Hash',)), (add_ib_check_if_missing,)],
'2c38f2c4': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('713b2a30', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'0acdbd8c': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('713b2a30', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'd537bc36': [
        (log, ('3.0: Seth weapon VB Hash',)),
        (add_section_if_missing, ('713b2a30', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'3b7803dd': [(log, ('3.0: Seth misc hash',)),],
'4b92cd34': [(log, ('3.0: Seth misc hash',)),],
'eeea5739': [(log, ('3.0: Seth misc hash',)),],
'd18b1600': [
        (log, ('3.0: Seth Hair VB Hash',)),
        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Seth Hair TEX Hash',)),
        (add_section_if_missing, ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
    ],
'c6131117': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'2f2525f7': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
'36d4290d': [
        (log, ('3.0: Seth weapon TEX Hash',)),
        (add_section_if_missing, ('d15922eb', 'Seth.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seth',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
