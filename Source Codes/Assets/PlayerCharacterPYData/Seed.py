"""
Seed Character Hash Commands
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
    Returns Seed's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '6cb35165': [
            (log,                             ('2.2 - 3.2: Seed Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '12bd16f4': [
            (log,                             ('2.2 - 3.2: Seed Hair Draw VB Hash',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        ],
        '25a8bde2': [
            (log,                             ('2.2 - 3.2: Seed Hair Position VB Hash',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        ],
        '9e25742c': [
            (log,                             ('2.2 - 3.2: Seed Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        ],
        'afe31e96': [
            (log,                             ('2.2 - 3.2: Seed Hair Blend VB Hash',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
        ],
        '2fff22a7': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9d4019f4', 'Seed.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9d4019f4', 'Seed.AccessoriesA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9d4019f4', 'Seed.ChestClothingA.Diffuse.1024')),
        ],
        '9d4019f4': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2fff22a7', 'Seed.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('2fff22a7', 'Seed.AccessoriesA.Diffuse.2048')),
            (multiply_section_if_missing,     ('2fff22a7', 'Seed.ChestClothingA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Seed HairA, BodyA, AccessoriesA, ChestClothingA, SelfBalancingScooterA, weapon - 常驻状态A, weapon - 躯干A, weapon - 手足A, weapon - 手部装置A and weapon - 背部装置A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.AccessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.ChestClothingA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.SelfBalancingScooterA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.weapon - 常驻状态A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.weapon - 躯干A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.weapon - 手足A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.weapon - 手部装置A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seed.weapon - 背部装置A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Seed HairA, BodyA, AccessoriesA, ChestClothingA, SelfBalancingScooterA, weapon - 常驻状态A, weapon - 躯干A, weapon - 手足A, weapon - 手部装置A and weapon - 背部装置A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.AccessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.ChestClothingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.SelfBalancingScooterA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.weapon - 常驻状态A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.weapon - 躯干A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.weapon - 手足A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.weapon - 手部装置A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seed.weapon - 背部装置A.NormalMap.2048')),
        ],
        'bf2c273a': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e7efee45', 'Seed.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('e7efee45', 'Seed.AccessoriesA.LightMap.1024')),
            (multiply_section_if_missing,     ('e7efee45', 'Seed.ChestClothingA.LightMap.1024')),
        ],
        'e7efee45': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf2c273a', 'Seed.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('bf2c273a', 'Seed.AccessoriesA.LightMap.2048')),
            (multiply_section_if_missing,     ('bf2c273a', 'Seed.ChestClothingA.LightMap.2048')),
        ],
        'a1658bbd': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bfcfcdc6', 'Seed.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('bfcfcdc6', 'Seed.AccessoriesA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('bfcfcdc6', 'Seed.ChestClothingA.MaterialMap.1024')),
        ],
        'bfcfcdc6': [
            (log,                             ('2.2 - 3.2: Seed HairA, AccessoriesA and ChestClothingA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6cb35165', 'Seed.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a1658bbd', 'Seed.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a1658bbd', 'Seed.AccessoriesA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a1658bbd', 'Seed.ChestClothingA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '468e0f21': [
            (log,                             ('2.2 - 3.2: Seed Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4d61e6f3': [
            (log,                             ('2.2 - 3.2: Seed Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '3a097353': [
            (log,                             ('2.2 - 3.2: Seed Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9f4d4106': [
            (log,                             ('2.2 - 3.2: Seed Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '1abfa087': [
            (log,                             ('2.2 - 3.2: Seed Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('468e0f21', 'Seed.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '634ac589': [
            (log,                             ('2.2 - 3.2: Seed Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '43185be9': [
            (log,                             ('2.2 - 3.2: Seed Body Draw VB Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        ],
        '5e2f1e06': [
            (log,                             ('2.2 - 3.2: Seed Body Position VB Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        ],
        'f4cf83ff': [
            (log,                             ('2.2 - 3.2: Seed Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        ],
        '5b3d022f': [
            (log,                             ('2.2 - 3.2: Seed Body Blend VB Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
        ],
        '7c7c2622': [
            (log,                             ('2.2 - 3.2: Seed BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('684d2bd5', 'Seed.BodyA.Diffuse.1024')),
        ],
        '684d2bd5': [
            (log,                             ('2.2 - 3.2: Seed BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7c7c2622', 'Seed.BodyA.Diffuse.2048')),
        ],
        'b14c9c6f': [
            (log,                             ('2.2 - 3.2: Seed BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('522ee460', 'Seed.BodyA.LightMap.1024')),
        ],
        '522ee460': [
            (log,                             ('2.2 - 3.2: Seed BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b14c9c6f', 'Seed.BodyA.LightMap.2048')),
        ],
        'da2deeaa': [
            (log,                             ('2.2 - 3.2: Seed BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be9dd4c2', 'Seed.BodyA.MaterialMap.1024')),
        ],
        'be9dd4c2': [
            (log,                             ('2.2 - 3.2: Seed BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('634ac589', 'Seed.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('da2deeaa', 'Seed.BodyA.MaterialMap.2048')),
        ],

        # ==================== Accessories Component ====================
        '914e39c6': [
            (log,                             ('2.2 - 3.2: Seed Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c24ebf3b': [
            (log,                             ('2.2 - 3.2: Seed Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        ],
        '12d6c223': [
            (log,                             ('2.2 - 3.2: Seed Accessories Position VB Hash',)),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        ],
        '99be167f': [
            (log,                             ('2.2 - 3.2: Seed Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        ],
        '746e7bf8': [
            (log,                             ('2.2 - 3.2: Seed Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('914e39c6', 'Seed.Accessories.IB', 'match_priority = 0\n')),
        ],

        # ==================== ChestClothing Component ====================
        '1d81bcc7': [
            (log,                             ('2.2 - 3.2: Seed ChestClothing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '72fbbba3': [
            (log,                             ('2.2 - 3.2: Seed ChestClothing Draw VB Hash',)),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
        ],
        'b2690ac8': [
            (log,                             ('2.2 - 3.2: Seed ChestClothing Position VB Hash',)),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
        ],
        '2f706a18': [
            (log,                             ('2.2 - 3.2: Seed ChestClothing Texcoord VB Hash',)),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
        ],
        '319ba025': [
            (log,                             ('2.2 - 3.2: Seed ChestClothing Blend VB Hash',)),
            (add_section_if_missing,          ('1d81bcc7', 'Seed.ChestClothing.IB', 'match_priority = 0\n')),
        ],

        # ==================== SelfBalancingScooter Component ====================
        '651f4fd5': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooter IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2d77a8c9': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooter Draw VB Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
        ],
        '95941dba': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooter Position VB Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
        ],
        '4635f4f0': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooter Texcoord VB Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
        ],
        '547acb7e': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooter Blend VB Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
        ],
        '91d18cf9': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('74b9c4c8', 'Seed.SelfBalancingScooterA.Diffuse.1024')),
        ],
        '74b9c4c8': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91d18cf9', 'Seed.SelfBalancingScooterA.Diffuse.2048')),
        ],
        'a6726612': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd0f0925', 'Seed.SelfBalancingScooterA.LightMap.1024')),
        ],
        'bd0f0925': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a6726612', 'Seed.SelfBalancingScooterA.LightMap.2048')),
        ],
        '9896a7c2': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f7b60c9', 'Seed.SelfBalancingScooterA.MaterialMap.1024')),
        ],
        '7f7b60c9': [
            (log,                             ('2.2 - 3.2: Seed SelfBalancingScooterA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('651f4fd5', 'Seed.SelfBalancingScooter.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9896a7c2', 'Seed.SelfBalancingScooterA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '09d9dca7': [
            (log,                             ('2.2 - 3.2: Seed Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '064aa73b': [
            (log,                             ('2.2 - 3.2: Seed Face Draw VB Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
        ],
        '3c58347c': [
            (log,                             ('2.2 - 3.2: Seed Face Position VB Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
        ],
        'a0dfaf80': [
            (log,                             ('2.2 - 3.1: Seed Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2bcb59f6',)),
        ],
        '2bcb59f6': [
            (log,                             ('3.2: Seed Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7625e6d6': [
            (log,                             ('2.2 - 3.2: Seed Face Blend VB Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
        ],
        'f02ebff3': [
            (log,                             ('2.2 - 3.2: Seed FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a7e3da19', 'Seed.FaceA.Diffuse.1024')),
        ],
        'a7e3da19': [
            (log,                             ('2.2 - 3.2: Seed FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('09d9dca7', 'Seed.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f02ebff3', 'Seed.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 常驻状态 Component ====================
        'c7f4f4ec': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0238f9fc': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态 Draw VB Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
        ],
        '8bb86a2d': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态 Position VB Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
        ],
        '5abfc179': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态 Texcoord VB Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
        ],
        'b6b679de': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态 Blend VB Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
        ],
        'a06afdbc': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('11be1be8', 'Seed.weapon - 常驻状态A.Diffuse.1024')),
        ],
        '11be1be8': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a06afdbc', 'Seed.weapon - 常驻状态A.Diffuse.2048')),
        ],
        'dd157642': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7a71ca0', 'Seed.weapon - 常驻状态A.LightMap.1024')),
        ],
        'c7a71ca0': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd157642', 'Seed.weapon - 常驻状态A.LightMap.2048')),
        ],
        '54a8ad89': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6cdfa1b1', 'Seed.weapon - 常驻状态A.MaterialMap.1024')),
        ],
        '6cdfa1b1': [
            (log,                             ('2.2 - 3.2: Seed weapon - 常驻状态A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('c7f4f4ec', 'Seed.weapon - 常驻状态.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54a8ad89', 'Seed.weapon - 常驻状态A.MaterialMap.2048')),
        ],

        # ==================== weapon - 驾驶舱 Component ====================
        '75e1ae0a': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5bca6676': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱 Draw VB Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
        ],
        'b095c5cf': [
            (log,                             ('2.2 -> 2.3: Seed weapon - 驾驶舱 Position Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (update_hash,                     ('567f9bcd',)),
        ],
        '567f9bcd': [
            (log,                             ('2.3 - 3.2: Seed weapon - 驾驶舱 Position VB Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
        ],
        '56979e94': [
            (log,                             ('2.2 -> 2.3: Seed weapon - 驾驶舱 Texcoord Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (update_hash,                     ('030e0aca',)),
        ],
        '030e0aca': [
            (log,                             ('2.3 - 3.2: Seed weapon - 驾驶舱 Texcoord VB Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
        ],
        '10c13253': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱 Blend VB Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
        ],
        'b2e81a28': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d8e36eca', 'Seed.weapon - 驾驶舱A.Diffuse.1024')),
        ],
        'd8e36eca': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b2e81a28', 'Seed.weapon - 驾驶舱A.Diffuse.2048')),
        ],
        'fc59be11': [
            (log,                             ('2.2 -> 2.3: Seed weapon - 驾驶舱A NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b35534a9',)),
        ],
        'b35534a9': [
            (log,                             ('2.3 - 2.7: Seed weapon - 驾驶舱A NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b87d9c50', 'Seed.weapon - 驾驶舱A.NormalMap.1024')),
        ],
        'b87d9c50': [
            (log,                             ('2.2 - 2.3: Seed weapon - 驾驶舱A NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b35534a9', 'Seed.weapon - 驾驶舱A.NormalMap.2048')),
        ],
        '6f269065': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bb3bae0e', 'Seed.weapon - 驾驶舱A.LightMap.1024')),
        ],
        'bb3bae0e': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f269065', 'Seed.weapon - 驾驶舱A.LightMap.2048')),
        ],
        'ceb90df0': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('efeed071', 'Seed.weapon - 驾驶舱A.MaterialMap.1024')),
        ],
        'efeed071': [
            (log,                             ('2.2 - 3.2: Seed weapon - 驾驶舱A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('75e1ae0a', 'Seed.weapon - 驾驶舱.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ceb90df0', 'Seed.weapon - 驾驶舱A.MaterialMap.2048')),
        ],

        # ==================== weapon - 躯干 Component ====================
        'b3f47664': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b7c36a17': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干 Draw VB Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
        ],
        'e2694177': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干 Position VB Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
        ],
        'efc82ade': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
        ],
        '09c28e33': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干 Blend VB Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
        ],
        '0a4cecd8': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a44bbeb3', 'Seed.weapon - 躯干A.Diffuse.1024')),
        ],
        'a44bbeb3': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0a4cecd8', 'Seed.weapon - 躯干A.Diffuse.2048')),
        ],
        '1962d85c': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3d66757d', 'Seed.weapon - 躯干A.LightMap.1024')),
        ],
        '3d66757d': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1962d85c', 'Seed.weapon - 躯干A.LightMap.2048')),
        ],
        '64bb6cb7': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5fa93693', 'Seed.weapon - 躯干A.MaterialMap.1024')),
        ],
        '5fa93693': [
            (log,                             ('2.2 - 3.2: Seed weapon - 躯干A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b3f47664', 'Seed.weapon - 躯干.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('64bb6cb7', 'Seed.weapon - 躯干A.MaterialMap.2048')),
        ],

        # ==================== weapon - 手足 Component ====================
        '126bd0a1': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e0736df2': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足 Draw VB Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
        ],
        'fdfdf144': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足 Position VB Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
        ],
        '255a77a9': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足 Texcoord VB Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
        ],
        '98f46d5b': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足 Blend VB Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
        ],
        'a065222f': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('93c858df', 'Seed.weapon - 手足A.Diffuse.1024')),
        ],
        '93c858df': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a065222f', 'Seed.weapon - 手足A.Diffuse.2048')),
        ],
        'f56f3ac1': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('494e24a6', 'Seed.weapon - 手足A.LightMap.1024')),
        ],
        '494e24a6': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f56f3ac1', 'Seed.weapon - 手足A.LightMap.2048')),
        ],
        'caf87ff4': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7832e989', 'Seed.weapon - 手足A.MaterialMap.1024')),
        ],
        '7832e989': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手足A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('126bd0a1', 'Seed.weapon - 手足.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('caf87ff4', 'Seed.weapon - 手足A.MaterialMap.2048')),
        ],

        # ==================== weapon - 手部装置 Component ====================
        '71e8d07a': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c6043e88': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置 Draw VB Hash',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
        ],
        '143481a0': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置 Position VB Hash',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
        ],
        'd06b00ad': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置 Texcoord VB Hash',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
        ],
        'd3adb384': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置 Blend VB Hash',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
        ],
        'a9a40828': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2e2a9097', 'Seed.weapon - 手部装置A.Diffuse.1024')),
            (multiply_section_if_missing,     ('2e2a9097', 'Seed.weapon - 背部装置A.Diffuse.1024')),
        ],
        '2e2a9097': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9a40828', 'Seed.weapon - 手部装置A.Diffuse.2048')),
            (multiply_section_if_missing,     ('a9a40828', 'Seed.weapon - 背部装置A.Diffuse.2048')),
        ],
        'd6e62b3f': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cc24383a', 'Seed.weapon - 手部装置A.LightMap.1024')),
            (multiply_section_if_missing,     ('cc24383a', 'Seed.weapon - 背部装置A.LightMap.1024')),
        ],
        'cc24383a': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d6e62b3f', 'Seed.weapon - 手部装置A.LightMap.2048')),
            (multiply_section_if_missing,     ('d6e62b3f', 'Seed.weapon - 背部装置A.LightMap.2048')),
        ],
        'bc0bd24c': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4be2f394', 'Seed.weapon - 手部装置A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('4be2f394', 'Seed.weapon - 背部装置A.MaterialMap.1024')),
        ],
        '4be2f394': [
            (log,                             ('2.2 - 3.2: Seed weapon - 手部装置A and weapon - 背部装置A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('71e8d07a', 'Seed.weapon - 手部装置.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc0bd24c', 'Seed.weapon - 手部装置A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('bc0bd24c', 'Seed.weapon - 背部装置A.MaterialMap.2048')),
        ],

        # ==================== weapon - 背部装置 Component ====================
        '8a995990': [
            (log,                             ('2.2 - 3.2: Seed weapon - 背部装置 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3253babd': [
            (log,                             ('2.2 - 3.2: Seed weapon - 背部装置 Draw VB Hash',)),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
        ],
        'f66c29e6': [
            (log,                             ('2.2 - 3.2: Seed weapon - 背部装置 Position VB Hash',)),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
        ],
        '72329a18': [
            (log,                             ('2.2 - 3.2: Seed weapon - 背部装置 Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
        ],
        '8cb92072': [
            (log,                             ('2.2 - 3.2: Seed weapon - 背部装置 Blend VB Hash',)),
            (add_section_if_missing,          ('8a995990', 'Seed.weapon - 背部装置.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seed',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
