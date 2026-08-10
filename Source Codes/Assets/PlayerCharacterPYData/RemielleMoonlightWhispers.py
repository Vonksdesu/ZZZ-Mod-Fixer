"""
RemielleMoonlightWhispers Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.1
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns RemielleMoonlightWhispers's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'789ae812': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'3a0100ab': [
        (log,                           ('3.1: RemielleMoonlightWhispers HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'f57f3e40': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'09a51ed3': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'9004a39a': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fcbae9a5': [
        (log,                           ('3.1: RemielleMoonlightWhispers Eyebrow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'7fbbcf0d': [
        (log,                           ('3.1: RemielleMoonlightWhispers Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'fbe70114': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],
'62b7da5e': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],
'fa8ab367': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],
'46eee329': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],
'22ec622c': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body VB Hash',)),
        (add_section_if_missing, ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
    ],
'554d46cf': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body VB Hash',)),
        (add_section_if_missing, ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
    ],
'5dcc6ee1': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body VB Hash',)),
        (add_section_if_missing, ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
    ],
'7f6fe876': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body VB Hash',)),
        (add_section_if_missing, ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
    ],
'96dc0a8e': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg VB Hash',)),
        (add_section_if_missing, ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
    ],
'fa9635bc': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg VB Hash',)),
        (add_section_if_missing, ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
    ],
'7c0db158': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg VB Hash',)),
        (add_section_if_missing, ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
    ],
'ff05e5f9': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg VB Hash',)),
        (add_section_if_missing, ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
    ],
'7bc98032': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
    ],
'f71d4482': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
    ],
'9d9b4d62': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
    ],
'7b12084f': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
    ],
'0faf109a': [
        (log,                           ('3.1: RemielleMoonlightWhispers Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
    ],
'35bd83dd': [
        (log,                           ('3.1: RemielleMoonlightWhispers Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
    ],
'7e8be536': [
        (log,                           ('3.1: RemielleMoonlightWhispers Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
    ],
'3ba8ce1b': [
        (log,                           ('3.1: RemielleMoonlightWhispers Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
# Hair Diffuse
'8a619774': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('578239d7', 'RemielleMoonlightWhispers.Hair.Diffuse.2048')),
    ],
'578239d7': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('8a619774', 'RemielleMoonlightWhispers.Hair.Diffuse.1024')),
    ],

# Hair LightMap
'45bb8a18': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('6f826e7d', 'RemielleMoonlightWhispers.Hair.LightMap.2048')),
    ],
'6f826e7d': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('45bb8a18', 'RemielleMoonlightWhispers.Hair.LightMap.1024')),
    ],

# Hair MaterialMap
'8b8df55e': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('b5a12580', 'RemielleMoonlightWhispers.Hair.MaterialMap.2048')),
    ],
'b5a12580': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('8b8df55e', 'RemielleMoonlightWhispers.Hair.MaterialMap.1024')),
    ],

'ebac056e': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: RemielleMoonlightWhispers Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Diffuse
'abb0d69d': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('0e408177', 'RemielleMoonlightWhispers.Body.Diffuse.2048')),
    ],
'0e408177': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('abb0d69d', 'RemielleMoonlightWhispers.Body.Diffuse.1024')),
    ],

# Body LightMap
'2aab9aa7': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('6102ae18', 'RemielleMoonlightWhispers.Body.LightMap.2048')),
    ],
'6102ae18': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('2aab9aa7', 'RemielleMoonlightWhispers.Body.LightMap.1024')),
    ],

# Body MaterialMap
'e9f33a20': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('cccb8109', 'RemielleMoonlightWhispers.Body.MaterialMap.2048')),
    ],
'cccb8109': [
        (log,                           ('3.1: RemielleMoonlightWhispers Body MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('e9f33a20', 'RemielleMoonlightWhispers.Body.MaterialMap.1024')),
    ],

# Leg Diffuse
'4c49a23c': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('877b0ce6', 'RemielleMoonlightWhispers.Leg.Diffuse.2048')),
    ],
'877b0ce6': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('4c49a23c', 'RemielleMoonlightWhispers.Leg.Diffuse.1024')),
    ],

# Leg LightMap
'17b9c313': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('baeb2662', 'RemielleMoonlightWhispers.Leg.LightMap.2048')),
    ],
'baeb2662': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('17b9c313', 'RemielleMoonlightWhispers.Leg.LightMap.1024')),
    ],

# Leg MaterialMap
'2dce69bd': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('3b0c9e0a', 'RemielleMoonlightWhispers.Leg.MaterialMap.2048')),
    ],
'3b0c9e0a': [
        (log,                           ('3.1: RemielleMoonlightWhispers Leg MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('2dce69bd', 'RemielleMoonlightWhispers.Leg.MaterialMap.1024')),
    ],

# Wings Diffuse
'b8574ee2': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('677ec0d0', 'RemielleMoonlightWhispers.Wings.Diffuse.2048')),
    ],
'677ec0d0': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('b8574ee2', 'RemielleMoonlightWhispers.Wings.Diffuse.1024')),
    ],

# Wings LightMap
'128e607f': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('04497af6', 'RemielleMoonlightWhispers.Wings.LightMap.2048')),
    ],
'04497af6': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('128e607f', 'RemielleMoonlightWhispers.Wings.LightMap.1024')),
    ],

# Wings MaterialMap
'c23e467e': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('0ec88318', 'RemielleMoonlightWhispers.Wings.MaterialMap.2048')),
    ],
'0ec88318': [
        (log,                           ('3.1: RemielleMoonlightWhispers Wings MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('c23e467e', 'RemielleMoonlightWhispers.Wings.MaterialMap.1024')),
    ],

'baf9e1be': [
        (log,                           ('3.1: RemielleMoonlightWhispers Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'RemielleMoonlightWhispers.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'5bc2bbdd': [
        (log,                           ('3.1: RemielleMoonlightWhispers Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'RemielleMoonlightWhispers.Eyebrow.IB', 'match_priority = 0\n')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'RemielleMoonlightWhispers',
    'game_versions': ['3.1'],
}
