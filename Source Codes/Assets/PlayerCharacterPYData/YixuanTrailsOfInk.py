"""
YixuanTrailsOfInk Character Hash Commands
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
    Returns YixuanTrailsOfInk's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ac8e9ee3': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '36a68b27': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        ],
        'cc898b44': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Position VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        ],
        'd4841137': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        ],
        'd7eb400e': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        ],
        '7e38b38b': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7e38b38b', 'YixuanTrailsOfInk.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('7e38b38b', '84fe943d'), 'YixuanTrailsOfInk.HairA.Diffuse.1024')),
        ],
        '84fe943d': [
            (log,                             ('3.1 -> 2.2: YixuanTrailsOfInk HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('7e38b38b',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairA, BodyA, BodyB, BottleA, BottleB, HairpinA and weapon - 鸟(非战斗状态)A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'YixuanTrailsOfInk.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '798adba3'), 'YixuanTrailsOfInk.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.BottleA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.BottleB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1 -> 2.2: YixuanTrailsOfInk HairA, BodyA, BodyB, BottleA, BottleB, HairpinA and weapon - 鸟(非战斗状态)A NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '086ac064': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('086ac064', 'YixuanTrailsOfInk.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('086ac064', '5574ca9f'), 'YixuanTrailsOfInk.HairA.LightMap.1024')),
        ],
        '5574ca9f': [
            (log,                             ('3.1 -> 2.2: YixuanTrailsOfInk HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('086ac064',)),
        ],
        '83b02982': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('83b02982', 'YixuanTrailsOfInk.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('83b02982', 'f4ac690c'), 'YixuanTrailsOfInk.HairA.MaterialMap.1024')),
        ],
        'f4ac690c': [
            (log,                             ('3.1 -> 2.2: YixuanTrailsOfInk HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('83b02982',)),
        ],

        # ==================== Hair Shadow Component ====================
        'd28b9c82': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7f5aba6c': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'c7748cbd': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a07eb5cf': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '07c7e48f': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '95de0d39': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4e321bef': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Body Draw VB Hash',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        ],
        'd1e95221': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Body Position VB Hash',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        ],
        '6c57cdb1': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        ],
        'b5c70816': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Body Blend VB Hash',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        ],
        'fe2cc6f3': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5460dbe4', 'YixuanTrailsOfInk.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('5460dbe4', 'YixuanTrailsOfInk.BottleA.Diffuse.1024')),
        ],
        '7683c132': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('89509335', 'YixuanTrailsOfInk.BodyB.Diffuse.1024')),
            (multiply_section_if_missing,     ('89509335', 'YixuanTrailsOfInk.BottleB.Diffuse.1024')),
        ],
        '487db3e0': [
            (log,                             ('2.0 -> 2.1: YixuanTrailsOfInk BodyB Diffuse 2048p Hash',)),
            (update_hash,                     ('7683c132',)),
        ],
        '5460dbe4': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fe2cc6f3', 'YixuanTrailsOfInk.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('fe2cc6f3', 'YixuanTrailsOfInk.BottleA.Diffuse.2048')),
        ],
        '89509335': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7683c132', 'YixuanTrailsOfInk.BodyB.Diffuse.2048')),
            (multiply_section_if_missing,     ('7683c132', 'YixuanTrailsOfInk.BottleB.Diffuse.2048')),
        ],
        'c13cac2c': [
            (log,                             ('2.0 -> 2.1: YixuanTrailsOfInk BodyB Diffuse 1024p Hash',)),
            (update_hash,                     ('89509335',)),
        ],
        '867e3b95': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7369431b', 'YixuanTrailsOfInk.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('7369431b', 'YixuanTrailsOfInk.BottleA.LightMap.1024')),
        ],
        'a22695c9': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed7abe1d', 'YixuanTrailsOfInk.BodyB.LightMap.1024')),
            (multiply_section_if_missing,     ('ed7abe1d', 'YixuanTrailsOfInk.BottleB.LightMap.1024')),
        ],
        '7369431b': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('867e3b95', 'YixuanTrailsOfInk.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('867e3b95', 'YixuanTrailsOfInk.BottleA.LightMap.2048')),
        ],
        'ed7abe1d': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a22695c9', 'YixuanTrailsOfInk.BodyB.LightMap.2048')),
            (multiply_section_if_missing,     ('a22695c9', 'YixuanTrailsOfInk.BottleB.LightMap.2048')),
        ],
        'c72a2356': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2d535255', 'YixuanTrailsOfInk.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2d535255', 'YixuanTrailsOfInk.BottleA.MaterialMap.1024')),
        ],
        '7e6747ac': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('229c5b0f', 'YixuanTrailsOfInk.BodyB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('229c5b0f', 'YixuanTrailsOfInk.BottleB.MaterialMap.1024')),
        ],
        '16a1fb10': [
            (log,                             ('2.0 -> 2.1: YixuanTrailsOfInk BodyB MaterialMap 2048p Hash',)),
            (update_hash,                     ('7e6747ac',)),
        ],
        '2d535255': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyA and BottleA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c72a2356', 'YixuanTrailsOfInk.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c72a2356', 'YixuanTrailsOfInk.BottleA.MaterialMap.2048')),
        ],
        '229c5b0f': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk BodyB and BottleB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7e6747ac', 'YixuanTrailsOfInk.BodyB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('7e6747ac', 'YixuanTrailsOfInk.BottleB.MaterialMap.2048')),
        ],
        '9a79cf64': [
            (log,                             ('2.0 -> 2.1: YixuanTrailsOfInk BodyB MaterialMap 1024p Hash',)),
            (update_hash,                     ('229c5b0f',)),
        ],

        # ==================== Bottle Component ====================
        '064cd7d3': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Bottle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e0a315c0': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Bottle Draw VB Hash',)),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        ],
        'f6564b67': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Bottle Position VB Hash',)),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        ],
        'ee08ae2a': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Bottle Texcoord VB Hash',)),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        ],
        '4df43644': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Bottle Blend VB Hash',)),
            (add_section_if_missing,          ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hairpin Component ====================
        '892858fd': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ba017cf3': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '3194141e': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'b3123168': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'de9d3ab7': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '2a4f37a6': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d7db2bc6', 'YixuanTrailsOfInk.HairpinA.Diffuse.1024')),
        ],
        'd7db2bc6': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2a4f37a6', 'YixuanTrailsOfInk.HairpinA.Diffuse.2048')),
        ],
        '5a291e85': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96f754a7', 'YixuanTrailsOfInk.HairpinA.LightMap.1024')),
        ],
        '96f754a7': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5a291e85', 'YixuanTrailsOfInk.HairpinA.LightMap.2048')),
        ],
        'd28370ec': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa1056a5', 'YixuanTrailsOfInk.HairpinA.MaterialMap.1024')),
        ],
        'aa1056a5': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk HairpinA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d28370ec', 'YixuanTrailsOfInk.HairpinA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '8b067f99': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '972e4b6d': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Face Position VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
        ],
        '2e04aac2': [
            (log,                             ('2.2 - 3.1: YixuanTrailsOfInk Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('02426764',)),
        ],
        '02426764': [
            (log,                             ('3.2: YixuanTrailsOfInk Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '4466e7ea': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk Face Blend VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
        ],
        'ad3cd82a': [
            (log,                             ('2.2 - 3.1: YixuanTrailsOfInk Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
        ],
        '7d9ee001': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9efd1605', 'YixuanTrailsOfInk.FaceA.Diffuse.1024')),
        ],
        '9efd1605': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d9ee001', 'YixuanTrailsOfInk.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 鸟(非战斗状态) Component ====================
        'ce38ac3b': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ccbbb7ea': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态) VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '9052084b': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态) Position VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        'f45313a0': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态) Texcoord VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '3ac6dfc7': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态) Blend VB Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '920caf66': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('677893d2', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.Diffuse.1024')),
        ],
        '677893d2': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('920caf66', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.Diffuse.2048')),
        ],
        '771d52eb': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1ee41dc', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.LightMap.1024')),
        ],
        'd1ee41dc': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('771d52eb', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.LightMap.2048')),
        ],
        'dc3c5667': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23d4f666', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.MaterialMap.1024')),
        ],
        '23d4f666': [
            (log,                             ('2.2 - 3.2: YixuanTrailsOfInk weapon - 鸟(非战斗状态)A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ce38ac3b', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc3c5667', 'YixuanTrailsOfInk.weapon - 鸟(非战斗状态)A.MaterialMap.2048')),
        ],

        # ==================== Ink Component (legacy, not in DB 2.2 - 3.1) ====================
        '0fdae851': [
            (log,                             ('2.5: YixuanTrailsOfInk Ink IB Hash',)),
            (add_ib_check_if_missing,),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YixuanTrailsOfInk',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
