"""
Alice Character Hash Commands
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
    Returns Alice's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd131acb1': [
            (log,                             ('2.1: Alice Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd515e182': [
            (log,                             ('2.2: Alice Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        ],
        'ad686c31': [
            (log,                             ('2.2: Alice Hair Position VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        ],
        'b86d14b0': [
            (log,                             ('2.2: Alice Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        ],
        'cf1202fd': [
            (log,                             ('2.2: Alice Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
        ],
        '705caac9': [
            (log,                             ('2.1: Alice HairA and LegsA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('91d2f9fd', '5f504114'), 'Alice.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('91d2f9fd', '5f504114'), 'Alice.LegsA.Diffuse.1024')),
        ],
        '91d2f9fd': [
            (log,                             ('2.1: Alice HairA and LegsA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('705caac9', 'Alice.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('705caac9', 'Alice.LegsA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2: Alice HairA, BodyA, LegsA, BackAccA, sword and handguardPlate NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.LegsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.BackAccA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.sword.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Alice.handguardPlate.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2: Alice HairA, BodyA, LegsA, BackAccA, sword and handguardPlate NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.LegsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.BackAccA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.sword.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Alice.handguardPlate.NormalMap.2048')),
        ],
        '03543db2': [
            (log,                             ('2.1: Alice HairA and LegsA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c957d8f', 'Alice.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('6c957d8f', 'Alice.LegsA.LightMap.1024')),
        ],
        '6c957d8f': [
            (log,                             ('2.1: Alice HairA and LegsA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('03543db2', 'Alice.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('03543db2', 'Alice.LegsA.LightMap.2048')),
        ],
        '508530fe': [
            (log,                             ('2.1: Alice HairA and LegsA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc4c87fd', 'Alice.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('bc4c87fd', 'Alice.LegsA.MaterialMap.1024')),
        ],
        'bc4c87fd': [
            (log,                             ('2.1: Alice HairA and LegsA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'Alice.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('508530fe', 'Alice.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('508530fe', 'Alice.LegsA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'ebbe2894': [
            (log,                             ('2.2: Alice Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd482d732': [
            (log,                             ('2.2: Alice Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a3fb836a': [
            (log,                             ('2.2: Alice Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '85fb0c65': [
            (log,                             ('2.2: Alice Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '14c96dd0': [
            (log,                             ('2.2: Alice Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'Alice.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '8a512b21': [
            (log,                             ('2.1: Alice Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7a318f3d': [
            (log,                             ('2.2: Alice Body Draw VB Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        ],
        '37a05757': [
            (log,                             ('2.2: Alice Body Position VB Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        ],
        '9ad7d70c': [
            (log,                             ('2.2: Alice Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        ],
        '15935e48': [
            (log,                             ('2.2: Alice Body Blend VB Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
        ],
        '269185ed': [
            (log,                             ('2.1: Alice BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9201609a', 'Alice.BodyA.Diffuse.1024')),
        ],
        '9201609a': [
            (log,                             ('2.1: Alice BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('269185ed', 'Alice.BodyA.Diffuse.2048')),
        ],
        '0d72cb85': [
            (log,                             ('2.1: Alice BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('548623cd', 'Alice.BodyA.LightMap.1024')),
        ],
        '548623cd': [
            (log,                             ('2.1: Alice BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0d72cb85', 'Alice.BodyA.LightMap.2048')),
        ],
        '95967afb': [
            (log,                             ('2.1: Alice BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e05e4c54', 'Alice.BodyA.MaterialMap.1024')),
        ],
        'e05e4c54': [
            (log,                             ('2.1: Alice BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('8a512b21', 'Alice.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95967afb', 'Alice.BodyA.MaterialMap.2048')),
        ],

        # ==================== Legs Component ====================
        '625c2692': [
            (log,                             ('2.1: Alice Legs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3e4c0174': [
            (log,                             ('2.2: Alice Legs Draw VB Hash',)),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        ],
        'c1aaa893': [
            (log,                             ('2.2: Alice Legs Position VB Hash',)),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        ],
        '2821afc9': [
            (log,                             ('2.2: Alice Legs Texcoord VB Hash',)),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        ],
        'a1b46da2': [
            (log,                             ('2.2: Alice Legs Blend VB Hash',)),
            (add_section_if_missing,          ('625c2692', 'Alice.Legs.IB', 'match_priority = 0\n')),
        ],

        # ==================== BeltAcc Component ====================
        '993d2ddd': [
            (log,                             ('2.2: Alice BeltAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c2b0bfbd': [
            (log,                             ('2.2: Alice BeltAcc Draw VB Hash',)),
            (add_section_if_missing,          ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'd0867379': [
            (log,                             ('2.2: Alice BeltAcc Position VB Hash',)),
            (add_section_if_missing,          ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'd72a4315': [
            (log,                             ('2.2: Alice BeltAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        '73b54620': [
            (log,                             ('2.2: Alice BeltAcc Blend VB Hash',)),
            (add_section_if_missing,          ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'bf0e4dab': [
            (log,                             ('2.2: Alice BeltAcc Diffuse 1024p & 2048p Hash',)),
            (add_section_if_missing,          ('993d2ddd', 'Alice.BeltAcc.IB', 'match_priority = 0\n')),
        ],

        # ==================== BackAcc Component ====================
        'bd2277ef': [
            (log,                             ('2.2: Alice BackAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '03090c30': [
            (log,                             ('2.2: Alice BackAcc Draw VB Hash',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '23712d3d': [
            (log,                             ('2.2: Alice BackAcc Position VB Hash',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '1c272241': [
            (log,                             ('2.2: Alice BackAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '37717c75': [
            (log,                             ('2.2: Alice BackAcc Blend VB Hash',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '79cbbcc4': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('228bdc7c', 'Alice.BackAccA.Diffuse.1024')),
            (multiply_section_if_missing,     ('228bdc7c', 'Alice.sword.Diffuse.1024')),
            (multiply_section_if_missing,     ('228bdc7c', 'Alice.handguardPlate.Diffuse.1024')),
        ],
        'a226ce08': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('980c7ed0', 'Alice.BackAccA.LightMap.1024')),
            (multiply_section_if_missing,     ('980c7ed0', 'Alice.sword.LightMap.1024')),
            (multiply_section_if_missing,     ('980c7ed0', 'Alice.handguardPlate.LightMap.1024')),
        ],
        '9ada942b': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('072eabe7', 'Alice.BackAccA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('072eabe7', 'Alice.sword.MaterialMap.1024')),
            (multiply_section_if_missing,     ('072eabe7', 'Alice.handguardPlate.MaterialMap.1024')),
        ],
        '228bdc7c': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('79cbbcc4', 'Alice.BackAccA.Diffuse.2048')),
            (multiply_section_if_missing,     ('79cbbcc4', 'Alice.sword.Diffuse.2048')),
            (multiply_section_if_missing,     ('79cbbcc4', 'Alice.handguardPlate.Diffuse.2048')),
        ],
        '980c7ed0': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a226ce08', 'Alice.BackAccA.LightMap.2048')),
            (multiply_section_if_missing,     ('a226ce08', 'Alice.sword.LightMap.2048')),
            (multiply_section_if_missing,     ('a226ce08', 'Alice.handguardPlate.LightMap.2048')),
        ],
        '072eabe7': [
            (log,                             ('2.2: Alice BackAccA, sword and handguardPlate MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('bd2277ef', 'Alice.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ada942b', 'Alice.BackAccA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9ada942b', 'Alice.sword.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9ada942b', 'Alice.handguardPlate.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'b078ff22': [
            (log,                             ('2.1: Alice Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '70088a4a': [
            (log,                             ('2.2: Alice Face Draw VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
        ],
        '4a1a190d': [
            (log,                             ('2.2: Alice Face Position VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
        ],
        '7c9dbd4a': [
            (log,                             ('2.2: Alice Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('0749a6d7',)),
        ],
        '0749a6d7': [
            (log,                             ('3.2: Alice Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '2326355e': [
            (log,                             ('2.2: Alice Face Blend VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
        ],
        '9f3e582c': [
            (log,                             ('2.1: Alice FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33fdeb6d', 'Alice.FaceA.Diffuse.1024')),
        ],
        '33fdeb6d': [
            (log,                             ('2.1: Alice FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b078ff22', 'Alice.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f3e582c', 'Alice.FaceA.Diffuse.2048')),
        ],

        # ==================== Sword Component ====================
        '30205a68': [
            (log,                             ('2.2: Alice sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f26a8aac': [
            (log,                             ('2.2: Alice sword Draw VB Hash',)),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
        ],
        '47a48c42': [
            (log,                             ('2.2: Alice sword Position VB Hash',)),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
        ],
        '7b3126b6': [
            (log,                             ('2.2: Alice sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
        ],
        'bb487b00': [
            (log,                             ('2.2: Alice sword Blend VB Hash',)),
            (add_section_if_missing,          ('30205a68', 'Alice.sword.IB', 'match_priority = 0\n')),
        ],

        # ==================== handguardPlate Component ====================
        '323b1a95': [
            (log,                             ('2.2: Alice handguardPlate IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0a06059e': [
            (log,                             ('2.2: Alice handguardPlate Draw VB Hash',)),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
        ],
        'bd544be3': [
            (log,                             ('2.2: Alice handguardPlate Position VB Hash',)),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
        ],
        '9a136061': [
            (log,                             ('2.2: Alice handguardPlate Texcoord VB Hash',)),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
        ],
        'aac53ae5': [
            (log,                             ('2.2: Alice handguardPlate Blend VB Hash',)),
            (add_section_if_missing,          ('323b1a95', 'Alice.handguardPlate.IB', 'match_priority = 0\n')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Alice',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}