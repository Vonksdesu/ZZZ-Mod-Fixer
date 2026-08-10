"""
Pyrois Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0
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
# === IB Hashes ===
'0a7c1023': [
        (log,                           ('3.0: Pyrois Arm IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd347d859': [
        (log,                           ('3.0: Pyrois Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'd98c8923': [
        (log,                           ('3.0: Pyrois Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Pyrois Textures (HairA) ===
'bee6766b': [
        (log,                           ('3.0: Pyrois HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('28b3c245', 'Pyrois.HairA.Diffuse.2048')),
    ],
'28b3c245': [
        (log,                           ('3.0: Pyrois HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('bee6766b', 'Pyrois.HairA.Diffuse.1024')),
    ],
'6bec1d56': [
        (log,                           ('3.0: Pyrois HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('0d24e396', 'Pyrois.HairA.LightMap.2048')),
    ],
'0d24e396': [
        (log,                           ('3.0: Pyrois HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('6bec1d56', 'Pyrois.HairA.LightMap.1024')),
    ],
'7405e2d5': [
        (log,                           ('3.0: Pyrois HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('bd5b0984', 'Pyrois.HairA.MaterialMap.2048')),
    ],
'bd5b0984': [
        (log,                           ('3.0: Pyrois HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('7405e2d5', 'Pyrois.HairA.MaterialMap.1024')),
    ],

# === Pyrois Textures (BodyA) ===
'1331e7ee': [
        (log,                           ('3.0: Pyrois BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('ef11e537', 'Pyrois.BodyA.Diffuse.2048')),
    ],
'ef11e537': [
        (log,                           ('3.0: Pyrois BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('1331e7ee', 'Pyrois.BodyA.Diffuse.1024')),
    ],
'3ed5431d': [
        (log,                           ('3.0: Pyrois BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c7a6063b', 'Pyrois.BodyA.LightMap.2048')),
    ],
'c7a6063b': [
        (log,                           ('3.0: Pyrois BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('3ed5431d', 'Pyrois.BodyA.LightMap.1024')),
    ],
'17c1a8e2': [
        (log,                           ('3.0: Pyrois BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('d81be7b3', 'Pyrois.BodyA.MaterialMap.2048')),
    ],
'd81be7b3': [
        (log,                           ('3.0: Pyrois BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('17c1a8e2', 'Pyrois.BodyA.MaterialMap.1024')),
    ],
'7fdd4865': [
        (log, ('3.0: Pyrois Hair VB Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'764bcab3': [
        (log, ('3.0: Pyrois Hair VB Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'b502aa23': [
        (log, ('3.0: Pyrois Hair VB Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Pyrois Hair TEX Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'c1f14931': [
        (log, ('3.0: Pyrois Body VB Hash',)),
        (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
    ],
'337fe1ee': [
        (log, ('3.0: Pyrois Body VB Hash',)),
        (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
    ],
'789800b3': [
        (log, ('3.0: Pyrois Body VB Hash',)),
        (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
    ],
'a816b4ec': [
        (log, ('3.0: Pyrois Arm VB Hash',)),
        (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'1abe00b9': [
        (log, ('3.0: Pyrois Arm VB Hash',)),
        (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'a946c036': [
        (log, ('3.0: Pyrois Arm VB Hash',)),
        (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'585b0241': [(log, ('3.0: Pyrois Sword IB Hash',)), (add_ib_check_if_missing,)],
'c942b027': [
        (log, ('3.0: Pyrois Sword VB Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'899ea8ea': [
        (log, ('3.0: Pyrois Sword VB Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'bc7a3429': [
        (log, ('3.0: Pyrois Sword VB Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'd51ce897': [
        (log, ('3.0: Pyrois Sword VB Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'bda9d364': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'6bc7e6b2': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'a71b1a4a': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Pyrois Hair TEX Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
'36cbf65b': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'964cadd0': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'8cb22c6d': [
        (log, ('3.0: Pyrois Sword TEX Hash',)),
        (add_section_if_missing, ('585b0241', 'Pyrois.Sword.IB', 'match_priority = 0\n')),
    ],
'8e155d0d': [
        (log, ('3.0: Pyrois Arm VB Hash',)),
        (add_section_if_missing, ('0a7c1023', 'Pyrois.Arm.IB', 'match_priority = 0\n')),
    ],
'5bbaca72': [
        (log, ('3.0: Pyrois Body VB Hash',)),
        (add_section_if_missing, ('d347d859', 'Pyrois.Body.IB', 'match_priority = 0\n')),
    ],
'6204c171': [
        (log, ('3.0: Pyrois Hair VB Hash',)),
        (add_section_if_missing, ('d98c8923', 'Pyrois.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pyrois',
    'game_versions': ['3.0'],
}
