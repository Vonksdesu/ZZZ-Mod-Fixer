"""
Piper Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Piper's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '940454ef': [
            (log,                             ('2.2 - 3.2: Piper Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'da8a2564': [
            (log,                             ('2.2 - 3.2: Piper Hair Draw VB Hash',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        ],
        'c4619559': [
            (log,                             ('2.2 - 3.2: Piper Hair Position VB Hash',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        ],
        'fd1b9c29': [
            (log,                             ('1.1 -> 1.2: Piper Hair Texcoord Hash',)),
            (update_hash,                     ('8b6b17f8',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_12_shrink_texcoord_color,    ('1.2',)),
        ],
        '8b6b17f8': [
            (log,                             ('1.3 -> 1.4: Piper Hair Texcoord Hash',)),
            (update_hash,                     ('1c6d41af',)),
        ],
        '1c6d41af': [
            (log,                             ('2.2 - 3.2: Piper Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        ],
        '64697011': [
            (log,                             ('2.2 - 3.2: Piper Hair Blend VB Hash',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        ],
        '69ed4d11': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9b743eab', 'Piper.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9b743eab', 'Piper.Glasses accessoriesA.Diffuse.1024')),
        ],
        '9b743eab': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('69ed4d11', 'Piper.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('69ed4d11', 'Piper.Glasses accessoriesA.Diffuse.2048')),
        ],
        '7ca957d8': [
            (log,                             ('1.0 -> 2.5: Piper HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'db7dccbf': [
            (log,                             ('1.0 -> 2.5: Piper HairA NormalMap 1024p Hash',)),
            (update_hash,                     ('8db36370',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Piper HairA, Glasses accessoriesA, BodyA, weapon - 斧头 and weapon - 转轮 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', '8db36370', 'db7dccbf', '73a61e88'), 'Piper.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '8db36370', 'db7dccbf', '73a61e88'), 'Piper.Glasses accessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '8db36370', 'db7dccbf', '73a61e88'), 'Piper.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '8db36370', 'db7dccbf', '73a61e88'), 'Piper.weapon - 斧头.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '8db36370', 'db7dccbf', '73a61e88'), 'Piper.weapon - 转轮.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Piper HairA, Glasses accessoriesA, BodyA, weapon - 斧头 and weapon - 转轮 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '7ca957d8', '51f1ec36'), 'Piper.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '7ca957d8', '51f1ec36'), 'Piper.Glasses accessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '7ca957d8', '51f1ec36'), 'Piper.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '7ca957d8', '51f1ec36'), 'Piper.weapon - 斧头.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '7ca957d8', '51f1ec36'), 'Piper.weapon - 转轮.NormalMap.2048')),
        ],
        '8db36370': [
            (log,                             ('2.5: Piper HairA and BodyA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        '79953d32': [
            (log,                             ('1.0 -> 2.5: Piper HairA LightMap 2048p Hash',)),
            (update_hash,                     ('1146c5c3',)),
        ],
        '92acb4d4': [
            (log,                             ('1.0 -> 2.5: Piper HairA LightMap 1024p Hash',)),
            (update_hash,                     ('46cbca7a',)),
        ],
        '1146c5c3': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('6bd15459', '46cbca7a', '92acb4d4'), 'Piper.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('6bd15459', '46cbca7a', '92acb4d4'), 'Piper.Glasses accessoriesA.LightMap.1024')),
        ],
        '6bd15459': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('1146c5c3', '79953d32'), 'Piper.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('1146c5c3', '79953d32'), 'Piper.Glasses accessoriesA.LightMap.2048')),
        ],
        '46cbca7a': [
            (log,                             ('2.5: Piper HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
        ],
        'b3034dff': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('78c42c66', 'Piper.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('78c42c66', 'Piper.Glasses accessoriesA.MaterialMap.1024')),
        ],
        '78c42c66': [
            (log,                             ('2.2 - 3.2: Piper HairA and Glasses accessoriesA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('940454ef', 'Piper.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b3034dff', 'Piper.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b3034dff', 'Piper.Glasses accessoriesA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '83736476': [
            (log,                             ('2.2 - 3.2: Piper Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8babfd25': [
            (log,                             ('2.2 - 3.2: Piper Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('83736476', 'Piper.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd45a3d8d': [
            (log,                             ('2.2 - 3.2: Piper Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('83736476', 'Piper.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '71574c65': [
            (log,                             ('2.2 - 3.2: Piper Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('83736476', 'Piper.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '7f2390d9': [
            (log,                             ('2.2 - 3.2: Piper Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('83736476', 'Piper.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no textures in any database version.

        # ==================== Glasses accessories Component ====================
        '90bc5b0f': [
            (log,                             ('2.2 - 3.2: Piper Glasses accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8db48e03': [
            (log,                             ('2.2 - 3.2: Piper Glasses accessories Draw VB Hash',)),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
        ],
        '17682368': [
            (log,                             ('2.2 - 3.2: Piper Glasses accessories Position VB Hash',)),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
        ],
        'e527157e': [
            (log,                             ('2.2 - 3.2: Piper Glasses accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
        ],
        '16060a52': [
            (log,                             ('2.2 - 3.2: Piper Glasses accessories Blend VB Hash',)),
            (add_section_if_missing,          ('90bc5b0f', 'Piper.Glasses accessories.IB', 'match_priority = 0\n')),
        ],
        # Glasses accessories shares its textures with Hair; see that Component above.

        # ==================== Body Component ====================
        '585da98b': [
            (log,                             ('2.2 - 3.2: Piper Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd28231af': [
            (log,                             ('2.2 - 3.2: Piper Body Draw VB Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        'b2f3e6aa': [
            (log,                             ('1.1 -> 1.2: Piper Body Position Hash',)),
            (update_hash,                     ('ffe8fea7',)),
        ],
        'ffe8fea7': [
            (log,                             ('2.2 - 3.2: Piper Body Position VB Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        'a0d146b3': [
            (log,                             ('1.1 -> 1.2: Piper Body Texcoord Hash',)),
            (update_hash,                     ('a011f94e',)),
        ],
        'a011f94e': [
            (log,                             ('1.2 -> 1.3: Piper Body Texcoord Hash',)),
            (update_hash,                     ('6357b120',)),
        ],
        '6357b120': [
            (log,                             ('2.2 - 3.2: Piper Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        '764276de': [
            (log,                             ('1.2 -> 1.3: Piper Body Blend Hash',)),
            (update_hash,                     ('3d329807',)),
        ],
        '3d329807': [
            (log,                             ('2.2 - 3.2: Piper Body Blend VB Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        'b4b74e7e': [
            (log,                             ('1.2 -> 1.3: Piper BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('fed40302',)),
        ],
        'fed40302': [
            (log,                             ('2.2 - 3.2: Piper BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b450949d', '621564e5'), 'Piper.BodyA.Diffuse.1024')),
        ],
        '621564e5': [
            (log,                             ('1.2 -> 1.3: Piper BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('b450949d',)),
        ],
        'b450949d': [
            (log,                             ('2.2 - 3.2: Piper BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fed40302', 'b4b74e7e'), 'Piper.BodyA.Diffuse.2048')),
        ],
        '51f1ec36': [
            (log,                             ('1.0 -> 2.5: Piper BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '73a61e88': [
            (log,                             ('1.0 -> 2.5: Piper BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('8db36370',)),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        '9cc2aaa0': [
            (log,                             ('1.0 -> 2.5: Piper BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('a32c39b9',)),
        ],
        'db9c7abf': [
            (log,                             ('1.0 -> 2.5: Piper BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('a0dcd60a',)),
        ],
        'a32c39b9': [
            (log,                             ('2.2 - 3.2: Piper BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7a281673', 'a0dcd60a', 'db9c7abf'), 'Piper.BodyA.LightMap.1024')),
        ],
        '7a281673': [
            (log,                             ('2.2 - 3.2: Piper BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a32c39b9', '9cc2aaa0'), 'Piper.BodyA.LightMap.2048')),
        ],
        'a0dcd60a': [
            (log,                             ('2.5: Piper BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
        ],
        '7fdee30d': [
            (log,                             ('2.2 - 3.2: Piper BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('73e72a1e', 'Piper.BodyA.MaterialMap.1024')),
        ],
        '73e72a1e': [
            (log,                             ('2.2 - 3.2: Piper BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('585da98b', 'Piper.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7fdee30d', 'Piper.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'e11baad9': [
            (log,                             ('2.2 - 3.2: Piper Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '67362536': [
            (log,                             ('2.2 - 3.2: Piper Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
        ],
        '5d24b671': [
            (log,                             ('2.2 - 3.2: Piper Face Position VB Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
        ],
        '58468aba': [
            (log,                             ('2.2 - 3.1: Piper Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2fe49591',)),
        ],
        '2fe49591': [
            (log,                             ('3.2: Piper Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '6059174c': [
            (log,                             ('2.2 - 3.2: Piper Face Blend VB Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
        ],
        '97a7862e': [
            (log,                             ('1.1 -> 1.2: Piper Face Diffuse 2048p Hash',)),
            (update_hash,                     ('3b2eb1d9',)),
        ],
        '3b2eb1d9': [
            (log,                             ('2.2 - 3.2: Piper FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f1c8f946', '48c96e2e', '4b06ffe6'), 'Piper.FaceA.Diffuse.1024')),
        ],
        '4b06ffe6': [
            (log,                             ('1.1 -> 1.2: Piper Face Diffuse 1024p Hash',)),
            (update_hash,                     ('f1c8f946',)),
        ],
        'f1c8f946': [
            (log,                             ('2.2 - 3.2: Piper FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('3b2eb1d9', '97a7862e'), 'Piper.FaceA.Diffuse.2048')),
        ],
        '48c96e2e': [
            (log,                             ('2.5: Piper FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e11baad9', 'Piper.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 斧头 Component ====================
        'b79e0a74': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9c1cfb7d': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
        ],
        '6753bce4': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 Position VB Hash',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
        ],
        '1f0dbd2b': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
        ],
        '731ab501': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 Blend VB Hash',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
        ],
        '9880cefa': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7c5e2403', 'Piper.weapon - 斧头.Diffuse.1024')),
            (multiply_section_if_missing,     ('7c5e2403', 'Piper.weapon - 转轮.Diffuse.1024')),
        ],
        '7c5e2403': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9880cefa', 'Piper.weapon - 斧头.Diffuse.2048')),
            (multiply_section_if_missing,     ('9880cefa', 'Piper.weapon - 转轮.Diffuse.2048')),
        ],
        # The weapon components share their NormalMap hashes with Hair; see that Component above.
        '4345e1e7': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa118562', 'Piper.weapon - 斧头.LightMap.1024')),
            (multiply_section_if_missing,     ('aa118562', 'Piper.weapon - 转轮.LightMap.1024')),
        ],
        'aa118562': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4345e1e7', 'Piper.weapon - 斧头.LightMap.2048')),
            (multiply_section_if_missing,     ('4345e1e7', 'Piper.weapon - 转轮.LightMap.2048')),
        ],
        'd06e2ef0': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2e830888', 'Piper.weapon - 斧头.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2e830888', 'Piper.weapon - 转轮.MaterialMap.1024')),
        ],
        '2e830888': [
            (log,                             ('2.2 - 3.2: Piper weapon - 斧头 and weapon - 转轮 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b79e0a74', 'Piper.weapon - 斧头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d06e2ef0', 'Piper.weapon - 斧头.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d06e2ef0', 'Piper.weapon - 转轮.MaterialMap.2048')),
        ],

        # ==================== weapon - 转轮 Component ====================
        'e85eae59': [
            (log,                             ('2.2 - 3.2: Piper weapon - 转轮 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '30ea10c9': [
            (log,                             ('2.2 - 3.2: Piper weapon - 转轮 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
        ],
        'd221c027': [
            (log,                             ('2.2 - 3.2: Piper weapon - 转轮 Position VB Hash',)),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
        ],
        'b7790fd4': [
            (log,                             ('2.2 - 3.2: Piper weapon - 转轮 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
        ],
        'ceec1b8e': [
            (log,                             ('2.2 - 3.2: Piper weapon - 转轮 Blend VB Hash',)),
            (add_section_if_missing,          ('e85eae59', 'Piper.weapon - 转轮.IB', 'match_priority = 0\n')),
        ],
        # weapon - 转轮 shares its textures with weapon - 斧头; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Piper',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
