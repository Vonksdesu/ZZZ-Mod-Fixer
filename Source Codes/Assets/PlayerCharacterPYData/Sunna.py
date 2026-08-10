"""
Sunna Character Hash Commands
ZZZ Mod Fixer v2.6
Game Version: 2.6
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Sunna's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'337a62c1': [
        (log,                           ('2.6: Sunna BagCharm IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b3c6ea5a': [
        (log,                           ('2.6: Sunna Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'1a2c8573': [
        (log,                           ('2.6: Sunna Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'904ecd0f': [
        (log,                           ('2.6: Sunna Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'e7a17172': [
        (log,                           ('2.6: Sunna Paopao IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'07a82c9c': [
        (log,                           ('2.6: Sunna PaopaoA IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === Sunna Textures (FaceA) ===
'1ef66a60': [
        (log,                           ('2.6: Sunna FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('c9b5c6ce', 'Sunna.FaceA.Diffuse.2048')),
    ],
'c9b5c6ce': [
        (log,                           ('2.6: Sunna FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('1ef66a60', 'Sunna.FaceA.Diffuse.1024')),
    ],

# === Sunna Textures (HairA) ===
'e85201e7': [
        (log,                           ('2.6: Sunna HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('2fcfee64', 'Sunna.HairA.Diffuse.2048')),
    ],
'2fcfee64': [
        (log,                           ('2.6: Sunna HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('e85201e7', 'Sunna.HairA.Diffuse.1024')),
    ],
'a2b36369': [
        (log,                           ('2.6: Sunna HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('8cd786f7', 'Sunna.HairA.LightMap.2048')),
    ],
'8cd786f7': [
        (log,                           ('2.6: Sunna HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('a2b36369', 'Sunna.HairA.LightMap.1024')),
    ],
'ab3c12c0': [
        (log,                           ('2.6: Sunna HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('3f11dfd9', 'Sunna.HairA.MaterialMap.2048')),
    ],
'3f11dfd9': [
        (log,                           ('2.6: Sunna HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('ab3c12c0', 'Sunna.HairA.MaterialMap.1024')),
    ],

# === Sunna Textures (BodyA) ===
'aa0f48fe': [
        (log,                           ('2.6: Sunna BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('f051c211', 'Sunna.BodyA.Diffuse.2048')),
    ],
'f051c211': [
        (log,                           ('2.6: Sunna BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('aa0f48fe', 'Sunna.BodyA.Diffuse.1024')),
    ],
'3987c8c2': [
        (log,                           ('2.6: Sunna BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('4aca364a', 'Sunna.BodyA.LightMap.2048')),
    ],
'4aca364a': [
        (log,                           ('2.6: Sunna BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('3987c8c2', 'Sunna.BodyA.LightMap.1024')),
    ],
'1d459d73': [
        (log,                           ('2.6: Sunna BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('f3f8895c', 'Sunna.BodyA.MaterialMap.2048')),
    ],
'f3f8895c': [
        (log,                           ('2.6: Sunna BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('1d459d73', 'Sunna.BodyA.MaterialMap.1024')),
    ],

# === Sunna Textures (BagCharmA) ===
'bde1bdad': [
        (log,                           ('2.6: Sunna BagCharmA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('6c04b56d', 'Sunna.BagCharmA.Diffuse.2048')),
    ],
'6c04b56d': [
        (log,                           ('2.6: Sunna BagCharmA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('bde1bdad', 'Sunna.BagCharmA.Diffuse.1024')),
    ],
'9368a6f9': [
        (log,                           ('2.6: Sunna BagCharmA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('39dac70b', 'Sunna.BagCharmA.LightMap.2048')),
    ],
'39dac70b': [
        (log,                           ('2.6: Sunna BagCharmA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('9368a6f9', 'Sunna.BagCharmA.LightMap.1024')),
    ],
'508c297c': [
        (log,                           ('2.6: Sunna BagCharmA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('95070f7f', 'Sunna.BagCharmA.MaterialMap.2048')),
    ],
'95070f7f': [
        (log,                           ('2.6: Sunna BagCharmA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('508c297c', 'Sunna.BagCharmA.MaterialMap.1024')),
    ],

# === Sunna Textures (PaopaoA) ===
'be5cd451': [
        (log,                           ('2.6: Sunna PaopaoA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('7d8ac131', 'Sunna.PaopaoA.Diffuse.2048')),
    ],
'7d8ac131': [
        (log,                           ('2.6: Sunna PaopaoA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('be5cd451', 'Sunna.PaopaoA.Diffuse.1024')),
    ],
'945afd67': [
        (log,                           ('2.6: Sunna PaopaoA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('5c5b6aad', 'Sunna.PaopaoA.LightMap.2048')),
    ],
'5c5b6aad': [
        (log,                           ('2.6: Sunna PaopaoA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('945afd67', 'Sunna.PaopaoA.LightMap.1024')),
    ],
'e9783f84': [
        (log,                           ('2.6: Sunna PaopaoA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('3c4378db', 'Sunna.PaopaoA.MaterialMap.2048')),
    ],
'3c4378db': [
        (log,                           ('2.6: Sunna PaopaoA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('e9783f84', 'Sunna.PaopaoA.MaterialMap.1024')),
    ],
'5c030eea': [
        (log, ('3.0: Sunna Hair VB Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'06bea24e': [
        (log, ('3.0: Sunna Hair VB Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'0c183c3f': [
        (log, ('3.0: Sunna Hair VB Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Sunna Hair TEX Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'3ab6d438': [(log, ('3.0: Sunna Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'8991360f': [
        (log, ('3.0: Sunna Body VB Hash',)),
        (add_section_if_missing, ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'6eb68b62': [
        (log, ('3.0: Sunna Body VB Hash',)),
        (add_section_if_missing, ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'712eb020': [
        (log, ('3.0: Sunna Body VB Hash',)),
        (add_section_if_missing, ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'53661c9a': [
        (log, ('3.0: Sunna Body VB Hash',)),
        (add_section_if_missing, ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
    ],
'30ea5791': [(log, ('3.0: Sunna Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'9f0ab8cd': [
        (log, ('3.0: Sunna Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'a5182b8a': [
        (log, ('3.0: Sunna Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'e3cc1981': [
        (log, ('3.0: Sunna Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f5daa764': [
        (log, ('3.0: Sunna Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'ac6b5110': [
        (log, ('3.0: Sunna Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
    ],
'506dc9e1': [
        (log, ('3.0: Sunna Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
    ],
'21299f88': [
        (log, ('3.0: Sunna Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
    ],
'0b9bd38f': [(log, ('3.0: Sunna DisplayScreen IB Hash',)), (add_ib_check_if_missing,)],
'dd676093': [
        (log, ('3.0: Sunna DisplayScreen VB Hash',)),
        (add_section_if_missing, ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
    ],
'6f7ae47c': [
        (log, ('3.0: Sunna DisplayScreen VB Hash',)),
        (add_section_if_missing, ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
    ],
'541d5b0f': [
        (log, ('3.0: Sunna DisplayScreen VB Hash',)),
        (add_section_if_missing, ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
    ],
'2ef8be58': [
        (log, ('3.0: Sunna DisplayScreen VB Hash',)),
        (add_section_if_missing, ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
    ],
'a28ba31c': [
        (log, ('3.0: Sunna WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'b642db41': [
        (log, ('3.0: Sunna WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'16e2d8ea': [
        (log, ('3.0: Sunna WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'3a7143a6': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('e7a17172', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'62519e38': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('e7a17172', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'38e2fe9f': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('e7a17172', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'df0f6142': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'd4e13802': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'c811c294': [(log, ('3.0: Sunna Weapon IB Hash',)), (add_ib_check_if_missing,)],
'6cbdb4d3': [
        (log, ('3.0: Sunna Weapon VB Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'9220fbd5': [
        (log, ('3.0: Sunna Weapon VB Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'5d7fdc2e': [
        (log, ('3.0: Sunna Weapon VB Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'4b46dfdc': [
        (log, ('3.0: Sunna Weapon VB Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'003c6497': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'4b4975a2': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'635f5cc9': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'0a237cd3': [(log, ('3.0: Sunna WeaponDecoration IB Hash',)), (add_ib_check_if_missing,)],
'dab9d122': [
        (log, ('3.0: Sunna WeaponDecoration VB Hash',)),
        (add_section_if_missing, ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
    ],
'0a41bae7': [
        (log, ('3.0: Sunna WeaponDecoration VB Hash',)),
        (add_section_if_missing, ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
    ],
'34dc63b4': [
        (log, ('3.0: Sunna WeaponDecoration VB Hash',)),
        (add_section_if_missing, ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
    ],
'a5ecc7ea': [
        (log, ('3.0: Sunna WeaponDecoration VB Hash',)),
        (add_section_if_missing, ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
    ],
'8ad8f57d': [(log, ('3.0: Sunna WeaponDecoration2 IB Hash',)), (add_ib_check_if_missing,)],
'84a9dfca': [
        (log, ('3.0: Sunna WeaponDecoration2 VB Hash',)),
        (add_section_if_missing, ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
    ],
'81321ee9': [
        (log, ('3.0: Sunna WeaponDecoration2 VB Hash',)),
        (add_section_if_missing, ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
    ],
'33a66c47': [
        (log, ('3.0: Sunna WeaponDecoration2 VB Hash',)),
        (add_section_if_missing, ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
    ],
'0d2178c5': [
        (log, ('3.0: Sunna WeaponDecoration2 VB Hash',)),
        (add_section_if_missing, ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Sunna Hair TEX Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
'b9d9b7a7': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'6c369f22': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'15cd94f7': [
        (log, ('3.0: Sunna Weapon TEX Hash',)),
        (add_section_if_missing, ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
    ],
'1a0cad46': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'ffe207d5': [
        (log, ('3.0: Sunna paopao VB Hash',)),
        (add_section_if_missing, ('e7a17172', 'Sunna.paopao.IB', 'match_priority = 0\n')),
    ],
'953975c0': [
        (log, ('3.0: Sunna WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'9679c257': [
        (log, ('3.0: Sunna Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
    ],
'cc070c66': [
        (log, ('3.0: Sunna Hair VB Hash',)),
        (add_section_if_missing, ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Sunna',
    'aliases': ['Chinatsu', '千夏'],
    'game_versions': ['2.6'],
}
