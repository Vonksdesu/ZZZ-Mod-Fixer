"""
AriaDiscordantNote Character Hash Commands
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
    Returns AriaDiscordantNote's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'c6bb960b': [
        (log,                           ('2.6: AriaDiscordantNote Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'923c64c0': [
        (log,                           ('2.6: AriaDiscordantNote Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === AriaDiscordantNote Textures (BodyA) ===
'3c6bd181': [
        (log,                           ('2.6 -> 2.7: AriaDiscordantNote BodyA Diffuse 1024p Hash',)),
        (update_hash,                        ('303c63bc',)),
    ],
'a55f187e': [
        (log,                           ('2.6 -> 2.7: AriaDiscordantNote BodyA Diffuse 2048p Hash',)),
        (update_hash,                        ('677f73d9',)),
    ],
'303c63bc': [
        (log,                           ('2.6: AriaDiscordantNote BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('a55f187e', '677f73d9'), 'AriaDiscordantNote.BodyA.Diffuse.2048')),
    ],
'677f73d9': [
        (log,                           ('2.6: AriaDiscordantNote BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('3c6bd181', '303c63bc'), 'AriaDiscordantNote.BodyA.Diffuse.1024')),
    ],
'a97204aa': [
        (log,                           ('2.6: AriaDiscordantNote BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('acee133c', 'AriaDiscordantNote.BodyA.LightMap.2048')),
    ],
'acee133c': [
        (log,                           ('2.6: AriaDiscordantNote BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('a97204aa', 'AriaDiscordantNote.BodyA.LightMap.1024')),
    ],
'2418c407': [
        (log,                           ('2.6: AriaDiscordantNote BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6ac35f02', 'AriaDiscordantNote.BodyA.MaterialMap.2048')),
    ],
'6ac35f02': [
        (log,                           ('2.6: AriaDiscordantNote BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('2418c407', 'AriaDiscordantNote.BodyA.MaterialMap.1024')),
    ],

# === AriaDiscordantNote Textures (LegA) ===
'd754c95b': [
        (log,                           ('2.6: AriaDiscordantNote LegA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('a34313c8', 'AriaDiscordantNote.LegA.Diffuse.2048')),
    ],
'a34313c8': [
        (log,                           ('2.6: AriaDiscordantNote LegA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('d754c95b', 'AriaDiscordantNote.LegA.Diffuse.1024')),
    ],
'83d872c2': [
        (log,                           ('2.6: AriaDiscordantNote LegA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d378c273', 'AriaDiscordantNote.LegA.LightMap.2048')),
    ],
'd378c273': [
        (log,                           ('2.6: AriaDiscordantNote LegA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('83d872c2', 'AriaDiscordantNote.LegA.LightMap.1024')),
    ],
'e86b5691': [
        (log,                           ('2.6: AriaDiscordantNote LegA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d3da0d5a', 'AriaDiscordantNote.LegA.MaterialMap.2048')),
    ],
'd3da0d5a': [
        (log,                           ('2.6: AriaDiscordantNote LegA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('e86b5691', 'AriaDiscordantNote.LegA.MaterialMap.1024')),
    ],
'8a7ae9c2': [(log, ('3.0: AriaDiscordantNote Hair IB Hash',)), (add_ib_check_if_missing,)],
'697c6c6a': [
        (log, ('3.0: AriaDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'6a495335': [
        (log, ('3.0: AriaDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'bcde58e5': [
        (log, ('3.0: AriaDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'8183ba3e': [
        (log, ('3.0: AriaDiscordantNote Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: AriaDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'2d1b7798': [(log, ('3.0: AriaDiscordantNote Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'1ece9f27': [
        (log, ('3.0: AriaDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'f84d5a49': [
        (log, ('3.0: AriaDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'2046d6f4': [
        (log, ('3.0: AriaDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'56eaff1c': [
        (log, ('3.0: AriaDiscordantNote Body VB Hash',)),
        (add_section_if_missing, ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
    ],
'12e0707a': [
        (log, ('3.0: AriaDiscordantNote Leg VB Hash',)),
        (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
'71977be5': [
        (log, ('3.0: AriaDiscordantNote Leg VB Hash',)),
        (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
'a7682298': [
        (log, ('3.0: AriaDiscordantNote Leg VB Hash',)),
        (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
'c0b0db5f': [(log, ('3.0: AriaDiscordantNote Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'cd444ce7': [
        (log, ('3.0: AriaDiscordantNote Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'b7d38cbb': [
        (log, ('3.0: AriaDiscordantNote Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'3b2d89e0': [
        (log, ('3.0: AriaDiscordantNote Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'1b2ae01f': [
        (log, ('3.0: AriaDiscordantNote Eyebrow TEX Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'27966f80': [(log, ('3.0: AriaDiscordantNote Face IB Hash',)), (add_ib_check_if_missing,)],
'fc43d4db': [
        (log, ('3.0: AriaDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'c651479c': [
        (log, ('3.0: AriaDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'39d7123a': [
        (log, ('3.0: AriaDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'3f418ccb': [
        (log, ('3.0: AriaDiscordantNote Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
    ],
'16979e4f': [(log, ('3.0: AriaDiscordantNote Weapon IB Hash',)), (add_ib_check_if_missing,)],
'380bb1a8': [
        (log, ('3.0: AriaDiscordantNote Weapon VB Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'adbfa4c4': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'71966d3f': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'328592b5': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: AriaDiscordantNote Hair TEX Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
    ],
'6146195d': [
        (log, ('3.0: AriaDiscordantNote Eyebrow TEX Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'2c3a5d8d': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'4a0da1fb': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'825f0b0b': [
        (log, ('3.0: AriaDiscordantNote Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
    ],
'80b5aa5e': [
        (log, ('3.0: AriaDiscordantNote Leg VB Hash',)),
        (add_section_if_missing, ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AriaDiscordantNote',
    'game_versions': ['2.6', '2.7'],
}
