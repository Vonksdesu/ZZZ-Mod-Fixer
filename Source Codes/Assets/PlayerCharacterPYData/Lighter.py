"""
Lighter Character Hash Commands
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
    Returns Lighter's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '542b8aa9': [
            (log,                             ('2.2 - 3.2: Lighter Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd669b85': [
            (log,                             ('2.2 - 3.2: Lighter Hair Draw VB Hash',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        ],
        '037b6287': [
            (log,                             ('2.2 - 3.2: Lighter Hair Position VB Hash',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        ],
        '22a08e39': [
            (log,                             ('2.2 - 3.2: Lighter Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        ],
        'd88fa0aa': [
            (log,                             ('2.2 - 3.2: Lighter Hair Blend VB Hash',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
        ],
        'c5d60a1d': [
            (log,                             ('2.7 -> 2.8: Lighter HairA and CloakA Diffuse 2048p Hash (shared)',)),
            (update_hash,                     ('4e088042',)),
        ],
        '4e088042': [
            (log,                             ('2.8 - 3.2: Lighter HairA and CloakA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0ee07935', '1cd2d442'), 'Lighter.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('0ee07935', '1cd2d442'), 'Lighter.CloakA.Diffuse.1024')),
        ],
        '1cd2d442': [
            (log,                             ('2.7 -> 2.8: Lighter HairA and CloakA Diffuse 1024p Hash (shared)',)),
            (update_hash,                     ('0ee07935',)),
        ],
        '0ee07935': [
            (log,                             ('2.8 - 3.2: Lighter HairA and CloakA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('4e088042', 'c5d60a1d'), 'Lighter.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('4e088042', 'c5d60a1d'), 'Lighter.CloakA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Lighter HairA, BodyA, CloakA, GlassesA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Lighter.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lighter.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lighter.CloakA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lighter.GlassesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lighter.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Lighter HairA, BodyA, CloakA, GlassesA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Lighter.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lighter.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lighter.CloakA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lighter.GlassesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lighter.weapon.NormalMap.2048')),
        ],
        '6d3f91bc': [
            (log,                             ('2.2 - 3.2: Lighter HairA and CloakA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('62ec7f01', 'Lighter.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('62ec7f01', 'Lighter.CloakA.LightMap.1024')),
        ],
        '62ec7f01': [
            (log,                             ('2.2 - 3.2: Lighter HairA and CloakA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d3f91bc', 'Lighter.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('6d3f91bc', 'Lighter.CloakA.LightMap.2048')),
        ],
        'd5ba9ea6': [
            (log,                             ('2.7 -> 2.8: Lighter HairA and CloakA MaterialMap 2048p Hash (shared)',)),
            (update_hash,                     ('d331b850',)),
        ],
        'd331b850': [
            (log,                             ('2.8 - 3.2: Lighter HairA and CloakA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('99ad14f1', '8687f7b8'), 'Lighter.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('99ad14f1', '8687f7b8'), 'Lighter.CloakA.MaterialMap.1024')),
        ],
        '8687f7b8': [
            (log,                             ('2.7 -> 2.8: Lighter HairA and CloakA MaterialMap 1024p Hash (shared)',)),
            (update_hash,                     ('99ad14f1',)),
        ],
        '99ad14f1': [
            (log,                             ('2.8 - 3.2: Lighter HairA and CloakA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('542b8aa9', 'Lighter.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d331b850', 'd5ba9ea6'), 'Lighter.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('d331b850', 'd5ba9ea6'), 'Lighter.CloakA.MaterialMap.2048')),
        ],
        # Cloak shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Hair; see that Component above.

        # ==================== Hair Shadow Component ====================
        'cf4c4714': [
            (log,                             ('2.2 - 3.2: Lighter Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4104c8e0': [
            (log,                             ('2.2 - 3.2: Lighter Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('cf4c4714', 'Lighter.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'e144ad1c': [
            (log,                             ('2.2 - 3.2: Lighter Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('cf4c4714', 'Lighter.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '7749cb20': [
            (log,                             ('2.2 - 3.2: Lighter Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('cf4c4714', 'Lighter.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '3abed50b': [
            (log,                             ('2.2 - 3.2: Lighter Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('cf4c4714', 'Lighter.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '8899e0fd': [
            (log,                             ('2.2 - 3.2: Lighter Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '84ed822e': [
            (log,                             ('2.2 - 3.2: Lighter Body Draw VB Hash',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        ],
        'f6bbabb5': [
            (log,                             ('2.2 - 3.2: Lighter Body Position VB Hash',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        ],
        '5e461440': [
            (log,                             ('1.5 -> 1.6: Lighter Body Position Hash',)),
            (update_hash,                     ('f6bbabb5',)),
        ],
        '0baec6b7': [
            (log,                             ('1.3 -> 1.4: Lighter Body Position Hash',)),
            (update_hash,                     ('5e461440',)),
        ],
        'e1ae7f38': [
            (log,                             ('2.2 - 3.2: Lighter Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        ],
        '25ad7289': [
            (log,                             ('1.5 -> 1.6: Lighter Body Texcoord Hash',)),
            (update_hash,                     ('e1ae7f38',)),
        ],
        '710bca71': [
            (log,                             ('1.3 -> 1.4: Lighter Body Texcoord Hash',)),
            (update_hash,                     ('25ad7289',)),
        ],
        'da216bb6': [
            (log,                             ('2.2 - 3.2: Lighter Body Blend VB Hash',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
        ],
        '5ed96bf2': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be46890b', 'Lighter.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('be46890b', 'Lighter.GlassesA.Diffuse.1024')),
        ],
        'be46890b': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ed96bf2', 'Lighter.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5ed96bf2', 'Lighter.GlassesA.Diffuse.2048')),
        ],
        'da6f4dc0': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b828635', 'Lighter.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('5b828635', 'Lighter.GlassesA.LightMap.1024')),
        ],
        '5b828635': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('da6f4dc0', 'Lighter.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('da6f4dc0', 'Lighter.GlassesA.LightMap.2048')),
        ],
        '94aebd7e': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('65f3bb7c', 'Lighter.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('65f3bb7c', 'Lighter.GlassesA.MaterialMap.1024')),
        ],
        '65f3bb7c': [
            (log,                             ('2.2 - 3.2: Lighter BodyA and GlassesA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8899e0fd', 'Lighter.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('94aebd7e', 'Lighter.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('94aebd7e', 'Lighter.GlassesA.MaterialMap.2048')),
        ],
        # Body and Glasses share their NormalMap hashes with Hair; see that Component above.

        # ==================== Cloak Component ====================
        '2de659bd': [
            (log,                             ('2.2 - 3.2: Lighter Cloak IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '701ad22d': [
            (log,                             ('2.2 - 3.2: Lighter Cloak Draw VB Hash',)),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        ],
        'b642df39': [
            (log,                             ('2.2 - 3.2: Lighter Cloak Position VB Hash',)),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        ],
        '1f9a45b3': [
            (log,                             ('2.2 - 3.2: Lighter Cloak Texcoord VB Hash',)),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        ],
        '609ecf0b': [
            (log,                             ('2.2 - 3.2: Lighter Cloak Blend VB Hash',)),
            (add_section_if_missing,          ('2de659bd', 'Lighter.Cloak.IB', 'match_priority = 0\n')),
        ],

        # ==================== Glasses Component ====================
        'b20b7cd5': [
            (log,                             ('2.2 - 3.2: Lighter Glasses IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '62623b11': [
            (log,                             ('2.2 - 3.2: Lighter Glasses Draw VB Hash',)),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
        ],
        'fc862707': [
            (log,                             ('2.2 - 3.2: Lighter Glasses Position VB Hash',)),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
        ],
        '527dad23': [
            (log,                             ('2.2 - 3.2: Lighter Glasses Texcoord VB Hash',)),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
        ],
        '3395524c': [
            (log,                             ('2.2 - 3.2: Lighter Glasses Blend VB Hash',)),
            (add_section_if_missing,          ('b20b7cd5', 'Lighter.Glasses.IB', 'match_priority = 0\n')),
        ],
        # Glasses shares its Diffuse, LightMap, MaterialMap and NormalMap hashes with Body and Hair; see those Components above.

        # ==================== Face Component ====================
        'dcc7bb78': [
            (log,                             ('2.2 - 3.2: Lighter Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '039f30cf': [
            (log,                             ('1.3 -> 1.4: Lighter Face IB Hash',)),
            (update_hash,                     ('dcc7bb78',)),
        ],
        'aa77af05': [
            (log,                             ('2.2 - 3.2: Lighter Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
        ],
        '90653c42': [
            (log,                             ('2.2 - 2.7: Lighter Face Position VB Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
        ],
        '7bbe9c75': [
            (log,                             ('1.6 -> 2.0: Lighter Face Position Hash',)),
            (update_hash,                     ('90653c42',)),
        ],
        'af14829b': [
            (log,                             ('2.2 - 3.0: Lighter Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('04cc2dfd',)),
        ],
        '04cc2dfd': [
            (log,                             ('3.1: Lighter Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
        ],
        '7edbb44e': [
            (log,                             ('2.2 - 3.2: Lighter Face Blend VB Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
        ],
        '4524e91a': [
            (log,                             ('2.2 - 3.2: Lighter FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8ec33dd0', 'Lighter.FaceA.Diffuse.1024')),
        ],
        '8ec33dd0': [
            (log,                             ('2.2 - 3.2: Lighter FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dcc7bb78', 'Lighter.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4524e91a', 'Lighter.FaceA.Diffuse.2048')),
        ],
        # Face has no NormalMap, LightMap or MaterialMap hashes; Diffuse is its only texture.

        # ==================== Weapon Component ====================
        '018b03f0': [
            (log,                             ('2.2 - 3.2: Lighter weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '390caccd': [
            (log,                             ('2.2 - 3.2: Lighter weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
        ],
        '5841afbd': [
            (log,                             ('2.2 - 3.2: Lighter weapon Position VB Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
        ],
        '88aecee2': [
            (log,                             ('2.2 - 3.2: Lighter weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
        ],
        'af2e48a6': [
            (log,                             ('1.3 -> 1.4: Lighter weapon Texcoord Hash',)),
            (update_hash,                     ('88aecee2',)),
        ],
        'e83ca18e': [
            (log,                             ('2.2 - 3.2: Lighter weapon Blend VB Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
        ],
        '8b854866': [
            (log,                             ('2.2 - 3.2: Lighter weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6506987b', 'Lighter.weapon.Diffuse.1024')),
        ],
        '6506987b': [
            (log,                             ('2.2 - 3.2: Lighter weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b854866', 'Lighter.weapon.Diffuse.2048')),
        ],
        '547cbcd8': [
            (log,                             ('2.2 - 3.2: Lighter weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('939a2e18', 'Lighter.weapon.LightMap.1024')),
        ],
        '939a2e18': [
            (log,                             ('2.2 - 3.2: Lighter weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('547cbcd8', 'Lighter.weapon.LightMap.2048')),
        ],
        '3617c303': [
            (log,                             ('2.2 - 3.2: Lighter weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1684d3e4', 'Lighter.weapon.MaterialMap.1024')),
        ],
        '1684d3e4': [
            (log,                             ('2.2 - 3.2: Lighter weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('018b03f0', 'Lighter.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3617c303', 'Lighter.weapon.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lighter',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
