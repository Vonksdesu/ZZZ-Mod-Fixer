"""
Caesar Character Hash Commands
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
    Returns Caesar's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'7a8fa826': [(log, ('1.2: Caesar Hair IB Hash',)), (add_ib_check_if_missing,)],
'92061e5e': [(log, ('1.2: Caesar Body IB Hash',)), (add_ib_check_if_missing,)],
'6caaeb53': [(log, ('1.2: Caesar Head IB Hash',)), (add_ib_check_if_missing,)],

# === Position VB Hashes ===
'6de24342': [(log, ('2.5: Caesar Hair Position Hash',))],
'7b6d4dab': [(log, ('2.5: Caesar Body Position Hash',))],

# === Blend VB Hashes ===
'c2417533': [(log, ('2.5: Caesar Hair Blend Hash',))],
'8a3da083': [(log, ('2.5: Caesar Body Blend Hash',))],

# === Texcoord VB Hashes ===
'af291513': [
        (log,            ('1.2 -> 1.3: Caesar Hair Texcoord Hash',)),
        (update_hash,    ('72537fa3',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_Caesar_hair',
            ('4B','2e','2f','2e'),
            ('4B','2f','2f','2f')
        )),
    ],
'72537fa3': [(log, ('1.3 -> 2.5: Caesar Hair Texcoord Hash',))],

'3b2a70a5': [
        (log,            ('1.2 -> 1.3: Caesar Body Texcoord Hash',)),
        (update_hash,    ('0ca81129',)),
        (log,            ('+ Remapping texcoord buffer',)),
        (zzz_13_remap_texcoord, (
            '13_Caesar_body',
            ('4B','2e','2f','2e', '2e'),
            ('4B','2f','2f','2f', '2f')
        )),
    ],
'0ca81129': [(log, ('1.3 -> 2.5: Caesar Body Texcoord Hash',))],

# === Face Textures ===
'84d53514': [
        (log,                           ('1.2 -> 2.5: Caesar FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6caaeb53', 'Caesar.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('13098244', 'Caesar.FaceA.Diffuse.2048')),
    ],
'13098244': [
        (log,                           ('1.2 -> 2.5: Caesar FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6caaeb53', 'Caesar.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('84d53514', 'Caesar.FaceA.Diffuse.1024')),
    ],

# === Hair Textures ===
'9ce3e80c': [
        (log,                           ('1.2 -> 2.5: Caesar HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b004ab49', 'Caesar.HairA.Diffuse.1024')),
    ],
'b004ab49': [
        (log,                           ('1.2 -> 2.5: Caesar HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9ce3e80c', 'Caesar.HairA.Diffuse.2048')),
    ],

'bf19954f': [(log, ('1.2 -> 2.5: Caesar HairA LightMap 2048p Hash',)), (update_hash, ('d5d3585b',)),],
'd5d3585b': [
        (log,                           ('2.5: Caesar HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c7115c4b', 'Caesar.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('89b2d3b3', 'c7115c4b'), 'Caesar.HairA.LightMap.1024')),
    ],

'89b2d3b3': [
        (log,                           ('2.5: Caesar HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c7115c4b', 'Caesar.HairA.LightMap.1024')),
        (multiply_section_if_missing,        (('d5d3585b', 'bf19954f'), 'Caesar.HairA.LightMap.2048')),
    ],
'c7115c4b': [
        (log,                           ('1.2 -> 2.5: Caesar HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('d5d3585b', 'bf19954f'), 'Caesar.HairA.LightMap.2048')),
    ],

'350b827e': [
        (log,                           ('1.2 -> 2.5: Caesar HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2204f89a', 'Caesar.HairA.MaterialMap.1024')),
    ],
'2204f89a': [
        (log,                           ('1.2 -> 2.5: Caesar HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('350b827e', 'Caesar.HairA.MaterialMap.2048')),
    ],

'10af3807': [(log, ('1.2 -> 2.5: Caesar HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'ebac056e': [
        (log,                           ('2.5: Caesar Hair/Body NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e17b3529', 'Caesar.HairA.NormalMap.1024')),
    ],
'e17b3529': [
        (log,                           ('1.2 -> 2.5: Caesar HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '10af3807'), 'Caesar.HairA.NormalMap.2048')),
    ],

# === Body Textures ===
'5e2cea1a': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f4b78da0', 'Caesar.BodyA.Diffuse.1024')),
    ],
'f4b78da0': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5e2cea1a', 'Caesar.BodyA.Diffuse.2048')),
    ],

'6296d481': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a9e24ba0', 'Caesar.BodyA.LightMap.1024')),
    ],
'a9e24ba0': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('6296d481', 'Caesar.BodyA.LightMap.2048')),
    ],

'd5d89d5b': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('328bc108', 'Caesar.BodyA.MaterialMap.1024')),
    ],
'328bc108': [
        (log,                           ('1.2 -> 2.5: Caesar BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d5d89d5b', 'Caesar.BodyA.MaterialMap.2048')),
    ],

'c1f1e12f': [(log, ('1.3 -> 2.5: Caesar BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'f1c6c309': [(log, ('1.4B -> 2.5: Caesar BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'36f39b49': [(log, ('1.4 -> 2.5: Caesar BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],

'8cdf95d0': [(log, ('1.3 -> 1.4: Caesar BodyA NormalMap 1024p Hash',)), (update_hash, ('a8abff9d',)),],
'a8abff9d': [
        (log,                           ('1.4 -> 2.5: Caesar BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('ebac056e', '36f39b49', 'f1c6c309', 'c1f1e12f'), 'Caesar.BodyA.NormalMap.2048')),
    ],
'f5b1c16e': [(log, ('3.0: Caesar Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'394dedc6': [
        (log, ('3.0: Caesar Hair Shadow VB Hash',)),
        (add_section_if_missing, ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'51c22365': [
        (log, ('3.0: Caesar Hair Shadow VB Hash',)),
        (add_section_if_missing, ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'25c45f17': [
        (log, ('3.0: Caesar Hair Shadow VB Hash',)),
        (add_section_if_missing, ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'6736df70': [
        (log, ('3.0: Caesar Hair Shadow VB Hash',)),
        (add_section_if_missing, ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'622b5a8d': [
        (log, ('3.0: Caesar Body VB Hash',)),
        (add_section_if_missing, ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
    ],
'57c63788': [(log, ('3.0: Caesar weapon IB Hash',)), (add_ib_check_if_missing,)],
'a00fcc14': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'5e0cdd97': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'be9d7d53': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'a9d32076': [(log, ('3.0: Caesar weapon IB Hash',)), (add_ib_check_if_missing,)],
'4a11c39b': [
        (log, ('3.0: Caesar Face VB Hash',)),
        (add_section_if_missing, ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
    ],
'845ee2b0': [
        (log, ('3.0: Caesar Face VB Hash',)),
        (add_section_if_missing, ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
    ],
'5af59912': [
        (log, ('3.0: Caesar Face VB Hash',)),
        (add_section_if_missing, ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
    ],
'3d6da969': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'e4d38c28': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'b0fd2b2e': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('a9d32076', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'4b76e29f': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('a9d32076', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'700350dc': [(log, ('3.0: Caesar misc hash',)),],
'b8d3109f': [(log, ('3.0: Caesar misc hash',)),],
'dc1c0ec2': [(log, ('3.0: Caesar misc hash',)),],
'bb723235': [
        (log, ('3.0: Caesar Hair VB Hash',)),
        (add_section_if_missing, ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Caesar Hair TEX Hash',)),
        (add_section_if_missing, ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
    ],
'1ead4a3e': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'973bc57d': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'f8dfb686': [
        (log, ('3.0: Caesar weapon TEX Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'3c1f14b7': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('a9d32076', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
'189abd09': [
        (log, ('3.0: Caesar weapon VB Hash',)),
        (add_section_if_missing, ('57c63788', 'Caesar.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Caesar',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
