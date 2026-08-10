"""
Ben Character Hash Commands
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
    Returns Ben's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ===== IB HASHES =====
'9c4f1a9a': [(log, ('2.5: Ben Face IB Hash',)), (add_ib_check_if_missing,)],
'94288cca': [(log, ('2.5: Ben Body IB Hash',)), (add_ib_check_if_missing,)],

# ===== FACE TEXTURES =====
# Face Diffuse - unchanged between versions
'00002f2c': [
        (log,                           ('2.5: Ben FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# Face LightMap - v1.0 hash updated to v2.5
'cc195dc5': [
        (log,                           ('1.0: Ben FaceA LightMap Hash (OLD)',)),
        (update_hash,                   ('2fa5ffa7',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'2fa5ffa7': [
        (log,                           ('2.5: Ben FaceA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('9372e123', '1439d2b9'), 'Ben.HairA.LightMap.1024')),
    ],

'9372e123': [
        (log,                           ('2.5: Ben FaceA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('2fa5ffa7', 'cc195dc5'), 'Ben.HairA.LightMap.2048')),
    ],

# Face MaterialMap - v1.0 hash updated to v2.5
'0bbceea0': [
        (log,                           ('1.0: Ben FaceA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('12e5120e',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
'12e5120e': [
        (log,                           ('2.5: Ben FaceA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('dd8c0b3a', 'd665246d'), 'Ben.HairA.MaterialMap.1024')),
    ],

'dd8c0b3a': [
        (log,                           ('2.5: Ben FaceA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('0bbceea0', '12e5120e'), 'Ben.HairA.MaterialMap.2048')),
    ],

# Face NormalMap - shared with Body, new in v2.5
'ebac056e': [
        (log,                           ('2.5: Ben Face/Body NormalMap Hash',)),
        (add_section_if_missing,        ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],

# ===== BODY TEXTURES =====
# Body Blend - v1.0 hash updated to v2.5
'a2f79d33': [
        (log,                           ('1.0: Ben Body Blend Hash (OLD)',)),
        (update_hash,                   ('21dd67a7',)),
    ],
'21dd67a7': [
        (log,                           ('2.5: Ben Body Blend Hash',)),
    ],

# Body Diffuse - unchanged between versions
'0313ed95': [
        (log,                           ('2.5: Ben BodyA Diffuse Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],

# Body LightMap - v1.0 hash updated to v2.5
'cb84ed5e': [
        (log,                           ('1.0: Ben BodyA LightMap Hash (OLD)',)),
        (update_hash,                   ('d27a8f6b',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'd27a8f6b': [
        (log,                           ('2.5: Ben BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('9a724295', '6a80c2d8'), 'Ben.BodyA.LightMap.1024')),
    ],

'9a724295': [
        (log,                           ('2.5: Ben BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('d27a8f6b', 'cb84ed5e'), 'Ben.BodyA.LightMap.2048')),
    ],

# Body MaterialMap - v1.0 hash updated to v2.5
'3f4f6bc0': [
        (log,                           ('1.0: Ben BodyA MaterialMap Hash (OLD)',)),
        (update_hash,                   ('2edd6f62',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'2edd6f62': [
        (log,                           ('2.5: Ben BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('3678fad4', 'decc28c5'), 'Ben.BodyA.MaterialMap.1024')),
    ],

'3678fad4': [
        (log,                           ('2.5: Ben BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('2edd6f62', '3f4f6bc0'), 'Ben.BodyA.MaterialMap.2048')),
    ],

# ===== LEGACY HASHES (1.0 - REMOVED IN 2.5) =====
# These hashes existed in v1.0 mods but are no longer used in v2.5
# Keeping them for backward compatibility with old mods

# Legacy 1024p texture variants (removed - v2.5 only uses single resolution)
'8d83daba': [
        (log,                           ('1.0: Ben FaceA Diffuse 1024p Hash (LEGACY)',)),
        (update_hash,                   ('00002f2c',)),
    ],
'1439d2b9': [
        (log,                           ('1.0: Ben FaceA LightMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('2fa5ffa7',)),
    ],
'd665246d': [
        (log,                           ('1.0: Ben FaceA MaterialMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('12e5120e',)),
    ],
'894ea737': [
        (log,                           ('1.0: Ben FaceA NormalMap 2048p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ba809960': [
        (log,                           ('1.0: Ben FaceA NormalMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],

'd8dc4645': [
        (log,                           ('1.0: Ben BodyA Diffuse 1024p Hash (LEGACY)',)),
        (update_hash,                   ('0313ed95',)),
    ],
'6a80c2d8': [
        (log,                           ('1.0: Ben BodyA LightMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('d27a8f6b',)),
    ],
'decc28c5': [
        (log,                           ('1.0: Ben BodyA MaterialMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('2edd6f62',)),
    ],
'1b79fa5c': [
        (log,                           ('1.0: Ben BodyA NormalMap 2048p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'f6ecc618': [
        (log,                           ('1.0: Ben BodyA NormalMap 1024p Hash (LEGACY)',)),
        (update_hash,                   ('ebac056e',)),
    ],
'dfd93ee5': [
        (log, ('3.0: Ben Body VB Hash',)),
        (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'b4db1979': [
        (log, ('3.0: Ben Body VB Hash',)),
        (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'c7b58675': [
        (log, ('3.0: Ben Body VB Hash',)),
        (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'4e4f3440': [(log, ('3.0: Ben weapon IB Hash',)), (add_ib_check_if_missing,)],
'bd88580a': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'6fc3d991': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'beeef18a': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'89932f55': [
        (log, ('3.0: Ben weapon VB Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'7a0c8bf9': [
        (log, ('3.0: Ben weapon VB Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'7e77201a': [(log, ('3.0: Ben misc hash',)),],
'fcc2accc': [(log, ('3.0: Ben misc hash',)),],
'798adba3': [
        (log, ('3.0: Ben Body TEX Hash',)),
        (add_section_if_missing, ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
    ],
'fb05197d': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'ac04b14e': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'7eec482a': [
        (log, ('3.0: Ben weapon TEX Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'3c5c930c': [
        (log, ('3.0: Ben weapon VB Hash',)),
        (add_section_if_missing, ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
    ],
'18d26bd2': [
        (log, ('3.0: Ben Face VB Hash',)),
        (add_section_if_missing, ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ben',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
