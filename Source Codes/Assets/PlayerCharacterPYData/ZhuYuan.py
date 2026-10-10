"""
ZhuYuan Character Hash Commands
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
    Returns ZhuYuan's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '9821017e': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a3091843': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Draw VB Hash',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'd140d2e7': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Position VB Hash',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'f3c092c5': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
        ],
        'fdc045fc': [
            (log,                             ('1.1 -> 1.2: ZhuYuan Hair Texcoord Hash',)),
            (update_hash,                     ('f3c092c5',)),
            (log,                             ('+ Reverting texcoord buffer remap',)),
            (zzz_12_shrink_texcoord_color,    ('1.2',)),
        ],
        '9d35aee2': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Blend VB Hash',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
        ],
        '7f823598': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9b86c2f6', 'ZhuYuan.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9b86c2f6', 'ZhuYuan.ExtrasA.Diffuse.1024')),
        ],
        '9b86c2f6': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7f823598', 'ZhuYuan.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('7f823598', 'ZhuYuan.ExtrasA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA, BodyA, ShoulderAmmoA, ExtrasA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 枪身B, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身A, weapon - 变形前 - 枪身B, weapon - 变形前 - e技能增幅器A and weapon - 变形前 - e技能增幅器B NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', '6eb346b9'), 'ZhuYuan.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', 'd5b175bf'), 'ZhuYuan.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '0fda74c3'), 'ZhuYuan.ShoulderAmmoA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '6eb346b9'), 'ZhuYuan.ExtrasA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '0fda74c3'), 'ZhuYuan.ExtrasB.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '0fda74c3'), 'ZhuYuan.HipAmmoA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形后 - 枪身A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形后 - 枪身B.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 枪把A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 枪变形用卡扣A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 枪变形用卡扣B.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形前 - 枪身A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形前 - 枪身B.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.NormalMap.1024')),
        ],
        '4ac1defe': [
            (log,                             ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA, BodyA, ShoulderAmmoA, ExtrasA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 枪身B, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身A, weapon - 变形前 - 枪身B, weapon - 变形前 - e技能增幅器A and weapon - 变形前 - e技能增幅器B NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '4ac1defe'), 'ZhuYuan.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', 'd81fb56e'), 'ZhuYuan.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', 'fb35b7e9'), 'ZhuYuan.ShoulderAmmoA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '4ac1defe'), 'ZhuYuan.ExtrasA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', 'fb35b7e9'), 'ZhuYuan.ExtrasB.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', 'fb35b7e9'), 'ZhuYuan.HipAmmoA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形后 - 枪身A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形后 - 枪身B.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 枪把A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 枪变形用卡扣A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 枪变形用卡扣B.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形前 - 枪身A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形前 - 枪身B.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.NormalMap.2048')),
        ],
        '6eb346b9': [
            (log,                             ('1.0 -> 1.2: ZhuYuan HairA, ExtrasA NormalMap 1024p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'd4ee59c7': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8955095f', 'ZhuYuan.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('8955095f', 'ZhuYuan.ExtrasA.LightMap.1024')),
        ],
        '8955095f': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4ee59c7', 'ZhuYuan.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('d4ee59c7', 'ZhuYuan.ExtrasA.LightMap.2048')),
        ],
        '12a407b1': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d884663', 'ZhuYuan.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7d884663', 'ZhuYuan.ExtrasA.MaterialMap.1024')),
        ],
        '7d884663': [
            (log,                             ('2.2 - 3.2: ZhuYuan HairA and ExtrasA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('9821017e', 'ZhuYuan.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('12a407b1', 'ZhuYuan.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('12a407b1', 'ZhuYuan.ExtrasA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'fb69fc45': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '72411765': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '35b94ea8': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'aecf6710': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '527b317a': [
            (log,                             ('2.2 - 3.2: ZhuYuan Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('fb69fc45', 'ZhuYuan.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '6619364f': [
            (log,                             ('2.2 - 3.2: ZhuYuan Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a4aeb1d5': [
            (log,                             ('1.0 -> 1.1: ZhuYuan Body IB Hash',)),
            (update_hash,                     ('6619364f',)),
        ],
        '291f7f5a': [
            (log,                             ('2.2 - 3.2: ZhuYuan Body Draw VB Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        ],
        'f595d24d': [
            (log,                             ('2.2 - 3.2: ZhuYuan Body Position VB Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        ],
        'f3569f8d': [
            (log,                             ('1.0 -> 1.1: ZhuYuan Body Position Hash',)),
            (update_hash,                     ('f595d24d',)),
        ],
        'cb885260': [
            (log,                             ('2.2 - 3.2: ZhuYuan Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        ],
        '160872c0': [
            (log,                             ('1.0 -> 1.1: ZhuYuan Body Texcoord Hash',)),
            (update_hash,                     ('cb885260',)),
        ],
        '01e0c8d9': [
            (log,                             ('2.2 - 3.2: ZhuYuan Body Blend VB Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
        ],
        '5e942526': [
            (log,                             ('1.0 -> 1.1: ZhuYuan Body Blend Hash',)),
            (update_hash,                     ('01e0c8d9',)),
        ],
        'a271e894': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('46af14f8', 'f6795718', 'b57a8744'), 'ZhuYuan.BodyA.Diffuse.1024')),
        ],
        'c88e7660': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('3ef82f41',)),
        ],
        '3ef82f41': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 2048p Hash',)),
            (update_hash,                     ('a271e894',)),
        ],
        '46af14f8': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a271e894', '3ef82f41', 'c88e7660'), 'ZhuYuan.BodyA.Diffuse.2048')),
        ],
        'b57a8744': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('f6795718',)),
        ],
        'f6795718': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA Diffuse 1024p Hash',)),
            (update_hash,                     ('46af14f8',)),
        ],
        'a396c53a': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('7195a311',)),
        ],
        '7195a311': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('d81fb56e',)),
        ],
        'd81fb56e': [
            (log,                             ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '833bafd5': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('729ea75a',)),
        ],
        '729ea75a': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('d5b175bf',)),
        ],
        'd5b175bf': [
            (log,                             ('1.2 -> 2.5: ZhuYuan BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'd02bc66c': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('fb385169', '14b638b6', '18d00ac6'), 'ZhuYuan.BodyA.LightMap.1024')),
        ],
        '13a38449': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('80ebf536',)),
        ],
        '80ebf536': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('d02bc66c',)),
        ],
        'fb385169': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d02bc66c', '80ebf536', '13a38449'), 'ZhuYuan.BodyA.LightMap.2048')),
        ],
        '18d00ac6': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('14b638b6',)),
        ],
        '14b638b6': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('fb385169',)),
        ],
        '3e808ef6': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('29e2ebc5', 'cd4dee2c', '1daa379f'), 'ZhuYuan.BodyA.MaterialMap.1024')),
        ],
        'b4e20235': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('10415de8',)),
        ],
        '10415de8': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('3e808ef6',)),
        ],
        '29e2ebc5': [
            (log,                             ('2.2 - 3.2: ZhuYuan BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6619364f', 'ZhuYuan.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('3e808ef6', '10415de8', 'b4e20235'), 'ZhuYuan.BodyA.MaterialMap.2048')),
        ],
        '1daa379f': [
            (log,                             ('1.0 -> 1.1: ZhuYuan BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('cd4dee2c',)),
        ],
        'cd4dee2c': [
            (log,                             ('1.1 -> 1.2: ZhuYuan BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('29e2ebc5',)),
        ],

        # ==================== ShoulderAmmo Component ====================
        '5e717358': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmo IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dd91b126': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmo Draw VB Hash',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
        ],
        'd55c7763': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmo Position VB Hash',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
        ],
        '1c68a02f': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmo Texcoord VB Hash',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
        ],
        'e6fca033': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmo Blend VB Hash',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
        ],
        '6a33b25e': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.ShoulderAmmoA.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.ExtrasB.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.HipAmmoA.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 变形后 - 枪身A.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 枪变形用卡扣B.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 变形前 - 枪身B.Diffuse.1024')),
            (multiply_section_if_missing,     ('222ae5ee', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.Diffuse.1024')),
        ],
        '222ae5ee': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.ShoulderAmmoA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.ExtrasB.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.HipAmmoA.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 变形后 - 枪身A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 枪变形用卡扣B.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 变形前 - 枪身B.Diffuse.2048')),
            (multiply_section_if_missing,     ('6a33b25e', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.Diffuse.2048')),
        ],
        'fb35b7e9': [
            (log,                             ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '0fda74c3': [
            (log,                             ('1.0 -> 1.2: ZhuYuan ExtrasB, ShoulderAmmoA, HipAmmoA NormalMap 1024p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'e30f025b': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.ShoulderAmmoA.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.ExtrasB.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.HipAmmoA.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 变形后 - 枪身A.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 枪变形用卡扣B.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 变形前 - 枪身B.LightMap.1024')),
            (multiply_section_if_missing,     ('790183b4', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.LightMap.1024')),
        ],
        '790183b4': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.ShoulderAmmoA.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.ExtrasB.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.HipAmmoA.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 变形后 - 枪身A.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 枪变形用卡扣B.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 变形前 - 枪身B.LightMap.2048')),
            (multiply_section_if_missing,     ('e30f025b', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.LightMap.2048')),
        ],
        '58d5c840': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.ShoulderAmmoA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.ExtrasB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.HipAmmoA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 变形后 - 枪身A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 枪变形用卡扣B.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 变形前 - 枪身B.MaterialMap.1024')),
            (multiply_section_if_missing,     ('84842409', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.MaterialMap.1024')),
        ],
        '84842409': [
            (log,                             ('2.2 - 3.2: ZhuYuan ShoulderAmmoA, ExtrasB, HipAmmoA, weapon - 变形后 - 枪身A, weapon - 变形后 - 霰弹发射器A, weapon - 变形后 - 中间组合部件A, weapon - 枪变形用卡扣B, weapon - 变形前 - 枪身B and weapon - 变形前 - e技能增幅器A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5e717358', 'ZhuYuan.ShoulderAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.ShoulderAmmoA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.ExtrasB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.HipAmmoA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 变形后 - 枪身A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 变形后 - 霰弹发射器A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 变形后 - 中间组合部件A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 枪变形用卡扣B.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 变形前 - 枪身B.MaterialMap.2048')),
            (multiply_section_if_missing,     ('58d5c840', 'ZhuYuan.weapon - 变形前 - e技能增幅器A.MaterialMap.2048')),
        ],

        # ==================== Extras Component ====================
        'fcac8411': [
            (log,                             ('2.2 - 3.2: ZhuYuan Extras IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '52e3c65f': [
            (log,                             ('2.2 - 3.2: ZhuYuan Extras Draw VB Hash',)),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
        ],
        '5f445c20': [
            (log,                             ('2.2 - 3.2: ZhuYuan Extras Position VB Hash',)),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
        ],
        'ac21fba4': [
            (log,                             ('2.2 - 3.2: ZhuYuan Extras Texcoord VB Hash',)),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
        ],
        '0f5035dd': [
            (log,                             ('2.2 - 3.2: ZhuYuan Extras Blend VB Hash',)),
            (add_section_if_missing,          ('fcac8411', 'ZhuYuan.Extras.IB', 'match_priority = 0\n')),
        ],

        # ==================== HipAmmo Component ====================
        'a63028ae': [
            (log,                             ('2.2 - 3.2: ZhuYuan HipAmmo IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '82889576': [
            (log,                             ('2.2 - 3.2: ZhuYuan HipAmmo Draw VB Hash',)),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
        ],
        '45d265c0': [
            (log,                             ('2.2 - 3.2: ZhuYuan HipAmmo Position VB Hash',)),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
        ],
        '75c5e659': [
            (log,                             ('2.2 - 3.2: ZhuYuan HipAmmo Texcoord VB Hash',)),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
        ],
        '9a268159': [
            (log,                             ('2.2 - 3.2: ZhuYuan HipAmmo Blend VB Hash',)),
            (add_section_if_missing,          ('a63028ae', 'ZhuYuan.HipAmmo.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        'f1c241b7': [
            (log,                             ('2.2 - 3.2: ZhuYuan Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '33e6da2d': [
            (log,                             ('2.2 - 3.2: ZhuYuan Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
        ],
        '09f4496a': [
            (log,                             ('2.2 - 3.2: ZhuYuan Face Position VB Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
        ],
        '0c6f696b': [
            (log,                             ('2.2 - 3.1: ZhuYuan Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('cc9f6187',)),
        ],
        'cc9f6187': [
            (log,                             ('3.2: ZhuYuan Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '6c9ffbbf': [
            (log,                             ('2.2 - 3.2: ZhuYuan Face Blend VB Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
        ],
        'a1eabb9f': [
            (log,                             ('2.2 - 3.2: ZhuYuan FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('138c7d76', 'ZhuYuan.FaceA.Diffuse.1024')),
        ],
        '138c7d76': [
            (log,                             ('2.2 - 3.2: ZhuYuan FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f1c241b7', 'ZhuYuan.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a1eabb9f', 'ZhuYuan.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 变形后 - 枪身 Component ====================
        'a9188e3c': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1756495e': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
        ],
        '04a00393': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身 Position VB Hash',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
        ],
        '8bade376': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
        ],
        '9d99178a': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身 Blend VB Hash',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
        ],
        '1747290f': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5ce66b3f', 'ZhuYuan.weapon - 变形后 - 枪身B.Diffuse.1024')),
            (multiply_section_if_missing,     ('5ce66b3f', 'ZhuYuan.weapon - 枪把A.Diffuse.1024')),
            (multiply_section_if_missing,     ('5ce66b3f', 'ZhuYuan.weapon - 枪变形用卡扣A.Diffuse.1024')),
            (multiply_section_if_missing,     ('5ce66b3f', 'ZhuYuan.weapon - 变形前 - 枪身A.Diffuse.1024')),
            (multiply_section_if_missing,     ('5ce66b3f', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.Diffuse.1024')),
        ],
        '5ce66b3f': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1747290f', 'ZhuYuan.weapon - 变形后 - 枪身B.Diffuse.2048')),
            (multiply_section_if_missing,     ('1747290f', 'ZhuYuan.weapon - 枪把A.Diffuse.2048')),
            (multiply_section_if_missing,     ('1747290f', 'ZhuYuan.weapon - 枪变形用卡扣A.Diffuse.2048')),
            (multiply_section_if_missing,     ('1747290f', 'ZhuYuan.weapon - 变形前 - 枪身A.Diffuse.2048')),
            (multiply_section_if_missing,     ('1747290f', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.Diffuse.2048')),
        ],
        '84de8345': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('51280394', 'ZhuYuan.weapon - 变形后 - 枪身B.LightMap.1024')),
            (multiply_section_if_missing,     ('51280394', 'ZhuYuan.weapon - 枪把A.LightMap.1024')),
            (multiply_section_if_missing,     ('51280394', 'ZhuYuan.weapon - 枪变形用卡扣A.LightMap.1024')),
            (multiply_section_if_missing,     ('51280394', 'ZhuYuan.weapon - 变形前 - 枪身A.LightMap.1024')),
            (multiply_section_if_missing,     ('51280394', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.LightMap.1024')),
        ],
        '51280394': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('84de8345', 'ZhuYuan.weapon - 变形后 - 枪身B.LightMap.2048')),
            (multiply_section_if_missing,     ('84de8345', 'ZhuYuan.weapon - 枪把A.LightMap.2048')),
            (multiply_section_if_missing,     ('84de8345', 'ZhuYuan.weapon - 枪变形用卡扣A.LightMap.2048')),
            (multiply_section_if_missing,     ('84de8345', 'ZhuYuan.weapon - 变形前 - 枪身A.LightMap.2048')),
            (multiply_section_if_missing,     ('84de8345', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.LightMap.2048')),
        ],
        '852f5de0': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2a06612e', 'ZhuYuan.weapon - 变形后 - 枪身B.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2a06612e', 'ZhuYuan.weapon - 枪把A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2a06612e', 'ZhuYuan.weapon - 枪变形用卡扣A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2a06612e', 'ZhuYuan.weapon - 变形前 - 枪身A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2a06612e', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.MaterialMap.1024')),
        ],
        '2a06612e': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 枪身B, weapon - 枪把A, weapon - 枪变形用卡扣A, weapon - 变形前 - 枪身A and weapon - 变形前 - e技能增幅器B MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a9188e3c', 'ZhuYuan.weapon - 变形后 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('852f5de0', 'ZhuYuan.weapon - 变形后 - 枪身B.MaterialMap.2048')),
            (multiply_section_if_missing,     ('852f5de0', 'ZhuYuan.weapon - 枪把A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('852f5de0', 'ZhuYuan.weapon - 枪变形用卡扣A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('852f5de0', 'ZhuYuan.weapon - 变形前 - 枪身A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('852f5de0', 'ZhuYuan.weapon - 变形前 - e技能增幅器B.MaterialMap.2048')),
        ],

        # ==================== weapon - 变形后 - 霰弹发射器 Component ====================
        'a7f00ae5': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 霰弹发射器 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd853623a': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 霰弹发射器 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
        ],
        '49c9bbf7': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 霰弹发射器 Position VB Hash',)),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
        ],
        'e03ad35f': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 霰弹发射器 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
        ],
        '0e291903': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 霰弹发射器 Blend VB Hash',)),
            (add_section_if_missing,          ('a7f00ae5', 'ZhuYuan.weapon - 变形后 - 霰弹发射器.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 变形后 - 中间组合部件 Component ====================
        'd19a5cd0': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 中间组合部件 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7ae1f70f': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 中间组合部件 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
        ],
        '53738d91': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 中间组合部件 Position VB Hash',)),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
        ],
        'c03acfb5': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 中间组合部件 Texcoord VB Hash',)),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
        ],
        '8f4f2e30': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形后 - 中间组合部件 Blend VB Hash',)),
            (add_section_if_missing,          ('d19a5cd0', 'ZhuYuan.weapon - 变形后 - 中间组合部件.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 枪把 Component ====================
        'db111545': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪把 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd04cc3dd': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪把 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
        ],
        'd3630839': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪把 Position VB Hash',)),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
        ],
        '3ffbf9b5': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪把 Texcoord VB Hash',)),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
        ],
        '32a33b84': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪把 Blend VB Hash',)),
            (add_section_if_missing,          ('db111545', 'ZhuYuan.weapon - 枪把.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 枪变形用卡扣 Component ====================
        'e5a92555': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪变形用卡扣 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3421e96d': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪变形用卡扣 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
        ],
        '7cab956b': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪变形用卡扣 Position VB Hash',)),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
        ],
        '61312746': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪变形用卡扣 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
        ],
        'c8e16aaf': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 枪变形用卡扣 Blend VB Hash',)),
            (add_section_if_missing,          ('e5a92555', 'ZhuYuan.weapon - 枪变形用卡扣.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 变形前 - 枪身 Component ====================
        'f8e6c967': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - 枪身 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7b103bdf': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - 枪身 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
        ],
        'e3e969f4': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - 枪身 Position VB Hash',)),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
        ],
        'a102d142': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - 枪身 Texcoord VB Hash',)),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
        ],
        'b0cda17f': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - 枪身 Blend VB Hash',)),
            (add_section_if_missing,          ('f8e6c967', 'ZhuYuan.weapon - 变形前 - 枪身.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 变形前 - e技能增幅器 Component ====================
        'e7263d9a': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - e技能增幅器 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b179d1e8': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - e技能增幅器 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
        ],
        'c84557c0': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - e技能增幅器 Position VB Hash',)),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
        ],
        'b7ad2492': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - e技能增幅器 Texcoord VB Hash',)),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
        ],
        '93d2f31a': [
            (log,                             ('2.2 - 3.2: ZhuYuan weapon - 变形前 - e技能增幅器 Blend VB Hash',)),
            (add_section_if_missing,          ('e7263d9a', 'ZhuYuan.weapon - 变形前 - e技能增幅器.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ZhuYuan',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
