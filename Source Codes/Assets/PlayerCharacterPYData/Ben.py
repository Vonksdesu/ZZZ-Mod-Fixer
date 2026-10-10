"""
Ben Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
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

        # ==================== Body Component ====================
        '94288cca': [
            (log,                             ('2.2 - 3.2: Ben Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dfd93ee5': [
            (log,                             ('2.2 - 3.2: Ben Body Draw VB Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        ],
        'b4db1979': [
            (log,                             ('2.2 - 3.2: Ben Body Position VB Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        ],
        'c7b58675': [
            (log,                             ('2.2 - 3.2: Ben Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        ],
        'a2f79d33': [
            (log,                             ('1.0: Ben Body Blend Hash (OLD)',)),
            (update_hash,                     ('21dd67a7',)),
        ],
        '21dd67a7': [
            (log,                             ('2.2 - 3.2: Ben Body Blend VB Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
        ],
        '0313ed95': [
            (log,                             ('2.2 - 3.2: Ben BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d8dc4645', 'Ben.BodyA.Diffuse.1024')),
        ],
        'd8dc4645': [
            (log,                             ('2.2 - 3.2: Ben BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0313ed95', 'Ben.BodyA.Diffuse.2048')),
        ],
        '1b79fa5c': [
            (log,                             ('1.0: Ben BodyA NormalMap 2048p Hash (LEGACY)',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'f6ecc618': [
            (log,                             ('1.0: Ben BodyA NormalMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '894ea737': [
            (log,                             ('1.0: Ben FaceA NormalMap 2048p Hash (LEGACY)',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ba809960': [
            (log,                             ('1.0: Ben FaceA NormalMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Ben FaceA, BodyA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Ben.FaceA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Ben.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Ben.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Ben FaceA, BodyA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Ben.FaceA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Ben.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Ben.weapon.NormalMap.2048')),
        ],
        'cb84ed5e': [
            (log,                             ('1.0: Ben BodyA LightMap 2048p Hash (OLD)',)),
            (update_hash,                     ('d27a8f6b',)),
        ],
        'd27a8f6b': [
            (log,                             ('2.2 - 3.2: Ben BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('9a724295', '6a80c2d8'), 'Ben.BodyA.LightMap.1024')),
        ],
        '6a80c2d8': [
            (log,                             ('1.0: Ben BodyA LightMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('d27a8f6b',)),
        ],
        '9a724295': [
            (log,                             ('2.2 - 3.2: Ben BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d27a8f6b', 'cb84ed5e'), 'Ben.BodyA.LightMap.2048')),
        ],
        '3f4f6bc0': [
            (log,                             ('1.0: Ben BodyA MaterialMap 2048p Hash (OLD)',)),
            (update_hash,                     ('2edd6f62',)),
        ],
        '2edd6f62': [
            (log,                             ('2.2 - 3.2: Ben BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('3678fad4', 'decc28c5'), 'Ben.BodyA.MaterialMap.1024')),
        ],
        'decc28c5': [
            (log,                             ('1.0: Ben BodyA MaterialMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('2edd6f62',)),
        ],
        '3678fad4': [
            (log,                             ('2.2 - 3.2: Ben BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('94288cca', 'Ben.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2edd6f62', '3f4f6bc0'), 'Ben.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '9c4f1a9a': [
            (log,                             ('2.2 - 3.2: Ben Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7e77201a': [
            (log,                             ('2.2 - 3.2: Ben Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        ],
        '893553e3': [
            (log,                             ('2.2: Ben Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        ],
        '18d26bd2': [
            (log,                             ('2.2 - 3.2: Ben Face Blend VB Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
        ],
        '00002f2c': [
            (log,                             ('2.2 - 3.2: Ben FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d83daba', 'Ben.FaceA.Diffuse.1024')),
        ],
        '8d83daba': [
            (log,                             ('2.2 - 3.2: Ben FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('00002f2c', 'Ben.FaceA.Diffuse.2048')),
        ],
        'cc195dc5': [
            (log,                             ('1.0: Ben FaceA LightMap 2048p Hash (OLD)',)),
            (update_hash,                     ('2fa5ffa7',)),
        ],
        '2fa5ffa7': [
            (log,                             ('2.2 - 3.2: Ben FaceA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('9372e123', '1439d2b9'), 'Ben.FaceA.LightMap.1024')),
        ],
        '1439d2b9': [
            (log,                             ('1.0: Ben FaceA LightMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('2fa5ffa7',)),
        ],
        '9372e123': [
            (log,                             ('2.2 - 3.2: Ben FaceA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2fa5ffa7', 'cc195dc5'), 'Ben.FaceA.LightMap.2048')),
        ],
        '0bbceea0': [
            (log,                             ('1.0: Ben FaceA MaterialMap 2048p Hash (OLD)',)),
            (update_hash,                     ('12e5120e',)),
        ],
        '12e5120e': [
            (log,                             ('2.2 - 3.2: Ben FaceA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('dd8c0b3a', 'd665246d'), 'Ben.FaceA.MaterialMap.1024')),
        ],
        'd665246d': [
            (log,                             ('1.0: Ben FaceA MaterialMap 1024p Hash (LEGACY)',)),
            (update_hash,                     ('12e5120e',)),
        ],
        'dd8c0b3a': [
            (log,                             ('2.2 - 3.2: Ben FaceA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9c4f1a9a', 'Ben.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0bbceea0', '12e5120e'), 'Ben.FaceA.MaterialMap.2048')),
        ],

        # ==================== Weapon Component ====================
        '4e4f3440': [
            (log,                             ('2.2 - 3.2: Ben weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fcc2accc': [
            (log,                             ('2.2 - 3.2: Ben weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
        ],
        '3c5c930c': [
            (log,                             ('2.2 - 3.2: Ben weapon Position VB Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
        ],
        '89932f55': [
            (log,                             ('2.2 - 3.2: Ben weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
        ],
        '7a0c8bf9': [
            (log,                             ('2.2 - 3.2: Ben weapon Blend VB Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
        ],
        'bd88580a': [
            (log,                             ('2.2 - 3.2: Ben weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb05197d', 'Ben.weapon.Diffuse.1024')),
        ],
        'fb05197d': [
            (log,                             ('2.2 - 3.2: Ben weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd88580a', 'Ben.weapon.Diffuse.2048')),
        ],
        '6fc3d991': [
            (log,                             ('2.2 - 3.2: Ben weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac04b14e', 'Ben.weapon.LightMap.1024')),
        ],
        'ac04b14e': [
            (log,                             ('2.2 - 3.2: Ben weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6fc3d991', 'Ben.weapon.LightMap.2048')),
        ],
        'beeef18a': [
            (log,                             ('2.2 - 3.2: Ben weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7eec482a', 'Ben.weapon.MaterialMap.1024')),
        ],
        '7eec482a': [
            (log,                             ('2.2 - 3.2: Ben weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4e4f3440', 'Ben.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('beeef18a', 'Ben.weapon.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Ben',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}

