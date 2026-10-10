"""
Promeia Character Hash Commands
ZZZ Mod Fixer v2.8
Game Version: 2.8 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Promeia's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '31178971': [
            (log,                             ('2.8 - 3.2: Promeia Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6cca89ab': [
            (log,                             ('2.8 -> 2.81: Promeia Hair IB Hash',)),
            (update_hash,                     ('31178971',)),
        ],
        '2d4c7c18': [
            (log,                             ('2.8 - 3.2: Promeia Hair Draw VB Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        ],
        '35096cb6': [
            (log,                             ('2.8 -> 2.81: Promeia Hair Position Hash',)),
            (update_hash,                     ('681aceaa',)),
        ],
        '681aceaa': [
            (log,                             ('2.8 - 3.2: Promeia Hair Position VB Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        ],
        '9c0aad96': [
            (log,                             ('2.8 -> 2.81: Promeia Hair Texcoord Hash',)),
            (update_hash,                     ('84d40d91',)),
        ],
        '84d40d91': [
            (log,                             ('2.8 - 3.2: Promeia Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        ],
        '5a263750': [
            (log,                             ('2.8 -> 2.81: Promeia Hair Blend Hash',)),
            (update_hash,                     ('3d4a4881',)),
        ],
        '3d4a4881': [
            (log,                             ('2.8 - 3.2: Promeia Hair Blend VB Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
        ],
        'c96de436': [
            (log,                             ('2.8 - 3.2: Promeia HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a0add414', 'Promeia.HairA.Diffuse.1024')),
        ],
        'a0add414': [
            (log,                             ('2.8 - 3.2: Promeia HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c96de436', 'Promeia.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.8 - 3.2: Promeia HairA, Body(Pinioned)A, Body(Normal)A, ClothesA, LegA and WeaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.Body(Pinioned)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.Body(Normal)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.ClothesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Promeia.WeaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.8 - 3.2: Promeia HairA, Body(Pinioned)A, Body(Normal)A, ClothesA, LegA and WeaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.Body(Pinioned)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.Body(Normal)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.ClothesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Promeia.WeaponA.NormalMap.2048')),
        ],
        'e34356a6': [
            (log,                             ('2.8 - 3.2: Promeia HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5c509f54', 'Promeia.HairA.LightMap.1024')),
        ],
        '5c509f54': [
            (log,                             ('2.8 - 3.2: Promeia HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e34356a6', 'Promeia.HairA.LightMap.2048')),
        ],
        '6bed1450': [
            (log,                             ('2.8 - 3.2: Promeia HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1f96c5d7', 'Promeia.HairA.MaterialMap.1024')),
        ],
        '1f96c5d7': [
            (log,                             ('2.8 - 3.2: Promeia HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('31178971', 'Promeia.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6bed1450', 'Promeia.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        'ff223b2c': [
            (log,                             ('2.8 - 3.2: Promeia HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'de6eb63b': [
            (log,                             ('2.8 -> 2.81: Promeia Shadow IB Hash',)),
            (update_hash,                     ('ff223b2c',)),
        ],
        # HairShadow has no VB hashes and no textures in any database version.

        # ==================== Body(Pinioned) Component ====================
        'b386901d': [
            (log,                             ('3.0 - 3.2: Promeia Body(Pinioned) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '36e794ea': [
            (log,                             ('2.81 -> 3.0: Promeia Pinioned IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('b386901d',)),
        ],
        'a633d5b7': [
            (log,                             ('2.8 -> 2.81: Promeia Pinioned IB Hash',)),
            (update_hash,                     ('36e794ea',)),
        ],
        '19ad87f6': [
            (log,                             ('2.8: Promeia Body(Pinioned) Draw VB Hash',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (update_hash,                     ('dd86f5ae',)),
        ],
        'a7769c93': [
            (log,                             ('2.8 -> 2.81: Promeia Pinioned Position Hash',)),
            (update_hash,                     ('ffaa183a',)),
        ],
        'ffaa183a': [
            (log,                             ('2.8: Promeia Body(Pinioned) Position VB Hash',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (update_hash,                     ('68e2baef',)),
        ],
        'bfcfb2f7': [
            (log,                             ('2.8 -> 2.81: Promeia Pinioned Texcoord Hash',)),
            (update_hash,                     ('2a9842a1',)),
        ],
        '2a9842a1': [
            (log,                             ('2.8: Promeia Body(Pinioned) Texcoord VB Hash',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (update_hash,                     ('6fe5f8c1',)),
        ],
        '61c399b6': [
            (log,                             ('2.8 -> 2.81: Promeia Pinioned Blend Hash',)),
            (update_hash,                     ('dae4abd0',)),
        ],
        'dae4abd0': [
            (log,                             ('2.8: Promeia Body(Pinioned) Blend VB Hash',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (update_hash,                     ('112582ea',)),
        ],
        'dd86f5ae': [
            (log,                             ('3.0 - 3.2: Promeia Body(Pinioned) Draw VB Hash',)),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
        ],
        '68e2baef': [
            (log,                             ('3.0 - 3.2: Promeia Body(Pinioned) Position VB Hash',)),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
        ],
        '6fe5f8c1': [
            (log,                             ('3.0 - 3.2: Promeia Body(Pinioned) Texcoord VB Hash',)),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
        ],
        '112582ea': [
            (log,                             ('3.0 - 3.2: Promeia Body(Pinioned) Blend VB Hash',)),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
        ],
        'ae109401': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d2d3a9e', 'Promeia.Body(Pinioned)A.Diffuse.1024')),
            (multiply_section_if_missing,     ('7d2d3a9e', 'Promeia.Body(Normal)A.Diffuse.1024')),
            (multiply_section_if_missing,     ('7d2d3a9e', 'Promeia.LegA.Diffuse.1024')),
        ],
        '7d2d3a9e': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ae109401', 'Promeia.Body(Pinioned)A.Diffuse.2048')),
            (multiply_section_if_missing,     ('ae109401', 'Promeia.Body(Normal)A.Diffuse.2048')),
            (multiply_section_if_missing,     ('ae109401', 'Promeia.LegA.Diffuse.2048')),
        ],
        '3864f20c': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('70ca6de8', 'Promeia.Body(Pinioned)A.LightMap.1024')),
            (multiply_section_if_missing,     ('70ca6de8', 'Promeia.Body(Normal)A.LightMap.1024')),
            (multiply_section_if_missing,     ('70ca6de8', 'Promeia.LegA.LightMap.1024')),
        ],
        '70ca6de8': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3864f20c', 'Promeia.Body(Pinioned)A.LightMap.2048')),
            (multiply_section_if_missing,     ('3864f20c', 'Promeia.Body(Normal)A.LightMap.2048')),
            (multiply_section_if_missing,     ('3864f20c', 'Promeia.LegA.LightMap.2048')),
        ],
        'd57df6aa': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('af976ad8', 'Promeia.Body(Pinioned)A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('af976ad8', 'Promeia.Body(Normal)A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('af976ad8', 'Promeia.LegA.MaterialMap.1024')),
        ],
        'af976ad8': [
            (log,                             ('2.8 - 3.2: Promeia Body(Pinioned)A, Body(Normal)A and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('36e794ea', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b386901d', 'Promeia.Body(Pinioned).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d57df6aa', 'Promeia.Body(Pinioned)A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d57df6aa', 'Promeia.Body(Normal)A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d57df6aa', 'Promeia.LegA.MaterialMap.2048')),
        ],

        # ==================== Body(Normal) Component ====================
        '10c77d62': [
            (log,                             ('3.0 - 3.2: Promeia Body(Normal) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '62a6b4bd': [
            (log,                             ('2.81 -> 3.0: Promeia Torso IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('10c77d62',)),
        ],
        '6abaa60a': [
            (log,                             ('2.8 -> 2.81: Promeia Torso IB Hash',)),
            (update_hash,                     ('62a6b4bd',)),
        ],
        '9cce6ba2': [
            (log,                             ('2.8 - 3.2: Promeia Body(Normal) Draw VB Hash',)),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
        ],
        'bf938187': [
            (log,                             ('2.8: Promeia Body(Normal) Position VB Hash',)),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (update_hash,                     ('2dbfe8c9',)),
        ],
        'b1ec331c': [
            (log,                             ('2.8 -> 2.81: Promeia Torso Texcoord Hash',)),
            (update_hash,                     ('d99d21e0',)),
        ],
        'd99d21e0': [
            (log,                             ('2.8: Promeia Body(Normal) Texcoord VB Hash',)),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (update_hash,                     ('1fc95f5b',)),
        ],
        'bca960d0': [
            (log,                             ('2.8 -> 2.81: Promeia Torso Blend Hash',)),
            (update_hash,                     ('575d8b1b',)),
        ],
        '575d8b1b': [
            (log,                             ('2.8: Promeia Body(Normal) Blend VB Hash',)),
            (add_section_if_missing,          ('62a6b4bd', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
            (update_hash,                     ('ee35cc06',)),
        ],
        '2dbfe8c9': [
            (log,                             ('3.0 - 3.2: Promeia Body(Normal) Position VB Hash',)),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
        ],
        '1fc95f5b': [
            (log,                             ('3.0 - 3.2: Promeia Body(Normal) Texcoord VB Hash',)),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
        ],
        'ee35cc06': [
            (log,                             ('3.0 - 3.2: Promeia Body(Normal) Blend VB Hash',)),
            (add_section_if_missing,          ('10c77d62', 'Promeia.Body(Normal).IB', 'match_priority = 0\n')),
        ],
        # Body(Normal) shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Clothes Component ====================
        '0ae14c24': [
            (log,                             ('3.0 - 3.2: Promeia Clothes IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '93f1f568': [
            (log,                             ('2.81 -> 3.0: Promeia Clothes IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('0ae14c24',)),
        ],
        '68f34958': [
            (log,                             ('2.8 -> 2.81: Promeia Clothes IB Hash',)),
            (update_hash,                     ('93f1f568',)),
        ],
        '947f29ae': [
            (log,                             ('2.8 - 3.2: Promeia Clothes Draw VB Hash',)),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        ],
        'd43597aa': [
            (log,                             ('2.8 -> 2.81: Promeia Clothes Position Hash',)),
            (update_hash,                     ('1d63183b',)),
        ],
        '1d63183b': [
            (log,                             ('2.8: Promeia Clothes Position VB Hash',)),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f6cc27b6',)),
        ],
        '9f083955': [
            (log,                             ('2.8 -> 2.81: Promeia Clothes Texcoord Hash',)),
            (update_hash,                     ('826446a7',)),
        ],
        '826446a7': [
            (log,                             ('2.8: Promeia Clothes Texcoord VB Hash',)),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (update_hash,                     ('bf00cc95',)),
        ],
        '870f56b5': [
            (log,                             ('2.8 -> 2.81: Promeia Clothes Blend Hash',)),
            (update_hash,                     ('58f42be3',)),
        ],
        '58f42be3': [
            (log,                             ('2.8: Promeia Clothes Blend VB Hash',)),
            (add_section_if_missing,          ('93f1f568', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (update_hash,                     ('4b0d6867',)),
        ],
        'f6cc27b6': [
            (log,                             ('3.0 - 3.2: Promeia Clothes Position VB Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        ],
        'bf00cc95': [
            (log,                             ('3.0 - 3.2: Promeia Clothes Texcoord VB Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        ],
        '4b0d6867': [
            (log,                             ('3.0 - 3.2: Promeia Clothes Blend VB Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
        ],
        'b9367016': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA Diffuse 2048p Hash',)),
            (update_hash,                     ('e1492a53',)),
        ],
        'e1492a53': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('47d294f4', '406b1373'), 'Promeia.ClothesA.Diffuse.1024')),
        ],
        '406b1373': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA Diffuse 1024p Hash',)),
            (update_hash,                     ('47d294f4',)),
        ],
        '47d294f4': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('e1492a53', 'b9367016'), 'Promeia.ClothesA.Diffuse.2048')),
        ],
        'd743acd0': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA LightMap 2048p Hash',)),
            (update_hash,                     ('9bf7f5cc',)),
        ],
        '9bf7f5cc': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('562616d5', '044d2d39'), 'Promeia.ClothesA.LightMap.1024')),
        ],
        '044d2d39': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA LightMap 1024p Hash',)),
            (update_hash,                     ('562616d5',)),
        ],
        '562616d5': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('9bf7f5cc', 'd743acd0'), 'Promeia.ClothesA.LightMap.2048')),
        ],
        '31d7cbad': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA MaterialMap 2048p Hash',)),
            (update_hash,                     ('d37b40a9',)),
        ],
        'd37b40a9': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('73aaae54', '01a5ba27'), 'Promeia.ClothesA.MaterialMap.1024')),
        ],
        '01a5ba27': [
            (log,                             ('2.8 -> 3.0: Promeia ClothesA MaterialMap 1024p Hash',)),
            (update_hash,                     ('73aaae54',)),
        ],
        '73aaae54': [
            (log,                             ('3.0 - 3.2: Promeia ClothesA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('0ae14c24', 'Promeia.Clothes.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d37b40a9', '31d7cbad'), 'Promeia.ClothesA.MaterialMap.2048')),
        ],
        # Clothes shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Leg Component ====================
        'ec003379': [
            (log,                             ('3.0 - 3.2: Promeia Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fd054d1d': [
            (log,                             ('2.81 -> 3.0: Promeia Leg IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('ec003379',)),
        ],
        '21871660': [
            (log,                             ('2.8 -> 2.81: Promeia Leg IB Hash',)),
            (update_hash,                     ('fd054d1d',)),
        ],
        'dfb01010': [
            (log,                             ('2.8 - 3.2: Promeia Leg Draw VB Hash',)),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        ],
        '595bd76e': [
            (log,                             ('2.8 -> 2.81: Promeia Leg Position Hash',)),
            (update_hash,                     ('0b822797',)),
        ],
        '0b822797': [
            (log,                             ('2.8: Promeia Leg Position VB Hash',)),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('4c1d0a70',)),
        ],
        '2918714e': [
            (log,                             ('2.8 -> 2.81: Promeia Leg Texcoord Hash',)),
            (update_hash,                     ('f5fd0e92',)),
        ],
        'f5fd0e92': [
            (log,                             ('2.8: Promeia Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('03d6f933',)),
        ],
        'fd3c3d9f': [
            (log,                             ('2.8 -> 2.81: Promeia Leg Blend Hash',)),
            (update_hash,                     ('9839b071',)),
        ],
        '9839b071': [
            (log,                             ('2.8: Promeia Leg Blend VB Hash',)),
            (add_section_if_missing,          ('fd054d1d', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('65bba179',)),
        ],
        '4c1d0a70': [
            (log,                             ('3.0 - 3.2: Promeia Leg Position VB Hash',)),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        ],
        '03d6f933': [
            (log,                             ('3.0 - 3.2: Promeia Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        ],
        '65bba179': [
            (log,                             ('3.0 - 3.2: Promeia Leg Blend VB Hash',)),
            (add_section_if_missing,          ('ec003379', 'Promeia.Leg.IB', 'match_priority = 0\n')),
        ],
        # Leg shares its NormalMap, Diffuse, LightMap and MaterialMap hashes with Body(Pinioned) and Body(Normal); see those Components above.

        # ==================== Eyebrow Component ====================
        'e032287a': [
            (log,                             ('2.8 - 3.2: Promeia Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cb9d17fc': [
            (log,                             ('2.8 -> 2.81: Promeia Eyebrow IB Hash',)),
            (update_hash,                     ('e032287a',)),
        ],
        'a1d5b256': [
            (log,                             ('2.8 - 3.2: Promeia Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '9bc72111': [
            (log,                             ('2.8 - 3.2: Promeia Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '3a00aa76': [
            (log,                             ('2.8 -> 2.81: Promeia Eyebrow Texcoord Hash',)),
            (update_hash,                     ('d3d65ca5',)),
        ],
        'd3d65ca5': [
            (log,                             ('2.8 - 3.1: Promeia Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('644e5029',)),
        ],
        '644e5029': [
            (log,                             ('3.2: Promeia Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '42594132': [
            (log,                             ('2.8 - 3.2: Promeia Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '9b293811': [
            (log,                             ('2.8 - 3.2: Promeia EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('328fa0cf', 'Promeia.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('328fa0cf', 'Promeia.FaceA.Diffuse.1024')),
        ],
        '328fa0cf': [
            (log,                             ('2.8 - 3.2: Promeia EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e032287a', 'Promeia.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9b293811', 'Promeia.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('9b293811', 'Promeia.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'ef3c4506': [
            (log,                             ('2.8 - 3.2: Promeia Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5ea47a32': [
            (log,                             ('2.8 -> 2.81: Promeia Face IB Hash',)),
            (update_hash,                     ('ef3c4506',)),
        ],
        '32a38de6': [
            (log,                             ('2.8 - 3.2: Promeia Face Draw VB Hash',)),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
        ],
        '08b11ea1': [
            (log,                             ('2.8 - 3.2: Promeia Face Position VB Hash',)),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
        ],
        'b7a6479f': [
            (log,                             ('2.8 -> 2.81: Promeia Face Texcoord Hash',)),
            (update_hash,                     ('dcd61276',)),
        ],
        'dcd61276': [
            (log,                             ('2.8 - 3.1: Promeia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('6ca475b9',)),
        ],
        '6ca475b9': [
            (log,                             ('3.2: Promeia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '5ff41c34': [
            (log,                             ('2.8 -> 2.81: Promeia Face Blend Hash',)),
            (update_hash,                     ('bf5b785d',)),
        ],
        'bf5b785d': [
            (log,                             ('2.8 - 3.2: Promeia Face Blend VB Hash',)),
            (add_section_if_missing,          ('ef3c4506', 'Promeia.Face.IB', 'match_priority = 0\n')),
        ],
        # Face has three object groups with identical textures and shares its Diffuse hashes with Eyebrow; see that Component above.

        # ==================== Weapon Component ====================
        '8995db58': [
            (log,                             ('2.8 - 3.2: Promeia Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '947ceb88': [
            (log,                             ('2.8 -> 2.81: Promeia Weapon IB Hash',)),
            (update_hash,                     ('8995db58',)),
        ],
        '7d76d686': [
            (log,                             ('2.8 -> 2.81: Promeia Weapon Draw Hash',)),
            (update_hash,                     ('0a06059e',)),
        ],
        '0a06059e': [
            (log,                             ('2.8 - 3.0: Promeia Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        ],
        '2f3a560d': [
            (log,                             ('2.8 -> 2.81: Promeia Weapon Position Hash',)),
            (update_hash,                     ('d242b77a',)),
        ],
        'd242b77a': [
            (log,                             ('2.8: Promeia Weapon Position VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('35ecba91',)),
        ],
        '23587131': [
            (log,                             ('2.8 -> 2.81: Promeia Weapon Texcoord Hash',)),
            (update_hash,                     ('f2f5bd28',)),
        ],
        'f2f5bd28': [
            (log,                             ('2.8: Promeia Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('064658e2',)),
        ],
        '21ac80fa': [
            (log,                             ('2.8 -> 2.81: Promeia Weapon Blend Hash',)),
            (update_hash,                     ('a864dc82',)),
        ],
        'a864dc82': [
            (log,                             ('2.8 - 3.0: Promeia Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        ],
        '35ecba91': [
            (log,                             ('3.0: Promeia Weapon Position VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        ],
        '064658e2': [
            (log,                             ('3.0: Promeia Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
        ],
        'd1399215': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA Diffuse 2048p Hash',)),
            (update_hash,                     ('328135c5',)),
        ],
        '328135c5': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7750fc88', '138bcaa1'), 'Promeia.WeaponA.Diffuse.1024')),
        ],
        '138bcaa1': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA Diffuse 1024p Hash',)),
            (update_hash,                     ('7750fc88',)),
        ],
        '7750fc88': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('328135c5', 'd1399215'), 'Promeia.WeaponA.Diffuse.2048')),
        ],
        '369f0efd': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA LightMap 2048p Hash',)),
            (update_hash,                     ('82f4146a',)),
        ],
        '82f4146a': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a1988612', '5e59380e'), 'Promeia.WeaponA.LightMap.1024')),
        ],
        '5e59380e': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA LightMap 1024p Hash',)),
            (update_hash,                     ('a1988612',)),
        ],
        'a1988612': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('82f4146a', '369f0efd'), 'Promeia.WeaponA.LightMap.2048')),
        ],
        'a179a69c': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA MaterialMap 2048p Hash',)),
            (update_hash,                     ('d672b87c',)),
        ],
        'd672b87c': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7559d574', '09271c02'), 'Promeia.WeaponA.MaterialMap.1024')),
        ],
        '09271c02': [
            (log,                             ('2.8 -> 3.0: Promeia WeaponA MaterialMap 1024p Hash',)),
            (update_hash,                     ('7559d574',)),
        ],
        '7559d574': [
            (log,                             ('3.0 - 3.2: Promeia WeaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('8995db58', 'Promeia.Weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d672b87c', 'a179a69c'), 'Promeia.WeaponA.MaterialMap.2048')),
        ],
        # Weapon shares its NormalMap hashes with Hair; see that Component above.

    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Promeia',
    'game_versions': ['2.8', '3.0', '3.1', '3.2'],
}
