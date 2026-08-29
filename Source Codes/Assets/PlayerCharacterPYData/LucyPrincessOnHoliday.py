"""
LucyPrincessOnHoliday Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.1
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns LucyPrincessOnHoliday's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'ba402095': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'f7d74190': [
        (log,                           ('3.1: LucyPrincessOnHoliday HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'7cec7c94': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'30abbad1': [
        (log,                           ('3.1: LucyPrincessOnHoliday Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'df3e3965': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd1e02a54': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'c136d7d8': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair VB Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],
'84dd6eaa': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair VB Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],
'bb60ba2a': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair VB Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],
'0a0ef4ca': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair VB Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],
'eae29c24': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat VB Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],
'9ef15072': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat VB Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],
'7a606e17': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat VB Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],
'c692080c': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat VB Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],
'ac5acb2d': [
        (log,                           ('3.1: LucyPrincessOnHoliday Body VB Hash',)),
        (add_section_if_missing, ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
    ],
'd31f22c6': [
        (log,                           ('3.1: LucyPrincessOnHoliday Body VB Hash',)),
        (add_section_if_missing, ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
    ],
'38a28e54': [
        (log,                           ('3.1: LucyPrincessOnHoliday Body VB Hash',)),
        (add_section_if_missing, ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
    ],
'0c802011': [
        (log,                           ('3.1: LucyPrincessOnHoliday Body VB Hash',)),
        (add_section_if_missing, ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
    ],
'2db957ac': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face VB Hash',)),
        (add_section_if_missing, ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
    ],
'17abc4eb': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face VB Hash',)),
        (add_section_if_missing, ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
    ],
'e78a4ee2': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face VB Hash',)),
        (add_section_if_missing, ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
    ],
'a2054778': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face VB Hash',)),
        (add_section_if_missing, ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
    ],
'2bbcadde': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon VB Hash',)),
        (add_section_if_missing, ('d1e02a54', 'LucyPrincessOnHoliday.Weapon.IB', 'match_priority = 0\n')),
    ],
'94c22510': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon VB Hash',)),
        (add_section_if_missing, ('d1e02a54', 'LucyPrincessOnHoliday.Weapon.IB', 'match_priority = 0\n')),
    ],
'98dfc0a3': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon VB Hash',)),
        (add_section_if_missing, ('d1e02a54', 'LucyPrincessOnHoliday.Weapon.IB', 'match_priority = 0\n')),
    ],
'0456e606': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon VB Hash',)),
        (add_section_if_missing, ('d1e02a54', 'LucyPrincessOnHoliday.Weapon.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
# Hair Diffuse
'753baa45': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('0fa60fe1', 'LucyPrincessOnHoliday.Hair.Diffuse.2048')),
    ],
'0fa60fe1': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('753baa45', 'LucyPrincessOnHoliday.Hair.Diffuse.1024')),
    ],

# Hair LightMap
'810c0878': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('1a3b30ba', 'LucyPrincessOnHoliday.Hair.LightMap.2048')),
    ],
'1a3b30ba': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('810c0878', 'LucyPrincessOnHoliday.Hair.LightMap.1024')),
    ],

# Hair MaterialMap
'368f931c': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('068aba7f', 'LucyPrincessOnHoliday.Hair.MaterialMap.2048')),
    ],
'068aba7f': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('368f931c', 'LucyPrincessOnHoliday.Hair.MaterialMap.1024')),
    ],

'ebac056e': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
    ],

'2cac44c0': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat Diffuse TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

'4901de52': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat Diffuse TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

'8d155fc7': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat LightMap TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

'ca69aa34': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat LightMap TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

'e96ce933': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat MaterialMap TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

'fdf85374': [
        (log,                           ('3.1: LucyPrincessOnHoliday Hat MaterialMap TEX Hash',)),
        (add_section_if_missing, ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
    ],

# Face Diffuse
'2578d35b': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('4e2d5baa', 'LucyPrincessOnHoliday.Face.Diffuse.2048')),
    ],
'4e2d5baa': [
        (log,                           ('3.1: LucyPrincessOnHoliday Face Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('2578d35b', 'LucyPrincessOnHoliday.Face.Diffuse.1024')),
    ],

# Weapon Diffuse
'78f83ff4': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('e1f0071b', 'LucyPrincessOnHoliday.Weapon.Diffuse.2048')),
    ],
'e1f0071b': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('78f83ff4', 'LucyPrincessOnHoliday.Weapon.Diffuse.1024')),
    ],

# Weapon LightMap
'9b4b3ffa': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('bc9df18b', 'LucyPrincessOnHoliday.Weapon.LightMap.2048')),
    ],
'bc9df18b': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('9b4b3ffa', 'LucyPrincessOnHoliday.Weapon.LightMap.1024')),
    ],

# Weapon MaterialMap
'acaa0bf6': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('a962e9eb', 'LucyPrincessOnHoliday.Weapon.MaterialMap.2048')),
    ],
'a962e9eb': [
        (log,                           ('3.1: LucyPrincessOnHoliday Weapon MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('acaa0bf6', 'LucyPrincessOnHoliday.Weapon.MaterialMap.1024')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'LucyPrincessOnHoliday',
    'game_versions': ['3.1'],
}
