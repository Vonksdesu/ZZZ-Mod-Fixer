"""
Nicole Character Hash Commands
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
    Returns Nicole's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '6847bbbd': [
            (log,                             ('1.0 -> 3.0: Nicole Hair IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('7dcfe907',)),
        ],
        '7dcfe907': [
            (log,                             ('3.0 - 3.2: Nicole Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f6344432': [
            (log,                             ('2.2 - 2.8: Nicole Hair Draw VB Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d9b8d61a',)),
        ],
        '199853eb': [
            (log,                             ('2.2 - 2.8: Nicole Hair Position VB Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('6f931ca7',)),
        ],
        '06e4fd79': [
            (log,                             ('2.2 - 2.8: Nicole Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e04f4893',)),
        ],
        '347e4a48': [
            (log,                             ('2.2 - 2.8: Nicole Hair Blend VB Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('8171f5c9',)),
        ],
        'd9b8d61a': [
            (log,                             ('3.0 - 3.2: Nicole Hair Draw VB Hash',)),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        '6f931ca7': [
            (log,                             ('3.0 - 3.2: Nicole Hair Position VB Hash',)),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        'e04f4893': [
            (log,                             ('3.0 - 3.2: Nicole Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        '8171f5c9': [
            (log,                             ('3.0 - 3.2: Nicole Hair Blend VB Hash',)),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        '6d3868f9': [
            (log,                             ('2.2 - 3.2: Nicole HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7a45adcd', 'Nicole.HairA.Diffuse.1024')),
        ],
        '7a45adcd': [
            (log,                             ('2.2 - 3.2: Nicole HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d3868f9', 'Nicole.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Nicole HairA, BodyA, AmillionA, weaponA and weaponB NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Nicole.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Nicole.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Nicole.AmillionA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Nicole.weaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Nicole.weaponB.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Nicole HairA, BodyA, AmillionA, weaponA and weaponB NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Nicole.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Nicole.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Nicole.AmillionA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Nicole.weaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Nicole.weaponB.NormalMap.2048')),
        ],
        'bffb4a66': [
            (log,                             ('1.0-1.7: Nicole HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'b8db0209': [
            (log,                             ('1.0-1.7: Nicole HairA NormalMap 1024p Hash (Removed in 2.5)',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        '1dfd9e16': [
            (log,                             ('1.0-1.7: Nicole HairA LightMap 2048p Hash',)),
            (update_hash,                     ('8c9c25d5',)),
        ],
        '9adc04ed': [
            (log,                             ('1.0-1.7: Nicole HairA LightMap 1024p Hash (Removed in 2.5)',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],
        '8c9c25d5': [
            (log,                             ('2.2 - 3.2: Nicole HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f3c21e41', '9adc04ed'), 'Nicole.HairA.LightMap.1024')),
        ],
        'f3c21e41': [
            (log,                             ('2.2 - 3.2: Nicole HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7dcfe907', 'Nicole.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8c9c25d5', '1dfd9e16'), 'Nicole.HairA.LightMap.2048')),
        ],
        'a05c2386': [
            (log,                             ('2.5: Nicole HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6847bbbd', 'Nicole.Hair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair Shadow Component ====================
        '4ed9a81f': [
            (log,                             ('2.2 - 3.2: Nicole Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4d61e6f3': [
            (log,                             ('2.2 - 3.2: Nicole Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b408b261': [
            (log,                             ('2.2 - 3.2: Nicole Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '322345a6': [
            (log,                             ('2.2 - 2.8: Nicole Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e6b9e50e',)),
        ],
        'e6b9e50e': [
            (log,                             ('3.0 - 3.2: Nicole Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ab4b28ad': [
            (log,                             ('2.2 - 3.2: Nicole Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'Nicole.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no texture hashes in the database.

        # ==================== Body Component ====================
        '5a4c1ef3': [
            (log,                             ('1.0 -> 3.0: Nicole Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('e53364dd',)),
        ],
        'e53364dd': [
            (log,                             ('3.0 - 3.2: Nicole Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8cc1262b': [
            (log,                             ('2.2 - 2.8: Nicole Body Draw VB Hash',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b19da99e',)),
        ],
        '89df5a07': [
            (log,                             ('2.2 - 2.8: Nicole Body Position VB Hash',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('4af0a4cd',)),
        ],
        '91c1b779': [
            (log,                             ('2.2 - 2.8: Nicole Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ed4c47a9',)),
        ],
        '7ecda89f': [
            (log,                             ('2.2 - 2.8: Nicole Body Blend VB Hash',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b793c804',)),
        ],
        'b19da99e': [
            (log,                             ('3.0 - 3.2: Nicole Body Draw VB Hash',)),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
        ],
        '4af0a4cd': [
            (log,                             ('3.0 - 3.2: Nicole Body Position VB Hash',)),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
        ],
        'ed4c47a9': [
            (log,                             ('3.0 - 3.2: Nicole Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
        ],
        'b793c804': [
            (log,                             ('3.0 - 3.2: Nicole Body Blend VB Hash',)),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
        ],
        'f86ffe2c': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ee9b402', 'Nicole.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9ee9b402', 'Nicole.AmillionA.Diffuse.1024')),
        ],
        '9ee9b402': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f86ffe2c', 'Nicole.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f86ffe2c', 'Nicole.AmillionA.Diffuse.2048')),
        ],
        '8cf23419': [
            (log,                             ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '580df52d': [
            (log,                             ('1.0-1.7: Nicole BodyA, BangbooA NormalMap 1024p Hash (Removed in 2.5)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
        ],
        '80855e0f': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2b5aa784', 'Nicole.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('2b5aa784', 'Nicole.AmillionA.LightMap.1024')),
        ],
        '2b5aa784': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('80855e0f', 'Nicole.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('80855e0f', 'Nicole.AmillionA.LightMap.2048')),
        ],
        '95cabef3': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb33129d', 'Nicole.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('bb33129d', 'Nicole.AmillionA.MaterialMap.1024')),
        ],
        'bb33129d': [
            (log,                             ('2.2 - 3.2: Nicole BodyA and AmillionA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5a4c1ef3', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e53364dd', 'Nicole.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95cabef3', 'Nicole.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95cabef3', 'Nicole.AmillionA.MaterialMap.2048')),
        ],
        # Body shares its Diffuse, LightMap and MaterialMap hashes with Amillion, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Amillion Component ====================
        '40e64ae2': [
            (log,                             ('2.2 - 3.2: Nicole Amillion IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bb7fffe9': [
            (log,                             ('2.2 - 3.2: Nicole Amillion Draw VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
        ],
        '176bf3d7': [
            (log,                             ('2.2 - 3.2: Nicole Amillion Position VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
        ],
        '077c3500': [
            (log,                             ('2.2 - 2.8: Nicole Amillion Texcoord VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f9f810ed',)),
        ],
        'f9f810ed': [
            (log,                             ('3.0 - 3.2: Nicole Amillion Texcoord VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
        ],
        '4e1d9c9a': [
            (log,                             ('2.2 - 3.2: Nicole Amillion Blend VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'Nicole.Amillion.IB', 'match_priority = 0\n')),
        ],
        # Amillion shares its Diffuse, LightMap and MaterialMap hashes with Body, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Face Component ====================
        '7435fc0e': [
            (log,                             ('1.0 -> 3.0: Nicole Face IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('93b02078',)),
        ],
        '93b02078': [
            (log,                             ('3.0 - 3.2: Nicole Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9274e401': [
            (log,                             ('2.2 - 2.8: Nicole Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('967c2f1c',)),
        ],
        '5714e5e6': [
            (log,                             ('2.2 - 2.8: Nicole Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d5958556',)),
        ],
        'b25ebcf6': [
            (log,                             ('2.2 - 2.8: Nicole Face Blend VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('292d1b1f',)),
        ],
        '967c2f1c': [
            (log,                             ('3.0 - 3.2: Nicole Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
        ],
        'd5958556': [
            (log,                             ('3.0 - 3.1: Nicole Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('31df6120',)),
        ],
        '31df6120': [
            (log,                             ('3.2: Nicole Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '292d1b1f': [
            (log,                             ('3.0 - 3.2: Nicole Face Blend VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
        ],
        'd1e84a34': [
            (log,                             ('2.2 - 3.2: Nicole FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6abd3dd3', 'Nicole.FaceA.Diffuse.1024')),
        ],
        '6abd3dd3': [
            (log,                             ('2.2 - 3.2: Nicole FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'Nicole.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1e84a34', 'Nicole.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        'f9befc51': [
            (log,                             ('2.2 - 3.2: Nicole weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f6325378': [
            (log,                             ('2.2 - 3.2: Nicole weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
        ],
        '00c8b3c5': [
            (log,                             ('2.2 - 3.2: Nicole weapon Position VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
        ],
        '14b0d6b6': [
            (log,                             ('2.2 - 3.2: Nicole weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
        ],
        '2f427bdb': [
            (log,                             ('2.2 - 3.2: Nicole weapon Blend VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
        ],
        'a365836f': [
            (log,                             ('2.2 - 3.2: Nicole weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('35951ccf', 'Nicole.weaponA.Diffuse.1024')),
        ],
        '35951ccf': [
            (log,                             ('2.2 - 3.2: Nicole weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a365836f', 'Nicole.weaponA.Diffuse.2048')),
        ],
        '76e8ac35': [
            (log,                             ('2.2 - 3.2: Nicole weaponB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1af36a8', 'Nicole.weaponB.Diffuse.1024')),
        ],
        'f1af36a8': [
            (log,                             ('2.2 - 3.2: Nicole weaponB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76e8ac35', 'Nicole.weaponB.Diffuse.2048')),
        ],
        'fda56c66': [
            (log,                             ('2.2 - 3.2: Nicole weaponA and weaponB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d5ee825', 'Nicole.weaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('6d5ee825', 'Nicole.weaponB.LightMap.1024')),
        ],
        '6d5ee825': [
            (log,                             ('2.2 - 3.2: Nicole weaponA and weaponB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fda56c66', 'Nicole.weaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('fda56c66', 'Nicole.weaponB.LightMap.2048')),
        ],
        'ad4bf30d': [
            (log,                             ('2.2 - 3.2: Nicole weaponA and weaponB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0fe671cc', 'Nicole.weaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('0fe671cc', 'Nicole.weaponB.MaterialMap.1024')),
        ],
        '0fe671cc': [
            (log,                             ('2.2 - 3.2: Nicole weaponA and weaponB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f9befc51', 'Nicole.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ad4bf30d', 'Nicole.weaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('ad4bf30d', 'Nicole.weaponB.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Nicole',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
