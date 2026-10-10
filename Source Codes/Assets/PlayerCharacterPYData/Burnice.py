"""
Burnice Character Hash Commands
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
    Returns Burnice's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'f779fb81': [
            (log,                             ('2.2 - 3.2: Burnice Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c22b4efe': [
            (log,                             ('2.2 - 3.2: Burnice Hair Draw VB Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        ],
        '511006ba': [
            (log,                             ('2.2 - 3.2: Burnice Hair Position VB Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        ],
        'c882e6eb': [
            (log,                             ('2.2 - 3.2: Burnice Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        ],
        '68027115': [
            (log,                             ('2.2 - 3.2: Burnice Hair Blend VB Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        ],
        '609b50a9': [
            (log,                             ('2.2 - 3.2: Burnice HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4568c6b3', 'Burnice.HairA.Diffuse.1024')),
        ],
        '4568c6b3': [
            (log,                             ('2.2 - 3.2: Burnice HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('609b50a9', 'Burnice.HairA.Diffuse.2048')),
        ],
        '438cf629': [
            (log,                             ('1.2 -> 2.5: Burnice HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '0050e0d2': [
            (log,                             ('1.2 - 2.5: Burnice HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Burnice Hair, Body and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', '0050e0d2'), 'Burnice.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '0c4f338a'), 'Burnice.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Burnice.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Burnice Hair, Body and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Burnice.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Burnice.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Burnice.weapon.NormalMap.2048')),
        ],
        'bf0042b9': [
            (log,                             ('2.2 - 3.2: Burnice HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08770e8c', 'Burnice.HairA.LightMap.1024')),
        ],
        '08770e8c': [
            (log,                             ('2.2 - 3.2: Burnice HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf0042b9', 'Burnice.HairA.LightMap.2048')),
        ],
        '5f2840f1': [
            (log,                             ('2.2 - 3.2: Burnice HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3ae3ea20', 'Burnice.HairA.MaterialMap.1024')),
        ],
        '3ae3ea20': [
            (log,                             ('2.2 - 3.2: Burnice HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5f2840f1', 'Burnice.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '40aa11a7': [
            (log,                             ('2.2 - 3.2: Burnice Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '164e3024': [
            (log,                             ('2.2 - 3.2: Burnice Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '831534e5': [
            (log,                             ('2.2 - 3.2: Burnice Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '4d570d70': [
            (log,                             ('2.2 - 3.2: Burnice Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9d6bbd22': [
            (log,                             ('2.2 - 3.2: Burnice Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'af63e974': [
            (log,                             ('2.2 - 3.2: Burnice Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'be10c4bb': [
            (log,                             ('2.2 - 3.2: Burnice Body Draw VB Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        ],
        '208d5e15': [
            (log,                             ('2.2 - 3.2: Burnice Body Position VB Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        ],
        '35826de5': [
            (log,                             ('2.2 - 3.2: Burnice Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        ],
        'c705bf55': [
            (log,                             ('2.2 - 3.2: Burnice Body Blend VB Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        ],
        '50bf6521': [
            (log,                             ('2.2 - 3.2: Burnice BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0e67001', 'Burnice.BodyA.Diffuse.1024')),
        ],
        'f0e67001': [
            (log,                             ('2.2 - 3.2: Burnice BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('50bf6521', 'Burnice.BodyA.Diffuse.2048')),
        ],
        '0f2c69e2': [
            (log,                             ('1.2 -> 2.5: Burnice BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '0c4f338a': [
            (log,                             ('1.2 - 2.5: Burnice BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        ],
        'f4e05ee7': [
            (log,                             ('2.2 - 3.2: Burnice BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0a3ba8ac', 'Burnice.BodyA.LightMap.1024')),
        ],
        '0a3ba8ac': [
            (log,                             ('2.2 - 3.2: Burnice BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f4e05ee7', 'Burnice.BodyA.LightMap.2048')),
        ],
        'c321481d': [
            (log,                             ('2.2 - 3.2: Burnice BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e37e7622', 'Burnice.BodyA.MaterialMap.1024')),
        ],
        'e37e7622': [
            (log,                             ('2.2 - 3.2: Burnice BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c321481d', 'Burnice.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'b3f6fcb3': [
            (log,                             ('2.2 - 3.2: Burnice Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '19ead1b7': [
            (log,                             ('2.2 - 3.2: Burnice Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
        ],
        '23f842f0': [
            (log,                             ('2.2 - 3.2: Burnice Face Position VB Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
        ],
        '14b70725': [
            (log,                             ('2.2 - 3.1: Burnice Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('61782f72',)),
        ],
        '61782f72': [
            (log,                             ('3.2: Burnice Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '12c38959': [
            (log,                             ('2.2 - 3.2: Burnice Face Blend VB Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
        ],
        'e338bb82': [
            (log,                             ('1.3 -> 1.4: Burnice FaceA Diffuse 2048p Hash',)),
            (update_hash,                     ('c4b6bb10',)),
        ],
        'c4b6bb10': [
            (log,                             ('2.2 - 3.2: Burnice FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('68f0fb19', 'c9c87bb1'), 'Burnice.FaceA.Diffuse.1024')),
        ],
        'c9c87bb1': [
            (log,                             ('1.3 -> 1.4: Burnice FaceA Diffuse 1024p Hash',)),
            (update_hash,                     ('68f0fb19',)),
        ],
        '68f0fb19': [
            (log,                             ('2.2 - 3.2: Burnice FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('c4b6bb10', 'e338bb82'), 'Burnice.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon Component ====================
        '6b08674c': [
            (log,                             ('2.2 - 3.2: Burnice weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c7e24774': [
            (log,                             ('2.2 - 3.2: Burnice weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
        ],
        '36821275': [
            (log,                             ('2.2 - 3.2: Burnice weapon Position VB Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
        ],
        '2981a076': [
            (log,                             ('2.2 - 3.2: Burnice weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
        ],
        'a5ca368d': [
            (log,                             ('2.2 - 3.2: Burnice weapon Blend VB Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
        ],
        '5f6615b0': [
            (log,                             ('2.2 - 3.2: Burnice weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('78876ed2', 'Burnice.weapon.Diffuse.1024')),
        ],
        '78876ed2': [
            (log,                             ('2.2 - 3.2: Burnice weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5f6615b0', 'Burnice.weapon.Diffuse.2048')),
        ],
        '5ef426d0': [
            (log,                             ('2.2 - 3.2: Burnice weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ae23adc', 'Burnice.weapon.LightMap.1024')),
        ],
        '1ae23adc': [
            (log,                             ('2.2 - 3.2: Burnice weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ef426d0', 'Burnice.weapon.LightMap.2048')),
        ],
        '9b7dfc16': [
            (log,                             ('2.2 - 3.2: Burnice weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5cb92b3', 'Burnice.weapon.MaterialMap.1024')),
        ],
        'b5cb92b3': [
            (log,                             ('2.2 - 3.2: Burnice weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9b7dfc16', 'Burnice.weapon.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Burnice',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}

