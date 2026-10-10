"""
Sunna Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.6 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Sunna's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '904ecd0f': [
            (log,                             ('2.6 - 3.2: Sunna Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cc070c66': [
            (log,                             ('2.6 - 3.2: Sunna Hair Draw VB Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
        ],
        '5c030eea': [
            (log,                             ('2.6 - 3.2: Sunna Hair Position VB Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
        ],
        '06bea24e': [
            (log,                             ('2.6 - 3.2: Sunna Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
        ],
        '0c183c3f': [
            (log,                             ('2.6 - 3.2: Sunna Hair Blend VB Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
        ],
        '2fcfee64': [
            (log,                             ('2.6 - 3.2: Sunna HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e85201e7', 'Sunna.HairA.Diffuse.1024')),
        ],
        'e85201e7': [
            (log,                             ('2.6 - 3.2: Sunna HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2fcfee64', 'Sunna.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6 - 3.2: Sunna HairA, BodyA, WeaponBackpackCharmGripA, paopao(战斗状态)A, paopao(非战斗状态)A, WeaponA, WeaponDecorationA and WeaponDecoration2A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.WeaponBackpackCharmGripA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.paopao(战斗状态)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.paopao(非战斗状态)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.WeaponDecorationA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sunna.WeaponDecoration2A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6 - 3.2: Sunna HairA, BodyA, WeaponBackpackCharmGripA, paopao(战斗状态)A, paopao(非战斗状态)A, WeaponA, WeaponDecorationA and WeaponDecoration2A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.WeaponBackpackCharmGripA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.paopao(战斗状态)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.paopao(非战斗状态)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.WeaponDecorationA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sunna.WeaponDecoration2A.NormalMap.2048')),
        ],
        '8cd786f7': [
            (log,                             ('2.6 - 3.2: Sunna HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2b36369', 'Sunna.HairA.LightMap.1024')),
        ],
        'a2b36369': [
            (log,                             ('2.6 - 3.2: Sunna HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8cd786f7', 'Sunna.HairA.LightMap.2048')),
        ],
        '3f11dfd9': [
            (log,                             ('2.6 - 3.2: Sunna HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab3c12c0', 'Sunna.HairA.MaterialMap.1024')),
        ],
        'ab3c12c0': [
            (log,                             ('2.6 - 3.2: Sunna HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('904ecd0f', 'Sunna.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f11dfd9', 'Sunna.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '3ab6d438': [
            (log,                             ('2.6 - 3.2: Sunna Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        'b3c6ea5a': [
            (log,                             ('2.6 - 3.2: Sunna Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8991360f': [
            (log,                             ('2.6 - 3.2: Sunna Body Draw VB Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
        ],
        '6eb68b62': [
            (log,                             ('2.6 - 3.2: Sunna Body Position VB Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
        ],
        '712eb020': [
            (log,                             ('2.6 - 3.2: Sunna Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
        ],
        '53661c9a': [
            (log,                             ('2.6 - 3.2: Sunna Body Blend VB Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
        ],
        'f051c211': [
            (log,                             ('2.6 - 3.2: Sunna BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa0f48fe', 'Sunna.BodyA.Diffuse.1024')),
        ],
        'aa0f48fe': [
            (log,                             ('2.6 - 3.2: Sunna BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f051c211', 'Sunna.BodyA.Diffuse.2048')),
        ],
        '4aca364a': [
            (log,                             ('2.6 - 3.2: Sunna BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3987c8c2', 'Sunna.BodyA.LightMap.1024')),
        ],
        '3987c8c2': [
            (log,                             ('2.6 - 3.2: Sunna BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4aca364a', 'Sunna.BodyA.LightMap.2048')),
        ],
        'f3f8895c': [
            (log,                             ('2.6 - 3.2: Sunna BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d459d73', 'Sunna.BodyA.MaterialMap.1024')),
        ],
        '1d459d73': [
            (log,                             ('2.6 - 3.2: Sunna BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b3c6ea5a', 'Sunna.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f3f8895c', 'Sunna.BodyA.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        '30ea5791': [
            (log,                             ('2.6 - 3.2: Sunna Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f0ab8cd': [
            (log,                             ('2.6 - 3.2: Sunna Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'a5182b8a': [
            (log,                             ('2.6 - 3.2: Sunna Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'e3cc1981': [
            (log,                             ('2.6 - 3.1: Sunna Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('fd41220d',)),
        ],
        'fd41220d': [
            (log,                             ('3.2: Sunna Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'f5daa764': [
            (log,                             ('2.6 - 3.2: Sunna Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'c9b5c6ce': [
            (log,                             ('2.6 - 3.2: Sunna EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ef66a60', 'Sunna.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1ef66a60', 'Sunna.FaceA.Diffuse.1024')),
        ],
        '1ef66a60': [
            (log,                             ('2.6 - 3.2: Sunna EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('30ea5791', 'Sunna.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c9b5c6ce', 'Sunna.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('c9b5c6ce', 'Sunna.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '1a2c8573': [
            (log,                             ('2.6 - 3.2: Sunna Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9679c257': [
            (log,                             ('2.6 - 3.2: Sunna Face Draw VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
        ],
        'ac6b5110': [
            (log,                             ('2.6 - 3.2: Sunna Face Position VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
        ],
        '506dc9e1': [
            (log,                             ('2.6 - 3.1: Sunna Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('f5ce8320',)),
        ],
        'f5ce8320': [
            (log,                             ('3.2: Sunna Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '21299f88': [
            (log,                             ('2.6 - 3.2: Sunna Face Blend VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'Sunna.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== DisplayScreen Component ====================
        '0b9bd38f': [
            (log,                             ('2.6 - 3.2: Sunna DisplayScreen IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dd676093': [
            (log,                             ('2.6 - 3.2: Sunna DisplayScreen Draw VB Hash',)),
            (add_section_if_missing,          ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
        ],
        '6f7ae47c': [
            (log,                             ('2.6 - 3.2: Sunna DisplayScreen Position VB Hash',)),
            (add_section_if_missing,          ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
        ],
        '541d5b0f': [
            (log,                             ('2.6 - 3.2: Sunna DisplayScreen Texcoord VB Hash',)),
            (add_section_if_missing,          ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
        ],
        '2ef8be58': [
            (log,                             ('2.6 - 3.2: Sunna DisplayScreen Blend VB Hash',)),
            (add_section_if_missing,          ('0b9bd38f', 'Sunna.DisplayScreen.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponBackpackCharmGrip Component ====================
        '337a62c1': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGrip IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '953975c0': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGrip Draw VB Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
        ],
        'a28ba31c': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGrip Position VB Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
        ],
        'b642db41': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGrip Texcoord VB Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
        ],
        '16e2d8ea': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGrip Blend VB Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
        ],
        '6c04b56d': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bde1bdad', 'Sunna.WeaponBackpackCharmGripA.Diffuse.1024')),
        ],
        'bde1bdad': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c04b56d', 'Sunna.WeaponBackpackCharmGripA.Diffuse.2048')),
        ],
        '39dac70b': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9368a6f9', 'Sunna.WeaponBackpackCharmGripA.LightMap.1024')),
        ],
        '9368a6f9': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('39dac70b', 'Sunna.WeaponBackpackCharmGripA.LightMap.2048')),
        ],
        '95070f7f': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('508c297c', 'Sunna.WeaponBackpackCharmGripA.MaterialMap.1024')),
        ],
        '508c297c': [
            (log,                             ('2.6 - 3.2: Sunna WeaponBackpackCharmGripA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('337a62c1', 'Sunna.WeaponBackpackCharmGrip.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95070f7f', 'Sunna.WeaponBackpackCharmGripA.MaterialMap.2048')),
        ],

        # ==================== paopao(战斗状态) Component ====================
        'e7a17172': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ffe207d5': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态) and paopao(非战斗状态) Draw VB Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        '3a7143a6': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态) Position VB Hash',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '62519e38': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态) Texcoord VB Hash',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '38e2fe9f': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态) Blend VB Hash',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
        ],
        '7d8ac131': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be5cd451', 'Sunna.paopao(战斗状态)A.Diffuse.1024')),
            (multiply_section_if_missing,     ('be5cd451', 'Sunna.paopao(非战斗状态)A.Diffuse.1024')),
        ],
        'be5cd451': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d8ac131', 'Sunna.paopao(战斗状态)A.Diffuse.2048')),
            (multiply_section_if_missing,     ('7d8ac131', 'Sunna.paopao(非战斗状态)A.Diffuse.2048')),
        ],
        '5c5b6aad': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('945afd67', 'Sunna.paopao(战斗状态)A.LightMap.1024')),
            (multiply_section_if_missing,     ('945afd67', 'Sunna.paopao(非战斗状态)A.LightMap.1024')),
        ],
        '945afd67': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5c5b6aad', 'Sunna.paopao(战斗状态)A.LightMap.2048')),
            (multiply_section_if_missing,     ('5c5b6aad', 'Sunna.paopao(非战斗状态)A.LightMap.2048')),
        ],
        '3c4378db': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e9783f84', 'Sunna.paopao(战斗状态)A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e9783f84', 'Sunna.paopao(非战斗状态)A.MaterialMap.1024')),
        ],
        'e9783f84': [
            (log,                             ('2.6 - 3.2: Sunna paopao(战斗状态)A and paopao(非战斗状态)A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e7a17172', 'Sunna.paopao(战斗状态).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3c4378db', 'Sunna.paopao(战斗状态)A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('3c4378db', 'Sunna.paopao(非战斗状态)A.MaterialMap.2048')),
        ],

        # ==================== paopao(非战斗状态) Component ====================
        '07a82c9c': [
            (log,                             ('2.6 - 3.2: Sunna paopao(非战斗状态) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1a0cad46': [
            (log,                             ('2.6 - 3.2: Sunna paopao(非战斗状态) Position VB Hash',)),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        'df0f6142': [
            (log,                             ('2.6 - 3.2: Sunna paopao(非战斗状态) Texcoord VB Hash',)),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
        ],
        'd4e13802': [
            (log,                             ('2.6 - 3.2: Sunna paopao(非战斗状态) Blend VB Hash',)),
            (add_section_if_missing,          ('07a82c9c', 'Sunna.paopao(非战斗状态).IB', 'match_priority = 0\n')),
        ],

        # ==================== Weapon Component ====================
        'c811c294': [
            (log,                             ('2.6 - 3.2: Sunna Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6cbdb4d3': [
            (log,                             ('2.6 - 3.2: Sunna Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        ],
        '9220fbd5': [
            (log,                             ('2.6 - 3.2: Sunna Weapon Position VB Hash',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        ],
        '5d7fdc2e': [
            (log,                             ('2.6 - 3.2: Sunna Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        ],
        '4b46dfdc': [
            (log,                             ('2.6 - 3.2: Sunna Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
        ],
        '003c6497': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9d9b7a7', 'Sunna.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b9d9b7a7', 'Sunna.WeaponDecorationA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b9d9b7a7', 'Sunna.WeaponDecoration2A.Diffuse.1024')),
        ],
        'b9d9b7a7': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('003c6497', 'Sunna.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('003c6497', 'Sunna.WeaponDecorationA.Diffuse.2048')),
            (multiply_section_if_missing,     ('003c6497', 'Sunna.WeaponDecoration2A.Diffuse.2048')),
        ],
        '4b4975a2': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c369f22', 'Sunna.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('6c369f22', 'Sunna.WeaponDecorationA.LightMap.1024')),
            (multiply_section_if_missing,     ('6c369f22', 'Sunna.WeaponDecoration2A.LightMap.1024')),
        ],
        '6c369f22': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4b4975a2', 'Sunna.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('4b4975a2', 'Sunna.WeaponDecorationA.LightMap.2048')),
            (multiply_section_if_missing,     ('4b4975a2', 'Sunna.WeaponDecoration2A.LightMap.2048')),
        ],
        '635f5cc9': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('15cd94f7', 'Sunna.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('15cd94f7', 'Sunna.WeaponDecorationA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('15cd94f7', 'Sunna.WeaponDecoration2A.MaterialMap.1024')),
        ],
        '15cd94f7': [
            (log,                             ('2.6 - 3.2: Sunna WeaponA, WeaponDecorationA and WeaponDecoration2A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('c811c294', 'Sunna.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('635f5cc9', 'Sunna.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('635f5cc9', 'Sunna.WeaponDecorationA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('635f5cc9', 'Sunna.WeaponDecoration2A.MaterialMap.2048')),
        ],

        # ==================== WeaponDecoration Component ====================
        '0a237cd3': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dab9d122': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration Draw VB Hash',)),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
        ],
        '0a41bae7': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration Position VB Hash',)),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
        ],
        '34dc63b4': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration Texcoord VB Hash',)),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
        ],
        'a5ecc7ea': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration Blend VB Hash',)),
            (add_section_if_missing,          ('0a237cd3', 'Sunna.WeaponDecoration.IB', 'match_priority = 0\n')),
        ],

        # ==================== WeaponDecoration2 Component ====================
        '8ad8f57d': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration2 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '84a9dfca': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration2 Draw VB Hash',)),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
        ],
        '81321ee9': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration2 Position VB Hash',)),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
        ],
        '33a66c47': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration2 Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
        ],
        '0d2178c5': [
            (log,                             ('2.6 - 3.2: Sunna WeaponDecoration2 Blend VB Hash',)),
            (add_section_if_missing,          ('8ad8f57d', 'Sunna.WeaponDecoration2.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Sunna',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
