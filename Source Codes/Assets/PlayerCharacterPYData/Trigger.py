"""
Trigger Character Hash Commands
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
    Returns Trigger's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'8e98ef9a': [(log, ('1.6: Trigger Hair IB Hash',)), (add_ib_check_if_missing,)],
'7f32eeae': [(log, ('1.6: Trigger Body IB Hash',)), (add_ib_check_if_missing,)],
'40cd4182': [(log, ('1.6: Trigger Face IB Hash',)), (add_ib_check_if_missing,)],
'88728785': [
        (log,                           ('1.6: Trigger FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cffc4b09', 'Trigger.FaceA.Diffuse.1024')),
    ],
'cffc4b09': [
        (log,                           ('1.6: Trigger FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('88728785', 'Trigger.FaceA.Diffuse.2048')),
    ],
'e826a564': [
        (log,                           ('1.6: Trigger HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('984e7896', 'Trigger.HairA.Diffuse.1024')),
    ],
'984e7896': [
        (log,                           ('1.6: Trigger HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e826a564', 'Trigger.HairA.Diffuse.2048')),
    ],
'23f2a4cf': [
        (log,                           ('1.6: Trigger HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c321345c', 'Trigger.HairA.LightMap.1024')),
    ],
'c321345c': [
        (log,                           ('1.6: Trigger HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('23f2a4cf', 'Trigger.HairA.LightMap.2048')),
    ],
'b24f1752': [
        (log,                           ('1.6: Trigger HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4ee3c3fe', 'Trigger.HairA.MaterialMap.1024')),
    ],
'4ee3c3fe': [
        (log,                           ('1.6: Trigger HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b24f1752', 'Trigger.HairA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('1.6: Trigger Shared NormalMap Hash (Hair & Body)',)),
        (add_section_if_missing,        ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],
'6631eadc': [
        (log,                           ('1.6: Trigger BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8cffa733', 'Trigger.BodyA.Diffuse.1024')),
    ],
'8cffa733': [
        (log,                           ('1.6: Trigger BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6631eadc', 'Trigger.BodyA.Diffuse.2048')),
    ],
'05250215': [
        (log,                           ('1.6: Trigger BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2c72b961', 'Trigger.BodyA.LightMap.1024')),
    ],
'2c72b961': [
        (log,                           ('1.6: Trigger BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('05250215', 'Trigger.BodyA.LightMap.2048')),
    ],
'985c5f52': [
        (log,                           ('1.6: Trigger BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cd507047', 'Trigger.BodyA.MaterialMap.1024')),
    ],
'cd507047': [
        (log,                           ('1.6: Trigger BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('985c5f52', 'Trigger.BodyA.MaterialMap.2048')),
    ],
'b0625293': [
        (log, ('3.0: Trigger Hair VB Hash',)),
        (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
    ],
'f066913d': [
        (log, ('3.0: Trigger Hair VB Hash',)),
        (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
    ],
'b12abbeb': [
        (log, ('3.0: Trigger Hair VB Hash',)),
        (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
    ],
'acd25c98': [
        (log, ('3.0: Trigger Hair VB Hash',)),
        (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
    ],
'69c27d44': [(log, ('3.0: Trigger Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'5fdaccd2': [
        (log, ('3.0: Trigger Body VB Hash',)),
        (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],
'e4ae41fd': [
        (log, ('3.0: Trigger Body VB Hash',)),
        (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],
'b3c0a13c': [
        (log, ('3.0: Trigger Body VB Hash',)),
        (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],
'e31a3b5f': [
        (log, ('3.0: Trigger Body VB Hash',)),
        (add_section_if_missing, ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
    ],
'f05e3a4a': [(log, ('3.0: Trigger weapon IB Hash',)), (add_ib_check_if_missing,)],
'19515c67': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'2236b80e': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'a6d2b50e': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'bb079ba3': [(log, ('3.0: Trigger weapon IB Hash',)), (add_ib_check_if_missing,)],
'f61f6acd': [(log, ('3.0: Trigger weapon IB Hash',)), (add_ib_check_if_missing,)],
'dfc69ad0': [
        (log, ('3.0: Trigger Face VB Hash',)),
        (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
    ],
'b9f0d595': [(log, ('2.2 -> 2.3: Trigger Face Texcoord',)), (update_hash, ('d4a12ab7',))],
'd4a12ab7': [
        (log, ('3.0: Trigger Face VB Hash',)),
        (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
    ],
'1a9a858c': [
        (log, ('3.0: Trigger Face VB Hash',)),
        (add_section_if_missing, ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
    ],
'60fcff00': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'ca8565b9': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'73555896': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('bb079ba3', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'7ab2b542': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('bb079ba3', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'89c48e15': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('f61f6acd', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'0cdfa94a': [(log, ('3.0: Trigger misc hash',)),],
'773c85f4': [(log, ('3.0: Trigger misc hash',)),],
'8057c562': [(log, ('3.0: Trigger misc hash',)),],
'fa2ee314': [(log, ('3.0: Trigger misc hash',)),],
'798adba3': [
        (log, ('3.0: Trigger Hair TEX Hash',)),
        (add_section_if_missing, ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
    ],
'748df67a': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'c7377a02': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'799820a8': [
        (log, ('3.0: Trigger weapon TEX Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'570ffcdc': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('bb079ba3', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
'ac917a82': [
        (log, ('3.0: Trigger weapon VB Hash',)),
        (add_section_if_missing, ('f05e3a4a', 'Trigger.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Trigger',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

