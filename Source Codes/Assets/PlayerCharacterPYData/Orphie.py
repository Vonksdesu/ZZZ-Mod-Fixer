"""
Orphie Character Hash Commands
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
    Returns Orphie's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '6988bfcd': [
            (log,                             ('2.2 - 3.2: Orphie Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f1dfc45': [
            (log,                             ('2.2 - 3.2: Orphie Hair Draw VB Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        ],
        '83c4fcaf': [
            (log,                             ('2.2 - 3.2: Orphie Hair Position VB Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        ],
        'c721249c': [
            (log,                             ('2.2 - 3.2: Orphie Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        ],
        'bb2a1769': [
            (log,                             ('2.2 - 3.2: Orphie Hair Blend VB Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
        ],
        'ce52779f': [
            (log,                             ('2.2 - 3.2: Orphie HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('78d4038b', 'Orphie.HairA.Diffuse.1024')),
        ],
        '78d4038b': [
            (log,                             ('2.2 - 3.2: Orphie HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ce52779f', 'Orphie.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Orphie HairA, BodyA, LegA, daggerA, Magus·tailA, Magus·headA and Magus·mouthA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.daggerA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.Magus·tailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.Magus·headA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Orphie.Magus·mouthA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Orphie HairA, BodyA, LegA, daggerA, Magus·tailA, Magus·headA and Magus·mouthA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.daggerA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.Magus·tailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.Magus·headA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Orphie.Magus·mouthA.NormalMap.2048')),
        ],
        '77abe83b': [
            (log,                             ('2.2 - 3.2: Orphie HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('643268b4', 'Orphie.HairA.LightMap.1024')),
        ],
        '643268b4': [
            (log,                             ('2.2 - 3.2: Orphie HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('77abe83b', 'Orphie.HairA.LightMap.2048')),
        ],
        '94ed2491': [
            (log,                             ('2.2 - 3.2: Orphie HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ef6e3a3b', 'Orphie.HairA.MaterialMap.1024')),
        ],
        'ef6e3a3b': [
            (log,                             ('2.2 - 3.2: Orphie HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6988bfcd', 'Orphie.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('94ed2491', 'Orphie.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'd98415dc': [
            (log,                             ('2.2 - 3.2: Orphie Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '79702a46': [
            (log,                             ('2.2 - 3.2: Orphie Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd635bad0': [
            (log,                             ('2.2 - 3.2: Orphie Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd8779413': [
            (log,                             ('2.2 - 3.2: Orphie Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '48a78cdc': [
            (log,                             ('2.2 - 3.2: Orphie Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('d98415dc', 'Orphie.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'a5eac582': [
            (log,                             ('2.2 - 3.2: Orphie Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd4b12374': [
            (log,                             ('2.2 - 3.2: Orphie Body Draw VB Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        ],
        'e0269fbf': [
            (log,                             ('2.2 - 3.2: Orphie Body Position VB Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        ],
        'd31ae32f': [
            (log,                             ('2.2 - 3.2: Orphie Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        ],
        'b823fb44': [
            (log,                             ('2.2 - 3.2: Orphie Body Blend VB Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
        ],
        'c9bea5d7': [
            (log,                             ('2.2 - 3.2: Orphie BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca89cd72', 'Orphie.BodyA.Diffuse.1024')),
        ],
        'ca89cd72': [
            (log,                             ('2.2 - 3.2: Orphie BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c9bea5d7', 'Orphie.BodyA.Diffuse.2048')),
        ],
        '9a0406fe': [
            (log,                             ('2.2 - 3.2: Orphie BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c797a191', 'Orphie.BodyA.LightMap.1024')),
        ],
        'c797a191': [
            (log,                             ('2.2 - 3.2: Orphie BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9a0406fe', 'Orphie.BodyA.LightMap.2048')),
        ],
        '1daf926d': [
            (log,                             ('2.2 - 3.2: Orphie BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f6aa298', 'Orphie.BodyA.MaterialMap.1024')),
        ],
        '7f6aa298': [
            (log,                             ('2.2 - 3.2: Orphie BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a5eac582', 'Orphie.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1daf926d', 'Orphie.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Leg Component ====================
        '80017921': [
            (log,                             ('2.2 - 3.2: Orphie Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f7b4360a': [
            (log,                             ('2.2 - 3.2: Orphie Leg Draw VB Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
        ],
        'b4e15dc4': [
            (log,                             ('2.2 - 3.2: Orphie Leg Position VB Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
        ],
        'f74b4cea': [
            (log,                             ('2.2 - 3.2: Orphie Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
        ],
        '5ca9ed4e': [
            (log,                             ('2.2 - 3.2: Orphie Leg Blend VB Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
        ],
        'dd4120db': [
            (log,                             ('2.2 - 3.2: Orphie LegA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aaeb5f0f', 'Orphie.LegA.Diffuse.1024')),
        ],
        'aaeb5f0f': [
            (log,                             ('2.2 - 3.2: Orphie LegA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd4120db', 'Orphie.LegA.Diffuse.2048')),
        ],
        'a9ae84df': [
            (log,                             ('2.2 - 3.2: Orphie LegA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ec3855fa', 'Orphie.LegA.LightMap.1024')),
        ],
        'ec3855fa': [
            (log,                             ('2.2 - 3.2: Orphie LegA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9ae84df', 'Orphie.LegA.LightMap.2048')),
        ],
        '867ceb5b': [
            (log,                             ('2.2 - 3.2: Orphie LegA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('70ff1eca', 'Orphie.LegA.MaterialMap.1024')),
        ],
        '70ff1eca': [
            (log,                             ('2.2 - 3.2: Orphie LegA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('80017921', 'Orphie.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('867ceb5b', 'Orphie.LegA.MaterialMap.2048')),
        ],
        # Leg shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        'ed85f33b': [
            (log,                             ('2.2 - 3.2: Orphie Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1542fac0': [
            (log,                             ('2.2 - 3.2: Orphie Face Draw VB Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
        ],
        '2f506987': [
            (log,                             ('2.2 - 3.2: Orphie Face Position VB Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
        ],
        '48191f72': [
            (log,                             ('2.2 - 3.1: Orphie Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('615a1f62',)),
        ],
        '615a1f62': [
            (log,                             ('3.2: Orphie Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3cde4ca0': [
            (log,                             ('2.2 - 3.2: Orphie Face Blend VB Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
        ],
        '0df52ae7': [
            (log,                             ('2.2 - 3.2: Orphie FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('66efca96', 'Orphie.FaceA.Diffuse.1024')),
        ],
        '66efca96': [
            (log,                             ('2.2 - 3.2: Orphie FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ed85f33b', 'Orphie.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0df52ae7', 'Orphie.FaceA.Diffuse.2048')),
        ],
        # Face shares its NormalMap hashes with Hair; see that Component above.

        # ==================== dagger Component ====================
        'aa1404dd': [
            (log,                             ('2.2 - 3.2: Orphie dagger IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6c9a0fb8': [
            (log,                             ('2.2 - 3.2: Orphie dagger Draw VB Hash',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
        ],
        '586b83df': [
            (log,                             ('2.2 - 3.2: Orphie dagger Position VB Hash',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
        ],
        '6b263148': [
            (log,                             ('2.2 - 3.2: Orphie dagger Texcoord VB Hash',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
        ],
        '7c7fd13b': [
            (log,                             ('2.2 - 3.2: Orphie dagger Blend VB Hash',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
        ],
        'dd80fa1d': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c64aea70', 'Orphie.daggerA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c64aea70', 'Orphie.Magus·tailA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c64aea70', 'Orphie.Magus·headA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c64aea70', 'Orphie.Magus·mouthA.Diffuse.1024')),
        ],
        'c64aea70': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd80fa1d', 'Orphie.daggerA.Diffuse.2048')),
            (multiply_section_if_missing,     ('dd80fa1d', 'Orphie.Magus·tailA.Diffuse.2048')),
            (multiply_section_if_missing,     ('dd80fa1d', 'Orphie.Magus·headA.Diffuse.2048')),
            (multiply_section_if_missing,     ('dd80fa1d', 'Orphie.Magus·mouthA.Diffuse.2048')),
        ],
        '92c6b20b': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('772b915b', 'Orphie.daggerA.LightMap.1024')),
            (multiply_section_if_missing,     ('772b915b', 'Orphie.Magus·tailA.LightMap.1024')),
            (multiply_section_if_missing,     ('772b915b', 'Orphie.Magus·headA.LightMap.1024')),
            (multiply_section_if_missing,     ('772b915b', 'Orphie.Magus·mouthA.LightMap.1024')),
        ],
        '772b915b': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('92c6b20b', 'Orphie.daggerA.LightMap.2048')),
            (multiply_section_if_missing,     ('92c6b20b', 'Orphie.Magus·tailA.LightMap.2048')),
            (multiply_section_if_missing,     ('92c6b20b', 'Orphie.Magus·headA.LightMap.2048')),
            (multiply_section_if_missing,     ('92c6b20b', 'Orphie.Magus·mouthA.LightMap.2048')),
        ],
        'cb65982e': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c1650e3b', 'Orphie.daggerA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c1650e3b', 'Orphie.Magus·tailA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c1650e3b', 'Orphie.Magus·headA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c1650e3b', 'Orphie.Magus·mouthA.MaterialMap.1024')),
        ],
        'c1650e3b': [
            (log,                             ('2.2 - 3.2: Orphie daggerA, Magus·tailA, Magus·headA and Magus·mouthA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('aa1404dd', 'Orphie.dagger.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cb65982e', 'Orphie.daggerA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('cb65982e', 'Orphie.Magus·tailA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('cb65982e', 'Orphie.Magus·headA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('cb65982e', 'Orphie.Magus·mouthA.MaterialMap.2048')),
        ],

        # ==================== Magus·tail Component ====================
        '3766fa59': [
            (log,                             ('2.2 - 3.2: Orphie Magus·tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fea2bd55': [
            (log,                             ('2.2 - 3.2: Orphie Magus·tail Draw VB Hash',)),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
        ],
        'f4a39978': [
            (log,                             ('2.2 - 3.2: Orphie Magus·tail Position VB Hash',)),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
        ],
        'f33946ec': [
            (log,                             ('2.2 - 3.2: Orphie Magus·tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
        ],
        '203664d5': [
            (log,                             ('2.2 - 3.2: Orphie Magus·tail Blend VB Hash',)),
            (add_section_if_missing,          ('3766fa59', 'Orphie.Magus·tail.IB', 'match_priority = 0\n')),
        ],
        # Magus·tail shares its NormalMap with Hair and its Diffuse, LightMap and MaterialMap with dagger; see those Components above.

        # ==================== Magus·head Component ====================
        '2935f885': [
            (log,                             ('2.2 - 3.2: Orphie Magus·head IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '49393f27': [
            (log,                             ('2.2 - 3.2: Orphie Magus·head Draw VB Hash',)),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
        ],
        '160ccb43': [
            (log,                             ('2.2 - 3.2: Orphie Magus·head Position VB Hash',)),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
        ],
        '43b63f81': [
            (log,                             ('2.2 - 3.2: Orphie Magus·head Texcoord VB Hash',)),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
        ],
        '17077e99': [
            (log,                             ('2.2 - 3.2: Orphie Magus·head Blend VB Hash',)),
            (add_section_if_missing,          ('2935f885', 'Orphie.Magus·head.IB', 'match_priority = 0\n')),
        ],
        # Magus·head shares its NormalMap with Hair and its Diffuse, LightMap and MaterialMap with dagger; see those Components above.

        # ==================== Magus·mouth Component ====================
        '389256d8': [
            (log,                             ('2.2 - 3.2: Orphie Magus·mouth IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '27b14e70': [
            (log,                             ('2.2 - 3.2: Orphie Magus·mouth Draw VB Hash',)),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
        ],
        'aeeebb95': [
            (log,                             ('2.2 - 3.2: Orphie Magus·mouth Position VB Hash',)),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
        ],
        '5662dd65': [
            (log,                             ('2.2 - 3.2: Orphie Magus·mouth Texcoord VB Hash',)),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
        ],
        '6fba1f7b': [
            (log,                             ('2.2 - 3.2: Orphie Magus·mouth Blend VB Hash',)),
            (add_section_if_missing,          ('389256d8', 'Orphie.Magus·mouth.IB', 'match_priority = 0\n')),
        ],
        # Magus·mouth shares its NormalMap with Hair and its Diffuse, LightMap and MaterialMap with dagger; see those Components above.

        # ==================== Magus·eye Component ====================
        'e63d22c3': [
            (log,                             ('2.2 - 3.2: Orphie Magus·eye IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Magus·eye has only its IB hash in any database version (no VB and no textures).
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Orphie',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
