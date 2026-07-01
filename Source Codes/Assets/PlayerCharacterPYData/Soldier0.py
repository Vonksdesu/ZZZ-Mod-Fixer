"""
Soldier0 Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
Pembaruan Database 2.8 oleh AI & Komunitas
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Soldier0's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
# ========== Hair Component ==========
'217ec790': [(log, ('2.5: Soldier0 Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Diffuse
'aa3d57ff': [
        (log,                           ('2.5: Soldier0 HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8cb4086a', 'Soldier0.HairA.Diffuse.1024')),
    ],
'8cb4086a': [
        (log,                           ('2.5: Soldier0 HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('aa3d57ff', 'Soldier0.HairA.Diffuse.2048')),
    ],

# Hair NormalMap
'ebac056e': [
        (log,                           ('2.5: Soldier0 HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f8e9a6c1', 'Soldier0.HairA.NormalMap.1024')),
    ],
'f8e9a6c1': [
        (log,                           ('2.5: Soldier0 HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Soldier0.HairA.NormalMap.2048')),
    ],

# Hair LightMap
'8d42a55b': [
        (log,                           ('2.5: Soldier0 HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('96a28554', 'Soldier0.HairA.LightMap.1024')),
    ],
'96a28554': [
        (log,                           ('2.5: Soldier0 HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8d42a55b', 'Soldier0.HairA.LightMap.2048')),
    ],

# Hair MaterialMap (v1.6 -> v2.5 update)
'464847b3': [(log, ('1.6: Soldier0 HairA MaterialMap 2048p Hash (Old)',)), (update_hash, ('0b059f91',))],
'0b059f91': [
        (log,                           ('2.5: Soldier0 HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ce3e73be', 'Soldier0.HairA.MaterialMap.1024')),
    ],
'ce3e73be': [
        (log,                           ('2.5: Soldier0 HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0b059f91', 'Soldier0.HairA.MaterialMap.2048')),
    ],

# ========== Body Component ==========
'53d3f4e5': [(log, ('2.5: Soldier0 Body IB Hash',)), (add_ib_check_if_missing,)],

# Body Diffuse
'627baf3f': [
        (log,                           ('2.5: Soldier0 BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0acef326', 'Soldier0.BodyA.Diffuse.1024')),
    ],
'0acef326': [
        (log,                           ('2.5: Soldier0 BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('627baf3f', 'Soldier0.BodyA.Diffuse.2048')),
    ],

# Body LightMap
'3a56b70b': [
        (log,                           ('2.5: Soldier0 BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('625ad0eb', 'Soldier0.BodyA.LightMap.1024')),
    ],
'625ad0eb': [
        (log,                           ('2.5: Soldier0 BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3a56b70b', 'Soldier0.BodyA.LightMap.2048')),
    ],

# Body MaterialMap
'7cfa12b6': [
        (log,                           ('2.5: Soldier0 BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dea3c5a0', 'Soldier0.BodyA.MaterialMap.1024')),
    ],
'dea3c5a0': [
        (log,                           ('2.5: Soldier0 BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7cfa12b6', 'Soldier0.BodyA.MaterialMap.2048')),
    ],

# ========== Face Component ==========
# Face IB (v1.6 -> v2.5 update)
'f2f539b8': [(log, ('1.6: Soldier0 Face IB Hash (Old)',)), (update_hash, ('e30ca87f',))],
'e30ca87f': [(log, ('2.5: Soldier0 Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Diffuse
'05d7b504': [
        (log,                           ('2.5: Soldier0 FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('692c6d2b', 'Soldier0.FaceA.Diffuse.1024')),
    ],
'692c6d2b': [
        (log,                           ('2.5: Soldier0 FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('05d7b504', 'Soldier0.FaceA.Diffuse.2048')),
    ],

# === Legacy Hash Updates ===
'fb432d20': [(log, ('2.0 -> 2.8: Soldier0 Weapon Diffuse Hash [Legacy]',)), (update_hash, ('c85b4097',))],
'1a20e036': [(log, ('2.0 -> 2.8: Soldier0 Weapon LightMap Hash [Legacy]',)), (update_hash, ('8353de2a',))],
'45f422c0': [(log, ('2.0 -> 2.8: Soldier0 Weapon MaterialMap Hash [Legacy]',)), (update_hash, ('88fe0e3c',))],
'57c9f0a3': [(log, ('1.7 -> 2.0: Soldier0 Face Blend Hash',)), (update_hash, ('df6b6f84',))],
'6a492df0': [(log, ('1.7 -> 2.0: Soldier0 Face Texcoord Hash',)), (update_hash, ('fc66ecd0',))],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# New Index Buffer (IB) Hashes
'3431e8b4': [(log, ('2.8: Soldier0 HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'4d5c8ade': [(log, ('2.8: Soldier0 ShortDagger IB Hash',)), (add_ib_check_if_missing,)],
'6df60902': [(log, ('2.8: Soldier0 LongDagger IB Hash',)),  (add_ib_check_if_missing,)],

# Hair VBs
'9a4ae9c7': [(log, ('2.8: Soldier0 Hair draw_vb',)),                    (add_section_if_missing, ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n'))],
'7aa2035c': [(log, ('2.8: Soldier0 Hair position_vb',)),                (add_section_if_missing, ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n'))],
'c6b7b3b2': [(log, ('2.8: Soldier0 Hair texcoord_vb',)),                (add_section_if_missing, ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n'))],
'd13ddfe1': [(log, ('2.8: Soldier0 Hair blend_vb',)),                   (add_section_if_missing, ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow VBs
'dd91b126': [(log, ('2.8: Soldier0 HairShadow draw_vb',)),              (add_section_if_missing, ('3431e8b4', 'Soldier0.HairShadow.IB', 'match_priority = 0\n'))],
'183df742': [(log, ('2.8: Soldier0 HairShadow position_vb',)),          (add_section_if_missing, ('3431e8b4', 'Soldier0.HairShadow.IB', 'match_priority = 0\n'))],
'2b4afe3c': [(log, ('2.8: Soldier0 HairShadow texcoord_vb',)),          (add_section_if_missing, ('3431e8b4', 'Soldier0.HairShadow.IB', 'match_priority = 0\n'))],
'376b601d': [(log, ('2.8: Soldier0 HairShadow blend_vb',)),             (add_section_if_missing, ('3431e8b4', 'Soldier0.HairShadow.IB', 'match_priority = 0\n'))],

# Body VBs
'36089968': [(log, ('2.8: Soldier0 Body draw_vb',)),                    (add_section_if_missing, ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n'))],
'f1c057e8': [(log, ('2.8: Soldier0 Body position_vb',)),                (add_section_if_missing, ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n'))],
'80d87313': [(log, ('2.8: Soldier0 Body texcoord_vb',)),                (add_section_if_missing, ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n'))],
'd4ff3f35': [(log, ('2.8: Soldier0 Body blend_vb',)),                   (add_section_if_missing, ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n'))],

# Face VBs & Limits
'9f6aa443': [(log, ('2.8: Soldier0 Face VertexLimit',)),                (add_section_if_missing, ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n'))],
'a5783704': [(log, ('2.8: Face Position',)),                             (add_section_if_missing, ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n'))],
'fc66ecd0': [(log, ('2.8: Face Texcoord',)),                             (add_section_if_missing, ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n'))],
'df6b6f84': [(log, ('2.8: Face Blend',)),                                (add_section_if_missing, ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n'))],

# Short Dagger VBs
'771b3e9f': [(log, ('2.8: Soldier0 ShortDagger VertexLimit',)),         (add_section_if_missing, ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n'))],
'a7b673bb': [(log, ('2.8: Soldier0 ShortDagger Position',)),            (add_section_if_missing, ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n'))],
'37c582f3': [(log, ('2.8: Soldier0 ShortDagger Texcoord',)),            (add_section_if_missing, ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n'))],
'698ef481': [(log, ('2.8: Soldier0 ShortDagger Blend',)),               (add_section_if_missing, ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n'))],

# Long Dagger VBs
'037b48d9': [(log, ('2.8: Soldier0 LongDagger VertexLimit',)),          (add_section_if_missing, ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n'))],
'6f413f77': [(log, ('2.8: Soldier0 LongDagger Position',)),             (add_section_if_missing, ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n'))],
'e45c71f4': [(log, ('2.8: Soldier0 LongDagger Texcoord',)),             (add_section_if_missing, ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n'))],
'c68ee4ea': [(log, ('2.8: Soldier0 LongDagger Blend',)),                (add_section_if_missing, ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n'))],

# Texture Hashes (v2.8 Target)
'bb979f59': [
        (log,                           ('2.8: Soldier0 HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
    ],
'c85b4097': [
        (log,                           ('2.8: Soldier0 Weapon Diffuse Hash',)),
        (add_section_if_missing,        ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n')),
    ],
'8353de2a': [
        (log,                           ('2.8: Soldier0 Weapon LightMap Hash',)),
        (add_section_if_missing,        ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n')),
    ],
'88fe0e3c': [
        (log,                           ('2.8: Soldier0 Weapon MaterialMap Hash',)),
        (add_section_if_missing,        ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log,                           ('2.8: Soldier0 Shared NormalMap Hash',)),
        (add_section_if_missing,        ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4d5c8ade', 'Soldier0.ShortDagger.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('6df60902', 'Soldier0.LongDagger.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soldier0',
    'game_versions': ['2.8', '3.0'],
}