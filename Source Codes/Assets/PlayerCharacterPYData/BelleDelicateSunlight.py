"""
BelleDelicateSunlight Outfit Character Hash Commands
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
    Returns BelleDelicateSunlight's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'aa9ffb85': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '992d149f': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair Draw VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        '71d2bf80': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair Position VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'a5e62ece': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        '39ac6700': [
            (log,                             ('2.8 -> 3.0: BelleDelicateSunlight Hair Blend Hash',)),
            (update_hash,                     ('8f7ae834',)),
        ],
        '8f7ae834': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Hair Blend VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        '1ce58567': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleDelicateSunlight.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleDelicateSunlight.HeadwearA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleDelicateSunlight.NeckB.Diffuse.1024')),
        ],
        '08f04d95': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleDelicateSunlight.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleDelicateSunlight.HeadwearA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleDelicateSunlight.NeckB.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear, Neck, Torso, Leg, Red Knot Rope, Orange green ribbon, Earrings1, Earrings2, Panda headgear, Cat Ear Accessories, Pink badge, Orange green badge and glasses NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'BelleDelicateSunlight.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleDelicateSunlight.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleDelicateSunlight.NeckA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleDelicateSunlight.TorsoA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleDelicateSunlight.LegA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear, Neck, Torso and Leg NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleDelicateSunlight.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleDelicateSunlight.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleDelicateSunlight.NeckA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleDelicateSunlight.TorsoA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleDelicateSunlight.LegA.NormalMap.2048')),
        ],
        '7d562f53': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleDelicateSunlight.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleDelicateSunlight.HeadwearA.LightMap.1024')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleDelicateSunlight.NeckB.LightMap.1024')),
        ],
        'f44f330b': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleDelicateSunlight.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleDelicateSunlight.HeadwearA.LightMap.2048')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleDelicateSunlight.NeckB.LightMap.2048')),
        ],
        '34bdb036': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleDelicateSunlight.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleDelicateSunlight.HeadwearA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleDelicateSunlight.NeckB.MaterialMap.1024')),
        ],
        '7542ef4b': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair, Headwear and Neck MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleDelicateSunlight.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleDelicateSunlight.HeadwearA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleDelicateSunlight.NeckB.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '403eace9': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Headwear Component ====================
        '20d3a340': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2f828e6a': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
        ],
        '4dec8913': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Headwear Position VB Hash',)),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
        ],
        'cdd7fc8a': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
        ],
        'db7add33': [
            (log,                             ('2.8 -> 3.0: BelleDelicateSunlight Headwear Blend Hash',)),
            (update_hash,                     ('f18dd23f',)),
        ],
        'f18dd23f': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Neck Component ====================
        '62ed56cc': [
            (log,                             ('2.5 - 2.8: BelleDelicateSunlight Neck IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('d0627e1f',)),
        ],
        'd0627e1f': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Neck IB Hash (Model Change)',)),
            (add_ib_check_if_missing,),
        ],
        '4c215c73': [
            (log,                             ('2.5 - 2.8: BelleDelicateSunlight Neck Draw VB Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        'be75a4be': [
            (log,                             ('2.5 - 2.8: BelleDelicateSunlight Neck Position VB Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        'dd2b89aa': [
            (log,                             ('2.5 - 2.8: BelleDelicateSunlight Neck Texcoord VB Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        '3bd79a0b': [
            (log,                             ('2.5 - 2.8: BelleDelicateSunlight Neck Blend VB Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        '3f594476': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Neck Draw VB Hash',)),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        'e2ee9309': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Neck Position VB Hash',)),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        '2f7f6398': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Neck Texcoord VB Hash',)),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        '0a11b1d7': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Neck Blend VB Hash',)),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        ],
        'cac9fd5d': [
            (log,                             ('2.0 -> 2.1: BelleDelicateSunlight BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('da2bfe2f',)),
        ],
        'da2bfe2f': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck, Leg, Red Knot Rope and Earrings1 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ((("fdf0b49e", "0a2e0f42")), 'BelleDelicateSunlight.TorsoA.Diffuse.1024')),
            (multiply_section_if_missing,     ((("fdf0b49e", "0a2e0f42")), 'BelleDelicateSunlight.NeckA.Diffuse.1024')),
            (multiply_section_if_missing,     ((("fdf0b49e", "0a2e0f42")), 'BelleDelicateSunlight.LegA.Diffuse.1024')),
        ],
        '59218fac': [
            (log,                             ('2.0 -> 2.1: BelleDelicateSunlight BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('fdf0b49e',)),
        ],
        'fdf0b49e': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck and Leg Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ((("da2bfe2f", "cac9fd5d")), 'BelleDelicateSunlight.TorsoA.Diffuse.2048')),
            (multiply_section_if_missing,     ((("da2bfe2f", "cac9fd5d")), 'BelleDelicateSunlight.NeckA.Diffuse.2048')),
            (multiply_section_if_missing,     ((("da2bfe2f", "cac9fd5d")), 'BelleDelicateSunlight.LegA.Diffuse.2048')),
        ],
        '0a2e0f42': [
            (log,                             ('2.5: BelleDelicateSunlight Torso/Neck/Leg Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('da2bfe2f'), 'BelleDelicateSunlight.TorsoA.Diffuse.2048')),
            (multiply_section_if_missing,     (('da2bfe2f'), 'BelleDelicateSunlight.NeckA.Diffuse.2048')),
            (multiply_section_if_missing,     (('da2bfe2f'), 'BelleDelicateSunlight.LegA.Diffuse.2048')),
        ],
        '74f2fae3': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck, Leg, Red Knot Rope and Earrings1 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ((("93d94f22", "f8e4e93a")), 'BelleDelicateSunlight.TorsoA.LightMap.1024')),
            (multiply_section_if_missing,     ((("93d94f22", "f8e4e93a")), 'BelleDelicateSunlight.NeckA.LightMap.1024')),
            (multiply_section_if_missing,     ((("93d94f22", "f8e4e93a")), 'BelleDelicateSunlight.LegA.LightMap.1024')),
        ],
        '93d94f22': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck and Leg LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.TorsoA.LightMap.2048')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.NeckA.LightMap.2048')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.LegA.LightMap.2048')),
        ],
        'f8e4e93a': [
            (log,                             ('2.5: BelleDelicateSunlight Torso/Neck/Leg LightMap 1024p Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.TorsoA.LightMap.2048')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.NeckA.LightMap.2048')),
            (multiply_section_if_missing,     (('74f2fae3'), 'BelleDelicateSunlight.LegA.LightMap.2048')),
        ],
        '657402d0': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck, Leg, Red Knot Rope and Earrings1 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ((("b95c08fb", "93c5f5ff")), 'BelleDelicateSunlight.TorsoA.MaterialMap.1024')),
            (multiply_section_if_missing,     ((("b95c08fb", "93c5f5ff")), 'BelleDelicateSunlight.NeckA.MaterialMap.1024')),
            (multiply_section_if_missing,     ((("b95c08fb", "93c5f5ff")), 'BelleDelicateSunlight.LegA.MaterialMap.1024')),
        ],
        'b95c08fb': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Torso, Neck and Leg MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('860e1558', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.TorsoA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.NeckA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.LegA.MaterialMap.2048')),
        ],
        '93c5f5ff': [
            (log,                             ('2.5: BelleDelicateSunlight Torso/Neck/Leg MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.TorsoA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.NeckA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('657402d0'), 'BelleDelicateSunlight.LegA.MaterialMap.2048')),
        ],

        # ==================== Torso Component ====================
        '860e1558': [
            (log,                             ('2.5: Updating BelleDelicateSunlight Torso IB to d509bdd4',)),
            (update_hash,                     ('d509bdd4',)),
        ],
        'd509bdd4': [
            (log,                             ('2.5 - 3.2: BelleDelicateSunlight Torso IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '02c9dc4b': [
            (log,                             ('2.5: Updating BelleDelicateSunlight Torso draw_vb to 19e5f486',)),
            (update_hash,                     ('19e5f486',)),
        ],
        '19e5f486': [
            (log,                             ('2.5 - 3.2: BelleDelicateSunlight Torso Draw VB Hash',)),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
        ],
        '0b3c5e7c': [
            (log,                             ('2.5: Updating BelleDelicateSunlight Torso position_vb to 8a4e97cd',)),
            (update_hash,                     ('8a4e97cd',)),
        ],
        '8a4e97cd': [
            (log,                             ('2.5 - 3.2: BelleDelicateSunlight Torso Position VB Hash',)),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
        ],
        '862dc27a': [
            (log,                             ('2.5: Updating BelleDelicateSunlight Torso texcoord_vb to d761e076',)),
            (update_hash,                     ('d761e076',)),
        ],
        'd761e076': [
            (log,                             ('2.5 - 3.2: BelleDelicateSunlight Torso Texcoord VB Hash',)),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
        ],
        '01b0c8b6': [
            (log,                             ('2.5: Updating BelleDelicateSunlight Torso blend_vb to f3dedb50',)),
            (update_hash,                     ('f3dedb50',)),
        ],
        'f3dedb50': [
            (log,                             ('2.8 -> 3.0: BelleDelicateSunlight Torso Blend Hash',)),
            (update_hash,                     ('4d74d5e9',)),
        ],
        '4d74d5e9': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Torso Blend VB Hash',)),
            (add_section_if_missing,          ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
        ],

        # ==================== Leg Component ====================
        'bcc9e4e1': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '720d6a16': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Leg Draw VB Hash',)),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
        ],
        '42b88f48': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Leg Position VB Hash',)),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
        ],
        '82d0aadd': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
        ],
        'f53b2eba': [
            (log,                             ('2.8 -> 3.0: BelleDelicateSunlight Leg Blend Hash',)),
            (update_hash,                     ('922a7db6',)),
        ],
        '922a7db6': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Leg Blend VB Hash',)),
            (add_section_if_missing,          ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '9a9780a7': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Face IB Hash (Shared with Belle)',)),
            (add_ib_check_if_missing,),
        ],
        '04abceb5': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Face Draw VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
        ],
        '3eb95df2': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Face Position VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
        ],
        'ccc76aea': [
            (log,                             ('2.2 - 2.5: BelleDelicateSunlight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bcfc3326',)),
        ],
        'bcfc3326': [
            (log,                             ('2.6 - 2.7: BelleDelicateSunlight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
        ],
        '0c9a075b': [
            (log,                             ('2.5 -> 3.0: BelleDelicateSunlight Face Blend Hash',)),
            (update_hash,                     ('359e4502',)),
        ],
        '359e4502': [
            (log,                             ('3.0 - 3.2: BelleDelicateSunlight Face Blend VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
        ],
        '75ec3614': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Face Diffuse 2048p Hash (Shared with Belle)',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77eef7e8', 'BelleDelicateSunlight.FaceA.Diffuse.1024')),
        ],
        '77eef7e8': [
            (log,                             ('2.2 - 3.2: BelleDelicateSunlight Face Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('75ec3614', 'BelleDelicateSunlight.FaceA.Diffuse.2048')),
        ],

        # ==================== Red Knot Rope Component ====================
        'c2189ddf': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Red Knot Rope IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '364415bf': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Red Knot Rope Draw VB Hash',)),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
        ],
        '903e5a55': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Red Knot Rope Position VB Hash',)),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
        ],
        '751107c4': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Red Knot Rope Texcoord VB Hash',)),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
        ],
        '83967fb0': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Red Knot Rope Blend VB Hash',)),
            (add_section_if_missing,          ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n')),
        ],

        # ==================== Orange green ribbon Component ====================
        '2ac09c8f': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green ribbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4fc2c5d3': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green ribbon Draw VB Hash',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        'bdfbdec4': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green ribbon Position VB Hash',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        '01118441': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green ribbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        '4e5447eb': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green ribbon Blend VB Hash',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        ],
        '96ad58d4': [
            (log,                             ('2.2 - 2.8: Orange green ribbon/badge Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        '8839d1fc': [
            (log,                             ('2.2 - 2.8: Orange green ribbon/badge LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        'cd075caa': [
            (log,                             ('2.2 - 2.8: Orange green ribbon/badge MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],

        # ==================== Earrings1 Component ====================
        'c0fcc53d': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c0eb7af5': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings1 Draw VB Hash',)),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
        ],
        'fc4bea64': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings1 Position VB Hash',)),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
        ],
        'dde5eb66': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
        ],
        'c2a072c2': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings1 Blend VB Hash',)),
            (add_section_if_missing,          ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n')),
        ],

        # ==================== Earrings2 Component ====================
        'e6e890a7': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8a73bd43': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings2 Draw VB Hash',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        ],
        'c64ed62f': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings2 Position VB Hash',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        ],
        'cd336cdb': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        ],
        '3d24a922': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Earrings2 Blend VB Hash',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        ],
        'ed1a5b7f': [
            (log,                             ('2.2 - 2.8: Earrings/CatEar/glasses/Pink badge Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        'f5dc4198': [
            (log,                             ('2.2 - 2.8: Earrings/CatEar/glasses/Pink badge LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '5346205a': [
            (log,                             ('2.2 - 2.8: Earrings/CatEar/glasses/Pink badge MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],

        # ==================== Panda headgear Component ====================
        'ac3a0dec': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Panda headgear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e7d550d0': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Panda headgear Draw VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        '910612d6': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Panda headgear Position VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'dc08776f': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Panda headgear Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'f621226d': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Panda headgear Blend VB Hash',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        'a2f096fc': [
            (log,                             ('2.2 - 2.8: Panda headgear Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        '78c2d1dd': [
            (log,                             ('2.2 - 2.8: Panda headgear LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],
        '2a7548a9': [
            (log,                             ('2.2 - 2.8: Panda headgear MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Cat Ear Accessories Component ====================
        'b28a7685': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Cat Ear Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7c3db690': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Cat Ear Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        'b4341a72': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Cat Ear Accessories Position VB Hash',)),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        'f98659b3': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Cat Ear Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],
        '8650be1b': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Cat Ear Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        ],

        # ==================== Pink badge Component ====================
        '4e8b2454': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Pink badge IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0406d75f': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Pink badge Draw VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '7109981c': [
            (log,                             ('2.5: BelleDelicateSunlight Pink badge Position VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        'a7882762': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Pink badge Position VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '3e725b6c': [
            (log,                             ('2.5: BelleDelicateSunlight Pink badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '1ff12440': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Pink badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        'e147258a': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Pink badge Blend VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '13e791fa': [
            (log,                             ('2.2 - 2.8: WiseSkin white badge Position VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        'fd95b568': [
            (log,                             ('2.2 - 2.8: WiseSkin white badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '5a8f8d57': [
            (log,                             ('2.5: BelleDelicateSunlight Pink badge Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        'a7e0cba0': [
            (log,                             ('2.5: BelleDelicateSunlight Pink badge LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],
        '07e9e8f5': [
            (log,                             ('2.5: BelleDelicateSunlight Pink badge MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4e8b2454', 'BelleDelicateSunlight.Pink badge.IB', 'match_priority = 0\n')),
        ],

        # ==================== Orange green badge Component ====================
        '4dcc384f': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green badge IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c62e9d0': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green badge Draw VB Hash',)),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        'e837ab1b': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green badge Position VB Hash',)),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        '632b2ed3': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green badge Texcoord VB Hash',)),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],
        '66797141': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight Orange green badge Blend VB Hash',)),
            (add_section_if_missing,          ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
        ],

        # ==================== glasses Component ====================
        '455bcfc7': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight glasses IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ba8bde72': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight glasses Draw VB Hash',)),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        ],
        '6018a88b': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight glasses Position VB Hash',)),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        ],
        'a70c787c': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight glasses Texcoord VB Hash',)),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        ],
        'a8620018': [
            (log,                             ('2.2 - 2.8: BelleDelicateSunlight glasses Blend VB Hash',)),
            (add_section_if_missing,          ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        ],

        # ==================== HeadAcc Component (legacy, not in DB 2.2 - 3.1) ====================
        '30e40390': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'eeea5739': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc Draw VB Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        ],
        '17f8b9dc': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc Position VB Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        ],
        'fb8393bd': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        ],
        'e5a8578f': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc Blend VB Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        ],
        '5e12872e': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc/BackAcc Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '714e278c': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc/BackAcc NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '54bd71d8': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc/BackAcc LightMap 2048p Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        'd7de8ddf': [
            (log,                             ('2.5: BelleDelicateSunlight HeadAcc/BackAcc MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],

        # ==================== BackAcc Component (legacy, not in DB 2.2 - 3.1) ====================
        'ce86946f': [
            (log,                             ('2.5: BelleDelicateSunlight BackAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '83ba6b1f': [
            (log,                             ('2.5: BelleDelicateSunlight BackAcc Draw VB Hash',)),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '601e27b5': [
            (log,                             ('2.5: BelleDelicateSunlight BackAcc Position VB Hash',)),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '81fd09f8': [
            (log,                             ('2.5: BelleDelicateSunlight BackAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '1a44a5ba': [
            (log,                             ('2.5: BelleDelicateSunlight BackAcc Blend VB Hash',)),
            (add_section_if_missing,          ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
        ],

        # ==================== HairWAcc Component (legacy, not in DB 2.2 - 3.1) ====================
        'db72ceab': [
            (log,                             ('2.5: BelleDelicateSunlight HairWAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '040e066c': [
            (log,                             ('2.5: BelleDelicateSunlight HairWAcc Draw VB Hash',)),
            (add_section_if_missing,          ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        '6824cbbe': [
            (log,                             ('2.5: BelleDelicateSunlight HairWAcc Position VB Hash',)),
            (add_section_if_missing,          ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'c6fe65c9': [
            (log,                             ('2.5: BelleDelicateSunlight HairWAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
        'd5b33c94': [
            (log,                             ('2.5: BelleDelicateSunlight HairWAcc Blend VB Hash',)),
            (add_section_if_missing,          ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleDelicateSunlight',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}

