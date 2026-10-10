"""
NangongYuHeartfeltSupport Character Hash Commands
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
    Returns NangongYuHeartfeltSupport's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '969152d4': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '536345c3': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Hair Draw VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
        ],
        'd1a15d0e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Hair Position VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
        ],
        'e67f6a3c': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
        ],
        '56699a62': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Hair Blend VB Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
        ],
        'df39b77c': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d2e23730', 'NangongYuHeartfeltSupport.HairA.Diffuse.1024')),
        ],
        'd2e23730': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('df39b77c', 'NangongYuHeartfeltSupport.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA, HeadbandA, BodyA, BodyB, WingA and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.HeadbandA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.WingA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NangongYuHeartfeltSupport.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA, HeadbandA, BodyA, BodyB, WingA and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.HeadbandA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.WingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NangongYuHeartfeltSupport.weaponA.NormalMap.2048')),
        ],
        'd94a0c41': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e3573bc8', 'NangongYuHeartfeltSupport.HairA.LightMap.1024')),
        ],
        'e3573bc8': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d94a0c41', 'NangongYuHeartfeltSupport.HairA.LightMap.2048')),
        ],
        'a458a615': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('687f57b8', 'NangongYuHeartfeltSupport.HairA.MaterialMap.1024')),
        ],
        '687f57b8': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('969152d4', 'NangongYuHeartfeltSupport.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a458a615', 'NangongYuHeartfeltSupport.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '17438fa9': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b44609d7': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('17438fa9', 'NangongYuHeartfeltSupport.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'd50f1169': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('17438fa9', 'NangongYuHeartfeltSupport.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '57fb5daa': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('17438fa9', 'NangongYuHeartfeltSupport.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'c34ed66a': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('17438fa9', 'NangongYuHeartfeltSupport.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Headband Component ====================
        'cd884c0a': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Headband IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5aac7571': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Headband Draw VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
        ],
        '74cbadea': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Headband Position VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
        ],
        '00cbd7a8': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Headband Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
        ],
        '82509f4f': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Headband Blend VB Hash',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
        ],
        'f0e8f22e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2eb1446e', 'NangongYuHeartfeltSupport.HeadbandA.Diffuse.1024')),
            (multiply_section_if_missing,     ('2eb1446e', 'NangongYuHeartfeltSupport.BodyA.Diffuse.1024')),
        ],
        '2eb1446e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0e8f22e', 'NangongYuHeartfeltSupport.HeadbandA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f0e8f22e', 'NangongYuHeartfeltSupport.BodyA.Diffuse.2048')),
        ],
        'fee3d533': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA, BodyA and WingA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYuHeartfeltSupport.HeadbandA.LightMap.1024')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYuHeartfeltSupport.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('ab51539c', 'NangongYuHeartfeltSupport.WingA.LightMap.1024')),
        ],
        'ab51539c': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA, BodyA and WingA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYuHeartfeltSupport.HeadbandA.LightMap.2048')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYuHeartfeltSupport.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('fee3d533', 'NangongYuHeartfeltSupport.WingA.LightMap.2048')),
        ],
        'beb11b78': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA, BodyA and WingA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYuHeartfeltSupport.HeadbandA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYuHeartfeltSupport.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('958e389e', 'NangongYuHeartfeltSupport.WingA.MaterialMap.1024')),
        ],
        '958e389e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport HeadbandA, BodyA and WingA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cd884c0a', 'NangongYuHeartfeltSupport.Headband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYuHeartfeltSupport.HeadbandA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYuHeartfeltSupport.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('beb11b78', 'NangongYuHeartfeltSupport.WingA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'fb76d934': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '722e2eda': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Body Draw VB Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
        ],
        '3a34be2f': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Body Position VB Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
        ],
        'c6657eaa': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
        ],
        'd5dd663f': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Body Blend VB Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
        ],
        '9cfeac60': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91f00b40', 'NangongYuHeartfeltSupport.BodyB.Diffuse.1024')),
        ],
        '91f00b40': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9cfeac60', 'NangongYuHeartfeltSupport.BodyB.Diffuse.2048')),
        ],
        '6193ed20': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c534187b', 'NangongYuHeartfeltSupport.BodyB.LightMap.1024')),
        ],
        'c534187b': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6193ed20', 'NangongYuHeartfeltSupport.BodyB.LightMap.2048')),
        ],
        'a9bf33e2': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e323c61a', 'NangongYuHeartfeltSupport.BodyB.MaterialMap.1024')),
        ],
        'e323c61a': [
            (log,                             ('3.2: NangongYuHeartfeltSupport BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fb76d934', 'NangongYuHeartfeltSupport.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9bf33e2', 'NangongYuHeartfeltSupport.BodyB.MaterialMap.2048')),
        ],

        # ==================== Wing Component ====================
        '3b4190ce': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Wing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6ab572d9': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Wing Draw VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
        ],
        'b90d042a': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Wing Position VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
        ],
        'e062b6fc': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Wing Texcoord VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
        ],
        '4d677fbd': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Wing Blend VB Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
        ],
        '11254966': [
            (log,                             ('3.2: NangongYuHeartfeltSupport WingA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc41fbbf', 'NangongYuHeartfeltSupport.WingA.Diffuse.1024')),
        ],
        'dc41fbbf': [
            (log,                             ('3.2: NangongYuHeartfeltSupport WingA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3b4190ce', 'NangongYuHeartfeltSupport.Wing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('11254966', 'NangongYuHeartfeltSupport.WingA.Diffuse.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'ba598cf9': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6e02f849': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '54106b0e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '37451b01': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '09fa4349': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '1fd77103': [
            (log,                             ('3.2: NangongYuHeartfeltSupport EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYuHeartfeltSupport.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b6e87aef', 'NangongYuHeartfeltSupport.FaceA.Diffuse.1024')),
        ],
        'b6e87aef': [
            (log,                             ('3.2: NangongYuHeartfeltSupport EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ba598cf9', 'NangongYuHeartfeltSupport.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYuHeartfeltSupport.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1fd77103', 'NangongYuHeartfeltSupport.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'd643e19a': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd70f65c1': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Face Draw VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
        ],
        'ed1df686': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Face Position VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
        ],
        'b8af50ce': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '93c1ec0c': [
            (log,                             ('3.2: NangongYuHeartfeltSupport Face Blend VB Hash',)),
            (add_section_if_missing,          ('d643e19a', 'NangongYuHeartfeltSupport.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        'dcd7242e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8252253e': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weapon Draw VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
        ],
        'fe68de06': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weapon Position VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
        ],
        '06639b26': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
        ],
        '4115d67b': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weapon Blend VB Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
        ],
        'acea6f2f': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84246d50', 'NangongYuHeartfeltSupport.weaponA.Diffuse.1024')),
        ],
        '84246d50': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('acea6f2f', 'NangongYuHeartfeltSupport.weaponA.Diffuse.2048')),
        ],
        '5e50a4f2': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fcc325af', 'NangongYuHeartfeltSupport.weaponA.LightMap.1024')),
        ],
        'fcc325af': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e50a4f2', 'NangongYuHeartfeltSupport.weaponA.LightMap.2048')),
        ],
        '766f3fca': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a64be703', 'NangongYuHeartfeltSupport.weaponA.MaterialMap.1024')),
        ],
        'a64be703': [
            (log,                             ('3.2: NangongYuHeartfeltSupport weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('dcd7242e', 'NangongYuHeartfeltSupport.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('766f3fca', 'NangongYuHeartfeltSupport.weaponA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYuHeartfeltSupport',
    'game_versions': ['3.2'],
}
