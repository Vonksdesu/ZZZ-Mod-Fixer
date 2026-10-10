"""
Aria Character Hash Commands
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
    Returns Aria's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '8a7ae9c2': [
            (log,                             ('2.6: Aria Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '697c6c6a': [
            (log,                             ('2.6: Aria Hair Draw VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
        ],
        '6a495335': [
            (log,                             ('2.6: Aria Hair Position VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
        ],
        'bcde58e5': [
            (log,                             ('2.6: Aria Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
        ],
        '8183ba3e': [
            (log,                             ('2.6: Aria Hair Blend VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
        ],
        'a572a368': [
            (log,                             ('2.6: Aria HairA and LegA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc18e71c', 'Aria.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('dc18e71c', 'Aria.LegA.Diffuse.1024')),
        ],
        'dc18e71c': [
            (log,                             ('2.6: Aria HairA and LegA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a572a368', 'Aria.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('a572a368', 'Aria.LegA.Diffuse.2048')),
        ],
        '34c4faaa': [
            (log,                             ('2.6: Aria HairA and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34583b2b', 'Aria.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('34583b2b', 'Aria.LegA.LightMap.1024')),
        ],
        '34583b2b': [
            (log,                             ('2.6: Aria HairA and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34c4faaa', 'Aria.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('34c4faaa', 'Aria.LegA.LightMap.2048')),
        ],
        '4309b48e': [
            (log,                             ('2.6: Aria HairA and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e32c606c', 'Aria.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e32c606c', 'Aria.LegA.MaterialMap.1024')),
        ],
        'e32c606c': [
            (log,                             ('2.6: Aria HairA and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4309b48e', 'Aria.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4309b48e', 'Aria.LegA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6: Aria HairA, BodyA, LegA and WeaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Aria.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Aria.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Aria.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Aria.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6: Aria HairA, BodyA, LegA and WeaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'Aria.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Aria.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Aria.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Aria.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Aria.WeaponA.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '2d1b7798': [
            (log,                             ('2.6: Aria Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        '8c5b553a': [
            (log,                             ('2.6: Aria Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '72cea90b': [
            (log,                             ('2.6: Aria Body Draw VB Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
        ],
        'be8eacb4': [
            (log,                             ('2.6: Aria Body Position VB Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
        ],
        '7bdc71a8': [
            (log,                             ('2.6: Aria Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
        ],
        'a08b2a67': [
            (log,                             ('2.6: Aria Body Blend VB Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
        ],
        'a33c5da6': [
            (log,                             ('2.6: Aria BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fda652ce', 'Aria.BodyA.Diffuse.1024')),
        ],
        'fda652ce': [
            (log,                             ('2.6: Aria BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a33c5da6', 'Aria.BodyA.Diffuse.2048')),
        ],
        'ab389fa7': [
            (log,                             ('2.6: Aria BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f575fc9d', 'Aria.BodyA.LightMap.1024')),
        ],
        'f575fc9d': [
            (log,                             ('2.6: Aria BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab389fa7', 'Aria.BodyA.LightMap.2048')),
        ],
        '40eff501': [
            (log,                             ('2.6: Aria BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aaec2e94', 'Aria.BodyA.MaterialMap.1024')),
        ],
        'aaec2e94': [
            (log,                             ('2.6: Aria BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('8c5b553a', 'Aria.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('40eff501', 'Aria.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        'e6ff7471': [
            (log,                             ('2.6: Aria Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '964f2afe': [
            (log,                             ('2.6: Aria Leg Draw VB Hash',)),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
        ],
        'bd9b3d7d': [
            (log,                             ('2.6: Aria Leg Position VB Hash',)),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
        ],
        '2ff0ce5d': [
            (log,                             ('2.6: Aria Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
        ],
        '3060206a': [
            (log,                             ('2.6: Aria Leg Blend VB Hash',)),
            (add_section_if_missing,          ('e6ff7471', 'Aria.Leg.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        'c0b0db5f': [
            (log,                             ('2.6: Aria Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cd444ce7': [
            (log,                             ('2.6: Aria Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'b7d38cbb': [
            (log,                             ('2.6: Aria Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('aeeeaa7f',)),
        ],
        'aeeeaa7f': [
            (log,                             ('3.2: Aria Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3b2d89e0': [
            (log,                             ('2.6: Aria Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '27966f80': [
            (log,                             ('2.6: Aria Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fc43d4db': [
            (log,                             ('2.6: Aria Face Draw VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
        ],
        'c651479c': [
            (log,                             ('2.6: Aria Face Position VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
        ],
        '39d7123a': [
            (log,                             ('2.6: Aria Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c493b91c',)),
        ],
        'c493b91c': [
            (log,                             ('3.2: Aria Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3f418ccb': [
            (log,                             ('2.6: Aria Face Blend VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
        ],
        '1b2ae01f': [
            (log,                             ('2.6: Aria FaceA and EyebrowA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6146195d', 'Aria.FaceA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6146195d', 'Aria.EyebrowA.Diffuse.1024')),
        ],
        '6146195d': [
            (log,                             ('2.6: Aria FaceA and EyebrowA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('27966f80', 'Aria.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0b0db5f', 'Aria.Eyebrow.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1b2ae01f', 'Aria.FaceA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1b2ae01f', 'Aria.EyebrowA.Diffuse.2048')),
        ],

        # ==================== Weapon Component ====================
        '16979e4f': [
            (log,                             ('2.6: Aria Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '380bb1a8': [
            (log,                             ('2.6: Aria Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
        ],
        'f797551b': [
            (log,                             ('2.6: Aria Weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ec4228a', 'Aria.WeaponA.Diffuse.1024')),
        ],
        '6c620c16': [
            (log,                             ('2.6: Aria Weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e180bd1c', 'Aria.WeaponA.LightMap.1024')),
        ],
        '9e9d8560': [
            (log,                             ('2.6: Aria Weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('777472dd', 'Aria.WeaponA.MaterialMap.1024')),
        ],
        '5ec4228a': [
            (log,                             ('2.6: Aria Weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f797551b', 'Aria.WeaponA.Diffuse.2048')),
        ],
        'e180bd1c': [
            (log,                             ('2.6: Aria Weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c620c16', 'Aria.WeaponA.LightMap.2048')),
        ],
        '777472dd': [
            (log,                             ('2.6: Aria Weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'Aria.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e9d8560', 'Aria.WeaponA.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Aria',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}