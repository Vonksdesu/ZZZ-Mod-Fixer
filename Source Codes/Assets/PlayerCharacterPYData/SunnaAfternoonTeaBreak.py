"""
SunnaAfternoonTeaBreak Character Hash Commands
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
    Returns SunnaAfternoonTeaBreak's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'ee17c9a2': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'6cc4d486': [
        (log,                           ('2.6 -> 2.7: SunnaAfternoonTeaBreak Hair IB Hash',)),
        (update_hash,                        ('a6d82ba5',)),
    ],
'a6d82ba5': [
        (log,                           ('2.7: SunnaAfternoonTeaBreak Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === SunnaAfternoonTeaBreak Textures (HairA) ===
'8de1219d': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('e5acd978', 'SunnaAfternoonTeaBreak.HairA.Diffuse.2048')),
    ],
'e5acd978': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('8de1219d', 'SunnaAfternoonTeaBreak.HairA.Diffuse.1024')),
    ],
'9795e08f': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('87ce81a5', 'SunnaAfternoonTeaBreak.HairA.LightMap.2048')),
    ],
'87ce81a5': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('9795e08f', 'SunnaAfternoonTeaBreak.HairA.LightMap.1024')),
    ],
'f240844c': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('5ae5a95b', 'SunnaAfternoonTeaBreak.HairA.MaterialMap.2048')),
    ],
'5ae5a95b': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('f240844c', 'SunnaAfternoonTeaBreak.HairA.MaterialMap.1024')),
    ],

# === SunnaAfternoonTeaBreak Textures (BodyA) ===
'5715ebbe': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('db757608', 'SunnaAfternoonTeaBreak.BodyA.Diffuse.2048')),
    ],
'db757608': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('5715ebbe', 'SunnaAfternoonTeaBreak.BodyA.Diffuse.1024')),
    ],
'335f4f3e': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c9724602', 'SunnaAfternoonTeaBreak.BodyA.LightMap.2048')),
    ],
'c9724602': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('335f4f3e', 'SunnaAfternoonTeaBreak.BodyA.LightMap.1024')),
    ],
'68807c0b': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('719036d1', 'SunnaAfternoonTeaBreak.BodyA.MaterialMap.2048')),
    ],
'719036d1': [
        (log,                           ('2.6: SunnaAfternoonTeaBreak BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('68807c0b', 'SunnaAfternoonTeaBreak.BodyA.MaterialMap.1024')),
    ],
'327644ee': [(log, ('2.6 -> 2.7: ChinatsuSkin Hair Position Hash',)), (update_hash, ('4b93d8eb',))],
'4b93d8eb': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair VB Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'5e70dde6': [(log, ('2.6 -> 2.7: ChinatsuSkin Hair Texcoord Hash',)), (update_hash, ('b9030f86',))],
'b9030f86': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair VB Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'79de92c7': [(log, ('2.6 -> 2.7: ChinatsuSkin Hair Blend Hash',)),    (update_hash, ('4a795f2a',))],
'4a795f2a': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair VB Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'2fcfee64': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'8cd786f7': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'3f11dfd9': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'4803b5d7': [(log, ('3.0: SunnaAfternoonTeaBreak Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'7353a665': [
        (log, ('3.0: SunnaAfternoonTeaBreak Body VB Hash',)),
        (add_section_if_missing, ('ee17c9a2', 'SunnaAfternoonTeaBreak.Body.IB', 'match_priority = 0\n')),
    ],
'c77b3235': [(log, ('2.6 -> 2.7: ChinatsuSkin Body Position Hash',)), (update_hash, ('25cf6bf7',))],
'25cf6bf7': [
        (log, ('3.0: SunnaAfternoonTeaBreak Body VB Hash',)),
        (add_section_if_missing, ('ee17c9a2', 'SunnaAfternoonTeaBreak.Body.IB', 'match_priority = 0\n')),
    ],
'0c6b95ca': [(log, ('2.6 -> 2.7: ChinatsuSkin Body Texcoord Hash',)), (update_hash, ('7a31eb8b',))],
'7a31eb8b': [
        (log, ('3.0: SunnaAfternoonTeaBreak Body VB Hash',)),
        (add_section_if_missing, ('ee17c9a2', 'SunnaAfternoonTeaBreak.Body.IB', 'match_priority = 0\n')),
    ],
'9b65412a': [
        (log, ('3.0: SunnaAfternoonTeaBreak Body VB Hash',)),
        (add_section_if_missing, ('ee17c9a2', 'SunnaAfternoonTeaBreak.Body.IB', 'match_priority = 0\n')),
    ],
'30ea5791': [(log, ('3.0: SunnaAfternoonTeaBreak Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'9f0ab8cd': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'a5182b8a': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'e3cc1981': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'f5daa764': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow VB Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'c9b5c6ce': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow TEX Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'1a2c8573': [(log, ('3.0: SunnaAfternoonTeaBreak Face IB Hash',)), (add_ib_check_if_missing,)],
'9679c257': [
        (log, ('3.0: SunnaAfternoonTeaBreak Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'SunnaAfternoonTeaBreak.Face.IB', 'match_priority = 0\n')),
    ],
'ac6b5110': [
        (log, ('3.0: SunnaAfternoonTeaBreak Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'SunnaAfternoonTeaBreak.Face.IB', 'match_priority = 0\n')),
    ],
'506dc9e1': [
        (log, ('3.0: SunnaAfternoonTeaBreak Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'SunnaAfternoonTeaBreak.Face.IB', 'match_priority = 0\n')),
    ],
'21299f88': [
        (log, ('3.0: SunnaAfternoonTeaBreak Face VB Hash',)),
        (add_section_if_missing, ('1a2c8573', 'SunnaAfternoonTeaBreak.Face.IB', 'match_priority = 0\n')),
    ],
'337a62c1': [(log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip IB Hash',)), (add_ib_check_if_missing,)],
'953975c0': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'a28ba31c': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'b642db41': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'16e2d8ea': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip VB Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'ad73df94': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'39dac70b': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'95070f7f': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'07a82c9c': [(log, ('3.0: SunnaAfternoonTeaBreak Paopao IB Hash',)), (add_ib_check_if_missing,)],
'ffe207d5': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'1a0cad46': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'df0f6142': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'd4e13802': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao VB Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'7d8ac131': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'5c5b6aad': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'3c4378db': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'e85201e7': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'a2b36369': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'ab3c12c0': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair TEX Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
'1ef66a60': [
        (log, ('3.0: SunnaAfternoonTeaBreak Eyebrow TEX Hash',)),
        (add_section_if_missing, ('30ea5791', 'SunnaAfternoonTeaBreak.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'37f00c45': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'9368a6f9': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'508c297c': [
        (log, ('3.0: SunnaAfternoonTeaBreak WeaponBackpackCharmGrip TEX Hash',)),
        (add_section_if_missing, ('337a62c1', 'SunnaAfternoonTeaBreak.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
    ],
'be5cd451': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'945afd67': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'e9783f84': [
        (log, ('3.0: SunnaAfternoonTeaBreak Paopao TEX Hash',)),
        (add_section_if_missing, ('07a82c9c', 'SunnaAfternoonTeaBreak.Paopao.IB', 'match_priority = 0\n')),
    ],
'22c82346': [(log, ('2.6 -> 2.7: ChinatsuSkin Hair Draw Hash',)),     (update_hash, ('74cc56df',))],
'74cc56df': [
        (log, ('3.0: SunnaAfternoonTeaBreak Hair VB Hash',)),
        (add_section_if_missing, ('a6d82ba5', 'SunnaAfternoonTeaBreak.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'SunnaAfternoonTeaBreak',
    'aliases': ['ChinatsuSkin', '千夏-皮肤'],
    'game_versions': ['2.6', '2.7'],
}

