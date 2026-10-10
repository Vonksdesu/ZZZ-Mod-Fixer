"""
LucyPrincessOnHoliday Character Hash Commands
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
    Returns LucyPrincessOnHoliday's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'ba402095': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c136d7d8': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair Draw VB Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
        ],
        '84dd6eaa': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair Position VB Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
        ],
        'bb60ba2a': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
        ],
        '0a0ef4ca': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair Blend VB Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
        ],
        '0fa60fe1': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('753baa45', 'LucyPrincessOnHoliday.HairA.Diffuse.1024')),
        ],
        '753baa45': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0fa60fe1', 'LucyPrincessOnHoliday.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA, HatA, BodyA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'LucyPrincessOnHoliday.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'LucyPrincessOnHoliday.HatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'LucyPrincessOnHoliday.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'LucyPrincessOnHoliday.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA, HatA, BodyA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'LucyPrincessOnHoliday.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'LucyPrincessOnHoliday.HatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'LucyPrincessOnHoliday.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'LucyPrincessOnHoliday.weapon.NormalMap.2048')),
        ],
        '1a3b30ba': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('810c0878', 'LucyPrincessOnHoliday.HairA.LightMap.1024')),
        ],
        '810c0878': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1a3b30ba', 'LucyPrincessOnHoliday.HairA.LightMap.2048')),
        ],
        '068aba7f': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('368f931c', 'LucyPrincessOnHoliday.HairA.MaterialMap.1024')),
        ],
        '368f931c': [
            (log,                             ('3.1: LucyPrincessOnHoliday HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ba402095', 'LucyPrincessOnHoliday.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('068aba7f', 'LucyPrincessOnHoliday.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'f7d74190': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # Hair Shadow has no vertex buffers or texture hashes in the database.

        # ==================== Hat Component ====================
        '7cec7c94': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'eae29c24': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hat Draw VB Hash',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
        ],
        '9ef15072': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hat Position VB Hash',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
        ],
        '7a606e17': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hat Texcoord VB Hash',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
        ],
        'c692080c': [
            (log,                             ('3.1: LucyPrincessOnHoliday Hat Blend VB Hash',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
        ],
        '2cac44c0': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('28a02ec1', '4901de52'), 'LucyPrincessOnHoliday.HatA.Diffuse.1024')),
            (multiply_section_if_missing,     (('28a02ec1', '4901de52'), 'LucyPrincessOnHoliday.BodyA.Diffuse.1024')),
            (update_hash,                     ('90b379de',)),
        ],
        '90b379de': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('28a02ec1', '4901de52'), 'LucyPrincessOnHoliday.HatA.Diffuse.1024')),
            (multiply_section_if_missing,     (('28a02ec1', '4901de52'), 'LucyPrincessOnHoliday.BodyA.Diffuse.1024')),
        ],
        '4901de52': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('90b379de', '2cac44c0'), 'LucyPrincessOnHoliday.HatA.Diffuse.2048')),
            (multiply_section_if_missing,     (('90b379de', '2cac44c0'), 'LucyPrincessOnHoliday.BodyA.Diffuse.2048')),
            (update_hash,                     ('28a02ec1',)),
        ],
        '28a02ec1': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('90b379de', '2cac44c0'), 'LucyPrincessOnHoliday.HatA.Diffuse.2048')),
            (multiply_section_if_missing,     (('90b379de', '2cac44c0'), 'LucyPrincessOnHoliday.BodyA.Diffuse.2048')),
        ],
        '8d155fc7': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d2ba0029', 'ca69aa34'), 'LucyPrincessOnHoliday.HatA.LightMap.1024')),
            (multiply_section_if_missing,     (('d2ba0029', 'ca69aa34'), 'LucyPrincessOnHoliday.BodyA.LightMap.1024')),
            (update_hash,                     ('f1d1a335',)),
        ],
        'f1d1a335': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d2ba0029', 'ca69aa34'), 'LucyPrincessOnHoliday.HatA.LightMap.1024')),
            (multiply_section_if_missing,     (('d2ba0029', 'ca69aa34'), 'LucyPrincessOnHoliday.BodyA.LightMap.1024')),
        ],
        'ca69aa34': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f1d1a335', '8d155fc7'), 'LucyPrincessOnHoliday.HatA.LightMap.2048')),
            (multiply_section_if_missing,     (('f1d1a335', '8d155fc7'), 'LucyPrincessOnHoliday.BodyA.LightMap.2048')),
            (update_hash,                     ('d2ba0029',)),
        ],
        'd2ba0029': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f1d1a335', '8d155fc7'), 'LucyPrincessOnHoliday.HatA.LightMap.2048')),
            (multiply_section_if_missing,     (('f1d1a335', '8d155fc7'), 'LucyPrincessOnHoliday.BodyA.LightMap.2048')),
        ],
        'e96ce933': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8ea3cc55', 'fdf85374'), 'LucyPrincessOnHoliday.HatA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('8ea3cc55', 'fdf85374'), 'LucyPrincessOnHoliday.BodyA.MaterialMap.1024')),
            (update_hash,                     ('dfd183e8',)),
        ],
        'dfd183e8': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('8ea3cc55', 'fdf85374'), 'LucyPrincessOnHoliday.HatA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('8ea3cc55', 'fdf85374'), 'LucyPrincessOnHoliday.BodyA.MaterialMap.1024')),
        ],
        'fdf85374': [
            (log,                             ('3.1: LucyPrincessOnHoliday HatA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('dfd183e8', 'e96ce933'), 'LucyPrincessOnHoliday.HatA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('dfd183e8', 'e96ce933'), 'LucyPrincessOnHoliday.BodyA.MaterialMap.2048')),
            (update_hash,                     ('8ea3cc55',)),
        ],
        '8ea3cc55': [
            (log,                             ('3.2: LucyPrincessOnHoliday HatA and BodyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('7cec7c94', 'LucyPrincessOnHoliday.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('dfd183e8', 'e96ce933'), 'LucyPrincessOnHoliday.HatA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('dfd183e8', 'e96ce933'), 'LucyPrincessOnHoliday.BodyA.MaterialMap.2048')),
        ],
        # Hat shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Body Component ====================
        '30abbad1': [
            (log,                             ('3.1: LucyPrincessOnHoliday Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ac5acb2d': [
            (log,                             ('3.1: LucyPrincessOnHoliday Body Draw VB Hash',)),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
        ],
        'd31f22c6': [
            (log,                             ('3.1: LucyPrincessOnHoliday Body Position VB Hash',)),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
        ],
        '38a28e54': [
            (log,                             ('3.1: LucyPrincessOnHoliday Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
        ],
        '0c802011': [
            (log,                             ('3.1: LucyPrincessOnHoliday Body Blend VB Hash',)),
            (add_section_if_missing,          ('30abbad1', 'LucyPrincessOnHoliday.Body.IB', 'match_priority = 0\n')),
        ],
        # Body shares its Diffuse, LightMap, MaterialMap and NormalMap hashes with Hat and Hair; see those Components above.

        # ==================== Face Component ====================
        'df3e3965': [
            (log,                             ('3.1: LucyPrincessOnHoliday Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2db957ac': [
            (log,                             ('3.1: LucyPrincessOnHoliday Face Draw VB Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
        ],
        '17abc4eb': [
            (log,                             ('3.1: LucyPrincessOnHoliday Face Position VB Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
        ],
        'e78a4ee2': [
            (log,                             ('3.1: LucyPrincessOnHoliday Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
        ],
        'a2054778': [
            (log,                             ('3.1: LucyPrincessOnHoliday Face Blend VB Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
        ],
        '4e2d5baa': [
            (log,                             ('3.1: LucyPrincessOnHoliday FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2578d35b', 'LucyPrincessOnHoliday.FaceA.Diffuse.1024')),
        ],
        '2578d35b': [
            (log,                             ('3.1: LucyPrincessOnHoliday FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('df3e3965', 'LucyPrincessOnHoliday.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4e2d5baa', 'LucyPrincessOnHoliday.FaceA.Diffuse.2048')),
        ],
        # Face has no NormalMap, LightMap or MaterialMap hashes; Diffuse is its only texture.

        # ==================== Weapon Component ====================
        'd1e02a54': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2bbcadde': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Draw VB Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
        ],
        '94c22510': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Position VB Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
        ],
        '98dfc0a3': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
        ],
        '0456e606': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Blend VB Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
        ],
        'e1f0071b': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('78f83ff4', 'LucyPrincessOnHoliday.weapon.Diffuse.1024')),
        ],
        '78f83ff4': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1f0071b', 'LucyPrincessOnHoliday.weapon.Diffuse.2048')),
        ],
        'bc9df18b': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9b4b3ffa', 'LucyPrincessOnHoliday.weapon.LightMap.1024')),
        ],
        '9b4b3ffa': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc9df18b', 'LucyPrincessOnHoliday.weapon.LightMap.2048')),
        ],
        'a962e9eb': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('599a0d46', 'acaa0bf6'), 'LucyPrincessOnHoliday.weapon.MaterialMap.1024')),
            (update_hash,                     ('2ece6f26',)),
        ],
        '2ece6f26': [
            (log,                             ('3.2: LucyPrincessOnHoliday weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('599a0d46', 'acaa0bf6'), 'LucyPrincessOnHoliday.weapon.MaterialMap.1024')),
        ],
        'acaa0bf6': [
            (log,                             ('3.1: LucyPrincessOnHoliday weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2ece6f26', 'a962e9eb'), 'LucyPrincessOnHoliday.weapon.MaterialMap.2048')),
            (update_hash,                     ('599a0d46',)),
        ],
        '599a0d46': [
            (log,                             ('3.2: LucyPrincessOnHoliday weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d1e02a54', 'LucyPrincessOnHoliday.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('2ece6f26', 'a962e9eb'), 'LucyPrincessOnHoliday.weapon.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'LucyPrincessOnHoliday',
    'game_versions': ['3.1', '3.2'],
}
