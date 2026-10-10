"""
Yanagi Character Hash Commands
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
    Returns Yanagi's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '9e12899f': [
            (log,                             ('2.2 - 3.2: Yanagi Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'daba2b23': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Draw VB Hash',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        ],
        '0e52a354': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Position VB Hash',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        ],
        '42ca0c9b': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        ],
        '0bbe1d7d': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Blend VB Hash',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        ],
        'ac5f6d76': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4edb5c79', 'Yanagi.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('4edb5c79', 'Yanagi.Hair accessoriesA.Diffuse.1024')),
        ],
        '4edb5c79': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac5f6d76', 'Yanagi.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ac5f6d76', 'Yanagi.Hair accessoriesA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Yanagi HairA, Hair accessoriesA, BodyA, weapon - 刀鞘A and weapon - 长刀A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Yanagi.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yanagi.Hair accessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yanagi.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yanagi.weapon - 刀鞘A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yanagi.weapon - 长刀A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Yanagi HairA, Hair accessoriesA, BodyA, weapon - 刀鞘A and weapon - 长刀A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Yanagi.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yanagi.Hair accessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yanagi.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yanagi.weapon - 刀鞘A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yanagi.weapon - 长刀A.NormalMap.2048')),
        ],
        '99cfa935': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5a43d985', 'Yanagi.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('5a43d985', 'Yanagi.Hair accessoriesA.LightMap.1024')),
        ],
        '5a43d985': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('99cfa935', 'Yanagi.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('99cfa935', 'Yanagi.Hair accessoriesA.LightMap.2048')),
        ],
        'f80b57f0': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('486e3c42', 'Yanagi.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('486e3c42', 'Yanagi.Hair accessoriesA.MaterialMap.1024')),
        ],
        '486e3c42': [
            (log,                             ('2.2 - 3.2: Yanagi HairA and Hair accessoriesA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f80b57f0', 'Yanagi.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f80b57f0', 'Yanagi.Hair accessoriesA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'c1628e55': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'de0bb6f9': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9c8be112': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bb35cc80': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'eb448ade': [
            (log,                             ('2.2 - 3.2: Yanagi Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair accessories Component ====================
        '13c75775': [
            (log,                             ('2.2 - 3.2: Yanagi Hair accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '01864eed': [
            (log,                             ('2.2 - 3.2: Yanagi Hair accessories Draw VB Hash',)),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
        ],
        'fe235fbb': [
            (log,                             ('2.2 - 3.2: Yanagi Hair accessories Position VB Hash',)),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
        ],
        '49188dc8': [
            (log,                             ('2.2 - 3.2: Yanagi Hair accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
        ],
        '07a1d434': [
            (log,                             ('2.2 - 3.2: Yanagi Hair accessories Blend VB Hash',)),
            (add_section_if_missing,          ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'f478ee4c': [
            (log,                             ('2.2 - 3.2: Yanagi Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2fe26340': [
            (log,                             ('2.2 - 3.2: Yanagi Body Draw VB Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        ],
        '7ff000de': [
            (log,                             ('2.2 - 3.2: Yanagi Body Position VB Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        ],
        'f4fbc5c0': [
            (log,                             ('2.2 - 3.2: Yanagi Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        ],
        'fd363c76': [
            (log,                             ('2.3 -> 2.4: Yanagi Body Blend Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b558d482',)),
        ],
        'b558d482': [
            (log,                             ('2.4 - 3.2: Yanagi Body Blend VB Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        ],
        'c7c4f5c5': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c119dbd7', 'Yanagi.BodyA.Diffuse.1024')),
        ],
        'c119dbd7': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7c4f5c5', 'Yanagi.BodyA.Diffuse.2048')),
        ],
        '616200aa': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('3ffcef9e', 'f60602ec'), 'Yanagi.BodyA.LightMap.1024')),
        ],
        '08933e28': [
            (log,                             ('1.7 -> 2.0: Yanagi BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('616200aa',)),
        ],
        '3ffcef9e': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('616200aa', '08933e28'), 'Yanagi.BodyA.LightMap.2048')),
        ],
        'f60602ec': [
            (log,                             ('2.5: Yanagi BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        ],
        'c2ae5d2b': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b29f0188', 'Yanagi.BodyA.MaterialMap.1024')),
        ],
        'b29f0188': [
            (log,                             ('2.2 - 3.2: Yanagi BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c2ae5d2b', 'Yanagi.BodyA.MaterialMap.2048')),
        ],

        # ==================== lens Component ====================
        '44d9123b': [
            (log,                             ('2.2 - 3.2: Yanagi lens IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2e92fc77': [
            (log,                             ('2.5: Yanagi Glasses ib (old hash)',)),
            (update_hash,                     ('44d9123b',)),
        ],
        '178a1ff8': [
            (log,                             ('2.2 - 3.2: Yanagi lens Draw VB Hash',)),
            (add_section_if_missing,          ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
        ],
        '8e3cf210': [
            (log,                             ('2.2 - 3.2: Yanagi lens Position VB Hash',)),
            (add_section_if_missing,          ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
        ],
        'dd32963a': [
            (log,                             ('2.2 - 3.2: Yanagi lens Texcoord VB Hash',)),
            (add_section_if_missing,          ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
        ],
        '6b5d6e39': [
            (log,                             ('2.2 - 3.2: Yanagi lens Blend VB Hash',)),
            (add_section_if_missing,          ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '0817204c': [
            (log,                             ('2.2 - 3.2: Yanagi Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '47323770': [
            (log,                             ('2.2 - 3.2: Yanagi Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        ],
        '7d20a437': [
            (log,                             ('2.2 - 3.2: Yanagi Face Position VB Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        ],
        '69c75b70': [
            (log,                             ('2.2 - 3.1: Yanagi Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('68efc509',)),
        ],
        '68efc509': [
            (log,                             ('3.2: Yanagi Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '4cb3e0ea': [
            (log,                             ('2.2 - 3.2: Yanagi Face Blend VB Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        ],
        '95d9e92e': [
            (log,                             ('2.2 - 3.2: Yanagi FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cfe7ab46', 'Yanagi.FaceA.Diffuse.1024')),
        ],
        'cfe7ab46': [
            (log,                             ('2.2 - 3.2: Yanagi FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95d9e92e', 'Yanagi.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 刀鞘 Component ====================
        '27d49f0b': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9e8cddbf': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        'a07928b5': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘 Position VB Hash',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        'c6d97eb4': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘 Texcoord VB Hash',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        '74491025': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘 Blend VB Hash',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        'b2aca818': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ab64737', 'Yanagi.weapon - 刀鞘A.Diffuse.1024')),
            (multiply_section_if_missing,     ('9ab64737', 'Yanagi.weapon - 长刀A.Diffuse.1024')),
        ],
        '9ab64737': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b2aca818', 'Yanagi.weapon - 刀鞘A.Diffuse.2048')),
            (multiply_section_if_missing,     ('b2aca818', 'Yanagi.weapon - 长刀A.Diffuse.2048')),
        ],
        'e4891108': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d9ac4e1e', 'Yanagi.weapon - 刀鞘A.LightMap.1024')),
            (multiply_section_if_missing,     ('d9ac4e1e', 'Yanagi.weapon - 长刀A.LightMap.1024')),
        ],
        'd9ac4e1e': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e4891108', 'Yanagi.weapon - 刀鞘A.LightMap.2048')),
            (multiply_section_if_missing,     ('e4891108', 'Yanagi.weapon - 长刀A.LightMap.2048')),
        ],
        '240ee9dc': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d18079e5', 'Yanagi.weapon - 刀鞘A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d18079e5', 'Yanagi.weapon - 长刀A.MaterialMap.1024')),
        ],
        'd18079e5': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 刀鞘A and weapon - 长刀A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('27d49f0b', 'Yanagi.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('240ee9dc', 'Yanagi.weapon - 刀鞘A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('240ee9dc', 'Yanagi.weapon - 长刀A.MaterialMap.2048')),
        ],

        # ==================== weapon - 长刀 Component ====================
        '2d7f2223': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 长刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b680db32': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 长刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        '03634f2c': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 长刀 Position VB Hash',)),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        '61f72721': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 长刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
        '14b8daf0': [
            (log,                             ('2.2 - 3.2: Yanagi weapon - 长刀 Blend VB Hash',)),
            (add_section_if_missing,          ('2d7f2223', 'Yanagi.weapon - 长刀.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yanagi',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
