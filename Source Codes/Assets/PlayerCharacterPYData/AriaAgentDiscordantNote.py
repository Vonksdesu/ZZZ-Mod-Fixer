"""
AriaAgentDiscordantNote Character Hash Commands
ZZZ Mod Fixer v2.6
Game Version: 2.6
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns AriaAgentDiscordantNote's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===


# === AriaAgentDiscordantNote Textures (FaceA) ===
'28466273': [
        (log,                           ('2.6: AriaAgentDiscordantNote FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('6b11a215', 'AriaAgentDiscordantNote.FaceA.Diffuse.2048')),
    ],
'6b11a215': [
        (log,                           ('2.6: AriaAgentDiscordantNote FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('28466273', 'AriaAgentDiscordantNote.FaceA.Diffuse.1024')),
    ],

# === AriaAgentDiscordantNote Textures (HairA) ===
'fc3231cd': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('fb2c3964', 'AriaAgentDiscordantNote.HairA.Diffuse.2048')),
    ],
'fb2c3964': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('fc3231cd', 'AriaAgentDiscordantNote.HairA.Diffuse.1024')),
    ],
'380fbecb': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('21aac04f', 'AriaAgentDiscordantNote.HairA.LightMap.2048')),
    ],
'21aac04f': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('380fbecb', 'AriaAgentDiscordantNote.HairA.LightMap.1024')),
    ],
'8f3cfb68': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e1ccfca4', 'AriaAgentDiscordantNote.HairA.MaterialMap.2048')),
    ],
'e1ccfca4': [
        (log,                           ('2.6: AriaAgentDiscordantNote HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('8f3cfb68', 'AriaAgentDiscordantNote.HairA.MaterialMap.1024')),
    ],

# === AriaAgentDiscordantNote Textures (BodyA) ===
'1bf43198': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('282c7753', 'AriaAgentDiscordantNote.BodyA.Diffuse.2048')),
    ],
'282c7753': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('1bf43198', 'AriaAgentDiscordantNote.BodyA.Diffuse.1024')),
    ],
'99f9094c': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('263f8811', 'AriaAgentDiscordantNote.BodyA.LightMap.2048')),
    ],
'263f8811': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('99f9094c', 'AriaAgentDiscordantNote.BodyA.LightMap.1024')),
    ],
'ab411caa': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('f5b45cc2', 'AriaAgentDiscordantNote.BodyA.MaterialMap.2048')),
    ],
'f5b45cc2': [
        (log,                           ('2.6: AriaAgentDiscordantNote BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ab411caa', 'AriaAgentDiscordantNote.BodyA.MaterialMap.1024')),
    ],
'1173ff78': [(log, ('3.0: AriaAgentDiscordantNote Hair IB Hash',)), (add_ib_check_if_missing,)],
'5bbaca72': [
        (log, ('3.0: AriaAgentDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'42a4622f': [
        (log, ('3.0: AriaAgentDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'23629315': [
        (log, ('3.0: AriaAgentDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'468e532f': [
        (log, ('3.0: AriaAgentDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'be70c507': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'41124010': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'01087a99': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'046400d3': [(log, ('3.0: AriaAgentDiscordantNote Body IB Hash',)), (add_ib_check_if_missing,)],
'a28a907a': [
        (log, ('3.0: AriaAgentDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'608bff86': [
        (log, ('3.0: AriaAgentDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'b019dae2': [
        (log, ('3.0: AriaAgentDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'7c85654d': [
        (log, ('3.0: AriaAgentDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'ac9c2ebb': [(log, ('3.0: AriaAgentDiscordantNote Decoration IB Hash',)), (add_ib_check_if_missing,)],
'8e2e89dc': [
        (log, ('3.0: AriaAgentDiscordantNote Decoration VB Hash',)),
        (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'09998ea7': [
        (log, ('3.0: AriaAgentDiscordantNote Decoration VB Hash',)),
        (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'9f6fa4fe': [
        (log, ('3.0: AriaAgentDiscordantNote Decoration VB Hash',)),
        (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'624d99aa': [
        (log, ('3.0: AriaAgentDiscordantNote Decoration VB Hash',)),
        (add_section_if_missing, ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
    ],
'ffa703e8': [(log, ('3.0: AriaAgentDiscordantNote Face IB Hash',)), (add_ib_check_if_missing,)],
'f0c79e51': [
        (log, ('3.0: AriaAgentDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'b62f2772': [
        (log, ('3.0: AriaAgentDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'9772ccda': [
        (log, ('3.0: AriaAgentDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'ea540ea2': [
        (log, ('3.0: AriaAgentDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'db7c8d25': [(log, ('3.0: AriaAgentDiscordantNote Eye IB Hash',)), (add_ib_check_if_missing,)],
'390a4a23': [
        (log, ('3.0: AriaAgentDiscordantNote Eye VB Hash',)),
        (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
    ],
'cf12b575': [
        (log, ('3.0: AriaAgentDiscordantNote Eye VB Hash',)),
        (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
    ],
'22b99744': [
        (log, ('3.0: AriaAgentDiscordantNote Eye VB Hash',)),
        (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
    ],
'71fabd1a': [
        (log, ('3.0: AriaAgentDiscordantNote Eye VB Hash',)),
        (add_section_if_missing, ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
    ],
'62cc8d20': [(log, ('3.0: AriaAgentDiscordantNote Weapon IB Hash',)), (add_ib_check_if_missing,)],
'380bb1a8': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon VB Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'adbfa4c4': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'71966d3f': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'328592b5': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'f0aec120': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'9e2e56b3': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'002360e1': [
        (log, ('3.0: AriaAgentDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'2c3a5d8d': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'4a0da1fb': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'825f0b0b': [
        (log, ('3.0: AriaAgentDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AriaAgentDiscordantNote',
    'game_versions': ['2.6'],
}
