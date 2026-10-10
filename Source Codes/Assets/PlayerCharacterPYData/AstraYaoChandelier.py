"""
AstraYaoChandelier Character Hash Commands
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
    Returns AstraYaoChandelier's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '53cdac6c': [
            (log,                             ('1.5: AstraYaoChandelier Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd3c951b9': [
            (log,                             ('2.2: AstraYaoChandelier Hair Draw VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
        ],
        'ee3c305a': [
            (log,                             ('2.2: AstraYaoChandelier Hair Position VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
        ],
        '8ba0b335': [
            (log,                             ('1.6: AstraYaoChandelier Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
        ],
        'c3c08f85': [
            (log,                             ('2.2: AstraYaoChandelier Hair Blend VB Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
        ],
        'e634238a': [
            (log,                             ('1.6: AstraYaoChandelier HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('56c71ea2', 'AstraYaoChandelier.HairA.Diffuse.1024')),
        ],
        '56c71ea2': [
            (log,                             ('1.6: AstraYaoChandelier HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e634238a', 'AstraYaoChandelier.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2: AstraYaoChandelier HairA, BodyA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYaoChandelier.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYaoChandelier.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYaoChandelier.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AstraYaoChandelier.WeaponB.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2: AstraYaoChandelier HairA, BodyA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYaoChandelier.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYaoChandelier.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYaoChandelier.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AstraYaoChandelier.WeaponB.NormalMap.2048')),
        ],
        '34f0706c': [
            (log,                             ('1.6: AstraYaoChandelier HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fd3ca2a6', 'AstraYaoChandelier.HairA.LightMap.1024')),
        ],
        'fd3ca2a6': [
            (log,                             ('1.6: AstraYaoChandelier HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34f0706c', 'AstraYaoChandelier.HairA.LightMap.2048')),
        ],
        '883a578f': [
            (log,                             ('1.6: AstraYaoChandelier HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('759c15e0', 'AstraYaoChandelier.HairA.MaterialMap.1024')),
        ],
        '759c15e0': [
            (log,                             ('1.6: AstraYaoChandelier HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('883a578f', 'AstraYaoChandelier.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '93d55a49': [
            (log,                             ('2.2: AstraYaoChandelier Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5e1e12aa': [
            (log,                             ('2.2: AstraYaoChandelier Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a378328a': [
            (log,                             ('2.2: AstraYaoChandelier Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'c4456161': [
            (log,                             ('2.2: AstraYaoChandelier Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '81ef699b': [
            (log,                             ('2.2: AstraYaoChandelier Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '02d8a2cb': [
            (log,                             ('1.5: AstraYaoChandelier Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '645d075e': [
            (log,                             ('2.2: AstraYaoChandelier Body Draw VB Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        ],
        '43f58537': [
            (log,                             ('2.2: AstraYaoChandelier Body Position VB Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        ],
        'f1e37ebf': [
            (log,                             ('2.2: AstraYaoChandelier Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        ],
        'b72fadfc': [
            (log,                             ('2.2: AstraYaoChandelier Body Blend VB Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        ],
        '7301ca3a': [
            (log,                             ('1.5: AstraYaoChandelier BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8212713f', 'AstraYaoChandelier.BodyA.Diffuse.1024')),
        ],
        '8212713f': [
            (log,                             ('1.5: AstraYaoChandelier BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7301ca3a', 'AstraYaoChandelier.BodyA.Diffuse.2048')),
        ],
        '7ce9f1db': [
            (log,                             ('1.6 -> 2.0: AstraYaoChandelier BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('515f9beb',)),
        ],
        '515f9beb': [
            (log,                             ('1.5: AstraYaoChandelier BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cf8ecb3b', '83ede428'), 'AstraYaoChandelier.BodyA.LightMap.1024')),
        ],
        '83ede428': [
            (log,                             ('1.6 -> 2.0: AstraYaoChandelier BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('cf8ecb3b',)),
        ],
        'cf8ecb3b': [
            (log,                             ('1.5: AstraYaoChandelier BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('515f9beb', '7ce9f1db'), 'AstraYaoChandelier.BodyA.LightMap.2048')),
        ],
        '56abc3a3': [
            (log,                             ('1.5 -> 1.6: AstraYaoChandelier BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('43a4d256',)),
        ],
        '43a4d256': [
            (log,                             ('1.6 -> 2.0: AstraYaoChandelier BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('fa2f509f',)),
        ],
        'fa2f509f': [
            (log,                             ('2.0: AstraYaoChandelier BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('03df0be9', '6da1b76a', '6989dc5a'), 'AstraYaoChandelier.BodyA.MaterialMap.1024')),
        ],
        '6989dc5a': [
            (log,                             ('1.5 -> 1.6: AstraYaoChandelier BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('6da1b76a',)),
        ],
        '6da1b76a': [
            (log,                             ('1.6 -> 2.0: AstraYaoChandelier BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('03df0be9',)),
        ],
        '03df0be9': [
            (log,                             ('2.0: AstraYaoChandelier BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fa2f509f', '43a4d256', '56abc3a3'), 'AstraYaoChandelier.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '51831437': [
            (log,                             ('1.5: AstraYaoChandelier Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5c578f85': [
            (log,                             ('2.2: AstraYaoChandelier Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
        ],
        '66451cc2': [
            (log,                             ('2.2: AstraYaoChandelier Face Position VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
        ],
        'ffac76ac': [
            (log,                             ('2.2: AstraYaoChandelier Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('01b43c04',)),
        ],
        '01b43c04': [
            (log,                             ('3.2: AstraYaoChandelier Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7e05c11a': [
            (log,                             ('2.2: AstraYaoChandelier Face Blend VB Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
        ],
        'c41341b2': [
            (log,                             ('1.6: AstraYaoChandelier FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3283b8be', 'AstraYaoChandelier.FaceA.Diffuse.1024')),
        ],
        '3283b8be': [
            (log,                             ('1.6: AstraYaoChandelier FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c41341b2', 'AstraYaoChandelier.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 本体 Component ====================
        '702b018e': [
            (log,                             ('2.2: AstraYaoChandelier weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ca16b939': [
            (log,                             ('2.2: AstraYaoChandelier weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        '9879faf3': [
            (log,                             ('2.2: AstraYaoChandelier weapon Position VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        'b3e27d5f': [
            (log,                             ('2.2: AstraYaoChandelier weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        '4a4fb44e': [
            (log,                             ('2.2: AstraYaoChandelier weapon Blend VB Hash',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        'b5a20274': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d652aa31', 'AstraYaoChandelier.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('d652aa31', 'AstraYaoChandelier.WeaponB.Diffuse.1024')),
        ],
        'd652aa31': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b5a20274', 'AstraYaoChandelier.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('b5a20274', 'AstraYaoChandelier.WeaponB.Diffuse.2048')),
        ],
        '57c44e60': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91c63955', 'AstraYaoChandelier.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('91c63955', 'AstraYaoChandelier.WeaponB.LightMap.1024')),
        ],
        '91c63955': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57c44e60', 'AstraYaoChandelier.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('57c44e60', 'AstraYaoChandelier.WeaponB.LightMap.2048')),
        ],
        'fdb82c44': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('98e011bc', 'AstraYaoChandelier.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('98e011bc', 'AstraYaoChandelier.WeaponB.MaterialMap.1024')),
        ],
        '98e011bc': [
            (log,                             ('2.2: AstraYaoChandelier WeaponA and WeaponB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fdb82c44', 'AstraYaoChandelier.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('fdb82c44', 'AstraYaoChandelier.WeaponB.MaterialMap.2048')),
        ],

        # ==================== Weapon - 唱片 Component ====================
        'f4f5348d': [
            (log,                             ('2.2: AstraYaoChandelier weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7ed93255': [
            (log,                             ('2.2: AstraYaoChandelier weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        'b8a9ba2e': [
            (log,                             ('2.2: AstraYaoChandelier weapon Position VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        'd6d5743e': [
            (log,                             ('2.2: AstraYaoChandelier weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
        'cb9405e1': [
            (log,                             ('2.2: AstraYaoChandelier weapon Blend VB Hash',)),
            (add_section_if_missing,          ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AstraYaoChandelier',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}