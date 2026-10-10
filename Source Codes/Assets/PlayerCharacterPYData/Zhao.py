"""
Zhao Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Zhao's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '2d519056': [
            (log,                             ('2.5 - 3.2: Zhao Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9bfc82f2': [
            (log,                             ('2.5 - 3.2: Zhao Hair Draw VB Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        ],
        'f86dba12': [
            (log,                             ('2.5 - 3.2: Zhao Hair Position VB Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        ],
        'e1fe5e10': [
            (log,                             ('2.5 - 3.2: Zhao Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        ],
        '4b9ea40c': [
            (log,                             ('2.5 - 3.2: Zhao Hair Blend VB Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
        ],
        '3400d1fc': [
            (log,                             ('2.5 - 3.2: Zhao HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('738b6ad0', 'Zhao.HairA.Diffuse.1024')),
        ],
        '738b6ad0': [
            (log,                             ('2.5 - 3.2: Zhao HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3400d1fc', 'Zhao.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.5 - 3.2: Zhao HairA, BodyA and KnifeA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Zhao.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Zhao.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Zhao.KnifeA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.5 - 3.2: Zhao HairA, BodyA and KnifeA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Zhao.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Zhao.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Zhao.KnifeA.NormalMap.2048')),
        ],
        '4c988418': [
            (log,                             ('2.5 - 3.2: Zhao HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('39dab7f4', 'Zhao.HairA.LightMap.1024')),
        ],
        '39dab7f4': [
            (log,                             ('2.5 - 3.2: Zhao HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4c988418', 'Zhao.HairA.LightMap.2048')),
        ],
        'bdc3666d': [
            (log,                             ('2.5 - 3.2: Zhao HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('06b8c2ae', 'Zhao.HairA.MaterialMap.1024')),
        ],
        '06b8c2ae': [
            (log,                             ('2.5 - 3.2: Zhao HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2d519056', 'Zhao.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bdc3666d', 'Zhao.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '75cf4c8a': [
            (log,                             ('2.5 - 3.2: Zhao Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '302715ad': [
            (log,                             ('2.5 - 3.2: Zhao Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9d33a619': [
            (log,                             ('2.5 - 3.2: Zhao Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'f4afa896': [
            (log,                             ('2.5 - 3.2: Zhao Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'f1c99dcc': [
            (log,                             ('2.5 - 3.2: Zhao Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('75cf4c8a', 'Zhao.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '6a57d06b': [
            (log,                             ('2.5 - 3.2: Zhao Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a08c7b83': [
            (log,                             ('2.5 - 3.2: Zhao Body Draw VB Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        ],
        'ac4490da': [
            (log,                             ('2.5 - 3.2: Zhao Body Position VB Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        ],
        '834b607a': [
            (log,                             ('2.5 - 3.2: Zhao Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        ],
        '06ce2ca1': [
            (log,                             ('2.5 - 3.2: Zhao Body Blend VB Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
        ],
        '77dc1746': [
            (log,                             ('2.5 - 3.2: Zhao BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bebe4176', 'Zhao.BodyA.Diffuse.1024')),
        ],
        'bebe4176': [
            (log,                             ('2.5 - 3.2: Zhao BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77dc1746', 'Zhao.BodyA.Diffuse.2048')),
        ],
        '5ed57658': [
            (log,                             ('2.5 - 3.2: Zhao BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd6cfe48', 'Zhao.BodyA.LightMap.1024')),
        ],
        'dd6cfe48': [
            (log,                             ('2.5 - 3.2: Zhao BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ed57658', 'Zhao.BodyA.LightMap.2048')),
        ],
        'e98b7e9e': [
            (log,                             ('2.5 - 3.2: Zhao BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('04383cb9', 'Zhao.BodyA.MaterialMap.1024')),
        ],
        '04383cb9': [
            (log,                             ('2.5 - 3.2: Zhao BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6a57d06b', 'Zhao.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e98b7e9e', 'Zhao.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '43c3c5a0': [
            (log,                             ('2.5 - 3.2: Zhao Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b26f9258': [
            (log,                             ('2.5 - 3.2: Zhao Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        ],
        '887d011f': [
            (log,                             ('2.5 - 3.2: Zhao Face Position VB Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        ],
        '76c4a041': [
            (log,                             ('2.5 - 3.1: Zhao Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c4618d41',)),
        ],
        'c4618d41': [
            (log,                             ('3.2: Zhao Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'd3c0fe17': [
            (log,                             ('2.5 - 3.2: Zhao Face Blend VB Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
        ],
        '6f06cdfa': [
            (log,                             ('2.5 - 3.2: Zhao FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9f4efa3', 'Zhao.FaceA.Diffuse.1024')),
        ],
        'b9f4efa3': [
            (log,                             ('2.5 - 3.2: Zhao FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('43c3c5a0', 'Zhao.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f06cdfa', 'Zhao.FaceA.Diffuse.2048')),
        ],

        # ==================== Knife Component ====================
        '4141c5ee': [
            (log,                             ('2.5 - 3.2: Zhao Knife IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1acc9c40': [
            (log,                             ('2.5 - 3.2: Zhao Knife VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
        ],
        '6caf1e01': [
            (log,                             ('2.5 - 3.2: Zhao Knife Position VB Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
        ],
        'b61f8d2c': [
            (log,                             ('2.5 - 3.2: Zhao Knife Texcoord VB Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
        ],
        '0a4341f5': [
            (log,                             ('2.5 - 3.2: Zhao Knife Blend VB Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
        ],
        'fa03bb15': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('61730662', 'Zhao.KnifeA.Diffuse.1024')),
        ],
        '61730662': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fa03bb15', 'Zhao.KnifeA.Diffuse.2048')),
        ],
        'c8892598': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c3cad120', 'Zhao.KnifeA.LightMap.1024')),
        ],
        'c3cad120': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c8892598', 'Zhao.KnifeA.LightMap.2048')),
        ],
        '36b0a2b1': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b900c202', 'Zhao.KnifeA.MaterialMap.1024')),
        ],
        'b900c202': [
            (log,                             ('2.5 - 3.2: Zhao KnifeA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4141c5ee', 'Zhao.Knife.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('36b0a2b1', 'Zhao.KnifeA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Zhao',
    'game_versions': ['2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
