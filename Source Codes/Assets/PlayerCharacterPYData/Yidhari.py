"""
Yidhari Character Hash Commands
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
    Returns Yidhari's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'2022936e': [(log, ('2.5: Yidhari Hair IB Hash',)),   (add_ib_check_if_missing,)],
'12251f42': [(log, ('2.5: Yidhari Body IB Hash',)),   (add_ib_check_if_missing,)],
'4cb99618': [(log, ('2.5: Yidhari Tentacles IB Hash',)),   (add_ib_check_if_missing,)],
'1c164f7f': [(log, ('2.5: Yidhari RgbBars IB Hash',)),   (add_ib_check_if_missing,)],
'02072970': [(log, ('2.5: Yidhari Brows IB Hash',)),   (add_ib_check_if_missing,)],
'a2406060': [(log, ('2.5: Yidhari Face IB Hash',)),   (add_ib_check_if_missing,)],

# Hair Textures
'd0587bc2': [
        (log,                           ('2.5: Yidhari HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('aefe5860', 'Yidhari.HairA.Diffuse.1024')),
    ],

'aefe5860': [
        (log,                           ('2.5: Yidhari HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d0587bc2', 'Yidhari.HairA.Diffuse.2048')),
    ],
'42ef8882': [
        (log,                           ('2.5: Yidhari HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('222b6f58', 'Yidhari.HairA.LightMap.1024')),
    ],

'222b6f58': [
        (log,                           ('2.5: Yidhari HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('42ef8882', 'Yidhari.HairA.LightMap.2048')),
    ],
'bc5d6f24': [
        (log,                           ('2.5: Yidhari HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('527ac41b', 'Yidhari.HairA.MaterialMap.1024')),
    ],

'527ac41b': [
        (log,                           ('2.5: Yidhari HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bc5d6f24', 'Yidhari.HairA.MaterialMap.2048')),
    ],

# Body Textures
'ca51f269': [
        (log,                           ('2.5: Yidhari BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('89bec19d', 'Yidhari.BodyA.Diffuse.1024')),
    ],

'89bec19d': [
        (log,                           ('2.5: Yidhari BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ca51f269', 'Yidhari.BodyA.Diffuse.2048')),
    ],
'2ae9bee8': [(log, ('2.3 -> 2.4: Yidhair BodyA LightMap 2048p Hash',)), (update_hash, ('5b985a6f',))],
'5b985a6f': [
        (log,                           ('2.5: Yidhari BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('9ad20501', '381e8e5a'), 'Yidhari.BodyA.LightMap.1024')),
    ],

'9ad20501': [(log, ('2.3 -> 2.4: Yidhair BodyA LightMap 1024p Hash',)), (update_hash, ('381e8e5a',))],
'381e8e5a': [
        (log,                           ('2.5: Yidhari BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('2ae9bee8', '5b985a6f'), 'Yidhari.BodyA.LightMap.2048')),
    ],
'0e91ed54': [
        (log,                           ('2.5: Yidhari BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9af65de7', 'Yidhari.BodyA.MaterialMap.1024')),
    ],

'9af65de7': [
        (log,                           ('2.5: Yidhari BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0e91ed54', 'Yidhari.BodyA.MaterialMap.2048')),
    ],

# Tentacles Textures
'2156a161': [
        (log,                           ('2.5: Yidhari TentaclesA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('067b0a15', 'Yidhari.TailA.Diffuse.1024')),
    ],

'067b0a15': [
        (log,                           ('2.5: Yidhari TentaclesA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2156a161', 'Yidhari.TailA.Diffuse.2048')),
    ],
'8bf59f48': [
        (log,                           ('2.5: Yidhari TentaclesA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6b99432e', 'Yidhari.TailA.LightMap.1024')),
    ],

'6b99432e': [
        (log,                           ('2.5: Yidhari TentaclesA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8bf59f48', 'Yidhari.TailA.LightMap.2048')),
    ],
'e0bb4de9': [
        (log,                           ('2.5: Yidhari TentaclesA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0bf712a3', 'Yidhari.TailA.MaterialMap.1024')),
    ],

'0bf712a3': [
        (log,                           ('2.5: Yidhari TentaclesA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e0bb4de9', 'Yidhari.TailA.MaterialMap.2048')),
    ],

# Face/Brows Shared Diffuse Texture
'c6e0cfbe': [
        (log,                           ('2.5: Yidhari Face & Brows Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02072970', 'Yidhari.Brows.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4753db8f', 'Yidhari.FaceA.Diffuse.1024')),
    ],

'4753db8f': [
        (log,                           ('2.5: Yidhari Face & Brows Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('02072970', 'Yidhari.Brows.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c6e0cfbe', 'Yidhari.FaceA.Diffuse.2048')),
    ],

# Shared NormalMap (Hair, Body, Tentacles)
'ebac056e': [
        (log,                           ('2.5: Yidhari Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4cb99618', 'Yidhari.Tentacles.IB', 'match_priority = 0\n')),
    ],
'4512a51e': [
        (log, ('3.0: Yidhari Hair VB Hash',)),
        (add_section_if_missing, ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'028c0d28': [
        (log, ('3.0: Yidhari Hair VB Hash',)),
        (add_section_if_missing, ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'6a65d55c': [
        (log, ('3.0: Yidhari Hair VB Hash',)),
        (add_section_if_missing, ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'a5a5654d': [(log, ('3.0: Yidhari Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'225ffc91': [
        (log, ('3.0: Yidhari Hair Shadow VB Hash',)),
        (add_section_if_missing, ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'e13a4a8c': [
        (log, ('3.0: Yidhari Hair Shadow VB Hash',)),
        (add_section_if_missing, ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a74fecc6': [
        (log, ('3.0: Yidhari Hair Shadow VB Hash',)),
        (add_section_if_missing, ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'7d881667': [
        (log, ('3.0: Yidhari Hair Shadow VB Hash',)),
        (add_section_if_missing, ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'471aa92a': [
        (log, ('3.0: Yidhari Body VB Hash',)),
        (add_section_if_missing, ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'74f07fc5': [
        (log, ('3.0: Yidhari Body VB Hash',)),
        (add_section_if_missing, ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'2abc67fb': [
        (log, ('3.0: Yidhari Body VB Hash',)),
        (add_section_if_missing, ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'eff05950': [
        (log, ('3.0: Yidhari Body VB Hash',)),
        (add_section_if_missing, ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
    ],
'bf5562d4': [
        (log, ('3.0: Yidhari Tail VB Hash',)),
        (add_section_if_missing, ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
    ],
'c9dab2d3': [
        (log, ('3.0: Yidhari Tail VB Hash',)),
        (add_section_if_missing, ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
    ],
'344e456e': [
        (log, ('3.0: Yidhari Tail VB Hash',)),
        (add_section_if_missing, ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
    ],
'9b99674d': [
        (log, ('3.0: Yidhari Tail VB Hash',)),
        (add_section_if_missing, ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
    ],
'695ebcdc': [
        (log, ('3.0: Yidhari eyebrow VB Hash',)),
        (add_section_if_missing, ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
    ],
'cf1a7297': [
        (log, ('3.0: Yidhari eyebrow VB Hash',)),
        (add_section_if_missing, ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
    ],
'ee532c5b': [
        (log, ('3.0: Yidhari eyebrow VB Hash',)),
        (add_section_if_missing, ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
    ],
'b0ac2b60': [
        (log, ('3.0: Yidhari Face VB Hash',)),
        (add_section_if_missing, ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
    ],
'08316415': [
        (log, ('3.0: Yidhari Face VB Hash',)),
        (add_section_if_missing, ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
    ],
'de712ebf': [
        (log, ('3.0: Yidhari Face VB Hash',)),
        (add_section_if_missing, ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
    ],
'bc96ab6e': [(log, ('3.0: Yidhari weapon IB Hash',)), (add_ib_check_if_missing,)],
'09c65b14': [
        (log, ('3.0: Yidhari weapon VB Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'5a6fe39e': [
        (log, ('3.0: Yidhari weapon VB Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'f98b369d': [
        (log, ('3.0: Yidhari weapon VB Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'48889652': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'e6728419': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'42666703': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'534c2f9b': [(log, ('3.0: Yidhari misc hash',)),],
'6bc320f0': [(log, ('3.0: Yidhari misc hash',)),],
'8abeb827': [(log, ('3.0: Yidhari misc hash',)),],
'2736d089': [
        (log, ('3.0: Yidhari Hair VB Hash',)),
        (add_section_if_missing, ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Yidhari Hair TEX Hash',)),
        (add_section_if_missing, ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
    ],
'85b7643e': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'cbb02c28': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
'd17095b0': [
        (log, ('3.0: Yidhari weapon TEX Hash',)),
        (add_section_if_missing, ('bc96ab6e', 'Yidhari.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yidhari',
    'game_versions': ['2.5'],
}

