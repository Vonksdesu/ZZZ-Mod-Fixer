"""
WisePeacefulWaves Character Hash Commands
ZZZ Mod Fixer v2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WisePeacefulWaves's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes (v2.5)
'1fdaf388': [(log, ('2.5: WisePeacefulWaves Face IB Hash (shared with Wise)',)), (add_ib_check_if_missing,)],
'4fe696c8': [(log, ('2.5: WisePeacefulWaves Body IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('19a3f02e',))],
'cb272754': [(log, ('2.5: WisePeacefulWaves Hair IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('0ec31440',))],
'19a3f02e': [(log, ('3.0: WisePeacefulWaves Body IB Hash',)), (add_ib_check_if_missing,)],
'0ec31440': [(log, ('3.0: WisePeacefulWaves Face IB Hash',)), (add_ib_check_if_missing,)],
'3f771e63': [(log, ('2.8: WisePeacefulWaves Hair Shadow IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('8d08b190',))],

# Face Textures (v2.5)
'5d75fddc': [
        (log,                           ('2.5: WisePeacefulWaves FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('6c4ae8ce', '588d7d2d'), 'WisePeacefulWaves.FaceA.Diffuse.1024')),
    ],

'588d7d2d': [
        (log,                           ('2.5: WisePeacefulWaves FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5d75fddc', 'WisePeacefulWaves.FaceA.Diffuse.2048')),
    ],
'c2c8606e': [
        (log,                           ('2.5: WisePeacefulWaves FaceA, BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d6996446', 'WisePeacefulWaves.BodyA.MaterialMap.1024')),
    ],

'd6996446': [
        (log,                           ('2.5: WisePeacefulWaves FaceA, BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c2c8606e', 'WisePeacefulWaves.BodyA.MaterialMap.2048')),
    ],

# Body Textures (v2.5)
'd476035d': [
        (log,                           ('2.5: WisePeacefulWaves BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5907afda', 'WisePeacefulWaves.BodyA.Diffuse.1024')),
    ],

'5907afda': [
        (log,                           ('2.5: WisePeacefulWaves BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('d476035d', 'WisePeacefulWaves.BodyA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: WisePeacefulWaves BodyA, HairA NormalMap Hash (shared)',)),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'0fa8f99c': [
        (log,                           ('2.5: WisePeacefulWaves BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7a142a7d', 'WisePeacefulWaves.BodyA.LightMap.1024')),
    ],

'7a142a7d': [
        (log,                           ('2.5: WisePeacefulWaves BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0fa8f99c', 'WisePeacefulWaves.BodyA.LightMap.2048')),
    ],

# Hair Textures (v2.5)
'28005a5b': [
        (log,                           ('2.5: WisePeacefulWaves HairA Diffuse Hash',)),
        (add_section_if_missing,        ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'8d8269f8': [
        (log,                           ('2.5: WisePeacefulWaves HairA LightMap Hash',)),
        (add_section_if_missing,        ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'f1b20f3d': [
        (log,                           ('2.5: WisePeacefulWaves HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'20f40e82': [
        (log, ('3.0: WisePeacefulWaves Hair VB Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'1a6be2b0': [
        (log, ('3.0: WisePeacefulWaves Hair VB Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'951a90bf': [
        (log, ('3.0: WisePeacefulWaves Hair VB Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'16c55ecc': [
        (log, ('3.0: WisePeacefulWaves Hair VB Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'8d08b190': [(log, ('3.0: WisePeacefulWaves Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'681651f9': [
        (log, ('3.0: WisePeacefulWaves Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4af493e5': [
        (log, ('3.0: WisePeacefulWaves Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ad7d7eca': [
        (log, ('3.0: WisePeacefulWaves Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'795e9a7c': [
        (log, ('3.0: WisePeacefulWaves Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'44accf08': [
        (log, ('3.0: WisePeacefulWaves Body VB Hash',)),
        (add_section_if_missing, ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'71a703c7': [
        (log, ('3.0: WisePeacefulWaves Body VB Hash',)),
        (add_section_if_missing, ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'31d424fc': [
        (log, ('3.0: WisePeacefulWaves Body VB Hash',)),
        (add_section_if_missing, ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'9ab40475': [
        (log, ('3.0: WisePeacefulWaves Body VB Hash',)),
        (add_section_if_missing, ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'c83b6cbf': [
        (log, ('3.0: WisePeacefulWaves Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('2b320847',)),
    ],
'2b320847': [
        (log, ('3.1: WisePeacefulWaves Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
    ],
'015fbf96': [
        (log, ('3.0: WisePeacefulWaves Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
    ],
'6c4552bb': [(log, ('3.0: WisePeacefulWaves misc hash',)),],
'798adba3': [
        (log, ('3.0: WisePeacefulWaves Hair TEX Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'cb0d0c22': [
        (log, ('3.0: WisePeacefulWaves Hair TEX Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'33368e12': [
        (log, ('3.0: WisePeacefulWaves Hair TEX Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'd9383a15': [
        (log, ('3.0: WisePeacefulWaves Hair TEX Hash',)),
        (add_section_if_missing, ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'5657c1fc': [
        (log, ('3.0: WisePeacefulWaves Face VB Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
    ],
# =============================================================================
# WisePeacefulWaves 2.8 VB Hashes (Dual-Key: 2.8 -> 3.0, active in 1024p)
# =============================================================================
'14fff21a': [
        (log, ('2.8: WisePeacefulWaves Hair Shadow position_vb Hash',)),
        (add_section_if_missing, ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'16ac44f6': [
        (log, ('2.8: WisePeacefulWaves Hair position_vb Hash',)),
        (add_section_if_missing, ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'18e704a8': [
        (log, ('2.8: WisePeacefulWaves Body draw_vb Hash',)),
        (add_section_if_missing, ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'49d81f9a': [
        (log, ('2.8: WisePeacefulWaves Hair Shadow texcoord_vb Hash',)),
        (add_section_if_missing, ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'5c5bde90': [
        (log, ('2.8: WisePeacefulWaves Hair texcoord_vb Hash',)),
        (add_section_if_missing, ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'757bc7cc': [
        (log, ('2.8: WisePeacefulWaves Face Blend Hash',)),
        (add_section_if_missing, ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('015fbf96',)),
    ],
'77045a80': [
        (log, ('2.8: WisePeacefulWaves Hair draw_vb Hash',)),
        (add_section_if_missing, ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'82396952': [
        (log, ('2.8: WisePeacefulWaves Hair blend_vb Hash',)),
        (add_section_if_missing, ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
    ],
'8e9a12c7': [
        (log, ('2.8: WisePeacefulWaves Hair Shadow draw_vb Hash',)),
        (add_section_if_missing, ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a2c79f8d': [
        (log, ('2.8: WisePeacefulWaves Hair Shadow blend_vb Hash',)),
        (add_section_if_missing, ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'acfe9fe4': [
        (log, ('2.8: WisePeacefulWaves Body texcoord_vb Hash',)),
        (add_section_if_missing, ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'd4147320': [
        (log, ('2.8: WisePeacefulWaves Body blend_vb Hash',)),
        (add_section_if_missing, ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'd6c86c1e': [
        (log, ('2.8: WisePeacefulWaves Body position_vb Hash',)),
        (add_section_if_missing, ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
    ],
'9741e2f0': [(log, ('2.1 -> 2.2: Wiseswimwear Body Blend Hash',)), (update_hash, ('d4147320',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WisePeacefulWaves',
    'game_versions': ['2.5', '3.0'],
}

