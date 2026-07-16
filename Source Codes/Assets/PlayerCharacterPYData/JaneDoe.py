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
    ],

# === Legacy Hash Updates ===
'c8ad344e': [
        (log, ('1.1 -> 1.2: Jane Hair Texcoord Hash',)),
        (update_hash, ('257a90d6',)),
        (log, ('+ Remapping texcoord buffer',)),
        (zzz_12_shrink_texcoord_color, ('1.2',))
    ],
'5721e4e7': [(log, ('1.3 -> 1.4: Jane Hair Draw Hash',)),               (update_hash, ('2d06e785',))],
'24323bf9': [(log, ('1.3 -> 1.4: Jane Hair Position Hash',)),           (update_hash, ('e7a3b7dc',))],
'0a10c747': [(log, ('1.3 -> 1.4: Jane Hair Blend Hash',)),              (update_hash, ('8721477f',))],
'257a90d6': [(log, ('1.3 -> 1.4: Jane Hair Texcoord Hash',)),           (update_hash, ('acec29f8',))],
'40fca454': [(log, ('1.3 -> 1.4: Jane Hair MaterialMap Hash',)),        (update_hash, ('5e34e275',))],
'd1f56c7d': [(log, ('1.3 -> 1.4: Jane Body Diffuse 2048p Hash',)),            (update_hash, ('e62ae3b5',))],
'3087f82a': [(log, ('1.3 -> 1.4: Jane Body LightMap 2048p Hash',)),           (update_hash, ('52fa9861',))],
'99eae42e': [(log, ('1.3 -> 1.4: Jane Body MaterialMap 2048p Hash',)),        (update_hash, ('5dce2408',))],
'd1aa4b85': [(log, ('1.3 -> 1.4: Jane Body Draw Hash',)),                  (update_hash, ('0e1c6740',))],
'06f9bc49': [(log, ('1.3 -> 1.4: Jane Body Position Hash',)),              (update_hash, ('10050266',))],
'8b85c03e': [(log, ('1.3 -> 1.4: Jane Body Texcoord Hash',)),              (update_hash, ('949549de',))],

# === Legacy Hash Updates (continued) ===
'689639a5': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 1024p Hash',)), (update_hash, ('d823ac80',))],
'8974fb74': [(log, ('1.3 -> 1.4: Jane HeadA Diffuse 2048p Hash',)), (update_hash, ('3b75aa2c',))],
'9727a184': [(log, ('1.3 -> 1.4: Jane Body Blend Hash',)),    (update_hash, ('e27f398e',))],
'9f2f7c53': [(log, ('2.4 -> 2.5: Jane Head Texcoord Hash',)), (update_hash, ('1fa404c1',))],
'850d4cbf': [(log, ('2.1 -> 2.2: Jane Face Position Hash [Legacy]',)), (update_hash, ('eace2dfa',))],
'eace2dfa': [(log, ('2.2: Jane Face Position Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
'7fd655de': [(log, ('2.1 -> 2.2: Jane Face Texcoord Hash [Legacy]',)), (update_hash, ('535e2453',))],
'535e2453': [(log, ('2.2: Jane Face Texcoord Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
'a14461d9': [(log, ('2.1 -> 2.2: Jane Face Blend Hash [Legacy]',)), (update_hash, ('7310ad6a',))],
'7310ad6a': [(log, ('2.2: Jane Face Blend Hash Target [Legacy Reference]',)), (add_ib_check_if_missing,)],
'0165f71c': [(log, ('1.1: Jane BodyA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('e2c0144e',))],
'387dfc9f': [(log, ('1.1: Jane BodyA NormalMap 1024p Hash [Legacy]',)), (update_hash, ('e2c0144e',))],
'4aa12b36': [(log, ('1.1: Jane HairA NormalMap 2048p Hash [Legacy]',)), (update_hash, ('7b16a708',))],
'f0aded31': [(log, ('1.1: Jane HairA NormalMap 1024p Hash [Legacy]',)), (update_hash, ('7b16a708',))],

# === Legacy Transition Paths ===
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
        (log,                           ('3.0: Jane Hand Knife Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],
    '0158a68f': [
        (log,                           ('3.0: Jane Hand Knife Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('59c18114', 'Jane.HandKnife.Diffuse.2048')),
    ],
    '76cda993': [
        (log,                           ('3.0: Jane Hand Knife LightMap 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],
    '655a0c17': [
        (log,                           ('3.0: Jane Hand Knife LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('76cda993', 'Jane.HandKnife.LightMap.2048')),
    ],
    'd83ad325': [
        (log,                           ('3.0: Jane Hand Knife MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('602c545a', 'Jane.HandKnife.IB', 'match_priority = 0\n')),
    ],
    'f9f30a0e': [
        (log,                           ('3.0: Jane Hand Knife MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d83ad325', 'Jane.HandKnife.MaterialMap.2048')),
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