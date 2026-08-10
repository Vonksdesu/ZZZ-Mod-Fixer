"""
AstraYaoChandelier Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 1.5 - 2.5
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
'53cdac6c': [(log, ('2.5: AstraYaoChandelier Hair IB Hash',)), (add_ib_check_if_missing,)],
'e634238a': [
        (log,                           ('2.5: AstraYaoChandelier HairA Diffuse Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: AstraYaoChandelier Hair/Body NormalMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'34f0706c': [
        (log,                           ('2.5: AstraYaoChandelier HairA LightMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'883a578f': [
        (log,                           ('2.5: AstraYaoChandelier HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],

# ==================== Body Component ====================
'02d8a2cb': [(log, ('1.5 - 2.5: AstraYaoChandelier Body IB Hash',)), (add_ib_check_if_missing,)],
'7301ca3a': [
        (log,                           ('1.5 - 2.5: AstraYaoChandelier BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8212713f', 'AstraYaoChandelier.BodyA.Diffuse.1024')),
    ],

'8212713f': [
        (log,                           ('1.5 - 2.5: AstraYaoChandelier BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7301ca3a', 'AstraYaoChandelier.BodyA.Diffuse.2048')),
    ],
# Note: ebac056e NormalMap is shared with Hair component above
'7ce9f1db': [(log, ('1.5 -> 2.5: AstraYaoChandelier BodyA LightMap Hash',)),   (update_hash, ('515f9beb',))],
'515f9beb': [
        (log,                           ('2.5: AstraYaoChandelier BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('83ede428', 'cf8ecb3b'), 'AstraYaoChandelier.BodyA.LightMap.1024')),
    ],

'83ede428': [(log, ('1.6 -> 2.0: AstraSkin BodyA LightMap 1024p Hash',)), (update_hash, ('cf8ecb3b',))],
'cf8ecb3b': [
        (log,                           ('2.5: AstraYaoChandelier BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('7ce9f1db', '515f9beb'), 'AstraYaoChandelier.BodyA.LightMap.2048')),
    ],
'56abc3a3': [(log, ('1.5 -> 1.6: AstraYaoChandelier BodyA MaterialMap Hash',)),   (update_hash, ('43a4d256',))],
'43a4d256': [(log, ('1.6 -> 2.5: AstraYaoChandelier BodyA MaterialMap Hash',)),   (update_hash, ('fa2f509f',))],
'fa2f509f': [
        (log,                           ('2.5: AstraYaoChandelier BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('6da1b76a', '6989dc5a', '03df0be9'), 'AstraYaoChandelier.BodyA.MaterialMap.1024')),
    ],

'6989dc5a': [(log, ('1.5 -> 1.6: AstraSkin BodyA MaterialMap 1024p Hash',)), (update_hash, ('6da1b76a',))],
'6da1b76a': [(log, ('1.6 -> 2.0: AstraSkin BodyA MaterialMap 1024p Hash',)), (update_hash, ('03df0be9',))],
'03df0be9': [
        (log,                           ('2.5: AstraYaoChandelier BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('43a4d256', '56abc3a3', 'fa2f509f'), 'AstraYaoChandelier.BodyA.MaterialMap.2048')),
    ],

# ==================== Face Component ====================
'51831437': [(log, ('2.5: AstraYaoChandelier Face IB Hash',)), (add_ib_check_if_missing,)],
'c41341b2': [
        (log,                           ('2.5: AstraYaoChandelier FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'ee3c305a': [
        (log, ('3.0: AstraYaoChandelier Hair VB Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'8ba0b335': [
        (log, ('3.0: AstraYaoChandelier Hair VB Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'c3c08f85': [
        (log, ('3.0: AstraYaoChandelier Hair VB Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'93d55a49': [(log, ('3.0: AstraYaoChandelier Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'5e1e12aa': [
        (log, ('3.0: AstraYaoChandelier Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a378328a': [
        (log, ('3.0: AstraYaoChandelier Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'c4456161': [
        (log, ('3.0: AstraYaoChandelier Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'81ef699b': [
        (log, ('3.0: AstraYaoChandelier Hair Shadow VB Hash',)),
        (add_section_if_missing, ('93d55a49', 'AstraYaoChandelier.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'43f58537': [
        (log, ('3.0: AstraYaoChandelier Body VB Hash',)),
        (add_section_if_missing, ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'f1e37ebf': [
        (log, ('3.0: AstraYaoChandelier Body VB Hash',)),
        (add_section_if_missing, ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'b72fadfc': [
        (log, ('3.0: AstraYaoChandelier Body VB Hash',)),
        (add_section_if_missing, ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
    ],
'ffac76ac': [
        (log, ('3.0: AstraYaoChandelier Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'7e05c11a': [
        (log, ('3.0: AstraYaoChandelier Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'702b018e': [(log, ('3.0: AstraYaoChandelier weapon IB Hash',)), (add_ib_check_if_missing,)],
'9879faf3': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'b3e27d5f': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'4a4fb44e': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'b5a20274': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'57c44e60': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'fdb82c44': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'f4f5348d': [(log, ('3.0: AstraYaoChandelier weapon IB Hash',)), (add_ib_check_if_missing,)],
'b8a9ba2e': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'd6d5743e': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'cb9405e1': [
        (log, ('3.0: AstraYaoChandelier weapon VB Hash',)),
        (add_section_if_missing, ('f4f5348d', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'5c578f85': [(log, ('3.0: AstraYaoChandelier misc hash',)),],
'7ed93255': [(log, ('3.0: AstraYaoChandelier misc hash',)),],
'ca16b939': [(log, ('3.0: AstraYaoChandelier misc hash',)),],
'd3c951b9': [
        (log, ('3.0: AstraYaoChandelier Hair VB Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'56c71ea2': [
        (log, ('3.0: AstraYaoChandelier Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: AstraYaoChandelier Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'fd3ca2a6': [
        (log, ('3.0: AstraYaoChandelier Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'759c15e0': [
        (log, ('3.0: AstraYaoChandelier Hair TEX Hash',)),
        (add_section_if_missing, ('53cdac6c', 'AstraYaoChandelier.Hair.IB', 'match_priority = 0\n')),
    ],
'3283b8be': [
        (log, ('3.0: AstraYaoChandelier Face TEX Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'd652aa31': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'91c63955': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'98e011bc': [
        (log, ('3.0: AstraYaoChandelier weapon TEX Hash',)),
        (add_section_if_missing, ('702b018e', 'AstraYaoChandelier.weapon.IB', 'match_priority = 0\n')),
    ],
'66451cc2': [
        (log, ('3.0: AstraYaoChandelier Face VB Hash',)),
        (add_section_if_missing, ('51831437', 'AstraYaoChandelier.Face.IB', 'match_priority = 0\n')),
    ],
'645d075e': [
        (log, ('3.0: AstraYaoChandelier Body VB Hash',)),
        (add_section_if_missing, ('02d8a2cb', 'AstraYaoChandelier.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AstraYaoChandelier',
    'game_versions': ['1.5', '1.6', '1.7', '2.5'],
}

