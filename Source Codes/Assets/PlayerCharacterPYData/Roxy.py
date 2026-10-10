"""
Roxy Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Roxy's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '4e6e989e': [
            (log,                             ('3.2: Roxy Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0ca0d1db': [
            (log,                             ('3.2: Roxy Hair Draw VB Hash',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
        ],
        '8d17b17d': [
            (log,                             ('3.2: Roxy Hair Position VB Hash',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
        ],
        '77598722': [
            (log,                             ('3.2: Roxy Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
        ],
        '831dc545': [
            (log,                             ('3.2: Roxy Hair Blend VB Hash',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
        ],
        'ba531329': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c4ef3f52', 'Roxy.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c4ef3f52', 'Roxy.HeadwearA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c4ef3f52', 'Roxy.GlassesA.Diffuse.1024')),
        ],
        'c4ef3f52': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ba531329', 'Roxy.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ba531329', 'Roxy.HeadwearA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ba531329', 'Roxy.GlassesA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.2: Roxy HairA, HeadwearA, GlassesA, BodyA, AccessoriesA, weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.HeadwearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.GlassesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.AccessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.weapon - 拉手A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.weapon - 匣子A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.weapon - 十字架A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.weapon - 枪杆A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Roxy.weapon - 钉子A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.2: Roxy HairA, HeadwearA, GlassesA, BodyA, AccessoriesA, weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.HeadwearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.GlassesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.AccessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.weapon - 拉手A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.weapon - 匣子A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.weapon - 十字架A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.weapon - 枪杆A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Roxy.weapon - 钉子A.NormalMap.2048')),
        ],
        '7885a317': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('311b79f8', 'Roxy.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('311b79f8', 'Roxy.HeadwearA.LightMap.1024')),
            (multiply_section_if_missing,     ('311b79f8', 'Roxy.GlassesA.LightMap.1024')),
        ],
        '311b79f8': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7885a317', 'Roxy.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('7885a317', 'Roxy.HeadwearA.LightMap.2048')),
            (multiply_section_if_missing,     ('7885a317', 'Roxy.GlassesA.LightMap.2048')),
        ],
        '4a701d9e': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('613d838a', 'Roxy.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('613d838a', 'Roxy.HeadwearA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('613d838a', 'Roxy.GlassesA.MaterialMap.1024')),
        ],
        '613d838a': [
            (log,                             ('3.2: Roxy HairA, HeadwearA and GlassesA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4e6e989e', 'Roxy.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4a701d9e', 'Roxy.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4a701d9e', 'Roxy.HeadwearA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4a701d9e', 'Roxy.GlassesA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '89fc5b32': [
            (log,                             ('3.2: Roxy HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Headwear Component ====================
        '4e6d8882': [
            (log,                             ('3.2: Roxy Headwear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '387f13af': [
            (log,                             ('3.2: Roxy Headwear Draw VB Hash',)),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
        ],
        'a43fefad': [
            (log,                             ('3.2: Roxy Headwear Position VB Hash',)),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
        ],
        '6f72141b': [
            (log,                             ('3.2: Roxy Headwear Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
        ],
        '1b4a25c8': [
            (log,                             ('3.2: Roxy Headwear Blend VB Hash',)),
            (add_section_if_missing,          ('4e6d8882', 'Roxy.Headwear.IB', 'match_priority = 0\n')),
        ],

        # ==================== Glasses Component ====================
        '3f797188': [
            (log,                             ('3.2: Roxy Glasses IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0183a3a6': [
            (log,                             ('3.2: Roxy Glasses Draw VB Hash',)),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
        ],
        '2b1539ff': [
            (log,                             ('3.2: Roxy Glasses Position VB Hash',)),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
        ],
        '3089925d': [
            (log,                             ('3.2: Roxy Glasses Texcoord VB Hash',)),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
        ],
        '7707cc68': [
            (log,                             ('3.2: Roxy Glasses Blend VB Hash',)),
            (add_section_if_missing,          ('3f797188', 'Roxy.Glasses.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'd5e1e7ff': [
            (log,                             ('3.2: Roxy Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'de6784e3': [
            (log,                             ('3.2: Roxy Body Draw VB Hash',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
        ],
        '9249ae8b': [
            (log,                             ('3.2: Roxy Body Position VB Hash',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
        ],
        'a268a2db': [
            (log,                             ('3.2: Roxy Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
        ],
        '7eb9cbc7': [
            (log,                             ('3.2: Roxy Body Blend VB Hash',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
        ],
        'da5be24c': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7bf9af64', 'Roxy.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('7bf9af64', 'Roxy.AccessoriesA.Diffuse.1024')),
        ],
        '7bf9af64': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('da5be24c', 'Roxy.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('da5be24c', 'Roxy.AccessoriesA.Diffuse.2048')),
        ],
        'e3703d1f': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb36eee9', 'Roxy.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('bb36eee9', 'Roxy.AccessoriesA.LightMap.1024')),
        ],
        'bb36eee9': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e3703d1f', 'Roxy.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('e3703d1f', 'Roxy.AccessoriesA.LightMap.2048')),
        ],
        '44ed4f24': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eda0dc75', 'Roxy.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('eda0dc75', 'Roxy.AccessoriesA.MaterialMap.1024')),
        ],
        'eda0dc75': [
            (log,                             ('3.2: Roxy BodyA and AccessoriesA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d5e1e7ff', 'Roxy.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('44ed4f24', 'Roxy.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('44ed4f24', 'Roxy.AccessoriesA.MaterialMap.2048')),
        ],

        # ==================== Accessories Component ====================
        '09c39441': [
            (log,                             ('3.2: Roxy Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4805f693': [
            (log,                             ('3.2: Roxy Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
        ],
        'ca82e547': [
            (log,                             ('3.2: Roxy Accessories Position VB Hash',)),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
        ],
        'bb5f669c': [
            (log,                             ('3.2: Roxy Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
        ],
        '7b88aa46': [
            (log,                             ('3.2: Roxy Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('09c39441', 'Roxy.Accessories.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '224a50cf': [
            (log,                             ('3.2: Roxy Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6e02f849': [
            (log,                             ('3.2: Roxy Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '54106b0e': [
            (log,                             ('3.2: Roxy Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '9fdf77b3': [
            (log,                             ('3.2: Roxy Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '09fa4349': [
            (log,                             ('3.2: Roxy Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '126d4a26': [
            (log,                             ('3.2: Roxy EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f3fd4ad', 'Roxy.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9f3fd4ad', 'Roxy.FaceA.Diffuse.1024')),
        ],
        '9f3fd4ad': [
            (log,                             ('3.2: Roxy EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('224a50cf', 'Roxy.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('126d4a26', 'Roxy.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('126d4a26', 'Roxy.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'e40b00b2': [
            (log,                             ('3.2: Roxy Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9770e8ef': [
            (log,                             ('3.2: Roxy Face Draw VB Hash',)),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
        ],
        'ad627ba8': [
            (log,                             ('3.2: Roxy Face Position VB Hash',)),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
        ],
        'c90eb75c': [
            (log,                             ('3.2: Roxy Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
        ],
        'c0b23b8b': [
            (log,                             ('3.2: Roxy Face Blend VB Hash',)),
            (add_section_if_missing,          ('e40b00b2', 'Roxy.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 拉手 Component ====================
        '2cc6a188': [
            (log,                             ('3.2: Roxy weapon - 拉手 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f3664d5f': [
            (log,                             ('3.2: Roxy weapon - 拉手 Draw VB Hash',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
        ],
        '9cad9afb': [
            (log,                             ('3.2: Roxy weapon - 拉手 Position VB Hash',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
        ],
        'c13b8459': [
            (log,                             ('3.2: Roxy weapon - 拉手 Texcoord VB Hash',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
        ],
        'a47afc40': [
            (log,                             ('3.2: Roxy weapon - 拉手 Blend VB Hash',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
        ],
        '805216e1': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bcd2c443', 'Roxy.weapon - 拉手A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bcd2c443', 'Roxy.weapon - 匣子A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bcd2c443', 'Roxy.weapon - 十字架A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bcd2c443', 'Roxy.weapon - 枪杆A.Diffuse.1024')),
            (multiply_section_if_missing,     ('bcd2c443', 'Roxy.weapon - 钉子A.Diffuse.1024')),
        ],
        'bcd2c443': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('805216e1', 'Roxy.weapon - 拉手A.Diffuse.2048')),
            (multiply_section_if_missing,     ('805216e1', 'Roxy.weapon - 匣子A.Diffuse.2048')),
            (multiply_section_if_missing,     ('805216e1', 'Roxy.weapon - 十字架A.Diffuse.2048')),
            (multiply_section_if_missing,     ('805216e1', 'Roxy.weapon - 枪杆A.Diffuse.2048')),
            (multiply_section_if_missing,     ('805216e1', 'Roxy.weapon - 钉子A.Diffuse.2048')),
        ],
        '7715da05': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('386872a5', 'Roxy.weapon - 拉手A.LightMap.1024')),
            (multiply_section_if_missing,     ('386872a5', 'Roxy.weapon - 匣子A.LightMap.1024')),
            (multiply_section_if_missing,     ('386872a5', 'Roxy.weapon - 十字架A.LightMap.1024')),
            (multiply_section_if_missing,     ('386872a5', 'Roxy.weapon - 枪杆A.LightMap.1024')),
            (multiply_section_if_missing,     ('386872a5', 'Roxy.weapon - 钉子A.LightMap.1024')),
        ],
        '386872a5': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7715da05', 'Roxy.weapon - 拉手A.LightMap.2048')),
            (multiply_section_if_missing,     ('7715da05', 'Roxy.weapon - 匣子A.LightMap.2048')),
            (multiply_section_if_missing,     ('7715da05', 'Roxy.weapon - 十字架A.LightMap.2048')),
            (multiply_section_if_missing,     ('7715da05', 'Roxy.weapon - 枪杆A.LightMap.2048')),
            (multiply_section_if_missing,     ('7715da05', 'Roxy.weapon - 钉子A.LightMap.2048')),
        ],
        'b88ed702': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57006300', 'Roxy.weapon - 拉手A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('57006300', 'Roxy.weapon - 匣子A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('57006300', 'Roxy.weapon - 十字架A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('57006300', 'Roxy.weapon - 枪杆A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('57006300', 'Roxy.weapon - 钉子A.MaterialMap.1024')),
        ],
        '57006300': [
            (log,                             ('3.2: Roxy weapon - 拉手A, weapon - 匣子A, weapon - 十字架A, weapon - 枪杆A and weapon - 钉子A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2cc6a188', 'Roxy.weapon - 拉手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b88ed702', 'Roxy.weapon - 拉手A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b88ed702', 'Roxy.weapon - 匣子A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b88ed702', 'Roxy.weapon - 十字架A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b88ed702', 'Roxy.weapon - 枪杆A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b88ed702', 'Roxy.weapon - 钉子A.MaterialMap.2048')),
        ],

        # ==================== weapon - 匣子 Component ====================
        '4ce97f81': [
            (log,                             ('3.2: Roxy weapon - 匣子 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6df8e318': [
            (log,                             ('3.2: Roxy weapon - 匣子 Draw VB Hash',)),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
        ],
        'aa80ba26': [
            (log,                             ('3.2: Roxy weapon - 匣子 Position VB Hash',)),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
        ],
        '82783b16': [
            (log,                             ('3.2: Roxy weapon - 匣子 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
        ],
        '476a3837': [
            (log,                             ('3.2: Roxy weapon - 匣子 Blend VB Hash',)),
            (add_section_if_missing,          ('4ce97f81', 'Roxy.weapon - 匣子.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 十字架 Component ====================
        'd0d437a1': [
            (log,                             ('3.2: Roxy weapon - 十字架 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c28724d': [
            (log,                             ('3.2: Roxy weapon - 十字架 Draw VB Hash',)),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
        ],
        '75387bcf': [
            (log,                             ('3.2: Roxy weapon - 十字架 Position VB Hash',)),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
        ],
        '5224917e': [
            (log,                             ('3.2: Roxy weapon - 十字架 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
        ],
        '60f9efde': [
            (log,                             ('3.2: Roxy weapon - 十字架 Blend VB Hash',)),
            (add_section_if_missing,          ('d0d437a1', 'Roxy.weapon - 十字架.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 枪杆 Component ====================
        'd92f1cdf': [
            (log,                             ('3.2: Roxy weapon - 枪杆 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '13087664': [
            (log,                             ('3.2: Roxy weapon - 枪杆 Draw VB Hash',)),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
        ],
        '4ed9c1cf': [
            (log,                             ('3.2: Roxy weapon - 枪杆 Position VB Hash',)),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
        ],
        '8914b14e': [
            (log,                             ('3.2: Roxy weapon - 枪杆 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
        ],
        'accfb45c': [
            (log,                             ('3.2: Roxy weapon - 枪杆 Blend VB Hash',)),
            (add_section_if_missing,          ('d92f1cdf', 'Roxy.weapon - 枪杆.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 钉子 Component ====================
        'd127180e': [
            (log,                             ('3.2: Roxy weapon - 钉子 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '80023ae0': [
            (log,                             ('3.2: Roxy weapon - 钉子 Draw VB Hash',)),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
        ],
        'ebca5b03': [
            (log,                             ('3.2: Roxy weapon - 钉子 Position VB Hash',)),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
        ],
        '75726e6c': [
            (log,                             ('3.2: Roxy weapon - 钉子 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
        ],
        '0ef4568b': [
            (log,                             ('3.2: Roxy weapon - 钉子 Blend VB Hash',)),
            (add_section_if_missing,          ('d127180e', 'Roxy.weapon - 钉子.IB', 'match_priority = 0\n')),
        ],

        # ==================== 3.2 -> 3.21 hotfix (old hashes) ====================
        # The 3.2 -> 3.21 hotfix renumbered Roxy's hair and face buffers. The
        # meshes changed too (object_indexes [0, 7350, 9216] -> [0, 6996, 9216]
        # for the face), but the buffer FORMAT is unchanged -- unlike 3.1 -> 3.2
        # this is not a 36 -> 48 repack, so no zzz_13_remap_texcoord here. These
        # are plain update_hash chains, same pattern as JaneDoe '9268a5af' ->
        # '3275b812'; the new-generation blocks above do the actual work.
        '2533ab1c': [
            (log,                             ('3.2 -> 3.21: Roxy Hair IB Hash',)),
            (update_hash,                     ('4e6e989e',)),
        ],
        '1fdb833a': [
            (log,                             ('3.2 -> 3.21: Roxy Hair Position VB Hash',)),
            (update_hash,                     ('8d17b17d',)),
        ],
        'b44f7eda': [
            (log,                             ('3.2 -> 3.21: Roxy Hair Texcoord VB Hash',)),
            (update_hash,                     ('77598722',)),
        ],
        '520d6267': [
            (log,                             ('3.2 -> 3.21: Roxy Hair Blend VB Hash',)),
            (update_hash,                     ('831dc545',)),
        ],
        '75b3aa9c': [
            (log,                             ('3.2 -> 3.21: Roxy Face IB Hash',)),
            (update_hash,                     ('e40b00b2',)),
        ],
        'e8bed423': [
            (log,                             ('3.2 -> 3.21: Roxy Face Texcoord VB Hash',)),
            (update_hash,                     ('c90eb75c',)),
        ],
        '551c5f22': [
            (log,                             ('3.2 -> 3.21: Roxy Face Blend VB Hash',)),
            (update_hash,                     ('c0b23b8b',)),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Roxy',
    'game_versions': ['3.2'],
}
