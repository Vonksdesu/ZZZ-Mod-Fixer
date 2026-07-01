"""
JaneDoe Character Hash Commands
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
    Returns JaneDoe's hash commands dictionary.
    """
    return {
# === IB Hashes ===
'3275b812': [(log, ('3.0: Jane Hair IB Hash',)),                        (add_ib_check_if_missing,)],
'ba4255a5': [(log, ('3.0: Jane Body IB Hash',)),                        (add_ib_check_if_missing,)],
'ef86fc9f': [(log, ('3.0: Jane Head/Face IB Hash',)),                   (add_ib_check_if_missing,)],
'27805144': [(log, ('3.0: Jane Hair Shadow IB Hash',)),                 (add_ib_check_if_missing,)],
'602c545a': [(log, ('3.0: Jane Weapon Hand Blade IB Hash',)),           (add_ib_check_if_missing,)],
'f7a304e8': [(log, ('3.0: Jane Weapon Leg Blade IB Hash',)),            (add_ib_check_if_missing,)],
'294a319a': [(log, ('3.0: Jane Hands & Accessories IB Hash',)),         (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'74bc0b7f': [(log, ('3.0: Jane Hair Draw Hash',)),                      (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'33a09cfe': [(log, ('3.0: Jane Hair Position Hash',)),                  (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'fa617c9a': [(log, ('3.0: Jane Hair Texcoord Hash',)),                  (add_section_if_missing, ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n'))],
'e42171df': [
        (log,                           ('3.0: Jane Hair Blend Hash',)),
        (add_section_if_missing,        ('3275b812', 'Jane.Hair.IB', 'match_priority = 0\n')),
        (log,                           ('+ Remapping hair blend indices (Jane 2.5+ bone fix)',)),
        (update_buffer_blend_indices,   (
            'e42171df',
            (26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126),
            (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 19, 20, 18, 22, 23, 24, 25, 26, 27, 28, 21, 29, 30, 31, 33, 34, 32, 36, 37, 35, 38, 39, 40, 41, 42, 44, 45, 46, 48, 47, 43, 49, 52, 53, 54, 55, 50, 51, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68),
        )),
    ],

# Body
'0e1c6740': [(log, ('3.0: Jane Body Draw Hash',)),                      (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'10050266': [(log, ('3.0: Jane Body Position Hash',)),                  (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'949549de': [(log, ('3.0: Jane Body Texcoord Hash',)),                  (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],
'e27f398e': [(log, ('3.0: Jane Body Blend Hash',)),                     (add_section_if_missing, ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n'))],

# Face
'5661afc3': [(log, ('3.0: Jane Face VertexLimit Hash',)),               (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'6c733c84': [(log, ('3.0: Jane Face position_vb Hash',)),               (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'1fa404c1': [(log, ('3.0: Jane Face texcoord_vb Hash',)),               (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],
'91846a84': [(log, ('3.0: Jane Face blend_vb Hash',)),                  (add_section_if_missing, ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n'))],

# Weapon - Hand Blade
'be378e74': [(log, ('3.0: Jane Hand Blade draw_vb Hash',)),             (add_section_if_missing, ('602c545a', 'Jane.HandBlade.IB', 'match_priority = 0\n'))],

# Weapon - Leg Blade
'29a81e40': [(log, ('3.0: Jane Leg Blade draw_vb Hash',)),              (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'566bb5f4': [(log, ('3.0: Jane Leg Blade position_vb Hash',)),          (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'aa4168d9': [(log, ('3.0: Jane Leg Blade texcoord_vb Hash',)),          (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],
'f038d9a5': [(log, ('3.0: Jane Leg Blade blend_vb Hash',)),             (add_section_if_missing, ('f7a304e8', 'Jane.LegBlade.IB', 'match_priority = 0\n'))],

# Hands & Accessories
'2b5dc947': [(log, ('3.0: Jane Hands & Accessories draw_vb Hash',)),    (add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'82e7c056': [(log, ('3.0: Jane Hands & Accessories position_vb Hash',)),(add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'6d482e21': [(log, ('3.0: Jane Hands & Accessories texcoord_vb Hash',)),(add_section_if_missing, ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n'))],
'd06a9206': [
        (log,                           ('3.0: Jane Hands & Accessories blend_vb Hash',)),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (log,                           ('+ Remapping hand blend indices (Jane 2.5+ bone fix)',)),
        (update_buffer_blend_indices,   (
            'd06a9206',
            (4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 127, 128, 129),
            (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60),
        )),
    ],

# === Legacy Hash Updates ===
'c8ad344e': [
        (log, ('1.1 -> 1.2: Jane Hair Texcoord Hash',)),
        (update_hash, ('257a90d6',)),
        (log, ('+ Remapping hair texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '11_Jane_Hair',
            ('4f','2e','2e'),
            ('4B','2f','2f')
        )),
    ],
'5721e4e7': [(log, ('1.3 -> 1.4: Jane Hair Draw Hash',)),               (update_hash, ('2d06e785',))],
'24323bf9': [(log, ('1.3 -> 1.4: Jane Hair Position Hash',)),           (update_hash, ('e7a3b7dc',))],
'0a10c747': [(log, ('1.3 -> 1.4: Jane Hair Blend Hash',)),              (update_hash, ('8721477f',))],
'257a90d6': [(log, ('1.3 -> 1.4: Jane Hair Texcoord Hash',)),           (update_hash, ('acec29f8',))],
'40fca454': [(log, ('1.3 -> 1.4: Jane Hair MaterialMap Hash',)),        (update_hash, ('5e34e275',))],
'd1f56c7d': [(log, ('1.3 -> 1.4: Jane Body Diffuse Hash',)),            (update_hash, ('e62ae3b5',))],
'3087f82a': [(log, ('1.3 -> 1.4: Jane Body LightMap Hash',)),           (update_hash, ('52fa9861',))],
'99eae42e': [(log, ('1.3 -> 1.4: Jane Body MaterialMap Hash',)),        (update_hash, ('5dce2408',))],

# === Legacy Hash Updates (continued) ===
'689639a5': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 1024p Hash',)), (update_hash, ('d823ac80',))],
'8974fb74': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 2048p Hash',)), (update_hash, ('3b75aa2c',))],
'9727a184': [(log, ('1.3 -> 1.4: Jane Body Blend Hash',)),    (update_hash, ('e27f398e',))],
'9f2f7c53': [(log, ('2.4 -> 2.5: Jane Head Texcoord Hash',)), (update_hash, ('1fa404c1',))],

# === Legacy Transition Paths ===
'06f9bc49': [(log, ('1.1 -> 3.0: Jane Body Position Hash [Legacy]',)),   (update_hash, ('10050266',))],
'd1aa4b85': [(log, ('1.1 -> 3.0: Jane Body VertexLimitRaise [Legacy]',)), (update_hash, ('0e1c6740',))],
'8b85c03e': [
        (log,                           ('1.1 -> 3.0: Jane Body Texcoord Hash [Legacy]',)),
        (update_hash,                   ('949549de',)),
        (log,                           ('+ Remapping body texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '11_Jane_Body',
            ('2e','2e','2e'),
            ('2f','2f','2f')
        )),
    ],
'7b16a708': [(log, ('1.3 -> 1.4: Jane Hair IB Hash [Legacy]',)),        (update_hash, ('9268a5af',))],
'9268a5af': [(log, ('1.4 -> 2.5: Jane Hair IB Hash [Legacy]',)),        (update_hash, ('3275b812',))],
'8721477f': [(log, ('1.4 -> 2.5: Jane Hair Blend Hash [Legacy]',)),     (update_hash, ('e42171df',))],
'e7a3b7dc': [(log, ('1.4 -> 2.5: Jane Hair Position Hash [Legacy]',)),  (update_hash, ('33a09cfe',))],
'acec29f8': [(log, ('1.4 -> 2.5: Jane Hair Texcoord Hash [Legacy]',)),  (update_hash, ('fa617c9a',))],
'2d06e785': [(log, ('1.4 -> 2.5: Jane Hair Draw Hash [Legacy]',)),      (update_hash, ('74bc0b7f',))],
'e2c0144e': [(log, ('1.3 -> 1.4: Jane Body IB Hash [Legacy]',)),        (update_hash, ('ba4255a5',))],

# === Face Textures ===
'3b75aa2c': [
        (log,                           ('3.0: Jane HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
    ],
'd823ac80': [
        (log,                           ('3.0: Jane HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ef86fc9f', 'Jane.Head.IB', 'match_priority = 0\n')),
    ],

# === Hair, Hands, Foot Knife Textures ===
'f7ef1a53': [
        (log,                           ('2.5 -> 3.0: Jane Hair Diffuse Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'b33a9770': [
        (log,                           ('3.0: Jane Hair Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'9ec4cd4f': [
        (log,                           ('3.0: Jane Hair LightMap Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'5e12acc1': [
        (log,                           ('3.0: Jane Hair LightMap Hash [Legacy]',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'5e34e275': [
        (log,                           ('3.0: Jane Hair MaterialMap Hash',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'40fca454': [
        (log,                           ('3.0: Jane Hair MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        (('3275b812', '9268a5af', '7b16a708'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e34e275', 'Jane.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'd1f56c7d': [
        (log,                           ('2.5: Jane BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e62ae3b5', 'Jane.BodyA.Diffuse.1024')),
    ],
'e62ae3b5': [
        (log,                           ('2.5: Jane BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d1f56c7d', 'Jane.BodyA.Diffuse.2048')),
    ],
'3087f82a': [
        (log,                           ('2.5: Jane BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('52fa9861', 'Jane.BodyA.LightMap.1024')),
    ],
'52fa9861': [
        (log,                           ('2.5: Jane BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3087f82a', 'Jane.BodyA.LightMap.2048')),
    ],
'99eae42e': [
        (log,                           ('2.5: Jane BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5dce2408', 'Jane.BodyA.MaterialMap.1024')),
    ],
'5dce2408': [
        (log,                           ('2.5: Jane BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('ba4255a5', 'e2c0144e'), 'Jane.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99eae42e', 'Jane.BodyA.MaterialMap.2048')),
    ],

# === Hand Knife Textures ===
'59c18114': [
        (log,                           ('3.0: Jane Hand Knife Diffuse Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],
'76cda993': [
        (log,                           ('3.0: Jane Hand Knife LightMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],
'd83ad325': [
        (log,                           ('3.0: Jane Hand Knife MaterialMap Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: Jane Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        (('3275b812', '9268a5af'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('3.0: Jane Shared NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        (('3275b812', '9268a5af'), 'Jane.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ba4255a5', 'Jane.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('294a319a', 'Jane.HandsAccessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f7a304e8', 'Jane.FootKnife.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoe',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}