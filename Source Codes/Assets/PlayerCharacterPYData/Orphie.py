"""
Orphie Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json data
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Orphie's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'6988bfcd': [(log, ('2.5: Orphie Hair IB Hash',)), (add_ib_check_if_missing,)],
'a5eac582': [(log, ('2.5: Orphie Body IB Hash',)), (add_ib_check_if_missing,)],
'80017921': [(log, ('2.5: Orphie Legs IB Hash',)), (add_ib_check_if_missing,)],
'3766fa59': [(log, ('2.5: Orphie MagusTail IB Hash',)), (add_ib_check_if_missing,)],
'389256d8': [(log, ('2.5: Orphie MagusNozzle IB Hash',)), (add_ib_check_if_missing,)],
'2935f885': [(log, ('2.5: Orphie MagusDrum IB Hash',)), (add_ib_check_if_missing,)],
'ed85f33b': [(log, ('2.5: Orphie Face IB Hash',)), (add_ib_check_if_missing,)],

# Hair Textures
'ce52779f': [
        (log,                           ('2.5: Orphie HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('78d4038b', 'Orphie.HairA.Diffuse.1024')),
    ],

'78d4038b': [
        (log,                           ('2.5: Orphie HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ce52779f', 'Orphie.HairA.Diffuse.2048')),
    ],
'77abe83b': [
        (log,                           ('2.5: Orphie HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('643268b4', 'Orphie.HairA.LightMap.1024')),
    ],

'643268b4': [
        (log,                           ('2.5: Orphie HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('77abe83b', 'Orphie.HairA.LightMap.2048')),
    ],
'94ed2491': [
        (log,                           ('2.5: Orphie HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ef6e3a3b', 'Orphie.HairA.MaterialMap.1024')),
    ],

'ef6e3a3b': [
        (log,                           ('2.5: Orphie HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('94ed2491', 'Orphie.HairA.MaterialMap.2048')),
    ],

# Body Textures
'c9bea5d7': [
        (log,                           ('2.5: Orphie BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ca89cd72', 'Orphie.BodyA.Diffuse.1024')),
    ],

'ca89cd72': [
        (log,                           ('2.5: Orphie BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c9bea5d7', 'Orphie.BodyA.Diffuse.2048')),
    ],
'9a0406fe': [
        (log,                           ('2.5: Orphie BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c797a191', 'Orphie.BodyA.LightMap.1024')),
    ],

'c797a191': [
        (log,                           ('2.5: Orphie BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9a0406fe', 'Orphie.BodyA.LightMap.2048')),
    ],
'1daf926d': [
        (log,                           ('2.5: Orphie BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7f6aa298', 'Orphie.BodyA.MaterialMap.1024')),
    ],

'7f6aa298': [
        (log,                           ('2.5: Orphie BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1daf926d', 'Orphie.BodyA.MaterialMap.2048')),
    ],

# Legs Textures
'dd4120db': [
        (log,                           ('2.5: Orphie LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('aaeb5f0f', 'Orphie.HoverboardA.Diffuse.1024')),
    ],

'aaeb5f0f': [
        (log,                           ('2.5: Orphie LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('dd4120db', 'Orphie.HoverboardA.Diffuse.2048')),
    ],
'a9ae84df': [
        (log,                           ('2.5: Orphie LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ec3855fa', 'Orphie.HoverboardA.LightMap.1024')),
    ],

'ec3855fa': [
        (log,                           ('2.5: Orphie LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a9ae84df', 'Orphie.HoverboardA.LightMap.2048')),
    ],
'867ceb5b': [
        (log,                           ('2.5: Orphie LegsA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('70ff1eca', 'Orphie.HoverboardA.MaterialMap.1024')),
    ],

'70ff1eca': [
        (log,                           ('2.5: Orphie LegsA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('867ceb5b', 'Orphie.HoverboardA.MaterialMap.2048')),
    ],

# Magus Shared Textures (MagusTail, MagusNozzle, MagusDrum)
'dd80fa1d': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) Diffuse Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'92c6b20b': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) LightMap Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'cb65982e': [
        (log,                           ('2.5: Orphie Magus (Tail/Nozzle/Drum) MaterialMap Hash',)),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],

# Face Textures
'0df52ae7': [
        (log,                           ('2.5: Orphie FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('66efca96', 'Orphie.FaceA.Diffuse.1024')),
    ],

'66efca96': [
        (log,                           ('2.5: Orphie FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0df52ae7', 'Orphie.FaceA.Diffuse.2048')),
    ],

# Shared NormalMap (across all components)
'ebac056e': [
        (log,                           ('2.5: Orphie Shared NormalMap Hash',)),
        (add_section_if_missing,        ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('80017921', 'Orphie.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3766fa59', 'Orphie.MagusTail.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('389256d8', 'Orphie.MagusNozzle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2935f885', 'Orphie.MagusDrum.IB', 'match_priority = 0\n')),
    ],
'83c4fcaf': [
        (log, ('3.0: Orphie Hair VB Hash',)),
        (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'c721249c': [
        (log, ('3.0: Orphie Hair VB Hash',)),
        (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'bb2a1769': [
        (log, ('3.0: Orphie Hair VB Hash',)),
        (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'd98415dc': [(log, ('3.0: Orphie Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'79702a46': [
        (log, ('3.0: Orphie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd635bad0': [
        (log, ('3.0: Orphie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd8779413': [
        (log, ('3.0: Orphie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'48a78cdc': [
        (log, ('3.0: Orphie Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'd4b12374': [
        (log, ('3.0: Orphie Body VB Hash',)),
        (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'e0269fbf': [
        (log, ('3.0: Orphie Body VB Hash',)),
        (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'd31ae32f': [
        (log, ('3.0: Orphie Body VB Hash',)),
        (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'b823fb44': [
        (log, ('3.0: Orphie Body VB Hash',)),
        (add_section_if_missing, ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
    ],
'f7b4360a': [
        (log, ('3.0: Orphie Leg VB Hash',)),
        (add_section_if_missing, ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
    ],
'b4e15dc4': [
        (log, ('3.0: Orphie Leg VB Hash',)),
        (add_section_if_missing, ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
    ],
'f74b4cea': [
        (log, ('3.0: Orphie Leg VB Hash',)),
        (add_section_if_missing, ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
    ],
'5ca9ed4e': [
        (log, ('3.0: Orphie Leg VB Hash',)),
        (add_section_if_missing, ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
    ],
'1542fac0': [
        (log, ('3.0: Orphie Face VB Hash',)),
        (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],
'2f506987': [
        (log, ('3.0: Orphie Face VB Hash',)),
        (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],
'48191f72': [
        (log, ('3.0: Orphie Face VB Hash',)),
        (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],
'3cde4ca0': [
        (log, ('3.0: Orphie Face VB Hash',)),
        (add_section_if_missing, ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
    ],
'aa1404dd': [(log, ('3.0: Orphie dagger IB Hash',)), (add_ib_check_if_missing,)],
'6c9a0fb8': [
        (log, ('3.0: Orphie dagger VB Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'586b83df': [
        (log, ('3.0: Orphie dagger VB Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'6b263148': [
        (log, ('3.0: Orphie dagger VB Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'7c7fd13b': [
        (log, ('3.0: Orphie dagger VB Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'fea2bd55': [
        (log, ('3.0: Orphie Magustail VB Hash',)),
        (add_section_if_missing, ('3766fa59', 'Orphie.Magustail.IB', 'match_priority = 0\n')),
    ],
'f4a39978': [
        (log, ('3.0: Orphie Magustail VB Hash',)),
        (add_section_if_missing, ('3766fa59', 'Orphie.Magustail.IB', 'match_priority = 0\n')),
    ],
'f33946ec': [
        (log, ('3.0: Orphie Magustail VB Hash',)),
        (add_section_if_missing, ('3766fa59', 'Orphie.Magustail.IB', 'match_priority = 0\n')),
    ],
'203664d5': [
        (log, ('3.0: Orphie Magustail VB Hash',)),
        (add_section_if_missing, ('3766fa59', 'Orphie.Magustail.IB', 'match_priority = 0\n')),
    ],
'49393f27': [
        (log, ('3.0: Orphie Magushead VB Hash',)),
        (add_section_if_missing, ('2935f885', 'Orphie.Magushead.IB', 'match_priority = 0\n')),
    ],
'160ccb43': [
        (log, ('3.0: Orphie Magushead VB Hash',)),
        (add_section_if_missing, ('2935f885', 'Orphie.Magushead.IB', 'match_priority = 0\n')),
    ],
'43b63f81': [
        (log, ('3.0: Orphie Magushead VB Hash',)),
        (add_section_if_missing, ('2935f885', 'Orphie.Magushead.IB', 'match_priority = 0\n')),
    ],
'17077e99': [
        (log, ('3.0: Orphie Magushead VB Hash',)),
        (add_section_if_missing, ('2935f885', 'Orphie.Magushead.IB', 'match_priority = 0\n')),
    ],
'27b14e70': [
        (log, ('3.0: Orphie Magusmouth VB Hash',)),
        (add_section_if_missing, ('389256d8', 'Orphie.Magusmouth.IB', 'match_priority = 0\n')),
    ],
'aeeebb95': [
        (log, ('3.0: Orphie Magusmouth VB Hash',)),
        (add_section_if_missing, ('389256d8', 'Orphie.Magusmouth.IB', 'match_priority = 0\n')),
    ],
'5662dd65': [
        (log, ('3.0: Orphie Magusmouth VB Hash',)),
        (add_section_if_missing, ('389256d8', 'Orphie.Magusmouth.IB', 'match_priority = 0\n')),
    ],
'6fba1f7b': [
        (log, ('3.0: Orphie Magusmouth VB Hash',)),
        (add_section_if_missing, ('389256d8', 'Orphie.Magusmouth.IB', 'match_priority = 0\n')),
    ],
'e63d22c3': [(log, ('3.0: Orphie Maguseye IB Hash',)), (add_ib_check_if_missing,)],
'9f1dfc45': [
        (log, ('3.0: Orphie Hair VB Hash',)),
        (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Orphie Hair TEX Hash',)),
        (add_section_if_missing, ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
    ],
'c64aea70': [
        (log, ('3.0: Orphie dagger TEX Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'772b915b': [
        (log, ('3.0: Orphie dagger TEX Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
'c1650e3b': [
        (log, ('3.0: Orphie dagger TEX Hash',)),
        (add_section_if_missing, ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Orphie',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Legs', 'MagusTail', 'MagusNozzle', 'MagusDrum', 'Face'],
}
