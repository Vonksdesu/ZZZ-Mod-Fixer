"""
Rina Character Hash Commands
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
    Returns Rina's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'cdb2cc7d': [(log, ('1.0: Rina Hair IB Hash',)), (add_ib_check_if_missing,)],
'2825da1e': [(log, ('1.0: Rina Body IB Hash',)), (add_ib_check_if_missing,)],
'9f90cfaa': [(log, ('1.0: Rina Head IB Hash',)), (add_ib_check_if_missing,)],
'7ecc44ce': [
        (log,                           ('1.0: Rina HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9f90cfaa', 'Rina.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('802a3281', 'Rina.HeadA.Diffuse.2048')),
    ],
'802a3281': [
        (log,                           ('1.0: Rina HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9f90cfaa', 'Rina.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7ecc44ce', 'Rina.HeadA.Diffuse.1024')),
    ],
'eb5d9d1c': [
        (log,                           ('1.0: Rina HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4b005a79', 'Rina.HairA.Diffuse.1024')),
    ],
'4b005a79': [
        (log,                           ('1.0: Rina HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('eb5d9d1c', 'Rina.HairA.Diffuse.2048')),
    ],
'1145d2b8': [
        (log,                           ('1.0: Rina HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fb61499f', 'Rina.HairA.LightMap.1024')),
    ],
'fb61499f': [
        (log,                           ('1.0: Rina HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1145d2b8', 'Rina.HairA.LightMap.2048')),
    ],
'82153e28': [
        (log,                           ('1.0: Rina HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ea08fd96', 'Rina.HairA.MaterialMap.1024')),
    ],
'ea08fd96': [
        (log,                           ('1.0: Rina HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('82153e28', 'Rina.HairA.MaterialMap.2048')),
    ],
'83ac7993': [
        (log,                           ('1.0 -> 2.5: Rina HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Rina Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'fa3c40e9': [
        (log,                           ('1.0: Rina HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('83ac7993', 'Rina.HairA.NormalMap.2048')),
    ],
'bf44bf67': [
        (log,                           ('1.0: Rina BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a23e2e14', 'Rina.BodyA.Diffuse.1024')),
    ],
'a23e2e14': [
        (log,                           ('1.0: Rina BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf44bf67', 'Rina.BodyA.Diffuse.2048')),
    ],
'95f4e9c8': [
        (log,                           ('1.0: Rina BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('fad76987', 'Rina.BodyA.LightMap.1024')),
    ],
'fad76987': [
        (log,                           ('1.0: Rina BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('95f4e9c8', 'Rina.BodyA.LightMap.2048')),
    ],
'ed47722f': [
        (log,                           ('1.0: Rina BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9fa6dfd3', 'Rina.BodyA.MaterialMap.1024')),
    ],
'9fa6dfd3': [
        (log,                           ('1.0: Rina BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ed47722f', 'Rina.BodyA.MaterialMap.2048')),
    ],
'97637a8f': [
        (log,                           ('1.0 -> 2.5: Rina BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (log,                           ('+ Updated to shared NormalMap hash',)),
    ],
'd6b20159': [
        (log,                           ('1.0: Rina BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('97637a8f', 'Rina.BodyA.NormalMap.2048')),
    ],
'06c78cb0': [
        (log, ('3.0: Rina Hair VB Hash',)),
        (add_section_if_missing, ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
    ],
'0dda44b1': [
        (log, ('3.0: Rina Hair VB Hash',)),
        (add_section_if_missing, ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
    ],
'fef908be': [
        (log, ('3.0: Rina Hair VB Hash',)),
        (add_section_if_missing, ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
    ],
'5116f2cb': [(log, ('3.0: Rina Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'8119483f': [
        (log, ('3.0: Rina Hair Shadow VB Hash',)),
        (add_section_if_missing, ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'112f8365': [
        (log, ('3.0: Rina Hair Shadow VB Hash',)),
        (add_section_if_missing, ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bd58eaab': [
        (log, ('3.0: Rina Hair Shadow VB Hash',)),
        (add_section_if_missing, ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'950dc06c': [
        (log, ('3.0: Rina Hair Shadow VB Hash',)),
        (add_section_if_missing, ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'03e8990d': [
        (log, ('3.0: Rina Body VB Hash',)),
        (add_section_if_missing, ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'41149c54': [
        (log, ('3.0: Rina Body VB Hash',)),
        (add_section_if_missing, ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'4c259bf3': [
        (log, ('3.0: Rina Body VB Hash',)),
        (add_section_if_missing, ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'17471aea': [
        (log, ('3.0: Rina Body VB Hash',)),
        (add_section_if_missing, ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
    ],
'f93611ef': [
        (log, ('3.0: Rina Face VB Hash',)),
        (add_section_if_missing, ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
    ],
'1866cf6a': [
        (log, ('3.0: Rina Face VB Hash',)),
        (add_section_if_missing, ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
    ],
'3124a1db': [
        (log, ('3.0: Rina Face VB Hash',)),
        (add_section_if_missing, ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
    ],
'4f795827': [(log, ('3.0: Rina weapon IB Hash',)), (add_ib_check_if_missing,)],
'e28891a4': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'9be6ba46': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'bc04a8d9': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'7aa85409': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'6aec8cd9': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'6d3db8fe': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'8ebe259d': [(log, ('3.0: Rina weapon IB Hash',)), (add_ib_check_if_missing,)],
'941f67ec': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'34a3b201': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'6fecdfb7': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'5b418f07': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'b8f3b02a': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'1d68e5ac': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'b990fcb9': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'4fba8b69': [(log, ('3.0: Rina weapon IB Hash',)), (add_ib_check_if_missing,)],
'd4492a43': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4fba8b69', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'8bcd9f92': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4fba8b69', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'a59d40f4': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('4fba8b69', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'a6bfc370': [(log, ('3.0: Rina weapon IB Hash',)), (add_ib_check_if_missing,)],
'187daa68': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('a6bfc370', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'a1695dc5': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('a6bfc370', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'cc1203fa': [
        (log, ('3.0: Rina weapon VB Hash',)),
        (add_section_if_missing, ('a6bfc370', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'11d72670': [(log, ('3.0: Rina misc hash',)),],
'16399986': [(log, ('3.0: Rina misc hash',)),],
'7a72d77f': [(log, ('3.0: Rina misc hash',)),],
'c32482a8': [(log, ('3.0: Rina misc hash',)),],
'c9174fa5': [(log, ('3.0: Rina misc hash',)),],
'8ca7dc4b': [
        (log, ('3.0: Rina Hair VB Hash',)),
        (add_section_if_missing, ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Rina Hair TEX Hash',)),
        (add_section_if_missing, ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
    ],
'203a9fa8': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'c99753e0': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'76939bab': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('4f795827', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'9a76e68e': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'e1864c72': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'f3653e23': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
'2f1e005f': [
        (log, ('3.0: Rina weapon TEX Hash',)),
        (add_section_if_missing, ('8ebe259d', 'Rina.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Rina',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
