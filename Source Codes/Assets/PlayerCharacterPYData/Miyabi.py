"""
Miyabi Character Hash Commands
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
    Returns Miyabi's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '4faabaac': [
            (log,                             ('2.2 - 3.2: Miyabi Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5a8d28f4': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Draw VB Hash',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        ],
        'f9b9b064': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Position VB Hash',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        ],
        'b6530b86': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        ],
        '8b2eeb77': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Blend VB Hash',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
        ],
        '012e84e9': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed6b94f7', 'Miyabi.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('ed6b94f7', 'Miyabi.LegsA.Diffuse.1024')),
        ],
        'ed6b94f7': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('012e84e9', 'Miyabi.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('012e84e9', 'Miyabi.LegsA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Miyabi HairA, BodyA, LegsA, weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.weapon - 刀身.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.weapon - 刀柄.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.weapon - 刀鞘.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.weapon - 剑灵.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Miyabi HairA, BodyA, LegsA, weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 NormalMap 1024p Hash, also HairpinA and Hairpin ribbonA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.weapon - 刀身.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.weapon - 刀柄.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.weapon - 刀鞘.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Miyabi.weapon - 剑灵.NormalMap.2048')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Miyabi.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Miyabi.Hairpin ribbonA.NormalMap.1024')),
        ],
        'a6ea6d83': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b5708f4', 'Miyabi.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('8b5708f4', 'Miyabi.LegsA.LightMap.1024')),
        ],
        '8b5708f4': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a6ea6d83', 'Miyabi.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('a6ea6d83', 'Miyabi.LegsA.LightMap.2048')),
        ],
        'd5462e37': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a84d9003', 'Miyabi.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('a84d9003', 'Miyabi.LegsA.MaterialMap.1024')),
        ],
        'a84d9003': [
            (log,                             ('2.2 - 3.2: Miyabi HairA and LegsA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4faabaac', 'Miyabi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d5462e37', 'Miyabi.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d5462e37', 'Miyabi.LegsA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'acff032e': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e8082f3c': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a10b08d2': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '70717c93': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9c3d5e1f': [
            (log,                             ('2.2 - 3.2: Miyabi Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('acff032e', 'Miyabi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no texture hashes in the database.

        # ==================== Hairpin Component ====================
        '02e62d7e': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bbce89b9': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'e7041a99': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '750d2a46': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '7ed40a2f': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'e24bfe0e': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4e752f58', 'Miyabi.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     ('4e752f58', 'Miyabi.Hairpin ribbonA.Diffuse.1024')),
        ],
        '4e752f58': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e24bfe0e', 'Miyabi.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     ('e24bfe0e', 'Miyabi.Hairpin ribbonA.Diffuse.2048')),
        ],
        'ffdc1ea7': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.HairpinA.NormalMap.2048')),
            (multiply_section_if_missing,     ('798adba3', 'Miyabi.Hairpin ribbonA.NormalMap.2048')),
        ],
        '9e1067e9': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e10040c7', 'Miyabi.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     ('e10040c7', 'Miyabi.Hairpin ribbonA.LightMap.1024')),
        ],
        'e10040c7': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e1067e9', 'Miyabi.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     ('9e1067e9', 'Miyabi.Hairpin ribbonA.LightMap.2048')),
        ],
        'f4d343b2': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3af946eb', 'Miyabi.HairpinA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('3af946eb', 'Miyabi.Hairpin ribbonA.MaterialMap.1024')),
        ],
        '3af946eb': [
            (log,                             ('2.2 - 3.2: Miyabi HairpinA and Hairpin ribbonA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('02e62d7e', 'Miyabi.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f4d343b2', 'Miyabi.HairpinA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f4d343b2', 'Miyabi.Hairpin ribbonA.MaterialMap.2048')),
        ],

        # ==================== Hairpin ribbon Component ====================
        '0c26a38b': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin ribbon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3421e96d': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin ribbon Draw VB Hash',)),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
        ],
        'be288799': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin ribbon Position VB Hash',)),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
        ],
        'fcc57f25': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin ribbon Texcoord VB Hash',)),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
        ],
        '827f5947': [
            (log,                             ('2.2 - 3.2: Miyabi Hairpin ribbon Blend VB Hash',)),
            (add_section_if_missing,          ('0c26a38b', 'Miyabi.Hairpin ribbon.IB', 'match_priority = 0\n')),
        ],
        # Hairpin ribbon shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Hairpin; see that Component above.

        # ==================== Body Component ====================
        '981c1a1e': [
            (log,                             ('2.2 - 3.2: Miyabi Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6201dd9e': [
            (log,                             ('2.2 - 3.2: Miyabi Body Draw VB Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        ],
        '8ecb10b3': [
            (log,                             ('2.2 - 3.2: Miyabi Body Position VB Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        ],
        '303fb1b6': [
            (log,                             ('2.2 - 3.2: Miyabi Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        ],
        '9a4227c8': [
            (log,                             ('2.2 - 3.2: Miyabi Body Blend VB Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
        ],
        '09a2bbd1': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1a3644e7', 'Miyabi.BodyA.Diffuse.1024')),
        ],
        '1a3644e7': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('09a2bbd1', 'Miyabi.BodyA.Diffuse.2048')),
        ],
        'fd289380': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0492f64a', 'Miyabi.BodyA.LightMap.1024')),
        ],
        '0492f64a': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fd289380', 'Miyabi.BodyA.LightMap.2048')),
        ],
        '450770fd': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('168b1df9', 'Miyabi.BodyA.MaterialMap.1024')),
        ],
        '168b1df9': [
            (log,                             ('2.2 - 3.2: Miyabi BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('981c1a1e', 'Miyabi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('450770fd', 'Miyabi.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Legs Component ====================
        'd8003df3': [
            (log,                             ('2.2 - 3.2: Miyabi Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8336ded4': [
            (log,                             ('2.2 - 3.2: Miyabi Legs Draw VB Hash',)),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
        ],
        'e71bbd08': [
            (log,                             ('2.2 - 3.2: Miyabi Legs Position VB Hash',)),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
        ],
        'fb94d66c': [
            (log,                             ('2.2 - 3.2: Miyabi Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
        ],
        'bc586fd9': [
            (log,                             ('2.2 - 3.2: Miyabi Legs Blend VB Hash',)),
            (add_section_if_missing,          ('d8003df3', 'Miyabi.Legs.IB', 'match_priority = 0\n')),
        ],
        # Legs shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        'dbd59d30': [
            (log,                             ('2.2 - 3.2: Miyabi Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0dbd45ea': [
            (log,                             ('2.2 - 3.2: Miyabi Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        ],
        '37afd6ad': [
            (log,                             ('2.2 - 3.1: Miyabi Face Position VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        ],
        '7a476f86': [
            (log,                             ('2.2 - 3.1: Miyabi Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        ],
        'd7781c46': [
            (log,                             ('2.2 - 3.1: Miyabi Face Blend VB Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
        ],
        '1d487fd5': [
            (log,                             ('2.2 - 3.2: Miyabi FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('92599e94', 'Miyabi.FaceA.Diffuse.1024')),
        ],
        '92599e94': [
            (log,                             ('2.2 - 3.2: Miyabi FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dbd59d30', 'Miyabi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d487fd5', 'Miyabi.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 刀身 Component ====================
        '0275d39f': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9d6f441f': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
        ],
        '81a99d68': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀身 Position VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
        ],
        'aeb95d61': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀身 Texcoord VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
        ],
        '8bc72b94': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀身 Blend VB Hash',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
        ],
        '718d7915': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac7673da', 'Miyabi.weapon - 刀身.Diffuse.1024')),
            (multiply_section_if_missing,     ('ac7673da', 'Miyabi.weapon - 刀柄.Diffuse.1024')),
            (multiply_section_if_missing,     ('ac7673da', 'Miyabi.weapon - 刀鞘.Diffuse.1024')),
            (multiply_section_if_missing,     ('ac7673da', 'Miyabi.weapon - 剑灵.Diffuse.1024')),
        ],
        'ac7673da': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('718d7915', 'Miyabi.weapon - 刀身.Diffuse.2048')),
            (multiply_section_if_missing,     ('718d7915', 'Miyabi.weapon - 刀柄.Diffuse.2048')),
            (multiply_section_if_missing,     ('718d7915', 'Miyabi.weapon - 刀鞘.Diffuse.2048')),
            (multiply_section_if_missing,     ('718d7915', 'Miyabi.weapon - 剑灵.Diffuse.2048')),
        ],
        'b73ed7e7': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f33cdee7', 'Miyabi.weapon - 刀身.LightMap.1024')),
            (multiply_section_if_missing,     ('f33cdee7', 'Miyabi.weapon - 刀柄.LightMap.1024')),
            (multiply_section_if_missing,     ('f33cdee7', 'Miyabi.weapon - 刀鞘.LightMap.1024')),
            (multiply_section_if_missing,     ('f33cdee7', 'Miyabi.weapon - 剑灵.LightMap.1024')),
        ],
        'f33cdee7': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b73ed7e7', 'Miyabi.weapon - 刀身.LightMap.2048')),
            (multiply_section_if_missing,     ('b73ed7e7', 'Miyabi.weapon - 刀柄.LightMap.2048')),
            (multiply_section_if_missing,     ('b73ed7e7', 'Miyabi.weapon - 刀鞘.LightMap.2048')),
            (multiply_section_if_missing,     ('b73ed7e7', 'Miyabi.weapon - 剑灵.LightMap.2048')),
        ],
        'e1603ca5': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8931b1ec', 'Miyabi.weapon - 刀身.MaterialMap.1024')),
            (multiply_section_if_missing,     ('8931b1ec', 'Miyabi.weapon - 刀柄.MaterialMap.1024')),
            (multiply_section_if_missing,     ('8931b1ec', 'Miyabi.weapon - 刀鞘.MaterialMap.1024')),
            (multiply_section_if_missing,     ('8931b1ec', 'Miyabi.weapon - 剑灵.MaterialMap.1024')),
        ],
        '8931b1ec': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀身, weapon - 刀柄, weapon - 刀鞘 and weapon - 剑灵 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0275d39f', 'Miyabi.weapon - 刀身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1603ca5', 'Miyabi.weapon - 刀身.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e1603ca5', 'Miyabi.weapon - 刀柄.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e1603ca5', 'Miyabi.weapon - 刀鞘.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e1603ca5', 'Miyabi.weapon - 剑灵.MaterialMap.2048')),
        ],
        # The weapon components share their NormalMap hashes with Hair; see that Component above.

        # ==================== weapon - 刀柄 Component ====================
        '1a82a439': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀柄 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5e1e12aa': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀柄 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
        ],
        '10545b04': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀柄 Position VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
        ],
        '51af1803': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀柄 Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
        ],
        'c55927b0': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀柄 Blend VB Hash',)),
            (add_section_if_missing,          ('1a82a439', 'Miyabi.weapon - 刀柄.IB', 'match_priority = 0\n')),
        ],
        # weapon - 刀柄 shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with weapon - 刀身; see that Component above.

        # ==================== weapon - 刀鞘 Component ====================
        '562b2030': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀鞘 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e3590e91': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 刀鞘 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        'fc93f762': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀鞘 Position VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        'a9ac3439': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀鞘 Texcoord VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        '38c91cb1': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 刀鞘 Blend VB Hash',)),
            (add_section_if_missing,          ('562b2030', 'Miyabi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        # weapon - 刀鞘 shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with weapon - 刀身; see that Component above.

        # ==================== weapon - 剑灵 Component ====================
        '12739125': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 剑灵 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '79bd2f22': [
            (log,                             ('2.2 - 3.2: Miyabi weapon - 剑灵 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
        ],
        'e106fdc0': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 剑灵 Position VB Hash',)),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
        ],
        'd6ea3283': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 剑灵 Texcoord VB Hash',)),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
        ],
        '51a4604d': [
            (log,                             ('2.2 - 3.1: Miyabi weapon - 剑灵 Blend VB Hash',)),
            (add_section_if_missing,          ('12739125', 'Miyabi.weapon - 剑灵.IB', 'match_priority = 0\n')),
        ],
        # weapon - 剑灵 shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with weapon - 刀身; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Miyabi',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
