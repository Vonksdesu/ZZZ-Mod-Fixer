"""
PanYinhu Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json data
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns PanYinhu's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'cb1a6db9': [(log, ('2.5: PanYinhu Body IB Hash',)), (add_ib_check_if_missing,)],
'ff7e9b40': [(log, ('2.5: PanYinhu Hat IB Hash',)), (add_ib_check_if_missing,)],
'ebb6a59b': [(log, ('2.5: PanYinhu Face IB Hash',)), (add_ib_check_if_missing,)],

# Body A & B + Hat B Textures (Shared)
'c0928025': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b20c7e8b', 'PanYinhu.BodyA.Diffuse.1024')),
    ],

'b20c7e8b': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c0928025', 'PanYinhu.BodyA.Diffuse.2048')),
    ],
'7d3c4c3d': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7967c15f', 'PanYinhu.BodyA.LightMap.1024')),
    ],

'7967c15f': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7d3c4c3d', 'PanYinhu.BodyA.LightMap.2048')),
    ],
'42fc25f0': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2daeed33', 'PanYinhu.BodyA.MaterialMap.1024')),
    ],

'2daeed33': [
        (log,                           ('2.5: PanYinhu Body A/B + Hat B MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('42fc25f0', 'PanYinhu.BodyA.MaterialMap.2048')),
    ],

# Body C + Hat A Textures (Shared)
'f2433e17': [
        (log,                           ('2.5: PanYinhu Body C + Hat A Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('cf6afa84', 'PanYinhu.HatA.Diffuse.1024')),
    ],

'cf6afa84': [
        (log,                           ('2.5: PanYinhu Body C + Hat A Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f2433e17', 'PanYinhu.HatA.Diffuse.2048')),
    ],
'ddeaa4c3': [
        (log,                           ('2.5: PanYinhu Body C + Hat A LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('26454e30', 'PanYinhu.HatA.LightMap.1024')),
    ],

'26454e30': [
        (log,                           ('2.5: PanYinhu Body C + Hat A LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ddeaa4c3', 'PanYinhu.HatA.LightMap.2048')),
    ],
'de553410': [
        (log,                           ('2.5: PanYinhu Body C + Hat A MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e0433c18', 'PanYinhu.HatA.MaterialMap.1024')),
    ],

'e0433c18': [
        (log,                           ('2.5: PanYinhu Body C + Hat A MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('de553410', 'PanYinhu.HatA.MaterialMap.2048')),
    ],

# Body D + Face A Textures (Shared)
'ed361b8f': [
        (log,                           ('2.5: PanYinhu Body D + Face A Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('452a0918', 'PanYinhu.FaceA.Diffuse.1024')),
    ],

'452a0918': [
        (log,                           ('2.5: PanYinhu Body D + Face A Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ed361b8f', 'PanYinhu.FaceA.Diffuse.2048')),
    ],
'96280008': [
        (log,                           ('2.5: PanYinhu Body D + Face A LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3744882e', 'PanYinhu.FaceA.LightMap.1024')),
    ],

'3744882e': [
        (log,                           ('2.5: PanYinhu Body D + Face A LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('96280008', 'PanYinhu.FaceA.LightMap.2048')),
    ],
'57446a22': [
        (log,                           ('2.5: PanYinhu Body D + Face A MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('18dd19bf', 'PanYinhu.FaceA.MaterialMap.1024')),
    ],

'18dd19bf': [
        (log,                           ('2.5: PanYinhu Body D + Face A MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('57446a22', 'PanYinhu.FaceA.MaterialMap.2048')),
    ],

# Shared NormalMap (across all components)
'ebac056e': [
        (log,                           ('2.5: PanYinhu Shared NormalMap Hash',)),
        (add_section_if_missing,        ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ff7e9b40', 'PanYinhu.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'aba31d2e': [
        (log, ('3.0: PanYinhu Body VB Hash',)),
        (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
    ],
'cc541390': [
        (log, ('3.0: PanYinhu Body VB Hash',)),
        (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
    ],
'4727992f': [
        (log, ('3.0: PanYinhu Body VB Hash',)),
        (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
    ],
'b3556f6e': [(log, ('3.0: PanYinhu weapon IB Hash',)), (add_ib_check_if_missing,)],
'534c2f9b': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('b3556f6e', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'4864dcdd': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('b3556f6e', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'a6f599e3': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('b3556f6e', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'b88cf297': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('b3556f6e', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'682e8e8d': [
        (log, ('3.0: PanYinhu Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'1eee2121': [
        (log, ('3.0: PanYinhu Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'4aae3329': [
        (log, ('3.0: PanYinhu Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
    ],
'45a8cd1b': [(log, ('3.0: PanYinhu weapon IB Hash',)), (add_ib_check_if_missing,)],
'2a45b03d': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('45a8cd1b', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'e56ae11f': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('45a8cd1b', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'1a769e88': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('45a8cd1b', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'cd763e6d': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('45a8cd1b', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'2e2d67ae': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('ff7e9b40', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'0ee4a87c': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('ff7e9b40', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'd569d88e': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('ff7e9b40', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'd141908c': [
        (log, ('3.0: PanYinhu weapon VB Hash',)),
        (add_section_if_missing, ('ff7e9b40', 'PanYinhu.weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: PanYinhu Body TEX Hash',)),
        (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
    ],
'b375f26b': [
        (log, ('3.0: PanYinhu Body VB Hash',)),
        (add_section_if_missing, ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhu',
    'game_versions': ['2.5'],
    'components': ['Body', 'Hat', 'Face'],
    'variants': {
        'Body': ['A', 'B', 'C', 'D'],
        'Hat': ['A', 'B'],
        'Face': ['A']
    },
}
