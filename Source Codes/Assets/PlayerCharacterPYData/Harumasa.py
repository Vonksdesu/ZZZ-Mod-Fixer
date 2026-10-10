"""
Harumasa Character Hash Commands
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
    Returns Harumasa's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '6324de38': [
            (log,                             ('2.2 - 3.2: Harumasa Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f51a89c1': [
            (log,                             ('1.4 -> 1.5: Harumasa Hair IB Hash',)),
            (update_hash,                     ('6324de38',)),
        ],
        '9f75c05c': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Draw VB Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        ],
        'fa851c10': [
            (log,                             ('1.4 -> 1.5: Harumasa Hair Draw Hash',)),
            (update_hash,                     ('9f75c05c',)),
        ],
        'eddb9012': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Position VB Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        ],
        'f5727f53': [
            (log,                             ('1.4 -> 1.5: Harumasa Hair Position Hash',)),
            (update_hash,                     ('eddb9012',)),
        ],
        '4f45a9c5': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        ],
        '9879fba3': [
            (log,                             ('1.4 -> 1.5: Harumasa Hair Texcoord Hash',)),
            (update_hash,                     ('4f45a9c5',)),
        ],
        '2644c499': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Blend VB Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
        ],
        '52787e7d': [
            (log,                             ('1.4 -> 1.5: Harumasa Hair Blend Hash',)),
            (update_hash,                     ('2644c499',)),
        ],
        'b8f268ee': [
            (log,                             ('2.2 - 3.2: Harumasa HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5700ced5', 'Harumasa.HairA.Diffuse.1024')),
        ],
        '5700ced5': [
            (log,                             ('2.2 - 3.2: Harumasa HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8f268ee', 'Harumasa.HairA.Diffuse.2048')),
        ],
        '11041778': [
            (log,                             ('2.2 - 3.2: Harumasa HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('54cc6a9a', 'a1310b4f'), 'Harumasa.HairA.LightMap.1024')),
        ],
        '54cc6a9a': [
            (log,                             ('2.2 - 3.2: Harumasa HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('11041778', 'd4838b9d'), 'Harumasa.HairA.LightMap.2048')),
        ],
        'd4838b9d': [
            (log,                             ('1.4 -> 2.5: Harumasa HairA LightMap 2048p Hash',)),
            (update_hash,                     ('11041778',)),
        ],
        'a1310b4f': [
            (log,                             ('1.4 -> 2.5: Harumasa HairA LightMap 1024p Hash',)),
            (update_hash,                     ('11041778',)),
        ],
        '7217c146': [
            (log,                             ('2.2 - 3.2: Harumasa HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c2c9ad2d', 'Harumasa.HairA.MaterialMap.1024')),
        ],
        'c2c9ad2d': [
            (log,                             ('2.2 - 3.2: Harumasa HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7217c146', 'Harumasa.HairA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Harumasa HairA, LegsA, BodyA, weapon - 箭矢, weapon - 箭袋A, weapon - 箭袋B, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 箭矢.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 箭袋A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 箭袋B.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 刀.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 刀鞘.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.weapon - 弓.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.radioA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Harumasa.bowstringA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Harumasa HairA, LegsA, BodyA, weapon - 箭矢, weapon - 箭袋A, weapon - 箭袋B, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('6324de38', 'Harumasa.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 箭矢.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 箭袋A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 箭袋B.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 刀.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 刀鞘.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.weapon - 弓.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.radioA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Harumasa.bowstringA.NormalMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '9bb92eee': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2c64fa81': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('9bb92eee', 'Harumasa.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '2c094dd4': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('9bb92eee', 'Harumasa.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd1116809': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('9bb92eee', 'Harumasa.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'c39d129c': [
            (log,                             ('2.2 - 3.2: Harumasa Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('9bb92eee', 'Harumasa.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Legs Component ====================
        'aa7ba2dc': [
            (log,                             ('2.2 - 3.2: Harumasa Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7fdd2495': [
            (log,                             ('2.2 - 3.2: Harumasa Legs Draw VB Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        ],
        '5991a6b6': [
            (log,                             ('2.2 - 3.2: Harumasa Legs Position VB Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        ],
        '9d044bbd': [
            (log,                             ('2.2 - 3.2: Harumasa Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        ],
        'f58e77a5': [
            (log,                             ('2.2 - 3.2: Harumasa Legs Blend VB Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
        ],
        '44d74a1a': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('897c74d5', 'Harumasa.LegsA.Diffuse.1024')),
        ],
        '897c74d5': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('44d74a1a', 'Harumasa.LegsA.Diffuse.2048')),
        ],
        '4b4d0ff6': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('822ec07f', 'Harumasa.LegsA.LightMap.1024')),
        ],
        '822ec07f': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4b4d0ff6', 'Harumasa.LegsA.LightMap.2048')),
        ],
        '72885950': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b84027c8', 'bdbf66a1'), 'Harumasa.LegsA.MaterialMap.1024')),
        ],
        'b84027c8': [
            (log,                             ('2.2 - 3.2: Harumasa LegsA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('aa7ba2dc', 'Harumasa.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('72885950', 'ba8e396b'), 'Harumasa.LegsA.MaterialMap.2048')),
        ],
        'ba8e396b': [
            (log,                             ('1.4 -> 2.5: Harumasa LegsA MaterialMap 2048p Hash',)),
            (update_hash,                     ('72885950',)),
        ],
        'bdbf66a1': [
            (log,                             ('1.4 -> 2.5: Harumasa LegsA MaterialMap 1024p Hash',)),
            (update_hash,                     ('72885950',)),
        ],
        # Legs shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Body Component ====================
        '79679a10': [
            (log,                             ('2.2 - 3.2: Harumasa Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '78bea30d': [
            (log,                             ('1.4 -> 1.5: Harumasa Body IB Hash',)),
            (update_hash,                     ('79679a10',)),
        ],
        '1fb92e46': [
            (log,                             ('2.2 - 3.2: Harumasa Body Draw VB Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
        ],
        'cafffd37': [
            (log,                             ('1.4 -> 1.5: Harumasa Body Draw Hash',)),
            (update_hash,                     ('1fb92e46',)),
        ],
        '0899751e': [
            (log,                             ('2.2 - 3.2: Harumasa Body Position VB Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
        ],
        '3fa41462': [
            (log,                             ('1.4 -> 1.5: Harumasa Body Position Hash',)),
            (update_hash,                     ('0899751e',)),
        ],
        'e14fbc30': [
            (log,                             ('2.2 - 3.2: Harumasa Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
        ],
        '95ee1030': [
            (log,                             ('1.4 -> 1.5: Harumasa Body Texcoord Hash',)),
            (update_hash,                     ('e14fbc30',)),
        ],
        '347a0e9d': [
            (log,                             ('2.2 - 3.2: Harumasa Body Blend VB Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
        ],
        'c0b32d17': [
            (log,                             ('1.4 -> 1.5: Harumasa Body Blend Hash',)),
            (update_hash,                     ('347a0e9d',)),
        ],
        '49f8aaf6': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('999ec526', 'e0b0c6eb'), 'Harumasa.BodyA.Diffuse.1024')),
        ],
        '999ec526': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('49f8aaf6', 'ba52ac92'), 'Harumasa.BodyA.Diffuse.2048')),
        ],
        'ba52ac92': [
            (log,                             ('1.4 -> 1.5: Harumasa BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('49f8aaf6',)),
        ],
        'e0b0c6eb': [
            (log,                             ('1.4 -> 1.5: Harumasa BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('999ec526',)),
        ],
        'cc51476a': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2b1230cf', 'Harumasa.BodyA.LightMap.1024')),
        ],
        '2b1230cf': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cc51476a', 'Harumasa.BodyA.LightMap.2048')),
        ],
        '6d105f7e': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('c90264db', '2b0017d5'), 'Harumasa.BodyA.MaterialMap.1024')),
        ],
        'c90264db': [
            (log,                             ('2.2 - 3.2: Harumasa BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('79679a10', 'Harumasa.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('6d105f7e', 'cd1e0187'), 'Harumasa.BodyA.MaterialMap.2048')),
        ],
        'cd1e0187': [
            (log,                             ('1.4 -> 1.5: Harumasa BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('6d105f7e',)),
        ],
        '2b0017d5': [
            (log,                             ('1.4 -> 1.5: Harumasa BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('c90264db',)),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        'b0688334': [
            (log,                             ('2.2 - 3.2: Harumasa Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '747c3263': [
            (log,                             ('2.2 - 3.1: Harumasa Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        ],
        '4e6ea124': [
            (log,                             ('2.2 - 3.2: Harumasa Face Position VB Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        ],
        '48152e31': [
            (log,                             ('2.2 - 3.1: Harumasa Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('20095c2e',)),
        ],
        '20095c2e': [
            (log,                             ('3.2: Harumasa Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '4c813358': [
            (log,                             ('2.2 - 3.2: Harumasa Face Blend VB Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
        ],
        '4394c0b2': [
            (log,                             ('2.2 - 3.2: Harumasa FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c5596262', 'Harumasa.FaceA.Diffuse.1024')),
        ],
        'c5596262': [
            (log,                             ('2.2 - 3.2: Harumasa FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b0688334', 'Harumasa.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4394c0b2', 'Harumasa.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 箭矢 Component ====================
        '8ae5340d': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5c7e0333': [
            (log,                             ('2.2 - 3.1: Harumasa weapon - 箭矢 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
        ],
        '8af12b9e': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢 Position VB Hash',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
        ],
        'e696e4c6': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢 Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
        ],
        'cbf4b91e': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢 Blend VB Hash',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
        ],
        '81f189a2': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.weapon - 箭矢.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.weapon - 箭袋A.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.weapon - 刀.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.weapon - 刀鞘.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.weapon - 弓.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.radioA.Diffuse.1024')),
            (multiply_section_if_missing,     ('cc14d492', 'Harumasa.bowstringA.Diffuse.1024')),
        ],
        'cc14d492': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.weapon - 箭矢.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.weapon - 箭袋A.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.weapon - 刀.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.weapon - 刀鞘.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.weapon - 弓.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.radioA.Diffuse.2048')),
            (multiply_section_if_missing,     ('81f189a2', 'Harumasa.bowstringA.Diffuse.2048')),
        ],
        '4302efb7': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.weapon - 箭矢.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.weapon - 箭袋A.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.weapon - 刀.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.weapon - 刀鞘.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.weapon - 弓.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.radioA.LightMap.1024')),
            (multiply_section_if_missing,     ('8d7254c3', 'Harumasa.bowstringA.LightMap.1024')),
        ],
        '8d7254c3': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.weapon - 箭矢.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.weapon - 箭袋A.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.weapon - 刀.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.weapon - 刀鞘.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.weapon - 弓.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.radioA.LightMap.2048')),
            (multiply_section_if_missing,     ('4302efb7', 'Harumasa.bowstringA.LightMap.2048')),
        ],
        '38b0417f': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.weapon - 箭矢.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.weapon - 箭袋A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.weapon - 刀.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.weapon - 刀鞘.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.weapon - 弓.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.radioA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('cf646184', 'Harumasa.bowstringA.MaterialMap.1024')),
        ],
        'cf646184': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭矢, weapon - 箭袋A, weapon - 刀, weapon - 刀鞘, weapon - 弓, radioA and bowstringA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ae5340d', 'Harumasa.weapon - 箭矢.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.weapon - 箭矢.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.weapon - 箭袋A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.weapon - 刀.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.weapon - 刀鞘.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.weapon - 弓.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.radioA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('38b0417f', 'Harumasa.bowstringA.MaterialMap.2048')),
        ],
        # weapon - 箭矢 shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Weapon - 箭袋 Component ====================
        '448ba3f6': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fc5a562a': [
            (log,                             ('2.2 - 3.1: Harumasa weapon - 箭袋 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
        ],
        '75e1907f': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋 Position VB Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
        ],
        '0d04cfb0': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋 Texcoord VB Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
        ],
        'ce8a5469': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋 Blend VB Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
        ],
        'c776b2ac': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e6cb774e', 'Harumasa.weapon - 箭袋B.Diffuse.1024')),
        ],
        'e6cb774e': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c776b2ac', 'Harumasa.weapon - 箭袋B.Diffuse.2048')),
        ],
        '0e38f04c': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B LightMap 2048p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('56b0cd82', 'Harumasa.weapon - 箭袋B.LightMap.1024')),
        ],
        '56b0cd82': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B LightMap 1024p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e38f04c', 'Harumasa.weapon - 箭袋B.LightMap.2048')),
        ],
        'ceb7b1fa': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('af798757', 'Harumasa.weapon - 箭袋B.MaterialMap.1024')),
        ],
        'af798757': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 箭袋B MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('448ba3f6', 'Harumasa.weapon - 箭袋.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ceb7b1fa', 'Harumasa.weapon - 箭袋B.MaterialMap.2048')),
        ],
        # weapon - 箭袋 shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.

        # ==================== Weapon - 刀 Component ====================
        '30f715df': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a23df160': [
            (log,                             ('2.2 - 3.1: Harumasa weapon - 刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
        ],
        'e7eb0751': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀 Position VB Hash',)),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
        ],
        '46a82ecd': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
        ],
        '1dcdd87d': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀 Blend VB Hash',)),
            (add_section_if_missing,          ('30f715df', 'Harumasa.weapon - 刀.IB', 'match_priority = 0\n')),
        ],
        # weapon - 刀 shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.

        # ==================== Weapon - 刀鞘 Component ====================
        'b92340c6': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀鞘 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '80fadc88': [
            (log,                             ('2.2 - 3.1: Harumasa weapon - 刀鞘 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        '4d13c1da': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀鞘 Position VB Hash',)),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        '8db5bfa8': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀鞘 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        '30c2db1a': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 刀鞘 Blend VB Hash',)),
            (add_section_if_missing,          ('b92340c6', 'Harumasa.weapon - 刀鞘.IB', 'match_priority = 0\n')),
        ],
        # weapon - 刀鞘 shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.

        # ==================== Weapon - 弓 Component ====================
        'fdaa94b9': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 弓 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a385ad88': [
            (log,                             ('2.2 - 3.1: Harumasa weapon - 弓 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
        ],
        '11ddc4c0': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 弓 Position VB Hash',)),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
        ],
        '0f901bce': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 弓 Texcoord VB Hash',)),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
        ],
        'd9d7d268': [
            (log,                             ('2.2 - 3.2: Harumasa weapon - 弓 Blend VB Hash',)),
            (add_section_if_missing,          ('fdaa94b9', 'Harumasa.weapon - 弓.IB', 'match_priority = 0\n')),
        ],
        # weapon - 弓 shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.

        # ==================== radio Component ====================
        '28ddcf0f': [
            (log,                             ('2.2 - 3.2: Harumasa radio IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '545441d8': [
            (log,                             ('2.2 - 3.2: Harumasa radio Draw VB Hash',)),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
        ],
        'fa0083a4': [
            (log,                             ('2.2 - 3.2: Harumasa radio Position VB Hash',)),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
        ],
        '74c5fd55': [
            (log,                             ('2.2 - 3.2: Harumasa radio Texcoord VB Hash',)),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
        ],
        '999c8d00': [
            (log,                             ('2.2 - 3.2: Harumasa radio Blend VB Hash',)),
            (add_section_if_missing,          ('28ddcf0f', 'Harumasa.radio.IB', 'match_priority = 0\n')),
        ],
        # radio shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.

        # ==================== bowstring Component ====================
        '4785491b': [
            (log,                             ('2.2 - 3.2: Harumasa bowstring IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b5c06ca5': [
            (log,                             ('2.2 - 3.2: Harumasa bowstring Draw VB Hash',)),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
        ],
        '84c629fe': [
            (log,                             ('2.2 - 3.2: Harumasa bowstring Position VB Hash',)),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
        ],
        '62fe83fc': [
            (log,                             ('2.2 - 3.2: Harumasa bowstring Texcoord VB Hash',)),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
        ],
        '02032760': [
            (log,                             ('2.2 - 3.2: Harumasa bowstring Blend VB Hash',)),
            (add_section_if_missing,          ('4785491b', 'Harumasa.bowstring.IB', 'match_priority = 0\n')),
        ],
        # bowstring shares its Diffuse/LightMap/MaterialMap with weapon - 箭矢, and NormalMap with Hair; see those Components above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Harumasa',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
