"""
Dialyn Character Hash Commands
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
    Returns Dialyn's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hash Updates ===
'6ff0e4ad': [(log, ('2.5: 1 Dialyn Body blend',)), (update_hash, ('3d7e53cf',))],

# === IB Hashes ===
'68f00074': [(log, ('2.5: Dialyn Hair IB Hash',)), (add_ib_check_if_missing,)],
'af39a873': [(log, ('2.5: Dialyn Body IB Hash',)), (add_ib_check_if_missing,)],
'cd519abe': [(log, ('2.5: Dialyn PhoneCable IB Hash',)), (add_ib_check_if_missing,)],
'd860525e': [(log, ('2.5: Dialyn Brows IB Hash',)), (add_ib_check_if_missing,)],
'facb2461': [(log, ('2.5: Dialyn Face IB Hash',)), (add_ib_check_if_missing,)],

# === Hair Textures (shared with PhoneCable) ===
'4f8d9492': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4dfbd393', 'Dialyn.HairA.Diffuse.1024')),
    ],

'4dfbd393': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4f8d9492', 'Dialyn.HairA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA, BodyA NormalMap Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe', 'af39a873'), 'Dialyn.NormalMap', 'match_priority = 0\n')),
    ],
'a3f74f7d': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA LightMap 2048p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.LightMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('df9b8ecd', 'Dialyn.HairA.LightMap.1024')),
    ],

'df9b8ecd': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA LightMap 1024p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.LightMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a3f74f7d', 'Dialyn.HairA.LightMap.2048')),
    ],
'17aadaf6': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.MaterialMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5e6d6607', 'Dialyn.HairA.MaterialMap.1024')),
    ],

'5e6d6607': [
        (log,                           ('2.5: Dialyn HairA, PhoneCableA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        (('68f00074', 'cd519abe'), 'Dialyn.HairA.MaterialMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('17aadaf6', 'Dialyn.HairA.MaterialMap.2048')),
    ],

# === Body Textures ===
'52ea588e': [
        (log,                           ('2.5: Dialyn BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('76ca930e', 'Dialyn.BodyA.Diffuse.1024')),
    ],

'76ca930e': [
        (log,                           ('2.5: Dialyn BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('52ea588e', 'Dialyn.BodyA.Diffuse.2048')),
    ],
'5cc175fe': [
        (log,                           ('2.5: Dialyn BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.LightMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8c2fea9f', 'Dialyn.BodyA.LightMap.1024')),
    ],

'8c2fea9f': [
        (log,                           ('2.5: Dialyn BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.LightMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5cc175fe', 'Dialyn.BodyA.LightMap.2048')),
    ],
'28a10401': [
        (log,                           ('2.5: Dialyn BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.MaterialMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a2425ea0', 'Dialyn.BodyA.MaterialMap.1024')),
    ],

'a2425ea0': [
        (log,                           ('2.5: Dialyn BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('af39a873', 'Dialyn.BodyA.MaterialMap', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('28a10401', 'Dialyn.BodyA.MaterialMap.2048')),
    ],

# === Face/Brows Textures ===
'ad65abbf': [
        (log,                           ('2.5: Dialyn FaceA, BrowsA Diffuse 2048p Hash',)),
        (add_section_if_missing,        (('facb2461', 'd860525e'), 'Dialyn.FaceA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('56bc2921', 'Dialyn.FaceA.Diffuse.1024')),
    ],

'56bc2921': [
        (log,                           ('2.5: Dialyn FaceA, BrowsA Diffuse 1024p Hash',)),
        (add_section_if_missing,        (('facb2461', 'd860525e'), 'Dialyn.FaceA.Diffuse', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ad65abbf', 'Dialyn.FaceA.Diffuse.2048')),
    ],
'00e453e9': [
        (log, ('3.0: Dialyn Hair VB Hash',)),
        (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
    ],
'a486f1bb': [
        (log, ('3.0: Dialyn Hair VB Hash',)),
        (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
    ],
'46019c5e': [
        (log, ('3.0: Dialyn Hair VB Hash',)),
        (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
    ],
'339f41eb': [
        (log, ('3.0: Dialyn Hair VB Hash',)),
        (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
    ],
'59390f5a': [(log, ('3.0: Dialyn Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'2e77bd1d': [
        (log, ('3.0: Dialyn Body VB Hash',)),
        (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
    ],
'ff36809b': [
        (log, ('3.0: Dialyn Body VB Hash',)),
        (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
    ],
'3f2079bc': [
        (log, ('3.0: Dialyn Body VB Hash',)),
        (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
    ],
'3d7e53cf': [
        (log, ('3.0: Dialyn Body VB Hash',)),
        (add_section_if_missing, ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
    ],
'38ce65ff': [
        (log, ('3.0: Dialyn TelephoneLine VB Hash',)),
        (add_section_if_missing, ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
    ],
'd0470351': [
        (log, ('3.0: Dialyn TelephoneLine VB Hash',)),
        (add_section_if_missing, ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
    ],
'2e6484db': [
        (log, ('3.0: Dialyn TelephoneLine VB Hash',)),
        (add_section_if_missing, ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
    ],
'312b6e12': [
        (log, ('3.0: Dialyn TelephoneLine VB Hash',)),
        (add_section_if_missing, ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
    ],
'fecc9606': [
        (log, ('3.0: Dialyn Eyebrow VB Hash',)),
        (add_section_if_missing, ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'c4de0541': [
        (log, ('3.0: Dialyn Eyebrow VB Hash',)),
        (add_section_if_missing, ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'd90368ed': [
        (log, ('3.0: Dialyn Eyebrow VB Hash',)),
        (add_section_if_missing, ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'7ec67741': [
        (log, ('3.0: Dialyn Eyebrow VB Hash',)),
        (add_section_if_missing, ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'fe5fb676': [
        (log, ('3.0: Dialyn Face VB Hash',)),
        (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
    ],
'c44d2531': [
        (log, ('3.0: Dialyn Face VB Hash',)),
        (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
    ],
'f6c5296e': [
        (log, ('3.0: Dialyn Face VB Hash',)),
        (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
    ],
'08923d3e': [
        (log, ('3.0: Dialyn Face VB Hash',)),
        (add_section_if_missing, ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
    ],
'1d8f8de6': [(log, ('3.0: Dialyn WeaponGrip IB Hash',)), (add_ib_check_if_missing,)],
'25f309c9': [
        (log, ('3.0: Dialyn WeaponGrip VB Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'fd32eb72': [
        (log, ('2.8: Dialyn WeaponGrip position_vb Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'5455d3c6': [
        (log, ('2.8: Dialyn WeaponGrip texcoord_vb Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'8fe19cc1': [
        (log, ('2.8: Dialyn WeaponGrip blend_vb Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'236576ee': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'036f72b3': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'4f0dc4f4': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'caa3c4ef': [(log, ('3.0: Dialyn WeaponChakramA IB Hash',)), (add_ib_check_if_missing,)],
'257c4603': [
        (log, ('3.0: Dialyn WeaponChakramA VB Hash',)),
        (add_section_if_missing, ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
    ],
'aae47bf3': [(log, ('3.0: Dialyn WeaponChakramB IB Hash',)), (add_ib_check_if_missing,)],
'798adba3': [
        (log, ('3.0: Dialyn Hair TEX Hash',)),
        (add_section_if_missing, ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
    ],
'87d209c3': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'a2264d99': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],
'7b07624c': [
        (log, ('3.0: Dialyn WeaponGrip TEX Hash',)),
        (add_section_if_missing, ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
    ],

# Historical hashes (2.4-2.7): WeaponGrip & Hair Shadow VB lama
'35709db4': [
        (log,                           ('2.4: Dialyn WeaponGrip Blend VB Hash',)),
        (update_hash,                   ('8fe19cc1',)),
    ],
'79fc6a95': [
        (log,                           ('2.4: Dialyn WeaponGrip Position VB Hash',)),
        (update_hash,                   ('fd32eb72',)),
    ],
'c0f5d550': [
        (log,                           ('2.4: Dialyn WeaponGrip Texcoord VB Hash',)),
        (update_hash,                   ('5455d3c6',)),
    ],
'3c007110': [
        (log,                           ('2.4: Dialyn Hair Shadow Draw VB Hash',)),
    ],
'42501c05': [
        (log,                           ('2.4: Dialyn Hair Shadow Position VB Hash',)),
    ],
'923b7623': [
        (log,                           ('2.4: Dialyn Hair Shadow Blend VB Hash',)),
    ],
'a935146f': [
        (log,                           ('2.4: Dialyn Hair Shadow Texcoord VB Hash',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Dialyn',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'PhoneCable', 'Brows', 'Face'],
}
