"""
Caesar Character Hash Commands
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
    Returns Caesar's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '7a8fa826': [
            (log,                             ('2.2 - 3.2: Caesar Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bb723235': [
            (log,                             ('2.2 - 3.2: Caesar Hair Draw VB Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        '6de24342': [
            (log,                             ('2.2 - 3.2: Caesar Hair Position VB Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        'af291513': [
            (log,                             ('1.2 -> 1.3: Caesar Hair Texcoord Hash',)),
            (update_hash,                     ('72537fa3',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_13_remap_texcoord,           (
                '13_Caesar_hair',
                ('4B','2e','2f','2e'),
                ('4B','2f','2f','2f')
            )),
        ],
        '72537fa3': [
            (log,                             ('2.2 - 3.2: Caesar Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        'c2417533': [
            (log,                             ('2.2 - 3.2: Caesar Hair Blend VB Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        '9ce3e80c': [
            (log,                             ('2.2 - 3.2: Caesar HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b004ab49', 'Caesar.HairA.Diffuse.1024')),
        ],
        'b004ab49': [
            (log,                             ('2.2 - 3.2: Caesar HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ce3e80c', 'Caesar.HairA.Diffuse.2048')),
        ],
        '10af3807': [
            (log,                             ('1.2 -> 2.5: Caesar HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Caesar HairA, BodyA, weapon - 盾 and weapon - 剑 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', 'e17b3529'), 'Caesar.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', 'a8abff9d'), 'Caesar.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Caesar.weapon - 盾.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Caesar.weapon - 剑.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Caesar HairA, BodyA, weapon - 盾 and weapon - 剑 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '10af3807'), 'Caesar.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '36f39b49', 'f1c6c309', 'c1f1e12f'), 'Caesar.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Caesar.weapon - 盾.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Caesar.weapon - 剑.NormalMap.2048')),
        ],
        'e17b3529': [
            (log,                             ('1.2 -> 2.5: Caesar HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        'bf19954f': [
            (log,                             ('1.2 -> 2.5: Caesar HairA LightMap 2048p Hash',)),
            (update_hash,                     ('d5d3585b',)),
        ],
        'd5d3585b': [
            (log,                             ('2.2 - 3.2: Caesar HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('89b2d3b3', 'c7115c4b'), 'Caesar.HairA.LightMap.1024')),
        ],
        '89b2d3b3': [
            (log,                             ('2.2 - 3.2: Caesar HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d5d3585b', 'bf19954f'), 'Caesar.HairA.LightMap.2048')),
        ],
        'c7115c4b': [
            (log,                             ('1.2 -> 2.5: Caesar HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
        ],
        '350b827e': [
            (log,                             ('2.2 - 3.2: Caesar HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2204f89a', 'Caesar.HairA.MaterialMap.1024')),
        ],
        '2204f89a': [
            (log,                             ('2.2 - 3.2: Caesar HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7a8fa826', 'Caesar.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('350b827e', 'Caesar.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'f5b1c16e': [
            (log,                             ('2.2 - 3.2: Caesar Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '394dedc6': [
            (log,                             ('2.2 - 3.2: Caesar Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '51c22365': [
            (log,                             ('2.2 - 3.2: Caesar Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '25c45f17': [
            (log,                             ('2.2 - 3.2: Caesar Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '6736df70': [
            (log,                             ('2.2 - 3.2: Caesar Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('f5b1c16e', 'Caesar.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '92061e5e': [
            (log,                             ('2.2 - 3.2: Caesar Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '622b5a8d': [
            (log,                             ('2.2 - 3.2: Caesar Body Draw VB Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        ],
        '7b6d4dab': [
            (log,                             ('2.2 - 3.2: Caesar Body Position VB Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        ],
        '3b2a70a5': [
            (log,                             ('1.2 -> 1.3: Caesar Body Texcoord Hash',)),
            (update_hash,                     ('0ca81129',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_13_remap_texcoord,           (
                '13_Caesar_body',
                ('4B','2e','2f','2e', '2e'),
                ('4B','2f','2f','2f', '2f')
            )),
        ],
        '0ca81129': [
            (log,                             ('2.2 - 3.2: Caesar Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        ],
        '8a3da083': [
            (log,                             ('2.2 - 3.2: Caesar Body Blend VB Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        ],
        '5e2cea1a': [
            (log,                             ('2.2 - 3.2: Caesar BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f4b78da0', 'Caesar.BodyA.Diffuse.1024')),
        ],
        'f4b78da0': [
            (log,                             ('2.2 - 3.2: Caesar BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e2cea1a', 'Caesar.BodyA.Diffuse.2048')),
        ],
        'c1f1e12f': [
            (log,                             ('1.3 -> 2.5: Caesar BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'f1c6c309': [
            (log,                             ('1.4B -> 2.5: Caesar BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '36f39b49': [
            (log,                             ('1.4 -> 2.5: Caesar BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '8cdf95d0': [
            (log,                             ('1.3 -> 1.4: Caesar BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('a8abff9d',)),
        ],
        'a8abff9d': [
            (log,                             ('1.4 -> 2.5: Caesar BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
        ],
        '6296d481': [
            (log,                             ('2.2 - 3.2: Caesar BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9e24ba0', 'Caesar.BodyA.LightMap.1024')),
        ],
        'a9e24ba0': [
            (log,                             ('2.2 - 3.2: Caesar BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6296d481', 'Caesar.BodyA.LightMap.2048')),
        ],
        'd5d89d5b': [
            (log,                             ('2.2 - 3.2: Caesar BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('328bc108', 'Caesar.BodyA.MaterialMap.1024')),
        ],
        '328bc108': [
            (log,                             ('2.2 - 3.2: Caesar BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('92061e5e', 'Caesar.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5d89d5b', 'Caesar.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '6caaeb53': [
            (log,                             ('2.2 - 3.2: Caesar Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '700350dc': [
            (log,                             ('2.2 - 3.2: Caesar Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
        ],
        '4a11c39b': [
            (log,                             ('2.2 - 3.1: Caesar Face Position VB Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
        ],
        '845ee2b0': [
            (log,                             ('2.2 - 3.1: Caesar Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
        ],
        '5af59912': [
            (log,                             ('2.2 - 3.1: Caesar Face Blend VB Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
        ],
        '13098244': [
            (log,                             ('2.2 - 3.2: Caesar FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84d53514', 'Caesar.FaceA.Diffuse.1024')),
        ],
        '84d53514': [
            (log,                             ('2.2 - 3.2: Caesar FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6caaeb53', 'Caesar.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('13098244', 'Caesar.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 盾 Component ====================
        '57c63788': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b8d3109f': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        '189abd09': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 盾 Position VB Hash',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        '3d6da969': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 盾 Texcoord VB Hash',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        'e4d38c28': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 盾 Blend VB Hash',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        'a00fcc14': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ead4a3e', 'Caesar.weapon - 盾.Diffuse.1024')),
            (multiply_section_if_missing,     ('1ead4a3e', 'Caesar.weapon - 剑.Diffuse.1024')),
        ],
        '1ead4a3e': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a00fcc14', 'Caesar.weapon - 盾.Diffuse.2048')),
            (multiply_section_if_missing,     ('a00fcc14', 'Caesar.weapon - 剑.Diffuse.2048')),
        ],
        '5e0cdd97': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('973bc57d', 'Caesar.weapon - 盾.LightMap.1024')),
            (multiply_section_if_missing,     ('973bc57d', 'Caesar.weapon - 剑.LightMap.1024')),
        ],
        '973bc57d': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e0cdd97', 'Caesar.weapon - 盾.LightMap.2048')),
            (multiply_section_if_missing,     ('5e0cdd97', 'Caesar.weapon - 剑.LightMap.2048')),
        ],
        'be9d7d53': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f8dfb686', 'Caesar.weapon - 盾.MaterialMap.1024')),
            (multiply_section_if_missing,     ('f8dfb686', 'Caesar.weapon - 剑.MaterialMap.1024')),
        ],
        'f8dfb686': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 盾 and weapon - 剑 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('57c63788', 'Caesar.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be9d7d53', 'Caesar.weapon - 盾.MaterialMap.2048')),
            (multiply_section_if_missing,     ('be9d7d53', 'Caesar.weapon - 剑.MaterialMap.2048')),
        ],

        # ==================== Weapon - 剑 Component ====================
        'a9d32076': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 剑 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dc1c0ec2': [
            (log,                             ('2.2 - 3.2: Caesar weapon - 剑 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
        ],
        '3c1f14b7': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 剑 Position VB Hash',)),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
        ],
        'b0fd2b2e': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 剑 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
        ],
        '4b76e29f': [
            (log,                             ('2.2 - 3.1: Caesar weapon - 剑 Blend VB Hash',)),
            (add_section_if_missing,          ('a9d32076', 'Caesar.weapon - 剑.IB', 'match_priority = 0\n')),
        ],
        # Weapon - 剑 shares all texture hashes with Weapon - 盾; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Caesar',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
