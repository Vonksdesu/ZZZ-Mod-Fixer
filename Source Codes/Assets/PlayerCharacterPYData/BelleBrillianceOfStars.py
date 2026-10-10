"""
BelleBrillianceOfStars Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns BelleBrillianceOfStars's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'aa9ffb85': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '992d149f': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hair Draw VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        ],
        'dbd537bb': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hair Position VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        ],
        '0f1d7b96': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        ],
        '2cf18f34': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hair Blend VB Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
        ],
        '1ce58567': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08f04d95', 'BelleBrillianceOfStars.HairA.Diffuse.1024')),
        ],
        '08f04d95': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ce58567', 'BelleBrillianceOfStars.HairA.Diffuse.2048')),
        ],
        '7d562f53': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f44f330b', 'BelleBrillianceOfStars.HairA.LightMap.1024')),
        ],
        'f44f330b': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d562f53', 'BelleBrillianceOfStars.HairA.LightMap.2048')),
        ],
        '34bdb036': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7542ef4b', 'BelleBrillianceOfStars.HairA.MaterialMap.1024')),
        ],
        '7542ef4b': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34bdb036', 'BelleBrillianceOfStars.HairA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA, HatA, EarringsA, TieA, PlayerA, BodyA and NeckA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.HatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.EarringsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.TieA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.PlayerA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'BelleBrillianceOfStars.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('d9a12c0a', 'BelleBrillianceOfStars.NeckA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairA, HatA, EarringsA, TieA, PlayerA and BodyA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa9ffb85', 'BelleBrillianceOfStars.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.HatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.EarringsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.TieA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.PlayerA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.BodyA.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '403eace9': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Hat Component ====================
        '0a843a8f': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0a877d89': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hat Draw VB Hash',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        ],
        '74d2da11': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hat Position VB Hash',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        ],
        '801cd45d': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hat Texcoord VB Hash',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        ],
        'd5070379': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Hat Blend VB Hash',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
        ],
        '8c0ea559': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('269a82f9', 'BelleBrillianceOfStars.HatA.Diffuse.1024')),
            (multiply_section_if_missing,     ('269a82f9', 'BelleBrillianceOfStars.EarringsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('269a82f9', 'BelleBrillianceOfStars.TieA.Diffuse.1024')),
            (multiply_section_if_missing,     ('269a82f9', 'BelleBrillianceOfStars.PlayerA.Diffuse.1024')),
        ],
        '269a82f9': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8c0ea559', 'BelleBrillianceOfStars.HatA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8c0ea559', 'BelleBrillianceOfStars.EarringsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8c0ea559', 'BelleBrillianceOfStars.TieA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8c0ea559', 'BelleBrillianceOfStars.PlayerA.Diffuse.2048')),
        ],
        'dcb8ba2e': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a21dde78', 'BelleBrillianceOfStars.HatA.LightMap.1024')),
            (multiply_section_if_missing,     ('a21dde78', 'BelleBrillianceOfStars.EarringsA.LightMap.1024')),
            (multiply_section_if_missing,     ('a21dde78', 'BelleBrillianceOfStars.TieA.LightMap.1024')),
            (multiply_section_if_missing,     ('a21dde78', 'BelleBrillianceOfStars.PlayerA.LightMap.1024')),
        ],
        'a21dde78': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dcb8ba2e', 'BelleBrillianceOfStars.HatA.LightMap.2048')),
            (multiply_section_if_missing,     ('dcb8ba2e', 'BelleBrillianceOfStars.EarringsA.LightMap.2048')),
            (multiply_section_if_missing,     ('dcb8ba2e', 'BelleBrillianceOfStars.TieA.LightMap.2048')),
            (multiply_section_if_missing,     ('dcb8ba2e', 'BelleBrillianceOfStars.PlayerA.LightMap.2048')),
        ],
        '57130f7c': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('08453671', 'BelleBrillianceOfStars.HatA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('08453671', 'BelleBrillianceOfStars.EarringsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('08453671', 'BelleBrillianceOfStars.TieA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('08453671', 'BelleBrillianceOfStars.PlayerA.MaterialMap.1024')),
        ],
        '08453671': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars HatA, EarringsA, TieA and PlayerA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('0a843a8f', 'BelleBrillianceOfStars.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57130f7c', 'BelleBrillianceOfStars.HatA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('57130f7c', 'BelleBrillianceOfStars.EarringsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('57130f7c', 'BelleBrillianceOfStars.TieA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('57130f7c', 'BelleBrillianceOfStars.PlayerA.MaterialMap.2048')),
        ],

        # ==================== Earrings Component ====================
        '62711f82': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Earrings IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e2c8decf': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Earrings Draw VB Hash',)),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
        ],
        '29324995': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Earrings Position VB Hash',)),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
        ],
        '8da231b5': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Earrings Texcoord VB Hash',)),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
        ],
        '611f1c52': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Earrings Blend VB Hash',)),
            (add_section_if_missing,          ('62711f82', 'BelleBrillianceOfStars.Earrings.IB', 'match_priority = 0\n')),
        ],
        # Earrings shares all texture hashes with Hat (Diffuse, LightMap, MaterialMap)
        # and NormalMap with the shared set; see the Hat and Hair Components above.

        # ==================== Tie Component ====================
        'b946c37f': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Tie IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c0ee97be': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Tie Draw VB Hash',)),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        ],
        '6aa2848f': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Tie Position VB Hash',)),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        ],
        '88e81d00': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Tie Texcoord VB Hash',)),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        ],
        'f83e837a': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Tie Blend VB Hash',)),
            (add_section_if_missing,          ('b946c37f', 'BelleBrillianceOfStars.Tie.IB', 'match_priority = 0\n')),
        ],
        # Tie shares all texture hashes with Hat (Diffuse, LightMap, MaterialMap)
        # and NormalMap with the shared set; see the Hat and Hair Components above.

        # ==================== Player Component ====================
        'a318b3c6': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Player IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f6ed0e7b': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Player Draw VB Hash',)),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
        ],
        'd9087948': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Player Position VB Hash',)),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
        ],
        '1cfe1205': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Player Texcoord VB Hash',)),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
        ],
        '82c81803': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Player Blend VB Hash',)),
            (add_section_if_missing,          ('a318b3c6', 'BelleBrillianceOfStars.Player.IB', 'match_priority = 0\n')),
        ],
        # Player shares all texture hashes with Hat (Diffuse, LightMap, MaterialMap)
        # and NormalMap with the shared set; see the Hat and Hair Components above.

        # ==================== Body Component ====================
        'feb1c4cd': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '76ceb325': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Body Draw VB Hash',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        ],
        'df17d505': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Body Position VB Hash',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        ],
        '3e19f179': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        ],
        '987395ef': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Body Blend VB Hash',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
        ],
        'a292d07d': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars BodyA and NeckA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d9dc65da', '639ad374'), 'BelleBrillianceOfStars.NeckA.Diffuse.1024')),
            (multiply_section_if_missing,     (('d9dc65da', '639ad374'), 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
        ],
        'fd906f9b': [
            (log,                             ('3.1: BelleBrillianceOfStars BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d9dc65da', '639ad374'), 'BelleBrillianceOfStars.BodyA.Diffuse.1024')),
        ],
        '639ad374': [
            (log,                             ('3.0 -> 3.1: BelleBrillianceOfStars BodyA and NeckA Diffuse 1024p Hash',)),
            (update_hash,                     ('d9dc65da',)),
        ],
        'd9dc65da': [
            (log,                             ('3.1: BelleBrillianceOfStars BodyA and NeckA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fd906f9b', 'a292d07d'), 'BelleBrillianceOfStars.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('a292d07d', 'BelleBrillianceOfStars.NeckA.Diffuse.2048')),
        ],
        '42310c0e': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars BodyA and NeckA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1f357ec', 'BelleBrillianceOfStars.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('e1f357ec', 'BelleBrillianceOfStars.NeckA.LightMap.1024')),
        ],
        'e1f357ec': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars BodyA and NeckA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('42310c0e', 'BelleBrillianceOfStars.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('42310c0e', 'BelleBrillianceOfStars.NeckA.LightMap.2048')),
        ],
        '5724e531': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars BodyA and NeckA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7c1fb5f6', 'BelleBrillianceOfStars.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7c1fb5f6', 'BelleBrillianceOfStars.NeckA.MaterialMap.1024')),
        ],
        '7c1fb5f6': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars BodyA and NeckA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('feb1c4cd', 'BelleBrillianceOfStars.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5724e531', 'BelleBrillianceOfStars.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('5724e531', 'BelleBrillianceOfStars.NeckA.MaterialMap.2048')),
        ],

        # ==================== Neck Component ====================
        'a6431856': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Neck IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0e72bdb7': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Neck Draw VB Hash',)),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        ],
        'd5c6a50f': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Neck Position VB Hash',)),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        ],
        '07a15f8e': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Neck Texcoord VB Hash',)),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        ],
        '57192494': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Neck Blend VB Hash',)),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
        ],
        'd9a12c0a': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars NeckA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('a6431856', 'BelleBrillianceOfStars.Neck.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'BelleBrillianceOfStars.NeckA.NormalMap.2048')),
        ],
        # Neck shares Diffuse, LightMap and MaterialMap hashes with Body, and NormalMap 2048p
        # with the shared set; see the Body and Hair Components above.

        # ==================== Face Component ====================
        '9a9780a7': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '04abceb5': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Face Draw VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
        ],
        '3eb95df2': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Face Position VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
        ],
        'd3000b22': [
            (log,                             ('3.0 -> 3.1: BelleBrillianceOfStars Face Texcoord Hash',)),
            (update_hash,                     ('228f5a8b',)),
        ],
        '228f5a8b': [
            (log,                             ('3.1: BelleBrillianceOfStars Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
        ],
        '359e4502': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars Face Blend VB Hash',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
        ],
        '75ec3614': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars FaceA and FaceB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77eef7e8', 'BelleBrillianceOfStars.FaceA.Diffuse.1024')),
            (multiply_section_if_missing,     ('77eef7e8', 'BelleBrillianceOfStars.FaceB.Diffuse.1024')),
        ],
        '77eef7e8': [
            (log,                             ('3.0 - 3.2: BelleBrillianceOfStars FaceA and FaceB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9a9780a7', 'BelleBrillianceOfStars.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('75ec3614', 'BelleBrillianceOfStars.FaceA.Diffuse.2048')),
            (multiply_section_if_missing,     ('75ec3614', 'BelleBrillianceOfStars.FaceB.Diffuse.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleBrillianceOfStars',
    'game_versions': ['3.0', '3.1', '3.2'],
}
