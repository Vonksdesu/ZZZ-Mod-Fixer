"""
NicoleCutie Character Hash Commands
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
    Returns NicoleCutie's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '776f5703': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bafa609a': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Draw VB Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        ],
        '7b4b4f06': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Position VB Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        ],
        'a09489fa': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        ],
        '0df63fc6': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Blend VB Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        ],
        'cdaa9ab5': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e55f39d', 'NicoleCutie.HairA.Diffuse.1024')),
        ],
        '0e55f39d': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdaa9ab5', 'NicoleCutie.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA, BodyA, AmillionA, weaponA, weaponB and mobile phoneA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.AmillionA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.weaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.weaponB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'NicoleCutie.mobile phoneA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA, BodyA, AmillionA, weaponA, weaponB and mobile phoneA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.AmillionA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.weaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.weaponB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'NicoleCutie.mobile phoneA.NormalMap.2048')),
        ],
        '4c8b0bce': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b3ef7388', 'NicoleCutie.HairA.LightMap.1024')),
        ],
        'b3ef7388': [
            (log,                             ('2.2 - 3.2: NicoleCutie HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4c8b0bce', 'NicoleCutie.HairA.LightMap.2048')),
        ],
        'a05c2386': [
            (log,                             ('2.5: NicoleCutie HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('776f5703', 'NicoleCutie.Hair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair Shadow Component ====================
        '4ed9a81f': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4d61e6f3': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b408b261': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '879a6522': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '720296ff': [
            (log,                             ('2.2 - 3.2: NicoleCutie Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('4ed9a81f', 'NicoleCutie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no texture hashes in the database.

        # ==================== Body Component ====================
        '52842f31': [
            (log,                             ('2.2 - 3.2: NicoleCutie Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4151c6c6': [
            (log,                             ('2.2 - 3.2: NicoleCutie Body Draw VB Hash',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        ],
        'dfab3761': [
            (log,                             ('2.2 - 3.2: NicoleCutie Body Position VB Hash',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        ],
        'fa58977c': [
            (log,                             ('2.2 - 3.2: NicoleCutie Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        ],
        'f9fb2aa0': [
            (log,                             ('2.2 - 3.2: NicoleCutie Body Blend VB Hash',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
        ],
        '4af0010c': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b2bd144b', 'NicoleCutie.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b2bd144b', 'NicoleCutie.AmillionA.Diffuse.1024')),
        ],
        'b2bd144b': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4af0010c', 'NicoleCutie.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('4af0010c', 'NicoleCutie.AmillionA.Diffuse.2048')),
        ],
        'c45a93a3': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5fcde3a6', 'NicoleCutie.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('5fcde3a6', 'NicoleCutie.AmillionA.LightMap.1024')),
        ],
        '5fcde3a6': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c45a93a3', 'NicoleCutie.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('c45a93a3', 'NicoleCutie.AmillionA.LightMap.2048')),
        ],
        '592cee08': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76774ee7', 'NicoleCutie.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('76774ee7', 'NicoleCutie.AmillionA.MaterialMap.1024')),
        ],
        '76774ee7': [
            (log,                             ('2.2 - 3.2: NicoleCutie BodyA and AmillionA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('52842f31', 'NicoleCutie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('592cee08', 'NicoleCutie.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('592cee08', 'NicoleCutie.AmillionA.MaterialMap.2048')),
        ],
        # Body shares its Diffuse, LightMap and MaterialMap hashes with Amillion, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Amillion Component ====================
        '40e64ae2': [
            (log,                             ('2.2 - 3.2: NicoleCutie Amillion IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bb7fffe9': [
            (log,                             ('2.2 - 3.2: NicoleCutie Amillion Draw VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        ],
        '176bf3d7': [
            (log,                             ('2.2 - 3.2: NicoleCutie Amillion Position VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        ],
        '077c3500': [
            (log,                             ('2.2 - 2.8: NicoleCutie Amillion Texcoord VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f9f810ed',)),
        ],
        'f9f810ed': [
            (log,                             ('3.0 - 3.2: NicoleCutie Amillion Texcoord VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        ],
        '4e1d9c9a': [
            (log,                             ('2.2 - 3.2: NicoleCutie Amillion Blend VB Hash',)),
            (add_section_if_missing,          ('40e64ae2', 'NicoleCutie.Amillion.IB', 'match_priority = 0\n')),
        ],
        # Amillion shares its Diffuse, LightMap and MaterialMap hashes with Body, and its NormalMap hashes with Hair; see those Components above.

        # ==================== Face Component ====================
        '7435fc0e': [
            (log,                             ('2.2 - 2.8: NicoleCutie Face IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('93b02078',)),
        ],
        '93b02078': [
            (log,                             ('3.0 - 3.2: NicoleCutie Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9274e401': [
            (log,                             ('2.2 - 2.8: NicoleCutie Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('967c2f1c',)),
        ],
        'a8667746': [
            (log,                             ('2.2 - 2.8: NicoleCutie Face Position VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ac6ebc5b',)),
        ],
        '5714e5e6': [
            (log,                             ('2.2 - 2.8: NicoleCutie Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d5958556',)),
        ],
        'b25ebcf6': [
            (log,                             ('2.2 - 2.8: NicoleCutie Face Blend VB Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('292d1b1f',)),
        ],
        '967c2f1c': [
            (log,                             ('3.0 - 3.2: NicoleCutie Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        ],
        'ac6ebc5b': [
            (log,                             ('3.0 - 3.2: NicoleCutie Face Position VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        ],
        'd5958556': [
            (log,                             ('3.0 - 3.1: NicoleCutie Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('31df6120',)),
        ],
        '31df6120': [
            (log,                             ('3.2: NicoleCutie Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '292d1b1f': [
            (log,                             ('3.0 - 3.2: NicoleCutie Face Blend VB Hash',)),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
        ],
        'd1e84a34': [
            (log,                             ('2.2 - 3.2: NicoleCutie FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6abd3dd3', 'NicoleCutie.FaceA.Diffuse.1024')),
        ],
        '6abd3dd3': [
            (log,                             ('2.2 - 3.2: NicoleCutie FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7435fc0e', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93b02078', 'NicoleCutie.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1e84a34', 'NicoleCutie.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        'f9befc51': [
            (log,                             ('2.2 - 3.2: NicoleCutie weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f6325378': [
            (log,                             ('2.2 - 3.2: NicoleCutie weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
        ],
        '00c8b3c5': [
            (log,                             ('2.2 - 3.2: NicoleCutie weapon Position VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
        ],
        '14b0d6b6': [
            (log,                             ('2.2 - 3.2: NicoleCutie weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
        ],
        '2f427bdb': [
            (log,                             ('2.2 - 3.2: NicoleCutie weapon Blend VB Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
        ],
        '67f0bd9c': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('89699adb', 'NicoleCutie.weaponA.Diffuse.1024')),
        ],
        '89699adb': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('67f0bd9c', 'NicoleCutie.weaponA.Diffuse.2048')),
        ],
        '7672fb0c': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b6f0f975', 'NicoleCutie.weaponB.Diffuse.1024')),
        ],
        'b6f0f975': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7672fb0c', 'NicoleCutie.weaponB.Diffuse.2048')),
        ],
        '28d0438d': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b89dc4e4', 'NicoleCutie.weaponA.LightMap.1024')),
        ],
        'b89dc4e4': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28d0438d', 'NicoleCutie.weaponA.LightMap.2048')),
        ],
        'c03d03de': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('df7b84ed', 'NicoleCutie.weaponB.LightMap.1024')),
        ],
        'df7b84ed': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c03d03de', 'NicoleCutie.weaponB.LightMap.2048')),
        ],
        'f1304abf': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('48f45547', 'NicoleCutie.weaponA.MaterialMap.1024')),
        ],
        '48f45547': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1304abf', 'NicoleCutie.weaponA.MaterialMap.2048')),
        ],
        '028c6ebf': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5c298267', 'NicoleCutie.weaponB.MaterialMap.1024')),
        ],
        '5c298267': [
            (log,                             ('2.2 - 3.2: NicoleCutie weaponB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f9befc51', 'NicoleCutie.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('028c6ebf', 'NicoleCutie.weaponB.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.

        # ==================== mobile phone Component ====================
        '262c96ff': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phone IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '63d1bd6f': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phone Draw VB Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
        ],
        'ef68beba': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phone Position VB Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
        ],
        '8424f0ec': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phone Texcoord VB Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
        ],
        'cbce3456': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phone Blend VB Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
        ],
        '6986beb1': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d484bf22', 'NicoleCutie.mobile phoneA.Diffuse.1024')),
        ],
        'd484bf22': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6986beb1', 'NicoleCutie.mobile phoneA.Diffuse.2048')),
        ],
        '4ae94b82': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d3aca36', 'NicoleCutie.mobile phoneA.LightMap.1024')),
        ],
        '8d3aca36': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ae94b82', 'NicoleCutie.mobile phoneA.LightMap.2048')),
        ],
        '4bbaadb9': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f8db9ea5', 'NicoleCutie.mobile phoneA.MaterialMap.1024')),
        ],
        'f8db9ea5': [
            (log,                             ('2.2 - 3.2: NicoleCutie mobile phoneA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('262c96ff', 'NicoleCutie.mobile phone.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4bbaadb9', 'NicoleCutie.mobile phoneA.MaterialMap.2048')),
        ],
        # mobile phone shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NicoleCutie',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
