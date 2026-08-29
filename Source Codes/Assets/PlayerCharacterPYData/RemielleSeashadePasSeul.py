"""
RemielleSeashadePasSeul Character Hash Commands
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
    Returns RemielleSeashadePasSeul's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'789ae812': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'3a0100ab': [
        (log,                           ('3.1: RemielleSeashadePasSeul HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'241deac5': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b1870eee': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'9004a39a': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fcbae9a5': [
        (log,                           ('3.1: RemielleSeashadePasSeul Eyebrow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'7fbbcf0d': [
        (log,                           ('3.1: RemielleSeashadePasSeul Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'fbe70114': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],
'62b7da5e': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],
'fa8ab367': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],
'46eee329': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],
'48288582': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body VB Hash',)),
        (add_section_if_missing, ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
    ],
'13c77c3a': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body VB Hash',)),
        (add_section_if_missing, ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
    ],
'c55c57ce': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body VB Hash',)),
        (add_section_if_missing, ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
    ],
'9bca83d8': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body VB Hash',)),
        (add_section_if_missing, ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
    ],
'041193d7': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg VB Hash',)),
        (add_section_if_missing, ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
    ],
'8ef10584': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg VB Hash',)),
        (add_section_if_missing, ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
    ],
'b31b61d1': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg VB Hash',)),
        (add_section_if_missing, ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
    ],
'cf15b1ce': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg VB Hash',)),
        (add_section_if_missing, ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
    ],
'7bc98032': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
    ],
'f71d4482': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
    ],
'9d9b4d62': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
    ],
'7b12084f': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
    ],
'0faf109a': [
        (log,                           ('3.1: RemielleSeashadePasSeul Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
    ],
'35bd83dd': [
        (log,                           ('3.1: RemielleSeashadePasSeul Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
    ],
'7e8be536': [
        (log,                           ('3.1: RemielleSeashadePasSeul Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
    ],
'3ba8ce1b': [
        (log,                           ('3.1: RemielleSeashadePasSeul Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
# Hair Diffuse
'8a619774': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('578239d7', 'RemielleSeashadePasSeul.Hair.Diffuse.2048')),
    ],
'578239d7': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('8a619774', 'RemielleSeashadePasSeul.Hair.Diffuse.1024')),
    ],

# Hair LightMap
'45bb8a18': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('6f826e7d', 'RemielleSeashadePasSeul.Hair.LightMap.2048')),
    ],
'6f826e7d': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('45bb8a18', 'RemielleSeashadePasSeul.Hair.LightMap.1024')),
    ],

# Hair MaterialMap
'8b8df55e': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('b5a12580', 'RemielleSeashadePasSeul.Hair.MaterialMap.2048')),
    ],
'b5a12580': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('8b8df55e', 'RemielleSeashadePasSeul.Hair.MaterialMap.1024')),
    ],

'ebac056e': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: RemielleSeashadePasSeul Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Diffuse
'fb0f2f5d': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('686a0805', 'RemielleSeashadePasSeul.Body.Diffuse.2048')),
    ],
'686a0805': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('fb0f2f5d', 'RemielleSeashadePasSeul.Body.Diffuse.1024')),
    ],

# Body LightMap
'c4d1c25b': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('a255803d', 'RemielleSeashadePasSeul.Body.LightMap.2048')),
    ],
'a255803d': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('c4d1c25b', 'RemielleSeashadePasSeul.Body.LightMap.1024')),
    ],

# Body MaterialMap
'd52ee692': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('fb91abe9', 'RemielleSeashadePasSeul.Body.MaterialMap.2048')),
    ],
'fb91abe9': [
        (log,                           ('3.1: RemielleSeashadePasSeul Body MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('d52ee692', 'RemielleSeashadePasSeul.Body.MaterialMap.1024')),
    ],

# Leg Diffuse
'1fb64395': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('517d9d7c', 'RemielleSeashadePasSeul.Leg.Diffuse.2048')),
    ],
'517d9d7c': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('1fb64395', 'RemielleSeashadePasSeul.Leg.Diffuse.1024')),
    ],

# Leg LightMap
'63ef7922': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('6a673bda', 'RemielleSeashadePasSeul.Leg.LightMap.2048')),
    ],
'6a673bda': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('63ef7922', 'RemielleSeashadePasSeul.Leg.LightMap.1024')),
    ],

# Leg MaterialMap
'ac5220b6': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('f87f83d9', 'RemielleSeashadePasSeul.Leg.MaterialMap.2048')),
    ],
'f87f83d9': [
        (log,                           ('3.1: RemielleSeashadePasSeul Leg MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('ac5220b6', 'RemielleSeashadePasSeul.Leg.MaterialMap.1024')),
    ],

# Wings Diffuse
'cdc91dce': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('80ad86c3', 'RemielleSeashadePasSeul.Wings.Diffuse.2048')),
    ],
'80ad86c3': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('cdc91dce', 'RemielleSeashadePasSeul.Wings.Diffuse.1024')),
    ],

# Wings LightMap
'128e607f': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('04497af6', 'RemielleSeashadePasSeul.Wings.LightMap.2048')),
    ],
'04497af6': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('128e607f', 'RemielleSeashadePasSeul.Wings.LightMap.1024')),
    ],

# Wings MaterialMap
'c23e467e': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('0ec88318', 'RemielleSeashadePasSeul.Wings.MaterialMap.2048')),
    ],
'0ec88318': [
        (log,                           ('3.1: RemielleSeashadePasSeul Wings MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('c23e467e', 'RemielleSeashadePasSeul.Wings.MaterialMap.1024')),
    ],

'baf9e1be': [
        (log,                           ('3.1: RemielleSeashadePasSeul Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'RemielleSeashadePasSeul.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'5bc2bbdd': [
        (log,                           ('3.1: RemielleSeashadePasSeul Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'RemielleSeashadePasSeul.Eyebrow.IB', 'match_priority = 0\n')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'RemielleSeashadePasSeul',
    'game_versions': ['3.1'],
}
