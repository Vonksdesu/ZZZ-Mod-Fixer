"""
AriaAgentDiscordantNote Character Hash Commands
ZZZ Mod Fixer v2.6
Game Version: 2.6 - 3.2
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

        # ==================== Hair Component ====================
        '1173ff78': [
            (log,                             ('2.6: AriaAgentDiscordantNote Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5bbaca72': [
            (log,                             ('2.6: AriaAgentDiscordantNote Hair Draw VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        '42a4622f': [
            (log,                             ('2.6: AriaAgentDiscordantNote Hair Position VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        '23629315': [
            (log,                             ('2.6: AriaAgentDiscordantNote Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        '468e532f': [
            (log,                             ('2.6: AriaAgentDiscordantNote Hair Blend VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        'be70c507': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0aec120', 'AriaAgentDiscordantNote.HairB.Diffuse.1024')),
        ],
        'f0aec120': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be70c507', 'AriaAgentDiscordantNote.HairB.Diffuse.2048')),
        ],
        '41124010': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e2e56b3', 'AriaAgentDiscordantNote.HairB.LightMap.1024')),
        ],
        '9e2e56b3': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('41124010', 'AriaAgentDiscordantNote.HairB.LightMap.2048')),
        ],
        '01087a99': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('002360e1', 'AriaAgentDiscordantNote.HairB.MaterialMap.1024')),
        ],
        '002360e1': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01087a99', 'AriaAgentDiscordantNote.HairB.MaterialMap.2048')),
        ],
        'fb2c3964': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fc3231cd', 'AriaAgentDiscordantNote.HairA.Diffuse.1024')),
        ],
        'fc3231cd': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb2c3964', 'AriaAgentDiscordantNote.HairA.Diffuse.2048')),
        ],
        '21aac04f': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('380fbecb', 'AriaAgentDiscordantNote.HairA.LightMap.1024')),
        ],
        '380fbecb': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('21aac04f', 'AriaAgentDiscordantNote.HairA.LightMap.2048')),
        ],
        'e1ccfca4': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8f3cfb68', 'AriaAgentDiscordantNote.HairA.MaterialMap.1024')),
        ],
        '8f3cfb68': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1ccfca4', 'AriaAgentDiscordantNote.HairA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA, BodyA, DecorationA and WeaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgentDiscordantNote.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgentDiscordantNote.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgentDiscordantNote.DecorationA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgentDiscordantNote.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6: AriaAgentDiscordantNote HairA, BodyA, DecorationA and WeaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgentDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgentDiscordantNote.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgentDiscordantNote.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgentDiscordantNote.DecorationA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgentDiscordantNote.WeaponA.NormalMap.2048')),
        ],

        # ==================== Body Component ====================
        '046400d3': [
            (log,                             ('2.6: AriaAgentDiscordantNote Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a28a907a': [
            (log,                             ('2.6: AriaAgentDiscordantNote Body Draw VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        '608bff86': [
            (log,                             ('2.6: AriaAgentDiscordantNote Body Position VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        'b019dae2': [
            (log,                             ('2.6: AriaAgentDiscordantNote Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        '7c85654d': [
            (log,                             ('2.6: AriaAgentDiscordantNote Body Blend VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        '282c7753': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1bf43198', 'AriaAgentDiscordantNote.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1bf43198', 'AriaAgentDiscordantNote.DecorationA.Diffuse.1024')),
        ],
        '1bf43198': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('282c7753', 'AriaAgentDiscordantNote.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('282c7753', 'AriaAgentDiscordantNote.DecorationA.Diffuse.2048')),
        ],
        '263f8811': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('99f9094c', 'AriaAgentDiscordantNote.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('99f9094c', 'AriaAgentDiscordantNote.DecorationA.LightMap.1024')),
        ],
        '99f9094c': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('263f8811', 'AriaAgentDiscordantNote.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('263f8811', 'AriaAgentDiscordantNote.DecorationA.LightMap.2048')),
        ],
        'f5b45cc2': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab411caa', 'AriaAgentDiscordantNote.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ab411caa', 'AriaAgentDiscordantNote.DecorationA.MaterialMap.1024')),
        ],
        'ab411caa': [
            (log,                             ('2.6: AriaAgentDiscordantNote BodyA and DecorationA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgentDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f5b45cc2', 'AriaAgentDiscordantNote.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5b45cc2', 'AriaAgentDiscordantNote.DecorationA.MaterialMap.2048')),
        ],

        # ==================== Decoration Component ====================
        'ac9c2ebb': [
            (log,                             ('2.6: AriaAgentDiscordantNote Decoration IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8e2e89dc': [
            (log,                             ('2.6: AriaAgentDiscordantNote Decoration Draw VB Hash',)),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
        ],
        '09998ea7': [
            (log,                             ('2.6: AriaAgentDiscordantNote Decoration Position VB Hash',)),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
        ],
        '9f6fa4fe': [
            (log,                             ('2.6: AriaAgentDiscordantNote Decoration Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
        ],
        '624d99aa': [
            (log,                             ('2.6: AriaAgentDiscordantNote Decoration Blend VB Hash',)),
            (add_section_if_missing,          ('ac9c2ebb', 'AriaAgentDiscordantNote.Decoration.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        'ffa703e8': [
            (log,                             ('2.6: AriaAgentDiscordantNote Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f0c79e51': [
            (log,                             ('2.6: AriaAgentDiscordantNote Face Draw VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],
        'b62f2772': [
            (log,                             ('2.6: AriaAgentDiscordantNote Face Position VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],
        '9772ccda': [
            (log,                             ('2.6: AriaAgentDiscordantNote Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e619a2b8',)),
        ],
        'e619a2b8': [
            (log,                             ('3.2: AriaAgentDiscordantNote Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ea540ea2': [
            (log,                             ('2.6: AriaAgentDiscordantNote Face Blend VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],
        '6b11a215': [
            (log,                             ('2.6: AriaAgentDiscordantNote FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28466273', 'AriaAgentDiscordantNote.FaceA.Diffuse.1024')),
        ],
        '28466273': [
            (log,                             ('2.6: AriaAgentDiscordantNote FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgentDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b11a215', 'AriaAgentDiscordantNote.FaceA.Diffuse.2048')),
        ],

        # ==================== Eye Component ====================
        'db7c8d25': [
            (log,                             ('2.6: AriaAgentDiscordantNote Eye IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '390a4a23': [
            (log,                             ('2.6: AriaAgentDiscordantNote Eye Draw VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
        ],
        'cf12b575': [
            (log,                             ('2.6: AriaAgentDiscordantNote Eye Position VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
        ],
        '22b99744': [
            (log,                             ('2.6: AriaAgentDiscordantNote Eye Texcoord VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
        ],
        '71fabd1a': [
            (log,                             ('2.6: AriaAgentDiscordantNote Eye Blend VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgentDiscordantNote.Eye.IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon Component ====================
        '62cc8d20': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '380bb1a8': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
        ],
        'adbfa4c4': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2c3a5d8d', 'AriaAgentDiscordantNote.WeaponA.Diffuse.1024')),
        ],
        '2c3a5d8d': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('adbfa4c4', 'AriaAgentDiscordantNote.WeaponA.Diffuse.2048')),
        ],
        '71966d3f': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a0da1fb', 'AriaAgentDiscordantNote.WeaponA.LightMap.1024')),
        ],
        '4a0da1fb': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('71966d3f', 'AriaAgentDiscordantNote.WeaponA.LightMap.2048')),
        ],
        '328592b5': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('825f0b0b', 'AriaAgentDiscordantNote.WeaponA.MaterialMap.1024')),
        ],
        '825f0b0b': [
            (log,                             ('2.6: AriaAgentDiscordantNote Weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgentDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('328592b5', 'AriaAgentDiscordantNote.WeaponA.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AriaAgentDiscordantNote',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}