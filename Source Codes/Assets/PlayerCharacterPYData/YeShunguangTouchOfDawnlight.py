"""
YeShunguangTouchOfDawnlight Character Hash Commands
ZZZ Mod Fixer v3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YeShunguangTouchOfDawnlight's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.8: YeShunguangTouchOfDawnlight Ears IB Hash',)),          (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.8: YeShunguangTouchOfDawnlight Legs IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.8: YeShunguangTouchOfDawnlight Brows IB Hash',)),         (add_ib_check_if_missing,)],
'6dc6c880': [(log, ('2.8: YeShunguangTouchOfDawnlight HairClips IB Hash',)),     (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.8: YeShunguangTouchOfDawnlight Tail IB Hash',)),          (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.8: YeShunguangTouchOfDawnlight Torso IB Hash',)),         (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.8: YeShunguangTouchOfDawnlight HairTassels IB Hash',)),   (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.8: YeShunguangTouchOfDawnlight Dress IB Hash',)),         (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.8: YeShunguangTouchOfDawnlight Face IB Hash',)),          (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.8: YeShunguangTouchOfDawnlight HairBow IB Hash',)),       (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.8: YeShunguangTouchOfDawnlight BraidRibbons IB Hash',)),  (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.8: YeShunguangTouchOfDawnlight RibbonFlower IB Hash',)),  (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.8: YeShunguangTouchOfDawnlight Bangs IB Hash',)),         (add_ib_check_if_missing,)],
'bdf6d0eb': [(log, ('2.8: YeShunguangTouchOfDawnlight HairShadow IB Hash',)),   (add_ib_check_if_missing,)],
'ba7164f5': [(log, ('2.8: YeShunguangTouchOfDawnlight TransparentCloth IB Hash',)),(add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'93c3c2b7': [(log, ('3.0: YeShunguangTouchOfDawnlight Sword IB Hash',)),         (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'bd9b6102': [(log, ('2.8: YeShunguangTouchOfDawnlight Hair draw_vb',)),             (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'f84ce9bf': [(log, ('2.8: YeShunguangTouchOfDawnlight Hair position_vb',)),         (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'afe311e8': [(log, ('2.8: YeShunguangTouchOfDawnlight Hair texcoord_vb',)),         (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'e841684d': [(log, ('2.8: YeShunguangTouchOfDawnlight Hair blend_vb',)),            (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],

# Hair Shadow
'9e743bd7': [(log, ('2.8: YeShunguangTouchOfDawnlight HairShadow draw_vb',)),       (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n'))],
'520b7f22': [(log, ('2.8: YeShunguangTouchOfDawnlight HairShadow position_vb',)),   (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n'))],
'af0e2b6e': [(log, ('2.8: YeShunguangTouchOfDawnlight HairShadow texcoord_vb',)),   (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n'))],
'1e57173e': [(log, ('2.8: YeShunguangTouchOfDawnlight HairShadow blend_vb',)),      (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n'))],

# FrontHair
'01d5a625': [(log, ('2.8: YeShunguangTouchOfDawnlight FrontHair draw_vb',)),        (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'bba40575': [(log, ('2.8: YeShunguangTouchOfDawnlight FrontHair position_vb',)),    (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'bea60077': [(log, ('2.8: YeShunguangTouchOfDawnlight FrontHair texcoord_vb',)),    (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],
'4ca25eef': [(log, ('2.8: YeShunguangTouchOfDawnlight FrontHair blend_vb',)),       (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n'))],

# Braid
'e05bf3a8': [(log, ('2.8: YeShunguangTouchOfDawnlight Braid draw_vb',)),            (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.BraidRibbons.IB', 'match_priority = 0\n'))],
'b871ef41': [(log, ('2.8: YeShunguangTouchOfDawnlight Braid position_vb',)),        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.BraidRibbons.IB', 'match_priority = 0\n'))],
'd7d41552': [(log, ('2.8: YeShunguangTouchOfDawnlight Braid texcoord_vb',)),        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.BraidRibbons.IB', 'match_priority = 0\n'))],
'06e29dd2': [(log, ('2.8: YeShunguangTouchOfDawnlight Braid blend_vb',)),           (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.BraidRibbons.IB', 'match_priority = 0\n'))],

# Body / Torso
'506b7080': [(log, ('2.8: YeShunguangTouchOfDawnlight Body draw_vb',)),             (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Torso.IB', 'match_priority = 0\n'))],
'22213b25': [(log, ('2.8: YeShunguangTouchOfDawnlight Body position_vb',)),         (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Torso.IB', 'match_priority = 0\n'))],
'2a98d810': [(log, ('2.8: YeShunguangTouchOfDawnlight Body texcoord_vb',)),         (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Torso.IB', 'match_priority = 0\n'))],
'b827643b': [(log, ('2.8: YeShunguangTouchOfDawnlight Body blend_vb',)),            (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Torso.IB', 'match_priority = 0\n'))],

# Legs
'b117fabb': [(log, ('2.8: YeShunguangTouchOfDawnlight Leg draw_vb',)),              (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Legs.IB', 'match_priority = 0\n'))],
'38b4c4e8': [(log, ('2.8: YeShunguangTouchOfDawnlight Leg position_vb',)),          (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Legs.IB', 'match_priority = 0\n'))],
'ea5a39d1': [(log, ('2.8: YeShunguangTouchOfDawnlight Leg texcoord_vb',)),          (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Legs.IB', 'match_priority = 0\n'))],
'352c95b2': [(log, ('2.8: YeShunguangTouchOfDawnlight Leg blend_vb',)),             (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Legs.IB', 'match_priority = 0\n'))],

# Skirt
'ff96a5d2': [(log, ('2.8: YeShunguangTouchOfDawnlight Skirt draw_vb',)),            (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n'))],
'43eb20a0': [(log, ('2.8: YeShunguangTouchOfDawnlight Skirt position_vb',)),        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n'))],
'1f27ab54': [(log, ('2.8: YeShunguangTouchOfDawnlight Skirt texcoord_vb',)),        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n'))],
'6468f592': [(log, ('2.8: YeShunguangTouchOfDawnlight Skirt blend_vb',)),           (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n'))],

# Tail
'3fe83226': [(log, ('2.8: YeShunguangTouchOfDawnlight Tail draw_vb',)),             (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n'))],
'9a2dfc61': [(log, ('2.8: YeShunguangTouchOfDawnlight Tail position_vb',)),         (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n'))],
'cb4b7cc7': [(log, ('2.8: YeShunguangTouchOfDawnlight Tail texcoord_vb',)),         (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n'))],
'690ba2b1': [(log, ('2.8: YeShunguangTouchOfDawnlight Tail blend_vb',)),            (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n'))],

# Headwear Flower
'0e30f719': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearFlower draw_vb',)),   (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.HairClips.IB', 'match_priority = 0\n'))],
'7fd64a5b': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearFlower position_vb',)),(add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.HairClips.IB', 'match_priority = 0\n'))],
'7105bdbb': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearFlower texcoord_vb',)),(add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.HairClips.IB', 'match_priority = 0\n'))],
'16a21c01': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearFlower blend_vb',)),  (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.HairClips.IB', 'match_priority = 0\n'))],

# Headwear Long Ribbon
'7ccb6725': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearLongRibbon draw_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.HairTassels.IB', 'match_priority = 0\n'))],
'682c1e3c': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearLongRibbon position_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.HairTassels.IB', 'match_priority = 0\n'))],
'1e3923d1': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearLongRibbon texcoord_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.HairTassels.IB', 'match_priority = 0\n'))],
'093ff56e': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearLongRibbon blend_vb',)),(add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.HairTassels.IB', 'match_priority = 0\n'))],

# Headwear Short Ribbon
'3874c939': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearShortRibbon draw_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.HairBow.IB', 'match_priority = 0\n'))],
'1b410367': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearShortRibbon position_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.HairBow.IB', 'match_priority = 0\n'))],
'e71ea768': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearShortRibbon texcoord_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.HairBow.IB', 'match_priority = 0\n'))],
'ae7cced6': [(log, ('2.8: YeShunguangTouchOfDawnlight HeadwearShortRibbon blend_vb',)),(add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.HairBow.IB', 'match_priority = 0\n'))],

# RibbonFlower
'a203c8fa': [(log, ('2.8: YeShunguangTouchOfDawnlight RibbonFlower draw_vb',)),      (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n'))],
'4c1d8708': [(log, ('2.8: YeShunguangTouchOfDawnlight RibbonFlower position_vb',)),  (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n'))],
'b8e7470f': [(log, ('2.8: YeShunguangTouchOfDawnlight RibbonFlower texcoord_vb',)),  (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n'))],
'917a4c3e': [(log, ('2.8: YeShunguangTouchOfDawnlight RibbonFlower blend_vb',)),     (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n'))],

# TransparentCloth
'b040f517': [(log, ('2.8: YeShunguangTouchOfDawnlight TransparentCloth draw_vb',)),  (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n'))],
'd98395a9': [(log, ('2.8: YeShunguangTouchOfDawnlight TransparentCloth position_vb',)),(add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n'))],
'0925ae65': [(log, ('2.8: YeShunguangTouchOfDawnlight TransparentCloth texcoord_vb',)),(add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n'))],
'651d14a2': [(log, ('2.8: YeShunguangTouchOfDawnlight TransparentCloth blend_vb',)), (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n'))],

# Eyebrow
'9f0ab8cd': [(log, ('2.8: YeShunguangTouchOfDawnlight Eyebrow draw_vb',)),          (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Brows.IB', 'match_priority = 0\n'))],
'a5182b8a': [(log, ('2.8: YeShunguangTouchOfDawnlight Eyebrow position_vb',)),      (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Brows.IB', 'match_priority = 0\n'))],
'287c161c': [(log, ('2.8: YeShunguangTouchOfDawnlight Eyebrow Position Hash',)),    (update_hash, ('a5182b8a',))],
'f5daa764': [(log, ('2.8: YeShunguangTouchOfDawnlight Eyebrow blend_vb',)),          (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Brows.IB', 'match_priority = 0\n'))],

# Face
'2f2f9780': [(log, ('2.8: YeShunguangTouchOfDawnlight Face draw_vb',)),             (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n'))],
'153d04c7': [(log, ('2.8: YeShunguangTouchOfDawnlight Face position_vb',)),         (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n'))],
'a1353cc8': [(log, ('2.8: YeShunguangTouchOfDawnlight Face texcoord_vb',)),         (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n'))],
'fa261a46': [(log, ('2.8: YeShunguangTouchOfDawnlight Face blend_vb',)),            (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n'))],

# === 3.0 Database Updates (Strict Sync) ===
# Sword VBs
'f927c4bb': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword draw_vb / Legacy Diffuse Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
        (update_hash,                   ('7eb1ca38',)),
    ],
'4dc4764e': [(log, ('3.0: YeShunguangTouchOfDawnlight Sword position_vb',)),         (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n'))],
'c8702180': [(log, ('3.0: YeShunguangTouchOfDawnlight Sword texcoord_vb',)),         (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n'))],
'5783614d': [(log, ('3.0: YeShunguangTouchOfDawnlight Sword blend_vb',)),            (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n'))],

# === Shared NormalMap ===
'798adba3': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('01ef4403', 'YeShunguangTouchOfDawnlight.Ears.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4df52aae', 'YeShunguangTouchOfDawnlight.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6dc6c880', 'YeShunguangTouchOfDawnlight.HairClips.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Torso.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9258d5f8', 'YeShunguangTouchOfDawnlight.HairTassels.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f383537b', 'YeShunguangTouchOfDawnlight.HairBow.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('38b3bd13', 'YeShunguangTouchOfDawnlight.BraidRibbons.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('999bff94', 'YeShunguangTouchOfDawnlight.Bangs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '6dc6c880', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '38b3bd13', '85d52cb7', '999bff94'), 'YeShunguangTouchOfDawnlight.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face and Brows Textures ===
'6ed0c951': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears and Bangs Textures ===
'79f6acd7': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight EarsA, BangsA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight EarsA, BangsA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight EarsA, BangsA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],

# === Legs and Tail Textures ===
'37c5aae5': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight LegsA, TailA Diffuse Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
    ],
'01e54e40': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight LegsA, TailA LightMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
    ],
'18370cad': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight LegsA, TailA MaterialMap Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
    ],

# === HairClips, Torso, and HairBow Textures ===
'956bcfbd': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA Diffuse Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'8e815da2': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA LightMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],
'2f2c27b5': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA MaterialMap Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
    ],

# === HairTassels, BraidRibbons, and RibbonFlower Textures ===
'8d400443': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA Diffuse Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'68e162a7': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA LightMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'fdd44e2a': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA MaterialMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],

# === Dress Textures ===
'f6d35967': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight DressA Diffuse Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
    ],
'405fa4b6': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight DressA LightMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
    ],
'e67e5577': [
        (log,                           ('2.8: YeShunguangTouchOfDawnlight DressA MaterialMap Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
    ],

# === Sword Textures (v3.0 Target) ===
'7eb1ca38': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword Diffuse Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'f9ec3ac8': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword Diffuse Hash [Legacy]',)),
        (update_hash,                   ('7eb1ca38',)),
    ],
'90250152': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword LightMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'9d2adcc5': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword LightMap Hash [Legacy]',)),
        (update_hash,                   ('90250152',)),
    ],
'0f21a6c9': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword LightMap Hash [Legacy] Alt',)),
        (update_hash,                   ('90250152',)),
    ],
'a355e13d': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword MaterialMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'4659445f': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword MaterialMap Hash [Legacy]',)),
        (update_hash,                   ('a355e13d',)),
    ],
'e6eab72f': [
        (log,                           ('2.8 -> 3.0: YeShunguangTouchOfDawnlight Sword MaterialMap Hash [Legacy] Alt',)),
        (update_hash,                   ('a355e13d',)),
    ],

# === Legacy 2.5 Texture Hashes ===
    'cc360f56': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('cc360f56', 'YeShunguangTouchOfDawnlight.BodyA.Diffuse.1024')),
    ],
    '8617f478': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('8617f478', 'YeShunguangTouchOfDawnlight.BodyA.LightMap.1024')),
    ],
    'b2efbac8': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('b2efbac8', 'YeShunguangTouchOfDawnlight.BodyA.MaterialMap.1024')),
    ],
    '03ed5c91': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('03ed5c91', 'YeShunguangTouchOfDawnlight.LegA.Diffuse.1024')),
    ],
    '4de697cf': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('4de697cf', 'YeShunguangTouchOfDawnlight.LegA.LightMap.1024')),
    ],
    'a7140533': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a7140533', 'YeShunguangTouchOfDawnlight.LegA.MaterialMap.1024')),
    ],
    'c87c6d8a': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight SkirtA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('c87c6d8a', 'YeShunguangTouchOfDawnlight.SkirtA.Diffuse.1024')),
    ],
    '043b86d0': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight SkirtA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('043b86d0', 'YeShunguangTouchOfDawnlight.SkirtA.LightMap.1024')),
    ],
    'a2ae050f': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight SkirtA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('a2ae050f', 'YeShunguangTouchOfDawnlight.SkirtA.MaterialMap.1024')),
    ],

# === Legacy 3.0 1024p Texture Hashes ===
    '3359b263': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight HairA, FrontHairA Diffuse 1024p Hash',)),
        (update_hash,                   ('79f6acd7',)),
        (multiply_section_if_missing,   (('79f6acd7', '3359b263'), 'YeShunguangTouchOfDawnlight.HairA.Diffuse.2048')),
    ],
    '3c140ab4': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight HairA, FrontHairA LightMap 1024p Hash',)),
        (update_hash,                   ('88269532',)),
        (multiply_section_if_missing,   (('88269532', '3c140ab4'), 'YeShunguangTouchOfDawnlight.HairA.LightMap.2048')),
    ],
    'c009d7c9': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight HairA, FrontHairA MaterialMap 1024p Hash',)),
        (update_hash,                   ('825fbf26',)),
        (multiply_section_if_missing,   (('825fbf26', 'c009d7c9'), 'YeShunguangTouchOfDawnlight.HairA.MaterialMap.2048')),
    ],
    '019fb20a': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight BraidA, HeadwearLongRibbonA, RibbonFlowerA Diffuse 1024p Hash',)),
        (update_hash,                   ('8d400443',)),
        (multiply_section_if_missing,   (('8d400443', '019fb20a'), 'YeShunguangTouchOfDawnlight.BraidA.Diffuse.2048')),
    ],
    '656d2415': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight BraidA, HeadwearLongRibbonA, RibbonFlowerA LightMap 1024p Hash',)),
        (update_hash,                   ('68e162a7',)),
        (multiply_section_if_missing,   (('68e162a7', '656d2415'), 'YeShunguangTouchOfDawnlight.BraidA.LightMap.2048')),
    ],
    '926bffd5': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight BraidA, HeadwearLongRibbonA, RibbonFlowerA MaterialMap 1024p Hash',)),
        (update_hash,                   ('fdd44e2a',)),
        (multiply_section_if_missing,   (('fdd44e2a', '926bffd5'), 'YeShunguangTouchOfDawnlight.BraidA.MaterialMap.2048')),
    ],
    '50f2ead2': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight FaceA, BrowsA Diffuse 1024p Hash',)),
        (update_hash,                   ('6ed0c951',)),
        (multiply_section_if_missing,   (('6ed0c951', '50f2ead2'), 'YeShunguangTouchOfDawnlight.FaceA.Diffuse.2048')),
    ],
    'f5e4bed0': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword Diffuse 1024p Hash',)),
        (update_hash,                   ('7eb1ca38',)),
        (multiply_section_if_missing,   (('7eb1ca38', 'f5e4bed0'), 'YeShunguangTouchOfDawnlight.Sword.Diffuse.2048')),
    ],
    'c2c54664': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword LightMap 1024p Hash',)),
        (update_hash,                   ('90250152',)),
        (multiply_section_if_missing,   (('90250152', 'c2c54664'), 'YeShunguangTouchOfDawnlight.Sword.LightMap.2048')),
    ],
    'ef4c4385': [
        (log,                           ('3.0: YeShunguangTouchOfDawnlight Sword MaterialMap 1024p Hash',)),
        (update_hash,                   ('a355e13d',)),
        (multiply_section_if_missing,   (('a355e13d', 'ef4c4385'), 'YeShunguangTouchOfDawnlight.Sword.MaterialMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangTouchOfDawnlight',
    'game_versions': ['2.8', '3.0'],
}