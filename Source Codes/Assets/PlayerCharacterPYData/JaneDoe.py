"""
JaneDoe Character Hash Commands
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
    Returns JaneDoe's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '3275b812': [
            (log,                             ('2.5 - 3.2: JaneDoe Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9268a5af': [
            (log,                             ('1.4 -> 2.5: Jane Hair IB Hash',)),
            (update_hash,                     ('3275b812',)),
        ],
        '7b16a708': [
            (log,                             ('1.3 -> 1.4: Jane Hair IB Hash',)),
            (update_hash,                     ('9268a5af',)),
        ],
        '74bc0b7f': [
            (log,                             ('2.5 - 3.2: JaneDoe Hair Draw VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
        ],
        '2d06e785': [
            (log,                             ('1.4 -> 2.5: Jane Hair Draw Hash',)),
            (update_hash,                     ('74bc0b7f',)),
        ],
        '5721e4e7': [
            (log,                             ('1.3 -> 1.4: Jane Hair Draw Hash',)),
            (update_hash,                     ('2d06e785',)),
        ],
        '33a09cfe': [
            (log,                             ('2.5 - 3.2: JaneDoe Hair Position VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
        ],
        'e7a3b7dc': [
            (log,                             ('1.4 -> 2.5: Jane Hair Position Hash',)),
            (update_hash,                     ('33a09cfe',)),
        ],
        '24323bf9': [
            (log,                             ('1.3 -> 1.4: Jane Hair Position Hash',)),
            (update_hash,                     ('e7a3b7dc',)),
        ],
        'fa617c9a': [
            (log,                             ('2.5 - 3.2: JaneDoe Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
        ],
        'acec29f8': [
            (log,                             ('1.4 -> 2.5: Jane Hair Texcoord Hash',)),
            (update_hash,                     ('fa617c9a',)),
        ],
        '257a90d6': [
            (log,                             ('1.3 -> 1.4: Jane Hair Texcoord Hash',)),
            (update_hash,                     ('acec29f8',)),
        ],
        'c8ad344e': [
            (log,                             ('1.1 -> 1.2: Jane Hair Texcoord Hash',)),
            (update_hash,                     ('257a90d6',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_12_shrink_texcoord_color,    ('1.2',)),
        ],
        'e42171df': [
            (log,                             ('2.5 - 3.2: JaneDoe Hair Blend VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
        ],
        '8721477f': [
            (log,                             ('1.4 -> 2.5: Jane Hair Blend Hash',)),
            (update_hash,                     ('e42171df',)),
        ],
        '0a10c747': [
            (log,                             ('1.3 -> 1.4: Jane Hair Blend Hash',)),
            (update_hash,                     ('8721477f',)),
        ],
        'f7ef1a53': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b33a9770', 'JaneDoe.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b33a9770', 'JaneDoe.Hands&AccessoriesA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b33a9770', 'JaneDoe.weapon - 脚刀.Diffuse.1024')),
        ],
        'b33a9770': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f7ef1a53', 'JaneDoe.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f7ef1a53', 'JaneDoe.Hands&AccessoriesA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f7ef1a53', 'JaneDoe.weapon - 脚刀.Diffuse.2048')),
        ],
        '9ec4cd4f': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e12acc1', 'JaneDoe.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('5e12acc1', 'JaneDoe.Hands&AccessoriesA.LightMap.1024')),
            (multiply_section_if_missing,     ('5e12acc1', 'JaneDoe.weapon - 脚刀.LightMap.1024')),
        ],
        '5e12acc1': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ec4cd4f', 'JaneDoe.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('9ec4cd4f', 'JaneDoe.Hands&AccessoriesA.LightMap.2048')),
            (multiply_section_if_missing,     ('9ec4cd4f', 'JaneDoe.weapon - 脚刀.LightMap.2048')),
        ],
        '5e34e275': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('40fca454', 'JaneDoe.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('40fca454', 'JaneDoe.Hands&AccessoriesA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('40fca454', 'JaneDoe.weapon - 脚刀.MaterialMap.1024')),
        ],
        '40fca454': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, Hands&AccessoriesA and weapon - 脚刀 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e34e275', 'JaneDoe.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('5e34e275', 'JaneDoe.Hands&AccessoriesA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('5e34e275', 'JaneDoe.weapon - 脚刀.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, BodyA, Hands&AccessoriesA, weapon - 手刀 and weapon - 脚刀 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoe.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoe.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoe.Hands&AccessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoe.weapon - 手刀.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoe.weapon - 脚刀.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: JaneDoe HairA, BodyA, Hands&AccessoriesA, weapon - 手刀 and weapon - 脚刀 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9268a5af', 'JaneDoe.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoe.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoe.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoe.Hands&AccessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoe.weapon - 手刀.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoe.weapon - 脚刀.NormalMap.2048')),
        ],

        # ==================== HeHair Shadowad Component ====================
        '27805144': [
            (log,                             ('2.5 - 3.2: JaneDoe HeHair Shadowad IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7c6eb690': [
            (log,                             ('2.4 -> 2.5: Jane Hair Shadow IB Hash (inferred)',)),
            (update_hash,                     ('27805144',)),
        ],
        '759a4b9f': [
            (log,                             ('2.2 - 2.4: JaneDoe HeHair Shadowad Draw VB Hash',)),
            (add_section_if_missing,          ('7c6eb690', 'JaneDoe.HeHair Shadowad.IB', 'match_priority = 0\n')),
        ],
        '5f8ea758': [
            (log,                             ('2.4 -> 2.5: Jane Hair Shadow Position Hash (inferred)',)),
            (update_hash,                     ('7c08cd53',)),
        ],
        '3ac849d5': [
            (log,                             ('2.4 -> 2.5: Jane Hair Shadow Texcoord Hash (inferred)',)),
            (update_hash,                     ('93c5b49a',)),
        ],
        'c5a06055': [
            (log,                             ('2.4 -> 2.5: Jane Hair Shadow Blend Hash (inferred)',)),
            (update_hash,                     ('6af472f5',)),
        ],

        # ==================== Body Component ====================
        'ba4255a5': [
            (log,                             ('2.2 - 3.2: JaneDoe Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e2c0144e': [
            (log,                             ('1.3 -> 1.4: Jane Body IB Hash',)),
            (update_hash,                     ('ba4255a5',)),
        ],
        '0e1c6740': [
            (log,                             ('2.2 - 3.2: JaneDoe Body Draw VB Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
        ],
        'd1aa4b85': [
            (log,                             ('1.3 -> 1.4: Jane Body Draw Hash',)),
            (update_hash,                     ('0e1c6740',)),
        ],
        '10050266': [
            (log,                             ('2.2 - 3.2: JaneDoe Body Position VB Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
        ],
        '06f9bc49': [
            (log,                             ('1.3 -> 1.4: Jane Body Position Hash',)),
            (update_hash,                     ('10050266',)),
        ],
        '949549de': [
            (log,                             ('2.2 - 3.2: JaneDoe Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
        ],
        '8b85c03e': [
            (log,                             ('1.3 -> 1.4: Jane Body Texcoord Hash',)),
            (update_hash,                     ('949549de',)),
        ],
        'e27f398e': [
            (log,                             ('2.2 - 3.2: JaneDoe Body Blend VB Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
        ],
        '9727a184': [
            (log,                             ('1.3 -> 1.4: Jane Body Blend Hash',)),
            (update_hash,                     ('e27f398e',)),
        ],
        'd1f56c7d': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e62ae3b5', 'JaneDoe.BodyA.Diffuse.1024')),
        ],
        'e62ae3b5': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1f56c7d', 'JaneDoe.BodyA.Diffuse.2048')),
        ],
        '3087f82a': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('52fa9861', 'JaneDoe.BodyA.LightMap.1024')),
        ],
        '52fa9861': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3087f82a', 'JaneDoe.BodyA.LightMap.2048')),
        ],
        '99eae42e': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5dce2408', 'JaneDoe.BodyA.MaterialMap.1024')),
        ],
        '5dce2408': [
            (log,                             ('2.2 - 3.2: JaneDoe BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ba4255a5', 'JaneDoe.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('99eae42e', 'JaneDoe.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Hands&Accessories Component ====================
        '294a319a': [
            (log,                             ('2.5 - 3.2: JaneDoe Hands&Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2b5dc947': [
            (log,                             ('2.5 - 3.2: JaneDoe Hands&Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
        ],
        '82e7c056': [
            (log,                             ('2.5 - 3.2: JaneDoe Hands&Accessories Position VB Hash',)),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
        ],
        '6d482e21': [
            (log,                             ('2.5 - 3.2: JaneDoe Hands&Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
        ],
        'd06a9206': [
            (log,                             ('2.5 - 3.2: JaneDoe Hands&Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('294a319a', 'JaneDoe.Hands&Accessories.IB', 'match_priority = 0\n')),
        ],
        # Hands&Accessories shares all its textures with Hair in both resolutions; see that Component above.

        # ==================== Face Component ====================
        'ef86fc9f': [
            (log,                             ('2.2 - 3.2: JaneDoe Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5661afc3': [
            (log,                             ('2.2 - 3.2: JaneDoe Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
        ],
        '6c733c84': [
            (log,                             ('2.2 - 3.2: JaneDoe Face Position VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
        ],
        '9f2f7c53': [
            (log,                             ('2.4 -> 2.5: Jane Head Texcoord Hash',)),
            (update_hash,                     ('1fa404c1',)),
        ],
        '1fa404c1': [
            (log,                             ('2.5 - 3.0: JaneDoe Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('3c32a411',)),
        ],
        '3c32a411': [
            (log,                             ('3.1: JaneDoe Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
        ],
        '91846a84': [
            (log,                             ('2.2 - 3.2: JaneDoe Face Blend VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
        ],
        '3b75aa2c': [
            (log,                             ('2.2 - 3.2: JaneDoe FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d823ac80', 'JaneDoe.FaceA.Diffuse.1024')),
        ],
        '8974fb74': [
            (log,                             ('1.3 -> 1.4: Jane HeadA Diffuse 2048p Hash',)),
            (update_hash,                     ('3b75aa2c',)),
        ],
        'd823ac80': [
            (log,                             ('2.2 - 3.2: JaneDoe FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoe.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3b75aa2c', 'JaneDoe.FaceA.Diffuse.2048')),
        ],
        '689639a5': [
            (log,                             ('1.3 -> 1.4: Jane HeadA Diffuse 1024p Hash',)),
            (update_hash,                     ('d823ac80',)),
        ],

        # ==================== Weapon - 手刀 Component ====================
        '602c545a': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'be378e74': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
        ],
        'eace2dfa': [
            (log,                             ('2.2 - 2.4: JaneDoe weapon - 手刀 Position VB Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
        ],
        '850d4cbf': [
            (log,                             ('2.1 -> 2.2: Jane Hand Blade Position Hash',)),
            (update_hash,                     ('eace2dfa',)),
        ],
        '535e2453': [
            (log,                             ('2.2 - 2.4: JaneDoe weapon - 手刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
        ],
        '7fd655de': [
            (log,                             ('2.1 -> 2.2: Jane Hand Blade Texcoord Hash',)),
            (update_hash,                     ('535e2453',)),
        ],
        '7310ad6a': [
            (log,                             ('2.2 - 2.4: JaneDoe weapon - 手刀 Blend VB Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
        ],
        'a14461d9': [
            (log,                             ('2.1 -> 2.2: Jane Hand Blade Blend Hash',)),
            (update_hash,                     ('7310ad6a',)),
        ],
        '59c18114': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0158a68f', 'JaneDoe.weapon - 手刀.Diffuse.1024')),
        ],
        '0158a68f': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('59c18114', 'JaneDoe.weapon - 手刀.Diffuse.2048')),
        ],
        '76cda993': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 LightMap 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('655a0c17', 'JaneDoe.weapon - 手刀.LightMap.1024')),
        ],
        '655a0c17': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 LightMap 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76cda993', 'JaneDoe.weapon - 手刀.LightMap.2048')),
        ],
        'd83ad325': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9f30a0e', 'JaneDoe.weapon - 手刀.MaterialMap.1024')),
        ],
        'f9f30a0e': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 手刀 MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoe.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d83ad325', 'JaneDoe.weapon - 手刀.MaterialMap.2048')),
        ],
        # weapon - 手刀 shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Weapon - 脚刀 Component ====================
        'f7a304e8': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 脚刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '29a81e40': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 脚刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
        ],
        '566bb5f4': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 脚刀 Position VB Hash',)),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
        ],
        'aa4168d9': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 脚刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
        ],
        'f038d9a5': [
            (log,                             ('2.2 - 3.2: JaneDoe weapon - 脚刀 Blend VB Hash',)),
            (add_section_if_missing,          ('f7a304e8', 'JaneDoe.weapon - 脚刀.IB', 'match_priority = 0\n')),
        ],
        # weapon - 脚刀 shares all its textures with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoe',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
