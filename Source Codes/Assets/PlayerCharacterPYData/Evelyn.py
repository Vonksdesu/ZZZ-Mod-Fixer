"""
Evelyn Character Hash Commands
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
    Returns Evelyn's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '10a5bde2': [
            (log,                             ('2.2 - 3.2: Evelyn Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '798bc78b': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Draw VB Hash',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        ],
        'c2fe4e27': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Position VB Hash',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        ],
        '066f6115': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        ],
        'b43809d2': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Blend VB Hash',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        ],
        '0e5c3c97': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.Hairpin - ribbonsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.JacketA.Diffuse.1024')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.weapon - 匕首展开状态.Diffuse.1024')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.weapon - 匕首收起状态.Diffuse.1024')),
            (multiply_section_if_missing,     ('65a7592d', 'Evelyn.silk string.Diffuse.1024')),
        ],
        '65a7592d': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.Hairpin - ribbonsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.JacketA.Diffuse.2048')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.weapon - 匕首展开状态.Diffuse.2048')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.weapon - 匕首收起状态.Diffuse.2048')),
            (multiply_section_if_missing,     ('0e5c3c97', 'Evelyn.silk string.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, ShoulderA, BodyA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.Hairpin - ribbonsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.JacketA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.ShoulderA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.weapon - 匕首展开状态.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.weapon - 匕首收起状态.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Evelyn.silk string.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, ShoulderA, BodyA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.Hairpin - ribbonsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.JacketA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.ShoulderA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.weapon - 匕首展开状态.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.weapon - 匕首收起状态.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Evelyn.silk string.NormalMap.2048')),
        ],
        'e1434e0d': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.Hairpin - ribbonsA.LightMap.1024')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.JacketA.LightMap.1024')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.weapon - 匕首展开状态.LightMap.1024')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.weapon - 匕首收起状态.LightMap.1024')),
            (multiply_section_if_missing,     ('eb414a98', 'Evelyn.silk string.LightMap.1024')),
        ],
        'eb414a98': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.Hairpin - ribbonsA.LightMap.2048')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.JacketA.LightMap.2048')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.weapon - 匕首展开状态.LightMap.2048')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.weapon - 匕首收起状态.LightMap.2048')),
            (multiply_section_if_missing,     ('e1434e0d', 'Evelyn.silk string.LightMap.2048')),
        ],
        'b2718585': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.Hairpin - ribbonsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.JacketA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.weapon - 匕首展开状态.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.weapon - 匕首收起状态.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e680f0c7', 'Evelyn.silk string.MaterialMap.1024')),
        ],
        'e680f0c7': [
            (log,                             ('2.2 - 3.2: Evelyn HairA, Hairpin - ribbonsA, JacketA, weapon - 匕首展开状态, weapon - 匕首收起状态 and silk string MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.Hairpin - ribbonsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.JacketA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.weapon - 匕首展开状态.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.weapon - 匕首收起状态.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b2718585', 'Evelyn.silk string.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '8ed17e5a': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '28913abf': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '1251bc38': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bf111b37': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '94ce70dd': [
            (log,                             ('2.2 - 3.2: Evelyn Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hairpin - ribbons Component ====================
        '2488810a': [
            (log,                             ('2.2 - 3.2: Evelyn Hairpin - ribbons IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '98a87a48': [
            (log,                             ('2.2 - 3.2: Evelyn Hairpin - ribbons Draw VB Hash',)),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
        ],
        'f1076f2a': [
            (log,                             ('2.2 - 3.2: Evelyn Hairpin - ribbons Position VB Hash',)),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
        ],
        '63d18ae4': [
            (log,                             ('2.2 - 3.2: Evelyn Hairpin - ribbons Texcoord VB Hash',)),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
        ],
        '35070aca': [
            (log,                             ('2.2 - 3.2: Evelyn Hairpin - ribbons Blend VB Hash',)),
            (add_section_if_missing,          ('2488810a', 'Evelyn.Hairpin - ribbons.IB', 'match_priority = 0\n')),
        ],
        # Hairpin - ribbons shares all texture hashes with Hair; see that Component above.

        # ==================== Jacket Component ====================
        'bb6d1023': [
            (log,                             ('2.2 - 3.2: Evelyn Jacket IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1fb9dfe2': [
            (log,                             ('2.2 - 3.2: Evelyn Jacket Draw VB Hash',)),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        ],
        '4edb27d5': [
            (log,                             ('2.2 - 3.2: Evelyn Jacket Position VB Hash',)),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        ],
        '8b3ed55f': [
            (log,                             ('2.2 - 3.2: Evelyn Jacket Texcoord VB Hash',)),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        ],
        '022d390f': [
            (log,                             ('2.2 - 3.2: Evelyn Jacket Blend VB Hash',)),
            (add_section_if_missing,          ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        ],
        # Jacket shares all texture hashes with Hair; see that Component above.

        # ==================== Shoulder Component ====================
        'b3eaedb0': [
            (log,                             ('2.2 - 3.2: Evelyn Shoulder IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '356f6430': [
            (log,                             ('2.2 - 3.2: Evelyn Shoulder Draw VB Hash',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
        ],
        '2b77b077': [
            (log,                             ('2.2 - 3.2: Evelyn Shoulder Position VB Hash',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
        ],
        '3cecd299': [
            (log,                             ('2.2 - 3.2: Evelyn Shoulder Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
        ],
        'a6b42907': [
            (log,                             ('2.2 - 3.2: Evelyn Shoulder Blend VB Hash',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
        ],
        'a59b14c0': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93033898', 'Evelyn.ShoulderA.Diffuse.1024')),
            (multiply_section_if_missing,     ('93033898', 'Evelyn.BodyA.Diffuse.1024')),
        ],
        '93033898': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a59b14c0', 'Evelyn.ShoulderA.Diffuse.2048')),
            (multiply_section_if_missing,     ('a59b14c0', 'Evelyn.BodyA.Diffuse.2048')),
        ],
        'd022d32c': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('16aab2ab', 'Evelyn.ShoulderA.LightMap.1024')),
            (multiply_section_if_missing,     ('16aab2ab', 'Evelyn.BodyA.LightMap.1024')),
        ],
        '16aab2ab': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d022d32c', 'Evelyn.ShoulderA.LightMap.2048')),
            (multiply_section_if_missing,     ('d022d32c', 'Evelyn.BodyA.LightMap.2048')),
        ],
        '8624e4e4': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('716561f0', 'Evelyn.ShoulderA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('716561f0', 'Evelyn.BodyA.MaterialMap.1024')),
        ],
        '716561f0': [
            (log,                             ('2.2 - 3.2: Evelyn ShoulderA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8624e4e4', 'Evelyn.ShoulderA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('8624e4e4', 'Evelyn.BodyA.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        '04b53ecd': [
            (log,                             ('2.2 - 3.2: Evelyn Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '02b04234': [
            (log,                             ('2.2 - 3.2: Evelyn Body Draw VB Hash',)),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        ],
        '67eafa06': [
            (log,                             ('2.2 - 3.2: Evelyn Body Position VB Hash',)),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        ],
        '26f9ba95': [
            (log,                             ('2.2 - 3.2: Evelyn Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        ],
        '5ea06832': [
            (log,                             ('2.2 - 3.2: Evelyn Body Blend VB Hash',)),
            (add_section_if_missing,          ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        ],
        # Body shares its Diffuse, LightMap and MaterialMap hashes with Shoulder (see that
        # Component above) and its NormalMap with Hair (see Hair Component above).

        # ==================== Face Component ====================
        'ddf4efa6': [
            (log,                             ('2.2 - 3.2: Evelyn Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c6afc18c': [
            (log,                             ('2.2 - 3.2: Evelyn Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        ],
        'fcbd52cb': [
            (log,                             ('2.2 - 3.2: Evelyn Face Position VB Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        ],
        'aa2f560e': [
            (log,                             ('2.2 - 3.1: Evelyn Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b3136c51',)),
        ],
        'b3136c51': [
            (log,                             ('3.2: Evelyn Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'f9fc3c8b': [
            (log,                             ('2.2 - 3.2: Evelyn Face Blend VB Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        ],
        '8e1d1a6f': [
            (log,                             ('2.2 - 3.2: Evelyn FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc090438', 'Evelyn.FaceA.Diffuse.1024')),
        ],
        'bc090438': [
            (log,                             ('2.2 - 3.2: Evelyn FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8e1d1a6f', 'Evelyn.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 匕首展开状态 Component ====================
        '78699e6c': [
            (log,                             ('2.2 - 3.2: Evelyn weapon - 匕首展开状态 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3ae20915': [
            (log,                             ('2.2 - 3.0: Evelyn weapon - 匕首展开状态 and weapon - 匕首收起状态 VertexLimit VB Hash (shared)',)),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
        ],
        '3e2abfae': [
            (log,                             ('2.2: Evelyn weapon - 匕首展开状态 Position VB Hash',)),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
        ],
        '691f1157': [
            (log,                             ('2.2: Evelyn weapon - 匕首展开状态 Texcoord VB Hash',)),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
        ],
        '99c7c611': [
            (log,                             ('2.2 - 3.0: Evelyn weapon - 匕首展开状态 and weapon - 匕首收起状态 Blend VB Hash (shared)',)),
            (add_section_if_missing,          ('78699e6c', 'Evelyn.weapon - 匕首展开状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
        ],
        # weapon - 匕首展开状态 shares all texture hashes with Hair; see that Component above.

        # ==================== Weapon - 匕首收起状态 Component ====================
        '7fb7467f': [
            (log,                             ('2.2 - 3.2: Evelyn weapon - 匕首收起状态 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '33d2866e': [
            (log,                             ('2.2 - 2.7: Evelyn weapon - 匕首收起状态 Position VB Hash',)),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
        ],
        '040993a0': [
            (log,                             ('2.2 - 2.7: Evelyn weapon - 匕首收起状态 Texcoord VB Hash',)),
            (add_section_if_missing,          ('7fb7467f', 'Evelyn.weapon - 匕首收起状态.IB', 'match_priority = 0\n')),
        ],
        # weapon - 匕首收起状态 shares all hashes with weapon - 匕首展开状态 (VertexLimit, Blend)
        # and with Hair (textures); see those Components above.

        # ==================== Silk String Component ====================
        'af10bd11': [
            (log,                             ('2.2 - 3.2: Evelyn silk string IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4ff726df': [
            (log,                             ('2.2 - 3.1: Evelyn silk string VertexLimit VB Hash',)),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
        ],
        '06c6a436': [
            (log,                             ('2.2 - 2.3: Evelyn silk string Position VB Hash',)),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
        ],
        '2c5dcebd': [
            (log,                             ('2.2 - 2.3: Evelyn silk string Texcoord VB Hash',)),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
        ],
        '99555cf2': [
            (log,                             ('2.2 - 2.3: Evelyn silk string Blend VB Hash',)),
            (add_section_if_missing,          ('af10bd11', 'Evelyn.silk string.IB', 'match_priority = 0\n')),
        ],
        # silk string shares all texture hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Evelyn',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
