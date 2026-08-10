"""
YeShunguangTouchOfDawnlight Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
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
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'01ef4403': [(log, ('2.5: YeShunguangTouchOfDawnlight Ears IB Hash',)),          (add_ib_check_if_missing,)],
'4df52aae': [(log, ('2.5: YeShunguangTouchOfDawnlight Legs IB Hash',)),          (add_ib_check_if_missing,)],
'611df76d': [(log, ('2.5: YeShunguangTouchOfDawnlight Brows IB Hash',)),         (add_ib_check_if_missing,)],
'6dc6c880': [(log, ('2.5: YeShunguangTouchOfDawnlight HairClips IB Hash',)),     (add_ib_check_if_missing,)],
'869976a3': [(log, ('2.5: YeShunguangTouchOfDawnlight Tail IB Hash',)),          (add_ib_check_if_missing,)],
'8e7f72d5': [(log, ('2.5: YeShunguangTouchOfDawnlight Torso IB Hash',)),         (add_ib_check_if_missing,)],
'9258d5f8': [(log, ('2.5: YeShunguangTouchOfDawnlight HairTassels IB Hash',)),   (add_ib_check_if_missing,)],
'bafd232d': [(log, ('2.5: YeShunguangTouchOfDawnlight Dress IB Hash',)),         (add_ib_check_if_missing,)],
'c28e6303': [(log, ('2.5: YeShunguangTouchOfDawnlight Face IB Hash',)),          (add_ib_check_if_missing,)],
'f383537b': [(log, ('2.5: YeShunguangTouchOfDawnlight HairBow IB Hash',)),       (add_ib_check_if_missing,)],
'38b3bd13': [(log, ('2.5: YeShunguangTouchOfDawnlight BraidRibbons IB Hash',)),  (add_ib_check_if_missing,)],
'85d52cb7': [(log, ('2.5: YeShunguangTouchOfDawnlight RibbonFlower IB Hash',)),  (add_ib_check_if_missing,)],
'999bff94': [(log, ('2.5: YeShunguangTouchOfDawnlight Bangs IB Hash',)),         (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight Shared NormalMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '4df52aae', '6dc6c880', '869976a3', '8e7f72d5', '9258d5f8', 'bafd232d', 'f383537b', '38b3bd13', '85d52cb7', '999bff94'), 'YeShunguangTouchOfDawnlight.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Face and Brows Textures ===
'6ed0c951': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight FaceA, BrowsA Diffuse Hash',)),
        (add_section_if_missing,        (('c28e6303', '611df76d'), 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],

# === Ears and Bangs Textures (Shared Set 1) ===
'79f6acd7': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight EarsA, BangsA Diffuse Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'88269532': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight EarsA, BangsA LightMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],
'825fbf26': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight EarsA, BangsA MaterialMap Hash',)),
        (add_section_if_missing,        (('01ef4403', '999bff94'), 'YeShunguangTouchOfDawnlight.EarsBangs.IB', 'match_priority = 0\n')),
    ],

# === Legs and Tail Textures (Shared Set 2) ===
'37c5aae5': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('03ed5c91', 'YeShunguangTouchOfDawnlight.LegA.Diffuse.1024')),
    ],

'03ed5c91': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('37c5aae5', 'YeShunguangTouchOfDawnlight.LegA.Diffuse.2048')),
    ],
'01e54e40': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4de697cf', 'YeShunguangTouchOfDawnlight.LegA.LightMap.1024')),
    ],

'4de697cf': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('01e54e40', 'YeShunguangTouchOfDawnlight.LegA.LightMap.2048')),
    ],
'18370cad': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a7140533', 'YeShunguangTouchOfDawnlight.LegA.MaterialMap.1024')),
    ],

'a7140533': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight LegsA, TailA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('4df52aae', '869976a3'), 'YeShunguangTouchOfDawnlight.LegsTail.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('18370cad', 'YeShunguangTouchOfDawnlight.LegA.MaterialMap.2048')),
    ],

# === HairClips, Torso, and HairBow Textures (Shared Set 3) ===
'956bcfbd': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('cc360f56', 'YeShunguangTouchOfDawnlight.BodyA.Diffuse.1024')),
    ],

'cc360f56': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('956bcfbd', 'YeShunguangTouchOfDawnlight.BodyA.Diffuse.2048')),
    ],
'8e815da2': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8617f478', 'YeShunguangTouchOfDawnlight.BodyA.LightMap.1024')),
    ],

'8617f478': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8e815da2', 'YeShunguangTouchOfDawnlight.BodyA.LightMap.2048')),
    ],
'2f2c27b5': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b2efbac8', 'YeShunguangTouchOfDawnlight.BodyA.MaterialMap.1024')),
    ],

'b2efbac8': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairClipsA, TorsoA, HairBowA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('6dc6c880', '8e7f72d5', 'f383537b'), 'YeShunguangTouchOfDawnlight.ClipsTorsoBow.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2f2c27b5', 'YeShunguangTouchOfDawnlight.BodyA.MaterialMap.2048')),
    ],

# === HairTassels, BraidRibbons, and RibbonFlower Textures (Shared Set 4) ===
'8d400443': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA Diffuse Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'68e162a7': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA LightMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],
'fdd44e2a': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight HairTasselsA, BraidRibbonsA, RibbonFlowerA MaterialMap Hash',)),
        (add_section_if_missing,        (('9258d5f8', '38b3bd13', '85d52cb7'), 'YeShunguangTouchOfDawnlight.TasselsRibbons.IB', 'match_priority = 0\n')),
    ],

# === Dress Textures ===
'f6d35967': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c87c6d8a', 'YeShunguangTouchOfDawnlight.SkirtA.Diffuse.1024')),
    ],

'c87c6d8a': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f6d35967', 'YeShunguangTouchOfDawnlight.SkirtA.Diffuse.2048')),
    ],
'405fa4b6': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('043b86d0', 'YeShunguangTouchOfDawnlight.SkirtA.LightMap.1024')),
    ],

'043b86d0': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('405fa4b6', 'YeShunguangTouchOfDawnlight.SkirtA.LightMap.2048')),
    ],
'e67e5577': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a2ae050f', 'YeShunguangTouchOfDawnlight.SkirtA.MaterialMap.1024')),
    ],

'a2ae050f': [
        (log,                           ('2.5: YeShunguangTouchOfDawnlight DressA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bafd232d', 'YeShunguangTouchOfDawnlight.Dress.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e67e5577', 'YeShunguangTouchOfDawnlight.SkirtA.MaterialMap.2048')),
    ],
'f84ce9bf': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'afe311e8': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'e841684d': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'bdf6d0eb': [(log, ('3.0: YeShunguangTouchOfDawnlight HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'9e743bd7': [
        (log, ('3.0: YeShunguangTouchOfDawnlight HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
    ],
'520b7f22': [
        (log, ('3.0: YeShunguangTouchOfDawnlight HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
    ],
'af0e2b6e': [
        (log, ('3.0: YeShunguangTouchOfDawnlight HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
    ],
'1e57173e': [
        (log, ('3.0: YeShunguangTouchOfDawnlight HairShadow VB Hash',)),
        (add_section_if_missing, ('bdf6d0eb', 'YeShunguangTouchOfDawnlight.HairShadow.IB', 'match_priority = 0\n')),
    ],
'01d5a625': [
        (log, ('3.0: YeShunguangTouchOfDawnlight FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
    ],
'bba40575': [
        (log, ('3.0: YeShunguangTouchOfDawnlight FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
    ],
'bea60077': [
        (log, ('3.0: YeShunguangTouchOfDawnlight FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
    ],
'4ca25eef': [
        (log, ('3.0: YeShunguangTouchOfDawnlight FrontHair VB Hash',)),
        (add_section_if_missing, ('999bff94', 'YeShunguangTouchOfDawnlight.FrontHair.IB', 'match_priority = 0\n')),
    ],
'e05bf3a8': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'b871ef41': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'd7d41552': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'06e29dd2': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid VB Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'506b7080': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Body VB Hash',)),
        (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
    ],
'22213b25': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Body VB Hash',)),
        (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
    ],
'2a98d810': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Body VB Hash',)),
        (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
    ],
'b827643b': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Body VB Hash',)),
        (add_section_if_missing, ('8e7f72d5', 'YeShunguangTouchOfDawnlight.Body.IB', 'match_priority = 0\n')),
    ],
'b117fabb': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Leg VB Hash',)),
        (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
    ],
'38b4c4e8': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Leg VB Hash',)),
        (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
    ],
'ea5a39d1': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Leg VB Hash',)),
        (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
    ],
'352c95b2': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Leg VB Hash',)),
        (add_section_if_missing, ('4df52aae', 'YeShunguangTouchOfDawnlight.Leg.IB', 'match_priority = 0\n')),
    ],
'ff96a5d2': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Skirt VB Hash',)),
        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
    ],
'43eb20a0': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Skirt VB Hash',)),
        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
    ],
'1f27ab54': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Skirt VB Hash',)),
        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
    ],
'6468f592': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Skirt VB Hash',)),
        (add_section_if_missing, ('bafd232d', 'YeShunguangTouchOfDawnlight.Skirt.IB', 'match_priority = 0\n')),
    ],
'3fe83226': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
    ],
'9a2dfc61': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
    ],
'cb4b7cc7': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
    ],
'690ba2b1': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Tail VB Hash',)),
        (add_section_if_missing, ('869976a3', 'YeShunguangTouchOfDawnlight.Tail.IB', 'match_priority = 0\n')),
    ],
'0e30f719': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'7fd64a5b': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'7105bdbb': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'16a21c01': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('6dc6c880', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'7ccb6725': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'682c1e3c': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'1e3923d1': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'093ff56e': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('9258d5f8', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'3874c939': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'1b410367': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'e71ea768': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'ae7cced6': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Headwear VB Hash',)),
        (add_section_if_missing, ('f383537b', 'YeShunguangTouchOfDawnlight.Headwear.IB', 'match_priority = 0\n')),
    ],
'a203c8fa': [
        (log, ('3.0: YeShunguangTouchOfDawnlight RibbonFlower VB Hash',)),
        (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
    ],
'4c1d8708': [
        (log, ('3.0: YeShunguangTouchOfDawnlight RibbonFlower VB Hash',)),
        (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
    ],
'b8e7470f': [
        (log, ('3.0: YeShunguangTouchOfDawnlight RibbonFlower VB Hash',)),
        (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
    ],
'917a4c3e': [
        (log, ('3.0: YeShunguangTouchOfDawnlight RibbonFlower VB Hash',)),
        (add_section_if_missing, ('85d52cb7', 'YeShunguangTouchOfDawnlight.RibbonFlower.IB', 'match_priority = 0\n')),
    ],
'ba7164f5': [(log, ('3.0: YeShunguangTouchOfDawnlight TransparentCloth IB Hash',)), (add_ib_check_if_missing,)],
'b040f517': [
        (log, ('3.0: YeShunguangTouchOfDawnlight TransparentCloth VB Hash',)),
        (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'd98395a9': [
        (log, ('3.0: YeShunguangTouchOfDawnlight TransparentCloth VB Hash',)),
        (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'0925ae65': [
        (log, ('3.0: YeShunguangTouchOfDawnlight TransparentCloth VB Hash',)),
        (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'651d14a2': [
        (log, ('3.0: YeShunguangTouchOfDawnlight TransparentCloth VB Hash',)),
        (add_section_if_missing, ('ba7164f5', 'YeShunguangTouchOfDawnlight.TransparentCloth.IB', 'match_priority = 0\n')),
    ],
'9f0ab8cd': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'a5182b8a': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'287c161c': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f5daa764': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Eyebrow VB Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'2f2f9780': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],
'153d04c7': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],
'a1353cc8': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],
'fa261a46': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Face VB Hash',)),
        (add_section_if_missing, ('c28e6303', 'YeShunguangTouchOfDawnlight.Face.IB', 'match_priority = 0\n')),
    ],
'93c3c2b7': [(log, ('3.0: YeShunguangTouchOfDawnlight Sword IB Hash',)), (add_ib_check_if_missing,)],
'f927c4bb': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'4dc4764e': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'c8702180': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'5783614d': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword VB Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'7eb1ca38': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'90250152': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'a355e13d': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'3359b263': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair TEX Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair TEX Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'3c140ab4': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair TEX Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'c009d7c9': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair TEX Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
'019fb20a': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'656d2415': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'926bffd5': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Braid TEX Hash',)),
        (add_section_if_missing, ('38b3bd13', 'YeShunguangTouchOfDawnlight.Braid.IB', 'match_priority = 0\n')),
    ],
'50f2ead2': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Eyebrow TEX Hash',)),
        (add_section_if_missing, ('611df76d', 'YeShunguangTouchOfDawnlight.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f5e4bed0': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'c2c54664': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'ef4c4385': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Sword TEX Hash',)),
        (add_section_if_missing, ('93c3c2b7', 'YeShunguangTouchOfDawnlight.Sword.IB', 'match_priority = 0\n')),
    ],
'bd9b6102': [
        (log, ('3.0: YeShunguangTouchOfDawnlight Hair VB Hash',)),
        (add_section_if_missing, ('01ef4403', 'YeShunguangTouchOfDawnlight.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangTouchOfDawnlight',
    'game_versions': ['2.5'],
}
