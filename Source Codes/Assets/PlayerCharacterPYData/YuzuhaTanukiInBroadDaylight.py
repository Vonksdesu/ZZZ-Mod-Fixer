"""
YuzuhaTanukiInBroadDaylight Character Hash Commands
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
    Returns YuzuhaTanukiInBroadDaylight's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '7a504287': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '630debc9': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Draw VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
        ],
        '051f9657': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Position VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
        ],
        'dc2821dc': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
        ],
        '606c88ae': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Blend VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
        ],
        '521a3242': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c9115930', 'YuzuhaTanukiInBroadDaylight.HairA.Diffuse.1024')),
        ],
        'c9115930': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('521a3242', 'YuzuhaTanukiInBroadDaylight.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA, BodyA, AccessoriesA, LeopardCat1A and weapon - 伞A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'YuzuhaTanukiInBroadDaylight.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YuzuhaTanukiInBroadDaylight.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('ebac056e', 'YuzuhaTanukiInBroadDaylight.AccessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '798adba3'), 'YuzuhaTanukiInBroadDaylight.AccessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1 -> 2.2: YuzuhaTanukiInBroadDaylight HairA, BodyA, AccessoriesA, LeopardCat1A and weapon - 伞A NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        'c400f5b7': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9730519', 'YuzuhaTanukiInBroadDaylight.HairA.LightMap.1024')),
        ],
        'a9730519': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c400f5b7', 'YuzuhaTanukiInBroadDaylight.HairA.LightMap.2048')),
        ],
        '3f70d124': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f5639e2', 'YuzuhaTanukiInBroadDaylight.HairA.MaterialMap.1024')),
        ],
        '4f5639e2': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f70d124', 'YuzuhaTanukiInBroadDaylight.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'afb6117a': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8a540628': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '3a4533fc': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a39c4806': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9fc9b6f8': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'b298482d': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f34fdc84': [
            (log,                             ('2.1 -> 2.11: YuzuhaTanukiInBroadDaylight Body IB Hash',)),
            (update_hash,                     ('b298482d',)),
        ],
        '07437c27': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Body Draw VB Hash',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        ],
        'cf3319f6': [
            (log,                             ('2.1 -> 2.11: YuzuhaTanukiInBroadDaylight Body Draw Hash',)),
            (update_hash,                     ('07437c27',)),
        ],
        '2a7b9144': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Body Position VB Hash',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        ],
        'a3b56c9b': [
            (log,                             ('2.1 -> 2.11: YuzuhaTanukiInBroadDaylight Body Position Hash',)),
            (update_hash,                     ('2a7b9144',)),
        ],
        '0c9062c5': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        ],
        '3d3199c5': [
            (log,                             ('2.1 -> 2.11: YuzuhaTanukiInBroadDaylight Body Texcoord Hash',)),
            (update_hash,                     ('0c9062c5',)),
        ],
        '523cf99d': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Body Blend VB Hash',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        ],
        'be70426a': [
            (log,                             ('2.1 -> 2.11: YuzuhaTanukiInBroadDaylight Body Blend Hash',)),
            (update_hash,                     ('523cf99d',)),
        ],
        '4f4c2b65': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7fc53810', 'YuzuhaTanukiInBroadDaylight.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('7fc53810', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.Diffuse.1024')),
        ],
        '7fc53810': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f4c2b65', 'YuzuhaTanukiInBroadDaylight.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('4f4c2b65', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.Diffuse.2048')),
        ],
        'c3e64779': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac06a4c8', 'YuzuhaTanukiInBroadDaylight.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('ac06a4c8', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.LightMap.1024')),
        ],
        'ac06a4c8': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c3e64779', 'YuzuhaTanukiInBroadDaylight.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('c3e64779', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.LightMap.2048')),
        ],
        'ac2f3dcb': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('58fd94ec', 'YuzuhaTanukiInBroadDaylight.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('58fd94ec', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.MaterialMap.1024')),
        ],
        '58fd94ec': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight BodyA and LeopardCat1A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac2f3dcb', 'YuzuhaTanukiInBroadDaylight.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('ac2f3dcb', 'YuzuhaTanukiInBroadDaylight.LeopardCat1A.MaterialMap.2048')),
        ],

        # ==================== Accessories Component ====================
        'a8de520e': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ca3209f7': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        ],
        'f271d524': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Accessories Position VB Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        ],
        'ce14b4b7': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        ],
        '294d341c': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        ],
        '54591ef6': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight AccessoriesA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54591ef6', 'YuzuhaTanukiInBroadDaylight.AccessoriesA.Diffuse.2048')),
            (multiply_section_if_missing,     (('54591ef6', '9f387d35'), 'YuzuhaTanukiInBroadDaylight.AccessoriesA.Diffuse.1024')),
        ],
        '9f387d35': [
            (log,                             ('3.1 -> 2.2: YuzuhaTanukiInBroadDaylight AccessoriesA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (update_hash,                     ('54591ef6',)),
        ],
        'a78340ed': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight AccessoriesA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a78340ed', 'YuzuhaTanukiInBroadDaylight.AccessoriesA.LightMap.2048')),
            (multiply_section_if_missing,     (('a78340ed', '00bcfe90'), 'YuzuhaTanukiInBroadDaylight.AccessoriesA.LightMap.1024')),
        ],
        '00bcfe90': [
            (log,                             ('3.1 -> 2.2: YuzuhaTanukiInBroadDaylight AccessoriesA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (update_hash,                     ('a78340ed',)),
        ],
        '1d0dabdb': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight AccessoriesA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d0dabdb', 'YuzuhaTanukiInBroadDaylight.AccessoriesA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('1d0dabdb', 'c2c76575'), 'YuzuhaTanukiInBroadDaylight.AccessoriesA.MaterialMap.1024')),
        ],
        'c2c76575': [
            (log,                             ('3.1 -> 2.2: YuzuhaTanukiInBroadDaylight AccessoriesA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
            (update_hash,                     ('1d0dabdb',)),
        ],

        # ==================== LeopardCat1 Component ====================
        '14ac0d52': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight LeopardCat1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b6e62152': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight LeopardCat1 Draw VB Hash',)),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        '9d4425e5': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight LeopardCat1 Position VB Hash',)),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        'a7394f34': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight LeopardCat1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        '2a45c137': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight LeopardCat1 Blend VB Hash',)),
            (add_section_if_missing,          ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '507384ea': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3578d11c': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
        ],
        '0f6a425b': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Face Position VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
        ],
        '9d0f7ef5': [
            (log,                             ('2.2 - 3.1: YuzuhaTanukiInBroadDaylight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('37a09c33',)),
        ],
        '37a09c33': [
            (log,                             ('3.2: YuzuhaTanukiInBroadDaylight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '52400cce': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight Face Blend VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
        ],
        'd394bc13': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('59f9e66f', 'YuzuhaTanukiInBroadDaylight.FaceA.Diffuse.1024')),
        ],
        '59f9e66f': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d394bc13', 'YuzuhaTanukiInBroadDaylight.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 伞 Component ====================
        'b34a880c': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b36355ab': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        '79849b37': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞 Position VB Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        'd5283f28': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        'd7204982': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞 Blend VB Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        'caeee529': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c8cb308c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.Diffuse.1024')),
        ],
        'c8cb308c': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('caeee529', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.Diffuse.2048')),
        ],
        'f74f81e8': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc683116', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.LightMap.1024')),
        ],
        'dc683116': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f74f81e8', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.LightMap.2048')),
        ],
        '6657efd2': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('114dafdf', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.MaterialMap.1024')),
        ],
        '114dafdf': [
            (log,                             ('2.2 - 3.2: YuzuhaTanukiInBroadDaylight weapon - 伞A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6657efd2', 'YuzuhaTanukiInBroadDaylight.weapon - 伞A.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YuzuhaTanukiInBroadDaylight',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
