"""
Yixuan Character Hash Commands
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
    Returns Yixuan's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# Hash Updates (Old -> New)
'0219df6e': [(log, ('1.0 -> 2.5: Yixuan Bottle IB Hash',)),           (update_hash, ('1630f2d0',))],
'55638d51': [(log, ('1.0 -> 2.5: Yixuan Bottle Blend Hash',)),        (update_hash, ('d89da8eb',))],
'd0ff2c18': [(log, ('1.0 -> 2.5: Yixuan Bottle Position Hash',)),     (update_hash, ('8555098d',))],
'f05da93a': [(log, ('1.0 -> 2.5: Yixuan Bottle Texcoord Hash',)),     (update_hash, ('ff4b112b',))],
'd000beae': [(log, ('1.0 -> 2.5: Yixuan Bottle Draw Hash',)),         (update_hash, ('05466ddf',))],

# IB Hashes
'ac8e9ee3': [(log, ('2.5: Yixuan Hair IB Hash',)),      (add_ib_check_if_missing,)],
'029c1f5a': [(log, ('2.5: Yixuan Body IB Hash',)),      (add_ib_check_if_missing,)],
'1630f2d0': [(log, ('2.5: Yixuan Bottle IB Hash',)),    (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.5: Yixuan BottleGlass IB Hash',)),(add_ib_check_if_missing,)],
'67c61080': [(log, ('2.5: Yixuan Coins IB Hash',)),     (add_ib_check_if_missing,)],
'892858fd': [(log, ('2.5: Yixuan Hairpin IB Hash',)),   (add_ib_check_if_missing,)],
'8c2fc05e': [(log, ('2.5: Yixuan Jacket IB Hash',)),    (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.5: Yixuan Face IB Hash',)),      (add_ib_check_if_missing,)],

# Bottle Vertex Buffer Hashes
'd89da8eb': [(log, ('2.5: Yixuan Bottle Blend Hash',))],
'8555098d': [(log, ('2.5: Yixuan Bottle Position Hash',))],
'ff4b112b': [(log, ('2.5: Yixuan Bottle Texcoord Hash',))],

# Bottle Draw Hash
'05466ddf': [(log, ('2.5: Yixuan Bottle Draw Hash',))],

# Shared Texture Hashes (used across multiple components)
'ebac056e': [
        (log,                           ('2.5: Yixuan Shared NormalMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],

# Hair, Bottle, BottleGlass, Coins Shared Textures
'7e38b38b': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('84fe943d', 'Yixuan.HairA.Diffuse.1024')),
    ],

'84fe943d': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7e38b38b', 'Yixuan.HairA.Diffuse.2048')),
    ],
'086ac064': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5574ca9f', 'Yixuan.HairA.LightMap.1024')),
    ],

'5574ca9f': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins LightMap 1024p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('086ac064', 'Yixuan.HairA.LightMap.2048')),
    ],
'83b02982': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f4ac690c', 'Yixuan.HairA.MaterialMap.1024')),
    ],

'f4ac690c': [
        (log,                           ('2.5: Yixuan Hair/Bottle/BottleGlass/Coins MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('67c61080', 'Yixuan.Coins.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('83b02982', 'Yixuan.HairA.MaterialMap.2048')),
    ],

# Body and Hairpin Shared Textures
'2a4f37a6': [
        (log,                           ('2.5: Yixuan Body/Hairpin Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d7db2bc6', 'Yixuan.BodyA.Diffuse.1024')),
    ],

'd7db2bc6': [
        (log,                           ('2.5: Yixuan Body/Hairpin Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2a4f37a6', 'Yixuan.BodyA.Diffuse.2048')),
    ],
'5a291e85': [
        (log,                           ('2.5: Yixuan Body/Hairpin LightMap 2048p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('96f754a7', 'Yixuan.BodyA.LightMap.1024')),
    ],

'96f754a7': [
        (log,                           ('2.5: Yixuan Body/Hairpin LightMap 1024p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5a291e85', 'Yixuan.BodyA.LightMap.2048')),
    ],
'd28370ec': [
        (log,                           ('2.5: Yixuan Body/Hairpin MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('aa1056a5', 'Yixuan.BodyA.MaterialMap.1024')),
    ],

'aa1056a5': [
        (log,                           ('2.5: Yixuan Body/Hairpin MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d28370ec', 'Yixuan.BodyA.MaterialMap.2048')),
    ],

# Jacket Textures
'e6dca725': [
        (log,                           ('2.5: Yixuan Jacket Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1fcedcc3', 'Yixuan.CoatA.Diffuse.1024')),
    ],

'1fcedcc3': [
        (log,                           ('2.5: Yixuan Jacket Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e6dca725', 'Yixuan.CoatA.Diffuse.2048')),
    ],
'59b2daf9': [
        (log,                           ('2.5: Yixuan Jacket LightMap 2048p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c4d167c3', 'Yixuan.CoatA.LightMap.1024')),
    ],

'c4d167c3': [
        (log,                           ('2.5: Yixuan Jacket LightMap 1024p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('59b2daf9', 'Yixuan.CoatA.LightMap.2048')),
    ],
'bb581f1e': [
        (log,                           ('2.5: Yixuan Jacket MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fd56fa4b', 'Yixuan.CoatA.MaterialMap.1024')),
    ],

'fd56fa4b': [
        (log,                           ('2.5: Yixuan Jacket MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('bb581f1e', 'Yixuan.CoatA.MaterialMap.2048')),
    ],

# Face Textures
'7d9ee001': [
        (log,                           ('2.5: Yixuan Face Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9efd1605', 'Yixuan.FaceA.Diffuse.1024')),
    ],

'9efd1605': [
        (log,                           ('2.5: Yixuan Face Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7d9ee001', 'Yixuan.FaceA.Diffuse.2048')),
    ],
'36a68b27': [
        (log, ('3.0: Yixuan Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'cc898b44': [
        (log, ('3.0: Yixuan Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'd4841137': [
        (log, ('3.0: Yixuan Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'd7eb400e': [
        (log, ('3.0: Yixuan Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'd28b9c82': [(log, ('3.0: Yixuan Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'7f5aba6c': [
        (log, ('3.0: Yixuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'c7748cbd': [
        (log, ('3.0: Yixuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a07eb5cf': [
        (log, ('3.0: Yixuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'07c7e48f': [
        (log, ('3.0: Yixuan Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f922d854': [
        (log, ('3.0: Yixuan Body VB Hash',)),
        (add_section_if_missing, ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'155737d9': [
        (log, ('3.0: Yixuan Body VB Hash',)),
        (add_section_if_missing, ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'7af146a0': [
        (log, ('3.0: Yixuan Body VB Hash',)),
        (add_section_if_missing, ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'3e629c05': [
        (log, ('3.0: Yixuan Body VB Hash',)),
        (add_section_if_missing, ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
    ],
'ddaf88bc': [
        (log, ('3.0: Yixuan Copper coin string VB Hash',)),
        (add_section_if_missing, ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
    ],
'eaf79039': [
        (log, ('3.0: Yixuan Copper coin string VB Hash',)),
        (add_section_if_missing, ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
    ],
'9714e6e6': [
        (log, ('3.0: Yixuan Copper coin string VB Hash',)),
        (add_section_if_missing, ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
    ],
'ee9b9cfe': [
        (log, ('3.0: Yixuan Copper coin string VB Hash',)),
        (add_section_if_missing, ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
    ],
'ba017cf3': [
        (log, ('3.0: Yixuan Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'3194141e': [
        (log, ('3.0: Yixuan Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'b3123168': [
        (log, ('3.0: Yixuan Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'de9d3ab7': [
        (log, ('3.0: Yixuan Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
    ],
'73599fbb': [
        (log, ('3.0: Yixuan Jacket VB Hash',)),
        (add_section_if_missing, ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'9b67bc72': [
        (log, ('3.0: Yixuan Jacket VB Hash',)),
        (add_section_if_missing, ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'9f95d565': [
        (log, ('3.0: Yixuan Jacket VB Hash',)),
        (add_section_if_missing, ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'0ff3af5a': [
        (log, ('3.0: Yixuan Jacket VB Hash',)),
        (add_section_if_missing, ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
    ],
'972e4b6d': [
        (log, ('3.0: Yixuan Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
    ],
'2e04aac2': [
        (log, ('3.0: Yixuan Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
    ],
'4466e7ea': [
        (log, ('3.0: Yixuan Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
    ],
'ce38ac3b': [(log, ('3.0: Yixuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'9052084b': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'f45313a0': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'3ac6dfc7': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'920caf66': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'771d52eb': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'dc3c5667': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'fd2cbc71': [(log, ('3.0: Yixuan weapon IB Hash',)), (add_ib_check_if_missing,)],
'1a201296': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'1a0934e4': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'2ad5c986': [
        (log, ('3.0: Yixuan weapon VB Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'7f504f10': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'96254967': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'4300c703': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'5a016c9b': [(log, ('3.0: Yixuan misc hash',)),],
'ad3cd82a': [(log, ('3.0: Yixuan misc hash',)),],
'ccbbb7ea': [(log, ('3.0: Yixuan misc hash',)),],
'798adba3': [
        (log, ('3.0: Yixuan Hair TEX Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
    ],
'677893d2': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'd1ee41dc': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'23d4f666': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'9263dc92': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'fc9ae2ff': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
'5e60bc3d': [
        (log, ('3.0: Yixuan weapon TEX Hash',)),
        (add_section_if_missing, ('fd2cbc71', 'Yixuan.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yixuan',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Bottle', 'BottleGlass', 'Coins', 'Hairpin', 'Jacket', 'Face'],
}
