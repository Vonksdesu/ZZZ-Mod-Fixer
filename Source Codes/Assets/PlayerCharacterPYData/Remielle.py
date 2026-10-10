"""
Remielle Character Hash Commands
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
    Returns Remielle's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '789ae812': [
            (log,                             ('3.1: Remielle Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fbe70114': [
            (log,                             ('3.1: Remielle Hair Draw VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
        ],
        '62b7da5e': [
            (log,                             ('3.1: Remielle Hair Position VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
        ],
        'fa8ab367': [
            (log,                             ('3.1: Remielle Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
        ],
        '46eee329': [
            (log,                             ('3.1: Remielle Hair Blend VB Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
        ],
        '578239d7': [
            (log,                             ('3.1: Remielle HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8a619774', 'Remielle.HairA.Diffuse.1024')),
        ],
        '8a619774': [
            (log,                             ('3.1: Remielle HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('578239d7', 'Remielle.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: Remielle HairA, BodyA, LegA, WingsA, SwordA, Hilt1A, Hilt2A, AircraftA, InjectorA and Injector2A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.WingsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.SwordA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.Hilt1A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.Hilt2A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.AircraftA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.InjectorA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Remielle.Injector2A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: Remielle HairA, BodyA, LegA, WingsA, SwordA, Hilt1A, Hilt2A, AircraftA, InjectorA and Injector2A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.WingsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.SwordA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.Hilt1A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.Hilt2A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.AircraftA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.InjectorA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Remielle.Injector2A.NormalMap.2048')),
        ],
        '6f826e7d': [
            (log,                             ('3.1: Remielle HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('45bb8a18', 'Remielle.HairA.LightMap.1024')),
        ],
        '45bb8a18': [
            (log,                             ('3.1: Remielle HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f826e7d', 'Remielle.HairA.LightMap.2048')),
        ],
        'b5a12580': [
            (log,                             ('3.1: Remielle HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8b8df55e', 'Remielle.HairA.MaterialMap.1024')),
        ],
        '8b8df55e': [
            (log,                             ('3.1: Remielle HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('789ae812', 'Remielle.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5a12580', 'Remielle.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3a0100ab': [
            (log,                             ('3.1: Remielle Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        '785b21f5': [
            (log,                             ('3.1: Remielle Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('28e05a59',)),
        ],
        '28e05a59': [
            (log,                             ('3.2: Remielle Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7a92a10a': [
            (log,                             ('3.1: Remielle Body Draw VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('97664f2f',)),
        ],
        '97664f2f': [
            (log,                             ('3.2: Remielle Body Draw VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
        ],
        '679a1bd8': [
            (log,                             ('3.1: Remielle Body Position VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d16f6790',)),
        ],
        'd16f6790': [
            (log,                             ('3.2: Remielle Body Position VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
        ],
        '9e33a8b6': [
            (log,                             ('3.1: Remielle Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b943ec9e',)),
        ],
        'b943ec9e': [
            (log,                             ('3.2: Remielle Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
        ],
        '9e8a27ae': [
            (log,                             ('3.1: Remielle Body Blend VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('da54a57a',)),
        ],
        'da54a57a': [
            (log,                             ('3.2: Remielle Body Blend VB Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
        ],
        'e51be5d1': [
            (log,                             ('3.1: Remielle BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d770d330', 'Remielle.BodyA.Diffuse.1024')),
        ],
        'd770d330': [
            (log,                             ('3.1: Remielle BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e51be5d1', 'Remielle.BodyA.Diffuse.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        '380d7bcf': [
            (log,                             ('3.1: Remielle BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b95031e2', 'Remielle.BodyA.LightMap.1024')),
        ],
        'b95031e2': [
            (log,                             ('3.1: Remielle BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('380d7bcf', 'Remielle.BodyA.LightMap.2048')),
        ],
        '61c42d63': [
            (log,                             ('3.1: Remielle BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed6ca67a', 'Remielle.BodyA.MaterialMap.1024')),
        ],
        'ed6ca67a': [
            (log,                             ('3.1: Remielle BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('785b21f5', 'Remielle.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('61c42d63', 'Remielle.BodyA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        'fe9fc31a': [
            (log,                             ('3.1: Remielle Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3bf3b3b0': [
            (log,                             ('3.1: Remielle Leg Draw VB Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
        ],
        '1bc49355': [
            (log,                             ('3.1: Remielle Leg Position VB Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
        ],
        'ed8feacb': [
            (log,                             ('3.1: Remielle Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
        ],
        '2702db6d': [
            (log,                             ('3.1: Remielle Leg Blend VB Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
        ],
        '6538d30d': [
            (log,                             ('3.1: Remielle LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('49ac9d9e', 'Remielle.LegA.Diffuse.1024')),
        ],
        '49ac9d9e': [
            (log,                             ('3.1: Remielle LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6538d30d', 'Remielle.LegA.Diffuse.2048')),
        ],
        # Leg shares its NormalMap hashes with Hair; see that Component above.
        '4049331b': [
            (log,                             ('3.1: Remielle LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95db220c', 'Remielle.LegA.LightMap.1024')),
        ],
        '95db220c': [
            (log,                             ('3.1: Remielle LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4049331b', 'Remielle.LegA.LightMap.2048')),
        ],
        'cdc2accb': [
            (log,                             ('3.1: Remielle LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1c782fe7', 'Remielle.LegA.MaterialMap.1024')),
        ],
        '1c782fe7': [
            (log,                             ('3.1: Remielle LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('fe9fc31a', 'Remielle.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdc2accb', 'Remielle.LegA.MaterialMap.2048')),
        ],

        # ==================== Wings Component ====================
        '9004a39a': [
            (log,                             ('3.1: Remielle Wings IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7bc98032': [
            (log,                             ('3.1: Remielle Wings Draw VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
        ],
        'f71d4482': [
            (log,                             ('3.1: Remielle Wings Position VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
        ],
        '9d9b4d62': [
            (log,                             ('3.1: Remielle Wings Texcoord VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
        ],
        '7b12084f': [
            (log,                             ('3.1: Remielle Wings Blend VB Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
        ],
        '80ad86c3': [
            (log,                             ('3.1: Remielle WingsA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cdc91dce', 'Remielle.WingsA.Diffuse.1024')),
        ],
        'cdc91dce': [
            (log,                             ('3.1: Remielle WingsA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('80ad86c3', 'Remielle.WingsA.Diffuse.2048')),
        ],
        # Wings shares its NormalMap hashes with Hair; see that Component above.
        '04497af6': [
            (log,                             ('3.1: Remielle WingsA and AircraftTextureA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('128e607f', 'Remielle.WingsA.LightMap.1024')),
            (multiply_section_if_missing,     ('128e607f', 'Remielle.AircraftTextureA.LightMap.1024')),
        ],
        '128e607f': [
            (log,                             ('3.1: Remielle WingsA and AircraftTextureA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('04497af6', 'Remielle.WingsA.LightMap.2048')),
            (multiply_section_if_missing,     ('04497af6', 'Remielle.AircraftTextureA.LightMap.2048')),
        ],
        '0ec88318': [
            (log,                             ('3.1: Remielle WingsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c23e467e', 'Remielle.WingsA.MaterialMap.1024')),
        ],
        'c23e467e': [
            (log,                             ('3.1: Remielle WingsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('9004a39a', 'Remielle.Wings.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0ec88318', 'Remielle.WingsA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        'fcbae9a5': [
            (log,                             ('3.1: Remielle Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'baf9e1be': [
            (log,                             ('3.1: Remielle EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'Remielle.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'Remielle.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('5bc2bbdd', 'Remielle.FaceA.Diffuse.1024')),
        ],
        '5bc2bbdd': [
            (log,                             ('3.1: Remielle EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fcbae9a5', 'Remielle.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('baf9e1be', 'Remielle.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('baf9e1be', 'Remielle.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '7fbbcf0d': [
            (log,                             ('3.1: Remielle Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0faf109a': [
            (log,                             ('3.1: Remielle Face Draw VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
        ],
        '35bd83dd': [
            (log,                             ('3.1: Remielle Face Position VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
        ],
        '7e8be536': [
            (log,                             ('3.1: Remielle Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
        ],
        '3ba8ce1b': [
            (log,                             ('3.1: Remielle Face Blend VB Hash',)),
            (add_section_if_missing,          ('7fbbcf0d', 'Remielle.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.

        # ==================== Sword Component ====================
        'e0b4b061': [
            (log,                             ('3.1: Remielle Sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd13c771a': [
            (log,                             ('3.1: Remielle Sword Draw VB Hash',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
        ],
        'bebcecd1': [
            (log,                             ('3.1: Remielle Sword Position VB Hash',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
        ],
        '04360ff9': [
            (log,                             ('3.1: Remielle Sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
        ],
        'df30a4a2': [
            (log,                             ('3.1: Remielle Sword Blend VB Hash',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
        ],
        '85b91845': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77d73d18', 'Remielle.SwordA.Diffuse.1024')),
            (multiply_section_if_missing,     ('77d73d18', 'Remielle.Hilt1A.Diffuse.1024')),
            (multiply_section_if_missing,     ('77d73d18', 'Remielle.Hilt2A.Diffuse.1024')),
        ],
        '77d73d18': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('85b91845', 'Remielle.SwordA.Diffuse.2048')),
            (multiply_section_if_missing,     ('85b91845', 'Remielle.Hilt1A.Diffuse.2048')),
            (multiply_section_if_missing,     ('85b91845', 'Remielle.Hilt2A.Diffuse.2048')),
        ],
        # Sword shares its NormalMap hashes with Hair; see that Component above.
        'e06fd26b': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2931c061', 'Remielle.SwordA.LightMap.1024')),
            (multiply_section_if_missing,     ('2931c061', 'Remielle.Hilt1A.LightMap.1024')),
            (multiply_section_if_missing,     ('2931c061', 'Remielle.Hilt2A.LightMap.1024')),
        ],
        '2931c061': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e06fd26b', 'Remielle.SwordA.LightMap.2048')),
            (multiply_section_if_missing,     ('e06fd26b', 'Remielle.Hilt1A.LightMap.2048')),
            (multiply_section_if_missing,     ('e06fd26b', 'Remielle.Hilt2A.LightMap.2048')),
        ],
        '9455f7a5': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4844d251', 'Remielle.SwordA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('4844d251', 'Remielle.Hilt1A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('4844d251', 'Remielle.Hilt2A.MaterialMap.1024')),
        ],
        '4844d251': [
            (log,                             ('3.1: Remielle SwordA, Hilt1A and Hilt2A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e0b4b061', 'Remielle.Sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9455f7a5', 'Remielle.SwordA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9455f7a5', 'Remielle.Hilt1A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9455f7a5', 'Remielle.Hilt2A.MaterialMap.2048')),
        ],

        # ==================== Hilt1 Component ====================
        '1b655510': [
            (log,                             ('3.1: Remielle Hilt1 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cb55081c': [
            (log,                             ('3.1: Remielle Hilt1 Draw VB Hash',)),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
        ],
        '3c5ffb4a': [
            (log,                             ('3.1: Remielle Hilt1 Position VB Hash',)),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
        ],
        '92f10a81': [
            (log,                             ('3.1: Remielle Hilt1 Texcoord VB Hash',)),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
        ],
        'b82da0bb': [
            (log,                             ('3.1: Remielle Hilt1 Blend VB Hash',)),
            (add_section_if_missing,          ('1b655510', 'Remielle.Hilt1.IB', 'match_priority = 0\n')),
        ],
        # Hilt1 shares its Diffuse, LightMap and MaterialMap hashes with Sword, and its NormalMap
        # hashes are shared with Hair; see those Components above.

        # ==================== Hilt2 Component ====================
        '14cf141e': [
            (log,                             ('3.1: Remielle Hilt2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd482d732': [
            (log,                             ('3.1: Remielle Hilt2 Draw VB Hash',)),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
        ],
        '95a2457a': [
            (log,                             ('3.1: Remielle Hilt2 Position VB Hash',)),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
        ],
        '96452d20': [
            (log,                             ('3.1: Remielle Hilt2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
        ],
        '44d4a8ad': [
            (log,                             ('3.1: Remielle Hilt2 Blend VB Hash',)),
            (add_section_if_missing,          ('14cf141e', 'Remielle.Hilt2.IB', 'match_priority = 0\n')),
        ],
        # Hilt2 shares its Diffuse, LightMap and MaterialMap hashes with Sword, and its NormalMap
        # hashes are shared with Hair; see those Components above.

        # ==================== Aircraft Component ====================
        'ca717c18': [
            (log,                             ('3.1: Remielle Aircraft IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dd402a5c': [
            (log,                             ('3.1: Remielle Aircraft Draw VB Hash',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
        ],
        '9615df83': [
            (log,                             ('3.1: Remielle Aircraft Position VB Hash',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
        ],
        'dd3180e4': [
            (log,                             ('3.1: Remielle Aircraft Texcoord VB Hash',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
        ],
        '945317d9': [
            (log,                             ('3.1: Remielle Aircraft Blend VB Hash',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
        ],
        '420e2418': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d930a5fa', 'Remielle.AircraftA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d930a5fa', 'Remielle.InjectorA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d930a5fa', 'Remielle.Injector2A.Diffuse.1024')),
        ],
        'd930a5fa': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('420e2418', 'Remielle.AircraftA.Diffuse.2048')),
            (multiply_section_if_missing,     ('420e2418', 'Remielle.InjectorA.Diffuse.2048')),
            (multiply_section_if_missing,     ('420e2418', 'Remielle.Injector2A.Diffuse.2048')),
        ],
        # Aircraft shares its NormalMap hashes with Hair; see that Component above.
        '5fda974c': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f940f25', 'Remielle.AircraftA.LightMap.1024')),
            (multiply_section_if_missing,     ('9f940f25', 'Remielle.InjectorA.LightMap.1024')),
            (multiply_section_if_missing,     ('9f940f25', 'Remielle.Injector2A.LightMap.1024')),
        ],
        '9f940f25': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5fda974c', 'Remielle.AircraftA.LightMap.2048')),
            (multiply_section_if_missing,     ('5fda974c', 'Remielle.InjectorA.LightMap.2048')),
            (multiply_section_if_missing,     ('5fda974c', 'Remielle.Injector2A.LightMap.2048')),
        ],
        '4948fe09': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f01b9d5c', 'Remielle.AircraftA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('f01b9d5c', 'Remielle.InjectorA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('f01b9d5c', 'Remielle.Injector2A.MaterialMap.1024')),
        ],
        'f01b9d5c': [
            (log,                             ('3.1: Remielle AircraftA, InjectorA and Injector2A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca717c18', 'Remielle.Aircraft.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('acfa670a', 'Remielle.Injector.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('760c8064', 'Remielle.Injector2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4948fe09', 'Remielle.AircraftA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4948fe09', 'Remielle.InjectorA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4948fe09', 'Remielle.Injector2A.MaterialMap.2048')),
        ],

        # ==================== AircraftTexture Component ====================
        '6ef3d666': [
            (log,                             ('3.1: Remielle AircraftTexture IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3b13c5c5': [
            (log,                             ('3.1: Remielle AircraftTexture Draw VB Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
        ],
        'f39a7cec': [
            (log,                             ('3.1: Remielle AircraftTexture Position VB Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
        ],
        '3b2b251d': [
            (log,                             ('3.1: Remielle AircraftTexture Texcoord VB Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
        ],
        '4fa9be65': [
            (log,                             ('3.1: Remielle AircraftTexture Blend VB Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
        ],
        'cd400938': [
            (log,                             ('3.1: Remielle AircraftTextureA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('037e650c', 'Remielle.AircraftTextureA.Diffuse.1024')),
        ],
        '037e650c': [
            (log,                             ('3.1: Remielle AircraftTextureA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cd400938', 'Remielle.AircraftTextureA.Diffuse.2048')),
        ],
        'b8f3b02a': [
            (log,                             ('3.1: Remielle AircraftTextureA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1864c72', 'Remielle.AircraftTextureA.NormalMap.1024')),
        ],
        'e1864c72': [
            (log,                             ('3.1: Remielle AircraftTextureA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8f3b02a', 'Remielle.AircraftTextureA.NormalMap.2048')),
        ],
        'dd0a0bd1': [
            (log,                             ('3.1: Remielle AircraftTextureA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23186e62', 'Remielle.AircraftTextureA.MaterialMap.1024')),
        ],
        '23186e62': [
            (log,                             ('3.1: Remielle AircraftTextureA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6ef3d666', 'Remielle.AircraftTexture.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd0a0bd1', 'Remielle.AircraftTextureA.MaterialMap.2048')),
        ],
        # AircraftTexture shares its LightMap hashes with Wings; see that Component above.

        # ==================== Injector Component ====================
        'acfa670a': [
            (log,                             ('3.1: Remielle Injector IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Injector shares its Diffuse, LightMap and MaterialMap hashes with Aircraft, and its NormalMap
        # hashes are shared with Hair; see those Components above.

        # ==================== Injector2 Component ====================
        '760c8064': [
            (log,                             ('3.1: Remielle Injector2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Injector2 shares its Diffuse, LightMap and MaterialMap hashes with Aircraft, and its NormalMap
        # hashes are shared with Hair; see those Components above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Remielle',
    'game_versions': ['3.1', '3.2'],
}
