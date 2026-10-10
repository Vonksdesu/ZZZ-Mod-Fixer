"""
Yuzuha Character Hash Commands
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
    Returns Yuzuha's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '7a504287': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '630debc9': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Draw VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        ],
        '051f9657': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Position VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        ],
        'dc2821dc': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        ],
        '606c88ae': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Blend VB Hash',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
        ],
        '521a3242': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c9115930', 'Yuzuha.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c9115930', 'Yuzuha.LegsA.Diffuse.1024')),
        ],
        'c9115930': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('521a3242', 'Yuzuha.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('521a3242', 'Yuzuha.LegsA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA, BodyA, LegsA, LeopardCat1A, LeopardCat2A, StrapsA and weapon - 伞A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.LeopardCat1A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.LeopardCat2A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.StrapsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yuzuha.weapon - 伞A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA, BodyA, LegsA, LeopardCat1A, LeopardCat2A, StrapsA and weapon - 伞A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.LeopardCat1A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.LeopardCat2A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.StrapsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yuzuha.weapon - 伞A.NormalMap.2048')),
        ],
        'c400f5b7': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9730519', 'Yuzuha.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('a9730519', 'Yuzuha.LegsA.LightMap.1024')),
        ],
        'a9730519': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c400f5b7', 'Yuzuha.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('c400f5b7', 'Yuzuha.LegsA.LightMap.2048')),
        ],
        '3f70d124': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f5639e2', 'Yuzuha.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('4f5639e2', 'Yuzuha.LegsA.MaterialMap.1024')),
        ],
        '4f5639e2': [
            (log,                             ('2.2 - 3.2: Yuzuha HairA and LegsA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7a504287', 'Yuzuha.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f70d124', 'Yuzuha.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('3f70d124', 'Yuzuha.LegsA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'afb6117a': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8a540628': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '3a4533fc': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a39c4806': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9fc9b6f8': [
            (log,                             ('2.2 - 3.2: Yuzuha Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('afb6117a', 'Yuzuha.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '5144c409': [
            (log,                             ('2.2 - 3.2: Yuzuha Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2a99e69b': [
            (log,                             ('2.2 - 3.2: Yuzuha Body Draw VB Hash',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        ],
        '20d44382': [
            (log,                             ('2.2 - 3.2: Yuzuha Body Position VB Hash',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        ],
        '688588f1': [
            (log,                             ('2.2 - 3.2: Yuzuha Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        ],
        '0db66603': [
            (log,                             ('2.2 - 3.2: Yuzuha Body Blend VB Hash',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
        ],
        'be85f061': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fabf669', 'Yuzuha.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1fabf669', 'Yuzuha.LeopardCat1A.Diffuse.1024')),
            (multiply_section_if_missing,     ('1fabf669', 'Yuzuha.LeopardCat2A.Diffuse.1024')),
            (multiply_section_if_missing,     ('1fabf669', 'Yuzuha.StrapsA.Diffuse.1024')),
        ],
        '1fabf669': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be85f061', 'Yuzuha.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('be85f061', 'Yuzuha.LeopardCat1A.Diffuse.2048')),
            (multiply_section_if_missing,     ('be85f061', 'Yuzuha.LeopardCat2A.Diffuse.2048')),
            (multiply_section_if_missing,     ('be85f061', 'Yuzuha.StrapsA.Diffuse.2048')),
        ],
        'ef192425': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eff3b0b0', 'Yuzuha.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('eff3b0b0', 'Yuzuha.LeopardCat1A.LightMap.1024')),
            (multiply_section_if_missing,     ('eff3b0b0', 'Yuzuha.LeopardCat2A.LightMap.1024')),
            (multiply_section_if_missing,     ('eff3b0b0', 'Yuzuha.StrapsA.LightMap.1024')),
        ],
        'eff3b0b0': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef192425', 'Yuzuha.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('ef192425', 'Yuzuha.LeopardCat1A.LightMap.2048')),
            (multiply_section_if_missing,     ('ef192425', 'Yuzuha.LeopardCat2A.LightMap.2048')),
            (multiply_section_if_missing,     ('ef192425', 'Yuzuha.StrapsA.LightMap.2048')),
        ],
        '76e5c6b7': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2fb36ecb', 'Yuzuha.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2fb36ecb', 'Yuzuha.LeopardCat1A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2fb36ecb', 'Yuzuha.LeopardCat2A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2fb36ecb', 'Yuzuha.StrapsA.MaterialMap.1024')),
        ],
        '2fb36ecb': [
            (log,                             ('2.2 - 3.2: Yuzuha BodyA, LeopardCat1A, LeopardCat2A and StrapsA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5144c409', 'Yuzuha.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76e5c6b7', 'Yuzuha.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('76e5c6b7', 'Yuzuha.LeopardCat1A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('76e5c6b7', 'Yuzuha.LeopardCat2A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('76e5c6b7', 'Yuzuha.StrapsA.MaterialMap.2048')),
        ],

        # ==================== Legs Component ====================
        '73757570': [
            (log,                             ('2.2 - 3.2: Yuzuha Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '93b3c078': [
            (log,                             ('2.2 - 3.2: Yuzuha Legs Draw VB Hash',)),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        ],
        'bc6a9f6f': [
            (log,                             ('2.2 - 3.2: Yuzuha Legs Position VB Hash',)),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        ],
        '882cf302': [
            (log,                             ('2.2 - 3.2: Yuzuha Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        ],
        '6fe5c40e': [
            (log,                             ('2.2 - 3.2: Yuzuha Legs Blend VB Hash',)),
            (add_section_if_missing,          ('73757570', 'Yuzuha.Legs.IB', 'match_priority = 0\n')),
        ],

        # ==================== LeopardCat1 Component ====================
        'e72984d1': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1a6468e1': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat1 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        '773bdaa3': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat1 Position VB Hash',)),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        'a5097f50': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
        ],
        '085ab253': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat1 Blend VB Hash',)),
            (add_section_if_missing,          ('e72984d1', 'Yuzuha.LeopardCat1.IB', 'match_priority = 0\n')),
        ],

        # ==================== LeopardCat2 Component ====================
        '81bca595': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '39b6000b': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat2 Draw VB Hash',)),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        ],
        '9662128e': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat2 Position VB Hash',)),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        ],
        'f95d8b57': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        ],
        'ba80c02b': [
            (log,                             ('2.2 - 3.2: Yuzuha LeopardCat2 Blend VB Hash',)),
            (add_section_if_missing,          ('81bca595', 'Yuzuha.LeopardCat2.IB', 'match_priority = 0\n')),
        ],

        # ==================== Straps Component ====================
        'cf3172e4': [
            (log,                             ('2.2 - 3.2: Yuzuha Straps IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '966e777b': [
            (log,                             ('2.2 - 3.2: Yuzuha Straps Draw VB Hash',)),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
        ],
        'b543b8d8': [
            (log,                             ('2.2 - 3.2: Yuzuha Straps Position VB Hash',)),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
        ],
        '4b13802b': [
            (log,                             ('2.2 - 3.2: Yuzuha Straps Texcoord VB Hash',)),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
        ],
        '7ca97675': [
            (log,                             ('2.2 - 3.2: Yuzuha Straps Blend VB Hash',)),
            (add_section_if_missing,          ('cf3172e4', 'Yuzuha.Straps.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '507384ea': [
            (log,                             ('2.2 - 3.2: Yuzuha Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3578d11c': [
            (log,                             ('2.2 - 3.2: Yuzuha Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
        ],
        '0f6a425b': [
            (log,                             ('2.2 - 3.2: Yuzuha Face Position VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
        ],
        '9d0f7ef5': [
            (log,                             ('2.2 - 3.1: Yuzuha Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('37a09c33',)),
        ],
        '37a09c33': [
            (log,                             ('3.2: Yuzuha Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '52400cce': [
            (log,                             ('2.2 - 3.2: Yuzuha Face Blend VB Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
        ],
        'd394bc13': [
            (log,                             ('2.2 - 3.2: Yuzuha FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('59f9e66f', 'Yuzuha.FaceA.Diffuse.1024')),
        ],
        '59f9e66f': [
            (log,                             ('2.2 - 3.2: Yuzuha FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('507384ea', 'Yuzuha.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d394bc13', 'Yuzuha.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 伞 Component ====================
        '2686f517': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '79c257b3': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        '1686ac84': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞 Position VB Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        '8a182e58': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞 Texcoord VB Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        '7d11ecaa': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞 Blend VB Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
        ],
        '7139e5b0': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('68856c57', 'Yuzuha.weapon - 伞A.Diffuse.1024')),
        ],
        '68856c57': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7139e5b0', 'Yuzuha.weapon - 伞A.Diffuse.2048')),
        ],
        '9dcd6e8e': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4fe5c926', 'Yuzuha.weapon - 伞A.LightMap.1024')),
        ],
        '4fe5c926': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9dcd6e8e', 'Yuzuha.weapon - 伞A.LightMap.2048')),
        ],
        '85142f08': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d0c14d9d', 'Yuzuha.weapon - 伞A.MaterialMap.1024')),
        ],
        'd0c14d9d': [
            (log,                             ('2.2 - 3.2: Yuzuha weapon - 伞A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2686f517', 'Yuzuha.weapon - 伞.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('85142f08', 'Yuzuha.weapon - 伞A.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yuzuha',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
