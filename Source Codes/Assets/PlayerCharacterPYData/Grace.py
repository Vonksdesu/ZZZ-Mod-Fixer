"""
Grace Character Hash Commands
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
    Returns Grace's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'89299f56': [(log, ('1.0: Grace Hair IB Hash',)), (add_ib_check_if_missing,)],
'8b240678': [(log, ('1.2: Grace Body IB Hash',)), (add_ib_check_if_missing,)],
'4d60568b': [(log, ('1.0: Grace Head IB Hash',)), (add_ib_check_if_missing,)],
'50837a5c': [(log, ('1.1 -> 1.2: Grace Body Blend Hash',)),     (update_hash, ('3b80154c',))],
'89d903ba': [(log, ('1.2 -> 1.3: Grace Hair Texcoord Hash',)),  (update_hash, ('d21f32ad',))],
'd21f32ad': [
        (log, ('1.1 -> 1.2: Grace Hair Texcoord Hash',)),
        (update_hash, ('89d903ba',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'e5e04f6f': [(log, ('1.1 -> 1.2: Grace Body Draw Hash',)),     (update_hash, ('f1cba806',))],
'26ffa186': [
        (log, ('1.1 -> 1.2: Grace Body Position Hash',)),
        (update_hash, ('8855c5cf',)),
        (log, ('1.1 -> 1.2: Grace Body Blend Remap',)),
        (update_buffer_blend_indices, (
            '8855c5cf',
            (35, 34, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,  68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89),
            (34, 35, 80, 85, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 51, 47, 48, 49, 50, 52, 54, 53, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66,  65, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 89, 78, 79, 81, 82, 83, 84, 86, 87, 88),
        ))
    ],
'e536af35': [(log, ('1.1 -> 1.2: Grace Body Texcoord Hash',)), (update_hash, ('4bb45448',))],
'0f82a13e': [
        (log, ('1.1 -> 1.2: Grace Body IB Hash',)),
        (update_hash, ('8b240678',)),
        (transfer_indexed_sections, {
            'src_indices': ['0', '42885'],
            'trg_indices': ['0', '42927'],
        })
    ],
'e75590cb': [
        (log,                           ('1.0: Grace HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4d60568b', 'Grace.HeadA.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7459ecf4', 'Grace.HeadA.Diffuse.2048')),
    ],
'7459ecf4': [
        (log,                           ('2.5: Grace HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4d60568b', 'Grace.HeadA.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e75590cb', 'Grace.HeadA.Diffuse.1024')),
    ],
'a87d2822': [
        (log,                           ('2.5: Grace HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('94d04401', 'Grace.HairA.Diffuse.1024')),
    ],
'94d04401': [
        (log,                           ('1.0: Grace HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a87d2822', 'Grace.HairA.Diffuse.2048')),
    ],
'8eddd041': [
        (log,                           ('1.0 -> 2.5: Grace HairA LightMap 2048p Hash',)),
        (update_hash,                   ('a22d2c2c',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('26bf1588', 'Grace.HairA.LightMap.1024')),
    ],
'a22d2c2c': [
        (log,                           ('2.5: Grace HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('26bf1588', 'Grace.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('48c17612', '26bf1588'), 'Grace.HairA.LightMap.1024')),
    ],

'48c17612': [
        (log,                           ('2.5: Grace HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('26bf1588', 'Grace.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('a22d2c2c', '8eddd041'), 'Grace.HairA.LightMap.2048')),
    ],
'26bf1588': [
        (log,                           ('1.0: Grace HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('8eddd041', 'a22d2c2c'), 'Grace.HairA.LightMap.2048')),
    ],
'3a38f6f9': [
        (log,                           ('1.0 -> 2.5: Grace HairA MaterialMap 2048p Hash',)),
        (update_hash,                   ('7bb81a4f',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e1cb3739', 'Grace.HairA.MaterialMap.1024')),
    ],
'7bb81a4f': [
        (log,                           ('2.5: Grace HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e1cb3739', 'Grace.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('381930fe', 'e1cb3739'), 'Grace.HairA.MaterialMap.1024')),
    ],

'381930fe': [
        (log,                           ('2.5: Grace HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e1cb3739', 'Grace.HairA.MaterialMap.1024')),
        (multiply_section_if_missing,        (('7bb81a4f', '3a38f6f9'), 'Grace.HairA.MaterialMap.2048')),
    ],
'e1cb3739': [
        (log,                           ('1.0: Grace HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('3a38f6f9', '7bb81a4f'), 'Grace.HairA.MaterialMap.2048')),
    ],
'846fab9a': [
        (log,                           ('1.0 -> 2.5: Grace HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1c4079f7', 'Grace.HairA.NormalMap.1024')),
    ],
'ebac056e': [
        (log,                           ('2.5: Grace HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1c4079f7', 'Grace.HairA.NormalMap.1024')),
    ],
'1c4079f7': [
        (log,                           ('1.0: Grace HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('846fab9a', 'ebac056e'), 'Grace.HairA.NormalMap.2048')),
    ],
'6d6ac4f4': [
        (log,                           ('2.5: Grace BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('397a8aed', 'Grace.BodyA.Diffuse.1024')),
    ],
'397a8aed': [
        (log,                           ('1.0: Grace BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6d6ac4f4', 'Grace.BodyA.Diffuse.2048')),
    ],
'993fe3e1': [
        (log,                           ('1.0 -> 2.5: Grace BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('895fa458',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('59dd8899', 'Grace.BodyA.LightMap.1024')),
    ],
'895fa458': [
        (log,                           ('2.5: Grace BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('59dd8899', 'Grace.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('7e2e15b3', '59dd8899'), 'Grace.BodyA.LightMap.1024')),
    ],

'7e2e15b3': [
        (log,                           ('2.5: Grace BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('59dd8899', 'Grace.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('895fa458', '993fe3e1'), 'Grace.BodyA.LightMap.2048')),
    ],
'59dd8899': [
        (log,                           ('1.0: Grace BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('993fe3e1', '895fa458'), 'Grace.BodyA.LightMap.2048')),
    ],
'e8345f2c': [
        (log,                           ('2.5: Grace BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a6c8c203', 'Grace.BodyA.MaterialMap.1024')),
    ],
'a6c8c203': [
        (log,                           ('1.0: Grace BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e8345f2c', 'Grace.BodyA.MaterialMap.2048')),
    ],
'1e794b69': [
        (log,                           ('1.0 -> 2.5: Grace BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9abd7824', 'Grace.BodyA.NormalMap.1024')),
    ],
'9abd7824': [
        (log,                           ('1.0: Grace BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1e794b69', 'Grace.BodyA.NormalMap.2048')),
    ],
'210b3ebf': [(log, ('1.3 -> 1.4: Grace BodyB Diffuse 2048p Hash',)), (update_hash, ('9c7057e8',))],
'9c7057e8': [
        (log,                           ('2.5: Grace BodyB Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ac361185', '21794bd6'), 'Grace.BodyB.Diffuse.1024')),
    ],
'21794bd6': [(log, ('1.3 -> 1.4: Grace BodyB Diffuse 1024p Hash',)), (update_hash, ('ac361185',))],
'ac361185': [
        (log,                           ('1.4: Grace BodyB Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('9c7057e8', '210b3ebf'), 'Grace.BodyB.Diffuse.2048')),
    ],
'08082f5f': [
        (log,                           ('2.5: Grace BodyB LightMap 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a60162a0', 'Grace.BodyB.LightMap.1024')),
    ],
'a60162a0': [
        (log,                           ('1.0: Grace BodyB LightMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('08082f5f', 'Grace.BodyB.LightMap.2048')),
    ],
'f176398a': [
        (log,                           ('2.5: Grace BodyB MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b5b88a3f', 'Grace.BodyB.MaterialMap.1024')),
    ],
'b5b88a3f': [
        (log,                           ('1.0: Grace BodyB MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f176398a', 'Grace.BodyB.MaterialMap.2048')),
    ],
'06cb1413': [
        (log,                           ('1.0 -> 2.5: Grace BodyB NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c5f703be', 'Grace.BodyB.NormalMap.1024')),
    ],
'c5f703be': [
        (log,                           ('1.0: Grace BodyB NormalMap 1024p Hash',)),
        (add_section_if_missing,        (('8b240678', '0f82a13e'), 'Grace.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('06cb1413', 'Grace.BodyB.NormalMap.2048')),
    ],
'1126fd58': [
        (log, ('3.0: Grace Hair VB Hash',)),
        (add_section_if_missing, ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
    ],
'1bed412f': [
        (log, ('3.0: Grace Hair VB Hash',)),
        (add_section_if_missing, ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
    ],
'9affd94c': [(log, ('3.0: Grace Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'c80c3d7a': [
        (log, ('3.0: Grace Hair Shadow VB Hash',)),
        (add_section_if_missing, ('9affd94c', 'Grace.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'6f2f2441': [
        (log, ('3.0: Grace Hair Shadow VB Hash',)),
        (add_section_if_missing, ('9affd94c', 'Grace.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'b9d0b1da': [
        (log, ('3.0: Grace Hair Shadow VB Hash',)),
        (add_section_if_missing, ('9affd94c', 'Grace.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'e96835d7': [
        (log, ('3.0: Grace Hair Shadow VB Hash',)),
        (add_section_if_missing, ('9affd94c', 'Grace.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f1cba806': [
        (log, ('3.0: Grace Body VB Hash',)),
        (add_section_if_missing, ('8b240678', 'Grace.Body.IB', 'match_priority = 0\n')),
    ],
'8855c5cf': [
        (log, ('3.0: Grace Body VB Hash',)),
        (add_section_if_missing, ('8b240678', 'Grace.Body.IB', 'match_priority = 0\n')),
    ],
'4bb45448': [
        (log, ('3.0: Grace Body VB Hash',)),
        (add_section_if_missing, ('8b240678', 'Grace.Body.IB', 'match_priority = 0\n')),
    ],
'3b80154c': [
        (log, ('3.0: Grace Body VB Hash',)),
        (add_section_if_missing, ('8b240678', 'Grace.Body.IB', 'match_priority = 0\n')),
    ],
'708448b3': [
        (log, ('3.0: Grace Face VB Hash',)),
        (add_section_if_missing, ('4d60568b', 'Grace.Face.IB', 'match_priority = 0\n')),
    ],
'c3b7516b': [
        (log, ('3.0: Grace Face VB Hash',)),
        (add_section_if_missing, ('4d60568b', 'Grace.Face.IB', 'match_priority = 0\n')),
    ],
'ebe2953b': [
        (log, ('3.0: Grace Face VB Hash',)),
        (add_section_if_missing, ('4d60568b', 'Grace.Face.IB', 'match_priority = 0\n')),
    ],
'd1a8c9de': [(log, ('3.0: Grace weapon IB Hash',)), (add_ib_check_if_missing,)],
'6ca434f3': [
        (log, ('3.0: Grace weapon VB Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'f238f1b9': [
        (log, ('3.0: Grace weapon VB Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'50c54607': [
        (log, ('3.0: Grace weapon VB Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'ba3ec8ff': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'a408585a': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'bc502577': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'3ad4e1bc': [(log, ('3.0: Grace misc hash',)),],
'4a96dbf4': [(log, ('3.0: Grace misc hash',)),],
'9e96a54f': [
        (log, ('3.0: Grace Hair VB Hash',)),
        (add_section_if_missing, ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Grace Hair TEX Hash',)),
        (add_section_if_missing, ('89299f56', 'Grace.Hair.IB', 'match_priority = 0\n')),
    ],
'a3d371fd': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'20d98756': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
'd788dcd7': [
        (log, ('3.0: Grace weapon TEX Hash',)),
        (add_section_if_missing, ('d1a8c9de', 'Grace.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Grace',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
