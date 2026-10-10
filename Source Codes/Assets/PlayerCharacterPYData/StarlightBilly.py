"""
StarlightBilly Character Hash Commands
ZZZ Mod Fixer v2.5
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
    Returns StarlightBilly's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'b126d40d': [
            (log,                             ('2.8 - 3.2: StarlightBilly Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0a1f876f': [
            (log,                             ('2.8 - 3.2: StarlightBilly Hair Draw VB Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
        ],
        '2182114e': [
            (log,                             ('2.8 - 3.2: StarlightBilly Hair Position VB Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
        ],
        'bedc10c4': [
            (log,                             ('2.8 - 3.2: StarlightBilly Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
        ],
        '794d5c7b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Hair Blend VB Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
        ],
        'ff939fb7': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6a6a1c79', 'StarlightBilly.HairA.Diffuse.1024')),
        ],
        '6a6a1c79': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ff939fb7', 'StarlightBilly.HairA.Diffuse.2048')),
        ],
        '798adba3': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA NormalMap 2048p Hash, also BodyA, TorsoA, LeftArmA, CollarA, BackDecoration1A, BackDecoration2A, MotorcycleA, FaceA, GunA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'StarlightBilly.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.TorsoA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.LeftArmA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.CollarA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.BackDecoration1A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.BackDecoration2A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.MotorcycleA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.FaceA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.GunA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.WeaponAccessory1A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.WeaponAccessory2A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.WeaponAccessory3A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'StarlightBilly.WeaponAccessory4A.NormalMap.2048')),
        ],
        'ffdc1ea7': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.HairA.NormalMap.2048')),
        ],
        'b6e1da4b': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2edbc842', 'StarlightBilly.HairA.LightMap.1024')),
        ],
        '2edbc842': [
            (log,                             ('2.8 - 3.2: StarlightBilly HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b6e1da4b', 'StarlightBilly.HairA.LightMap.2048')),
        ],

        # ==================== Body Component ====================
        '099cc55b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c0d45183': [
            (log,                             ('2.8 - 3.2: StarlightBilly Body Draw VB Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
        ],
        'b792110b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Body Position VB Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
        ],
        '203e1a47': [
            (log,                             ('2.8 - 3.2: StarlightBilly Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
        ],
        'ccfa3c1f': [
            (log,                             ('2.8 - 3.2: StarlightBilly Body Blend VB Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
        ],
        '30b6b9c7': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be5165ce', 'StarlightBilly.BodyA.Diffuse.1024')),
        ],
        'be5165ce': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('30b6b9c7', 'StarlightBilly.BodyA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA, TorsoA, LeftArmA, CollarA, BackDecoration1A, BackDecoration2A, MotorcycleA, FaceA, GunA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.TorsoA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.LeftArmA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.CollarA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.BackDecoration1A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.BackDecoration2A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.MotorcycleA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.FaceA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.GunA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.WeaponAccessory1A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.WeaponAccessory2A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.WeaponAccessory3A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'StarlightBilly.WeaponAccessory4A.NormalMap.1024')),
        ],
        'da2181cf': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7ac1a66a', 'StarlightBilly.BodyA.LightMap.1024')),
        ],
        '7ac1a66a': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('da2181cf', 'StarlightBilly.BodyA.LightMap.2048')),
        ],
        'd85dec5d': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('150df321', 'StarlightBilly.BodyA.MaterialMap.1024')),
        ],
        '150df321': [
            (log,                             ('2.8 - 3.2: StarlightBilly BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d85dec5d', 'StarlightBilly.BodyA.MaterialMap.2048')),
        ],

        # ==================== Torso Component ====================
        'b602e4de': [
            (log,                             ('2.8 - 3.2: StarlightBilly Torso IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '617a4f7c': [
            (log,                             ('2.8 - 3.2: StarlightBilly Torso Draw VB Hash',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        ],
        '45992c18': [
            (log,                             ('2.8 - 3.2: StarlightBilly Torso Position VB Hash',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        ],
        '97c35484': [
            (log,                             ('2.8 - 3.2: StarlightBilly Torso Texcoord VB Hash',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        ],
        'a829800f': [
            (log,                             ('2.8 - 3.2: StarlightBilly Torso Blend VB Hash',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
        ],
        'd82e8cd7': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a6ef0c74', 'StarlightBilly.TorsoA.Diffuse.1024')),
            (multiply_section_if_missing,     ('a6ef0c74', 'StarlightBilly.CollarA.Diffuse.1024')),
            (multiply_section_if_missing,     ('a6ef0c74', 'StarlightBilly.BackDecoration1A.Diffuse.1024')),
            (multiply_section_if_missing,     ('a6ef0c74', 'StarlightBilly.BackDecoration2A.Diffuse.1024')),
        ],
        'a6ef0c74': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d82e8cd7', 'StarlightBilly.TorsoA.Diffuse.2048')),
            (multiply_section_if_missing,     ('d82e8cd7', 'StarlightBilly.CollarA.Diffuse.2048')),
            (multiply_section_if_missing,     ('d82e8cd7', 'StarlightBilly.BackDecoration1A.Diffuse.2048')),
            (multiply_section_if_missing,     ('d82e8cd7', 'StarlightBilly.BackDecoration2A.Diffuse.2048')),
        ],
        'a28930f3': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6effa144', 'StarlightBilly.TorsoA.LightMap.1024')),
            (multiply_section_if_missing,     ('6effa144', 'StarlightBilly.CollarA.LightMap.1024')),
            (multiply_section_if_missing,     ('6effa144', 'StarlightBilly.BackDecoration1A.LightMap.1024')),
            (multiply_section_if_missing,     ('6effa144', 'StarlightBilly.BackDecoration2A.LightMap.1024')),
        ],
        '6effa144': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a28930f3', 'StarlightBilly.TorsoA.LightMap.2048')),
            (multiply_section_if_missing,     ('a28930f3', 'StarlightBilly.CollarA.LightMap.2048')),
            (multiply_section_if_missing,     ('a28930f3', 'StarlightBilly.BackDecoration1A.LightMap.2048')),
            (multiply_section_if_missing,     ('a28930f3', 'StarlightBilly.BackDecoration2A.LightMap.2048')),
        ],
        'f8f7fdbe': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('744b53d4', 'StarlightBilly.TorsoA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('744b53d4', 'StarlightBilly.CollarA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('744b53d4', 'StarlightBilly.BackDecoration1A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('744b53d4', 'StarlightBilly.BackDecoration2A.MaterialMap.1024')),
        ],
        '744b53d4': [
            (log,                             ('2.8 - 3.2: StarlightBilly TorsoA, CollarA, BackDecoration1A and BackDecoration2A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f8f7fdbe', 'StarlightBilly.TorsoA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f8f7fdbe', 'StarlightBilly.CollarA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f8f7fdbe', 'StarlightBilly.BackDecoration1A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f8f7fdbe', 'StarlightBilly.BackDecoration2A.MaterialMap.2048')),
        ],

        # ==================== LeftArm Component ====================
        '85ec4f39': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArm IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5a7ee5ae': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArm Draw VB Hash',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        ],
        '0d842713': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArm Position VB Hash',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        ],
        'd4575d84': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArm Texcoord VB Hash',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        ],
        '6d19734d': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArm Blend VB Hash',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
        ],
        '6fe50be9': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.LeftArmA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.WeaponAccessory1A.Diffuse.1024')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.WeaponAccessory2A.Diffuse.1024')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.WeaponAccessory3A.Diffuse.1024')),
            (multiply_section_if_missing,     ('1d5dcd0a', 'StarlightBilly.WeaponAccessory4A.Diffuse.1024')),
        ],
        '1d5dcd0a': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.LeftArmA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.WeaponAccessory1A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.WeaponAccessory2A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.WeaponAccessory3A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6fe50be9', 'StarlightBilly.WeaponAccessory4A.Diffuse.2048')),
        ],
        'c0a681c1': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.LeftArmA.LightMap.1024')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.WeaponAccessory1A.LightMap.1024')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.WeaponAccessory2A.LightMap.1024')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.WeaponAccessory3A.LightMap.1024')),
            (multiply_section_if_missing,     ('16d85b96', 'StarlightBilly.WeaponAccessory4A.LightMap.1024')),
        ],
        '16d85b96': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.LeftArmA.LightMap.2048')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.WeaponAccessory1A.LightMap.2048')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.WeaponAccessory2A.LightMap.2048')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.WeaponAccessory3A.LightMap.2048')),
            (multiply_section_if_missing,     ('c0a681c1', 'StarlightBilly.WeaponAccessory4A.LightMap.2048')),
        ],
        '95454832': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.LeftArmA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.WeaponAccessory1A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.WeaponAccessory2A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.WeaponAccessory3A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('02ac888a', 'StarlightBilly.WeaponAccessory4A.MaterialMap.1024')),
        ],
        '02ac888a': [
            (log,                             ('2.8 - 3.2: StarlightBilly LeftArmA, WeaponA, WeaponAccessory1A, WeaponAccessory2A, WeaponAccessory3A and WeaponAccessory4A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.LeftArmA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.WeaponAccessory1A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.WeaponAccessory2A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.WeaponAccessory3A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('95454832', 'StarlightBilly.WeaponAccessory4A.MaterialMap.2048')),
        ],

        # ==================== Collar Component ====================
        'fed4432c': [
            (log,                             ('2.8 - 3.2: StarlightBilly Collar IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b729d418': [
            (log,                             ('2.8 - 3.2: StarlightBilly Collar Draw VB Hash',)),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        ],
        'b5ba7f2c': [
            (log,                             ('2.8 - 3.2: StarlightBilly Collar Position VB Hash',)),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        ],
        '6cbb0e03': [
            (log,                             ('2.8 - 3.2: StarlightBilly Collar Texcoord VB Hash',)),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        ],
        '0c780fde': [
            (log,                             ('2.8 - 3.2: StarlightBilly Collar Blend VB Hash',)),
            (add_section_if_missing,          ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
        ],

        # ==================== BackDecoration1 Component ====================
        '169e16c1': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '730440ae': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration1 Draw VB Hash',)),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
        ],
        '9eda96ca': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration1 Position VB Hash',)),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
        ],
        '02125c63': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
        ],
        '14896011': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration1 Blend VB Hash',)),
            (add_section_if_missing,          ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
        ],

        # ==================== BackDecoration2 Component ====================
        '11727cec': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '93a9492c': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration2 Draw VB Hash',)),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
        ],
        'c9c3436f': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration2 Position VB Hash',)),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
        ],
        '2f2f4055': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
        ],
        '52225c15': [
            (log,                             ('2.8 - 3.2: StarlightBilly BackDecoration2 Blend VB Hash',)),
            (add_section_if_missing,          ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
        ],

        # ==================== Motorcycle Component ====================
        '26d71d07': [
            (log,                             ('2.8 - 3.2: StarlightBilly Motorcycle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7a547ef8': [
            (log,                             ('2.8 - 3.2: StarlightBilly Motorcycle Draw VB Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
        ],
        'a7516e2b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Motorcycle Position VB Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
        ],
        '09439f49': [
            (log,                             ('2.8 - 3.2: StarlightBilly Motorcycle Texcoord VB Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
        ],
        '5c3aba5b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Motorcycle Blend VB Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
        ],
        'ed4bde0d': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4aabf11', 'StarlightBilly.MotorcycleA.Diffuse.1024')),
        ],
        'd4aabf11': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed4bde0d', 'StarlightBilly.MotorcycleA.Diffuse.2048')),
        ],
        '573e87e3': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5dc62b0b', 'StarlightBilly.MotorcycleA.LightMap.1024')),
        ],
        '5dc62b0b': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('573e87e3', 'StarlightBilly.MotorcycleA.LightMap.2048')),
        ],
        '6b61b30c': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81cd8366', 'StarlightBilly.MotorcycleA.MaterialMap.1024')),
        ],
        '81cd8366': [
            (log,                             ('2.8 - 3.2: StarlightBilly MotorcycleA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b61b30c', 'StarlightBilly.MotorcycleA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '47be3135': [
            (log,                             ('2.8 - 3.2: StarlightBilly Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'eabcb930': [
            (log,                             ('2.8 - 3.2: StarlightBilly Face Draw VB Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
        ],
        'd0ae2a77': [
            (log,                             ('2.8 - 3.2: StarlightBilly Face Position VB Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
        ],
        '7d045e09': [
            (log,                             ('2.8 - 3.2: StarlightBilly Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
        ],
        'be8fd496': [
            (log,                             ('2.8 - 3.2: StarlightBilly Face Blend VB Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
        ],
        'f55b5dbb': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e706ba29', 'StarlightBilly.FaceA.Diffuse.1024')),
        ],
        'e706ba29': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f55b5dbb', 'StarlightBilly.FaceA.Diffuse.2048')),
        ],
        'ba8a1e40': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4784f14a', 'StarlightBilly.FaceA.LightMap.1024')),
        ],
        '4784f14a': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ba8a1e40', 'StarlightBilly.FaceA.LightMap.2048')),
        ],
        'bdc617ad': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d08a92b4', 'StarlightBilly.FaceA.MaterialMap.1024')),
        ],
        'd08a92b4': [
            (log,                             ('2.8 - 3.2: StarlightBilly FaceA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bdc617ad', 'StarlightBilly.FaceA.MaterialMap.2048')),
        ],

        # ==================== Gun Component ====================
        '9f671d6b': [
            (log,                             ('2.8 - 3.2: StarlightBilly Gun IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ccd59cb9': [
            (log,                             ('2.8 - 3.2: StarlightBilly Gun Draw VB Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
        ],
        'e2a3e69e': [
            (log,                             ('2.8 - 3.2: StarlightBilly Gun Position VB Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
        ],
        'dceb0608': [
            (log,                             ('2.8 - 3.2: StarlightBilly Gun Texcoord VB Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
        ],
        '1f409c43': [
            (log,                             ('2.8 - 3.2: StarlightBilly Gun Blend VB Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
        ],
        '3541c183': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3a1ee1d7', 'StarlightBilly.GunA.Diffuse.1024')),
        ],
        '3a1ee1d7': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3541c183', 'StarlightBilly.GunA.Diffuse.2048')),
        ],
        '6f6aad09': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4b0a8224', 'StarlightBilly.GunA.LightMap.1024')),
        ],
        '4b0a8224': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f6aad09', 'StarlightBilly.GunA.LightMap.2048')),
        ],
        '11af0644': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('49782d36', 'StarlightBilly.GunA.MaterialMap.1024')),
        ],
        '49782d36': [
            (log,                             ('2.8 - 3.2: StarlightBilly GunA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('11af0644', 'StarlightBilly.GunA.MaterialMap.2048')),
        ],

        # ==================== Weapon Component ====================
        '75f90347': [
            (log,                             ('2.8 - 3.2: StarlightBilly Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cf21b035': [
            (log,                             ('2.8 - 3.2: StarlightBilly Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        ],
        'db0321a9': [
            (log,                             ('2.8 - 3.2: StarlightBilly Weapon Position VB Hash',)),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        ],
        'bbe34d15': [
            (log,                             ('2.8 - 3.2: StarlightBilly Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        ],
        '6023cad8': [
            (log,                             ('2.8 - 3.2: StarlightBilly Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponAccessory1 Component ====================
        '1ee52291': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '696bd946': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory1 Draw VB Hash',)),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
        ],
        'f293dadb': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory1 Position VB Hash',)),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
        ],
        '804cf62d': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
        ],
        '7b217048': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory1 Blend VB Hash',)),
            (add_section_if_missing,          ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponAccessory2 Component ====================
        '8f4285cd': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f91227b7': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory2 Draw VB Hash',)),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
        ],
        'ce8c77da': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory2 Position VB Hash',)),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
        ],
        '8190a48a': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
        ],
        '131e5a0a': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory2 Blend VB Hash',)),
            (add_section_if_missing,          ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponAccessory3 Component ====================
        '15ae37ae': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory3 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '84a7e817': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory3 Draw VB Hash',)),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
        ],
        '612b519c': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory3 Position VB Hash',)),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
        ],
        '8a828eae': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory3 Texcoord VB Hash',)),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
        ],
        'fbf0b1bb': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory3 Blend VB Hash',)),
            (add_section_if_missing,          ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponAccessory4 Component ====================
        'd3e8cd51': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory4 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6ccff03a': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory4 Draw VB Hash',)),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
        ],
        '20ccc597': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory4 Position VB Hash',)),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
        ],
        '4cfcbaf4': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory4 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
        ],
        '82c72748': [
            (log,                             ('2.8 - 3.2: StarlightBilly WeaponAccessory4 Blend VB Hash',)),
            (add_section_if_missing,          ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'StarlightBilly',
    'game_versions': ['2.8', '3.0', '3.1', '3.2'],
}
