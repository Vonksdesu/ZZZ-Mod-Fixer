"""
Soldier11 Character Hash Commands
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
    Returns Soldier11's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# ==========================================
# 1. ORIGINAL COMMUNITY CODES (DIPERTAHANKAN)
# ==========================================
'2fa74e2f': [(log, ('2.5: Soldier11 Hair IB Hash',)), (add_ib_check_if_missing,)],
'e3ee72d9': [(log, ('2.5: Soldier11 Body IB Hash',)), (add_ib_check_if_missing,)],
'bb315c43': [(log, ('2.5: Soldier11 Head IB Hash',)), (add_ib_check_if_missing,)],
'3c8697e8': [
        (log,                           ('1.0: Soldier11 HeadA Diffuse 1024p Hash',)),
        (update_hash,                   ('67821d9d',)),
        (add_section_if_missing,        ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n')),
    ],
'67821d9d': [
        (log,                           ('2.5: Soldier11 HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n')),
    ],
'b41b671a': [
        (log,                           ('2.5: Soldier11 HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'15f933dc': [
        (log,                           ('1.0: Soldier11 HairA Diffuse 1024p Hash',)),
        (update_hash,                   ('b41b671a',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'787659b9': [
        (log,                           ('1.0: Soldier11 HairA LightMap 2048p Hash',)),
        (update_hash,                   ('71993491',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'71993491': [
        (log,                           ('2.5: Soldier11 HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'baa3c836': [
        (log,                           ('1.0: Soldier11 HairA LightMap 1024p Hash',)),
        (update_hash,                   ('71993491',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'68d9644a': [
        (log,                           ('1.0: Soldier11 HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: Soldier11 HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'4e08e50b': [
        (log,                           ('1.0: Soldier11 HairA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'1f8bd622': [
        (log,                           ('2.5: Soldier11 HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'640a8c01': [
        (log,                           ('2.5: Soldier11 BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'd7f2269b': [
        (log,                           ('1.0: Soldier11 BodyA Diffuse 1024p Hash',)),
        (update_hash,                   ('640a8c01',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'2f88092e': [
        (log,                           ('1.0: Soldier11 BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('33e8af55',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'33e8af55': [
        (log,                           ('2.5: Soldier11 BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'ce581269': [
        (log,                           ('1.0: Soldier11 BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('33e8af55',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'81db8cbe': [
        (log,                           ('1.0: Soldier11 BodyA MaterialMap 2048p Hash',)),
        (update_hash,                   ('8ab5b59d',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'8ab5b59d': [
        (log,                           ('2.5: Soldier11 BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'874f9f68': [
        (log,                           ('1.0: Soldier11 BodyA MaterialMap 1024p Hash',)),
        (update_hash,                   ('8ab5b59d',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'c94bb3d6': [
        (log,                           ('1.0: Soldier11 BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'eb924a91': [
        (log,                           ('1.0: Soldier11 BodyA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],

# ==========================================
# 2. PEMBARUAN DATABASE 2.8 (SINKRONISASI STRICT)
# ==========================================
# New Index Buffer (IB) Hashes
'0fa08b01': [(log, ('2.8: Soldier11 HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'3a262de5': [(log, ('2.8: Soldier11 Weapon IB Hash',)),     (add_ib_check_if_missing,)],

# Hair VBs
'ba0c408b': [(log, ('2.8: Soldier11 Hair draw_vb',)),                    (add_section_if_missing, ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n'))],
'cf814b3c': [(log, ('2.8: Soldier11 Hair position_vb',)),                (add_section_if_missing, ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n'))],
'a1305cc6': [(log, ('2.8: Soldier11 Hair texcoord_vb',)),                (add_section_if_missing, ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n'))],
'67fe929d': [(log, ('2.8: Soldier11 Hair blend_vb',)),                   (add_section_if_missing, ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n'))],

# Hair Shadow VBs
'7c366c06': [(log, ('2.8: Soldier11 HairShadow draw_vb',)),              (add_section_if_missing, ('0fa08b01', 'Soldier11.HairShadow.IB', 'match_priority = 0\n'))],
'ede368aa': [(log, ('2.8: Soldier11 HairShadow position_vb',)),          (add_section_if_missing, ('0fa08b01', 'Soldier11.HairShadow.IB', 'match_priority = 0\n'))],
'93054dd8': [(log, ('2.8: Soldier11 HairShadow texcoord_vb',)),          (add_section_if_missing, ('0fa08b01', 'Soldier11.HairShadow.IB', 'match_priority = 0\n'))],
'b117ad1a': [(log, ('2.8: Soldier11 HairShadow blend_vb',)),             (add_section_if_missing, ('0fa08b01', 'Soldier11.HairShadow.IB', 'match_priority = 0\n'))],

# Body VBs
'59b61855': [(log, ('2.8: Soldier11 Body draw_vb',)),                    (add_section_if_missing, ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n'))],
'003ff258': [(log, ('2.8: Soldier11 Body position_vb',)),                (add_section_if_missing, ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n'))],
'29cd94d6': [(log, ('2.8: Soldier11 Body texcoord_vb',)),                (add_section_if_missing, ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n'))],
'2cb26d03': [(log, ('2.8: Soldier11 Body blend_vb',)),                   (add_section_if_missing, ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n'))],

# Face VBs
'dc49f140': [(log, ('2.8: Soldier11 Face draw_vb',)),                    (add_section_if_missing, ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n'))],
'e65b6207': [(log, ('2.8: Soldier11 Face position_vb',)),                (add_section_if_missing, ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n'))],
'39de00d5': [(log, ('2.8: Soldier11 Face texcoord_vb',)),                (add_section_if_missing, ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n'))],
'3ac13527': [(log, ('2.8: Soldier11 Face blend_vb',)),                   (add_section_if_missing, ('bb315c43', 'Soldier11.Head.IB', 'match_priority = 0\n'))],

# Weapon VBs & Limits
'8524602e': [(log, ('2.8: Soldier11 Weapon VertexLimit',)),              (add_section_if_missing, ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n'))],
'2a474e15': [(log, ('2.8: Soldier11 Weapon Position',)),                 (add_section_if_missing, ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n'))],
'84a49156': [(log, ('2.8: Soldier11 Weapon Texcoord',)),                 (add_section_if_missing, ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n'))],
'd623cbf7': [(log, ('2.8: Soldier11 Weapon Blend',)),                    (add_section_if_missing, ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n'))],

# Texture Hashes (v2.8)
'17e75c76': [
        (log,                           ('2.8: Soldier11 Hair LightMap Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log,                           ('2.8: Soldier11 Shared NormalMap Hash',)),
        (add_section_if_missing,        ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
'744e39e9': [
        (log,                           ('2.8: Soldier11 Body LightMap Hash',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'9d09159b': [
        (log,                           ('2.8: Soldier11 Body MaterialMap Hash',)),
        (add_section_if_missing,        ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
    ],
'ac0b0749': [
        (log,                           ('2.8: Soldier11 Weapon Diffuse Hash [Legacy]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
'116bde23': [
        (log,                           ('2.8: Soldier11 Weapon LightMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
'08ff5178': [
        (log,                           ('2.8: Soldier11 Weapon MaterialMap Hash [Legacy]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],

# === New Database 2.8 Synced Weapon Texture Hashes ===
'735b23b2': [
        (log,                           ('2.8: Soldier11 Weapon Diffuse 2048p Hash [New]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
'81fe09dc': [
        (log,                           ('2.8: Soldier11 Weapon LightMap 2048p Hash [New]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
'e2af379d': [
        (log,                           ('2.8: Soldier11 Weapon MaterialMap 2048p Hash [New]',)),
        (add_section_if_missing,        ('3a262de5', 'Soldier11.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soldier11',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.8', '3.0'],
}