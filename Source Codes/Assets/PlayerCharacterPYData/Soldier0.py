"""
Soldier0 Character Hash Commands
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
    Returns Soldier0's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '217ec790': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9a4ae9c7': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Draw VB Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        '7aa2035c': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Position VB Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        'c6b7b3b2': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        'd13ddfe1': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Blend VB Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        'aa3d57ff': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8cb4086a', 'Soldier0.HairA.Diffuse.1024')),
        ],
        '8cb4086a': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa3d57ff', 'Soldier0.HairA.Diffuse.2048')),
        ],
        'f8e9a6c1': [
            (log,                             ('2.5: Soldier0 HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA, BodyA, weapon - 短刀A and weapon - 长刀A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier0.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier0.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier0.weapon - 短刀A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soldier0.weapon - 长刀A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA, BodyA, weapon - 短刀A and weapon - 长刀A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier0.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier0.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier0.weapon - 短刀A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soldier0.weapon - 长刀A.NormalMap.2048')),
        ],
        '8d42a55b': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96a28554', 'Soldier0.HairA.LightMap.1024')),
        ],
        '96a28554': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d42a55b', 'Soldier0.HairA.LightMap.2048')),
        ],
        '464847b3': [
            (log,                             ('1.6: Soldier0 HairA MaterialMap 2048p Hash (Old)',)),
            (update_hash,                     ('0b059f91',)),
        ],
        'ce3e73be': [
            (log,                             ('2.5: Soldier0 HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
        ],
        '0b059f91': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb979f59', 'Soldier0.HairA.MaterialMap.1024')),
        ],
        'bb979f59': [
            (log,                             ('2.2 - 3.2: Soldier0 HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('217ec790', 'Soldier0.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0b059f91', 'Soldier0.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3431e8b4': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dd91b126': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('3431e8b4', 'Soldier0.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '183df742': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('3431e8b4', 'Soldier0.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '2b4afe3c': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('3431e8b4', 'Soldier0.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '376b601d': [
            (log,                             ('2.2 - 3.2: Soldier0 Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('3431e8b4', 'Soldier0.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '53d3f4e5': [
            (log,                             ('2.2 - 3.2: Soldier0 Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '36089968': [
            (log,                             ('2.2 - 3.2: Soldier0 Body Draw VB Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        ],
        'f1c057e8': [
            (log,                             ('2.2 - 3.2: Soldier0 Body Position VB Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        ],
        '80d87313': [
            (log,                             ('2.2 - 3.2: Soldier0 Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        ],
        'd4ff3f35': [
            (log,                             ('2.2 - 3.2: Soldier0 Body Blend VB Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
        ],
        '627baf3f': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0acef326', 'Soldier0.BodyA.Diffuse.1024')),
        ],
        '0acef326': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('627baf3f', 'Soldier0.BodyA.Diffuse.2048')),
        ],
        '3a56b70b': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('625ad0eb', 'Soldier0.BodyA.LightMap.1024')),
        ],
        '625ad0eb': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3a56b70b', 'Soldier0.BodyA.LightMap.2048')),
        ],
        '7cfa12b6': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dea3c5a0', 'Soldier0.BodyA.MaterialMap.1024')),
        ],
        'dea3c5a0': [
            (log,                             ('2.2 - 3.2: Soldier0 BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('53d3f4e5', 'Soldier0.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7cfa12b6', 'Soldier0.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'f2f539b8': [
            (log,                             ('1.6: Soldier0 Face IB Hash (Old)',)),
            (update_hash,                     ('e30ca87f',)),
        ],
        'e30ca87f': [
            (log,                             ('2.2 - 3.2: Soldier0 Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f6aa443': [
            (log,                             ('2.2 - 3.2: Soldier0 Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        ],
        'a5783704': [
            (log,                             ('2.2 - 3.2: Soldier0 Face Position VB Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        ],
        'fc66ecd0': [
            (log,                             ('2.2 - 3.1: Soldier0 Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('be99c90e',)),
        ],
        'be99c90e': [
            (log,                             ('3.2: Soldier0 Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'df6b6f84': [
            (log,                             ('2.2 - 3.2: Soldier0 Face Blend VB Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
        ],
        '05d7b504': [
            (log,                             ('2.2 - 3.2: Soldier0 FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('692c6d2b', 'Soldier0.FaceA.Diffuse.1024')),
        ],
        '692c6d2b': [
            (log,                             ('2.2 - 3.2: Soldier0 FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('e30ca87f', 'Soldier0.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('05d7b504', 'Soldier0.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 短刀 Component ====================
        '4d5c8ade': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '771b3e9f': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
        ],
        'a7b673bb': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀 Position VB Hash',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
        ],
        '37c582f3': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
        ],
        '698ef481': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀 Blend VB Hash',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
        ],
        'c85b4097': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb432d20', 'Soldier0.weapon - 短刀A.Diffuse.1024')),
            (multiply_section_if_missing,     ('fb432d20', 'Soldier0.weapon - 长刀A.Diffuse.1024')),
        ],
        'fb432d20': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c85b4097', 'Soldier0.weapon - 短刀A.Diffuse.2048')),
            (multiply_section_if_missing,     ('c85b4097', 'Soldier0.weapon - 长刀A.Diffuse.2048')),
        ],
        '8353de2a': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1a20e036', 'Soldier0.weapon - 短刀A.LightMap.1024')),
            (multiply_section_if_missing,     ('1a20e036', 'Soldier0.weapon - 长刀A.LightMap.1024')),
        ],
        '1a20e036': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8353de2a', 'Soldier0.weapon - 短刀A.LightMap.2048')),
            (multiply_section_if_missing,     ('8353de2a', 'Soldier0.weapon - 长刀A.LightMap.2048')),
        ],
        '88fe0e3c': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45f422c0', 'Soldier0.weapon - 短刀A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('45f422c0', 'Soldier0.weapon - 长刀A.MaterialMap.1024')),
        ],
        '45f422c0': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 短刀A and weapon - 长刀A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4d5c8ade', 'Soldier0.weapon - 短刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('88fe0e3c', 'Soldier0.weapon - 短刀A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('88fe0e3c', 'Soldier0.weapon - 长刀A.MaterialMap.2048')),
        ],

        # ==================== weapon - 长刀 Component ====================
        '6df60902': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 长刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '037b48d9': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 长刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        '6f413f77': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 长刀 Position VB Hash',)),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        'e45c71f4': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 长刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        'c68ee4ea': [
            (log,                             ('2.2 - 3.2: Soldier0 weapon - 长刀 Blend VB Hash',)),
            (add_section_if_missing,          ('6df60902', 'Soldier0.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soldier0',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
