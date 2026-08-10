"""
Alice Character Hash Commands
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
    Returns Alice's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'd131acb1': [(log, ('2.5: Alice Hair IB Hash',)), (add_ib_check_if_missing,)],
'8a512b21': [(log, ('2.5: Alice Body IB Hash',)), (add_ib_check_if_missing,)],
'625c2692': [(log, ('2.5: Alice Legs IB Hash',)), (add_ib_check_if_missing,)],
'993d2ddd': [(log, ('2.5: Alice Sensor IB Hash',)), (add_ib_check_if_missing,)],
'bd2277ef': [(log, ('2.5: Alice Backpack IB Hash',)), (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.5: Alice Face IB Hash',)), (add_ib_check_if_missing,)],
'9f3e582c': [
        (log,                           ('2.5: Alice FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('33fdeb6d', 'Alice.FaceA.Diffuse.1024')),
    ],

'33fdeb6d': [
        (log,                           ('2.5: Alice FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9f3e582c', 'Alice.FaceA.Diffuse.2048')),
    ],
'705caac9': [
        (log,                           ('2.5: Alice HairA, LegsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('5f504114', '91d2f9fd'), 'Alice.HairA.Diffuse.1024')),
    ],

'91d2f9fd': [
        (log,                           ('2.5: Alice HairA, LegsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('705caac9', 'Alice.HairA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Alice HairA, LegsA, BodyA, BackpackA NormalMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.5: Alice HairA, LegsA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6c957d8f', 'Alice.HairA.LightMap.1024')),
    ],

'6c957d8f': [
        (log,                           ('2.5: Alice HairA, LegsA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('03543db2', 'Alice.HairA.LightMap.2048')),
    ],
'508530fe': [
        (log,                           ('2.5: Alice HairA, LegsA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bc4c87fd', 'Alice.HairA.MaterialMap.1024')),
    ],

'bc4c87fd': [
        (log,                           ('2.5: Alice HairA, LegsA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('508530fe', 'Alice.HairA.MaterialMap.2048')),
    ],
'269185ed': [
        (log,                           ('2.5: Alice BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9201609a', 'Alice.BodyA.Diffuse.1024')),
    ],

'9201609a': [
        (log,                           ('2.5: Alice BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('269185ed', 'Alice.BodyA.Diffuse.2048')),
    ],
'0d72cb85': [
        (log,                           ('2.5: Alice BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('548623cd', 'Alice.BodyA.LightMap.1024')),
    ],

'548623cd': [
        (log,                           ('2.5: Alice BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0d72cb85', 'Alice.BodyA.LightMap.2048')),
    ],
'95967afb': [
        (log,                           ('2.5: Alice BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e05e4c54', 'Alice.BodyA.MaterialMap.1024')),
    ],

'e05e4c54': [
        (log,                           ('2.5: Alice BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('95967afb', 'Alice.BodyA.MaterialMap.2048')),
    ],
'79cbbcc4': [
        (log,                           ('2.5: Alice BackpackA Diffuse Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'a226ce08': [
        (log,                           ('2.5: Alice BackpackA LightMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'9ada942b': [
        (log,                           ('2.5: Alice BackpackA MaterialMap Hash',)),
        (add_section_if_missing,        ('bd2277ef', 'Alice.Backpack.IB', 'match_priority = 0\n')),
    ],
'ad686c31': [
        (log, ('3.0: Alice Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
    ],
'b86d14b0': [
        (log, ('3.0: Alice Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
    ],
'cf1202fd': [
        (log, ('3.0: Alice Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
    ],
'ebbe2894': [(log, ('3.0: Alice Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'd482d732': [
        (log, ('3.0: Alice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a3fb836a': [
        (log, ('3.0: Alice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'85fb0c65': [
        (log, ('3.0: Alice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'14c96dd0': [
        (log, ('3.0: Alice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'7a318f3d': [
        (log, ('3.0: Alice Body VB Hash',)),
        (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'37a05757': [
        (log, ('3.0: Alice Body VB Hash',)),
        (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'9ad7d70c': [
        (log, ('3.0: Alice Body VB Hash',)),
        (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'15935e48': [
        (log, ('3.0: Alice Body VB Hash',)),
        (add_section_if_missing, ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
    ],
'3e4c0174': [
        (log, ('3.0: Alice Legs VB Hash',)),
        (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'c1aaa893': [
        (log, ('3.0: Alice Legs VB Hash',)),
        (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'2821afc9': [
        (log, ('3.0: Alice Legs VB Hash',)),
        (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'a1b46da2': [
        (log, ('3.0: Alice Legs VB Hash',)),
        (add_section_if_missing, ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
    ],
'c2b0bfbd': [
        (log, ('3.0: Alice BeltAcc VB Hash',)),
        (add_section_if_missing, ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'd0867379': [
        (log, ('3.0: Alice BeltAcc VB Hash',)),
        (add_section_if_missing, ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'd72a4315': [
        (log, ('3.0: Alice BeltAcc VB Hash',)),
        (add_section_if_missing, ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'73b54620': [
        (log, ('3.0: Alice BeltAcc VB Hash',)),
        (add_section_if_missing, ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'bf0e4dab': [
        (log, ('3.0: Alice BeltAcc TEX Hash',)),
        (add_section_if_missing, ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'03090c30': [
        (log, ('3.0: Alice BackAcc VB Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'23712d3d': [
        (log, ('3.0: Alice BackAcc VB Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'1c272241': [
        (log, ('3.0: Alice BackAcc VB Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'37717c75': [
        (log, ('3.0: Alice BackAcc VB Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'70088a4a': [
        (log, ('3.0: Alice Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'4a1a190d': [
        (log, ('3.0: Alice Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'7c9dbd4a': [
        (log, ('3.0: Alice Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'2326355e': [
        (log, ('3.0: Alice Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
    ],
'30205a68': [(log, ('3.0: Alice sword IB Hash',)), (add_ib_check_if_missing,)],
'f26a8aac': [
        (log, ('3.0: Alice sword VB Hash',)),
        (add_section_if_missing, ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
    ],
'47a48c42': [
        (log, ('3.0: Alice sword VB Hash',)),
        (add_section_if_missing, ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
    ],
'7b3126b6': [
        (log, ('3.0: Alice sword VB Hash',)),
        (add_section_if_missing, ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
    ],
'bb487b00': [
        (log, ('3.0: Alice sword VB Hash',)),
        (add_section_if_missing, ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
    ],
'323b1a95': [(log, ('3.0: Alice handguardPlate IB Hash',)), (add_ib_check_if_missing,)],
'0a06059e': [
        (log, ('3.0: Alice handguardPlate VB Hash',)),
        (add_section_if_missing, ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
    ],
'bd544be3': [
        (log, ('3.0: Alice handguardPlate VB Hash',)),
        (add_section_if_missing, ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
    ],
'9a136061': [
        (log, ('3.0: Alice handguardPlate VB Hash',)),
        (add_section_if_missing, ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
    ],
'aac53ae5': [
        (log, ('3.0: Alice handguardPlate VB Hash',)),
        (add_section_if_missing, ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Alice Hair TEX Hash',)),
        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
    ],
'228bdc7c': [
        (log, ('3.0: Alice BackAcc TEX Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'980c7ed0': [
        (log, ('3.0: Alice BackAcc TEX Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'072eabe7': [
        (log, ('3.0: Alice BackAcc TEX Hash',)),
        (add_section_if_missing, ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
    ],
'd515e182': [
        (log, ('3.0: Alice Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Alice',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
