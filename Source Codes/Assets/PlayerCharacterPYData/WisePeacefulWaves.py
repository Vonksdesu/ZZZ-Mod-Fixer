"""
WisePeacefulWaves Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
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

        # ==================== Hair Component ====================
        'cb272754': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('0ec31440',)),
        ],
        '0ec31440': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '77045a80': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Draw Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('20f40e82',)),
        ],
        '20f40e82': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Draw VB Hash',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
        ],
        '16ac44f6': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Position Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('1a6be2b0',)),
        ],
        '1a6be2b0': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Position VB Hash',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
        ],
        '5c5bde90': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Texcoord Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('951a90bf',)),
        ],
        '951a90bf': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
        ],
        '82396952': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Blend Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('16c55ecc',)),
        ],
        '16c55ecc': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Blend VB Hash',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
        ],
        '28005a5b': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cb0d0c22', 'WisePeacefulWaves.HairB.Diffuse.1024')),
        ],
        'd476035d': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5907afda', 'WisePeacefulWaves.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('5907afda', 'WisePeacefulWaves.BodyA.Diffuse.1024')),
        ],
        'cb0d0c22': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28005a5b', 'WisePeacefulWaves.HairB.Diffuse.2048')),
        ],
        '5907afda': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d476035d', 'WisePeacefulWaves.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('d476035d', 'WisePeacefulWaves.BodyA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA, HairB and BodyA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'WisePeacefulWaves.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WisePeacefulWaves.HairB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'WisePeacefulWaves.BodyA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA, HairB and BodyA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'WisePeacefulWaves.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WisePeacefulWaves.HairB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'WisePeacefulWaves.BodyA.NormalMap.2048')),
        ],
        '8d8269f8': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33368e12', 'WisePeacefulWaves.HairB.LightMap.1024')),
        ],
        '0fa8f99c': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7a142a7d', 'WisePeacefulWaves.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('7a142a7d', 'WisePeacefulWaves.BodyA.LightMap.1024')),
        ],
        '33368e12': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d8269f8', 'WisePeacefulWaves.HairB.LightMap.2048')),
        ],
        '7a142a7d': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0fa8f99c', 'WisePeacefulWaves.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('0fa8f99c', 'WisePeacefulWaves.BodyA.LightMap.2048')),
        ],
        'f1b20f3d': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d9383a15', 'WisePeacefulWaves.HairB.MaterialMap.1024')),
        ],
        'c2c8606e': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d6996446', 'WisePeacefulWaves.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d6996446', 'WisePeacefulWaves.BodyA.MaterialMap.1024')),
        ],
        'd9383a15': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('cb272754', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1b20f3d', 'WisePeacefulWaves.HairB.MaterialMap.2048')),
        ],
        'd6996446': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves HairA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0ec31440', 'WisePeacefulWaves.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c2c8606e', 'WisePeacefulWaves.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c2c8606e', 'WisePeacefulWaves.BodyA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3f771e63': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('8d08b190',)),
        ],
        '8d08b190': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8e9a12c7': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Shadow Draw Hash',)),
            (add_section_if_missing,          ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('681651f9',)),
        ],
        '681651f9': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '14fff21a': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Shadow Position Hash',)),
            (add_section_if_missing,          ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('4af493e5',)),
        ],
        '4af493e5': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '49d81f9a': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Shadow Texcoord Hash',)),
            (add_section_if_missing,          ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ad7d7eca',)),
        ],
        'ad7d7eca': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a2c79f8d': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Hair Shadow Blend Hash',)),
            (add_section_if_missing,          ('3f771e63', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('795e9a7c',)),
        ],
        '795e9a7c': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('8d08b190', 'WisePeacefulWaves.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '4fe696c8': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('19a3f02e',)),
        ],
        '19a3f02e': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '18e704a8': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Body Draw Hash',)),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('44accf08',)),
        ],
        '44accf08': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Body Draw VB Hash',)),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        ],
        'd6c86c1e': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Body Position Hash',)),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('71a703c7',)),
        ],
        '71a703c7': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Body Position VB Hash',)),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        ],
        'acfe9fe4': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Body Texcoord Hash',)),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('31d424fc',)),
        ],
        '31d424fc': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        ],
        'd4147320': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Body Blend Hash',)),
            (add_section_if_missing,          ('4fe696c8', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('9ab40475',)),
        ],
        '9ab40475': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Body Blend VB Hash',)),
            (add_section_if_missing,          ('19a3f02e', 'WisePeacefulWaves.Body.IB', 'match_priority = 0\n')),
        ],
        '9741e2f0': [
            (log,                             ('2.1 -> 2.2: WisePeacefulWaves Body Blend Hash',)),
            (update_hash,                     ('d4147320',)),
        ],

        # ==================== Face Component ====================
        '1fdaf388': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c4552bb': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        ],
        '5657c1fc': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves Face Position VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        ],
        'c83b6cbf': [
            (log,                             ('3.0 -> 3.1: WisePeacefulWaves Face Texcoord Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2b320847',)),
        ],
        '2b320847': [
            (log,                             ('3.1: WisePeacefulWaves Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        ],
        '757bc7cc': [
            (log,                             ('2.8 -> 3.0: WisePeacefulWaves Face Blend Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('015fbf96',)),
        ],
        '015fbf96': [
            (log,                             ('3.0 - 3.2: WisePeacefulWaves Face Blend VB Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
        ],
        '5d75fddc': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('588d7d2d', '6c4ae8ce'), 'WisePeacefulWaves.FaceA.Diffuse.1024')),
        ],
        '588d7d2d': [
            (log,                             ('2.2 - 3.2: WisePeacefulWaves FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1fdaf388', 'WisePeacefulWaves.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5d75fddc', 'WisePeacefulWaves.FaceA.Diffuse.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'WisePeacefulWaves',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
