"""
NangongYu Character Hash Commands
ZZZ Mod Fixer v2.7
Game Version: 2.7 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns NangongYu's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '969152d4': [
            (log,                             ('2.7 - 3.2: NangongYu Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '536345c3': [
            (log,                             ('2.7 - 3.2: NangongYu Hair Draw VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
        ],
        'd1a15d0e': [
            (log,                             ('2.7 - 3.2: NangongYu Hair Position VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
        ],
        'e67f6a3c': [
            (log,                             ('2.7 - 3.2: NangongYu Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
        ],
        '56699a62': [
            (log,                             ('2.7 - 3.2: NangongYu Hair Blend VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
        ],
        'df39b77c': [
            (log,                             ('2.7 - 3.2: NangongYu HairA Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d2e23730', 'NangongYu.HairA.Diffuse.1024')),
        ],
        'd2e23730': [
            (log,                             ('2.8 - 3.2: NangongYu HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('df39b77c', 'NangongYu.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.7 - 3.2: NangongYu HairA, HeadbandA, wingA, BodyA and Weapon NormalMap 2048p Hash, also NormalMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYu.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYu.HeadbandA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYu.wingA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYu.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYu.Weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.8 - 3.2: NangongYu HairA, HeadbandA, wingA, BodyA and Weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYu.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYu.HeadbandA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYu.wingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYu.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYu.Weapon.NormalMap.2048')),
        ],
        'd94a0c41': [
            (log,                             ('2.7 - 3.2: NangongYu HairA LightMap 2048p Hash, also LightMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e3573bc8', 'NangongYu.HairA.LightMap.1024')),
        ],
        'e3573bc8': [
            (log,                             ('2.8 - 3.2: NangongYu HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d94a0c41', 'NangongYu.HairA.LightMap.2048')),
        ],
        'a458a615': [
            (log,                             ('2.7 - 3.2: NangongYu HairA MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('687f57b8', 'NangongYu.HairA.MaterialMap.1024')),
        ],
        '687f57b8': [
            (log,                             ('2.8 - 3.2: NangongYu HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYu.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a458a615', 'NangongYu.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '17438fa9': [
            (log,                             ('2.7 - 3.2: NangongYu Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Hair Shadow has no VB or texture hashes in the database.

        # ==================== Headband Component ====================
        'cd884c0a': [
            (log,                             ('2.7 - 3.2: NangongYu Headband IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5aac7571': [
            (log,                             ('2.7 - 3.2: NangongYu Headband Draw VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
        ],
        '74cbadea': [
            (log,                             ('2.7 - 3.2: NangongYu Headband Position VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
        ],
        '00cbd7a8': [
            (log,                             ('2.7 - 3.2: NangongYu Headband Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
        ],
        '82509f4f': [
            (log,                             ('2.7 - 3.2: NangongYu Headband Blend VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
        ],
        '2d290490': [
            (log,                             ('2.7 -> 2.8: NangongYu HeadbandA, wingA and BodyA Diffuse 1024p & 2048p Hash (shared)',)),
            (update_hash,                     ('11254966',)),
        ],
        '11254966': [
            (log,                             ('2.8 - 3.2: NangongYu HeadbandA, wingA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('dc41fbbf', 'fe06152c'), 'NangongYu.HeadbandA.Diffuse.1024')),
            (multiply_section_if_missing,     (('dc41fbbf', 'fe06152c'), 'NangongYu.wingA.Diffuse.1024')),
            (multiply_section_if_missing,     (('dc41fbbf', 'fe06152c'), 'NangongYu.BodyA.Diffuse.1024')),
        ],
        'fe06152c': [
            (log,                             ('2.7 -> 2.8: NangongYu BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('dc41fbbf',)),
        ],
        'dc41fbbf': [
            (log,                             ('2.8 - 3.2: NangongYu HeadbandA, wingA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('11254966', '2d290490'), 'NangongYu.HeadbandA.Diffuse.2048')),
            (multiply_section_if_missing,     (('11254966', '2d290490'), 'NangongYu.wingA.Diffuse.2048')),
            (multiply_section_if_missing,     (('11254966', '2d290490'), 'NangongYu.BodyA.Diffuse.2048')),
        ],
        'fee3d533': [
            (log,                             ('2.7 - 3.2: NangongYu HeadbandA, wingA and BodyA LightMap 2048p Hash, also LightMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYu.HeadbandA.LightMap.1024')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYu.wingA.LightMap.1024')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYu.BodyA.LightMap.1024')),
        ],
        'ab51539c': [
            (log,                             ('2.8 - 3.2: NangongYu HeadbandA, wingA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYu.HeadbandA.LightMap.2048')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYu.wingA.LightMap.2048')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYu.BodyA.LightMap.2048')),
        ],
        'beb11b78': [
            (log,                             ('2.7 - 3.2: NangongYu HeadbandA, wingA and BodyA MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYu.HeadbandA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYu.wingA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYu.BodyA.MaterialMap.1024')),
        ],
        '958e389e': [
            (log,                             ('2.8 - 3.2: NangongYu HeadbandA, wingA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYu.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYu.HeadbandA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYu.wingA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYu.BodyA.MaterialMap.2048')),
        ],

        # ==================== wing Component ====================
        '3b4190ce': [
            (log,                             ('2.7 - 3.2: NangongYu wing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6ab572d9': [
            (log,                             ('2.7 - 3.2: NangongYu wing Draw VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
        ],
        'b90d042a': [
            (log,                             ('2.7 - 3.2: NangongYu wing Position VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
        ],
        'e062b6fc': [
            (log,                             ('2.7 - 3.2: NangongYu wing Texcoord VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
        ],
        '4d677fbd': [
            (log,                             ('2.7 - 3.2: NangongYu wing Blend VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYu.wing.IB', 'match_priority = 0\n')),
        ],
        # wing shares its Diffuse, LightMap and MaterialMap hashes with Headband, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Body Component ====================
        '4586e530': [
            (log,                             ('2.7 - 3.2: NangongYu Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5b0185fc': [
            (log,                             ('2.7 - 3.2: NangongYu Body Draw VB Hash',)),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
        ],
        'd4908293': [
            (log,                             ('2.7 - 3.2: NangongYu Body Position VB Hash',)),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
        ],
        '5ebf2446': [
            (log,                             ('2.7 - 3.2: NangongYu Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
        ],
        'f43a1dba': [
            (log,                             ('2.7 - 3.2: NangongYu Body Blend VB Hash',)),
            (add_section_if_missing,          ('4586e530', 'NangongYu.Body.IB', 'match_priority = 0\n')),
        ],
        # Body shares its Diffuse, LightMap and MaterialMap hashes with Headband and wing, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Eyebrow Component ====================
        'ba598cf9': [
            (log,                             ('2.7 - 3.2: NangongYu Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1fd77103': [
            (log,                             ('2.7 - 3.2: NangongYu EyebrowA and FaceA Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYu.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYu.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYu.FaceA.Diffuse.1024')),
        ],
        'b6e87aef': [
            (log,                             ('2.8 - 3.2: NangongYu EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYu.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYu.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYu.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd643e19a': [
            (log,                             ('2.7 - 3.2: NangongYu Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd70f65c1': [
            (log,                             ('2.7 - 3.2: NangongYu Face Draw VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
        ],
        'ed1df686': [
            (log,                             ('2.7 - 3.2: NangongYu Face Position VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
        ],
        '45910aef': [
            (log,                             ('2.7 - 3.1: NangongYu Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b8af50ce',)),
        ],
        'b8af50ce': [
            (log,                             ('3.2: NangongYu Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '93c1ec0c': [
            (log,                             ('2.7 - 3.2: NangongYu Face Blend VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYu.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.

        # ==================== Weapon Component ====================
        'dcd7242e': [
            (log,                             ('2.7 - 3.2: NangongYu Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8252253e': [
            (log,                             ('2.7: NangongYu Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
        ],
        'fe68de06': [
            (log,                             ('2.7: NangongYu Weapon Position VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
        ],
        '06639b26': [
            (log,                             ('2.7: NangongYu Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4115d67b': [
            (log,                             ('2.7: NangongYu Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
        ],
        'acea6f2f': [
            (log,                             ('2.7 - 3.2: NangongYu Weapon Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84246d50', 'NangongYu.Weapon.Diffuse.1024')),
        ],
        '84246d50': [
            (log,                             ('2.8 - 3.2: NangongYu Weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('acea6f2f', 'NangongYu.Weapon.Diffuse.2048')),
        ],
        '5e50a4f2': [
            (log,                             ('2.7 - 3.2: NangongYu Weapon LightMap 2048p Hash, also LightMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fcc325af', 'NangongYu.Weapon.LightMap.1024')),
        ],
        'fcc325af': [
            (log,                             ('2.8 - 3.2: NangongYu Weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e50a4f2', 'NangongYu.Weapon.LightMap.2048')),
        ],
        '766f3fca': [
            (log,                             ('2.7 - 3.2: NangongYu Weapon MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a64be703', 'NangongYu.Weapon.MaterialMap.1024')),
        ],
        'a64be703': [
            (log,                             ('2.8 - 3.2: NangongYu Weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYu.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('766f3fca', 'NangongYu.Weapon.MaterialMap.2048')),
        ],
        # Weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYu',
    'game_versions': ['2.7', '2.8', '3.0', '3.1', '3.2'],
}
