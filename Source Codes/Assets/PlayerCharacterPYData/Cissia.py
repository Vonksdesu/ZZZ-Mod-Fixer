"""
Cissia Character Hash Commands
ZZZ Mod Fixer v2.7
Game Version: 2.7
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Cissia's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'ff2ec4d6': [
        (log,                           ('2.7: Cissia Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd1a31f0b': [
        (log,                           ('2.7: Cissia Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'e4785f80': [
        (log,                           ('2.7: Cissia Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'4c11c155': [
        (log,                           ('2.7: Cissia Tail IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Cissia Textures (FaceA) ===
'c72539cd': [
        (log,                           ('2.7: Cissia FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,    ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8f55186a', 'Cissia.FaceA.Diffuse.2048')),
    ],
'8f55186a': [
        (log,                           ('2.7: Cissia FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,    ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c72539cd', 'Cissia.FaceA.Diffuse.1024')),
    ],

# === Cissia Textures (BodyA) ===
'2638fa23': [
        (log,                           ('2.7: Cissia BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('fcfeb117', 'Cissia.BodyA.Diffuse.2048')),
    ],
'fcfeb117': [
        (log,                           ('2.7: Cissia BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('2638fa23', 'Cissia.BodyA.Diffuse.1024')),
    ],
'4862ab5d': [
        (log,                           ('2.7: Cissia BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('2b6d5c26', 'Cissia.BodyA.LightMap.2048')),
    ],
'2b6d5c26': [
        (log,                           ('2.7: Cissia BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('4862ab5d', 'Cissia.BodyA.LightMap.1024')),
    ],
'b0a060f2': [
        (log,                           ('2.7: Cissia BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e5edf7dd', 'Cissia.BodyA.MaterialMap.2048')),
    ],
'e5edf7dd': [
        (log,                           ('2.7: Cissia BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('b0a060f2', 'Cissia.BodyA.MaterialMap.1024')),
    ],

# === Cissia Textures (BodyB) ===
'9aa301f1': [
        (log,                           ('2.7: Cissia BodyB Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('b39896c4', 'Cissia.BodyB.Diffuse.2048')),
    ],
'b39896c4': [
        (log,                           ('2.7: Cissia BodyB Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('9aa301f1', 'Cissia.BodyB.Diffuse.1024')),
    ],
'0c2d5ee2': [
        (log,                           ('2.7: Cissia BodyB LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('31674c56', 'Cissia.BodyB.LightMap.2048')),
    ],
'31674c56': [
        (log,                           ('2.7: Cissia BodyB LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('0c2d5ee2', 'Cissia.BodyB.LightMap.1024')),
    ],
'64a85915': [
        (log,                           ('2.7: Cissia BodyB MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('abb852a0', 'Cissia.BodyB.MaterialMap.2048')),
    ],
'abb852a0': [
        (log,                           ('2.7: Cissia BodyB MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('64a85915', 'Cissia.BodyB.MaterialMap.1024')),
    ],

# === Cissia Textures (BodyC) ===
'f5ecd616': [
        (log,                           ('2.7 -> 2.8: Cissia BodyC Diffuse 1024p Hash',)),
        (update_hash,                        ('6d861173',)),
    ],
'6d861173': [
        (log,                           ('2.7: Cissia BodyC Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        (('f8739729', 'ec85e98d'), 'Cissia.BodyC.Diffuse.2048')),
    ],
'f8739729': [
        (log,                           ('2.7 -> 2.8: Cissia BodyC Diffuse 2048p Hash',)),
        (update_hash,                        ('ec85e98d',)),
    ],
'ec85e98d': [
        (log,                           ('2.7: Cissia BodyC Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        (('f5ecd616', '6d861173'), 'Cissia.BodyC.Diffuse.1024')),
    ],
'090684bd': [
        (log,                           ('2.7: Cissia BodyC LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6fadb6f5', 'Cissia.BodyC.LightMap.2048')),
    ],
'6fadb6f5': [
        (log,                           ('2.7: Cissia BodyC LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('090684bd', 'Cissia.BodyC.LightMap.1024')),
    ],
'd59dc29c': [
        (log,                           ('2.7: Cissia BodyC MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('1d5d53cd', 'Cissia.BodyC.MaterialMap.2048')),
    ],
'1d5d53cd': [
        (log,                           ('2.7: Cissia BodyC MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('d59dc29c', 'Cissia.BodyC.MaterialMap.1024')),
    ],
'639456c7': [
        (log, ('3.0: Cissia Hair VB Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'a36d2401': [
        (log, ('3.0: Cissia Hair VB Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'b93219f1': [
        (log, ('3.0: Cissia Hair VB Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Cissia Hair TEX Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'8f34fc78': [(log, ('3.0: Cissia Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'e5ced7d5': [(log, ('3.0: Cissia Tongue IB Hash',)), (add_ib_check_if_missing,)],
'a3b04e84': [
        (log, ('3.0: Cissia Tongue VB Hash',)),
        (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
    ],
'3e82033f': [
        (log, ('3.0: Cissia Tongue VB Hash',)),
        (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
    ],
'32f6d33a': [
        (log, ('3.0: Cissia Tongue VB Hash',)),
        (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
    ],
'c3082752': [
        (log, ('3.0: Cissia Tongue VB Hash',)),
        (add_section_if_missing, ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
    ],
'1a95227f': [
        (log, ('3.0: Cissia Body VB Hash',)),
        (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'e6527ff0': [
        (log, ('3.0: Cissia Body VB Hash',)),
        (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'3b944072': [
        (log, ('3.0: Cissia Body VB Hash',)),
        (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'efed0e09': [
        (log, ('3.0: Cissia Tail VB Hash',)),
        (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
    ],
'8f017202': [
        (log, ('3.0: Cissia Tail VB Hash',)),
        (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
    ],
'90634c3b': [
        (log, ('3.0: Cissia Tail VB Hash',)),
        (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
    ],
'7c01dc6b': [(log, ('3.0: Cissia Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'6e02f849': [
        (log, ('2.8: Cissia Eyebrow draw_vb Hash',)),
        (add_section_if_missing, ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'8b927127': [
        (log, ('2.8: Cissia Eyebrow position_vb Hash',)),
        (add_section_if_missing, ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'cd87eb81': [
        (log, ('2.8: Cissia Eyebrow texcoord_vb Hash',)),
        (add_section_if_missing, ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'09fa4349': [
        (log, ('2.8: Cissia Eyebrow blend_vb Hash',)),
        (add_section_if_missing, ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'a2d2a224': [
        (log, ('3.0: Cissia Face VB Hash',)),
        (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
    ],
'98c03163': [
        (log, ('3.0: Cissia Face VB Hash',)),
        (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
    ],
'dfc76798': [
        (log, ('3.0: Cissia Face VB Hash',)),
        (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
    ],
'ed3245f0': [
        (log, ('3.0: Cissia Face VB Hash',)),
        (add_section_if_missing, ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
    ],
'29b5b0b0': [(log, ('3.0: Cissia SpearHandle IB Hash',)), (add_ib_check_if_missing,)],
'9af3bf00': [
        (log, ('3.0: Cissia SpearHandle VB Hash',)),
        (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
    ],
'dee92405': [
        (log, ('3.0: Cissia SpearHandle VB Hash',)),
        (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
    ],
'880e958d': [
        (log, ('3.0: Cissia SpearHandle VB Hash',)),
        (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
    ],
'6354dee4': [
        (log, ('3.0: Cissia SpearHandle VB Hash',)),
        (add_section_if_missing, ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
    ],
'29123d5a': [(log, ('3.0: Cissia SpearHead IB Hash',)), (add_ib_check_if_missing,)],
'bad668cc': [(log, ('3.0: Cissia SpearBarrel IB Hash',)), (add_ib_check_if_missing,)],
'19bac37e': [
        (log, ('3.0: Cissia SpearBarrel VB Hash',)),
        (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
    ],
'91e05512': [
        (log, ('3.0: Cissia SpearBarrel VB Hash',)),
        (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
    ],
'2785fe49': [
        (log, ('3.0: Cissia SpearBarrel VB Hash',)),
        (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
    ],
'b813c97f': [
        (log, ('3.0: Cissia SpearBarrel VB Hash',)),
        (add_section_if_missing, ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
    ],
'd49a5866': [(log, ('3.0: Cissia Spear(changing form) IB Hash',)), (add_ib_check_if_missing,)],
'7647eba5': [
        (log, ('3.0: Cissia Spear(changing form) VB Hash',)),
        (add_section_if_missing, ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
    ],
'5b71ede8': [
        (log, ('3.0: Cissia Spear(changing form) VB Hash',)),
        (add_section_if_missing, ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
    ],
'c37f63b8': [
        (log, ('3.0: Cissia Spear(changing form) VB Hash',)),
        (add_section_if_missing, ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
    ],
'32b90f8b': [
        (log, ('3.0: Cissia Spear(changing form) VB Hash',)),
        (add_section_if_missing, ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Cissia Hair TEX Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
'3b4de0d1': [
        (log, ('3.0: Cissia Tail VB Hash',)),
        (add_section_if_missing, ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
    ],
'9645e284': [
        (log, ('3.0: Cissia Body VB Hash',)),
        (add_section_if_missing, ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
    ],
'33b532e5': [
        (log, ('3.0: Cissia Hair VB Hash',)),
        (add_section_if_missing, ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Cissia',
    'game_versions': ['2.7', '2.8'],
}
