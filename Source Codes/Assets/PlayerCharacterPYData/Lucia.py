"""
Lucia Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.3 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Lucia's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '340fc999': [
            (log,                             ('2.3 - 3.2: Lucia Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fed6eef6': [
            (log,                             ('2.3 - 3.2: Lucia Hair Draw VB Hash',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        ],
        '78043df0': [
            (log,                             ('2.3 - 3.2: Lucia Hair Position VB Hash',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        ],
        '97dde567': [
            (log,                             ('2.3 - 3.2: Lucia Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        ],
        'bfd60db5': [
            (log,                             ('2.3 - 3.2: Lucia Hair Blend VB Hash',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        ],
        '5b0b47c9': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab461f68', 'Lucia.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('ab461f68', 'Lucia.CapeA.Diffuse.1024')),
            (multiply_section_if_missing,     ('ab461f68', 'Lucia.CapeAccessoryA.Diffuse.1024')),
        ],
        'ab461f68': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b0b47c9', 'Lucia.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5b0b47c9', 'Lucia.CapeA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5b0b47c9', 'Lucia.CapeAccessoryA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA, CapeAccessoryA, BodyA, weapon - 权杖 and weapon - 书 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.CapeA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.CapeAccessoryA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.weapon - 权杖.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Lucia.weapon - 书.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA, CapeAccessoryA, BodyA, weapon - 权杖 and weapon - 书 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.CapeA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.CapeAccessoryA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.weapon - 权杖.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Lucia.weapon - 书.NormalMap.2048')),
        ],
        '243feee8': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dda3939e', 'Lucia.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('dda3939e', 'Lucia.CapeA.LightMap.1024')),
            (multiply_section_if_missing,     ('dda3939e', 'Lucia.CapeAccessoryA.LightMap.1024')),
        ],
        'dda3939e': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('243feee8', 'Lucia.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('243feee8', 'Lucia.CapeA.LightMap.2048')),
            (multiply_section_if_missing,     ('243feee8', 'Lucia.CapeAccessoryA.LightMap.2048')),
        ],
        '211a5700': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c09e5350', 'Lucia.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c09e5350', 'Lucia.CapeA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('c09e5350', 'Lucia.CapeAccessoryA.MaterialMap.1024')),
        ],
        'c09e5350': [
            (log,                             ('2.3 - 3.2: Lucia HairA, CapeA and CapeAccessoryA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('211a5700', 'Lucia.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('211a5700', 'Lucia.CapeA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('211a5700', 'Lucia.CapeAccessoryA.MaterialMap.2048')),
        ],
        # Cape and CapeAccessory share their Diffuse, LightMap and MaterialMap hashes with Hair; see that Component above.

        # ==================== Hair Shadow Component ====================
        '7be43e2b': [
            (log,                             ('2.3 - 3.2: Lucia Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0695fa38': [
            (log,                             ('2.3 - 3.2: Lucia Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '82729474': [
            (log,                             ('2.3 - 3.2: Lucia Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '38f2daa7': [
            (log,                             ('2.3 - 3.2: Lucia Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9662cc92': [
            (log,                             ('2.3 - 3.2: Lucia Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Cape Component ====================
        'cd80d116': [
            (log,                             ('2.3 - 3.2: Lucia Cape IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6533c56a': [
            (log,                             ('2.3 - 3.2: Lucia Cape Draw VB Hash',)),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
        ],
        '5f21562d': [
            (log,                             ('2.3 - 3.2: Lucia Cape Position VB Hash',)),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
        ],
        '08ae4b5d': [
            (log,                             ('2.5: Lucia Cape Position Hash',)),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
        ],
        'dd0e570f': [
            (log,                             ('2.3 - 3.2: Lucia Cape Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
        ],
        'b917fca5': [
            (log,                             ('2.3 - 3.2: Lucia Cape Blend VB Hash',)),
            (add_section_if_missing,          ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
        ],

        # ==================== CapeAccessory Component ====================
        '692a4e10': [
            (log,                             ('2.3 - 3.2: Lucia CapeAccessory IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '439208cc': [
            (log,                             ('2.3 - 3.2: Lucia CapeAccessory Draw VB Hash',)),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
        ],
        'c035f6bd': [
            (log,                             ('2.3 - 3.2: Lucia CapeAccessory Position VB Hash',)),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
        ],
        '90f30bc1': [
            (log,                             ('2.3 - 3.2: Lucia CapeAccessory Texcoord VB Hash',)),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
        ],
        '946dc2ff': [
            (log,                             ('2.3 - 3.2: Lucia CapeAccessory Blend VB Hash',)),
            (add_section_if_missing,          ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'd39c304d': [
            (log,                             ('2.3 - 3.2: Lucia Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b3a498b5': [
            (log,                             ('2.3 - 3.2: Lucia Body Draw VB Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        ],
        '234c641a': [
            (log,                             ('2.3 - 3.2: Lucia Body Position VB Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        ],
        '0400f04f': [
            (log,                             ('2.3 - 3.2: Lucia Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        ],
        '3f4f9fa9': [
            (log,                             ('2.3 - 3.2: Lucia Body Blend VB Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        ],
        '2ca45943': [
            (log,                             ('2.3 - 3.2: Lucia BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('614c9ad5', 'Lucia.BodyA.Diffuse.1024')),
        ],
        '614c9ad5': [
            (log,                             ('2.3 - 3.2: Lucia BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2ca45943', 'Lucia.BodyA.Diffuse.2048')),
        ],
        'f117c868': [
            (log,                             ('2.3 - 3.2: Lucia BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('30b94be9', 'Lucia.BodyA.LightMap.1024')),
        ],
        '30b94be9': [
            (log,                             ('2.3 - 3.2: Lucia BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f117c868', 'Lucia.BodyA.LightMap.2048')),
        ],
        'a16861d2': [
            (log,                             ('2.3 - 3.2: Lucia BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c0fe7e43', 'Lucia.BodyA.MaterialMap.1024')),
        ],
        'c0fe7e43': [
            (log,                             ('2.3 - 3.2: Lucia BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a16861d2', 'Lucia.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== eyebrow Component ====================
        '84eaa4c6': [
            (log,                             ('2.3 - 3.2: Lucia eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f917cafc': [
            (log,                             ('2.3 - 3.2: Lucia eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
        ],
        'c30559bb': [
            (log,                             ('2.3 - 3.2: Lucia eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
        ],
        '05342ce9': [
            (log,                             ('2.3 - 3.1: Lucia eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('9e121fda',)),
        ],
        '9e121fda': [
            (log,                             ('3.2: Lucia eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '8893a84c': [
            (log,                             ('2.3 - 3.2: Lucia eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
        ],
        '20a6224d': [
            (log,                             ('2.3 - 3.2: Lucia eyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('12ec6e26', 'Lucia.eyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('12ec6e26', 'Lucia.FaceA.Diffuse.1024')),
        ],
        '12ec6e26': [
            (log,                             ('2.3 - 3.2: Lucia eyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('20a6224d', 'Lucia.eyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('20a6224d', 'Lucia.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '6986f28e': [
            (log,                             ('2.3 - 3.2: Lucia Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7915db83': [
            (log,                             ('2.3 - 3.2: Lucia Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        ],
        '430748c4': [
            (log,                             ('2.3 - 3.2: Lucia Face Position VB Hash',)),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        ],
        '9648c6d3': [
            (log,                             ('2.3 - 3.1: Lucia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('43cb221f',)),
        ],
        '43cb221f': [
            (log,                             ('3.2: Lucia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '925947a7': [
            (log,                             ('2.3 - 3.2: Lucia Face Blend VB Hash',)),
            (add_section_if_missing,          ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with eyebrow; see that Component above.

        # ==================== Weapon - 权杖 Component ====================
        '5cca4239': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '73acb40f': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
        ],
        'adc940e0': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 Position VB Hash',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
        ],
        '9f2822c3': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 Texcoord VB Hash',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
        ],
        '7a83c0d2': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 Blend VB Hash',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
        ],
        '5a602448': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8d72bc12', 'Lucia.weapon - 权杖.Diffuse.1024')),
            (multiply_section_if_missing,     ('8d72bc12', 'Lucia.weapon - 书.Diffuse.1024')),
        ],
        '8d72bc12': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5a602448', 'Lucia.weapon - 权杖.Diffuse.2048')),
            (multiply_section_if_missing,     ('5a602448', 'Lucia.weapon - 书.Diffuse.2048')),
        ],
        'e2e48852': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84e4fd19', 'Lucia.weapon - 权杖.LightMap.1024')),
            (multiply_section_if_missing,     ('84e4fd19', 'Lucia.weapon - 书.LightMap.1024')),
        ],
        '84e4fd19': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e2e48852', 'Lucia.weapon - 权杖.LightMap.2048')),
            (multiply_section_if_missing,     ('e2e48852', 'Lucia.weapon - 书.LightMap.2048')),
        ],
        '74814017': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('009caccb', 'Lucia.weapon - 权杖.MaterialMap.1024')),
            (multiply_section_if_missing,     ('009caccb', 'Lucia.weapon - 书.MaterialMap.1024')),
        ],
        '009caccb': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 权杖 and weapon - 书 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5cca4239', 'Lucia.weapon - 权杖.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('74814017', 'Lucia.weapon - 权杖.MaterialMap.2048')),
            (multiply_section_if_missing,     ('74814017', 'Lucia.weapon - 书.MaterialMap.2048')),
        ],
        # weapon - 权杖 and weapon - 书 share their NormalMap hashes with Hair; see that Component above.

        # ==================== Weapon - 书 Component ====================
        'ebc05d0c': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 书 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '08ecb686': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 书 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
        ],
        '0ee71df8': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 书 Position VB Hash',)),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
        ],
        '2d98213f': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 书 Texcoord VB Hash',)),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
        ],
        'b1ebb25d': [
            (log,                             ('2.3 - 3.2: Lucia weapon - 书 Blend VB Hash',)),
            (add_section_if_missing,          ('ebc05d0c', 'Lucia.weapon - 书.IB', 'match_priority = 0\n')),
        ],
        # weapon - 书 shares its Diffuse, LightMap, MaterialMap and NormalMap hashes with weapon - 权杖 and Hair; see those Components above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lucia',
    'game_versions': ['2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
