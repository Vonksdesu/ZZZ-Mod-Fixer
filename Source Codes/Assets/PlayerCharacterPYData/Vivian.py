"""
Vivian Character Hash Commands
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
    Returns Vivian's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'c4eb6168': [
            (log,                             ('2.2 - 3.2: Vivian Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2e01f7f7': [
            (log,                             ('2.2 - 3.2: Vivian Hair Draw VB Hash',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        ],
        '71d0dfd9': [
            (log,                             ('2.2 - 3.2: Vivian Hair Position VB Hash',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        ],
        '406beb54': [
            (log,                             ('2.2 - 3.2: Vivian Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        ],
        'ef4a8bb6': [
            (log,                             ('2.2 - 3.2: Vivian Hair Blend VB Hash',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
        ],
        'a84d933f': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2df6f7b5', 'Vivian.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('2df6f7b5', 'Vivian.GemA.Diffuse.1024')),
        ],
        '2df6f7b5': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a84d933f', 'Vivian.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('a84d933f', 'Vivian.GemA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Vivian HairA, BodyA, GemA, weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.GemA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.weapon - 伞柄展开A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.weapon - 伞柄收起A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.weapon - 伞面A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.weapon - sword剑A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Vivian.weapon - 喷射器A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Vivian HairA, BodyA, GemA, weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.GemA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.weapon - 伞柄展开A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.weapon - 伞柄收起A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.weapon - 伞面A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.weapon - sword剑A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Vivian.weapon - 喷射器A.NormalMap.2048')),
        ],
        '8e3a20ea': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('36b80366', 'Vivian.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('36b80366', 'Vivian.GemA.LightMap.1024')),
        ],
        '36b80366': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8e3a20ea', 'Vivian.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('8e3a20ea', 'Vivian.GemA.LightMap.2048')),
        ],
        '2af66072': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2d5b1412', 'Vivian.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2d5b1412', 'Vivian.GemA.MaterialMap.1024')),
        ],
        '2d5b1412': [
            (log,                             ('2.2 - 3.2: Vivian HairA and GemA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c4eb6168', 'Vivian.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2af66072', 'Vivian.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('2af66072', 'Vivian.GemA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '548f7dff': [
            (log,                             ('2.2 - 3.2: Vivian Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b1bf0e1a': [
            (log,                             ('2.2 - 3.2: Vivian Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a544d14e': [
            (log,                             ('2.2 - 3.2: Vivian Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '4a5054ba': [
            (log,                             ('2.2 - 3.2: Vivian Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '2376d129': [
            (log,                             ('2.2 - 3.2: Vivian Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('548f7dff', 'Vivian.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'cd609d98': [
            (log,                             ('2.2 - 3.2: Vivian Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5c34690a': [
            (log,                             ('2.2 - 3.2: Vivian Body Draw VB Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        ],
        '64a6b06d': [
            (log,                             ('2.2 - 3.2: Vivian Body Position VB Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        ],
        '55dae493': [
            (log,                             ('2.2 - 3.2: Vivian Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        ],
        'e7122fe8': [
            (log,                             ('2.2 - 3.2: Vivian Body Blend VB Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
        ],
        '0635e2dd': [
            (log,                             ('2.2 - 3.2: Vivian BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('da41fbd6', 'Vivian.BodyA.Diffuse.1024')),
        ],
        'da41fbd6': [
            (log,                             ('2.2 - 3.2: Vivian BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0635e2dd', 'Vivian.BodyA.Diffuse.2048')),
        ],
        'e21c3a6b': [
            (log,                             ('2.2 - 3.2: Vivian BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a86e169', 'Vivian.BodyA.LightMap.1024')),
        ],
        '4a86e169': [
            (log,                             ('2.2 - 3.2: Vivian BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e21c3a6b', 'Vivian.BodyA.LightMap.2048')),
        ],
        '81f7d37c': [
            (log,                             ('2.2 - 3.2: Vivian BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fa650e6c', 'Vivian.BodyA.MaterialMap.1024')),
        ],
        'fa650e6c': [
            (log,                             ('2.2 - 3.2: Vivian BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('cd609d98', 'Vivian.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81f7d37c', 'Vivian.BodyA.MaterialMap.2048')),
        ],

        # ==================== Gem Component ====================
        '14602a61': [
            (log,                             ('2.2 - 3.2: Vivian Gem IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8a6fd2f9': [
            (log,                             ('2.2 - 3.2: Vivian Gem Draw VB Hash',)),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        ],
        '3c32547b': [
            (log,                             ('2.2 - 3.2: Vivian Gem Position VB Hash',)),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        ],
        '45c0ac67': [
            (log,                             ('2.2 - 3.2: Vivian Gem Texcoord VB Hash',)),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        ],
        'a23da1ce': [
            (log,                             ('2.2 - 3.2: Vivian Gem Blend VB Hash',)),
            (add_section_if_missing,          ('14602a61', 'Vivian.Gem.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '39944f20': [
            (log,                             ('2.2 - 3.2: Vivian Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fcf74fc0': [
            (log,                             ('2.2 - 3.2: Vivian Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        ],
        'c6e5dc87': [
            (log,                             ('2.2 - 3.2: Vivian Face Position VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        ],
        '0afe5a44': [
            (log,                             ('2.2 - 3.1: Vivian Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('50c5d703',)),
        ],
        '50c5d703': [
            (log,                             ('3.2: Vivian Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ef07b6f6': [
            (log,                             ('2.2 - 3.2: Vivian Face Blend VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
        ],
        '7b262ab6': [
            (log,                             ('2.2 - 3.2: Vivian FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('66b5da8e', 'Vivian.FaceA.Diffuse.1024')),
        ],
        '66b5da8e': [
            (log,                             ('2.2 - 3.2: Vivian FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('39944f20', 'Vivian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7b262ab6', 'Vivian.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 伞柄展开 Component ====================
        '1b843cb1': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '66cc3370': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
        ],
        '7c80f1d8': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开 Position VB Hash',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
        ],
        '79ee2ea7': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开 Texcoord VB Hash',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
        ],
        '5d4a63ca': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开 Blend VB Hash',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
        ],
        'e2327fb8': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf6a1304', 'Vivian.weapon - 伞柄展开A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf6a1304', 'Vivian.weapon - 伞柄收起A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf6a1304', 'Vivian.weapon - 伞面A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf6a1304', 'Vivian.weapon - sword剑A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bf6a1304', 'Vivian.weapon - 喷射器A.Diffuse.1024')),
        ],
        'bf6a1304': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e2327fb8', 'Vivian.weapon - 伞柄展开A.Diffuse.2048')),
            (multiply_section_if_missing,     ('e2327fb8', 'Vivian.weapon - 伞柄收起A.Diffuse.2048')),
            (multiply_section_if_missing,     ('e2327fb8', 'Vivian.weapon - 伞面A.Diffuse.2048')),
            (multiply_section_if_missing,     ('e2327fb8', 'Vivian.weapon - sword剑A.Diffuse.2048')),
            (multiply_section_if_missing,     ('e2327fb8', 'Vivian.weapon - 喷射器A.Diffuse.2048')),
        ],
        '9277a2c1': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a33edccd', 'Vivian.weapon - 伞柄展开A.LightMap.1024')),
            (multiply_section_if_missing,     ('a33edccd', 'Vivian.weapon - 伞柄收起A.LightMap.1024')),
            (multiply_section_if_missing,     ('a33edccd', 'Vivian.weapon - 伞面A.LightMap.1024')),
            (multiply_section_if_missing,     ('a33edccd', 'Vivian.weapon - sword剑A.LightMap.1024')),
            (multiply_section_if_missing,     ('a33edccd', 'Vivian.weapon - 喷射器A.LightMap.1024')),
        ],
        'a33edccd': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9277a2c1', 'Vivian.weapon - 伞柄展开A.LightMap.2048')),
            (multiply_section_if_missing,     ('9277a2c1', 'Vivian.weapon - 伞柄收起A.LightMap.2048')),
            (multiply_section_if_missing,     ('9277a2c1', 'Vivian.weapon - 伞面A.LightMap.2048')),
            (multiply_section_if_missing,     ('9277a2c1', 'Vivian.weapon - sword剑A.LightMap.2048')),
            (multiply_section_if_missing,     ('9277a2c1', 'Vivian.weapon - 喷射器A.LightMap.2048')),
        ],
        'dd8a1851': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab4cde14', 'Vivian.weapon - 伞柄展开A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ab4cde14', 'Vivian.weapon - 伞柄收起A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ab4cde14', 'Vivian.weapon - 伞面A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ab4cde14', 'Vivian.weapon - sword剑A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('ab4cde14', 'Vivian.weapon - 喷射器A.MaterialMap.1024')),
        ],
        'ab4cde14': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄展开A, weapon - 伞柄收起A, weapon - 伞面A, weapon - sword剑A and weapon - 喷射器A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1b843cb1', 'Vivian.weapon - 伞柄展开.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd8a1851', 'Vivian.weapon - 伞柄展开A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('dd8a1851', 'Vivian.weapon - 伞柄收起A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('dd8a1851', 'Vivian.weapon - 伞面A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('dd8a1851', 'Vivian.weapon - sword剑A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('dd8a1851', 'Vivian.weapon - 喷射器A.MaterialMap.2048')),
        ],

        # ==================== weapon - 伞柄收起 Component ====================
        '7232ac6f': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄收起 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '56ccb629': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄收起 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
        ],
        'd06d75e0': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄收起 Position VB Hash',)),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
        ],
        '2e01f6e0': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄收起 Texcoord VB Hash',)),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
        ],
        'b24f5c99': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞柄收起 Blend VB Hash',)),
            (add_section_if_missing,          ('7232ac6f', 'Vivian.weapon - 伞柄收起.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 伞面 Component ====================
        '28f8090e': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞面 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd175e722': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞面 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        'b586b07e': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞面 Position VB Hash',)),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        '2809e5db': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞面 Texcoord VB Hash',)),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        'd97d4c96': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 伞面 Blend VB Hash',)),
            (add_section_if_missing,          ('28f8090e', 'Vivian.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - sword剑 Component ====================
        'a031575e': [
            (log,                             ('2.2 - 3.2: Vivian weapon - sword剑 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8413730c': [
            (log,                             ('2.2 - 3.2: Vivian weapon - sword剑 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
        ],
        'cb21ccdf': [
            (log,                             ('2.2 - 3.2: Vivian weapon - sword剑 Position VB Hash',)),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
        ],
        'af180e46': [
            (log,                             ('2.2 - 3.2: Vivian weapon - sword剑 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
        ],
        '12f34479': [
            (log,                             ('2.2 - 3.2: Vivian weapon - sword剑 Blend VB Hash',)),
            (add_section_if_missing,          ('a031575e', 'Vivian.weapon - sword剑.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 喷射器 Component ====================
        'e69dfc8c': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 喷射器 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cc2d7ad1': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 喷射器 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
        ],
        '30e3560c': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 喷射器 Position VB Hash',)),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
        ],
        'c8ede4d4': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 喷射器 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
        ],
        '15002e84': [
            (log,                             ('2.2 - 3.2: Vivian weapon - 喷射器 Blend VB Hash',)),
            (add_section_if_missing,          ('e69dfc8c', 'Vivian.weapon - 喷射器.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Vivian',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
