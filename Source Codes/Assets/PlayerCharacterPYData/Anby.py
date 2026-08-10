"""
Anby Character Hash Commands
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
    Returns Anby's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'5c0240db': [(log, ('1.0: Anby Hair IB Hash',)), (add_ib_check_if_missing,)],
'4816de84': [(log, ('1.0: Anby Body IB Hash',)), (add_ib_check_if_missing,)],
'19df8e84': [(log, ('1.0: Anby Head IB Hash',)), (add_ib_check_if_missing,)],
'39538886': [
        (log, ('1.1 -> 1.2: Anby Hair Texcoord Hash',)),
        (update_hash, ('496a781d',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'cc114f4f': [(log, ('1.5 -> 1.6: Anby HeadA Diffuse 1024p Hash',)), (update_hash, ('692c6d2b',))],
'692c6d2b': [
        (log,                           ('1.6: Anby HeadA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   (('05d7b504', '2a29cb9b'), 'Anby.HeadA.Diffuse.2048')),
    ],
'2a29cb9b': [(log, ('1.5 -> 1.6: Anby HeadA Diffuse 2048p Hash',)), (update_hash, ('05d7b504',))],
'2a23f612': [(log, ('1.5 -> 1.6: Anby HeadA Diffuse 2048p Hash',)), (update_hash, ('05d7b504',))],
'05d7b504': [
        (log,                           ('1.6: Anby HeadA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   (('692c6d2b', 'cc114f4f'), 'Anby.HeadA.Diffuse.1024')),
    ],
'6ea0023c': [
        (log,                           ('1.0: Anby HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7c7f96d2', 'Anby.HairA.Diffuse.1024')),
    ],
'7c7f96d2': [
        (log,                           ('1.0: Anby HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6ea0023c', 'Anby.HairA.Diffuse.2048')),
    ],
'b54f2a3d': [(log, ('1.0 -> 2.5: Anby HairA LightMap 2048p Hash',)), (update_hash, ('057f3c55',))],
'9ceea795': [(log, ('1.0 -> 2.5: Anby HairA LightMap 1024p Hash',)), (update_hash, ('057f3c55',))],
'057f3c55': [
        (log,                           ('2.5: Anby HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('476ab69c', '9ceea795'), 'Anby.HairA.LightMap.1024')),
    ],

'476ab69c': [
        (log,                           ('2.5: Anby HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('057f3c55', 'b54f2a3d'), 'Anby.HairA.LightMap.2048')),
    ],
'20890a00': [(log, ('1.0 -> 2.5: Anby HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'3101f0da': [(log, ('1.0 -> 2.5: Anby HairA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'ebac056e': [
        (log,                           ('2.5: Anby HairA & BodyA NormalMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'790278b4': [
        (log,                           ('2.5: Anby HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'b37c3b4e': [(log, ('1.5 -> 1.6: Anby BodyA Diffuse 2048p Hash',)), (update_hash, ('215ff74d',))],
'215ff74d': [
        (log,                           ('1.6: Anby BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8df45cb8', '8bd7966f'), 'Anby.BodyA.Diffuse.1024')),
    ],
'8bd7966f': [(log, ('1.5 -> 1.6: Anby BodyA Diffuse 1024p Hash',)), (update_hash, ('8df45cb8',))],
'8df45cb8': [
        (log,                           ('1.6: Anby BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('215ff74d', 'b37c3b4e'), 'Anby.BodyA.Diffuse.2048')),
    ],
'7c24acc9': [(log, ('1.0 -> 2.5: Anby BodyA LightMap 2048p Hash',)), (update_hash, ('59b123c2',))],
'9cddbf1e': [(log, ('1.0 -> 2.5: Anby BodyA LightMap 1024p Hash',)), (update_hash, ('59b123c2',))],
'59b123c2': [
        (log,                           ('2.5: Anby BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('9b57e140', '9cddbf1e'), 'Anby.BodyA.LightMap.1024')),
    ],

'9b57e140': [
        (log,                           ('2.5: Anby BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('59b123c2', '7c24acc9'), 'Anby.BodyA.LightMap.2048')),
    ],
'ccca3b8e': [
        (log,                           ('1.0: Anby BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1115f163', 'Anby.BodyA.MaterialMap.1024')),
    ],
'1115f163': [
        (log,                           ('1.0: Anby BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ccca3b8e', 'Anby.BodyA.MaterialMap.2048')),
    ],
'19226ead': [(log, ('1.0 -> 2.5: Anby BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',))],
'6346d69d': [(log, ('1.0 -> 2.5: Anby BodyA NormalMap 1024p Hash',)), (update_hash, ('ebac056e',))],
'91ffb01c': [
        (log, ('3.0: Anby Hair VB Hash',)),
        (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'9af848eb': [
        (log, ('3.0: Anby Hair VB Hash',)),
        (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'496a781d': [
        (log, ('3.0: Anby Hair VB Hash',)),
        (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'313933a0': [
        (log, ('3.0: Anby Hair VB Hash',)),
        (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'6f5e7cdb': [(log, ('3.0: Anby Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'f6ed0e7b': [
        (log, ('3.0: Anby Hair Shadow VB Hash',)),
        (add_section_if_missing, ('6f5e7cdb', 'Anby.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd431dddb': [
        (log, ('3.0: Anby Hair Shadow VB Hash',)),
        (add_section_if_missing, ('6f5e7cdb', 'Anby.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b62ac7fe': [
        (log, ('3.0: Anby Hair Shadow VB Hash',)),
        (add_section_if_missing, ('6f5e7cdb', 'Anby.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'64fc015c': [
        (log, ('3.0: Anby Hair Shadow VB Hash',)),
        (add_section_if_missing, ('6f5e7cdb', 'Anby.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'45b2509c': [
        (log, ('3.0: Anby Body VB Hash',)),
        (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'1c9533eb': [
        (log, ('3.0: Anby Body VB Hash',)),
        (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'a33e8b5e': [
        (log, ('3.0: Anby Body VB Hash',)),
        (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'137cbdbe': [
        (log, ('3.0: Anby Body VB Hash',)),
        (add_section_if_missing, ('4816de84', 'Anby.Body.IB', 'match_priority = 0\n')),
    ],
'ba016a6e': [(log, ('1.7 -> 2.0: Anby Head Texcoord Hash',)),    (update_hash, ('f818271a',)),],
'f818271a': [
        (log, ('3.0: Anby Face VB Hash',)),
        (add_section_if_missing, ('19df8e84', 'Anby.Face.IB', 'match_priority = 0\n')),
    ],
'9680d55d': [
        (log, ('3.0: Anby Face VB Hash',)),
        (add_section_if_missing, ('19df8e84', 'Anby.Face.IB', 'match_priority = 0\n')),
    ],
'92209737': [(log, ('3.0: Anby weapon IB Hash',)), (add_ib_check_if_missing,)],
'332be630': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'cec4d67b': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'dd507f00': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'd487eaac': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'3de2dae5': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'62f1b72e': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'5bb510c6': [(log, ('3.0: Anby weapon IB Hash',)), (add_ib_check_if_missing,)],
'47da5929': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('5bb510c6', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'58ec8ffb': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('5bb510c6', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'0385188d': [
        (log, ('3.0: Anby weapon VB Hash',)),
        (add_section_if_missing, ('5bb510c6', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'1500b06e': [(log, ('3.0: Anby misc hash',)),],
'9f6aa443': [(log, ('3.0: Anby misc hash',)),],
'baf7ad46': [(log, ('3.0: Anby misc hash',)),],
'798adba3': [
        (log, ('3.0: Anby Hair TEX Hash',)),
        (add_section_if_missing, ('5c0240db', 'Anby.Hair.IB', 'match_priority = 0\n')),
    ],
'85d97523': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'a5e8de50': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
'd4ddc318': [
        (log, ('3.0: Anby weapon TEX Hash',)),
        (add_section_if_missing, ('92209737', 'Anby.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Anby',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

