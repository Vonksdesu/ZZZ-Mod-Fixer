"""
NangongYuRhapsodyMuse Character Hash Commands
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
    Returns NangongYuRhapsodyMuse's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'5f2741ff': [
        (log,                           ('2.7: NangongYuRhapsodyMuse Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === NangongYuRhapsodyMuse Textures (HairA) ===
'4fa2f495': [
        (log,                           ('2.7: NangongYuRhapsodyMuse HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('5a026445', 'NangongYuRhapsodyMuse.HairA.Diffuse.2048')),
    ],
'5a026445': [
        (log,                           ('2.7: NangongYuRhapsodyMuse HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('4fa2f495', 'NangongYuRhapsodyMuse.HairA.Diffuse.1024')),
    ],

# === NangongYuRhapsodyMuse Textures (BodyA) ===
'263aba53': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('46c73033', 'NangongYuRhapsodyMuse.BodyA.Diffuse.2048')),
    ],
'46c73033': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('263aba53', 'NangongYuRhapsodyMuse.BodyA.Diffuse.1024')),
    ],
'79423b33': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c17bc21d', 'NangongYuRhapsodyMuse.BodyA.LightMap.2048')),
    ],
'c17bc21d': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('79423b33', 'NangongYuRhapsodyMuse.BodyA.LightMap.1024')),
    ],
'1786d968': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('e8200d09', 'NangongYuRhapsodyMuse.BodyA.MaterialMap.2048')),
    ],
'e8200d09': [
        (log,                           ('2.7: NangongYuRhapsodyMuse BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('1786d968', 'NangongYuRhapsodyMuse.BodyA.MaterialMap.1024')),
    ],
'969152d4': [(log, ('3.0: NangongYuRhapsodyMuse Hair IB Hash',)), (add_ib_check_if_missing,)],
'536345c3': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'd1a15d0e': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'e67f6a3c': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'56699a62': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair VB Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'd94a0c41': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'a458a615': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'17438fa9': [(log, ('3.0: NangongYuRhapsodyMuse Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'cd884c0a': [(log, ('3.0: NangongYuRhapsodyMuse Headband IB Hash',)), (add_ib_check_if_missing,)],
'5aac7571': [
        (log, ('3.0: NangongYuRhapsodyMuse Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'74cbadea': [
        (log, ('3.0: NangongYuRhapsodyMuse Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'00cbd7a8': [
        (log, ('3.0: NangongYuRhapsodyMuse Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'82509f4f': [
        (log, ('3.0: NangongYuRhapsodyMuse Headband VB Hash',)),
        (add_section_if_missing, ('cd884c0a', 'NangongYuRhapsodyMuse.Headband.IB', 'match_priority = 0\n')),
    ],
'5b186a44': [(log, ('3.0: NangongYuRhapsodyMuse wing IB Hash',)), (add_ib_check_if_missing,)],
'4f3fcef0': [
        (log, ('3.0: NangongYuRhapsodyMuse wing VB Hash',)),
        (add_section_if_missing, ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
    ],
'f0922b32': [
        (log, ('3.0: NangongYuRhapsodyMuse wing VB Hash',)),
        (add_section_if_missing, ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
    ],
'f1ca59db': [
        (log, ('3.0: NangongYuRhapsodyMuse wing VB Hash',)),
        (add_section_if_missing, ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
    ],
'701bb859': [
        (log, ('3.0: NangongYuRhapsodyMuse wing VB Hash',)),
        (add_section_if_missing, ('5b186a44', 'NangongYuRhapsodyMuse.wing.IB', 'match_priority = 0\n')),
    ],
'6a7b86e3': [
        (log, ('3.0: NangongYuRhapsodyMuse Body VB Hash',)),
        (add_section_if_missing, ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'584ee20f': [
        (log, ('3.0: NangongYuRhapsodyMuse Body VB Hash',)),
        (add_section_if_missing, ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'bcfea595': [
        (log, ('3.0: NangongYuRhapsodyMuse Body VB Hash',)),
        (add_section_if_missing, ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'ba598cf9': [(log, ('3.0: NangongYuRhapsodyMuse Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'1fd77103': [
        (log, ('3.0: NangongYuRhapsodyMuse Eyebrow TEX Hash',)),
        (add_section_if_missing, ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'd643e19a': [(log, ('3.0: NangongYuRhapsodyMuse Face IB Hash',)), (add_ib_check_if_missing,)],
'd70f65c1': [
        (log, ('3.0: NangongYuRhapsodyMuse Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
    ],
'ed1df686': [
        (log, ('3.0: NangongYuRhapsodyMuse Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
    ],
'45910aef': [
        (log, ('3.0: NangongYuRhapsodyMuse Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
    ],
'93c1ec0c': [
        (log, ('3.0: NangongYuRhapsodyMuse Face VB Hash',)),
        (add_section_if_missing, ('d643e19a', 'NangongYuRhapsodyMuse.Face.IB', 'match_priority = 0\n')),
    ],
'dcd7242e': [(log, ('3.0: NangongYuRhapsodyMuse Weapon IB Hash',)), (add_ib_check_if_missing,)],
'cf34f106': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'5e50a4f2': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'766f3fca': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'e3573bc8': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'687f57b8': [
        (log, ('3.0: NangongYuRhapsodyMuse Hair TEX Hash',)),
        (add_section_if_missing, ('969152d4', 'NangongYuRhapsodyMuse.Hair.IB', 'match_priority = 0\n')),
    ],
'fcc325af': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'a64be703': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'6f39c5ff': [
        (log, ('3.0: NangongYuRhapsodyMuse Body VB Hash',)),
        (add_section_if_missing, ('5f2741ff', 'NangongYuRhapsodyMuse.Body.IB', 'match_priority = 0\n')),
    ],
'08ff63ac': [
        (log, ('3.0: NangongYuRhapsodyMuse Weapon TEX Hash',)),
        (add_section_if_missing, ('dcd7242e', 'NangongYuRhapsodyMuse.Weapon.IB', 'match_priority = 0\n')),
    ],
'b6e87aef': [
        (log, ('3.0: NangongYuRhapsodyMuse Eyebrow TEX Hash',)),
        (add_section_if_missing, ('ba598cf9', 'NangongYuRhapsodyMuse.Eyebrow.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'NangongYuRhapsodyMuse',
    'game_versions': ['2.7'],
}
