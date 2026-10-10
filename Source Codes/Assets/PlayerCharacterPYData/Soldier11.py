"""
Soldier11 Character Hash Commands
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
    Returns Soldier11's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '2fa74e2f': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ba0c408b': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Draw VB Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        ],
        'cf814b3c': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Position VB Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        ],
        'a1305cc6': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        ],
        '67fe929d': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Blend VB Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        ],
        'b41b671a': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('15f933dc', 'Soldier11.HairA.Diffuse.1024')),
        ],
        '15f933dc': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b41b671a', 'Soldier11.HairA.Diffuse.2048')),
        ],
        '68d9644a': [
            (log,                             ('1.0: Soldier11 HairA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '4e08e50b': [
            (log,                             ('1.0: Soldier11 HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA, BodyA and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier11.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier11.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier11.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA, BodyA and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier11.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier11.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier11.weaponA.NormalMap.2048')),
        ],
        '787659b9': [
            (log,                             ('1.0: Soldier11 HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('71993491',)),
        ],
        'baa3c836': [
            (log,                             ('1.0: Soldier11 HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('71993491',)),
        ],
        '71993491': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('17e75c76', 'Soldier11.HairA.LightMap.1024')),
        ],
        '17e75c76': [
            (log,                             ('2.2 - 3.2: Soldier11 HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('71993491', 'Soldier11.HairA.LightMap.2048')),
        ],
        '1f8bd622': [
            (log,                             ('2.5: Soldier11 HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2fa74e2f', 'Soldier11.Hair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair Shadow Component ====================
        '0fa08b01': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7c366c06': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('0fa08b01', 'Soldier11.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ede368aa': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('0fa08b01', 'Soldier11.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '93054dd8': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('0fa08b01', 'Soldier11.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b117ad1a': [
            (log,                             ('2.2 - 3.2: Soldier11 Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('0fa08b01', 'Soldier11.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'e3ee72d9': [
            (log,                             ('2.2 - 3.2: Soldier11 Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '59b61855': [
            (log,                             ('2.2 - 3.2: Soldier11 Body Draw VB Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
        ],
        '003ff258': [
            (log,                             ('2.2 - 3.2: Soldier11 Body Position VB Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
        ],
        '29cd94d6': [
            (log,                             ('2.2 - 3.2: Soldier11 Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
        ],
        '2cb26d03': [
            (log,                             ('2.2 - 3.2: Soldier11 Body Blend VB Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
        ],
        '640a8c01': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d7f2269b', 'Soldier11.BodyA.Diffuse.1024')),
        ],
        'd7f2269b': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('640a8c01', 'Soldier11.BodyA.Diffuse.2048')),
        ],
        'c94bb3d6': [
            (log,                             ('1.0: Soldier11 BodyA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        'eb924a91': [
            (log,                             ('1.0: Soldier11 BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '2f88092e': [
            (log,                             ('1.0: Soldier11 BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('33e8af55',)),
        ],
        'ce581269': [
            (log,                             ('1.0: Soldier11 BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('33e8af55',)),
        ],
        '33e8af55': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('744e39e9', 'Soldier11.BodyA.LightMap.1024')),
        ],
        '744e39e9': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33e8af55', 'Soldier11.BodyA.LightMap.2048')),
        ],
        '81db8cbe': [
            (log,                             ('1.0: Soldier11 BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('8ab5b59d',)),
        ],
        '874f9f68': [
            (log,                             ('1.0: Soldier11 BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('8ab5b59d',)),
        ],
        '8ab5b59d': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9d09159b', 'Soldier11.BodyA.MaterialMap.1024')),
        ],
        '9d09159b': [
            (log,                             ('2.2 - 3.2: Soldier11 BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('e3ee72d9', 'Soldier11.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8ab5b59d', 'Soldier11.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'bb315c43': [
            (log,                             ('2.2 - 3.2: Soldier11 Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dc49f140': [
            (log,                             ('2.2 - 3.2: Soldier11 Face Draw VB Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
        ],
        'e65b6207': [
            (log,                             ('2.2 - 3.2: Soldier11 Face Position VB Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
        ],
        '39de00d5': [
            (log,                             ('2.2 - 3.1: Soldier11 Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f30b174b',)),
        ],
        'f30b174b': [
            (log,                             ('3.2: Soldier11 Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3ac13527': [
            (log,                             ('2.2 - 3.2: Soldier11 Face Blend VB Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
        ],
        '67821d9d': [
            (log,                             ('2.2 - 3.2: Soldier11 FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3c8697e8', 'Soldier11.FaceA.Diffuse.1024')),
        ],
        '3c8697e8': [
            (log,                             ('2.2 - 3.2: Soldier11 FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('bb315c43', 'Soldier11.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('67821d9d', 'Soldier11.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        '3a262de5': [
            (log,                             ('2.2 - 3.2: Soldier11 weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8524602e': [
            (log,                             ('2.2 - 3.2: Soldier11 weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
        ],
        '2a474e15': [
            (log,                             ('2.2 - 3.2: Soldier11 weapon Position VB Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
        ],
        '84a49156': [
            (log,                             ('2.2 - 3.2: Soldier11 weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
        ],
        'd623cbf7': [
            (log,                             ('2.2 - 3.2: Soldier11 weapon Blend VB Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
        ],
        '735b23b2': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac0b0749', 'Soldier11.weaponA.Diffuse.1024')),
        ],
        'ac0b0749': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('735b23b2', 'Soldier11.weaponA.Diffuse.2048')),
        ],
        '81fe09dc': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('116bde23', 'Soldier11.weaponA.LightMap.1024')),
        ],
        '116bde23': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81fe09dc', 'Soldier11.weaponA.LightMap.2048')),
        ],
        'e2af379d': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08ff5178', 'Soldier11.weaponA.MaterialMap.1024')),
        ],
        '08ff5178': [
            (log,                             ('2.2 - 3.2: Soldier11 weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3a262de5', 'Soldier11.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e2af379d', 'Soldier11.weaponA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soldier11',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
