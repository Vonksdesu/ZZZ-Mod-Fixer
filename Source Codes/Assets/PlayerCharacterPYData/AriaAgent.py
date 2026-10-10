"""
AriaAgent Character Hash Commands
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
    Returns AriaAgent's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '1173ff78': [
            (log,                             ('2.6: AriaAgent Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5bbaca72': [
            (log,                             ('2.6: AriaAgent Hair Draw VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
        ],
        '42a4622f': [
            (log,                             ('2.6: AriaAgent Hair Position VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
        ],
        '23629315': [
            (log,                             ('2.6: AriaAgent Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
        ],
        '468e532f': [
            (log,                             ('2.6: AriaAgent Hair Blend VB Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
        ],
        'be70c507': [
            (log,                             ('2.6: AriaAgent HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0aec120', 'AriaAgent.HairA.Diffuse.1024')),
        ],
        'f0aec120': [
            (log,                             ('2.6: AriaAgent HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be70c507', 'AriaAgent.HairA.Diffuse.2048')),
        ],
        '41124010': [
            (log,                             ('2.6: AriaAgent HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e2e56b3', 'AriaAgent.HairA.LightMap.1024')),
        ],
        '9e2e56b3': [
            (log,                             ('2.6: AriaAgent HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('41124010', 'AriaAgent.HairA.LightMap.2048')),
        ],
        '01087a99': [
            (log,                             ('2.6: AriaAgent HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('002360e1', 'AriaAgent.HairA.MaterialMap.1024')),
        ],
        '002360e1': [
            (log,                             ('2.6: AriaAgent HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01087a99', 'AriaAgent.HairA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6: AriaAgent HairA, BodyA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgent.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgent.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaAgent.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6: AriaAgent HairA, BodyA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1173ff78', 'AriaAgent.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgent.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgent.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaAgent.WeaponA.NormalMap.2048')),
        ],

        # ==================== Body Component ====================
        '046400d3': [
            (log,                             ('2.6: AriaAgent Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a28a907a': [
            (log,                             ('2.6: AriaAgent Body Draw VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
        ],
        '608bff86': [
            (log,                             ('2.6: AriaAgent Body Position VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
        ],
        'b019dae2': [
            (log,                             ('2.6: AriaAgent Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
        ],
        '7c85654d': [
            (log,                             ('2.6: AriaAgent Body Blend VB Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
        ],
        '859bb461': [
            (log,                             ('2.6: AriaAgent BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('702063c7', 'AriaAgent.BodyA.Diffuse.1024')),
        ],
        '702063c7': [
            (log,                             ('2.6: AriaAgent BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('859bb461', 'AriaAgent.BodyA.Diffuse.2048')),
        ],
        'ba534b39': [
            (log,                             ('2.6: AriaAgent BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a588ea59', 'AriaAgent.BodyA.LightMap.1024')),
        ],
        'a588ea59': [
            (log,                             ('2.6: AriaAgent BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ba534b39', 'AriaAgent.BodyA.LightMap.2048')),
        ],
        '14aa84e5': [
            (log,                             ('2.6: AriaAgent BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0a8badcd', 'AriaAgent.BodyA.MaterialMap.1024')),
        ],
        '0a8badcd': [
            (log,                             ('2.6: AriaAgent BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('046400d3', 'AriaAgent.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('14aa84e5', 'AriaAgent.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'ffa703e8': [
            (log,                             ('2.6: AriaAgent Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f0c79e51': [
            (log,                             ('2.6: AriaAgent Face Draw VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
        ],
        'b62f2772': [
            (log,                             ('2.6: AriaAgent Face Position VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
        ],
        '9772ccda': [
            (log,                             ('2.6: AriaAgent Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e619a2b8',)),
        ],
        'e619a2b8': [
            (log,                             ('3.2: AriaAgent Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ea540ea2': [
            (log,                             ('2.6: AriaAgent Face Blend VB Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
        ],
        '741d7c8f': [
            (log,                             ('2.6: AriaAgent FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6611eaa1', 'AriaAgent.FaceA.Diffuse.1024')),
        ],
        '6611eaa1': [
            (log,                             ('2.6: AriaAgent FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ffa703e8', 'AriaAgent.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('741d7c8f', 'AriaAgent.FaceA.Diffuse.2048')),
        ],

        # ==================== Eye Component ====================
        'db7c8d25': [
            (log,                             ('2.6: AriaAgent Eye IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '390a4a23': [
            (log,                             ('2.6: AriaAgent Eye Draw VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgent.Eye.IB', 'match_priority = 0\n')),
        ],
        'cf12b575': [
            (log,                             ('2.6: AriaAgent Eye Position VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgent.Eye.IB', 'match_priority = 0\n')),
        ],
        '22b99744': [
            (log,                             ('2.6: AriaAgent Eye Texcoord VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgent.Eye.IB', 'match_priority = 0\n')),
        ],
        '71fabd1a': [
            (log,                             ('2.6: AriaAgent Eye Blend VB Hash',)),
            (add_section_if_missing,          ('db7c8d25', 'AriaAgent.Eye.IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon Component ====================
        '62cc8d20': [
            (log,                             ('2.6: AriaAgent weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '380bb1a8': [
            (log,                             ('2.6: AriaAgent weapon Draw VB Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
        ],
        'f797551b': [
            (log,                             ('2.6: AriaAgent weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ec4228a', 'AriaAgent.WeaponA.Diffuse.1024')),
        ],
        '6c620c16': [
            (log,                             ('2.6: AriaAgent weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e180bd1c', 'AriaAgent.WeaponA.LightMap.1024')),
        ],
        '9e9d8560': [
            (log,                             ('2.6: AriaAgent weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('777472dd', 'AriaAgent.WeaponA.MaterialMap.1024')),
        ],
        '5ec4228a': [
            (log,                             ('2.6: AriaAgent weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f797551b', 'AriaAgent.WeaponA.Diffuse.2048')),
        ],
        'e180bd1c': [
            (log,                             ('2.6: AriaAgent weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c620c16', 'AriaAgent.WeaponA.LightMap.2048')),
        ],
        '777472dd': [
            (log,                             ('2.6: AriaAgent weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('62cc8d20', 'AriaAgent.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e9d8560', 'AriaAgent.WeaponA.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AriaAgent',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}