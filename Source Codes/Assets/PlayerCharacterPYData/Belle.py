"""
Belle Character Hash Commands
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
    Returns Belle's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'bea4a483': [
            (log,                             ('1.0 -> 3.0: Belle Hair IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('3acf9aea',)),
        ],
        '3acf9aea': [
            (log,                             ('3.0 - 3.2: Belle Hair and Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '142ddbbc': [
            (log,                             ('2.2 - 2.8: Belle Hair Draw VB Hash',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        ],
        'a9673001': [
            (log,                             ('2.2 - 2.8: Belle Hair Position VB Hash',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        ],
        '11e38ebb': [
            (log,                             ('2.2 - 2.8: Belle Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        ],
        'cc32660c': [
            (log,                             ('2.2 - 2.8: Belle Hair Blend VB Hash',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
        ],
        '84a9dfca': [
            (log,                             ('3.0 - 3.2: Belle Hair and Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
        ],
        'a678dff4': [
            (log,                             ('3.0 - 3.2: Belle Hair and Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '77932137': [
            (log,                             ('3.0 - 3.2: Belle Hair and Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '6e583c52': [
            (log,                             ('3.0 - 3.2: Belle Hair and Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '1ce58567': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08f04d95', 'Belle.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'Belle.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'Belle.EarPendantA.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'Belle.BodyB.Diffuse.1024')),
            (multiply_section_if_missing,     ('08f04d95', 'Belle.LegA.Diffuse.1024')),
        ],
        '08f04d95': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ce58567', 'Belle.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'Belle.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'Belle.EarPendantA.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'Belle.BodyB.Diffuse.2048')),
            (multiply_section_if_missing,     ('1ce58567', 'Belle.LegA.Diffuse.2048')),
        ],
        'f1ee2105': [
            (log,                             ('1.7 -> 2.0: Belle HairA LightMap 2048p Hash',)),
            (update_hash,                     ('7d562f53',)),
        ],
        '7d562f53': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f44f330b', '2e656f2f'), 'Belle.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('f44f330b', '2e656f2f'), 'Belle.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     (('f44f330b', '2e656f2f'), 'Belle.EarPendantA.LightMap.1024')),
            (multiply_section_if_missing,     (('f44f330b', '2e656f2f'), 'Belle.BodyB.LightMap.1024')),
            (multiply_section_if_missing,     (('f44f330b', '2e656f2f'), 'Belle.LegA.LightMap.1024')),
        ],
        '2e656f2f': [
            (log,                             ('1.7 -> 2.0: Belle HairA LightMap 1024p Hash',)),
            (update_hash,                     ('f44f330b',)),
        ],
        'f44f330b': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7d562f53', 'f1ee2105'), 'Belle.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('7d562f53', 'f1ee2105'), 'Belle.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     (('7d562f53', 'f1ee2105'), 'Belle.EarPendantA.LightMap.2048')),
            (multiply_section_if_missing,     (('7d562f53', 'f1ee2105'), 'Belle.BodyB.LightMap.2048')),
            (multiply_section_if_missing,     (('7d562f53', 'f1ee2105'), 'Belle.LegA.LightMap.2048')),
        ],
        '24c47ca5': [
            (log,                             ('1.4 -> 1.5: Belle HairA MaterialMap 2048p Hash',)),
            (update_hash,                     ('34bdb036',)),
        ],
        '34bdb036': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7542ef4b', '4b6ef993'), 'Belle.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('7542ef4b', '4b6ef993'), 'Belle.HairpinA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('7542ef4b', '4b6ef993'), 'Belle.EarPendantA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('7542ef4b', '4b6ef993'), 'Belle.BodyB.MaterialMap.1024')),
            (multiply_section_if_missing,     (('7542ef4b', '4b6ef993'), 'Belle.LegA.MaterialMap.1024')),
        ],
        '4b6ef993': [
            (log,                             ('1.4 -> 1.5: Belle HairA MaterialMap 1024p Hash',)),
            (update_hash,                     ('7542ef4b',)),
        ],
        '7542ef4b': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyB and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('34bdb036', '24c47ca5'), 'Belle.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('34bdb036', '24c47ca5'), 'Belle.HairpinA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('34bdb036', '24c47ca5'), 'Belle.EarPendantA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('34bdb036', '24c47ca5'), 'Belle.BodyB.MaterialMap.2048')),
            (multiply_section_if_missing,     (('34bdb036', '24c47ca5'), 'Belle.LegA.MaterialMap.2048')),
        ],
        '89b147ff': [
            (log,                             ('1.0 -> 2.0: Belle HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'f04f7ab9': [
            (log,                             ('1.0 -> 2.0: Belle BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyA, BodyB and LegA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.EarPendantA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6b55c039', 'c0bd8516'), 'Belle.LegA.NormalMap.1024')),
        ],
        '6b55c039': [
            (log,                             ('1.0 -> 2.0: Belle HairA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        'c0bd8516': [
            (log,                             ('1.0 -> 2.0: Belle BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Belle HairA, HairpinA, EarPendantA, BodyA, BodyB and LegA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bea4a483', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3acf9aea', 'Belle.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.HairpinA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.EarPendantA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '89b147ff', 'f04f7ab9'), 'Belle.LegA.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '403eace9': [
            (log,                             ('2.2 - 3.2: Belle Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Hairpin Component ====================
        # Hairpin shares all hashes with Hair; see the Hair Component above.

        # ==================== EarPendant Component ====================
        '07920753': [
            (log,                             ('3.0 - 3.2: Belle EarPendant IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c4e3b1e8': [
            (log,                             ('3.0 - 3.2: Belle EarPendant Draw VB Hash',)),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
        ],
        '66a4bab6': [
            (log,                             ('3.0 - 3.2: Belle EarPendant Position VB Hash',)),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
        ],
        'a2ee3518': [
            (log,                             ('3.0 - 3.2: Belle EarPendant Texcoord VB Hash',)),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
        ],
        '28720ee7': [
            (log,                             ('3.0 - 3.2: Belle EarPendant Blend VB Hash',)),
            (add_section_if_missing,          ('07920753', 'Belle.EarPendant.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '1817f3ca': [
            (log,                             ('1.0 -> 3.0: Belle Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('c2b4ce3a',)),
        ],
        'c2b4ce3a': [
            (log,                             ('3.0 - 3.2: Belle Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ac1c8f80': [
            (log,                             ('2.2 - 2.8: Belle Body Draw VB Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        'd2844c01': [
            (log,                             ('2.2 - 2.8: Belle Body Position VB Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        'caf95576': [
            (log,                             ('1.0 -> 1.1: Belle Body Texcoord Hash',)),
            (update_hash,                     ('801edbf4',)),
            (log,                             ('1.0 -> 1.1: Belle Body Blend Remap',)),
            (update_buffer_blend_indices,     (
                'd2844c01',
                (3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 126, 127),
                (6, 7, 3, 5, 4, 18, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 25, 24, 20, 22, 23, 38, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 47, 48, 53, 56, 45, 46, 49, 50, 51, 52, 54, 55, 60, 61, 66, 58, 59, 62, 63, 64, 65, 104, 95, 96, 97, 98, 99, 100, 101, 102, 103, 127, 126),
            )),
        ],
        '801edbf4': [
            (log,                             ('2.2 - 2.8: Belle Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        'd7ca821f': [
            (log,                             ('1.0 -> 1.1: Belle Body Blend Hash',)),
            (update_hash,                     ('c92a17d8',)),
        ],
        'c92a17d8': [
            (log,                             ('2.2 - 2.8: Belle Body Blend VB Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        'bea2b94e': [
            (log,                             ('3.0 - 3.2: Belle Body Draw VB Hash',)),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        '5838ad30': [
            (log,                             ('3.0 - 3.2: Belle Body Position VB Hash',)),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        '40a897ab': [
            (log,                             ('3.0 - 3.2: Belle Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        '3ee01622': [
            (log,                             ('3.0 - 3.2: Belle Body Blend VB Hash',)),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
        ],
        'd2960560': [
            (log,                             ('1.4 -> 1.5: Belle BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('24639b77',)),
        ],
        '24639b77': [
            (log,                             ('2.2 - 3.2: Belle BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b9c7f71b', '4454fb58'), 'Belle.BodyA.Diffuse.1024')),
        ],
        '4454fb58': [
            (log,                             ('1.4 -> 1.5: Belle BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('b9c7f71b',)),
        ],
        'b9c7f71b': [
            (log,                             ('2.2 - 3.2: Belle BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('24639b77', 'd2960560'), 'Belle.BodyA.Diffuse.2048')),
        ],
        'bf286c84': [
            (log,                             ('1.4 -> 1.5: Belle BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('7947679c',)),
        ],
        '7947679c': [
            (log,                             ('2.2 - 3.2: Belle BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a4d3687d', '2ed82c57'), 'Belle.BodyA.LightMap.1024')),
        ],
        '2ed82c57': [
            (log,                             ('1.4 -> 1.5: Belle BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('a4d3687d',)),
        ],
        'a4d3687d': [
            (log,                             ('2.2 - 3.2: Belle BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7947679c', 'bf286c84'), 'Belle.BodyA.LightMap.2048')),
        ],
        '33f28c6d': [
            (log,                             ('2.2 - 3.2: Belle BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b1abe877', 'Belle.BodyA.MaterialMap.1024')),
        ],
        'b1abe877': [
            (log,                             ('2.2 - 3.2: Belle BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('1817f3ca', 'Belle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c2b4ce3a', 'Belle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33f28c6d', 'Belle.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        'e6afd8d1': [
            (log,                             ('3.0 - 3.2: Belle Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7217e342': [
            (log,                             ('3.0 - 3.2: Belle Leg Draw VB Hash',)),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        ],
        'ca81bde5': [
            (log,                             ('3.0 - 3.2: Belle Leg Position VB Hash',)),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        ],
        'e317bb99': [
            (log,                             ('3.0 - 3.2: Belle Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        ],
        'b4cd8580': [
            (log,                             ('3.0 - 3.2: Belle Leg Blend VB Hash',)),
            (add_section_if_missing,          ('e6afd8d1', 'Belle.Leg.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '9a9780a7': [
            (log,                             ('2.2 - 3.2: Belle Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '04abceb5': [
            (log,                             ('2.2 - 3.2: Belle Face Draw VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
        ],
        '3eb95df2': [
            (log,                             ('2.2 - 3.2: Belle Face Position VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
        ],
        '1de8fc08': [
            (log,                             ('2.2 -> 3.0: Belle Face Texcoord VB Hash',)),
            (update_hash,                     ('d3000b22',)),
        ],
        'd3000b22': [
            (log,                             ('3.0 -> 3.1: Belle Face Texcoord VB Hash',)),
            (update_hash,                     ('228f5a8b',)),
        ],
        '228f5a8b': [
            (log,                             ('3.1: Belle Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
        ],
        '36138f65': [
            (log,                             ('2.2 -> 3.0: Belle Face Blend VB Hash',)),
            (update_hash,                     ('6ade3fdc',)),
        ],
        '6ade3fdc': [
            (log,                             ('3.0 - 3.2: Belle Face Blend VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
        ],
        '75ec3614': [
            (log,                             ('2.2 - 3.2: Belle FaceA and FaceB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77eef7e8', 'Belle.FaceA.Diffuse.1024')),
            (multiply_section_if_missing,     ('77eef7e8', 'Belle.FaceB.Diffuse.1024')),
        ],
        '77eef7e8': [
            (log,                             ('2.2 - 3.2: Belle FaceA and FaceB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9a9780a7', 'Belle.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('75ec3614', 'Belle.FaceA.Diffuse.2048')),
            (multiply_section_if_missing,     ('75ec3614', 'Belle.FaceB.Diffuse.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Belle',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
