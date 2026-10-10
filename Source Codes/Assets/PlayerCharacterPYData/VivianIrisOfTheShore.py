"""
VivianIrisOfTheShore Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.3 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns VivianIrisOfTheShore's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '4108c0da': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '713a8587': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Draw VB Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        ],
        'bec9acb0': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Position VB Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        ],
        '128d277f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        ],
        '5b569848': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Blend VB Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
        ],
        '15dcce65': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('427be7bd', 'VivianIrisOfTheShore.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('427be7bd', 'VivianIrisOfTheShore.BodyB.Diffuse.1024')),
            (multiply_section_if_missing,     ('427be7bd', 'VivianIrisOfTheShore.GemA.Diffuse.1024')),
        ],
        '427be7bd': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('15dcce65', 'VivianIrisOfTheShore.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('15dcce65', 'VivianIrisOfTheShore.BodyB.Diffuse.2048')),
            (multiply_section_if_missing,     ('15dcce65', 'VivianIrisOfTheShore.GemA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, HairB, BodyA, BodyB, GemA, weapon - 伞柄A and weapon - 伞面A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.HairB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.GemA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.weapon - 伞柄A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'VivianIrisOfTheShore.weapon - 伞面A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, HairB, BodyA, BodyB, GemA, weapon - 伞柄A and weapon - 伞面A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.HairB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.GemA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.weapon - 伞柄A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'VivianIrisOfTheShore.weapon - 伞面A.NormalMap.2048')),
        ],
        '8a82d289': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45b67c0b', 'VivianIrisOfTheShore.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('45b67c0b', 'VivianIrisOfTheShore.BodyB.LightMap.1024')),
            (multiply_section_if_missing,     ('45b67c0b', 'VivianIrisOfTheShore.GemA.LightMap.1024')),
        ],
        '45b67c0b': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a82d289', 'VivianIrisOfTheShore.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('8a82d289', 'VivianIrisOfTheShore.BodyB.LightMap.2048')),
            (multiply_section_if_missing,     ('8a82d289', 'VivianIrisOfTheShore.GemA.LightMap.2048')),
        ],
        'c23ddbea': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdb06288', 'VivianIrisOfTheShore.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cdb06288', 'VivianIrisOfTheShore.BodyB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cdb06288', 'VivianIrisOfTheShore.GemA.MaterialMap.1024')),
        ],
        'cdb06288': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairA, BodyB and GemA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c23ddbea', 'VivianIrisOfTheShore.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c23ddbea', 'VivianIrisOfTheShore.BodyB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c23ddbea', 'VivianIrisOfTheShore.GemA.MaterialMap.2048')),
        ],
        'a84d933f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2df6f7b5', 'VivianIrisOfTheShore.HairB.Diffuse.1024')),
        ],
        '2df6f7b5': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a84d933f', 'VivianIrisOfTheShore.HairB.Diffuse.2048')),
        ],
        '8e3a20ea': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('36b80366', 'VivianIrisOfTheShore.HairB.LightMap.1024')),
        ],
        '36b80366': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8e3a20ea', 'VivianIrisOfTheShore.HairB.LightMap.2048')),
        ],
        '2af66072': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2d5b1412', 'VivianIrisOfTheShore.HairB.MaterialMap.1024')),
        ],
        '2d5b1412': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore HairB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4108c0da', 'VivianIrisOfTheShore.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2af66072', 'VivianIrisOfTheShore.HairB.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'b79903af': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9898740f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bbb7d4b1': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'fa9735df': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '1853b047': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('b79903af', 'VivianIrisOfTheShore.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '3060793b': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd96480bc': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Body Draw VB Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        ],
        '5e46216b': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Body Position VB Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        ],
        'fb44f88a': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        ],
        'f32eec8a': [
            (log,                             ('2.3 -> 2.4: VivianIrisOfTheShore Body Blend Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('723bccec',)),
        ],
        '723bccec': [
            (log,                             ('2.4 - 3.2: VivianIrisOfTheShore Body Blend VB Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
        ],
        '136b3e29': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ea05046', 'VivianIrisOfTheShore.BodyA.Diffuse.1024')),
        ],
        '1ea05046': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('136b3e29', 'VivianIrisOfTheShore.BodyA.Diffuse.2048')),
        ],
        '69a6a15f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8bb6a0f', 'VivianIrisOfTheShore.BodyA.LightMap.1024')),
        ],
        'e8bb6a0f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('69a6a15f', 'VivianIrisOfTheShore.BodyA.LightMap.2048')),
        ],
        '527c3676': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('909ea74d', 'VivianIrisOfTheShore.BodyA.MaterialMap.1024')),
        ],
        '909ea74d': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3060793b', 'VivianIrisOfTheShore.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('527c3676', 'VivianIrisOfTheShore.BodyA.MaterialMap.2048')),
        ],

        # ==================== Gem Component ====================
        'ec7b047c': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Gem IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9829025f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Gem Draw VB Hash',)),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        ],
        '3c88ea03': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Gem Position VB Hash',)),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        ],
        'a55d2f46': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Gem Texcoord VB Hash',)),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        ],
        '53a21868': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Gem Blend VB Hash',)),
            (add_section_if_missing,          ('ec7b047c', 'VivianIrisOfTheShore.Gem.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '39944f20': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fcf74fc0': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
        ],
        'c6e5dc87': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Face Position VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
        ],
        '0afe5a44': [
            (log,                             ('2.3 - 3.1: VivianIrisOfTheShore Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('50c5d703',)),
        ],
        '50c5d703': [
            (log,                             ('3.2: VivianIrisOfTheShore Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ef07b6f6': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore Face Blend VB Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
        ],
        '7b262ab6': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('66b5da8e', 'VivianIrisOfTheShore.FaceA.Diffuse.1024')),
        ],
        '66b5da8e': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('39944f20', 'VivianIrisOfTheShore.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7b262ab6', 'VivianIrisOfTheShore.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 伞柄 Component ====================
        '4adf1f7a': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bd5b581e': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
        ],
        '117996c2': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄 Position VB Hash',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
        ],
        'fa34947b': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
        ],
        'ee28f6c2': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄 Blend VB Hash',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
        ],
        '1dbeec1f': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('756ebf6b', 'VivianIrisOfTheShore.weapon - 伞柄A.Diffuse.1024')),
            (multiply_section_if_missing,     ('756ebf6b', 'VivianIrisOfTheShore.weapon - 伞面A.Diffuse.1024')),
        ],
        '756ebf6b': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1dbeec1f', 'VivianIrisOfTheShore.weapon - 伞柄A.Diffuse.2048')),
            (multiply_section_if_missing,     ('1dbeec1f', 'VivianIrisOfTheShore.weapon - 伞面A.Diffuse.2048')),
        ],
        '7270dab3': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d96fe324', 'VivianIrisOfTheShore.weapon - 伞柄A.LightMap.1024')),
            (multiply_section_if_missing,     ('d96fe324', 'VivianIrisOfTheShore.weapon - 伞面A.LightMap.1024')),
        ],
        'd96fe324': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7270dab3', 'VivianIrisOfTheShore.weapon - 伞柄A.LightMap.2048')),
            (multiply_section_if_missing,     ('7270dab3', 'VivianIrisOfTheShore.weapon - 伞面A.LightMap.2048')),
        ],
        '6ecc2389': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6af50aef', 'VivianIrisOfTheShore.weapon - 伞柄A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('6af50aef', 'VivianIrisOfTheShore.weapon - 伞面A.MaterialMap.1024')),
        ],
        '6af50aef': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞柄A and weapon - 伞面A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4adf1f7a', 'VivianIrisOfTheShore.weapon - 伞柄.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ecc2389', 'VivianIrisOfTheShore.weapon - 伞柄A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('6ecc2389', 'VivianIrisOfTheShore.weapon - 伞面A.MaterialMap.2048')),
        ],

        # ==================== weapon - 伞面 Component ====================
        '15c97ffc': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞面 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7f5aba6c': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞面 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        'd4bb64cc': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞面 Position VB Hash',)),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        'bd66871a': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞面 Texcoord VB Hash',)),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
        '431b0b24': [
            (log,                             ('2.3 - 3.2: VivianIrisOfTheShore weapon - 伞面 Blend VB Hash',)),
            (add_section_if_missing,          ('15c97ffc', 'VivianIrisOfTheShore.weapon - 伞面.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'VivianIrisOfTheShore',
    'game_versions': ['2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
