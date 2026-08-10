"""
SigridMajesticWavechaser Character Hash Commands
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
    Returns SigridMajesticWavechaser's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'84618ee0': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'81e925ed': [
        (log,                           ('3.1: SigridMajesticWavechaser HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b51bdd59': [
        (log,                           ('3.1: SigridMajesticWavechaser Hairpin IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd9e49957': [
        (log,                           ('3.1: SigridMajesticWavechaser Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b30db54e': [
        (log,                           ('3.1: SigridMajesticWavechaser Tail IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'454ff522': [
        (log,                           ('3.1: SigridMajesticWavechaser Eyebrow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'48625d6d': [
        (log,                           ('3.1: SigridMajesticWavechaser Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'285aa61f': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd892c658': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b4f608f5': [
        (log,                           ('3.1: SigridMajesticWavechaser RotorBearing IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'840c1713': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],
'53d5d966': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],
'6b1c911c': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],
'380ee24b': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],
'6a8ea608': [
        (log,                           ('3.1: SigridMajesticWavechaser Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
    ],
'63981c38': [
        (log,                           ('3.1: SigridMajesticWavechaser Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
    ],
'937473ae': [
        (log,                           ('3.1: SigridMajesticWavechaser Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
    ],
'68bfe8f5': [
        (log,                           ('3.1: SigridMajesticWavechaser Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
    ],
'5f83ec60': [
        (log,                           ('3.1: SigridMajesticWavechaser Body VB Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],
'525d51d8': [
        (log,                           ('3.1: SigridMajesticWavechaser Body VB Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],
'9331668a': [
        (log,                           ('3.1: SigridMajesticWavechaser Body VB Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],
'4923328d': [
        (log,                           ('3.1: SigridMajesticWavechaser Body VB Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],
'cb72b377': [
        (log,                           ('3.1: SigridMajesticWavechaser Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
    ],
'b3aeb830': [
        (log,                           ('3.1: SigridMajesticWavechaser Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
    ],
'84ef2fb1': [
        (log,                           ('3.1: SigridMajesticWavechaser Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
    ],
'710b43f7': [
        (log,                           ('3.1: SigridMajesticWavechaser Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
    ],
'9b76d1d7': [
        (log,                           ('3.1: SigridMajesticWavechaser Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
    ],
'a1644290': [
        (log,                           ('3.1: SigridMajesticWavechaser Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
    ],
'c90ff663': [
        (log,                           ('3.1: SigridMajesticWavechaser Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
    ],
'e768b061': [
        (log,                           ('3.1: SigridMajesticWavechaser Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
    ],
'cc9f0724': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear VB Hash',)),
        (add_section_if_missing, ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
    ],
'f7f0b608': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear VB Hash',)),
        (add_section_if_missing, ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
    ],
'5ae0d9a1': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear VB Hash',)),
        (add_section_if_missing, ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
    ],
'830f0c5c': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear VB Hash',)),
        (add_section_if_missing, ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
    ],
'914dcde9': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
    ],
'fe91db45': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
    ],
'cd92341a': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
    ],
'0bacf856': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
    ],
'efe37d81': [
        (log,                           ('3.1: SigridMajesticWavechaser RotorBearing VB Hash',)),
        (add_section_if_missing, ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'513d615a': [
        (log,                           ('3.1: SigridMajesticWavechaser RotorBearing VB Hash',)),
        (add_section_if_missing, ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'f8153d33': [
        (log,                           ('3.1: SigridMajesticWavechaser RotorBearing VB Hash',)),
        (add_section_if_missing, ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'09f65e9d': [
        (log,                           ('3.1: SigridMajesticWavechaser RotorBearing VB Hash',)),
        (add_section_if_missing, ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
'0c4bea0f': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair Diffuse TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'66dbe05f': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair Diffuse TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'da6a6f0b': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair LightMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'bc582555': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair LightMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'f5da0fcd': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair MaterialMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'd055f8e9': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair MaterialMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'ebac056e': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: SigridMajesticWavechaser Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
    ],

'b07c43ef': [
        (log,                           ('3.1: SigridMajesticWavechaser Body Diffuse TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'82a7f32e': [
        (log,                           ('3.1: SigridMajesticWavechaser Body Diffuse TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'5e907c41': [
        (log,                           ('3.1: SigridMajesticWavechaser Body LightMap TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'1b4edd7b': [
        (log,                           ('3.1: SigridMajesticWavechaser Body LightMap TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'e104d477': [
        (log,                           ('3.1: SigridMajesticWavechaser Body MaterialMap TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'aa626489': [
        (log,                           ('3.1: SigridMajesticWavechaser Body MaterialMap TEX Hash',)),
        (add_section_if_missing, ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
    ],

'18b20f06': [
        (log,                           ('3.1: SigridMajesticWavechaser Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('454ff522', 'SigridMajesticWavechaser.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'f178a6f2': [
        (log,                           ('3.1: SigridMajesticWavechaser Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('454ff522', 'SigridMajesticWavechaser.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# Spear Diffuse
'98a57712': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('ec9c1ac4', 'SigridMajesticWavechaser.Spear.Diffuse.2048')),
    ],
'ec9c1ac4': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('98a57712', 'SigridMajesticWavechaser.Spear.Diffuse.1024')),
    ],

# Spear LightMap
'6c9142f7': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('3da2b650', 'SigridMajesticWavechaser.Spear.LightMap.2048')),
    ],
'3da2b650': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('6c9142f7', 'SigridMajesticWavechaser.Spear.LightMap.1024')),
    ],

# Spear MaterialMap
'e1240523': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('1521edda', 'SigridMajesticWavechaser.Spear.MaterialMap.2048')),
    ],
'1521edda': [
        (log,                           ('3.1: SigridMajesticWavechaser Spear MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('e1240523', 'SigridMajesticWavechaser.Spear.MaterialMap.1024')),
    ],

# Rotor Diffuse
'a58912ea': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('4fa99352', 'SigridMajesticWavechaser.Rotor.Diffuse.2048')),
    ],
'4fa99352': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('a58912ea', 'SigridMajesticWavechaser.Rotor.Diffuse.1024')),
    ],

# Rotor LightMap
'01f5701a': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('980d9016', 'SigridMajesticWavechaser.Rotor.LightMap.2048')),
    ],
'980d9016': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('01f5701a', 'SigridMajesticWavechaser.Rotor.LightMap.1024')),
    ],

# Rotor MaterialMap
'4ba54e3f': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('1f036c21', 'SigridMajesticWavechaser.Rotor.MaterialMap.2048')),
    ],
'1f036c21': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('4ba54e3f', 'SigridMajesticWavechaser.Rotor.MaterialMap.1024')),
    ],

'ffdc1ea7': [
        (log,                           ('3.1: SigridMajesticWavechaser Rotor NormalMap TEX Hash',)),
        (add_section_if_missing, ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'SigridMajesticWavechaser',
    'game_versions': ['3.1'],
}
