"""
Yixuan Character Hash Commands
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
    Returns Yixuan's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ac8e9ee3': [
            (log,                             ('2.2 - 3.2: Yixuan Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '36a68b27': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'cc898b44': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Position VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'd4841137': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'd7eb400e': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
        ],
        '7e38b38b': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84fe943d', 'Yixuan.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('84fe943d', 'Yixuan.BottleA.Diffuse.1024')),
            (multiply_section_if_missing,     ('84fe943d', 'Yixuan.Copper coin stringA.Diffuse.1024')),
        ],
        '84fe943d': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7e38b38b', 'Yixuan.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('7e38b38b', 'Yixuan.BottleA.Diffuse.2048')),
            (multiply_section_if_missing,     ('7e38b38b', 'Yixuan.Copper coin stringA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BodyA, BottleA, Copper coin stringA, HairpinA, JacketA, weapon - 鸟(非战斗状态)A and weapon - 鸟(战斗状态)A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.BottleA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.Copper coin stringA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.JacketA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.weapon - 鸟(非战斗状态)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yixuan.weapon - 鸟(战斗状态)A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BodyA, BottleA, Copper coin stringA, HairpinA, JacketA, weapon - 鸟(非战斗状态)A and weapon - 鸟(战斗状态)A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.BottleA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.Copper coin stringA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.HairpinA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.JacketA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.weapon - 鸟(非战斗状态)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yixuan.weapon - 鸟(战斗状态)A.NormalMap.2048')),
        ],
        '086ac064': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5574ca9f', 'Yixuan.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('5574ca9f', 'Yixuan.BottleA.LightMap.1024')),
            (multiply_section_if_missing,     ('5574ca9f', 'Yixuan.Copper coin stringA.LightMap.1024')),
        ],
        '5574ca9f': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('086ac064', 'Yixuan.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('086ac064', 'Yixuan.BottleA.LightMap.2048')),
            (multiply_section_if_missing,     ('086ac064', 'Yixuan.Copper coin stringA.LightMap.2048')),
        ],
        '83b02982': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f4ac690c', 'Yixuan.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('f4ac690c', 'Yixuan.BottleA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('f4ac690c', 'Yixuan.Copper coin stringA.MaterialMap.1024')),
        ],
        'f4ac690c': [
            (log,                             ('2.2 - 3.2: Yixuan HairA, BottleA and Copper coin stringA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'Yixuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0fdae851', 'Yixuan.BottleGlass.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('83b02982', 'Yixuan.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('83b02982', 'Yixuan.BottleA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('83b02982', 'Yixuan.Copper coin stringA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'd28b9c82': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7f5aba6c': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'c7748cbd': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a07eb5cf': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '07c7e48f': [
            (log,                             ('2.2 - 3.2: Yixuan Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'Yixuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '029c1f5a': [
            (log,                             ('2.2 - 3.2: Yixuan Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f922d854': [
            (log,                             ('2.2 - 3.2: Yixuan Body Draw VB Hash',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        ],
        '155737d9': [
            (log,                             ('2.2 - 3.2: Yixuan Body Position VB Hash',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        ],
        '7af146a0': [
            (log,                             ('2.2 - 3.2: Yixuan Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        ],
        '3e629c05': [
            (log,                             ('2.2 - 3.2: Yixuan Body Blend VB Hash',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
        ],
        '2a4f37a6': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d7db2bc6', 'Yixuan.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d7db2bc6', 'Yixuan.HairpinA.Diffuse.1024')),
        ],
        'd7db2bc6': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2a4f37a6', 'Yixuan.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('2a4f37a6', 'Yixuan.HairpinA.Diffuse.2048')),
        ],
        '5a291e85': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96f754a7', 'Yixuan.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('96f754a7', 'Yixuan.HairpinA.LightMap.1024')),
        ],
        '96f754a7': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5a291e85', 'Yixuan.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('5a291e85', 'Yixuan.HairpinA.LightMap.2048')),
        ],
        'd28370ec': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa1056a5', 'Yixuan.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('aa1056a5', 'Yixuan.HairpinA.MaterialMap.1024')),
        ],
        'aa1056a5': [
            (log,                             ('2.2 - 3.2: Yixuan BodyA and HairpinA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('029c1f5a', 'Yixuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d28370ec', 'Yixuan.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d28370ec', 'Yixuan.HairpinA.MaterialMap.2048')),
        ],

        # ==================== Bottle Component ====================
        '1630f2d0': [
            (log,                             ('2.2 - 3.2: Yixuan Bottle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0219df6e': [
            (log,                             ('1.0 -> 2.5: Yixuan Bottle IB Hash',)),
            (update_hash,                     ('1630f2d0',)),
        ],
        '05466ddf': [
            (log,                             ('2.2 - 3.2: Yixuan Bottle Draw VB Hash',)),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        ],
        'd000beae': [
            (log,                             ('1.0 -> 2.5: Yixuan Bottle Draw Hash',)),
            (update_hash,                     ('05466ddf',)),
        ],
        '8555098d': [
            (log,                             ('2.2 - 3.2: Yixuan Bottle Position VB Hash',)),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        ],
        'd0ff2c18': [
            (log,                             ('1.0 -> 2.5: Yixuan Bottle Position Hash',)),
            (update_hash,                     ('8555098d',)),
        ],
        'ff4b112b': [
            (log,                             ('2.2 - 3.2: Yixuan Bottle Texcoord VB Hash',)),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        ],
        'f05da93a': [
            (log,                             ('1.0 -> 2.5: Yixuan Bottle Texcoord Hash',)),
            (update_hash,                     ('ff4b112b',)),
        ],
        'd89da8eb': [
            (log,                             ('2.2 - 3.2: Yixuan Bottle Blend VB Hash',)),
            (add_section_if_missing,          ('1630f2d0', 'Yixuan.Bottle.IB', 'match_priority = 0\n')),
        ],
        '55638d51': [
            (log,                             ('1.0 -> 2.5: Yixuan Bottle Blend Hash',)),
            (update_hash,                     ('d89da8eb',)),
        ],

        # ==================== Copper coin string Component ====================
        '67c61080': [
            (log,                             ('2.2 - 3.2: Yixuan Copper coin string IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ddaf88bc': [
            (log,                             ('2.2 - 3.2: Yixuan Copper coin string Draw VB Hash',)),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
        ],
        'eaf79039': [
            (log,                             ('2.2 - 3.2: Yixuan Copper coin string Position VB Hash',)),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
        ],
        '9714e6e6': [
            (log,                             ('2.2 - 3.2: Yixuan Copper coin string Texcoord VB Hash',)),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
        ],
        'ee9b9cfe': [
            (log,                             ('2.2 - 3.2: Yixuan Copper coin string Blend VB Hash',)),
            (add_section_if_missing,          ('67c61080', 'Yixuan.Copper coin string.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hairpin Component ====================
        '892858fd': [
            (log,                             ('2.2 - 3.2: Yixuan Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ba017cf3': [
            (log,                             ('2.2 - 3.2: Yixuan Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '3194141e': [
            (log,                             ('2.2 - 3.2: Yixuan Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'b3123168': [
            (log,                             ('2.2 - 3.2: Yixuan Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'de9d3ab7': [
            (log,                             ('2.2 - 3.2: Yixuan Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'Yixuan.Hairpin.IB', 'match_priority = 0\n')),
        ],

        # ==================== Jacket Component ====================
        '8c2fc05e': [
            (log,                             ('2.2 - 3.2: Yixuan Jacket IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '73599fbb': [
            (log,                             ('2.2 - 3.2: Yixuan Jacket Draw VB Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        ],
        '9b67bc72': [
            (log,                             ('2.2 - 3.2: Yixuan Jacket Position VB Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        ],
        '9f95d565': [
            (log,                             ('2.2 - 3.2: Yixuan Jacket Texcoord VB Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        ],
        '0ff3af5a': [
            (log,                             ('2.2 - 3.2: Yixuan Jacket Blend VB Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
        ],
        'e6dca725': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fcedcc3', 'Yixuan.JacketA.Diffuse.1024')),
        ],
        '1fcedcc3': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e6dca725', 'Yixuan.JacketA.Diffuse.2048')),
        ],
        '59b2daf9': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c4d167c3', 'Yixuan.JacketA.LightMap.1024')),
        ],
        'c4d167c3': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('59b2daf9', 'Yixuan.JacketA.LightMap.2048')),
        ],
        'bb581f1e': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fd56fa4b', 'Yixuan.JacketA.MaterialMap.1024')),
        ],
        'fd56fa4b': [
            (log,                             ('2.2 - 3.2: Yixuan JacketA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('8c2fc05e', 'Yixuan.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb581f1e', 'Yixuan.JacketA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '8b067f99': [
            (log,                             ('2.2 - 3.2: Yixuan Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '972e4b6d': [
            (log,                             ('2.2 - 3.2: Yixuan Face Position VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
        ],
        '2e04aac2': [
            (log,                             ('2.2 - 3.1: Yixuan Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('02426764',)),
        ],
        '02426764': [
            (log,                             ('3.2: Yixuan Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '4466e7ea': [
            (log,                             ('2.2 - 3.2: Yixuan Face Blend VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
        ],
        'ad3cd82a': [
            (log,                             ('2.2 - 3.1: Yixuan Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
        ],
        '7d9ee001': [
            (log,                             ('2.2 - 3.2: Yixuan FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9efd1605', 'Yixuan.FaceA.Diffuse.1024')),
        ],
        '9efd1605': [
            (log,                             ('2.2 - 3.2: Yixuan FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8b067f99', 'Yixuan.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d9ee001', 'Yixuan.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 鸟(非战斗状态) Component ====================
        'ce38ac3b': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ccbbb7ea': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态) VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '9052084b': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态) Position VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        'f45313a0': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态) Texcoord VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '3ac6dfc7': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态) Blend VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '920caf66': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('677893d2', 'Yixuan.weapon - 鸟(非战斗状态)A.Diffuse.1024')),
        ],
        '677893d2': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('920caf66', 'Yixuan.weapon - 鸟(非战斗状态)A.Diffuse.2048')),
        ],
        '771d52eb': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1ee41dc', 'Yixuan.weapon - 鸟(非战斗状态)A.LightMap.1024')),
        ],
        'd1ee41dc': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('771d52eb', 'Yixuan.weapon - 鸟(非战斗状态)A.LightMap.2048')),
        ],
        'dc3c5667': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23d4f666', 'Yixuan.weapon - 鸟(非战斗状态)A.MaterialMap.1024')),
        ],
        '23d4f666': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(非战斗状态)A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'Yixuan.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc3c5667', 'Yixuan.weapon - 鸟(非战斗状态)A.MaterialMap.2048')),
        ],

        # ==================== weapon - 鸟(战斗状态) Component ====================
        'fd2cbc71': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5a016c9b': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态) VertexLimit VB Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '1a201296': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态) Position VB Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '1a0934e4': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态) Texcoord VB Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '2ad5c986': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态) Blend VB Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '7f504f10': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9263dc92', 'Yixuan.weapon - 鸟(战斗状态)A.Diffuse.1024')),
        ],
        '9263dc92': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f504f10', 'Yixuan.weapon - 鸟(战斗状态)A.Diffuse.2048')),
        ],
        '96254967': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fc9ae2ff', 'Yixuan.weapon - 鸟(战斗状态)A.LightMap.1024')),
        ],
        'fc9ae2ff': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96254967', 'Yixuan.weapon - 鸟(战斗状态)A.LightMap.2048')),
        ],
        '4300c703': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e60bc3d', 'Yixuan.weapon - 鸟(战斗状态)A.MaterialMap.1024')),
        ],
        '5e60bc3d': [
            (log,                             ('2.2 - 3.2: Yixuan weapon - 鸟(战斗状态)A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fd2cbc71', 'Yixuan.weapon - 鸟(战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4300c703', 'Yixuan.weapon - 鸟(战斗状态)A.MaterialMap.2048')),
        ],

        # ==================== BottleGlass Component (legacy, not in DB 2.2 - 3.1) ====================
        '0fdae851': [
            (log,                             ('2.5: Yixuan BottleGlass IB Hash',)),
            (add_ib_check_if_missing,),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yixuan',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
