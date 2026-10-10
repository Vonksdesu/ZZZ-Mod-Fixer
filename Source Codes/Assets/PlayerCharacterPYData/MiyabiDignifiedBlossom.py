"""
MiyabiDignifiedBlossom Character Hash Commands
ZZZ Mod Fixer v2.8
Game Version: 2.8 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns MiyabiDignifiedBlossom's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ecaf558f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd011ed6c': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
        ],
        'e49def56': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Hair Position VB Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
        ],
        'b8cb383f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
        ],
        '28a01b2c': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
        ],
        '012e84e9': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed6b94f7', 'MiyabiDignifiedBlossom.HairA.Diffuse.1024')),
        ],
        'ed6b94f7': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('012e84e9', 'MiyabiDignifiedBlossom.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA, BodyA, ClothesA, Sword, SwordSheath and SwordHandle NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.ClothesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.Sword.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.SwordSheath.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'MiyabiDignifiedBlossom.SwordHandle.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA, BodyA, ClothesA, Sword, SwordSheath and SwordHandle NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.ClothesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.Sword.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.SwordSheath.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'MiyabiDignifiedBlossom.SwordHandle.NormalMap.2048')),
        ],
        'a6ea6d83': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b5708f4', 'MiyabiDignifiedBlossom.HairA.LightMap.1024')),
        ],
        '8b5708f4': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a6ea6d83', 'MiyabiDignifiedBlossom.HairA.LightMap.2048')),
        ],
        'd5462e37': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a84d9003', 'MiyabiDignifiedBlossom.HairA.MaterialMap.1024')),
        ],
        'a84d9003': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ecaf558f', 'MiyabiDignifiedBlossom.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5462e37', 'MiyabiDignifiedBlossom.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '244eb75a': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # HairShadow has no vertex buffers or texture hashes in the database.

        # ==================== Body Component ====================
        'a913e9a9': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a4a705f6': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Body Draw VB Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
        ],
        '6567066b': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Body Position VB Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
        ],
        '01c36f40': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
        ],
        'f2f19cb2': [
            (log,                             ('2.8 -> 2.81: MiyabiSkin Body Blend Hash',)),
            (update_hash,                     ('5121459b',)),
        ],
        '5121459b': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Body Blend VB Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
        ],
        '18299e4d': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d420160', 'MiyabiDignifiedBlossom.BodyA.Diffuse.1024')),
        ],
        '7d420160': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18299e4d', 'MiyabiDignifiedBlossom.BodyA.Diffuse.2048')),
        ],
        '6b59bc2d': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d8ad1898', 'MiyabiDignifiedBlossom.BodyA.LightMap.1024')),
        ],
        'd8ad1898': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b59bc2d', 'MiyabiDignifiedBlossom.BodyA.LightMap.2048')),
        ],
        '93d7173c': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('417337f2', 'MiyabiDignifiedBlossom.BodyA.MaterialMap.1024')),
        ],
        '417337f2': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a913e9a9', 'MiyabiDignifiedBlossom.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93d7173c', 'MiyabiDignifiedBlossom.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Clothes Component ====================
        'fbb18630': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Clothes IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '467f402c': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Clothes Draw VB Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
        ],
        'c2b0eca3': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Clothes Position VB Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
        ],
        '6eb82b02': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Clothes Texcoord VB Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
        ],
        '958db681': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Clothes Blend VB Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
        ],
        '66724f5a': [
            (log,                             ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA Diffuse 2048p Hash',)),
            (update_hash,                     ('4e6c90bd',)),
        ],
        '4e6c90bd': [
            (log,                             ('3.0 - 3.2: MiyabiDignifiedBlossom ClothesA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7d80f565', '88e357af'), 'MiyabiDignifiedBlossom.ClothesA.Diffuse.1024')),
        ],
        '88e357af': [
            (log,                             ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA Diffuse 1024p Hash',)),
            (update_hash,                     ('7d80f565',)),
        ],
        '7d80f565': [
            (log,                             ('3.0 - 3.2: MiyabiDignifiedBlossom ClothesA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('4e6c90bd', '66724f5a'), 'MiyabiDignifiedBlossom.ClothesA.Diffuse.2048')),
        ],
        '7b8eb437': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom ClothesA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93b264d9', 'MiyabiDignifiedBlossom.ClothesA.LightMap.1024')),
        ],
        '93b264d9': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom ClothesA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7b8eb437', 'MiyabiDignifiedBlossom.ClothesA.LightMap.2048')),
        ],
        '1e1485e7': [
            (log,                             ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA MaterialMap 2048p Hash',)),
            (update_hash,                     ('30590865',)),
        ],
        '30590865': [
            (log,                             ('3.0 - 3.2: MiyabiDignifiedBlossom ClothesA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2fbabf2e', '85aad660'), 'MiyabiDignifiedBlossom.ClothesA.MaterialMap.1024')),
        ],
        '85aad660': [
            (log,                             ('2.8 -> 3.0: MiyabiDignifiedBlossom ClothesA MaterialMap 1024p Hash',)),
            (update_hash,                     ('2fbabf2e',)),
        ],
        '2fbabf2e': [
            (log,                             ('3.0 - 3.2: MiyabiDignifiedBlossom ClothesA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fbb18630', 'MiyabiDignifiedBlossom.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('30590865', '1e1485e7'), 'MiyabiDignifiedBlossom.ClothesA.MaterialMap.2048')),
        ],
        # Clothes shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        'dbd59d30': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0dbd45ea': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Face Draw VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
        ],
        '37afd6ad': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Face Position VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
        ],
        '7a476f86': [
            (log,                             ('2.8 - 3.1: MiyabiDignifiedBlossom Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('60732ab5',)),
        ],
        '60732ab5': [
            (log,                             ('3.2: MiyabiDignifiedBlossom Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'd7781c46': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Face Blend VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
        ],
        '1d487fd5': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('92599e94', 'MiyabiDignifiedBlossom.FaceA.Diffuse.1024')),
        ],
        '92599e94': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'MiyabiDignifiedBlossom.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d487fd5', 'MiyabiDignifiedBlossom.FaceA.Diffuse.2048')),
        ],

        # ==================== Sword Component ====================
        '0275d39f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9d6f441f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword Draw VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        ],
        '81a99d68': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword Position VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        ],
        'aeb95d61': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        ],
        '8bc72b94': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword Blend VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
        ],
        'e1215530': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9ec3ac8', 'MiyabiDignifiedBlossom.Sword.Diffuse.1024')),
            (multiply_section_if_missing,     ('f9ec3ac8', 'MiyabiDignifiedBlossom.SwordSheath.Diffuse.1024')),
            (multiply_section_if_missing,     ('f9ec3ac8', 'MiyabiDignifiedBlossom.SwordHandle.Diffuse.1024')),
        ],
        'f9ec3ac8': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1215530', 'MiyabiDignifiedBlossom.Sword.Diffuse.2048')),
            (multiply_section_if_missing,     ('e1215530', 'MiyabiDignifiedBlossom.SwordSheath.Diffuse.2048')),
            (multiply_section_if_missing,     ('e1215530', 'MiyabiDignifiedBlossom.SwordHandle.Diffuse.2048')),
        ],
        '9d2adcc5': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0f21a6c9', 'MiyabiDignifiedBlossom.Sword.LightMap.1024')),
            (multiply_section_if_missing,     ('0f21a6c9', 'MiyabiDignifiedBlossom.SwordSheath.LightMap.1024')),
            (multiply_section_if_missing,     ('0f21a6c9', 'MiyabiDignifiedBlossom.SwordHandle.LightMap.1024')),
        ],
        '0f21a6c9': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9d2adcc5', 'MiyabiDignifiedBlossom.Sword.LightMap.2048')),
            (multiply_section_if_missing,     ('9d2adcc5', 'MiyabiDignifiedBlossom.SwordSheath.LightMap.2048')),
            (multiply_section_if_missing,     ('9d2adcc5', 'MiyabiDignifiedBlossom.SwordHandle.LightMap.2048')),
        ],
        '4659445f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e6eab72f', 'MiyabiDignifiedBlossom.Sword.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e6eab72f', 'MiyabiDignifiedBlossom.SwordSheath.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e6eab72f', 'MiyabiDignifiedBlossom.SwordHandle.MaterialMap.1024')),
        ],
        'e6eab72f': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom Sword, SwordSheath and SwordHandle MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'MiyabiDignifiedBlossom.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4659445f', 'MiyabiDignifiedBlossom.Sword.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4659445f', 'MiyabiDignifiedBlossom.SwordSheath.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4659445f', 'MiyabiDignifiedBlossom.SwordHandle.MaterialMap.2048')),
        ],
        # The Sword components share their NormalMap hashes with Hair; see that Component above.

        # ==================== SwordSheath Component ====================
        '562b2030': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordSheath IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e3590e91': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordSheath Draw VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        ],
        'fc93f762': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordSheath Position VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        ],
        'a9ac3439': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordSheath Texcoord VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        ],
        '38c91cb1': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordSheath Blend VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'MiyabiDignifiedBlossom.SwordSheath.IB', 'match_priority = 0\n')),
        ],
        # SwordSheath shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Sword; see that Component above.

        # ==================== SwordHandle Component ====================
        '1a82a439': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordHandle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5e1e12aa': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordHandle Draw VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
        ],
        '10545b04': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordHandle Position VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
        ],
        '51af1803': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordHandle Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
        ],
        'c55927b0': [
            (log,                             ('2.8 - 3.2: MiyabiDignifiedBlossom SwordHandle Blend VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'MiyabiDignifiedBlossom.SwordHandle.IB', 'match_priority = 0\n')),
        ],
        # SwordHandle shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Sword; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'MiyabiDignifiedBlossom',
    'game_versions': ['2.8', '3.0', '3.1', '3.2'],
}
