"""
Aria Character Hash Commands
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
    Returns Aria's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'8c5b553a': [
        (log,                           ('2.6: Aria Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'27966f80': [
        (log,                           ('2.6: Aria Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'8a7ae9c2': [
        (log,                           ('2.6: Aria Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'e6ff7471': [
        (log,                           ('2.6: Aria Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === Aria Textures (FaceA) ===
'6146195d': [
        (log,                           ('2.6: Aria FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('1b2ae01f', 'Aria.FaceA.Diffuse.2048')),
    ],
'1b2ae01f': [
        (log,                           ('2.6: Aria FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('6146195d', 'Aria.FaceA.Diffuse.1024')),
    ],

# === Aria Textures (HairA) ===
'dc18e71c': [
        (log,                           ('2.6: Aria HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('a572a368', 'Aria.HairA.Diffuse.2048')),
    ],
'a572a368': [
        (log,                           ('2.6: Aria HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('dc18e71c', 'Aria.HairA.Diffuse.1024')),
    ],
'34583b2b': [
        (log,                           ('2.6: Aria HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('34c4faaa', 'Aria.HairA.LightMap.2048')),
    ],
'34c4faaa': [
        (log,                           ('2.6: Aria HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('34583b2b', 'Aria.HairA.LightMap.1024')),
    ],
'e32c606c': [
        (log,                           ('2.6: Aria HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('4309b48e', 'Aria.HairA.MaterialMap.2048')),
    ],
'4309b48e': [
        (log,                           ('2.6: Aria HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('e32c606c', 'Aria.HairA.MaterialMap.1024')),
    ],

# === Aria Textures (BodyA) ===
'fda652ce': [
        (log,                           ('2.6: Aria BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('a33c5da6', 'Aria.BodyA.Diffuse.2048')),
    ],
'a33c5da6': [
        (log,                           ('2.6: Aria BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('fda652ce', 'Aria.BodyA.Diffuse.1024')),
    ],
'f575fc9d': [
        (log,                           ('2.6: Aria BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('ab389fa7', 'Aria.BodyA.LightMap.2048')),
    ],
'ab389fa7': [
        (log,                           ('2.6: Aria BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('f575fc9d', 'Aria.BodyA.LightMap.1024')),
    ],
'aaec2e94': [
        (log,                           ('2.6: Aria BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('40eff501', 'Aria.BodyA.MaterialMap.2048')),
    ],
'40eff501': [
        (log,                           ('2.6: Aria BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('aaec2e94', 'Aria.BodyA.MaterialMap.1024')),
    ],
'6a495335': [
        (log, ('3.0: Aria Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
'bcde58e5': [
        (log, ('3.0: Aria Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
'8183ba3e': [
        (log, ('3.0: Aria Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Aria Hair TEX Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
'2d1b7798': [(log, ('3.0: Aria Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'72cea90b': [
        (log, ('3.0: Aria Body VB Hash',)),
        (add_section_if_missing, ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
    ],
'be8eacb4': [
        (log, ('3.0: Aria Body VB Hash',)),
        (add_section_if_missing, ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
    ],
'7bdc71a8': [
        (log, ('3.0: Aria Body VB Hash',)),
        (add_section_if_missing, ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
    ],
'a08b2a67': [
        (log, ('3.0: Aria Body VB Hash',)),
        (add_section_if_missing, ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
    ],
'bd9b3d7d': [
        (log, ('3.0: Aria Leg VB Hash',)),
        (add_section_if_missing, ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
    ],
'2ff0ce5d': [
        (log, ('3.0: Aria Leg VB Hash',)),
        (add_section_if_missing, ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
    ],
'3060206a': [
        (log, ('3.0: Aria Leg VB Hash',)),
        (add_section_if_missing, ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
    ],
'c0b0db5f': [(log, ('3.0: Aria Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'cd444ce7': [
        (log, ('3.0: Aria Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'b7d38cbb': [
        (log, ('3.0: Aria Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'3b2d89e0': [
        (log, ('3.0: Aria Eyebrow VB Hash',)),
        (add_section_if_missing, ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'c651479c': [
        (log, ('3.0: Aria Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
    ],
'39d7123a': [
        (log, ('3.0: Aria Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
    ],
'3f418ccb': [
        (log, ('3.0: Aria Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
    ],
'16979e4f': [(log, ('3.0: Aria Weapon IB Hash',)), (add_ib_check_if_missing,)],
'380bb1a8': [
        (log, ('3.0: Aria Weapon VB Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'f797551b': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'6c620c16': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'9e9d8560': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Aria Hair TEX Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
'5ec4228a': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'e180bd1c': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'777472dd': [
        (log, ('3.0: Aria Weapon TEX Hash',)),
        (add_section_if_missing, ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
    ],
'fc43d4db': [
        (log, ('3.0: Aria Face VB Hash',)),
        (add_section_if_missing, ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
    ],
'964f2afe': [
        (log, ('3.0: Aria Leg VB Hash',)),
        (add_section_if_missing, ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
    ],
'697c6c6a': [
        (log, ('3.0: Aria Hair VB Hash',)),
        (add_section_if_missing, ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Aria',
    'game_versions': ['2.6'],
}
