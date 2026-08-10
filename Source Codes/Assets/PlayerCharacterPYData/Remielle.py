"""
Remielle Character Hash Commands
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
    Returns Remielle's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'789ae812': [
        (log,                           ('3.1: Remielle Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'3a0100ab': [
        (log,                           ('3.1: Remielle HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'785b21f5': [
        (log,                           ('3.1: Remielle Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fe9fc31a': [
        (log,                           ('3.1: Remielle Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'9004a39a': [
        (log,                           ('3.1: Remielle Wings IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fcbae9a5': [
        (log,                           ('3.1: Remielle Eyebrow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'7fbbcf0d': [
        (log,                           ('3.1: Remielle Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'e0b4b061': [
        (log,                           ('3.1: Remielle Sword IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'1b655510': [
        (log,                           ('3.1: Remielle Hilt1 IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'14cf141e': [
        (log,                           ('3.1: Remielle Hilt2 IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'ca717c18': [
        (log,                           ('3.1: Remielle Aircraft IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6ef3d666': [
        (log,                           ('3.1: Remielle AircraftTexture IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'acfa670a': [
        (log,                           ('3.1: Remielle Injector IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'fbe70114': [
        (log,                           ('3.1: Remielle Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],
'62b7da5e': [
        (log,                           ('3.1: Remielle Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],
'fa8ab367': [
        (log,                           ('3.1: Remielle Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],
'46eee329': [
        (log,                           ('3.1: Remielle Hair VB Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],
'7a92a10a': [
        (log,                           ('3.1: Remielle Body VB Hash',)),
        (add_section_if_missing, ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
    ],
'679a1bd8': [
        (log,                           ('3.1: Remielle Body VB Hash',)),
        (add_section_if_missing, ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
    ],
'9e33a8b6': [
        (log,                           ('3.1: Remielle Body VB Hash',)),
        (add_section_if_missing, ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
    ],
'9e8a27ae': [
        (log,                           ('3.1: Remielle Body VB Hash',)),
        (add_section_if_missing, ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
    ],
'3bf3b3b0': [
        (log,                           ('3.1: Remielle Leg VB Hash',)),
        (add_section_if_missing, ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
    ],
'1bc49355': [
        (log,                           ('3.1: Remielle Leg VB Hash',)),
        (add_section_if_missing, ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
    ],
'ed8feacb': [
        (log,                           ('3.1: Remielle Leg VB Hash',)),
        (add_section_if_missing, ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
    ],
'2702db6d': [
        (log,                           ('3.1: Remielle Leg VB Hash',)),
        (add_section_if_missing, ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
    ],
'7bc98032': [
        (log,                           ('3.1: Remielle Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],
'f71d4482': [
        (log,                           ('3.1: Remielle Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],
'9d9b4d62': [
        (log,                           ('3.1: Remielle Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],
'7b12084f': [
        (log,                           ('3.1: Remielle Wings VB Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],
'0faf109a': [
        (log,                           ('3.1: Remielle Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
    ],
'35bd83dd': [
        (log,                           ('3.1: Remielle Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
    ],
'7e8be536': [
        (log,                           ('3.1: Remielle Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
    ],
'3ba8ce1b': [
        (log,                           ('3.1: Remielle Face VB Hash',)),
        (add_section_if_missing, ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
    ],
'd13c771a': [
        (log,                           ('3.1: Remielle Sword VB Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],
'bebcecd1': [
        (log,                           ('3.1: Remielle Sword VB Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],
'04360ff9': [
        (log,                           ('3.1: Remielle Sword VB Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],
'df30a4a2': [
        (log,                           ('3.1: Remielle Sword VB Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],
'cb55081c': [
        (log,                           ('3.1: Remielle Hilt1 VB Hash',)),
        (add_section_if_missing, ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
    ],
'3c5ffb4a': [
        (log,                           ('3.1: Remielle Hilt1 VB Hash',)),
        (add_section_if_missing, ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
    ],
'92f10a81': [
        (log,                           ('3.1: Remielle Hilt1 VB Hash',)),
        (add_section_if_missing, ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
    ],
'b82da0bb': [
        (log,                           ('3.1: Remielle Hilt1 VB Hash',)),
        (add_section_if_missing, ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
    ],
'd482d732': [
        (log,                           ('3.1: Remielle Hilt2 VB Hash',)),
        (add_section_if_missing, ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
    ],
'95a2457a': [
        (log,                           ('3.1: Remielle Hilt2 VB Hash',)),
        (add_section_if_missing, ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
    ],
'96452d20': [
        (log,                           ('3.1: Remielle Hilt2 VB Hash',)),
        (add_section_if_missing, ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
    ],
'44d4a8ad': [
        (log,                           ('3.1: Remielle Hilt2 VB Hash',)),
        (add_section_if_missing, ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
    ],
'dd402a5c': [
        (log,                           ('3.1: Remielle Aircraft VB Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],
'9615df83': [
        (log,                           ('3.1: Remielle Aircraft VB Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],
'dd3180e4': [
        (log,                           ('3.1: Remielle Aircraft VB Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],
'945317d9': [
        (log,                           ('3.1: Remielle Aircraft VB Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],
'3b13c5c5': [
        (log,                           ('3.1: Remielle AircraftTexture VB Hash',)),
        (add_section_if_missing, ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
    ],
'f39a7cec': [
        (log,                           ('3.1: Remielle AircraftTexture VB Hash',)),
        (add_section_if_missing, ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
    ],
'3b2b251d': [
        (log,                           ('3.1: Remielle AircraftTexture VB Hash',)),
        (add_section_if_missing, ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
    ],
'4fa9be65': [
        (log,                           ('3.1: Remielle AircraftTexture VB Hash',)),
        (add_section_if_missing, ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
# Hair Diffuse
'8a619774': [
        (log,                           ('3.1: Remielle Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('578239d7', 'Remielle.Hair.Diffuse.2048')),
    ],
'578239d7': [
        (log,                           ('3.1: Remielle Hair Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('8a619774', 'Remielle.Hair.Diffuse.1024')),
    ],

# Hair LightMap
'45bb8a18': [
        (log,                           ('3.1: Remielle Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('6f826e7d', 'Remielle.Hair.LightMap.2048')),
    ],
'6f826e7d': [
        (log,                           ('3.1: Remielle Hair LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('45bb8a18', 'Remielle.Hair.LightMap.1024')),
    ],

# Hair MaterialMap
'8b8df55e': [
        (log,                           ('3.1: Remielle Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('b5a12580', 'Remielle.Hair.MaterialMap.2048')),
    ],
'b5a12580': [
        (log,                           ('3.1: Remielle Hair MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('8b8df55e', 'Remielle.Hair.MaterialMap.1024')),
    ],

'ebac056e': [
        (log,                           ('3.1: Remielle Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: Remielle Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Diffuse
'd770d330': [
        (log,                           ('3.1: Remielle Body Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('e51be5d1', 'Remielle.Body.Diffuse.2048')),
    ],
'e51be5d1': [
        (log,                           ('3.1: Remielle Body Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('d770d330', 'Remielle.Body.Diffuse.1024')),
    ],

# Body LightMap
'b95031e2': [
        (log,                           ('3.1: Remielle Body LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('380d7bcf', 'Remielle.Body.LightMap.2048')),
    ],
'380d7bcf': [
        (log,                           ('3.1: Remielle Body LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('b95031e2', 'Remielle.Body.LightMap.1024')),
    ],

# Body MaterialMap
'ed6ca67a': [
        (log,                           ('3.1: Remielle Body MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('61c42d63', 'Remielle.Body.MaterialMap.2048')),
    ],
'61c42d63': [
        (log,                           ('3.1: Remielle Body MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('ed6ca67a', 'Remielle.Body.MaterialMap.1024')),
    ],

# Leg Diffuse
'49ac9d9e': [
        (log,                           ('3.1: Remielle Leg Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('6538d30d', 'Remielle.Leg.Diffuse.2048')),
    ],
'6538d30d': [
        (log,                           ('3.1: Remielle Leg Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('49ac9d9e', 'Remielle.Leg.Diffuse.1024')),
    ],

# Leg LightMap
'95db220c': [
        (log,                           ('3.1: Remielle Leg LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('4049331b', 'Remielle.Leg.LightMap.2048')),
    ],
'4049331b': [
        (log,                           ('3.1: Remielle Leg LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('95db220c', 'Remielle.Leg.LightMap.1024')),
    ],

# Leg MaterialMap
'1c782fe7': [
        (log,                           ('3.1: Remielle Leg MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('cdc2accb', 'Remielle.Leg.MaterialMap.2048')),
    ],
'cdc2accb': [
        (log,                           ('3.1: Remielle Leg MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('1c782fe7', 'Remielle.Leg.MaterialMap.1024')),
    ],

# Wings Diffuse
'cdc91dce': [
        (log,                           ('3.1: Remielle Wings Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('80ad86c3', 'Remielle.Wings.Diffuse.2048')),
    ],
'80ad86c3': [
        (log,                           ('3.1: Remielle Wings Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('cdc91dce', 'Remielle.Wings.Diffuse.1024')),
    ],

'04497af6': [
        (log,                           ('3.1: Remielle Wings LightMap TEX Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],

'128e607f': [
        (log,                           ('3.1: Remielle Wings LightMap TEX Hash',)),
        (add_section_if_missing, ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
    ],

# Wings MaterialMap
'c23e467e': [
        (log,                           ('3.1: Remielle Wings MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('0ec88318', 'Remielle.Wings.MaterialMap.2048')),
    ],
'0ec88318': [
        (log,                           ('3.1: Remielle Wings MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('c23e467e', 'Remielle.Wings.MaterialMap.1024')),
    ],

'baf9e1be': [
        (log,                           ('3.1: Remielle Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'Remielle.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'5bc2bbdd': [
        (log,                           ('3.1: Remielle Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('fcbae9a5', 'Remielle.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'85b91845': [
        (log,                           ('3.1: Remielle Sword Diffuse TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'77d73d18': [
        (log,                           ('3.1: Remielle Sword Diffuse TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'e06fd26b': [
        (log,                           ('3.1: Remielle Sword LightMap TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'2931c061': [
        (log,                           ('3.1: Remielle Sword LightMap TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'9455f7a5': [
        (log,                           ('3.1: Remielle Sword MaterialMap TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'4844d251': [
        (log,                           ('3.1: Remielle Sword MaterialMap TEX Hash',)),
        (add_section_if_missing, ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
    ],

'420e2418': [
        (log,                           ('3.1: Remielle Aircraft Diffuse TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

'd930a5fa': [
        (log,                           ('3.1: Remielle Aircraft Diffuse TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

'5fda974c': [
        (log,                           ('3.1: Remielle Aircraft LightMap TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

'9f940f25': [
        (log,                           ('3.1: Remielle Aircraft LightMap TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

'4948fe09': [
        (log,                           ('3.1: Remielle Aircraft MaterialMap TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

'f01b9d5c': [
        (log,                           ('3.1: Remielle Aircraft MaterialMap TEX Hash',)),
        (add_section_if_missing, ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
    ],

# AircraftTexture Diffuse
'037e650c': [
        (log,                           ('3.1: Remielle AircraftTexture Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('cd400938', 'Remielle.AircraftTexture.Diffuse.2048')),
    ],
'cd400938': [
        (log,                           ('3.1: Remielle AircraftTexture Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('037e650c', 'Remielle.AircraftTexture.Diffuse.1024')),
    ],

# AircraftTexture MaterialMap
'23186e62': [
        (log,                           ('3.1: Remielle AircraftTexture MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('dd0a0bd1', 'Remielle.AircraftTexture.MaterialMap.2048')),
    ],
'dd0a0bd1': [
        (log,                           ('3.1: Remielle AircraftTexture MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('23186e62', 'Remielle.AircraftTexture.MaterialMap.1024')),
    ],

# AircraftTexture NormalMap
'e1864c72': [
        (log,                           ('3.1: Remielle AircraftTexture NormalMap 1024p Hash',)),
        (multiply_section_if_missing, ('b8f3b02a', 'Remielle.AircraftTexture.NormalMap.2048')),
    ],
'b8f3b02a': [
        (log,                           ('3.1: Remielle AircraftTexture NormalMap 2048p Hash',)),
        (multiply_section_if_missing, ('e1864c72', 'Remielle.AircraftTexture.NormalMap.1024')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Remielle',
    'game_versions': ['3.1'],
}
