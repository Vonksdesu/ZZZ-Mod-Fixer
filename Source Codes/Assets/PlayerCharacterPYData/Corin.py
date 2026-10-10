"""
Corin Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Corin's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '5a839fb2': [
            (log,                             ('2.2 - 3.2: Corin Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd345e472': [
            (log,                             ('2.2 - 3.2: Corin Hair Draw VB Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        '7e7eee0d': [
            (log,                             ('2.2 - 3.2: Corin Hair Position VB Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        'abc95b03': [
            (log,                             ('2.2 - 3.2: Corin Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        '5fa50113': [
            (log,                             ('2.2 - 3.2: Corin Hair Blend VB Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        '60526444': [
            (log,                             ('2.2 - 3.2: Corin HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('651e96f8', 'Corin.HairA.Diffuse.1024')),
        ],
        '651e96f8': [
            (log,                             ('2.2 - 3.2: Corin HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('60526444', 'Corin.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Corin HairA, BodyA, BearA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', 'ab8956c8'), 'Corin.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '640141d4'), 'Corin.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '640141d4'), 'Corin.BearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Corin.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Corin HairA, BodyA, BearA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '4a68ef99'), 'Corin.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Corin.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Corin.BearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Corin.weapon.NormalMap.2048')),
        ],
        '74d66671': [
            (log,                             ('2.2 - 3.2: Corin HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0f300531', 'edff2372'), 'Corin.HairA.LightMap.1024')),
        ],
        '0f300531': [
            (log,                             ('2.2 - 3.2: Corin HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('74d66671', '929aca42'), 'Corin.HairA.LightMap.2048')),
        ],
        '8d999156': [
            (log,                             ('1.3 -> 1.4: Corin Hair Blend Hash (Old)',)),
            (update_hash,                     ('5fa50113',)),
        ],
        '2cf242f4': [
            (log,                             ('1.3 -> 1.4: Corin Hair Texcoord Hash (Old)',)),
            (update_hash,                     ('abc95b03',)),
        ],
        '929aca42': [
            (log,                             ('1.0 -> 1.4: Corin HairA LightMap 2048p Hash (Old)',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('74d66671',)),
        ],
        'edff2372': [
            (log,                             ('1.0 -> 2.5: Corin HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        '4a68ef99': [
            (log,                             ('1.0 -> 1.4: Corin HairA NormalMap 2048p Hash (Old)',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        'ab8956c8': [
            (log,                             ('1.0 -> 2.5: Corin HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],
        'c6398bc8': [
            (log,                             ('2.5: Corin HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('5a839fb2', 'Corin.Hair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair Shadow Component ====================
        '294af6bd': [
            (log,                             ('2.2 - 3.2: Corin Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '16399986': [
            (log,                             ('2.2 - 3.2: Corin Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('294af6bd', 'Corin.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b3c22aee': [
            (log,                             ('2.2 - 3.2: Corin Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('294af6bd', 'Corin.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'e134a479': [
            (log,                             ('2.2 - 3.2: Corin Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('294af6bd', 'Corin.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '81a22a15': [
            (log,                             ('2.2 - 3.2: Corin Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('294af6bd', 'Corin.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'e74620b5': [
            (log,                             ('2.2 - 3.2: Corin Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2eb162ef': [
            (log,                             ('2.2 - 3.2: Corin Body Draw VB Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
        ],
        '5dc40184': [
            (log,                             ('2.2 - 3.2: Corin Body Position VB Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
        ],
        '4c6b7bda': [
            (log,                             ('2.2 - 3.2: Corin Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
        ],
        'aa71e514': [
            (log,                             ('2.2 - 3.2: Corin Body Blend VB Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
        ],
        'af9d845a': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('681f5162', 'Corin.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('681f5162', 'Corin.BearA.Diffuse.1024')),
        ],
        '681f5162': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('af9d845a', 'Corin.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('af9d845a', 'Corin.BearA.Diffuse.2048')),
        ],
        'e1c1718f': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('068be251', 'af7eda82'), 'Corin.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     (('068be251', 'af7eda82'), 'Corin.BearA.LightMap.1024')),
        ],
        '068be251': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('e1c1718f', '75e05cdc'), 'Corin.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     (('e1c1718f', '75e05cdc'), 'Corin.BearA.LightMap.2048')),
        ],
        'e58d9767': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('50ed6c50', '9dc9c0f6'), 'Corin.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('50ed6c50', '9dc9c0f6'), 'Corin.BearA.MaterialMap.1024')),
        ],
        '50ed6c50': [
            (log,                             ('2.2 - 3.2: Corin BodyA and BearA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('e58d9767', '50a0faea'), 'Corin.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('e58d9767', '50a0faea'), 'Corin.BearA.MaterialMap.2048')),
        ],
        '75e05cdc': [
            (log,                             ('1.0 -> 1.4: Corin BodyA, BearA LightMap 2048p Hash (Old)',)),
            (update_hash,                     ('e1c1718f',)),
        ],
        'af7eda82': [
            (log,                             ('1.0 -> 2.5: Corin BodyA, BearA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        '50a0faea': [
            (log,                             ('1.0 -> 1.4: Corin BodyA, BearA MaterialMap 2048p Hash (Old)',)),
            (update_hash,                     ('e58d9767',)),
        ],
        '9dc9c0f6': [
            (log,                             ('1.0 -> 2.5: Corin BodyA, BearA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        '289f4c58': [
            (log,                             ('1.0 -> 1.4: Corin BodyA, BearA NormalMap 2048p Hash (Old)',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '640141d4': [
            (log,                             ('1.0 -> 2.5: Corin BodyA, BearA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('e74620b5', 'Corin.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Bear Component ====================
        '5f803336': [
            (log,                             ('2.2 - 3.2: Corin Bear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1a7ee1b5': [
            (log,                             ('2.2 - 3.2: Corin Bear Draw VB Hash',)),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        '4e1c9e44': [
            (log,                             ('2.2 - 3.2: Corin Bear Position VB Hash',)),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        '21987873': [
            (log,                             ('2.2 - 3.2: Corin Bear Texcoord VB Hash',)),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        '6ffea6f6': [
            (log,                             ('2.2 - 3.2: Corin Bear Blend VB Hash',)),
            (add_section_if_missing,          ('5f803336', 'Corin.Bear.IB', 'match_priority = 0\n')),
        ],
        # Bear shares all texture hashes with Body; see Body Component above.

        # ==================== Face Component ====================
        'a0c80593': [
            (log,                             ('2.2 - 3.2: Corin Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'eda4d773': [
            (log,                             ('2.2 - 3.2: Corin Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
        ],
        'd7b64434': [
            (log,                             ('2.2 - 3.2: Corin Face Position VB Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
        ],
        '1c0725e4': [
            (log,                             ('2.2 - 3.1: Corin Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('daff87b1',)),
        ],
        'daff87b1': [
            (log,                             ('3.2: Corin Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '4892e6b4': [
            (log,                             ('2.2 - 3.2: Corin Face Blend VB Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
        ],
        '6d662824': [
            (log,                             ('2.2 - 3.2: Corin FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('97022d3c', 'Corin.FaceA.Diffuse.1024')),
        ],
        '97022d3c': [
            (log,                             ('2.2 - 3.2: Corin FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a0c80593', 'Corin.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d662824', 'Corin.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon Component ====================
        '6f2286a6': [
            (log,                             ('2.2 - 3.2: Corin weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6bf8f421': [
            (log,                             ('2.2 - 3.2: Corin weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
        ],
        '17a67595': [
            (log,                             ('2.2 - 3.2: Corin weapon Position VB Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
        ],
        'f8da5b79': [
            (log,                             ('2.2 - 3.2: Corin weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
        ],
        'df7728c8': [
            (log,                             ('2.2 - 3.2: Corin weapon Blend VB Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
        ],
        '8dd64c09': [
            (log,                             ('2.2 - 3.2: Corin weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be466746', 'Corin.weapon.Diffuse.1024')),
        ],
        'be466746': [
            (log,                             ('2.2 - 3.2: Corin weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8dd64c09', 'Corin.weapon.Diffuse.2048')),
        ],
        'e8c22497': [
            (log,                             ('2.2 - 3.2: Corin weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d897d14c', 'Corin.weapon.LightMap.1024')),
        ],
        'd897d14c': [
            (log,                             ('2.2 - 3.2: Corin weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8c22497', 'Corin.weapon.LightMap.2048')),
        ],
        'b921465e': [
            (log,                             ('2.2 - 3.2: Corin weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d97382e2', 'Corin.weapon.MaterialMap.1024')),
        ],
        'd97382e2': [
            (log,                             ('2.2 - 3.2: Corin weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6f2286a6', 'Corin.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b921465e', 'Corin.weapon.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap with Hair, Body and Bear; see Hair Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Corin',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
