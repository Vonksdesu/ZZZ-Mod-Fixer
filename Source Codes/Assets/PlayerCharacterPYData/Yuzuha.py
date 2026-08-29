"""
Yuzuha Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Yuzuha's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'7a504287': [(log, ('2.5: Yuzuha Hair IB Hash',)), (add_ib_check_if_missing,)],
'5144c409': [(log, ('2.5: Yuzuha Body IB Hash',)), (add_ib_check_if_missing,)],
'73757570': [(log, ('2.5: Yuzuha Legs IB Hash',)), (add_ib_check_if_missing,)],
'e72984d1': [(log, ('2.5: Yuzuha Kama IB Hash',)), (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.5: Yuzuha Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'd394bc13': [
        (log,                           ('2.5: Yuzuha FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('59f9e66f', 'Yuzuha.FaceA.Diffuse.1024')),
    ],

'59f9e66f': [
        (log,                           ('2.5: Yuzuha FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d394bc13', 'Yuzuha.FaceA.Diffuse.2048')),
    ],

# Hair Textures (shared between Hair and Legs components)
'521a3242': [
        (log,                           ('2.5: Yuzuha Hair/Legs Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c9115930', 'Yuzuha.HairA.Diffuse.1024')),
    ],

'c9115930': [
        (log,                           ('2.5: Yuzuha Hair/Legs Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('521a3242', 'Yuzuha.HairA.Diffuse.2048')),
    ],
'c400f5b7': [
        (log,                           ('2.5: Yuzuha Hair/Legs LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a9730519', 'Yuzuha.HairA.LightMap.1024')),
    ],

'a9730519': [
        (log,                           ('2.5: Yuzuha Hair/Legs LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c400f5b7', 'Yuzuha.HairA.LightMap.2048')),
    ],
'3f70d124': [
        (log,                           ('2.5: Yuzuha Hair/Legs MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4f5639e2', 'Yuzuha.HairA.MaterialMap.1024')),
    ],

'4f5639e2': [
        (log,                           ('2.5: Yuzuha Hair/Legs MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3f70d124', 'Yuzuha.HairA.MaterialMap.2048')),
    ],

# Body Textures (shared between Body and Kama components)
'be85f061': [
        (log,                           ('2.5: Yuzuha Body/Kama Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1fabf669', 'Yuzuha.BodyA.Diffuse.1024')),
    ],

'1fabf669': [
        (log,                           ('2.5: Yuzuha Body/Kama Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('be85f061', 'Yuzuha.BodyA.Diffuse.2048')),
    ],
'ef192425': [
        (log,                           ('2.5: Yuzuha Body/Kama LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('eff3b0b0', 'Yuzuha.BodyA.LightMap.1024')),
    ],

'eff3b0b0': [
        (log,                           ('2.5: Yuzuha Body/Kama LightMap 1024p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ef192425', 'Yuzuha.BodyA.LightMap.2048')),
    ],
'76e5c6b7': [
        (log,                           ('2.5: Yuzuha Body/Kama MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2fb36ecb', 'Yuzuha.BodyA.MaterialMap.1024')),
    ],

'2fb36ecb': [
        (log,                           ('2.5: Yuzuha Body/Kama MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('76e5c6b7', 'Yuzuha.BodyA.MaterialMap.2048')),
    ],

# Shared NormalMap (used across Hair, Body, Legs, and Kama)
'ebac056e': [
        (log,                           ('2.5: Yuzuha Shared NormalMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e72984d1', 'Yuzuha.Kama.IB', 'match_priority = 0\n')),
    ],
'051f9657': [
        (log, ('3.0: Yuzuha Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
    ],
'dc2821dc': [
        (log, ('3.0: Yuzuha Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
    ],
'606c88ae': [
        (log, ('3.0: Yuzuha Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
    ],
'afb6117a': [(log, ('3.0: Yuzuha Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'8a540628': [
        (log, ('3.0: Yuzuha Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'3a4533fc': [
        (log, ('3.0: Yuzuha Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a39c4806': [
        (log, ('3.0: Yuzuha Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9fc9b6f8': [
        (log, ('3.0: Yuzuha Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'2a99e69b': [
        (log, ('3.0: Yuzuha Body VB Hash',)),
        (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
    ],
'20d44382': [
        (log, ('3.0: Yuzuha Body VB Hash',)),
        (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
    ],
'688588f1': [
        (log, ('3.0: Yuzuha Body VB Hash',)),
        (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
    ],
'0db66603': [
        (log, ('3.0: Yuzuha Body VB Hash',)),
        (add_section_if_missing, ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
    ],
'93b3c078': [
        (log, ('3.0: Yuzuha Legs VB Hash',)),
        (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'bc6a9f6f': [
        (log, ('3.0: Yuzuha Legs VB Hash',)),
        (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'882cf302': [
        (log, ('3.0: Yuzuha Legs VB Hash',)),
        (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'6fe5c40e': [
        (log, ('3.0: Yuzuha Legs VB Hash',)),
        (add_section_if_missing, ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
    ],
'773bdaa3': [
        (log, ('3.0: Yuzuha LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'a5097f50': [
        (log, ('3.0: Yuzuha LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'085ab253': [
        (log, ('3.0: Yuzuha LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'81bca595': [(log, ('3.0: Yuzuha LeopardCat2 IB Hash',)), (add_ib_check_if_missing,)],
'39b6000b': [
        (log, ('3.0: Yuzuha LeopardCat2 VB Hash',)),
        (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
    ],
'9662128e': [
        (log, ('3.0: Yuzuha LeopardCat2 VB Hash',)),
        (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
    ],
'f95d8b57': [
        (log, ('3.0: Yuzuha LeopardCat2 VB Hash',)),
        (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
    ],
'ba80c02b': [
        (log, ('3.0: Yuzuha LeopardCat2 VB Hash',)),
        (add_section_if_missing, ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
    ],
'cf3172e4': [(log, ('3.0: Yuzuha Straps IB Hash',)), (add_ib_check_if_missing,)],
'966e777b': [
        (log, ('3.0: Yuzuha Straps VB Hash',)),
        (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'b543b8d8': [
        (log, ('3.0: Yuzuha Straps VB Hash',)),
        (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'4b13802b': [
        (log, ('3.0: Yuzuha Straps VB Hash',)),
        (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'7ca97675': [
        (log, ('3.0: Yuzuha Straps VB Hash',)),
        (add_section_if_missing, ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
    ],
'0f6a425b': [
        (log, ('3.0: Yuzuha Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],
'9d0f7ef5': [
        (log, ('3.0: Yuzuha Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],
'52400cce': [
        (log, ('3.0: Yuzuha Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
    ],
'2686f517': [(log, ('3.0: Yuzuha weapon IB Hash',)), (add_ib_check_if_missing,)],
'1686ac84': [
        (log, ('3.0: Yuzuha weapon VB Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'8a182e58': [
        (log, ('3.0: Yuzuha weapon VB Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'7d11ecaa': [
        (log, ('3.0: Yuzuha weapon VB Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'7139e5b0': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'9dcd6e8e': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'85142f08': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'1a6468e1': [(log, ('3.0: Yuzuha misc hash',)),],
'3578d11c': [(log, ('3.0: Yuzuha misc hash',)),],
'79c257b3': [(log, ('3.0: Yuzuha misc hash',)),],
'630debc9': [
        (log, ('3.0: Yuzuha Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Yuzuha Hair TEX Hash',)),
        (add_section_if_missing, ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
    ],
'68856c57': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'4fe5c926': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
'd0c14d9d': [
        (log, ('3.0: Yuzuha weapon TEX Hash',)),
        (add_section_if_missing, ('2686f517', 'Yuzuha.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yuzuha',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Legs', 'Kama', 'Face'],
}
