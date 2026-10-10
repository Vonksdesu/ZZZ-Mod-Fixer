"""
Seth Character Hash Commands
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
    Returns Seth's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '35cf83ad': [
            (log,                             ('2.2 - 3.2: Seth Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd18b1600': [
            (log,                             ('2.2 - 3.2: Seth Hair Draw VB Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        ],
        '9b358a6b': [
            (log,                             ('2.2 - 3.2: Seth Hair Position VB Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        ],
        'a72f760f': [
            (log,                             ('1.3 -> 1.4: Seth Hair Texcoord Hash',)),
            (update_hash,                     ('a91eeef2',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_13_remap_texcoord,           ('14_Seth_Hair', ('4f', '2e', '2f', '2e'), ('4B', '2e', '2f', '2e'))),
        ],
        'a91eeef2': [
            (log,                             ('2.2 - 3.2: Seth Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        ],
        'df779976': [
            (log,                             ('2.2 - 3.2: Seth Hair Blend VB Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
        ],
        'dc8e244d': [
            (log,                             ('2.2 - 3.2: Seth HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d3756c37', 'Seth.HairA.Diffuse.1024')),
        ],
        'd3756c37': [
            (log,                             ('2.2 - 3.2: Seth HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc8e244d', 'Seth.HairA.Diffuse.2048')),
        ],
        '3376b58c': [
            (log,                             ('1.1 -> 2.5: Seth HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '24d52dd8': [
            (log,                             ('1.1 -> 2.5: Seth HairA NormalMap 1024p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Seth HairA, BodyA, weapon - 盾A and weapon - 棍A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Seth.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seth.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seth.weapon - 盾A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Seth.weapon - 棍A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Seth HairA, BodyA, weapon - 盾A and weapon - 棍A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Seth.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seth.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seth.weapon - 盾A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Seth.weapon - 棍A.NormalMap.2048')),
        ],
        'd4de9ec1': [
            (log,                             ('1.1 -> 2.5: Seth HairA LightMap 2048p Hash',)),
            (update_hash,                     ('a855884d',)),
        ],
        'c01dbf6c': [
            (log,                             ('1.1 -> 2.5: Seth HairA LightMap 1024p Hash',)),
            (update_hash,                     ('a855884d',)),
        ],
        'a855884d': [
            (log,                             ('2.2 - 3.2: Seth HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca070fa7', 'Seth.HairA.LightMap.1024')),
        ],
        'ca070fa7': [
            (log,                             ('2.2 - 3.2: Seth HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a855884d', 'Seth.HairA.LightMap.2048')),
        ],
        '3c256565': [
            (log,                             ('2.2 - 3.2: Seth HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('833e9405', 'Seth.HairA.MaterialMap.1024')),
        ],
        '833e9405': [
            (log,                             ('2.2 - 3.2: Seth HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('35cf83ad', 'Seth.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3c256565', 'Seth.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '52930334': [
            (log,                             ('2.2 - 3.2: Seth Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2719bad1': [
            (log,                             ('2.2 - 3.2: Seth Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ab8a95a3': [
            (log,                             ('2.2 - 3.2: Seth Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ca884fde': [
            (log,                             ('2.2 - 3.2: Seth Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '85cb63a9': [
            (log,                             ('2.2 - 3.2: Seth Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('52930334', 'Seth.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '00172ec3': [
            (log,                             ('2.2 - 3.2: Seth Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2e990d11': [
            (log,                             ('2.2 - 3.2: Seth Body Draw VB Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        ],
        'c5e25439': [
            (log,                             ('2.2 - 3.2: Seth Body Position VB Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        ],
        'd4837e60': [
            (log,                             ('2.2 - 3.2: Seth Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        ],
        'b758d72f': [
            (log,                             ('2.2 - 3.2: Seth Body Blend VB Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
        ],
        '7f8416ab': [
            (log,                             ('2.2 - 3.2: Seth BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dbc90150', 'Seth.BodyA.Diffuse.1024')),
        ],
        'dbc90150': [
            (log,                             ('2.2 - 3.2: Seth BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f8416ab', 'Seth.BodyA.Diffuse.2048')),
        ],
        'dde45d3d': [
            (log,                             ('1.1 -> 2.5: Seth BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '62b047c5': [
            (log,                             ('1.1 -> 2.5: Seth BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '3d97c2ef': [
            (log,                             ('1.1 -> 2.5: Seth BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('5b205468',)),
        ],
        '9436aa83': [
            (log,                             ('1.1 -> 2.5: Seth BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('5b205468',)),
        ],
        '5b205468': [
            (log,                             ('2.2 - 3.2: Seth BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57cf813c', 'Seth.BodyA.LightMap.1024')),
        ],
        '57cf813c': [
            (log,                             ('2.2 - 3.2: Seth BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b205468', 'Seth.BodyA.LightMap.2048')),
        ],
        '732d3f81': [
            (log,                             ('2.2 - 3.2: Seth BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('56775fcb', 'Seth.BodyA.MaterialMap.1024')),
        ],
        '56775fcb': [
            (log,                             ('2.2 - 3.2: Seth BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('00172ec3', 'Seth.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('732d3f81', 'Seth.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '52f5aa74': [
            (log,                             ('2.2 - 3.2: Seth Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3b7803dd': [
            (log,                             ('2.2 - 3.2: Seth Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
        ],
        '016a909a': [
            (log,                             ('2.2 - 3.2: Seth Face Position VB Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
        ],
        'bff3e0b3': [
            (log,                             ('3.0 -> 3.1: Seth Face Texcoord Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b3f6842f',)),
        ],
        'b3f6842f': [
            (log,                             ('3.1: Seth Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
        ],
        '9dad4eb7': [
            (log,                             ('2.2 - 3.2: Seth Face Blend VB Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
        ],
        '09981aff': [
            (log,                             ('2.2 - 3.2: Seth FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fe5b7534', 'Seth.FaceA.Diffuse.1024')),
        ],
        'fe5b7534': [
            (log,                             ('2.2 - 3.2: Seth FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('52f5aa74', 'Seth.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('09981aff', 'Seth.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 盾 Component ====================
        'd15922eb': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4b92cd34': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        'c17c87ba': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾 Position VB Hash',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        'bb5022ce': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        '08a86fef': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾 Blend VB Hash',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
        ],
        'c5f5e59c': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c6131117', 'Seth.weapon - 盾A.Diffuse.1024')),
            (multiply_section_if_missing,     ('c6131117', 'Seth.weapon - 棍A.Diffuse.1024')),
        ],
        'c6131117': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c5f5e59c', 'Seth.weapon - 盾A.Diffuse.2048')),
            (multiply_section_if_missing,     ('c5f5e59c', 'Seth.weapon - 棍A.Diffuse.2048')),
        ],
        '47016fd0': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2f2525f7', 'Seth.weapon - 盾A.LightMap.1024')),
            (multiply_section_if_missing,     ('2f2525f7', 'Seth.weapon - 棍A.LightMap.1024')),
        ],
        '2f2525f7': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('47016fd0', 'Seth.weapon - 盾A.LightMap.2048')),
            (multiply_section_if_missing,     ('47016fd0', 'Seth.weapon - 棍A.LightMap.2048')),
        ],
        '4e10eb19': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('36d4290d', 'Seth.weapon - 盾A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('36d4290d', 'Seth.weapon - 棍A.MaterialMap.1024')),
        ],
        '36d4290d': [
            (log,                             ('2.2 - 3.2: Seth weapon - 盾A and weapon - 棍A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d15922eb', 'Seth.weapon - 盾.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4e10eb19', 'Seth.weapon - 盾A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4e10eb19', 'Seth.weapon - 棍A.MaterialMap.2048')),
        ],

        # ==================== weapon - 棍 Component ====================
        '713b2a30': [
            (log,                             ('2.2 - 3.2: Seth weapon - 棍 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'eeea5739': [
            (log,                             ('2.2 - 3.2: Seth weapon - 棍 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
        ],
        '2c38f2c4': [
            (log,                             ('2.2 - 3.2: Seth weapon - 棍 Position VB Hash',)),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
        ],
        '0acdbd8c': [
            (log,                             ('2.2 - 3.2: Seth weapon - 棍 Texcoord VB Hash',)),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
        ],
        'd537bc36': [
            (log,                             ('2.2 - 3.2: Seth weapon - 棍 Blend VB Hash',)),
            (add_section_if_missing,          ('713b2a30', 'Seth.weapon - 棍.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Seth',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
