"""
Pyrois Character Hash Commands
ZZZ Mod Fixer v3.0
Game Version: 3.0 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Pyrois's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd98c8923': [
            (log,                             ('3.0 - 3.2: Pyrois Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6204c171': [
            (log,                             ('3.0 - 3.2: Pyrois Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        ],
        '7fdd4865': [
            (log,                             ('3.0 - 3.2: Pyrois Hair Position VB Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        ],
        '764bcab3': [
            (log,                             ('3.0 - 3.2: Pyrois Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        ],
        'b502aa23': [
            (log,                             ('3.0 - 3.2: Pyrois Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
        ],
        '28b3c245': [
            (log,                             ('3.0 - 3.2: Pyrois HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bee6766b', 'Pyrois.HairA.Diffuse.1024')),
        ],
        'bee6766b': [
            (log,                             ('3.0 - 3.2: Pyrois HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28b3c245', 'Pyrois.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.0 - 3.2: Pyrois HairA, BodyA, ArmA and SwordA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Pyrois.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pyrois.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pyrois.ArmA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pyrois.SwordA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.0 - 3.2: Pyrois HairA, BodyA, ArmA and SwordA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Pyrois.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pyrois.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pyrois.ArmA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pyrois.SwordA.NormalMap.2048')),
        ],
        '0d24e396': [
            (log,                             ('3.0 - 3.2: Pyrois HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6bec1d56', 'Pyrois.HairA.LightMap.1024')),
        ],
        '6bec1d56': [
            (log,                             ('3.0 - 3.2: Pyrois HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0d24e396', 'Pyrois.HairA.LightMap.2048')),
        ],
        'bd5b0984': [
            (log,                             ('3.0 - 3.2: Pyrois HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7405e2d5', 'Pyrois.HairA.MaterialMap.1024')),
        ],
        '7405e2d5': [
            (log,                             ('3.0 - 3.2: Pyrois HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd5b0984', 'Pyrois.HairA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'd347d859': [
            (log,                             ('3.0 - 3.2: Pyrois Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5bbaca72': [
            (log,                             ('3.0 - 3.2: Pyrois Body Draw VB Hash',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        ],
        'c1f14931': [
            (log,                             ('3.0 - 3.2: Pyrois Body Position VB Hash',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        ],
        '337fe1ee': [
            (log,                             ('3.0 - 3.2: Pyrois Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        ],
        '789800b3': [
            (log,                             ('3.0 - 3.2: Pyrois Body Blend VB Hash',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
        ],
        'ef11e537': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1331e7ee', 'Pyrois.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1331e7ee', 'Pyrois.ArmA.Diffuse.1024')),
        ],
        '1331e7ee': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef11e537', 'Pyrois.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ef11e537', 'Pyrois.ArmA.Diffuse.2048')),
        ],
        'c7a6063b': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3ed5431d', 'Pyrois.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('3ed5431d', 'Pyrois.ArmA.LightMap.1024')),
        ],
        '3ed5431d': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7a6063b', 'Pyrois.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('c7a6063b', 'Pyrois.ArmA.LightMap.2048')),
        ],
        'd81be7b3': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('17c1a8e2', 'Pyrois.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('17c1a8e2', 'Pyrois.ArmA.MaterialMap.1024')),
        ],
        '17c1a8e2': [
            (log,                             ('3.0 - 3.2: Pyrois BodyA and ArmA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d81be7b3', 'Pyrois.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d81be7b3', 'Pyrois.ArmA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Arm Component ====================
        '0a7c1023': [
            (log,                             ('3.0 - 3.2: Pyrois Arm IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8e155d0d': [
            (log,                             ('3.0 - 3.2: Pyrois Arm Draw VB Hash',)),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        ],
        'a816b4ec': [
            (log,                             ('3.0 - 3.2: Pyrois Arm Position VB Hash',)),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        ],
        '1abe00b9': [
            (log,                             ('3.0 - 3.2: Pyrois Arm Texcoord VB Hash',)),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        ],
        'a946c036': [
            (log,                             ('3.0 - 3.2: Pyrois Arm Blend VB Hash',)),
            (add_section_if_missing,          ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
        ],
        # Arm shares its Diffuse, LightMap and MaterialMap hashes with Body and its NormalMap hashes with Hair; see those Components above.

        # ==================== Sword Component ====================
        '585b0241': [
            (log,                             ('3.0 - 3.2: Pyrois Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c942b027': [
            (log,                             ('3.0 - 3.2: Pyrois Sword Draw VB Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
        ],
        '899ea8ea': [
            (log,                             ('3.0 - 3.2: Pyrois Sword Position VB Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
        ],
        'bc7a3429': [
            (log,                             ('3.0 - 3.2: Pyrois Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
        ],
        'd51ce897': [
            (log,                             ('3.0 - 3.2: Pyrois Sword Blend VB Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
        ],
        'bda9d364': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('36cbf65b', 'Pyrois.SwordA.Diffuse.1024')),
        ],
        '36cbf65b': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bda9d364', 'Pyrois.SwordA.Diffuse.2048')),
        ],
        '6bc7e6b2': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('964cadd0', 'Pyrois.SwordA.LightMap.1024')),
        ],
        '964cadd0': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6bc7e6b2', 'Pyrois.SwordA.LightMap.2048')),
        ],
        'a71b1a4a': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8cb22c6d', 'Pyrois.SwordA.MaterialMap.1024')),
        ],
        '8cb22c6d': [
            (log,                             ('3.0 - 3.2: Pyrois SwordA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a71b1a4a', 'Pyrois.SwordA.MaterialMap.2048')),
        ],
        # Sword shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pyrois',
    'game_versions': ['3.0', '3.1', '3.2'],
}
