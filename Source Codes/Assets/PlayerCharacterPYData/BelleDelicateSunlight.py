"""
BelleDelicateSunlight Outfit Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
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
# =============================================================================
# BelleDelicateSunlight IB Hashes
# =============================================================================
'30e40390': [(log, ('2.5: BelleDelicateSunlight HeadAcc IB Hash',)), (add_ib_check_if_missing,)],
'4e8b2454': [(log, ('2.5: BelleDelicateSunlight TorsoAcc IB Hash',)), (add_ib_check_if_missing,)],
'62ed56cc': [(log, ('2.5: BelleDelicateSunlight Neck IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('d0627e1f',))],
'd0627e1f': [(log, ('3.0: BelleDelicateSunlight Neck IB Hash (Model Change)',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.5: BelleDelicateSunlight Face IB Hash (Shared with Belle)',)), (add_ib_check_if_missing,)],
'aa9ffb85': [(log, ('2.5: BelleDelicateSunlight Hair IB Hash',)), (add_ib_check_if_missing,)],
'bcc9e4e1': [(log, ('2.5: BelleDelicateSunlight Legs IB Hash',)), (add_ib_check_if_missing,)],
'ce86946f': [(log, ('2.5: BelleDelicateSunlight BackAcc IB Hash',)), (add_ib_check_if_missing,)],
'd509bdd4': [(log, ('2.5: BelleDelicateSunlight Body IB Hash',)), (add_ib_check_if_missing,)],
'db72ceab': [(log, ('2.5: BelleDelicateSunlight HairWAcc IB Hash',)), (add_ib_check_if_missing,)],
'2ac09c8f': [(log, ('2.8: BelleSkin Orange green ribbon IB Hash',)), (add_ib_check_if_missing,)],
'c2189ddf': [(log, ('2.8: BelleSkin Red Knot Rope IB Hash',)), (add_ib_check_if_missing,)],
'e6e890a7': [(log, ('2.8: BelleSkin Earrings2 IB Hash',)), (add_ib_check_if_missing,)],
'455bcfc7': [(log, ('2.8: BelleSkin glasses IB Hash',)), (add_ib_check_if_missing,)],
'4dcc384f': [(log, ('2.8: BelleSkin Orange green badge IB Hash',)), (add_ib_check_if_missing,)],
'b28a7685': [(log, ('2.8: BelleSkin Cat Ear Accessories IB Hash',)), (add_ib_check_if_missing,)],
'c0fcc53d': [(log, ('2.8: BelleSkin Earrings1 IB Hash',)), (add_ib_check_if_missing,)],

# =============================================================================
# BelleDelicateSunlight VB Hashes - HeadAcc
# =============================================================================
'eeea5739': [(log, ('2.5: BelleDelicateSunlight HeadAcc draw_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n'))],
'17f8b9dc': [(log, ('2.5: BelleDelicateSunlight HeadAcc position_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n'))],
'e5a8578f': [(log, ('2.5: BelleDelicateSunlight HeadAcc blend_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n'))],
'fb8393bd': [(log, ('2.5: BelleDelicateSunlight HeadAcc texcoord_vb Hash',)), (add_section_if_missing, ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - TorsoAcc
# =============================================================================
'0406d75f': [(log, ('2.5: BelleDelicateSunlight TorsoAcc draw_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],
'7109981c': [(log, ('2.5: BelleDelicateSunlight TorsoAcc position_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],
'e147258a': [(log, ('2.5: BelleDelicateSunlight TorsoAcc blend_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],
'3e725b6c': [(log, ('2.5: BelleDelicateSunlight TorsoAcc texcoord_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - BackAcc
# =============================================================================
'83ba6b1f': [(log, ('2.5: BelleDelicateSunlight BackAcc draw_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n'))],
'601e27b5': [(log, ('2.5: BelleDelicateSunlight BackAcc position_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n'))],
'1a44a5ba': [(log, ('2.5: BelleDelicateSunlight BackAcc blend_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n'))],
'81fd09f8': [(log, ('2.5: BelleDelicateSunlight BackAcc texcoord_vb Hash',)), (add_section_if_missing, ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - Hair
# =============================================================================
'992d149f': [(log, ('2.5: BelleDelicateSunlight Hair draw_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],
'71d2bf80': [(log, ('2.5: BelleDelicateSunlight Hair position_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],
'39ac6700': [(log, ('2.8 -> 3.0: BelleDelicateSunlight Hair Blend Hash',)), (update_hash, ('8f7ae834',))],
'a5e62ece': [(log, ('2.5: BelleDelicateSunlight Hair texcoord_vb Hash',)), (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - HairWAcc
# =============================================================================
'040e066c': [(log, ('2.5: BelleDelicateSunlight HairWAcc draw_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],
'6824cbbe': [(log, ('2.5: BelleDelicateSunlight HairWAcc position_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],
'd5b33c94': [(log, ('2.5: BelleDelicateSunlight HairWAcc blend_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],
'c6fe65c9': [(log, ('2.5: BelleDelicateSunlight HairWAcc texcoord_vb Hash',)), (add_section_if_missing, ('db72ceab', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - Face
# =============================================================================
'04abceb5': [(log, ('2.5: BelleDelicateSunlight Face draw_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n'))],
'3eb95df2': [(log, ('2.5: BelleDelicateSunlight Face position_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n'))],
'0c9a075b': [
        (log,                           ('2.5 -> 3.0: BelleDelicateSunlight Face blend_vb Hash',)),
        (update_hash,                   ('359e4502',)),
    ],
'359e4502': [
        (log,                           ('3.0: BelleDelicateSunlight Face blend_vb Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
    ],
'ccc76aea': [(log, ('2.5: BelleDelicateSunlight Face texcoord_vb Hash',)), (add_section_if_missing, ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')), (update_hash, ('bcfc3326',))],
'bcfc3326': [(log, ('2.6: BelleDelicateSunlight Face texcoord_vb Hash (1024p active)',)), (add_section_if_missing, ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - Neck
# =============================================================================
'4c215c73': [(log, ('2.5: BelleDelicateSunlight Neck draw_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n'))],
'be75a4be': [(log, ('2.5: BelleDelicateSunlight Neck position_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n'))],
'3bd79a0b': [(log, ('2.5: BelleDelicateSunlight Neck blend_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n'))],
'dd2b89aa': [(log, ('2.5: BelleDelicateSunlight Neck texcoord_vb Hash',)), (add_section_if_missing, ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - Body
# =============================================================================
'19e5f486': [(log, ('2.5: BelleDelicateSunlight Body draw_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n'))],
'8a4e97cd': [(log, ('2.5: BelleDelicateSunlight Body position_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n'))],
'f3dedb50': [(log, ('2.8 -> 3.0: BelleDelicateSunlight Body Blend Hash',)), (update_hash, ('4d74d5e9',))],
'd761e076': [(log, ('2.5: BelleDelicateSunlight Body texcoord_vb Hash',)), (add_section_if_missing, ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight VB Hashes - Legs
# =============================================================================
'720d6a16': [(log, ('2.5: BelleDelicateSunlight Legs draw_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n'))],
'42b88f48': [(log, ('2.5: BelleDelicateSunlight Legs position_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n'))],
'f53b2eba': [(log, ('2.8 -> 3.0: BelleDelicateSunlight Leg Blend Hash',)), (update_hash, ('922a7db6',))],
'82d0aadd': [(log, ('2.5: BelleDelicateSunlight Legs texcoord_vb Hash',)), (add_section_if_missing, ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n'))],

# =============================================================================
# BelleDelicateSunlight Body Hash Updates (Old → New)
# =============================================================================
'01b0c8b6': [(log, ('2.5: Updating BelleDelicateSunlight Body blend_vb to f3dedb50',)), (update_hash, ('f3dedb50',))],
'862dc27a': [(log, ('2.5: Updating BelleDelicateSunlight Body texcoord_vb to d761e076',)), (update_hash, ('d761e076',))],
'0b3c5e7c': [(log, ('2.5: Updating BelleDelicateSunlight Body position_vb to 8a4e97cd',)), (update_hash, ('8a4e97cd',))],
'02c9dc4b': [(log, ('2.5: Updating BelleDelicateSunlight Body draw_vb to 19e5f486',)), (update_hash, ('19e5f486',))],
'860e1558': [(log, ('2.5: Updating BelleDelicateSunlight Body IB to d509bdd4',)), (update_hash, ('d509bdd4',))],

# =============================================================================
# BelleDelicateSunlight Neck Hash Updates (Old → New)
# =============================================================================
'20d3a340': [(log, ('2.5: Updating BelleDelicateSunlight Neck IB to 62ed56cc',)), (update_hash, ('62ed56cc',))],
'2f828e6a': [(log, ('2.5: Updating BelleDelicateSunlight Neck draw_vb to 4c215c73',)), (update_hash, ('4c215c73',))],
'cdd7fc8a': [(log, ('2.5: Updating BelleDelicateSunlight Neck texcoord_vb to dd2b89aa',)), (update_hash, ('dd2b89aa',))],
'db7add33': [(log, ('2.8 -> 3.0: BelleDelicateSunlight Headwear Blend Hash',)), (update_hash, ('f18dd23f',))],

# =============================================================================
# BelleDelicateSunlight Face Textures (shares Face IB and Head Diffuse with Belle)
# =============================================================================
# Face Diffuse 2048p: 75ec3614 (same as Belle HeadA Diffuse 2048p)
# This is handled by Belle.py but we ensure the IB check exists

# =============================================================================
# BelleDelicateSunlight HeadAcc Textures
# =============================================================================
'5e12872e': [
        (log,                           ('2.5: BelleDelicateSunlight HeadAcc/BackAcc Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
    ],
'714e278c': [
        (log,                           ('2.5: BelleDelicateSunlight HeadAcc/BackAcc NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
    ],
'54bd71d8': [
        (log,                           ('2.5: BelleDelicateSunlight HeadAcc/BackAcc LightMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
    ],
'd7de8ddf': [
        (log,                           ('2.5: BelleDelicateSunlight HeadAcc/BackAcc MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('30e40390', 'BelleDelicateSunlight.HeadAcc.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ce86946f', 'BelleDelicateSunlight.BackAcc.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# BelleDelicateSunlight TorsoAcc Textures
# =============================================================================
'5a8f8d57': [
        (log,                           ('2.5: BelleDelicateSunlight TorsoAcc Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'a7e0cba0': [
        (log,                           ('2.5: BelleDelicateSunlight TorsoAcc LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'07e9e8f5': [
        (log,                           ('2.5: BelleDelicateSunlight TorsoAcc MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# BelleDelicateSunlight Hair Textures (shares texture hashes with Belle)
# =============================================================================
# Hair Diffuse 2048p: 1ce58567 (same as Belle HairA Diffuse 2048p)
# Hair LightMap 2048p: 7d562f53 (same as Belle HairA LightMap 2048p) 
# Hair MaterialMap 2048p: 34bdb036 (same as Belle HairA MaterialMap 2048p)
# Hair NormalMap 2048p: ebac056e (same as Belle shared NormalMap)
# These are handled by Belle.py but we ensure the IB check exists for BelleDelicateSunlight Hair IB

# =============================================================================
# BelleDelicateSunlight Body/Neck/Legs Shared Textures
# =============================================================================
'cac9fd5d': [(log, ('2.0 -> 2.1: BelleSkin BodyA Diffuse 2048p Hash',)), (update_hash, ('da2bfe2f',))],
'da2bfe2f': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0a2e0f42', 'BelleDelicateSunlight.BodyNeckLegs.Diffuse.1024')),
        (multiply_section_if_missing,        (('59218fac', 'fdf0b49e'), 'BelleDelicateSunlight.BodyA.Diffuse.1024')),
    ],

'59218fac': [(log, ('2.0 -> 2.1: BelleSkin BodyA Diffuse 1024p Hash',)), (update_hash, ('fdf0b49e',))],
'fdf0b49e': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0a2e0f42', 'BelleDelicateSunlight.BodyNeckLegs.Diffuse.1024')),
        (multiply_section_if_missing,        (('da2bfe2f', 'cac9fd5d'), 'BelleDelicateSunlight.BodyA.Diffuse.2048')),
    ],
'0a2e0f42': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('da2bfe2f', 'BelleDelicateSunlight.BodyNeckLegs.Diffuse.2048')),
    ],

# NormalMap: ebac056e (same as Belle - shared across Hair+Body)
# This is handled by Belle.py with add_section_if_missing calls

'74f2fae3': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs LightMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f8e4e93a', 'BelleDelicateSunlight.BodyNeckLegs.LightMap.1024')),
        (multiply_section_if_missing,        ('93d94f22', 'BelleDelicateSunlight.BodyA.LightMap.1024')),
    ],

'93d94f22': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs LightMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f8e4e93a', 'BelleDelicateSunlight.BodyNeckLegs.LightMap.1024')),
        (multiply_section_if_missing,        ('74f2fae3', 'BelleDelicateSunlight.BodyA.LightMap.2048')),
    ],
'f8e4e93a': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs LightMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('74f2fae3', 'BelleDelicateSunlight.BodyNeckLegs.LightMap.2048')),
    ],

'657402d0': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('93c5f5ff', 'BelleDelicateSunlight.BodyNeckLegs.MaterialMap.1024')),
        (multiply_section_if_missing,        ('b95c08fb', 'BelleDelicateSunlight.BodyA.MaterialMap.1024')),
    ],

'b95c08fb': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('93c5f5ff', 'BelleDelicateSunlight.BodyNeckLegs.MaterialMap.1024')),
        (multiply_section_if_missing,        ('657402d0', 'BelleDelicateSunlight.BodyA.MaterialMap.2048')),
    ],
'93c5f5ff': [
        (log,                           ('2.5: BelleDelicateSunlight Body/Neck/Legs MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('62ed56cc', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc9e4e1', 'BelleDelicateSunlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d509bdd4', 'BelleDelicateSunlight.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('657402d0', 'BelleDelicateSunlight.BodyNeckLegs.MaterialMap.2048')),
    ],

# =============================================================================
# BelleDelicateSunlight Face Textures (Note: Face MaterialMap uses Hair MaterialMap)
# =============================================================================
'75ec3614': [
        (log,                           ('2.5: BelleDelicateSunlight Face Diffuse 2048p Hash (Shared with Belle)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
    ],
# Face MaterialMap 2048p: 34bdb036 (same as Belle Hair MaterialMap - handled by Belle.py)
'8f7ae834': [
        (log, ('3.0: BelleDelicateSunlight Hair VB Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'1ce58567': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'403eace9': [(log, ('3.0: BelleDelicateSunlight Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'4dec8913': [
        (log, ('3.0: BelleDelicateSunlight Headwear VB Hash',)),
        (add_section_if_missing, ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'f18dd23f': [
        (log, ('3.0: BelleDelicateSunlight Headwear VB Hash',)),
        (add_section_if_missing, ('20d3a340', 'BelleDelicateSunlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'3f594476': [
        (log, ('3.0: BelleDelicateSunlight Neck VB Hash',)),
        (add_section_if_missing, ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
    ],
'e2ee9309': [
        (log, ('3.0: BelleDelicateSunlight Neck VB Hash',)),
        (add_section_if_missing, ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
    ],
'2f7f6398': [
        (log, ('3.0: BelleDelicateSunlight Neck VB Hash',)),
        (add_section_if_missing, ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
    ],
'0a11b1d7': [
        (log, ('3.0: BelleDelicateSunlight Neck VB Hash',)),
        (add_section_if_missing, ('d0627e1f', 'BelleDelicateSunlight.Neck.IB', 'match_priority = 0\n')),
    ],
'4d74d5e9': [
        (log, ('3.0: BelleDelicateSunlight Torso VB Hash',)),
        (add_section_if_missing, ('d509bdd4', 'BelleDelicateSunlight.Torso.IB', 'match_priority = 0\n')),
    ],
'922a7db6': [
        (log, ('3.0: BelleDelicateSunlight Leg VB Hash',)),
        (add_section_if_missing, ('bcc9e4e1', 'BelleDelicateSunlight.Leg.IB', 'match_priority = 0\n')),
    ],
'08f04d95': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'7542ef4b': [
        (log, ('3.0: BelleDelicateSunlight Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleDelicateSunlight.Hair.IB', 'match_priority = 0\n')),
    ],
'77eef7e8': [
        (log, ('3.0: BelleDelicateSunlight Face TEX Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleDelicateSunlight.Face.IB', 'match_priority = 0\n')),
    ],

# =============================================================================
# 2.8: WiseSkin white badge (shares TorsoAcc IB 4e8b2454 with BelleDelicateSunlight)
# =============================================================================
'13e791fa': [(log, ('2.8: WiseSkin white badge position_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],
'fd95b568': [(log, ('2.8: WiseSkin white badge texcoord_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Pink badge (shares TorsoAcc IB 4e8b2454)
# =============================================================================
'a7882762': [(log, ('2.8: BelleSkin Pink badge position_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],
'1ff12440': [(log, ('2.8: BelleSkin Pink badge texcoord_vb Hash',)), (add_section_if_missing, ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Red Knot Rope
# =============================================================================
'364415bf': [(log, ('2.8: BelleSkin Red Knot Rope draw_vb Hash',)), (add_section_if_missing, ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n'))],
'903e5a55': [(log, ('2.8: BelleSkin Red Knot Rope position_vb Hash',)), (add_section_if_missing, ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n'))],
'751107c4': [(log, ('2.8: BelleSkin Red Knot Rope texcoord_vb Hash',)), (add_section_if_missing, ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n'))],
'83967fb0': [(log, ('2.8: BelleSkin Red Knot Rope blend_vb Hash',)), (add_section_if_missing, ('c2189ddf', 'BelleDelicateSunlight.Red Knot Rope.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Orange green ribbon
# =============================================================================
'4fc2c5d3': [(log, ('2.8: BelleSkin Orange green ribbon draw_vb Hash',)), (add_section_if_missing, ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n'))],
'bdfbdec4': [(log, ('2.8: BelleSkin Orange green ribbon position_vb Hash',)), (add_section_if_missing, ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n'))],
'01118441': [(log, ('2.8: BelleSkin Orange green ribbon texcoord_vb Hash',)), (add_section_if_missing, ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n'))],
'4e5447eb': [(log, ('2.8: BelleSkin Orange green ribbon blend_vb Hash',)), (add_section_if_missing, ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Earrings1
# =============================================================================
'c0eb7af5': [(log, ('2.8: BelleSkin Earrings1 draw_vb Hash',)), (add_section_if_missing, ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n'))],
'fc4bea64': [(log, ('2.8: BelleSkin Earrings1 position_vb Hash',)), (add_section_if_missing, ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n'))],
'dde5eb66': [(log, ('2.8: BelleSkin Earrings1 texcoord_vb Hash',)), (add_section_if_missing, ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n'))],
'c2a072c2': [(log, ('2.8: BelleSkin Earrings1 blend_vb Hash',)), (add_section_if_missing, ('c0fcc53d', 'BelleDelicateSunlight.Earrings1.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Earrings2
# =============================================================================
'8a73bd43': [(log, ('2.8: BelleSkin Earrings2 draw_vb Hash',)), (add_section_if_missing, ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n'))],
'c64ed62f': [(log, ('2.8: BelleSkin Earrings2 position_vb Hash',)), (add_section_if_missing, ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n'))],
'cd336cdb': [(log, ('2.8: BelleSkin Earrings2 texcoord_vb Hash',)), (add_section_if_missing, ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n'))],
'3d24a922': [(log, ('2.8: BelleSkin Earrings2 blend_vb Hash',)), (add_section_if_missing, ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Panda headgear (shares IB ac3a0dec with WiseSoaringCrane)
# =============================================================================
'910612d6': [(log, ('2.8: BelleSkin Panda headgear position_vb Hash',)), (add_section_if_missing, ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n'))],
'dc08776f': [(log, ('2.8: BelleSkin Panda headgear texcoord_vb Hash',)), (add_section_if_missing, ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n'))],
'f621226d': [(log, ('2.8: BelleSkin Panda headgear blend_vb Hash',)), (add_section_if_missing, ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Cat Ear Accessories
# =============================================================================
'7c3db690': [(log, ('2.8: BelleSkin Cat Ear Accessories draw_vb Hash',)), (add_section_if_missing, ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n'))],
'b4341a72': [(log, ('2.8: BelleSkin Cat Ear Accessories position_vb Hash',)), (add_section_if_missing, ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n'))],
'f98659b3': [(log, ('2.8: BelleSkin Cat Ear Accessories texcoord_vb Hash',)), (add_section_if_missing, ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n'))],
'8650be1b': [(log, ('2.8: BelleSkin Cat Ear Accessories blend_vb Hash',)), (add_section_if_missing, ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin Orange green badge
# =============================================================================
'6c62e9d0': [(log, ('2.8: BelleSkin Orange green badge draw_vb Hash',)), (add_section_if_missing, ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n'))],
'e837ab1b': [(log, ('2.8: BelleSkin Orange green badge position_vb Hash',)), (add_section_if_missing, ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n'))],
'632b2ed3': [(log, ('2.8: BelleSkin Orange green badge texcoord_vb Hash',)), (add_section_if_missing, ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n'))],
'66797141': [(log, ('2.8: BelleSkin Orange green badge blend_vb Hash',)), (add_section_if_missing, ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: BelleSkin glasses
# =============================================================================
'6018a88b': [(log, ('2.8: BelleSkin glasses position_vb Hash',)), (add_section_if_missing, ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n'))],
'a70c787c': [(log, ('2.8: BelleSkin glasses texcoord_vb Hash',)), (add_section_if_missing, ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n'))],

# =============================================================================
# 2.8: WiseSkin + BelleSkin shared accessory textures
# =============================================================================
'ed1a5b7f': [
        (log,                           ('2.8: Earrings/CatEar/glasses/Pink badge Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'f5dc4198': [
        (log,                           ('2.8: Earrings/CatEar/glasses/Pink badge LightMap 2048p Hash',)),
        (add_section_if_missing,        ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'5346205a': [
        (log,                           ('2.8: Earrings/CatEar/glasses/Pink badge MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('e6e890a7', 'BelleDelicateSunlight.Earrings2.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b28a7685', 'BelleDelicateSunlight.Cat Ear Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('455bcfc7', 'BelleDelicateSunlight.glasses.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4e8b2454', 'BelleDelicateSunlight.TorsoAcc.IB', 'match_priority = 0\n')),
    ],
'96ad58d4': [
        (log,                           ('2.8: Orange green ribbon/badge Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'8839d1fc': [
        (log,                           ('2.8: Orange green ribbon/badge LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'cd075caa': [
        (log,                           ('2.8: Orange green ribbon/badge MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2ac09c8f', 'BelleDelicateSunlight.Orange green ribbon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4dcc384f', 'BelleDelicateSunlight.Orange green badge.IB', 'match_priority = 0\n')),
    ],
'a2f096fc': [
        (log,                           ('2.8: Panda headgear Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'78c2d1dd': [
        (log,                           ('2.8: Panda headgear LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
    ],
'2a7548a9': [
        (log,                           ('2.8: Panda headgear MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ac3a0dec', 'BelleDelicateSunlight.Panda headgear.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleDelicateSunlight',
    'game_versions': ['2.5', '3.0'],
}

