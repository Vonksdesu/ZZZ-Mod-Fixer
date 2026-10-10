"""
RemielleMoonlightWhispers Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.1 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns RemielleMoonlightWhispers's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '789ae812': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fbe70114': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair Draw VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
        ],
        '62b7da5e': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair Position VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
        ],
        'fa8ab367': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
        ],
        '46eee329': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair Blend VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
        ],
        '578239d7': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a619774', 'RemielleMoonlightWhispers.HairA.Diffuse.1024')),
        ],
        '8a619774': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('578239d7', 'RemielleMoonlightWhispers.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA, BodyA, LegA and WingsA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleMoonlightWhispers.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleMoonlightWhispers.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleMoonlightWhispers.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleMoonlightWhispers.WingsA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA, BodyA, LegA and WingsA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleMoonlightWhispers.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleMoonlightWhispers.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleMoonlightWhispers.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleMoonlightWhispers.WingsA.NormalMap.2048')),
        ],
        '6f826e7d': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45bb8a18', 'RemielleMoonlightWhispers.HairA.LightMap.1024')),
        ],
        '45bb8a18': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f826e7d', 'RemielleMoonlightWhispers.HairA.LightMap.2048')),
        ],
        'b5a12580': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b8df55e', 'RemielleMoonlightWhispers.HairA.MaterialMap.1024')),
        ],
        '8b8df55e': [
            (log,                             ('3.1: RemielleMoonlightWhispers HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleMoonlightWhispers.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5a12580', 'RemielleMoonlightWhispers.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3a0100ab': [
            (log,                             ('3.1: RemielleMoonlightWhispers Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        'f57f3e40': [
            (log,                             ('3.1: RemielleMoonlightWhispers Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('92cb56c9',)),
        ],
        '92cb56c9': [
            (log,                             ('3.2: RemielleMoonlightWhispers Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '22ec622c': [
            (log,                             ('3.1: RemielleMoonlightWhispers Body Draw VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('6a0d36f2',)),
        ],
        '6a0d36f2': [
            (log,                             ('3.2: RemielleMoonlightWhispers Body Draw VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
        ],
        '554d46cf': [
            (log,                             ('3.1: RemielleMoonlightWhispers Body Position VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('0929171b',)),
        ],
        '0929171b': [
            (log,                             ('3.2: RemielleMoonlightWhispers Body Position VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
        ],
        '5dcc6ee1': [
            (log,                             ('3.1: RemielleMoonlightWhispers Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c24cc6a1',)),
        ],
        'c24cc6a1': [
            (log,                             ('3.2: RemielleMoonlightWhispers Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
        ],
        '7f6fe876': [
            (log,                             ('3.1: RemielleMoonlightWhispers Body Blend VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('93b69961',)),
        ],
        '93b69961': [
            (log,                             ('3.2: RemielleMoonlightWhispers Body Blend VB Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
        ],
        '0e408177': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('578353ea', 'abb0d69d'), 'RemielleMoonlightWhispers.BodyA.Diffuse.1024')),
            (update_hash,                     ('bb0f08b9',)),
        ],
        'bb0f08b9': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('578353ea', 'abb0d69d'), 'RemielleMoonlightWhispers.BodyA.Diffuse.1024')),
        ],
        'abb0d69d': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('bb0f08b9', '0e408177'), 'RemielleMoonlightWhispers.BodyA.Diffuse.2048')),
            (update_hash,                     ('578353ea',)),
        ],
        '578353ea': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('bb0f08b9', '0e408177'), 'RemielleMoonlightWhispers.BodyA.Diffuse.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        '6102ae18': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('312bbc0c', '2aab9aa7'), 'RemielleMoonlightWhispers.BodyA.LightMap.1024')),
            (update_hash,                     ('0e9d14dc',)),
        ],
        '0e9d14dc': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('312bbc0c', '2aab9aa7'), 'RemielleMoonlightWhispers.BodyA.LightMap.1024')),
        ],
        '2aab9aa7': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0e9d14dc', '6102ae18'), 'RemielleMoonlightWhispers.BodyA.LightMap.2048')),
            (update_hash,                     ('312bbc0c',)),
        ],
        '312bbc0c': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0e9d14dc', '6102ae18'), 'RemielleMoonlightWhispers.BodyA.LightMap.2048')),
        ],
        'cccb8109': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2367a92b', 'e9f33a20'), 'RemielleMoonlightWhispers.BodyA.MaterialMap.1024')),
            (update_hash,                     ('8240c688',)),
        ],
        '8240c688': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2367a92b', 'e9f33a20'), 'RemielleMoonlightWhispers.BodyA.MaterialMap.1024')),
        ],
        'e9f33a20': [
            (log,                             ('3.1: RemielleMoonlightWhispers BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8240c688', 'cccb8109'), 'RemielleMoonlightWhispers.BodyA.MaterialMap.2048')),
            (update_hash,                     ('2367a92b',)),
        ],
        '2367a92b': [
            (log,                             ('3.2: RemielleMoonlightWhispers BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('f57f3e40', 'RemielleMoonlightWhispers.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8240c688', 'cccb8109'), 'RemielleMoonlightWhispers.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        '09a51ed3': [
            (log,                             ('3.1: RemielleMoonlightWhispers Leg IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('24a512cb',)),
        ],
        '24a512cb': [
            (log,                             ('3.2: RemielleMoonlightWhispers Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '96dc0a8e': [
            (log,                             ('3.1: RemielleMoonlightWhispers Leg Draw VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ea50e1d1',)),
        ],
        'ea50e1d1': [
            (log,                             ('3.2: RemielleMoonlightWhispers Leg Draw VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
        ],
        'fa9635bc': [
            (log,                             ('3.1: RemielleMoonlightWhispers Leg Position VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('11fbd4a3',)),
        ],
        '11fbd4a3': [
            (log,                             ('3.2: RemielleMoonlightWhispers Leg Position VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
        ],
        '7c0db158': [
            (log,                             ('3.1: RemielleMoonlightWhispers Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('14ab0adc',)),
        ],
        '14ab0adc': [
            (log,                             ('3.2: RemielleMoonlightWhispers Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
        ],
        'ff05e5f9': [
            (log,                             ('3.1: RemielleMoonlightWhispers Leg Blend VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (update_hash,                     ('3841a909',)),
        ],
        '3841a909': [
            (log,                             ('3.2: RemielleMoonlightWhispers Leg Blend VB Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
        ],
        '877b0ce6': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d0eb079f', '4c49a23c'), 'RemielleMoonlightWhispers.LegA.Diffuse.1024')),
            (update_hash,                     ('017c13e4',)),
        ],
        '017c13e4': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d0eb079f', '4c49a23c'), 'RemielleMoonlightWhispers.LegA.Diffuse.1024')),
        ],
        '4c49a23c': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('017c13e4', '877b0ce6'), 'RemielleMoonlightWhispers.LegA.Diffuse.2048')),
            (update_hash,                     ('d0eb079f',)),
        ],
        'd0eb079f': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('017c13e4', '877b0ce6'), 'RemielleMoonlightWhispers.LegA.Diffuse.2048')),
        ],
        # Leg shares its NormalMap hashes with Hair; see that Component above.
        'baeb2662': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b9a73372', '17b9c313'), 'RemielleMoonlightWhispers.LegA.LightMap.1024')),
            (update_hash,                     ('0a902460',)),
        ],
        '0a902460': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b9a73372', '17b9c313'), 'RemielleMoonlightWhispers.LegA.LightMap.1024')),
        ],
        '17b9c313': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0a902460', 'baeb2662'), 'RemielleMoonlightWhispers.LegA.LightMap.2048')),
            (update_hash,                     ('b9a73372',)),
        ],
        'b9a73372': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0a902460', 'baeb2662'), 'RemielleMoonlightWhispers.LegA.LightMap.2048')),
        ],
        '3b0c9e0a': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0b54d931', '2dce69bd'), 'RemielleMoonlightWhispers.LegA.MaterialMap.1024')),
            (update_hash,                     ('fb096287',)),
        ],
        'fb096287': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('0b54d931', '2dce69bd'), 'RemielleMoonlightWhispers.LegA.MaterialMap.1024')),
        ],
        '2dce69bd': [
            (log,                             ('3.1: RemielleMoonlightWhispers LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fb096287', '3b0c9e0a'), 'RemielleMoonlightWhispers.LegA.MaterialMap.2048')),
            (update_hash,                     ('0b54d931',)),
        ],
        '0b54d931': [
            (log,                             ('3.2: RemielleMoonlightWhispers LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('09a51ed3', 'RemielleMoonlightWhispers.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fb096287', '3b0c9e0a'), 'RemielleMoonlightWhispers.LegA.MaterialMap.2048')),
        ],

        # ==================== Wings Component ====================
        '9004a39a': [
            (log,                             ('3.1: RemielleMoonlightWhispers Wings IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7bc98032': [
            (log,                             ('3.1: RemielleMoonlightWhispers Wings Draw VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
        ],
        'f71d4482': [
            (log,                             ('3.1: RemielleMoonlightWhispers Wings Position VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
        ],
        '9d9b4d62': [
            (log,                             ('3.1: RemielleMoonlightWhispers Wings Texcoord VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
        ],
        '7b12084f': [
            (log,                             ('3.1: RemielleMoonlightWhispers Wings Blend VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
        ],
        '677ec0d0': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8574ee2', 'RemielleMoonlightWhispers.WingsA.Diffuse.1024')),
        ],
        'b8574ee2': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('677ec0d0', 'RemielleMoonlightWhispers.WingsA.Diffuse.2048')),
        ],
        # Wings shares its NormalMap hashes with Hair; see that Component above.
        '04497af6': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('128e607f', 'RemielleMoonlightWhispers.WingsA.LightMap.1024')),
        ],
        '128e607f': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('04497af6', 'RemielleMoonlightWhispers.WingsA.LightMap.2048')),
        ],
        '0ec88318': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c23e467e', 'RemielleMoonlightWhispers.WingsA.MaterialMap.1024')),
        ],
        'c23e467e': [
            (log,                             ('3.1: RemielleMoonlightWhispers WingsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleMoonlightWhispers.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0ec88318', 'RemielleMoonlightWhispers.WingsA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'fcbae9a5': [
            (log,                             ('3.1: RemielleMoonlightWhispers Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'baf9e1be': [
            (log,                             ('3.1: RemielleMoonlightWhispers EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'RemielleMoonlightWhispers.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'RemielleMoonlightWhispers.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'RemielleMoonlightWhispers.FaceA.Diffuse.1024')),
        ],
        '5bc2bbdd': [
            (log,                             ('3.1: RemielleMoonlightWhispers EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'RemielleMoonlightWhispers.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('baf9e1be', 'RemielleMoonlightWhispers.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('baf9e1be', 'RemielleMoonlightWhispers.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '7fbbcf0d': [
            (log,                             ('3.1: RemielleMoonlightWhispers Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0faf109a': [
            (log,                             ('3.1: RemielleMoonlightWhispers Face Draw VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
        ],
        '35bd83dd': [
            (log,                             ('3.1: RemielleMoonlightWhispers Face Position VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
        ],
        '7e8be536': [
            (log,                             ('3.1: RemielleMoonlightWhispers Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
        ],
        '3ba8ce1b': [
            (log,                             ('3.1: RemielleMoonlightWhispers Face Blend VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleMoonlightWhispers.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'RemielleMoonlightWhispers',
    'game_versions': ['3.1', '3.2'],
}
