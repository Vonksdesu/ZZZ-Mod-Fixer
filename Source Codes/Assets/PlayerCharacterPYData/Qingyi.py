"""
Qingyi Character Hash Commands
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
    Returns Qingyi's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '3cacba0a': [
            (log,                             ('2.2 - 3.2: Qingyi Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '33f6d1f2': [
            (log,                             ('2 -> 1.1: Qingyi Hair IB Hash',)),
            (update_hash,                     ('3cacba0a',)),
        ],
        '6a52010a': [
            (log,                             ('2 -> 1.1: Qingyi Hair Draw Hash',)),
            (update_hash,                     ('7b43d317',)),
        ],
        '7b43d317': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Draw VB Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        ],
        'b6e5374d': [
            (log,                             ('2 -> 1.1: Qingyi Hair Position Hash',)),
            (update_hash,                     ('dd08951b',)),
        ],
        'dd08951b': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Position VB Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        ],
        'dae0117f': [
            (log,                             ('2 -> 1.1: Qingyi Hair Texcoord Hash',)),
            (update_hash,                     ('0643440c',)),
        ],
        '0643440c': [
            (log,                             ('1.1 -> 1.2: Qingyi Hair Texcoord Hash',)),
            (update_hash,                     ('53a2b66e',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_12_shrink_texcoord_color,    ('1.2',)),
        ],
        '53a2b66e': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        ],
        'd196bd5c': [
            (log,                             ('2 -> 1.1: Qingyi Hair Blend Hash',)),
            (update_hash,                     ('6e7650bc',)),
        ],
        '6e7650bc': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Blend VB Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
        ],
        '3212a0ca': [
            (log,                             ('2.2 - 3.2: Qingyi HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a472db9a', 'Qingyi.HairA.Diffuse.1024')),
        ],
        'a472db9a': [
            (log,                             ('2.2 - 3.2: Qingyi HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3212a0ca', 'Qingyi.HairA.Diffuse.2048')),
        ],
        '2910fbd0': [
            (log,                             ('1.1 -> 2.5: Qingyi HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'fc1847a9': [
            (log,                             ('1.1 -> 2.5: Qingyi HairA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Qingyi HairA, BodyA, kettleA and weapon - 武器A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', 'fc1847a9', '4fbf05be'), 'Qingyi.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', 'fc1847a9', '4fbf05be'), 'Qingyi.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', 'fc1847a9', '4fbf05be'), 'Qingyi.kettleA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', 'fc1847a9', '4fbf05be'), 'Qingyi.weapon - 武器A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Qingyi HairA, BodyA, kettleA and weapon - 武器A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '2910fbd0', '542c6b04'), 'Qingyi.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '2910fbd0', '542c6b04'), 'Qingyi.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '2910fbd0', '542c6b04'), 'Qingyi.kettleA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '2910fbd0', '542c6b04'), 'Qingyi.weapon - 武器A.NormalMap.2048')),
        ],
        '6e3ac847': [
            (log,                             ('2.2 - 3.2: Qingyi HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('683414c1', 'Qingyi.HairA.LightMap.1024')),
        ],
        '683414c1': [
            (log,                             ('2.2 - 3.2: Qingyi HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6e3ac847', 'Qingyi.HairA.LightMap.2048')),
        ],
        '4a77fd3b': [
            (log,                             ('2.2 - 3.2: Qingyi HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bfefa200', 'Qingyi.HairA.MaterialMap.1024')),
        ],
        'bfefa200': [
            (log,                             ('2.2 - 3.2: Qingyi HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3cacba0a', 'Qingyi.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a77fd3b', 'Qingyi.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '0a94bfd8': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '472bb581': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '0971a397': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ee99ded9': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'b7ce94d8': [
            (log,                             ('2.2 - 3.2: Qingyi Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('0a94bfd8', 'Qingyi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '195857d8': [
            (log,                             ('2.2 - 3.2: Qingyi Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd915de65': [
            (log,                             ('1 -> 1.1: Qingyi Body IB Hash',)),
            (update_hash,                     ('195857d8',)),
        ],
        'b1f382cd': [
            (log,                             ('1 -> 1.1: Qingyi Body Draw Hash',)),
            (update_hash,                     ('7be61bce',)),
        ],
        '7be61bce': [
            (log,                             ('2.2 - 3.2: Qingyi Body Draw VB Hash',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        ],
        'dd421c3a': [
            (log,                             ('1 -> 1.1: Qingyi Body Position Hash',)),
            (update_hash,                     ('ac54012f',)),
        ],
        'ac54012f': [
            (log,                             ('2.2 - 3.2: Qingyi Body Position VB Hash',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        ],
        '00487185': [
            (log,                             ('1 -> 1.1: Qingyi Body Texcoord Hash',)),
            (update_hash,                     ('4cbe7fbe',)),
        ],
        '4cbe7fbe': [
            (log,                             ('2.2 - 3.2: Qingyi Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        ],
        '0287b8fb': [
            (log,                             ('1 -> 1.1: Qingyi Body Blend Hash',)),
            (update_hash,                     ('88a6f633',)),
        ],
        '88a6f633': [
            (log,                             ('2.2 - 3.2: Qingyi Body Blend VB Hash',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
        ],
        '1fa7e18e': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa3c1147', 'Qingyi.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('aa3c1147', 'Qingyi.kettleA.Diffuse.1024')),
        ],
        'aa3c1147': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fa7e18e', 'Qingyi.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1fa7e18e', 'Qingyi.kettleA.Diffuse.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        '542c6b04': [
            (log,                             ('1.1 -> 2.5: Qingyi BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '4fbf05be': [
            (log,                             ('1.1 -> 2.5: Qingyi BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        '35c2a022': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a484257', 'Qingyi.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('4a484257', 'Qingyi.kettleA.LightMap.1024')),
        ],
        '4a484257': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('35c2a022', 'Qingyi.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('35c2a022', 'Qingyi.kettleA.LightMap.2048')),
        ],
        '41054bb6': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4e561ee5', 'Qingyi.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('4e561ee5', 'Qingyi.kettleA.MaterialMap.1024')),
        ],
        '4e561ee5': [
            (log,                             ('2.2 - 3.2: Qingyi BodyA and kettleA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('195857d8', 'Qingyi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('41054bb6', 'Qingyi.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('41054bb6', 'Qingyi.kettleA.MaterialMap.2048')),
        ],

        # ==================== kettle Component ====================
        '8e8426df': [
            (log,                             ('2.2 - 3.2: Qingyi kettle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fca2b042': [
            (log,                             ('2.2 - 3.2: Qingyi kettle Draw VB Hash',)),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
        ],
        '24282218': [
            (log,                             ('2.2 - 3.2: Qingyi kettle Position VB Hash',)),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
        ],
        '1707933f': [
            (log,                             ('2.2 - 3.2: Qingyi kettle Texcoord VB Hash',)),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
        ],
        '807eb474': [
            (log,                             ('2.2 - 3.2: Qingyi kettle Blend VB Hash',)),
            (add_section_if_missing,          ('8e8426df', 'Qingyi.kettle.IB', 'match_priority = 0\n')),
        ],
        # kettle shares its Diffuse, LightMap and MaterialMap hashes with Body, and its NormalMap
        # hashes are shared with Hair; see those Components above.

        # ==================== Face Component ====================
        'f6e96452': [
            (log,                             ('2.2 - 3.2: Qingyi Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f6aa443': [
            (log,                             ('2.2 - 3.2: Qingyi Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
        ],
        'a5783704': [
            (log,                             ('2.2 - 3.2: Qingyi Face Position VB Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
        ],
        '6a492df0': [
            (log,                             ('3.0 -> 3.1: Qingyi Face Texcoord Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('db1f2dfa',)),
        ],
        'db1f2dfa': [
            (log,                             ('3.1: Qingyi Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
        ],
        '57c9f0a3': [
            (log,                             ('2.2 - 3.2: Qingyi Face Blend VB Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
        ],
        '0b75cd32': [
            (log,                             ('2.2 - 3.2: Qingyi FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a58b5444', 'Qingyi.FaceA.Diffuse.1024')),
        ],
        'a58b5444': [
            (log,                             ('2.2 - 3.2: Qingyi FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f6e96452', 'Qingyi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0b75cd32', 'Qingyi.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        '6b62986f': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e5a4128b': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        'fb916456': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器 Position VB Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        '8658ef62': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器 Texcoord VB Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        'f75514db': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器 Blend VB Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        '330dfe54': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('46406a81', 'Qingyi.weapon - 武器A.Diffuse.1024')),
        ],
        '46406a81': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('330dfe54', 'Qingyi.weapon - 武器A.Diffuse.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
        '2d703fde': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22b43462', 'Qingyi.weapon - 武器A.LightMap.1024')),
        ],
        '22b43462': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2d703fde', 'Qingyi.weapon - 武器A.LightMap.2048')),
        ],
        '8d6da65b': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('39e8fda1', 'Qingyi.weapon - 武器A.MaterialMap.1024')),
        ],
        '39e8fda1': [
            (log,                             ('2.2 - 3.2: Qingyi weapon - 武器A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6b62986f', 'Qingyi.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d6da65b', 'Qingyi.weapon - 武器A.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Qingyi',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
