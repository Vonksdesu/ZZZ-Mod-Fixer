"""
StarlightBilly Character Hash Commands
ZZZ Mod Fixer v2.8
Game Version: 2.8
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
# === IB Hashes ===
'099cc55b': [
        (log,                           ('2.8: StarlightBilly Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'fed4432c': [
        (log,                           ('2.8: StarlightBilly Collar IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'47be3135': [
        (log,                           ('2.8: StarlightBilly Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b126d40d': [
        (log,                           ('2.8: StarlightBilly Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'85ec4f39': [
        (log,                           ('2.8: StarlightBilly LeftArm IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'26d71d07': [
        (log,                           ('2.8: StarlightBilly Motorcycle IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b602e4de': [
        (log,                           ('2.8: StarlightBilly Torso IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === StarlightBilly Textures (FaceA) ===
'e706ba29': [
        (log,                           ('2.8: StarlightBilly FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('f55b5dbb', 'StarlightBilly.FaceA.Diffuse.2048')),
    ],
'f55b5dbb': [
        (log,                           ('2.8: StarlightBilly FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('e706ba29', 'StarlightBilly.FaceA.Diffuse.1024')),
    ],
'4784f14a': [
        (log,                           ('2.8: StarlightBilly FaceA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('ba8a1e40', 'StarlightBilly.FaceA.LightMap.2048')),
    ],
'ba8a1e40': [
        (log,                           ('2.8: StarlightBilly FaceA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('4784f14a', 'StarlightBilly.FaceA.LightMap.1024')),
    ],
'd08a92b4': [
        (log,                           ('2.8: StarlightBilly FaceA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('bdc617ad', 'StarlightBilly.FaceA.MaterialMap.2048')),
    ],
'bdc617ad': [
        (log,                           ('2.8: StarlightBilly FaceA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d08a92b4', 'StarlightBilly.FaceA.MaterialMap.1024')),
    ],

# === StarlightBilly Textures (BodyA) ===
'be5165ce': [
        (log,                           ('2.8: StarlightBilly BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('30b6b9c7', 'StarlightBilly.BodyA.Diffuse.2048')),
    ],
'30b6b9c7': [
        (log,                           ('2.8: StarlightBilly BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('be5165ce', 'StarlightBilly.BodyA.Diffuse.1024')),
    ],
'7ac1a66a': [
        (log,                           ('2.8: StarlightBilly BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('da2181cf', 'StarlightBilly.BodyA.LightMap.2048')),
    ],
'da2181cf': [
        (log,                           ('2.8: StarlightBilly BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('7ac1a66a', 'StarlightBilly.BodyA.LightMap.1024')),
    ],
'150df321': [
        (log,                           ('2.8: StarlightBilly BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d85dec5d', 'StarlightBilly.BodyA.MaterialMap.2048')),
    ],
'd85dec5d': [
        (log,                           ('2.8: StarlightBilly BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('150df321', 'StarlightBilly.BodyA.MaterialMap.1024')),
    ],

# === StarlightBilly Textures (LeftArmA) ===
'1d5dcd0a': [
        (log,                           ('2.8: StarlightBilly LeftArmA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('6fe50be9', 'StarlightBilly.LeftArmA.Diffuse.2048')),
    ],
'6fe50be9': [
        (log,                           ('2.8: StarlightBilly LeftArmA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('1d5dcd0a', 'StarlightBilly.LeftArmA.Diffuse.1024')),
    ],
'16d85b96': [
        (log,                           ('2.8: StarlightBilly LeftArmA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c0a681c1', 'StarlightBilly.LeftArmA.LightMap.2048')),
    ],
'c0a681c1': [
        (log,                           ('2.8: StarlightBilly LeftArmA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('16d85b96', 'StarlightBilly.LeftArmA.LightMap.1024')),
    ],
'02ac888a': [
        (log,                           ('2.8: StarlightBilly LeftArmA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('95454832', 'StarlightBilly.LeftArmA.MaterialMap.2048')),
    ],
'95454832': [
        (log,                           ('2.8: StarlightBilly LeftArmA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('02ac888a', 'StarlightBilly.LeftArmA.MaterialMap.1024')),
    ],

# === StarlightBilly Textures (TorsoA) ===
'a6ef0c74': [
        (log,                           ('2.8: StarlightBilly TorsoA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('d82e8cd7', 'StarlightBilly.TorsoA.Diffuse.2048')),
    ],
'd82e8cd7': [
        (log,                           ('2.8: StarlightBilly TorsoA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('a6ef0c74', 'StarlightBilly.TorsoA.Diffuse.1024')),
    ],
'6effa144': [
        (log,                           ('2.8: StarlightBilly TorsoA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('a28930f3', 'StarlightBilly.TorsoA.LightMap.2048')),
    ],
'a28930f3': [
        (log,                           ('2.8: StarlightBilly TorsoA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('6effa144', 'StarlightBilly.TorsoA.LightMap.1024')),
    ],
'744b53d4': [
        (log,                           ('2.8: StarlightBilly TorsoA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('f8f7fdbe', 'StarlightBilly.TorsoA.MaterialMap.2048')),
    ],
'f8f7fdbe': [
        (log,                           ('2.8: StarlightBilly TorsoA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('744b53d4', 'StarlightBilly.TorsoA.MaterialMap.1024')),
    ],

# === StarlightBilly Textures (MotorcycleA) ===
'd4aabf11': [
        (log,                           ('2.8: StarlightBilly MotorcycleA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('ed4bde0d', 'StarlightBilly.MotorcycleA.Diffuse.2048')),
    ],
'ed4bde0d': [
        (log,                           ('2.8: StarlightBilly MotorcycleA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('d4aabf11', 'StarlightBilly.MotorcycleA.Diffuse.1024')),
    ],
'5dc62b0b': [
        (log,                           ('2.8: StarlightBilly MotorcycleA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('573e87e3', 'StarlightBilly.MotorcycleA.LightMap.2048')),
    ],
'573e87e3': [
        (log,                           ('2.8: StarlightBilly MotorcycleA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('5dc62b0b', 'StarlightBilly.MotorcycleA.LightMap.1024')),
    ],
'81cd8366': [
        (log,                           ('2.8: StarlightBilly MotorcycleA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6b61b30c', 'StarlightBilly.MotorcycleA.MaterialMap.2048')),
    ],
'6b61b30c': [
        (log,                           ('2.8: StarlightBilly MotorcycleA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('81cd8366', 'StarlightBilly.MotorcycleA.MaterialMap.1024')),
    ],
'2182114e': [
        (log, ('3.0: StarlightBilly Hair VB Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'bedc10c4': [
        (log, ('3.0: StarlightBilly Hair VB Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'794d5c7b': [
        (log, ('3.0: StarlightBilly Hair VB Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'ff939fb7': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'b6e1da4b': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'b792110b': [
        (log, ('3.0: StarlightBilly Body VB Hash',)),
        (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'203e1a47': [
        (log, ('3.0: StarlightBilly Body VB Hash',)),
        (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'ccfa3c1f': [
        (log, ('3.0: StarlightBilly Body VB Hash',)),
        (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: StarlightBilly Body TEX Hash',)),
        (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'45992c18': [
        (log, ('3.0: StarlightBilly Torso VB Hash',)),
        (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
    ],
'97c35484': [
        (log, ('3.0: StarlightBilly Torso VB Hash',)),
        (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
    ],
'a829800f': [
        (log, ('3.0: StarlightBilly Torso VB Hash',)),
        (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
    ],
'0d842713': [
        (log, ('3.0: StarlightBilly LeftArm VB Hash',)),
        (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
    ],
'd4575d84': [
        (log, ('3.0: StarlightBilly LeftArm VB Hash',)),
        (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
    ],
'6d19734d': [
        (log, ('3.0: StarlightBilly LeftArm VB Hash',)),
        (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
    ],
'b5ba7f2c': [
        (log, ('3.0: StarlightBilly Collar VB Hash',)),
        (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
    ],
'6cbb0e03': [
        (log, ('3.0: StarlightBilly Collar VB Hash',)),
        (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
    ],
'0c780fde': [
        (log, ('3.0: StarlightBilly Collar VB Hash',)),
        (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
    ],
'169e16c1': [(log, ('3.0: StarlightBilly BackDecoration1 IB Hash',)), (add_ib_check_if_missing,)],
'730440ae': [
        (log, ('3.0: StarlightBilly BackDecoration1 VB Hash',)),
        (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
    ],
'9eda96ca': [
        (log, ('3.0: StarlightBilly BackDecoration1 VB Hash',)),
        (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
    ],
'02125c63': [
        (log, ('3.0: StarlightBilly BackDecoration1 VB Hash',)),
        (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
    ],
'14896011': [
        (log, ('3.0: StarlightBilly BackDecoration1 VB Hash',)),
        (add_section_if_missing, ('169e16c1', 'StarlightBilly.BackDecoration1.IB', 'match_priority = 0\n')),
    ],
'11727cec': [(log, ('3.0: StarlightBilly BackDecoration2 IB Hash',)), (add_ib_check_if_missing,)],
'93a9492c': [
        (log, ('3.0: StarlightBilly BackDecoration2 VB Hash',)),
        (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
    ],
'c9c3436f': [
        (log, ('3.0: StarlightBilly BackDecoration2 VB Hash',)),
        (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
    ],
'2f2f4055': [
        (log, ('3.0: StarlightBilly BackDecoration2 VB Hash',)),
        (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
    ],
'52225c15': [
        (log, ('3.0: StarlightBilly BackDecoration2 VB Hash',)),
        (add_section_if_missing, ('11727cec', 'StarlightBilly.BackDecoration2.IB', 'match_priority = 0\n')),
    ],
'a7516e2b': [
        (log, ('3.0: StarlightBilly Motorcycle VB Hash',)),
        (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'09439f49': [
        (log, ('3.0: StarlightBilly Motorcycle VB Hash',)),
        (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'5c3aba5b': [
        (log, ('3.0: StarlightBilly Motorcycle VB Hash',)),
        (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'd0ae2a77': [
        (log, ('3.0: StarlightBilly Face VB Hash',)),
        (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'7d045e09': [
        (log, ('3.0: StarlightBilly Face VB Hash',)),
        (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'be8fd496': [
        (log, ('3.0: StarlightBilly Face VB Hash',)),
        (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'9f671d6b': [(log, ('3.0: StarlightBilly Gun IB Hash',)), (add_ib_check_if_missing,)],
'ccd59cb9': [
        (log, ('3.0: StarlightBilly Gun VB Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'e2a3e69e': [
        (log, ('3.0: StarlightBilly Gun VB Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'dceb0608': [
        (log, ('3.0: StarlightBilly Gun VB Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'1f409c43': [
        (log, ('3.0: StarlightBilly Gun VB Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'3541c183': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'6f6aad09': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'11af0644': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'75f90347': [(log, ('3.0: StarlightBilly Weapon IB Hash',)), (add_ib_check_if_missing,)],
'cf21b035': [
        (log, ('3.0: StarlightBilly Weapon VB Hash',)),
        (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
    ],
'db0321a9': [
        (log, ('3.0: StarlightBilly Weapon VB Hash',)),
        (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
    ],
'bbe34d15': [
        (log, ('3.0: StarlightBilly Weapon VB Hash',)),
        (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
    ],
'6023cad8': [
        (log, ('3.0: StarlightBilly Weapon VB Hash',)),
        (add_section_if_missing, ('75f90347', 'StarlightBilly.Weapon.IB', 'match_priority = 0\n')),
    ],
'1ee52291': [(log, ('3.0: StarlightBilly WeaponAccessory1 IB Hash',)), (add_ib_check_if_missing,)],
'696bd946': [
        (log, ('3.0: StarlightBilly WeaponAccessory1 VB Hash',)),
        (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
    ],
'f293dadb': [
        (log, ('3.0: StarlightBilly WeaponAccessory1 VB Hash',)),
        (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
    ],
'804cf62d': [
        (log, ('3.0: StarlightBilly WeaponAccessory1 VB Hash',)),
        (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
    ],
'7b217048': [
        (log, ('3.0: StarlightBilly WeaponAccessory1 VB Hash',)),
        (add_section_if_missing, ('1ee52291', 'StarlightBilly.WeaponAccessory1.IB', 'match_priority = 0\n')),
    ],
'8f4285cd': [(log, ('3.0: StarlightBilly WeaponAccessory2 IB Hash',)), (add_ib_check_if_missing,)],
'f91227b7': [
        (log, ('3.0: StarlightBilly WeaponAccessory2 VB Hash',)),
        (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
    ],
'ce8c77da': [
        (log, ('3.0: StarlightBilly WeaponAccessory2 VB Hash',)),
        (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
    ],
'8190a48a': [
        (log, ('3.0: StarlightBilly WeaponAccessory2 VB Hash',)),
        (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
    ],
'131e5a0a': [
        (log, ('3.0: StarlightBilly WeaponAccessory2 VB Hash',)),
        (add_section_if_missing, ('8f4285cd', 'StarlightBilly.WeaponAccessory2.IB', 'match_priority = 0\n')),
    ],
'15ae37ae': [(log, ('3.0: StarlightBilly WeaponAccessory3 IB Hash',)), (add_ib_check_if_missing,)],
'84a7e817': [
        (log, ('3.0: StarlightBilly WeaponAccessory3 VB Hash',)),
        (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
    ],
'612b519c': [
        (log, ('3.0: StarlightBilly WeaponAccessory3 VB Hash',)),
        (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
    ],
'8a828eae': [
        (log, ('3.0: StarlightBilly WeaponAccessory3 VB Hash',)),
        (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
    ],
'fbf0b1bb': [
        (log, ('3.0: StarlightBilly WeaponAccessory3 VB Hash',)),
        (add_section_if_missing, ('15ae37ae', 'StarlightBilly.WeaponAccessory3.IB', 'match_priority = 0\n')),
    ],
'd3e8cd51': [(log, ('3.0: StarlightBilly WeaponAccessory4 IB Hash',)), (add_ib_check_if_missing,)],
'6ccff03a': [
        (log, ('3.0: StarlightBilly WeaponAccessory4 VB Hash',)),
        (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
    ],
'20ccc597': [
        (log, ('3.0: StarlightBilly WeaponAccessory4 VB Hash',)),
        (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
    ],
'4cfcbaf4': [
        (log, ('3.0: StarlightBilly WeaponAccessory4 VB Hash',)),
        (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
    ],
'82c72748': [
        (log, ('3.0: StarlightBilly WeaponAccessory4 VB Hash',)),
        (add_section_if_missing, ('d3e8cd51', 'StarlightBilly.WeaponAccessory4.IB', 'match_priority = 0\n')),
    ],
'6a6a1c79': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'2edbc842': [
        (log, ('3.0: StarlightBilly Hair TEX Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
'3a1ee1d7': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'4b0a8224': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'49782d36': [
        (log, ('3.0: StarlightBilly Gun TEX Hash',)),
        (add_section_if_missing, ('9f671d6b', 'StarlightBilly.Gun.IB', 'match_priority = 0\n')),
    ],
'eabcb930': [
        (log, ('3.0: StarlightBilly Face VB Hash',)),
        (add_section_if_missing, ('47be3135', 'StarlightBilly.Face.IB', 'match_priority = 0\n')),
    ],
'7a547ef8': [
        (log, ('3.0: StarlightBilly Motorcycle VB Hash',)),
        (add_section_if_missing, ('26d71d07', 'StarlightBilly.Motorcycle.IB', 'match_priority = 0\n')),
    ],
'b729d418': [
        (log, ('3.0: StarlightBilly Collar VB Hash',)),
        (add_section_if_missing, ('fed4432c', 'StarlightBilly.Collar.IB', 'match_priority = 0\n')),
    ],
'5a7ee5ae': [
        (log, ('3.0: StarlightBilly LeftArm VB Hash',)),
        (add_section_if_missing, ('85ec4f39', 'StarlightBilly.LeftArm.IB', 'match_priority = 0\n')),
    ],
'617a4f7c': [
        (log, ('3.0: StarlightBilly Torso VB Hash',)),
        (add_section_if_missing, ('b602e4de', 'StarlightBilly.Torso.IB', 'match_priority = 0\n')),
    ],
'c0d45183': [
        (log, ('3.0: StarlightBilly Body VB Hash',)),
        (add_section_if_missing, ('099cc55b', 'StarlightBilly.Body.IB', 'match_priority = 0\n')),
    ],
'0a1f876f': [
        (log, ('3.0: StarlightBilly Hair VB Hash',)),
        (add_section_if_missing, ('b126d40d', 'StarlightBilly.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'StarlightBilly',
    'game_versions': ['2.8'],
}
