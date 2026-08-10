"""
Banyue Character Hash Commands
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
    Returns Banyue's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==================== Hair Component ====================
'f3b6e869': [(log, ('2.5: Banyue Hair IB Hash',)), (add_ib_check_if_missing,)],
'0a1f42fb': [
        (log,                           ('2.5: Banyue HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fc9c6235', 'Banyue.HeadA.Diffuse.1024')),
    ],

'fc9c6235': [
        (log,                           ('2.5: Banyue HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0a1f42fb', 'Banyue.HeadA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Banyue Hair/Legs/Body NormalMap Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
    ],
'81cd7414': [
        (log,                           ('2.5: Banyue HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6c0d6d52', 'Banyue.HeadA.LightMap.1024')),
    ],

'6c0d6d52': [
        (log,                           ('2.5: Banyue HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('81cd7414', 'Banyue.HeadA.LightMap.2048')),
    ],
'ef8ba12a': [
        (log,                           ('2.5: Banyue HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ca2b8ca8', 'Banyue.HeadA.MaterialMap.1024')),
    ],

'ca2b8ca8': [
        (log,                           ('2.5: Banyue HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f3b6e869', 'Banyue.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ef8ba12a', 'Banyue.HeadA.MaterialMap.2048')),
    ],

# ==================== Legs Component ====================
'5f855404': [(log, ('2.5: Banyue Legs IB Hash',)), (add_ib_check_if_missing,)],
'a75cf25e': [
        (log,                           ('2.5: Banyue LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('950ca70a', 'Banyue.LegA.Diffuse.1024')),
    ],

'950ca70a': [
        (log,                           ('2.5: Banyue LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a75cf25e', 'Banyue.LegA.Diffuse.2048')),
    ],
# Note: ebac056e NormalMap is shared with Hair and Body components above
'1003c4df': [
        (log,                           ('2.5: Banyue LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('62c9fcaa', 'Banyue.LegA.LightMap.1024')),
    ],

'62c9fcaa': [
        (log,                           ('2.5: Banyue LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1003c4df', 'Banyue.LegA.LightMap.2048')),
    ],
'1125ccff': [
        (log,                           ('2.5: Banyue LegsA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8b0fcc7b', 'Banyue.LegA.MaterialMap.1024')),
    ],

'8b0fcc7b': [
        (log,                           ('2.5: Banyue LegsA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('5f855404', 'Banyue.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1125ccff', 'Banyue.LegA.MaterialMap.2048')),
    ],

# ==================== Body Component ====================
'698046e6': [(log, ('2.5: Banyue Body IB Hash',)), (add_ib_check_if_missing,)],
'19c3125c': [
        (log,                           ('2.5: Banyue BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b3b968a5', 'Banyue.BodyA.Diffuse.1024')),
    ],

'b3b968a5': [
        (log,                           ('2.5: Banyue BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('19c3125c', 'Banyue.BodyA.Diffuse.2048')),
    ],
# Note: ebac056e NormalMap is shared with Hair and Legs components above
'f44f6316': [
        (log,                           ('2.5: Banyue BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('cdecf7ef', 'Banyue.BodyA.LightMap.1024')),
    ],

'cdecf7ef': [
        (log,                           ('2.5: Banyue BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f44f6316', 'Banyue.BodyA.LightMap.2048')),
    ],
'7099d2dc': [
        (log,                           ('2.5: Banyue BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('77d743f8', 'Banyue.BodyA.MaterialMap.1024')),
    ],

'77d743f8': [
        (log,                           ('2.5: Banyue BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7099d2dc', 'Banyue.BodyA.MaterialMap.2048')),
    ],

# Resolusi tambahan (1024p/2048p)

'b91ab7b9': [
        (log,                           ('2.5: Banyue BothArmsA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('d6a9d46e', 'Banyue.BothArmsA.Diffuse.2048')),
    ],

'd6a9d46e': [
        (log,                           ('2.5: Banyue BothArmsA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('b91ab7b9', 'Banyue.BothArmsA.Diffuse.1024')),
    ],

'a2b682d6': [
        (log,                           ('2.5: Banyue BothArmsA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('46d2edd3', 'Banyue.BothArmsA.LightMap.2048')),
    ],

'46d2edd3': [
        (log,                           ('2.5: Banyue BothArmsA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('a2b682d6', 'Banyue.BothArmsA.LightMap.1024')),
    ],

'd6ac66fa': [
        (log,                           ('2.5: Banyue BothArmsA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('721a29de', 'Banyue.BothArmsA.MaterialMap.2048')),
    ],

'721a29de': [
        (log,                           ('2.5: Banyue BothArmsA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d6ac66fa', 'Banyue.BothArmsA.MaterialMap.1024')),
    ],
'635709b5': [(log, ('2.5: Banyue BothArms IB Hash',)), (add_ib_check_if_missing,)],
'1aab74cc': [
        (log, ('3.0: Banyue Body VB Hash',)),
        (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'6fab5f8b': [
        (log, ('3.0: Banyue Body VB Hash',)),
        (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'9b4cef87': [
        (log, ('3.0: Banyue Body VB Hash',)),
        (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'dba0d45e': [
        (log, ('3.0: Banyue Body VB Hash',)),
        (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'121a1aa7': [
        (log, ('3.0: Banyue BothArms VB Hash',)),
        (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
'd17bb604': [
        (log, ('3.0: Banyue BothArms VB Hash',)),
        (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
'0bc8c485': [
        (log, ('3.0: Banyue BothArms VB Hash',)),
        (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
'dc2a8ff5': [
        (log, ('3.0: Banyue Leg VB Hash',)),
        (add_section_if_missing, ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
    ],
'132c3f5c': [
        (log, ('3.0: Banyue Leg VB Hash',)),
        (add_section_if_missing, ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
    ],
'edc17446': [
        (log, ('3.0: Banyue Leg VB Hash',)),
        (add_section_if_missing, ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
    ],
'8be7477c': [
        (log, ('3.0: Banyue Face VB Hash',)),
        (add_section_if_missing, ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
    ],
'ec9b7916': [
        (log, ('3.0: Banyue Face VB Hash',)),
        (add_section_if_missing, ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
    ],
'bafd83bb': [
        (log, ('3.0: Banyue Face VB Hash',)),
        (add_section_if_missing, ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
    ],
'084eb825': [(log, ('3.0: Banyue PalmsBall IB Hash',)), (add_ib_check_if_missing,)],
'16698b4f': [
        (log, ('3.0: Banyue PalmsBall VB Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'679f2627': [
        (log, ('3.0: Banyue PalmsBall VB Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'daf0e9f9': [
        (log, ('3.0: Banyue PalmsBall VB Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'3a3a9a42': [
        (log, ('3.0: Banyue PalmsBall VB Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'3b8e4eda': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'4a7ef137': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'cc671a53': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'9bb1eb14': [(log, ('3.0: Banyue WeaponBall IB Hash',)), (add_ib_check_if_missing,)],
'00f0ed60': [
        (log, ('3.0: Banyue WeaponBall VB Hash',)),
        (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'289bb2ef': [
        (log, ('3.0: Banyue WeaponBall VB Hash',)),
        (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'd6d66d05': [
        (log, ('3.0: Banyue WeaponBall VB Hash',)),
        (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'48237f26': [
        (log, ('3.0: Banyue WeaponBall VB Hash',)),
        (add_section_if_missing, ('9bb1eb14', 'Banyue.WeaponBall.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Banyue Body TEX Hash',)),
        (add_section_if_missing, ('698046e6', 'Banyue.Body.IB', 'match_priority = 0\n')),
    ],
'd70384d8': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'1be5d33e': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'a0df0d6c': [
        (log, ('3.0: Banyue PalmsBall TEX Hash',)),
        (add_section_if_missing, ('084eb825', 'Banyue.PalmsBall.IB', 'match_priority = 0\n')),
    ],
'0a12bb17': [
        (log, ('3.0: Banyue Face VB Hash',)),
        (add_section_if_missing, ('f3b6e869', 'Banyue.Face.IB', 'match_priority = 0\n')),
    ],
'ae8abe08': [
        (log, ('3.0: Banyue Leg VB Hash',)),
        (add_section_if_missing, ('5f855404', 'Banyue.Leg.IB', 'match_priority = 0\n')),
    ],
'8e08205b': [
        (log, ('3.0: Banyue BothArms VB Hash',)),
        (add_section_if_missing, ('635709b5', 'Banyue.BothArms.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Banyue',
    'element': 'Fire',
    'faction': 'Yunkui Summit',
    'game_versions': ['2.5'],
}
