"""
RemielleSeashadePasSeul Character Hash Commands
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
    Returns RemielleSeashadePasSeul's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '789ae812': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fbe70114': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair Draw VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
        ],
        '62b7da5e': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair Position VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
        ],
        'fa8ab367': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
        ],
        '46eee329': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair Blend VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
        ],
        '578239d7': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a619774', 'RemielleSeashadePasSeul.HairA.Diffuse.1024')),
        ],
        '8a619774': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('578239d7', 'RemielleSeashadePasSeul.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA, BodyA, LegA and WingsA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleSeashadePasSeul.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleSeashadePasSeul.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleSeashadePasSeul.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'RemielleSeashadePasSeul.WingsA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA, BodyA, LegA and WingsA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleSeashadePasSeul.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleSeashadePasSeul.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleSeashadePasSeul.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'RemielleSeashadePasSeul.WingsA.NormalMap.2048')),
        ],
        '6f826e7d': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45bb8a18', 'RemielleSeashadePasSeul.HairA.LightMap.1024')),
        ],
        '45bb8a18': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f826e7d', 'RemielleSeashadePasSeul.HairA.LightMap.2048')),
        ],
        'b5a12580': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b8df55e', 'RemielleSeashadePasSeul.HairA.MaterialMap.1024')),
        ],
        '8b8df55e': [
            (log,                             ('3.1: RemielleSeashadePasSeul HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'RemielleSeashadePasSeul.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5a12580', 'RemielleSeashadePasSeul.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3a0100ab': [
            (log,                             ('3.1: RemielleSeashadePasSeul Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        '241deac5': [
            (log,                             ('3.1: RemielleSeashadePasSeul Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('2cd6516a',)),
        ],
        '2cd6516a': [
            (log,                             ('3.2: RemielleSeashadePasSeul Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '48288582': [
            (log,                             ('3.1: RemielleSeashadePasSeul Body Draw VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('df41c403',)),
        ],
        'df41c403': [
            (log,                             ('3.2: RemielleSeashadePasSeul Body Draw VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
        ],
        '13c77c3a': [
            (log,                             ('3.1: RemielleSeashadePasSeul Body Position VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('22d04ad5',)),
        ],
        '22d04ad5': [
            (log,                             ('3.2: RemielleSeashadePasSeul Body Position VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
        ],
        'c55c57ce': [
            (log,                             ('3.1: RemielleSeashadePasSeul Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d637a74d',)),
        ],
        'd637a74d': [
            (log,                             ('3.2: RemielleSeashadePasSeul Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
        ],
        '9bca83d8': [
            (log,                             ('3.1: RemielleSeashadePasSeul Body Blend VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('5ec5e567',)),
        ],
        '5ec5e567': [
            (log,                             ('3.2: RemielleSeashadePasSeul Body Blend VB Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
        ],
        '686a0805': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb0f2f5d', 'RemielleSeashadePasSeul.BodyA.Diffuse.1024')),
        ],
        'fb0f2f5d': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('686a0805', 'RemielleSeashadePasSeul.BodyA.Diffuse.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        'a255803d': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c4d1c25b', 'RemielleSeashadePasSeul.BodyA.LightMap.1024')),
        ],
        'c4d1c25b': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a255803d', 'RemielleSeashadePasSeul.BodyA.LightMap.2048')),
        ],
        'fb91abe9': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d52ee692', 'RemielleSeashadePasSeul.BodyA.MaterialMap.1024')),
        ],
        'd52ee692': [
            (log,                             ('3.1: RemielleSeashadePasSeul BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('241deac5', 'RemielleSeashadePasSeul.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb91abe9', 'RemielleSeashadePasSeul.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        'b1870eee': [
            (log,                             ('3.1: RemielleSeashadePasSeul Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '041193d7': [
            (log,                             ('3.1: RemielleSeashadePasSeul Leg Draw VB Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
        ],
        '8ef10584': [
            (log,                             ('3.1: RemielleSeashadePasSeul Leg Position VB Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
        ],
        'b31b61d1': [
            (log,                             ('3.1: RemielleSeashadePasSeul Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
        ],
        'cf15b1ce': [
            (log,                             ('3.1: RemielleSeashadePasSeul Leg Blend VB Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
        ],
        '517d9d7c': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fb64395', 'RemielleSeashadePasSeul.LegA.Diffuse.1024')),
        ],
        '1fb64395': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('517d9d7c', 'RemielleSeashadePasSeul.LegA.Diffuse.2048')),
        ],
        # Leg shares its NormalMap hashes with Hair; see that Component above.
        '6a673bda': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('63ef7922', 'RemielleSeashadePasSeul.LegA.LightMap.1024')),
        ],
        '63ef7922': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6a673bda', 'RemielleSeashadePasSeul.LegA.LightMap.2048')),
        ],
        'f87f83d9': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac5220b6', 'RemielleSeashadePasSeul.LegA.MaterialMap.1024')),
        ],
        'ac5220b6': [
            (log,                             ('3.1: RemielleSeashadePasSeul LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b1870eee', 'RemielleSeashadePasSeul.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f87f83d9', 'RemielleSeashadePasSeul.LegA.MaterialMap.2048')),
        ],

        # ==================== Wings Component ====================
        '9004a39a': [
            (log,                             ('3.1: RemielleSeashadePasSeul Wings IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7bc98032': [
            (log,                             ('3.1: RemielleSeashadePasSeul Wings Draw VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
        ],
        'f71d4482': [
            (log,                             ('3.1: RemielleSeashadePasSeul Wings Position VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
        ],
        '9d9b4d62': [
            (log,                             ('3.1: RemielleSeashadePasSeul Wings Texcoord VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
        ],
        '7b12084f': [
            (log,                             ('3.1: RemielleSeashadePasSeul Wings Blend VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
        ],
        '80ad86c3': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdc91dce', 'RemielleSeashadePasSeul.WingsA.Diffuse.1024')),
        ],
        'cdc91dce': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('80ad86c3', 'RemielleSeashadePasSeul.WingsA.Diffuse.2048')),
        ],
        # Wings shares its NormalMap hashes with Hair; see that Component above.
        '04497af6': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('128e607f', 'RemielleSeashadePasSeul.WingsA.LightMap.1024')),
        ],
        '128e607f': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('04497af6', 'RemielleSeashadePasSeul.WingsA.LightMap.2048')),
        ],
        '0ec88318': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c23e467e', 'RemielleSeashadePasSeul.WingsA.MaterialMap.1024')),
        ],
        'c23e467e': [
            (log,                             ('3.1: RemielleSeashadePasSeul WingsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'RemielleSeashadePasSeul.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0ec88318', 'RemielleSeashadePasSeul.WingsA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'fcbae9a5': [
            (log,                             ('3.1: RemielleSeashadePasSeul Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'baf9e1be': [
            (log,                             ('3.1: RemielleSeashadePasSeul EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'RemielleSeashadePasSeul.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'RemielleSeashadePasSeul.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'RemielleSeashadePasSeul.FaceA.Diffuse.1024')),
        ],
        '5bc2bbdd': [
            (log,                             ('3.1: RemielleSeashadePasSeul EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'RemielleSeashadePasSeul.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('baf9e1be', 'RemielleSeashadePasSeul.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('baf9e1be', 'RemielleSeashadePasSeul.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '7fbbcf0d': [
            (log,                             ('3.1: RemielleSeashadePasSeul Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0faf109a': [
            (log,                             ('3.1: RemielleSeashadePasSeul Face Draw VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
        ],
        '35bd83dd': [
            (log,                             ('3.1: RemielleSeashadePasSeul Face Position VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
        ],
        '7e8be536': [
            (log,                             ('3.1: RemielleSeashadePasSeul Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
        ],
        '3ba8ce1b': [
            (log,                             ('3.1: RemielleSeashadePasSeul Face Blend VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'RemielleSeashadePasSeul.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'RemielleSeashadePasSeul',
    'game_versions': ['3.1', '3.2'],
}
