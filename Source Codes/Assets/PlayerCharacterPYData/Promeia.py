"""
Promeia Character Hash Commands
ZZZ Mod Fixer v2.8
Game Version: 2.8
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Promeia's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'a633d5b7': [
        (log,                           ('2.8 -> 2.81: Promeia Pinioned IB Hash',)),
        (update_hash,                        ('36e794ea',)),
    ],
'36e794ea': [
        (log,                           ('2.81 -> 3.0: Promeia Pinioned IB Hash',)),
        (update_hash,                        ('b386901d',)),
    ],
'b386901d': [
        (log,                           ('3.0: Promeia Pinioned IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'68f34958': [
        (log,                           ('2.8 -> 2.81: Promeia Clothes IB Hash',)),
        (update_hash,                        ('93f1f568',)),
    ],
'93f1f568': [
        (log,                           ('2.81 -> 3.0: Promeia Clothes IB Hash',)),
        (update_hash,                        ('0ae14c24',)),
    ],
'0ae14c24': [
        (log,                           ('3.0: Promeia Clothes IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'5ea47a32': [
        (log,                           ('2.8 -> 2.81: Promeia Face IB Hash',)),
        (update_hash,                        ('ef3c4506',)),
    ],
'ef3c4506': [
        (log,                           ('3.0: Promeia Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6cca89ab': [
        (log,                           ('2.8 -> 2.81: Promeia Hair IB Hash',)),
        (update_hash,                        ('31178971',)),
    ],
'31178971': [
        (log,                           ('2.81: Promeia Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'21871660': [
        (log,                           ('2.8 -> 2.81: Promeia Leg IB Hash',)),
        (update_hash,                        ('fd054d1d',)),
    ],
'fd054d1d': [
        (log,                           ('2.81 -> 3.0: Promeia Leg IB Hash',)),
        (update_hash,                        ('ec003379',)),
    ],
'ec003379': [
        (log,                           ('3.0: Promeia Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6abaa60a': [(log, ('2.8 -> 2.81: Promeia Torso IB Hash',)),      (update_hash, ('62a6b4bd',)),],
'62a6b4bd': [
        (log,                           ('2.81 -> 3.0: Promeia Torso IB Hash',)),
        (update_hash,                        ('10c77d62',)),
    ],
'10c77d62': [
        (log,                           ('3.0: Promeia Torso IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Promeia Textures (FaceA) ===
'328fa0cf': [
        (log,                           ('2.8: Promeia FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('9b293811', 'Promeia.FaceA.Diffuse.2048')),
    ],
'9b293811': [
        (log,                           ('2.8: Promeia FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('328fa0cf', 'Promeia.FaceA.Diffuse.1024')),
    ],

# === Promeia Textures (HairA) ===
'a0add414': [
        (log,                           ('2.8: Promeia HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('c96de436', 'Promeia.HairA.Diffuse.2048')),
    ],
'c96de436': [
        (log,                           ('2.8: Promeia HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('a0add414', 'Promeia.HairA.Diffuse.1024')),
    ],
'5c509f54': [
        (log,                           ('2.8: Promeia HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e34356a6', 'Promeia.HairA.LightMap.2048')),
    ],
'e34356a6': [
        (log,                           ('2.8: Promeia HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('5c509f54', 'Promeia.HairA.LightMap.1024')),
    ],
'1f96c5d7': [
        (log,                           ('2.8: Promeia HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6bed1450', 'Promeia.HairA.MaterialMap.2048')),
    ],
'6bed1450': [
        (log,                           ('2.8: Promeia HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('1f96c5d7', 'Promeia.HairA.MaterialMap.1024')),
    ],

# === Promeia Textures (BodyA) ===
'7d2d3a9e': [
        (log,                           ('2.8: Promeia BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('ae109401', 'Promeia.BodyA.Diffuse.2048')),
    ],
'ae109401': [
        (log,                           ('2.8: Promeia BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('7d2d3a9e', 'Promeia.BodyA.Diffuse.1024')),
    ],
'70ca6de8': [
        (log,                           ('2.8: Promeia BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('3864f20c', 'Promeia.BodyA.LightMap.2048')),
    ],
'3864f20c': [
        (log,                           ('2.8: Promeia BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('70ca6de8', 'Promeia.BodyA.LightMap.1024')),
    ],
'af976ad8': [
        (log,                           ('2.8: Promeia BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d57df6aa', 'Promeia.BodyA.MaterialMap.2048')),
    ],
'd57df6aa': [
        (log,                           ('2.8: Promeia BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('af976ad8', 'Promeia.BodyA.MaterialMap.1024')),
    ],

# === Promeia Textures (ClothesA) ===
'406b1373': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA Diffuse 1024p Hash',)),
        (update_hash,                        ('47d294f4',)),
    ],
'47d294f4': [
        (log,                           ('2.8: Promeia ClothesA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('b9367016', 'e1492a53'), 'Promeia.ClothesA.Diffuse.2048')),
    ],
'b9367016': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA Diffuse 2048p Hash',)),
        (update_hash,                        ('e1492a53',)),
    ],
'e1492a53': [
        (log,                           ('2.8: Promeia ClothesA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('406b1373', '47d294f4'), 'Promeia.ClothesA.Diffuse.1024')),
    ],
'044d2d39': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA LightMap 1024p Hash',)),
        (update_hash,                        ('562616d5',)),
    ],
'562616d5': [
        (log,                           ('2.8: Promeia ClothesA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        (('d743acd0', '9bf7f5cc'), 'Promeia.ClothesA.LightMap.2048')),
    ],
'd743acd0': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA LightMap 2048p Hash',)),
        (update_hash,                        ('9bf7f5cc',)),
    ],
'9bf7f5cc': [
        (log,                           ('2.8: Promeia ClothesA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        (('044d2d39', '562616d5'), 'Promeia.ClothesA.LightMap.1024')),
    ],
'01a5ba27': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA MaterialMap 1024p Hash',)),
        (update_hash,                        ('73aaae54',)),
    ],
'73aaae54': [
        (log,                           ('2.8: Promeia ClothesA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        (('31d7cbad', 'd37b40a9'), 'Promeia.ClothesA.MaterialMap.2048')),
    ],
'31d7cbad': [
        (log,                           ('2.8 -> 3.0: Promeia ClothesA MaterialMap 2048p Hash',)),
        (update_hash,                        ('d37b40a9',)),
    ],
'd37b40a9': [
        (log,                           ('2.8: Promeia ClothesA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        (('01a5ba27', '73aaae54'), 'Promeia.ClothesA.MaterialMap.1024')),
    ],

# === Promeia Textures (WeaponA) ===
'138bcaa1': [(log, ('2.8 -> 3.0: Promeia WeaponA Diffuse 1024p Hash',)), (update_hash, ('7750fc88',))],
'7750fc88': [
        (log,                           ('2.8: Promeia WeaponA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('d1399215', '328135c5'), 'Promeia.WeaponA.Diffuse.2048')),
    ],
'd1399215': [(log, ('2.8 -> 3.0: Promeia WeaponA Diffuse 2048p Hash',)), (update_hash, ('328135c5',))],
'328135c5': [
        (log,                           ('2.8: Promeia WeaponA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('138bcaa1', '7750fc88'), 'Promeia.WeaponA.Diffuse.1024')),
    ],
'5e59380e': [(log, ('2.8 -> 3.0: Promeia WeaponA LightMap 1024p Hash',)), (update_hash, ('a1988612',))],
'a1988612': [
        (log,                           ('2.8: Promeia WeaponA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        (('369f0efd', '82f4146a'), 'Promeia.WeaponA.LightMap.2048')),
    ],
'369f0efd': [(log, ('2.8 -> 3.0: Promeia WeaponA LightMap 2048p Hash',)), (update_hash, ('82f4146a',))],
'82f4146a': [
        (log,                           ('2.8: Promeia WeaponA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        (('5e59380e', 'a1988612'), 'Promeia.WeaponA.LightMap.1024')),
    ],
'09271c02': [(log, ('2.8 -> 3.0: Promeia WeaponA MaterialMap 1024p Hash',)), (update_hash, ('7559d574',))],
'7559d574': [
        (log,                           ('2.8: Promeia WeaponA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        (('a179a69c', 'd672b87c'), 'Promeia.WeaponA.MaterialMap.2048')),
    ],
'a179a69c': [(log, ('2.8 -> 3.0: Promeia WeaponA MaterialMap 2048p Hash',)), (update_hash, ('d672b87c',))],
'd672b87c': [
        (log,                           ('2.8: Promeia WeaponA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        (('09271c02', '7559d574'), 'Promeia.WeaponA.MaterialMap.1024')),
    ],
'35096cb6': [(log, ('2.8 -> 2.81: Promeia Hair Position Hash',)),(update_hash, ('681aceaa',)),],
'681aceaa': [
        (log, ('3.0: Promeia Hair VB Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'9c0aad96': [(log, ('2.8 -> 2.81: Promeia Hair Texcoord Hash',)),(update_hash, ('84d40d91',)),],
'84d40d91': [
        (log, ('3.0: Promeia Hair VB Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'5a263750': [(log, ('2.8 -> 2.81: Promeia Hair Blend Hash',)),   (update_hash, ('3d4a4881',)),],
'3d4a4881': [
        (log, ('3.0: Promeia Hair VB Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Promeia Hair TEX Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'de6eb63b': [(log, ('2.8 -> 2.81: Promeia Shadow IB Hash',)),      (update_hash, ('ff223b2c',)),],
'ff223b2c': [(log, ('3.0: Promeia HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'19ad87f6': [(log, ('2.81 -> 3.0: Promeia Pinioned Draw Hash',)),    (update_hash, ('dd86f5ae',)),],
'dd86f5ae': [
        (log, ('3.0: Promeia Body(BoundState) VB Hash',)),
        (add_section_if_missing, ('b386901d', 'Promeia.Body(BoundState).IB', 'match_priority = 0\n')),
    ],
'a7769c93': [(log, ('2.8 -> 2.81: Promeia Pinioned Position Hash',)),(update_hash, ('ffaa183a',)),],
'ffaa183a': [(log, ('2.81 -> 3.0: Promeia Pinioned Position Hash',)),(update_hash, ('68e2baef',)),],
'68e2baef': [
        (log, ('3.0: Promeia Body(BoundState) VB Hash',)),
        (add_section_if_missing, ('b386901d', 'Promeia.Body(BoundState).IB', 'match_priority = 0\n')),
    ],
'bfcfb2f7': [(log, ('2.8 -> 2.81: Promeia Pinioned Texcoord Hash',)),(update_hash, ('2a9842a1',)),],
'2a9842a1': [(log, ('2.81 -> 3.0: Promeia Pinioned Texcoord Hash',)),(update_hash, ('6fe5f8c1',)),],
'6fe5f8c1': [
        (log, ('3.0: Promeia Body(BoundState) VB Hash',)),
        (add_section_if_missing, ('b386901d', 'Promeia.Body(BoundState).IB', 'match_priority = 0\n')),
    ],
'61c399b6': [(log, ('2.8 -> 2.81: Promeia Pinioned Blend Hash',)),   (update_hash, ('dae4abd0',)),],
'dae4abd0': [(log, ('2.81 -> 3.0: Promeia Pinioned Blend Hash',)),   (update_hash, ('112582ea',)),],
'112582ea': [
        (log, ('3.0: Promeia Body(BoundState) VB Hash',)),
        (add_section_if_missing, ('b386901d', 'Promeia.Body(BoundState).IB', 'match_priority = 0\n')),
    ],
'bf938187': [(log, ('2.81 -> 3.0: Promeia Torso Position Hash',)),(update_hash, ('2dbfe8c9',)),],
'2dbfe8c9': [
        (log, ('3.0: Promeia Body(Normal) VB Hash',)),
        (add_section_if_missing, ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
    ],
'b1ec331c': [(log, ('2.8 -> 2.81: Promeia Torso Texcoord Hash',)),(update_hash, ('d99d21e0',)),],
'd99d21e0': [(log, ('2.81 -> 3.0: Promeia Torso Texcoord Hash',)),(update_hash, ('1fc95f5b',)),],
'1fc95f5b': [
        (log, ('3.0: Promeia Body(Normal) VB Hash',)),
        (add_section_if_missing, ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
    ],
'bca960d0': [(log, ('2.8 -> 2.81: Promeia Torso Blend Hash',)),   (update_hash, ('575d8b1b',)),],
'575d8b1b': [(log, ('2.81 -> 3.0: Promeia Torso Blend Hash',)),   (update_hash, ('ee35cc06',)),],
'ee35cc06': [
        (log, ('3.0: Promeia Body(Normal) VB Hash',)),
        (add_section_if_missing, ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
    ],
'd43597aa': [(log, ('2.8 -> 2.81: Promeia Clothes Position Hash',)),(update_hash, ('1d63183b',)),],
'1d63183b': [(log, ('2.81 -> 3.0: Promeia Clothes Position Hash',)),(update_hash, ('f6cc27b6',)),],
'f6cc27b6': [
        (log, ('3.0: Promeia Clothes VB Hash',)),
        (add_section_if_missing, ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'9f083955': [(log, ('2.8 -> 2.81: Promeia Clothes Texcoord Hash',)),(update_hash, ('826446a7',)),],
'826446a7': [(log, ('2.81 -> 3.0: Promeia Clothes Texcoord Hash',)),(update_hash, ('bf00cc95',)),],
'bf00cc95': [
        (log, ('3.0: Promeia Clothes VB Hash',)),
        (add_section_if_missing, ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'870f56b5': [(log, ('2.8 -> 2.81: Promeia Clothes Blend Hash',)),   (update_hash, ('58f42be3',)),],
'58f42be3': [(log, ('2.81 -> 3.0: Promeia Clothes Blend Hash',)),   (update_hash, ('4b0d6867',)),],
'4b0d6867': [
        (log, ('3.0: Promeia Clothes VB Hash',)),
        (add_section_if_missing, ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'595bd76e': [(log, ('2.8 -> 2.81: Promeia Leg Position Hash',)),(update_hash, ('0b822797',)),],
'0b822797': [(log, ('2.81 -> 3.0: Promeia Leg Position Hash',)),(update_hash, ('4c1d0a70',)),],
'4c1d0a70': [
        (log, ('3.0: Promeia Leg VB Hash',)),
        (add_section_if_missing, ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
    ],
'2918714e': [(log, ('2.8 -> 2.81: Promeia Leg Texcoord Hash',)),(update_hash, ('f5fd0e92',)),],
'f5fd0e92': [(log, ('2.81 -> 3.0: Promeia Leg Texcoord Hash',)),(update_hash, ('03d6f933',)),],
'03d6f933': [
        (log, ('3.0: Promeia Leg VB Hash',)),
        (add_section_if_missing, ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
    ],
'fd3c3d9f': [(log, ('2.8 -> 2.81: Promeia Leg Blend Hash',)),   (update_hash, ('9839b071',)),],
'9839b071': [(log, ('2.81 -> 3.0: Promeia Leg Blend Hash',)),   (update_hash, ('65bba179',)),],
'65bba179': [
        (log, ('3.0: Promeia Leg VB Hash',)),
        (add_section_if_missing, ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
    ],
'cb9d17fc': [(log, ('2.8 -> 2.81: Promeia Eyebrow IB Hash',)),      (update_hash, ('e032287a',)),],
'e032287a': [(log, ('3.0: Promeia Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'a1d5b256': [
        (log, ('3.0: Promeia Eyebrow VB Hash',)),
        (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'9bc72111': [
        (log, ('3.0: Promeia Eyebrow VB Hash',)),
        (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'3a00aa76': [(log, ('2.8 -> 2.81: Promeia Eyebrow Texcoord Hash',)),(update_hash, ('d3d65ca5',)),],
'd3d65ca5': [
        (log, ('3.0: Promeia Eyebrow VB Hash',)),
        (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'42594132': [
        (log, ('3.0: Promeia Eyebrow VB Hash',)),
        (add_section_if_missing, ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'08b11ea1': [
        (log, ('3.0: Promeia Face VB Hash',)),
        (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
    ],
'b7a6479f': [(log, ('2.8 -> 2.81: Promeia Face Texcoord Hash',)),(update_hash, ('dcd61276',)),],
'dcd61276': [
        (log, ('3.0: Promeia Face VB Hash',)),
        (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
    ],
'5ff41c34': [(log, ('2.8 -> 2.81: Promeia Face Blend Hash',)),   (update_hash, ('bf5b785d',)),],
'bf5b785d': [
        (log, ('3.0: Promeia Face VB Hash',)),
        (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
    ],
'947ceb88': [(log, ('2.8 -> 2.81: Promeia Weapon IB Hash',)),      (update_hash, ('8995db58',)),],
'8995db58': [(log, ('3.0: Promeia Weapon IB Hash',)), (add_ib_check_if_missing,)],
'7d76d686': [(log, ('2.8 -> 2.81: Promeia Weapon Draw Hash',)),    (update_hash, ('0a06059e',)),],
'0a06059e': [
        (log, ('3.0: Promeia Weapon VB Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'35ecba91': [
        (log, ('3.0: Promeia Weapon VB Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'064658e2': [
        (log, ('3.0: Promeia Weapon VB Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'21ac80fa': [(log, ('2.8 -> 2.81: Promeia Weapon Blend Hash',)),   (update_hash, ('a864dc82',)),],
'a864dc82': [
        (log, ('3.0: Promeia Weapon VB Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Promeia Hair TEX Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'32a38de6': [
        (log, ('3.0: Promeia Face VB Hash',)),
        (add_section_if_missing, ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
    ],
'dfb01010': [
        (log, ('3.0: Promeia Leg VB Hash',)),
        (add_section_if_missing, ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
    ],
'947f29ae': [
        (log, ('3.0: Promeia Clothes VB Hash',)),
        (add_section_if_missing, ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
    ],
'9cce6ba2': [
        (log, ('3.0: Promeia Body(Normal) VB Hash',)),
        (add_section_if_missing, ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
    ],
'2d4c7c18': [
        (log, ('3.0: Promeia Hair VB Hash',)),
        (add_section_if_missing, ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
    ],
'2f3a560d': [(log, ('2.8 -> 2.81: Promeia Weapon Position Hash',)),(update_hash, ('d242b77a',)),],
'23587131': [(log, ('2.8 -> 2.81: Promeia Weapon Texcoord Hash',)),(update_hash, ('f2f5bd28',)),],
'd242b77a': [
        (log, ('2.81: Promeia Weapon Position Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
'f2f5bd28': [
        (log, ('2.81: Promeia Weapon Texcoord Hash',)),
        (add_section_if_missing, ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Promeia',
    'game_versions': ['2.8', '2.81', '3.0'],
}

