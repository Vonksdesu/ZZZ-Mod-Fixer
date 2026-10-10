"""
AriaCutenessLoading Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns AriaCutenessLoading's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '8a7ae9c2': [
            (log,                             ('3.2: AriaCutenessLoading Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '697c6c6a': [
            (log,                             ('3.2: AriaCutenessLoading Hair Draw VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
        ],
        '6a495335': [
            (log,                             ('3.2: AriaCutenessLoading Hair Position VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
        ],
        'bcde58e5': [
            (log,                             ('3.2: AriaCutenessLoading Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
        ],
        '8183ba3e': [
            (log,                             ('3.2: AriaCutenessLoading Hair Blend VB Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
        ],
        'a572a368': [
            (log,                             ('3.2: AriaCutenessLoading HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc18e71c', 'AriaCutenessLoading.HairA.Diffuse.1024')),
        ],
        'dc18e71c': [
            (log,                             ('3.2: AriaCutenessLoading HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a572a368', 'AriaCutenessLoading.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.2: AriaCutenessLoading HairA, BodyA, LegA and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AriaCutenessLoading.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaCutenessLoading.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaCutenessLoading.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AriaCutenessLoading.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.2: AriaCutenessLoading HairA, BodyA, LegA and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaCutenessLoading.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaCutenessLoading.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaCutenessLoading.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AriaCutenessLoading.weaponA.NormalMap.2048')),
        ],
        '34c4faaa': [
            (log,                             ('3.2: AriaCutenessLoading HairA and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34583b2b', 'AriaCutenessLoading.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('34583b2b', 'AriaCutenessLoading.LegA.LightMap.1024')),
        ],
        '34583b2b': [
            (log,                             ('3.2: AriaCutenessLoading HairA and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34c4faaa', 'AriaCutenessLoading.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('34c4faaa', 'AriaCutenessLoading.LegA.LightMap.2048')),
        ],
        '4309b48e': [
            (log,                             ('3.2: AriaCutenessLoading HairA and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e32c606c', 'AriaCutenessLoading.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e32c606c', 'AriaCutenessLoading.LegA.MaterialMap.1024')),
        ],
        'e32c606c': [
            (log,                             ('3.2: AriaCutenessLoading HairA and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8a7ae9c2', 'AriaCutenessLoading.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4309b48e', 'AriaCutenessLoading.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4309b48e', 'AriaCutenessLoading.LegA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '2d1b7798': [
            (log,                             ('3.2: AriaCutenessLoading HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4a05fb84': [
            (log,                             ('3.2: AriaCutenessLoading HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('2d1b7798', 'AriaCutenessLoading.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'e010f06b': [
            (log,                             ('3.2: AriaCutenessLoading HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('2d1b7798', 'AriaCutenessLoading.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '5a62da45': [
            (log,                             ('3.2: AriaCutenessLoading HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('2d1b7798', 'AriaCutenessLoading.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '28f97cf3': [
            (log,                             ('3.2: AriaCutenessLoading HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('2d1b7798', 'AriaCutenessLoading.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '175a0c0a': [
            (log,                             ('3.2: AriaCutenessLoading Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '39aa6fb1': [
            (log,                             ('3.2: AriaCutenessLoading Body Draw VB Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
        ],
        '0f807bb9': [
            (log,                             ('3.2: AriaCutenessLoading Body Position VB Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
        ],
        '0e41a5a0': [
            (log,                             ('3.2: AriaCutenessLoading Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
        ],
        '74dfb803': [
            (log,                             ('3.2: AriaCutenessLoading Body Blend VB Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
        ],
        '6d0ce8c7': [
            (log,                             ('3.2: AriaCutenessLoading BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('52d90d4e', 'AriaCutenessLoading.BodyA.Diffuse.1024')),
        ],
        '52d90d4e': [
            (log,                             ('3.2: AriaCutenessLoading BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d0ce8c7', 'AriaCutenessLoading.BodyA.Diffuse.2048')),
        ],
        '6193ed20': [
            (log,                             ('3.2: AriaCutenessLoading BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c534187b', 'AriaCutenessLoading.BodyA.LightMap.1024')),
        ],
        'c534187b': [
            (log,                             ('3.2: AriaCutenessLoading BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6193ed20', 'AriaCutenessLoading.BodyA.LightMap.2048')),
        ],
        'a9bf33e2': [
            (log,                             ('3.2: AriaCutenessLoading BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e323c61a', 'AriaCutenessLoading.BodyA.MaterialMap.1024')),
        ],
        'e323c61a': [
            (log,                             ('3.2: AriaCutenessLoading BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('175a0c0a', 'AriaCutenessLoading.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9bf33e2', 'AriaCutenessLoading.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '73976aee': [
            (log,                             ('3.2: AriaCutenessLoading Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f678c8e5': [
            (log,                             ('3.2: AriaCutenessLoading Leg Draw VB Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
        ],
        '14ab176f': [
            (log,                             ('3.2: AriaCutenessLoading Leg Position VB Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
        ],
        '1f60e6f6': [
            (log,                             ('3.2: AriaCutenessLoading Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
        ],
        '1db87491': [
            (log,                             ('3.2: AriaCutenessLoading Leg Blend VB Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
        ],
        'e227c76b': [
            (log,                             ('3.2: AriaCutenessLoading LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef6c7cf7', 'AriaCutenessLoading.LegA.Diffuse.1024')),
        ],
        'ef6c7cf7': [
            (log,                             ('3.2: AriaCutenessLoading LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('73976aee', 'AriaCutenessLoading.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e227c76b', 'AriaCutenessLoading.LegA.Diffuse.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'c0b0db5f': [
            (log,                             ('3.2: AriaCutenessLoading Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cd444ce7': [
            (log,                             ('3.2: AriaCutenessLoading Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'f756dfa0': [
            (log,                             ('3.2: AriaCutenessLoading Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'aeeeaa7f': [
            (log,                             ('3.2: AriaCutenessLoading Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3b2d89e0': [
            (log,                             ('3.2: AriaCutenessLoading Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '1b2ae01f': [
            (log,                             ('3.2: AriaCutenessLoading EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6146195d', 'AriaCutenessLoading.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6146195d', 'AriaCutenessLoading.FaceA.Diffuse.1024')),
        ],
        '6146195d': [
            (log,                             ('3.2: AriaCutenessLoading EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c0b0db5f', 'AriaCutenessLoading.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1b2ae01f', 'AriaCutenessLoading.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1b2ae01f', 'AriaCutenessLoading.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '27966f80': [
            (log,                             ('3.2: AriaCutenessLoading Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fc43d4db': [
            (log,                             ('3.2: AriaCutenessLoading Face Draw VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
        ],
        'c651479c': [
            (log,                             ('3.2: AriaCutenessLoading Face Position VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
        ],
        'c493b91c': [
            (log,                             ('3.2: AriaCutenessLoading Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3f418ccb': [
            (log,                             ('3.2: AriaCutenessLoading Face Blend VB Hash',)),
            (add_section_if_missing,          ('27966f80', 'AriaCutenessLoading.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        '16979e4f': [
            (log,                             ('3.2: AriaCutenessLoading weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f797551b': [
            (log,                             ('3.2: AriaCutenessLoading weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ec4228a', 'AriaCutenessLoading.weaponA.Diffuse.1024')),
        ],
        '5ec4228a': [
            (log,                             ('3.2: AriaCutenessLoading weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f797551b', 'AriaCutenessLoading.weaponA.Diffuse.2048')),
        ],
        '6c620c16': [
            (log,                             ('3.2: AriaCutenessLoading weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e180bd1c', 'AriaCutenessLoading.weaponA.LightMap.1024')),
        ],
        'e180bd1c': [
            (log,                             ('3.2: AriaCutenessLoading weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c620c16', 'AriaCutenessLoading.weaponA.LightMap.2048')),
        ],
        '9e9d8560': [
            (log,                             ('3.2: AriaCutenessLoading weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('777472dd', 'AriaCutenessLoading.weaponA.MaterialMap.1024')),
        ],
        '777472dd': [
            (log,                             ('3.2: AriaCutenessLoading weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('16979e4f', 'AriaCutenessLoading.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e9d8560', 'AriaCutenessLoading.weaponA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AriaCutenessLoading',
    'game_versions': ['3.2'],
}
