"""
NangongYuRhapsodyMuse Character Hash Commands
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
    Returns NangongYuRhapsodyMuse's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '969152d4': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '536345c3': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair Draw VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
        ],
        'd1a15d0e': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair Position VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
        ],
        'e67f6a3c': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
        ],
        '56699a62': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair Blend VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
        ],
        '5a026445': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HairA Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4fa2f495', 'NangongYuRhapsodyMuse.HairA.Diffuse.1024')),
        ],
        '4fa2f495': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5a026445', 'NangongYuRhapsodyMuse.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HairA, HeadbandA, wingA, BodyA and Weapon NormalMap 2048p Hash, also NormalMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuRhapsodyMuse.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuRhapsodyMuse.HeadbandA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuRhapsodyMuse.wingA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuRhapsodyMuse.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuRhapsodyMuse.Weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HairA, HeadbandA, wingA, BodyA and Weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuRhapsodyMuse.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuRhapsodyMuse.HeadbandA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuRhapsodyMuse.wingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuRhapsodyMuse.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuRhapsodyMuse.Weapon.NormalMap.2048')),
        ],
        'd94a0c41': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HairA LightMap 2048p Hash, also LightMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e3573bc8', 'NangongYuRhapsodyMuse.HairA.LightMap.1024')),
        ],
        'e3573bc8': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d94a0c41', 'NangongYuRhapsodyMuse.HairA.LightMap.2048')),
        ],
        'a458a615': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HairA MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('687f57b8', 'NangongYuRhapsodyMuse.HairA.MaterialMap.1024')),
        ],
        '687f57b8': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a458a615', 'NangongYuRhapsodyMuse.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '17438fa9': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Hair Shadow has no VB or texture hashes in the database.

        # ==================== Headband Component ====================
        'cd884c0a': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Headband IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5aac7571': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Headband Draw VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        ],
        '74cbadea': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Headband Position VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        ],
        '00cbd7a8': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Headband Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        ],
        '82509f4f': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Headband Blend VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
        ],
        '46c73033': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('263aba53', 'NangongYuRhapsodyMuse.HeadbandA.Diffuse.1024')),
            (multiply_section_if_missing,     ('263aba53', 'NangongYuRhapsodyMuse.wingA.Diffuse.1024')),
            (multiply_section_if_missing,     ('263aba53', 'NangongYuRhapsodyMuse.BodyA.Diffuse.1024')),
        ],
        '263aba53': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('46c73033', 'NangongYuRhapsodyMuse.HeadbandA.Diffuse.2048')),
            (multiply_section_if_missing,     ('46c73033', 'NangongYuRhapsodyMuse.wingA.Diffuse.2048')),
            (multiply_section_if_missing,     ('46c73033', 'NangongYuRhapsodyMuse.BodyA.Diffuse.2048')),
        ],
        'c17bc21d': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA LightMap 2048p Hash, also LightMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('79423b33', 'NangongYuRhapsodyMuse.HeadbandA.LightMap.1024')),
            (multiply_section_if_missing,     ('79423b33', 'NangongYuRhapsodyMuse.wingA.LightMap.1024')),
            (multiply_section_if_missing,     ('79423b33', 'NangongYuRhapsodyMuse.BodyA.LightMap.1024')),
        ],
        '79423b33': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c17bc21d', 'NangongYuRhapsodyMuse.HeadbandA.LightMap.2048')),
            (multiply_section_if_missing,     ('c17bc21d', 'NangongYuRhapsodyMuse.wingA.LightMap.2048')),
            (multiply_section_if_missing,     ('c17bc21d', 'NangongYuRhapsodyMuse.BodyA.LightMap.2048')),
        ],
        'e8200d09': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1786d968', 'NangongYuRhapsodyMuse.HeadbandA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('1786d968', 'NangongYuRhapsodyMuse.wingA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('1786d968', 'NangongYuRhapsodyMuse.BodyA.MaterialMap.1024')),
        ],
        '1786d968': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse HeadbandA, wingA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8200d09', 'NangongYuRhapsodyMuse.HeadbandA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e8200d09', 'NangongYuRhapsodyMuse.wingA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e8200d09', 'NangongYuRhapsodyMuse.BodyA.MaterialMap.2048')),
        ],

        # ==================== wing Component ====================
        '5b186a44': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse wing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4f3fcef0': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse wing Draw VB Hash',)),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
        ],
        'f0922b32': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse wing Position VB Hash',)),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
        ],
        'f1ca59db': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse wing Texcoord VB Hash',)),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
        ],
        '701bb859': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse wing Blend VB Hash',)),
            (add_section_if_missing,          ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
        ],
        # wing shares its Diffuse, LightMap and MaterialMap hashes with Headband, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Body Component ====================
        '5f2741ff': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6f39c5ff': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Body Draw VB Hash',)),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
        ],
        '6a7b86e3': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Body Position VB Hash',)),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
        ],
        '584ee20f': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
        ],
        'bcfea595': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Body Blend VB Hash',)),
            (add_section_if_missing,          ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
        ],
        # Body shares its Diffuse, LightMap and MaterialMap hashes with Headband and wing, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Eyebrow Component ====================
        'ba598cf9': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1fd77103': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse EyebrowA and FaceA Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7 (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYuRhapsodyMuse.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYuRhapsodyMuse.FaceA.Diffuse.1024')),
        ],
        'b6e87aef': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYuRhapsodyMuse.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYuRhapsodyMuse.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd643e19a': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd70f65c1': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Face Draw VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
        ],
        'ed1df686': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Face Position VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
        ],
        '45910aef': [
            (log,                             ('2.7 - 3.1: NangongYuRhapsodyMuse Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b8af50ce',)),
        ],
        'b8af50ce': [
            (log,                             ('3.2: NangongYuRhapsodyMuse Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '93c1ec0c': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Face Blend VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.

        # ==================== Weapon Component ====================
        'dcd7242e': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Weapon has no VB hashes in any database version.
        'cf34f106': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Weapon Diffuse 2048p Hash, also Diffuse 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08ff63ac', 'NangongYuRhapsodyMuse.Weapon.Diffuse.1024')),
        ],
        '08ff63ac': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse Weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf34f106', 'NangongYuRhapsodyMuse.Weapon.Diffuse.2048')),
        ],
        '5e50a4f2': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Weapon LightMap 2048p Hash, also LightMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fcc325af', 'NangongYuRhapsodyMuse.Weapon.LightMap.1024')),
        ],
        'fcc325af': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse Weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e50a4f2', 'NangongYuRhapsodyMuse.Weapon.LightMap.2048')),
        ],
        '766f3fca': [
            (log,                             ('2.7 - 3.2: NangongYuRhapsodyMuse Weapon MaterialMap 2048p Hash, also MaterialMap 1024p Hash in 2.7',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a64be703', 'NangongYuRhapsodyMuse.Weapon.MaterialMap.1024')),
        ],
        'a64be703': [
            (log,                             ('2.8 - 3.2: NangongYuRhapsodyMuse Weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('766f3fca', 'NangongYuRhapsodyMuse.Weapon.MaterialMap.2048')),
        ],
        # Weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYuRhapsodyMuse',
    'game_versions': ['2.7', '2.8', '3.0', '3.1', '3.2'],
}
