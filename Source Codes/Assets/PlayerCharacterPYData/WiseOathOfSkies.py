"""
WiseOathOfSkies Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns WiseOathOfSkies's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd5ca0411': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ef9c0510': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        'e8df7ff3': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Hair Position VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '774071dd': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '68e4f572': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
        ],
        '28005a5b': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cb0d0c22', 'WiseOathOfSkies.HairA.Diffuse.1024')),
        ],
        'cb0d0c22': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28005a5b', 'WiseOathOfSkies.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA, BodyA, NeckA and TieA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'WiseOathOfSkies.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseOathOfSkies.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseOathOfSkies.NeckA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WiseOathOfSkies.TieA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA, BodyA, NeckA and TieA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseOathOfSkies.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseOathOfSkies.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseOathOfSkies.NeckA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WiseOathOfSkies.TieA.NormalMap.2048')),
        ],
        '8d8269f8': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33368e12', 'WiseOathOfSkies.HairA.LightMap.1024')),
        ],
        '33368e12': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d8269f8', 'WiseOathOfSkies.HairA.LightMap.2048')),
        ],
        'f1b20f3d': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d9383a15', 'WiseOathOfSkies.HairA.MaterialMap.1024')),
        ],
        'd9383a15': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d5ca0411', 'WiseOathOfSkies.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1b20f3d', 'WiseOathOfSkies.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '8d08b190': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        '22fe3236': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '164b2ccb': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Body Draw VB Hash',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '4dcfe033': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Body Position VB Hash',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '0c2cc3dd': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        ],
        '8bab814c': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Body Blend VB Hash',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
        ],
        'b9dcce2e': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a0a4c84e', 'WiseOathOfSkies.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('a0a4c84e', 'WiseOathOfSkies.NeckA.Diffuse.1024')),
        ],
        'a0a4c84e': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9dcce2e', 'WiseOathOfSkies.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('b9dcce2e', 'WiseOathOfSkies.NeckA.Diffuse.2048')),
        ],
        'bd86c7c4': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d09dc95', 'WiseOathOfSkies.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('8d09dc95', 'WiseOathOfSkies.NeckA.LightMap.1024')),
        ],
        '8d09dc95': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd86c7c4', 'WiseOathOfSkies.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('bd86c7c4', 'WiseOathOfSkies.NeckA.LightMap.2048')),
        ],
        '4d7473b1': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('31707abe', 'WiseOathOfSkies.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('31707abe', 'WiseOathOfSkies.NeckA.MaterialMap.1024')),
        ],
        '31707abe': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies BodyA and NeckA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('22fe3236', 'WiseOathOfSkies.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4d7473b1', 'WiseOathOfSkies.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4d7473b1', 'WiseOathOfSkies.NeckA.MaterialMap.2048')),
        ],

        # ==================== Neck Component ====================
        '8a1ec07e': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Neck IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c4a1fb46': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Neck Draw VB Hash',)),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        ],
        '6171b974': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Neck Position VB Hash',)),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        ],
        '0da56abf': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Neck Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        ],
        '98a06e7d': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Neck Blend VB Hash',)),
            (add_section_if_missing,          ('8a1ec07e', 'WiseOathOfSkies.Neck.IB', 'match_priority = 0\n')),
        ],

        # ==================== Tie Component ====================
        'f21a2bac': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Tie IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '86f21a82': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Tie Draw VB Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        ],
        'fb0a401a': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Tie Position VB Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        ],
        '052d4b48': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Tie Texcoord VB Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        ],
        '4b19b5b5': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Tie Blend VB Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
        ],
        '1024352b': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd08a467', 'WiseOathOfSkies.TieA.Diffuse.1024')),
        ],
        'dd08a467': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1024352b', 'WiseOathOfSkies.TieA.Diffuse.2048')),
        ],
        'e550cd81': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f211318', 'WiseOathOfSkies.TieA.LightMap.1024')),
        ],
        '4f211318': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e550cd81', 'WiseOathOfSkies.TieA.LightMap.2048')),
        ],
        '6649f407': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ba59a4d0', 'WiseOathOfSkies.TieA.MaterialMap.1024')),
        ],
        'ba59a4d0': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies TieA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f21a2bac', 'WiseOathOfSkies.Tie.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6649f407', 'WiseOathOfSkies.TieA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '1fdaf388': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c4552bb': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Face Draw VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '5657c1fc': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Face Position VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
        ],
        'c83b6cbf': [
            (log,                             ('3.0 -> 3.1: WiseOathOfSkies Face Texcoord Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2b320847',)),
        ],
        '2b320847': [
            (log,                             ('3.1: WiseOathOfSkies Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '015fbf96': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies Face Blend VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
        ],
        '5d75fddc': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('588d7d2d', 'WiseOathOfSkies.FaceA.Diffuse.1024')),
        ],
        '588d7d2d': [
            (log,                             ('3.0 - 3.2: WiseOathOfSkies FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WiseOathOfSkies.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5d75fddc', 'WiseOathOfSkies.FaceA.Diffuse.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WiseOathOfSkies',
    'game_versions': ['3.0', '3.1', '3.2'],
}
