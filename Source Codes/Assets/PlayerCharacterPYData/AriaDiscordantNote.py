"""
AriaDiscordantNote Character Hash Commands
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
    Returns AriaDiscordantNote's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '8a7ae9c2': [
            (log,                             ('2.6: AriaDiscordantNote Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '697c6c6a': [
            (log,                             ('2.6: AriaDiscordantNote Hair Draw VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        '6a495335': [
            (log,                             ('2.6: AriaDiscordantNote Hair Position VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        'bcde58e5': [
            (log,                             ('2.6: AriaDiscordantNote Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        '8183ba3e': [
            (log,                             ('2.6: AriaDiscordantNote Hair Blend VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
        ],
        'a34313c8': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d754c95b', 'AriaDiscordantNote.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d754c95b', 'AriaDiscordantNote.LegA.Diffuse.1024')),
        ],
        'd754c95b': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a34313c8', 'AriaDiscordantNote.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('a34313c8', 'AriaDiscordantNote.LegA.Diffuse.2048')),
        ],
        'd378c273': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('83d872c2', 'AriaDiscordantNote.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('83d872c2', 'AriaDiscordantNote.LegA.LightMap.1024')),
        ],
        '83d872c2': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d378c273', 'AriaDiscordantNote.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('d378c273', 'AriaDiscordantNote.LegA.LightMap.2048')),
        ],
        'd3da0d5a': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e86b5691', 'AriaDiscordantNote.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e86b5691', 'AriaDiscordantNote.LegA.MaterialMap.1024')),
        ],
        'e86b5691': [
            (log,                             ('2.6: AriaDiscordantNote HairA and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d3da0d5a', 'AriaDiscordantNote.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d3da0d5a', 'AriaDiscordantNote.LegA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6: AriaDiscordantNote HairA, BodyA, LegA and WeaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AriaDiscordantNote.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaDiscordantNote.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaDiscordantNote.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaDiscordantNote.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6: AriaDiscordantNote HairA, BodyA, LegA and WeaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaDiscordantNote.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaDiscordantNote.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaDiscordantNote.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaDiscordantNote.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaDiscordantNote.WeaponA.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '2d1b7798': [
            (log,                             ('2.6: AriaDiscordantNote Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        'c6bb960b': [
            (log,                             ('2.6: AriaDiscordantNote Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1ece9f27': [
            (log,                             ('2.6: AriaDiscordantNote Body Draw VB Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        'f84d5a49': [
            (log,                             ('2.6: AriaDiscordantNote Body Position VB Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        '2046d6f4': [
            (log,                             ('2.6: AriaDiscordantNote Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        '56eaff1c': [
            (log,                             ('2.6: AriaDiscordantNote Body Blend VB Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
        ],
        'a55f187e': [
            (log,                             ('2.6 -> 2.7: AriaDiscordantNote BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('677f73d9',)),
        ],
        '677f73d9': [
            (log,                             ('2.7: AriaDiscordantNote BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('303c63bc', '3c6bd181'), 'AriaDiscordantNote.BodyA.Diffuse.1024')),
        ],
        '3c6bd181': [
            (log,                             ('2.6 -> 2.7: AriaDiscordantNote BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('303c63bc',)),
        ],
        '303c63bc': [
            (log,                             ('2.7: AriaDiscordantNote BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('677f73d9', 'a55f187e'), 'AriaDiscordantNote.BodyA.Diffuse.2048')),
        ],
        'acee133c': [
            (log,                             ('2.6: AriaDiscordantNote BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a97204aa', 'AriaDiscordantNote.BodyA.LightMap.1024')),
        ],
        'a97204aa': [
            (log,                             ('2.6: AriaDiscordantNote BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('acee133c', 'AriaDiscordantNote.BodyA.LightMap.2048')),
        ],
        '6ac35f02': [
            (log,                             ('2.6: AriaDiscordantNote BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2418c407', 'AriaDiscordantNote.BodyA.MaterialMap.1024')),
        ],
        '2418c407': [
            (log,                             ('2.6: AriaDiscordantNote BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('c6bb960b', 'AriaDiscordantNote.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ac35f02', 'AriaDiscordantNote.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '923c64c0': [
            (log,                             ('2.6: AriaDiscordantNote Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '80b5aa5e': [
            (log,                             ('2.6: AriaDiscordantNote Leg Draw VB Hash',)),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        ],
        '12e0707a': [
            (log,                             ('2.6: AriaDiscordantNote Leg Position VB Hash',)),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        ],
        '71977be5': [
            (log,                             ('2.6: AriaDiscordantNote Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        ],
        'a7682298': [
            (log,                             ('2.6: AriaDiscordantNote Leg Blend VB Hash',)),
            (add_section_if_missing,          ('923c64c0', 'AriaDiscordantNote.Leg.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        'c0b0db5f': [
            (log,                             ('2.6: AriaDiscordantNote Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cd444ce7': [
            (log,                             ('2.6: AriaDiscordantNote Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'b7d38cbb': [
            (log,                             ('2.6: AriaDiscordantNote Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('aeeeaa7f',)),
        ],
        'aeeeaa7f': [
            (log,                             ('3.2: AriaDiscordantNote Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3b2d89e0': [
            (log,                             ('2.6: AriaDiscordantNote Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '1b2ae01f': [
            (log,                             ('2.6: AriaDiscordantNote FaceA and EyebrowA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6146195d', 'AriaDiscordantNote.FaceA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6146195d', 'AriaDiscordantNote.EyebrowA.Diffuse.1024')),
        ],
        '6146195d': [
            (log,                             ('2.6: AriaDiscordantNote FaceA and EyebrowA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaDiscordantNote.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1b2ae01f', 'AriaDiscordantNote.FaceA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1b2ae01f', 'AriaDiscordantNote.EyebrowA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '27966f80': [
            (log,                             ('2.6: AriaDiscordantNote Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fc43d4db': [
            (log,                             ('2.6: AriaDiscordantNote Face Draw VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],
        'c651479c': [
            (log,                             ('2.6: AriaDiscordantNote Face Position VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],
        '39d7123a': [
            (log,                             ('2.6: AriaDiscordantNote Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c493b91c',)),
        ],
        'c493b91c': [
            (log,                             ('3.2: AriaDiscordantNote Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3f418ccb': [
            (log,                             ('2.6: AriaDiscordantNote Face Blend VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaDiscordantNote.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon Component ====================
        '16979e4f': [
            (log,                             ('2.6: AriaDiscordantNote Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '380bb1a8': [
            (log,                             ('2.6: AriaDiscordantNote Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
        ],
        'adbfa4c4': [
            (log,                             ('2.6: AriaDiscordantNote Weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2c3a5d8d', 'AriaDiscordantNote.WeaponA.Diffuse.1024')),
        ],
        '2c3a5d8d': [
            (log,                             ('2.6: AriaDiscordantNote Weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('adbfa4c4', 'AriaDiscordantNote.WeaponA.Diffuse.2048')),
        ],
        '71966d3f': [
            (log,                             ('2.6: AriaDiscordantNote Weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a0da1fb', 'AriaDiscordantNote.WeaponA.LightMap.1024')),
        ],
        '4a0da1fb': [
            (log,                             ('2.6: AriaDiscordantNote Weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('71966d3f', 'AriaDiscordantNote.WeaponA.LightMap.2048')),
        ],
        '328592b5': [
            (log,                             ('2.6: AriaDiscordantNote Weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('825f0b0b', 'AriaDiscordantNote.WeaponA.MaterialMap.1024')),
        ],
        '825f0b0b': [
            (log,                             ('2.6: AriaDiscordantNote Weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaDiscordantNote.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('328592b5', 'AriaDiscordantNote.WeaponA.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AriaDiscordantNote',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}