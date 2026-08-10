"""
Seed Character Hash Commands
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
    Returns Seed's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'6cb35165': [(log, ('2.5: Seed Hair IB Hash',)),        (add_ib_check_if_missing,)],
'634ac589': [(log, ('2.5: Seed Body IB Hash',)),        (add_ib_check_if_missing,)],
'1d81bcc7': [(log, ('2.5: Seed Bib IB Hash',)),         (add_ib_check_if_missing,)],
'914e39c6': [(log, ('2.5: Seed Accessories IB Hash',)), (add_ib_check_if_missing,)],
'09d9dca7': [(log, ('2.5: Seed Face IB Hash',)),        (add_ib_check_if_missing,)],

# Face Textures
'f02ebff3': [
        (log,                           ('2.5: Seed FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a7e3da19', 'Seed.FaceA.Diffuse.1024')),
    ],

'a7e3da19': [
        (log,                           ('2.5: Seed FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f02ebff3', 'Seed.FaceA.Diffuse.2048')),
    ],

# Shared Textures (Hair, Bib, Accessories)
'2fff22a7': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9d4019f4', 'Seed.HairA.Diffuse.1024')),
    ],

'9d4019f4': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2fff22a7', 'Seed.HairA.Diffuse.2048')),
    ],
'bf2c273a': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e7efee45', 'Seed.HairA.LightMap.1024')),
    ],

'e7efee45': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bf2c273a', 'Seed.HairA.LightMap.2048')),
    ],
'a1658bbd': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bfcfcdc6', 'Seed.HairA.MaterialMap.1024')),
    ],

'bfcfcdc6': [
        (log,                           ('2.5: Seed HairA, BibA, AccessoriesA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a1658bbd', 'Seed.HairA.MaterialMap.2048')),
    ],

# Body Textures
'7c7c2622': [
        (log,                           ('2.5: Seed BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('684d2bd5', 'Seed.BodyA.Diffuse.1024')),
    ],

'684d2bd5': [
        (log,                           ('2.5: Seed BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7c7c2622', 'Seed.BodyA.Diffuse.2048')),
    ],
'b14c9c6f': [
        (log,                           ('2.5: Seed BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('522ee460', 'Seed.BodyA.LightMap.1024')),
    ],

'522ee460': [
        (log,                           ('2.5: Seed BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b14c9c6f', 'Seed.BodyA.LightMap.2048')),
    ],
'da2deeaa': [
        (log,                           ('2.5: Seed BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('be9dd4c2', 'Seed.BodyA.MaterialMap.1024')),
    ],

'be9dd4c2': [
        (log,                           ('2.5: Seed BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('da2deeaa', 'Seed.BodyA.MaterialMap.2048')),
    ],

# Shared NormalMap (Hair, Body, Bib, Accessories)
'ebac056e': [
        (log,                           ('2.5: Seed Shared NormalMap Hash',)),
        (add_section_if_missing,        ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1d81bcc7', 'Seed.Bib.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],

# Resolusi tambahan (1024p/2048p)

'74b9c4c8': [
        (log,                           ('2.5: Seed HoverboardA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('91d18cf9', 'Seed.HoverboardA.Diffuse.2048')),
    ],

'91d18cf9': [
        (log,                           ('2.5: Seed HoverboardA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('74b9c4c8', 'Seed.HoverboardA.Diffuse.1024')),
    ],

'bd0f0925': [
        (log,                           ('2.5: Seed HoverboardA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('a6726612', 'Seed.HoverboardA.LightMap.2048')),
    ],

'a6726612': [
        (log,                           ('2.5: Seed HoverboardA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('bd0f0925', 'Seed.HoverboardA.LightMap.1024')),
    ],

'7f7b60c9': [
        (log,                           ('2.5: Seed HoverboardA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('9896a7c2', 'Seed.HoverboardA.MaterialMap.2048')),
    ],

'9896a7c2': [
        (log,                           ('2.5: Seed HoverboardA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('7f7b60c9', 'Seed.HoverboardA.MaterialMap.1024')),
    ],
'651f4fd5': [(log, ('2.5: Seed Hoverboard IB Hash',)), (add_ib_check_if_missing,)],
'12bd16f4': [
        (log, ('3.0: Seed Hair VB Hash',)),
        (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
    ],
'25a8bde2': [
        (log, ('3.0: Seed Hair VB Hash',)),
        (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
    ],
'9e25742c': [
        (log, ('3.0: Seed Hair VB Hash',)),
        (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
    ],
'afe31e96': [
        (log, ('3.0: Seed Hair VB Hash',)),
        (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
    ],
'468e0f21': [(log, ('3.0: Seed Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'4d61e6f3': [
        (log, ('3.0: Seed Hair Shadow VB Hash',)),
        (add_section_if_missing, ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'3a097353': [
        (log, ('3.0: Seed Hair Shadow VB Hash',)),
        (add_section_if_missing, ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9f4d4106': [
        (log, ('3.0: Seed Hair Shadow VB Hash',)),
        (add_section_if_missing, ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'1abfa087': [
        (log, ('3.0: Seed Hair Shadow VB Hash',)),
        (add_section_if_missing, ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'43185be9': [
        (log, ('3.0: Seed Body VB Hash',)),
        (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'5e2f1e06': [
        (log, ('3.0: Seed Body VB Hash',)),
        (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'f4cf83ff': [
        (log, ('3.0: Seed Body VB Hash',)),
        (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'5b3d022f': [
        (log, ('3.0: Seed Body VB Hash',)),
        (add_section_if_missing, ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
    ],
'c24ebf3b': [
        (log, ('3.0: Seed Accessories VB Hash',)),
        (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'12d6c223': [
        (log, ('3.0: Seed Accessories VB Hash',)),
        (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'99be167f': [
        (log, ('3.0: Seed Accessories VB Hash',)),
        (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'746e7bf8': [
        (log, ('3.0: Seed Accessories VB Hash',)),
        (add_section_if_missing, ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
    ],
'72fbbba3': [
        (log, ('3.0: Seed ChestClothing VB Hash',)),
        (add_section_if_missing, ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
    ],
'b2690ac8': [
        (log, ('3.0: Seed ChestClothing VB Hash',)),
        (add_section_if_missing, ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
    ],
'2f706a18': [
        (log, ('3.0: Seed ChestClothing VB Hash',)),
        (add_section_if_missing, ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
    ],
'319ba025': [
        (log, ('3.0: Seed ChestClothing VB Hash',)),
        (add_section_if_missing, ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
    ],
'95941dba': [
        (log, ('3.0: Seed SelfBalancingScooter VB Hash',)),
        (add_section_if_missing, ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
    ],
'4635f4f0': [
        (log, ('3.0: Seed SelfBalancingScooter VB Hash',)),
        (add_section_if_missing, ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
    ],
'547acb7e': [
        (log, ('3.0: Seed SelfBalancingScooter VB Hash',)),
        (add_section_if_missing, ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
    ],
'064aa73b': [
        (log, ('3.0: Seed Face VB Hash',)),
        (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],
'3c58347c': [
        (log, ('3.0: Seed Face VB Hash',)),
        (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],
'a0dfaf80': [
        (log, ('3.0: Seed Face VB Hash',)),
        (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],
'7625e6d6': [
        (log, ('3.0: Seed Face VB Hash',)),
        (add_section_if_missing, ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
    ],
'c7f4f4ec': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'0238f9fc': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'8bb86a2d': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'5abfc179': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'b6b679de': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'a06afdbc': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'dd157642': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'54a8ad89': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'75e1ae0a': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'5bca6676': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'567f9bcd': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'030e0aca': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'10c13253': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'b2e81a28': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'6f269065': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'ceb90df0': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'b3f47664': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'b7c36a17': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'e2694177': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'efc82ade': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'09c28e33': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'0a4cecd8': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'1962d85c': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'64bb6cb7': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'126bd0a1': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'e0736df2': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'fdfdf144': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'255a77a9': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'98f46d5b': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'a065222f': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'f56f3ac1': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'caf87ff4': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'71e8d07a': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'c6043e88': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'143481a0': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'd06b00ad': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'd3adb384': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'a9a40828': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'd6e62b3f': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'bc0bd24c': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'8a995990': [(log, ('3.0: Seed weapon IB Hash',)), (add_ib_check_if_missing,)],
'3253babd': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('8a995990', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'f66c29e6': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('8a995990', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'72329a18': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('8a995990', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'8cb92072': [
        (log, ('3.0: Seed weapon VB Hash',)),
        (add_section_if_missing, ('8a995990', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Seed Hair TEX Hash',)),
        (add_section_if_missing, ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
    ],
'11be1be8': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'c7a71ca0': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'6cdfa1b1': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('c7f4f4ec', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'd8e36eca': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'bb3bae0e': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'efeed071': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('75e1ae0a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'a44bbeb3': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'3d66757d': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'5fa93693': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('b3f47664', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'93c858df': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'494e24a6': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'7832e989': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('126bd0a1', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'2e2a9097': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'cc24383a': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'4be2f394': [
        (log, ('3.0: Seed weapon TEX Hash',)),
        (add_section_if_missing, ('71e8d07a', 'Seed.weapon.IB', 'match_priority = 0\n')),
    ],
'2d77a8c9': [
        (log, ('3.0: Seed SelfBalancingScooter VB Hash',)),
        (add_section_if_missing, ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seed',
    'game_versions': ['2.5'],
}
