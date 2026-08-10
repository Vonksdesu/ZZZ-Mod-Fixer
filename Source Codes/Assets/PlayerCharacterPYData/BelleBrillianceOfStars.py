"""
BelleBrillianceOfStars Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns BelleBrillianceOfStars's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'feb1c4cd': [
        (log,                           ('3.0: BelleBrillianceOfStars Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'62711f82': [
        (log,                           ('3.0: BelleBrillianceOfStars Earrings IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'0a843a8f': [
        (log,                           ('3.0: BelleBrillianceOfStars Hat IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'a318b3c6': [
        (log,                           ('3.0: BelleBrillianceOfStars Player IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b946c37f': [
        (log,                           ('3.0: BelleBrillianceOfStars Tie IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === BelleBrillianceOfStars Textures (BodyA) ===
'639ad374': [
        (log,                           ('3.0 -> 3.1: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('a292d07d', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
        (update_hash,                        ('d9dc65da',)),
    ],
'a292d07d': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('639ad374', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'd9dc65da': [
        (log,                           ('3.1: BelleBrillianceOfStars BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('fd906f9b', 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
    ],
'fd906f9b': [
        (log,                           ('3.1: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('d9dc65da', 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
    ],
'e1f357ec': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
    ],
'42310c0e': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
    ],
'7c1fb5f6': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
    ],
'5724e531': [
        (log,                           ('3.0: BelleBrillianceOfStars BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),
    ],

# === BelleBrillianceOfStars Textures (HatA) ===
'269a82f9': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
    ],
'8c0ea559': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
    ],
'a21dde78': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
    ],
'dcb8ba2e': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
    ],
'08453671': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
    ],
'57130f7c': [
        (log,                           ('3.0: BelleBrillianceOfStars HatA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
    ],
'aa9ffb85': [(log, ('3.0: BelleBrillianceOfStars Hair IB Hash',)), (add_ib_check_if_missing,)],
'992d149f': [
        (log, ('3.0: BelleBrillianceOfStars Hair VB Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'dbd537bb': [
        (log, ('3.0: BelleBrillianceOfStars Hair VB Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'0f1d7b96': [
        (log, ('3.0: BelleBrillianceOfStars Hair VB Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'2cf18f34': [
        (log, ('3.0: BelleBrillianceOfStars Hair VB Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'1ce58567': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'403eace9': [(log, ('3.0: BelleBrillianceOfStars HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'0a877d89': [
        (log, ('3.0: BelleBrillianceOfStars Hat VB Hash',)),
        (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
    ],
'74d2da11': [
        (log, ('3.0: BelleBrillianceOfStars Hat VB Hash',)),
        (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
    ],
'801cd45d': [
        (log, ('3.0: BelleBrillianceOfStars Hat VB Hash',)),
        (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
    ],
'd5070379': [
        (log, ('3.0: BelleBrillianceOfStars Hat VB Hash',)),
        (add_section_if_missing, ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
    ],
'29324995': [
        (log, ('3.0: BelleBrillianceOfStars Earrings VB Hash',)),
        (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'8da231b5': [
        (log, ('3.0: BelleBrillianceOfStars Earrings VB Hash',)),
        (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'611f1c52': [
        (log, ('3.0: BelleBrillianceOfStars Earrings VB Hash',)),
        (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
'6aa2848f': [
        (log, ('3.0: BelleBrillianceOfStars Tie VB Hash',)),
        (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
    ],
'88e81d00': [
        (log, ('3.0: BelleBrillianceOfStars Tie VB Hash',)),
        (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
    ],
'f83e837a': [
        (log, ('3.0: BelleBrillianceOfStars Tie VB Hash',)),
        (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
    ],
'd9087948': [
        (log, ('3.0: BelleBrillianceOfStars Player VB Hash',)),
        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
    ],
'1cfe1205': [
        (log, ('3.0: BelleBrillianceOfStars Player VB Hash',)),
        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
    ],
'82c81803': [
        (log, ('3.0: BelleBrillianceOfStars Player VB Hash',)),
        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
    ],
'df17d505': [
        (log, ('3.0: BelleBrillianceOfStars Body VB Hash',)),
        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'3e19f179': [
        (log, ('3.0: BelleBrillianceOfStars Body VB Hash',)),
        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'987395ef': [
        (log, ('3.0: BelleBrillianceOfStars Body VB Hash',)),
        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'a6431856': [(log, ('3.0: BelleBrillianceOfStars Neck IB Hash',)), (add_ib_check_if_missing,)],
'0e72bdb7': [
        (log, ('3.0: BelleBrillianceOfStars Neck VB Hash',)),
        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
    ],
'd5c6a50f': [
        (log, ('3.0: BelleBrillianceOfStars Neck VB Hash',)),
        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
    ],
'07a15f8e': [
        (log, ('3.0: BelleBrillianceOfStars Neck VB Hash',)),
        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
    ],
'57192494': [
        (log, ('3.0: BelleBrillianceOfStars Neck VB Hash',)),
        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
    ],
'9a9780a7': [(log, ('3.0: BelleBrillianceOfStars Face IB Hash',)), (add_ib_check_if_missing,)],
'04abceb5': [
        (log, ('3.0: BelleBrillianceOfStars Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'3eb95df2': [
        (log, ('3.0: BelleBrillianceOfStars Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'd3000b22': [
        (log, ('3.0: BelleBrillianceOfStars Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'228f5a8b': [
        (log, ('3.1: BelleBrillianceOfStars Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'359e4502': [
        (log, ('3.0: BelleBrillianceOfStars Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'75ec3614': [
        (log, ('3.0: BelleBrillianceOfStars Face TEX Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'08f04d95': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'7542ef4b': [
        (log, ('3.0: BelleBrillianceOfStars Hair TEX Hash',)),
        (add_section_if_missing, ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
    ],
'd9a12c0a': [
        (log, ('3.0: BelleBrillianceOfStars Neck TEX Hash',)),
        (add_section_if_missing, ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
    ],
'77eef7e8': [
        (log, ('3.0: BelleBrillianceOfStars Face TEX Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
    ],
'76ceb325': [
        (log, ('3.0: BelleBrillianceOfStars Body VB Hash',)),
        (add_section_if_missing, ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
    ],
'f6ed0e7b': [
        (log, ('3.0: BelleBrillianceOfStars Player VB Hash',)),
        (add_section_if_missing, ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
    ],
'c0ee97be': [
        (log, ('3.0: BelleBrillianceOfStars Tie VB Hash',)),
        (add_section_if_missing, ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
    ],
'e2c8decf': [
        (log, ('3.0: BelleBrillianceOfStars Earrings VB Hash',)),
        (add_section_if_missing, ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleBrillianceOfStars',
    'game_versions': ['3.0'],
}
