"""
Sigrid Character Hash Commands
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
    Returns Sigrid's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'84618ee0': [
        (log,                           ('3.1: Sigrid Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'81e925ed': [
        (log,                           ('3.1: Sigrid HairShadow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b51bdd59': [
        (log,                           ('3.1: Sigrid Hairpin IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'64d7d56f': [
        (log,                           ('3.1: Sigrid Hairband IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'a23aa8a3': [
        (log,                           ('3.1: Sigrid Body IB Hash',)),
        (add_ib_check_if_missing,),
        (update_hash,                   ('38daef11',)),
    ],
'38daef11': [
        (log,                           ('3.1: Sigrid Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b20f90ea': [
        (log,                           ('3.1: Sigrid Leg IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'b30db54e': [
        (log,                           ('3.1: Sigrid Tail IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'454ff522': [
        (log,                           ('3.1: Sigrid Eyebrow IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'48625d6d': [
        (log,                           ('3.1: Sigrid Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'19086112': [
        (log,                           ('3.1: Sigrid Spear IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd892c658': [
        (log,                           ('3.1: Sigrid Rotor IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'add6ff13': [
        (log,                           ('3.1: Sigrid RotorBearing IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === VB Hashes ===
'840c1713': [
        (log,                           ('3.1: Sigrid Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],
'53d5d966': [
        (log,                           ('3.1: Sigrid Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],
'6b1c911c': [
        (log,                           ('3.1: Sigrid Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],
'380ee24b': [
        (log,                           ('3.1: Sigrid Hair VB Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],
'6a8ea608': [
        (log,                           ('3.1: Sigrid Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
    ],
'63981c38': [
        (log,                           ('3.1: Sigrid Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
    ],
'937473ae': [
        (log,                           ('3.1: Sigrid Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
    ],
'68bfe8f5': [
        (log,                           ('3.1: Sigrid Hairpin VB Hash',)),
        (add_section_if_missing, ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
    ],
'62a109a8': [
        (log,                           ('3.1: Sigrid Hairband VB Hash',)),
        (add_section_if_missing, ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
    ],
'3412aeb6': [
        (log,                           ('3.1: Sigrid Hairband VB Hash',)),
        (add_section_if_missing, ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
    ],
'951e896a': [
        (log,                           ('3.1: Sigrid Hairband VB Hash',)),
        (add_section_if_missing, ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
    ],
'228eb9d6': [
        (log,                           ('3.1: Sigrid Hairband VB Hash',)),
        (add_section_if_missing, ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
    ],
'01b35c45': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        (update_hash,                   ('d0bf0e87',)),
    ],
'08c15b45': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        (update_hash,                   ('e2a28287',)),
    ],
'f6474154': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        (update_hash,                   ('08ddaed3',)),
    ],
'8c0622d7': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        (update_hash,                   ('018ea72c',)),
    ],

'd0bf0e87': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],
'e2a28287': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],
'08ddaed3': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],
'018ea72c': [
        (log,                           ('3.1: Sigrid Body VB Hash',)),
        (add_section_if_missing, ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],
'dd9c8d5e': [
        (log,                           ('3.1: Sigrid Leg VB Hash',)),
        (add_section_if_missing, ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
    ],
'122883aa': [
        (log,                           ('3.1: Sigrid Leg VB Hash',)),
        (add_section_if_missing, ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
    ],
'5c0fefda': [
        (log,                           ('3.1: Sigrid Leg VB Hash',)),
        (add_section_if_missing, ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
    ],
'bf543990': [
        (log,                           ('3.1: Sigrid Leg VB Hash',)),
        (add_section_if_missing, ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
    ],
'cb72b377': [
        (log,                           ('3.1: Sigrid Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
    ],
'b3aeb830': [
        (log,                           ('3.1: Sigrid Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
    ],
'84ef2fb1': [
        (log,                           ('3.1: Sigrid Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
    ],
'710b43f7': [
        (log,                           ('3.1: Sigrid Tail VB Hash',)),
        (add_section_if_missing, ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
    ],
'9b76d1d7': [
        (log,                           ('3.1: Sigrid Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
    ],
'a1644290': [
        (log,                           ('3.1: Sigrid Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
    ],
'c90ff663': [
        (log,                           ('3.1: Sigrid Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
    ],
'e768b061': [
        (log,                           ('3.1: Sigrid Face VB Hash',)),
        (add_section_if_missing, ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
    ],
'0351cfca': [
        (log,                           ('3.1: Sigrid Spear VB Hash',)),
        (add_section_if_missing, ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
    ],
'72a71f98': [
        (log,                           ('3.1: Sigrid Spear VB Hash',)),
        (add_section_if_missing, ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
    ],
'9365ad01': [
        (log,                           ('3.1: Sigrid Spear VB Hash',)),
        (add_section_if_missing, ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
    ],
'9c60a66e': [
        (log,                           ('3.1: Sigrid Spear VB Hash',)),
        (add_section_if_missing, ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
    ],
'914dcde9': [
        (log,                           ('3.1: Sigrid Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
    ],
'fe91db45': [
        (log,                           ('3.1: Sigrid Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
    ],
'cd92341a': [
        (log,                           ('3.1: Sigrid Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
    ],
'0bacf856': [
        (log,                           ('3.1: Sigrid Rotor VB Hash',)),
        (add_section_if_missing, ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
    ],
'fab82e2f': [
        (log,                           ('3.1: Sigrid RotorBearing VB Hash',)),
        (add_section_if_missing, ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'3b09c896': [
        (log,                           ('3.1: Sigrid RotorBearing VB Hash',)),
        (add_section_if_missing, ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'ece3a3d2': [
        (log,                           ('3.1: Sigrid RotorBearing VB Hash',)),
        (add_section_if_missing, ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
    ],
'098fd9e8': [
        (log,                           ('3.1: Sigrid RotorBearing VB Hash',)),
        (add_section_if_missing, ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
    ],

# === Texture Hashes ===
'0c4bea0f': [
        (log,                           ('3.1: Sigrid Hair Diffuse TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'66dbe05f': [
        (log,                           ('3.1: Sigrid Hair Diffuse TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'da6a6f0b': [
        (log,                           ('3.1: Sigrid Hair LightMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'bc582555': [
        (log,                           ('3.1: Sigrid Hair LightMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'f5da0fcd': [
        (log,                           ('3.1: Sigrid Hair MaterialMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'd055f8e9': [
        (log,                           ('3.1: Sigrid Hair MaterialMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'ebac056e': [
        (log,                           ('3.1: Sigrid Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'798adba3': [
        (log,                           ('3.1: Sigrid Hair NormalMap TEX Hash',)),
        (add_section_if_missing, ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
    ],

'5b733af8': [
        (log,                           ('3.1: Sigrid Body Diffuse TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'037f456b': [
        (log,                           ('3.1: Sigrid Body Diffuse TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'13775170': [
        (log,                           ('3.1: Sigrid Body LightMap TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'a73e5eea': [
        (log,                           ('3.1: Sigrid Body LightMap TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'af950416': [
        (log,                           ('3.1: Sigrid Body MaterialMap TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'764b45ad': [
        (log,                           ('3.1: Sigrid Body MaterialMap TEX Hash',)),
        (add_section_if_missing, ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
    ],

'18b20f06': [
        (log,                           ('3.1: Sigrid Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('454ff522', 'Sigrid.Eyebrow.IB', 'match_priority = 0\n')),
    ],

'f178a6f2': [
        (log,                           ('3.1: Sigrid Eyebrow Diffuse TEX Hash',)),
        (add_section_if_missing, ('454ff522', 'Sigrid.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# Spear Diffuse
'2df6caf1': [
        (log,                           ('3.1: Sigrid Spear Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('f827c5f5', 'Sigrid.Spear.Diffuse.2048')),
    ],
'f827c5f5': [
        (log,                           ('3.1: Sigrid Spear Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('2df6caf1', 'Sigrid.Spear.Diffuse.1024')),
    ],

# Spear LightMap
'b85d4c23': [
        (log,                           ('3.1: Sigrid Spear LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('494a83dc', 'Sigrid.Spear.LightMap.2048')),
    ],
'494a83dc': [
        (log,                           ('3.1: Sigrid Spear LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('b85d4c23', 'Sigrid.Spear.LightMap.1024')),
    ],

# Spear MaterialMap
'648d17e4': [
        (log,                           ('3.1: Sigrid Spear MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('f30e1ce6', 'Sigrid.Spear.MaterialMap.2048')),
    ],
'f30e1ce6': [
        (log,                           ('3.1: Sigrid Spear MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('648d17e4', 'Sigrid.Spear.MaterialMap.1024')),
    ],

# Rotor Diffuse
'a58912ea': [
        (log,                           ('3.1: Sigrid Rotor Diffuse 1024p Hash',)),
        (multiply_section_if_missing, ('4fa99352', 'Sigrid.Rotor.Diffuse.2048')),
    ],
'4fa99352': [
        (log,                           ('3.1: Sigrid Rotor Diffuse 2048p Hash',)),
        (multiply_section_if_missing, ('a58912ea', 'Sigrid.Rotor.Diffuse.1024')),
    ],

# Rotor LightMap
'01f5701a': [
        (log,                           ('3.1: Sigrid Rotor LightMap 1024p Hash',)),
        (multiply_section_if_missing, ('980d9016', 'Sigrid.Rotor.LightMap.2048')),
    ],
'980d9016': [
        (log,                           ('3.1: Sigrid Rotor LightMap 2048p Hash',)),
        (multiply_section_if_missing, ('01f5701a', 'Sigrid.Rotor.LightMap.1024')),
    ],

# Rotor MaterialMap
'4ba54e3f': [
        (log,                           ('3.1: Sigrid Rotor MaterialMap 1024p Hash',)),
        (multiply_section_if_missing, ('1f036c21', 'Sigrid.Rotor.MaterialMap.2048')),
    ],
'1f036c21': [
        (log,                           ('3.1: Sigrid Rotor MaterialMap 2048p Hash',)),
        (multiply_section_if_missing, ('4ba54e3f', 'Sigrid.Rotor.MaterialMap.1024')),
    ],

'ffdc1ea7': [
        (log,                           ('3.1: Sigrid Rotor NormalMap TEX Hash',)),
        (add_section_if_missing, ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
    ],

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Sigrid',
    'game_versions': ['3.1'],
}
