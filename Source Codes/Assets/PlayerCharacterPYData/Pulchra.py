"""
Pulchra Character Hash Commands
ZZZ Mod Fixer v2.2
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
    Returns Pulchra's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Shadow Component ====================
        '243cdff6': [
            (log,                             ('2.2 - 3.2: Pulchra Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '096ad3f4': [
            (log,                             ('2.2 - 3.2: Pulchra Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '3dba047b': [
            (log,                             ('2.2 - 3.2: Pulchra Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '09fcf321': [
            (log,                             ('2.2 - 3.2: Pulchra Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '6b643cdd': [
            (log,                             ('2.2 - 3.2: Pulchra Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('243cdff6', 'Pulchra.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no textures in any database version.

        # ==================== Mask Component ====================
        '5b30f4da': [
            (log,                             ('2.2 - 3.2: Pulchra Mask IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '992028e7': [
            (log,                             ('2.2 - 3.2: Pulchra Mask Draw VB Hash',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        ],
        'eed9f960': [
            (log,                             ('2.2 - 3.2: Pulchra Mask Position VB Hash',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        ],
        '0e117b28': [
            (log,                             ('2.2 - 3.2: Pulchra Mask Texcoord VB Hash',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        ],
        '0db288cb': [
            (log,                             ('2.2 - 3.2: Pulchra Mask Blend VB Hash',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        ],
        '46bab365': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('128c8f2e', 'Pulchra.MaskA.Diffuse.1024')),
            (multiply_section_if_missing,     ('128c8f2e', 'Pulchra.weapon - 左手A.Diffuse.1024')),
            (multiply_section_if_missing,     ('128c8f2e', 'Pulchra.weapon - 右手A.Diffuse.1024')),
        ],
        '128c8f2e': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('46bab365', 'Pulchra.MaskA.Diffuse.2048')),
            (multiply_section_if_missing,     ('46bab365', 'Pulchra.weapon - 左手A.Diffuse.2048')),
            (multiply_section_if_missing,     ('46bab365', 'Pulchra.weapon - 右手A.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, BodyA, BodyB, weapon - 左手A and weapon - 右手A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.MaskA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.weapon - 左手A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.weapon - 右手A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, BodyA, BodyB, weapon - 左手A and weapon - 右手A NormalMap 1024p Hash, also Waist supply and Wrist supply NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Pulchra.MaskA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pulchra.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pulchra.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pulchra.weapon - 左手A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Pulchra.weapon - 右手A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Pulchra.Waist supplyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Pulchra.Wrist supplyA.NormalMap.1024')),
        ],
        '03d28ecd': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e522177c', 'Pulchra.MaskA.LightMap.1024')),
            (multiply_section_if_missing,     ('e522177c', 'Pulchra.weapon - 左手A.LightMap.1024')),
            (multiply_section_if_missing,     ('e522177c', 'Pulchra.weapon - 右手A.LightMap.1024')),
        ],
        'e522177c': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('03d28ecd', 'Pulchra.MaskA.LightMap.2048')),
            (multiply_section_if_missing,     ('03d28ecd', 'Pulchra.weapon - 左手A.LightMap.2048')),
            (multiply_section_if_missing,     ('03d28ecd', 'Pulchra.weapon - 右手A.LightMap.2048')),
        ],
        '6b141146': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f1ee6734', '820ded20'), 'Pulchra.MaskA.MaterialMap.1024')),
            (multiply_section_if_missing,     (('f1ee6734', '820ded20'), 'Pulchra.weapon - 左手A.MaterialMap.1024')),
            (multiply_section_if_missing,     (('f1ee6734', '820ded20'), 'Pulchra.weapon - 右手A.MaterialMap.1024')),
        ],
        '320a1179': [
            (log,                             ('2.5: Pulchra MaskA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
        ],
        '820ded20': [
            (log,                             ('1.7 -> 2.0: Pulchra MaskA MaterialMap 1024p Hash',)),
            (update_hash,                     ('f1ee6734',)),
        ],
        'f1ee6734': [
            (log,                             ('2.2 - 3.2: Pulchra MaskA, weapon - 左手A and weapon - 右手A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('5b30f4da', 'Pulchra.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5b644956', 'Pulchra.weapon - 左手.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bfc94dff', 'Pulchra.weapon - 右手.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('6b141146', '320a1179'), 'Pulchra.MaskA.MaterialMap.2048')),
            (multiply_section_if_missing,     (('6b141146', '320a1179'), 'Pulchra.weapon - 左手A.MaterialMap.2048')),
            (multiply_section_if_missing,     (('6b141146', '320a1179'), 'Pulchra.weapon - 右手A.MaterialMap.2048')),
        ],

        # ==================== Body Component ====================
        'bd385763': [
            (log,                             ('2.2 - 3.2: Pulchra Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2be39a26': [
            (log,                             ('2.2 - 3.2: Pulchra Body Draw VB Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        ],
        'a74c8d89': [
            (log,                             ('2.2 - 3.2: Pulchra Body Position VB Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        ],
        '5204f58d': [
            (log,                             ('2.2 - 3.2: Pulchra Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        ],
        '9381fa0b': [
            (log,                             ('2.2 - 3.2: Pulchra Body Blend VB Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
        ],
        '7fc03353': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf7eba0f', 'Pulchra.BodyA.Diffuse.1024')),
        ],
        'bf7eba0f': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7fc03353', 'Pulchra.BodyA.Diffuse.2048')),
        ],
        'd8462af0': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('47040200', 'Pulchra.BodyA.LightMap.1024')),
        ],
        '47040200': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d8462af0', 'Pulchra.BodyA.LightMap.2048')),
        ],
        'd404b789': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a66a11d0', 'Pulchra.BodyA.MaterialMap.1024')),
        ],
        'a66a11d0': [
            (log,                             ('2.2 - 3.2: Pulchra BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d404b789', 'Pulchra.BodyA.MaterialMap.2048')),
        ],
        '57be79d6': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb0a816a', 'Pulchra.BodyB.Diffuse.1024')),
        ],
        'fb0a816a': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57be79d6', 'Pulchra.BodyB.Diffuse.2048')),
        ],
        '12c44063': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f475e822', 'Pulchra.BodyB.LightMap.1024')),
        ],
        'f475e822': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('12c44063', 'Pulchra.BodyB.LightMap.2048')),
        ],
        'a553df20': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('64d75415', 'Pulchra.BodyB.MaterialMap.1024')),
        ],
        '64d75415': [
            (log,                             ('2.2 - 3.2: Pulchra BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('bd385763', 'Pulchra.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a553df20', 'Pulchra.BodyB.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Mask; see that Component above.

        # ==================== Waist supply Component ====================
        '425a7565': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supply IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ec497419': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supply Draw VB Hash',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
        ],
        '5391a870': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supply Blend VB Hash',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
        ],
        'ebd6c100': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cae1373a', 'Pulchra.Waist supplyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('cae1373a', 'Pulchra.Wrist supplyA.Diffuse.1024')),
        ],
        'cae1373a': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebd6c100', 'Pulchra.Waist supplyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ebd6c100', 'Pulchra.Wrist supplyA.Diffuse.2048')),
        ],
        'ffdc1ea7': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.Waist supplyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('798adba3', 'Pulchra.Wrist supplyA.NormalMap.2048')),
        ],
        '6f17d782': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f23d32e1', 'Pulchra.Waist supplyA.LightMap.1024')),
            (multiply_section_if_missing,     ('f23d32e1', 'Pulchra.Wrist supplyA.LightMap.1024')),
        ],
        'f23d32e1': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f17d782', 'Pulchra.Waist supplyA.LightMap.2048')),
            (multiply_section_if_missing,     ('6f17d782', 'Pulchra.Wrist supplyA.LightMap.2048')),
        ],
        'b8e1e3f6': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ea60b10', 'Pulchra.Waist supplyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('9ea60b10', 'Pulchra.Wrist supplyA.MaterialMap.1024')),
        ],
        '9ea60b10': [
            (log,                             ('2.2 - 3.2: Pulchra Waist supplyA and Wrist supplyA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('425a7565', 'Pulchra.Waist supply.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8e1e3f6', 'Pulchra.Waist supplyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b8e1e3f6', 'Pulchra.Wrist supplyA.MaterialMap.2048')),
        ],
        # Waist supply has no Position and no Texcoord VB hashes in any database version and shares its NormalMap hashes with Mask; see that Component above.

        # ==================== Wrist supply Component ====================
        '96cb7dc9': [
            (log,                             ('2.2 - 3.2: Pulchra Wrist supply IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '29a6299d': [
            (log,                             ('2.2 - 3.2: Pulchra Wrist supply Draw VB Hash',)),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
        ],
        '8329562b': [
            (log,                             ('2.2 - 3.2: Pulchra Wrist supply Position VB Hash',)),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
        ],
        'caa1f21c': [
            (log,                             ('2.2 - 3.2: Pulchra Wrist supply Texcoord VB Hash',)),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
        ],
        '55119041': [
            (log,                             ('2.2 - 3.2: Pulchra Wrist supply Blend VB Hash',)),
            (add_section_if_missing,          ('96cb7dc9', 'Pulchra.Wrist supply.IB', 'match_priority = 0\n')),
        ],
        # Wrist supply shares its Diffuse, LightMap and MaterialMap hashes with Waist supply and its NormalMap hashes with Mask; see those Components above.

        # ==================== Face Component ====================
        '62de5837': [
            (log,                             ('2.2 - 3.2: Pulchra Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd704bf57': [
            (log,                             ('2.2 - 3.2: Pulchra Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        ],
        'ed162c10': [
            (log,                             ('2.2 - 3.2: Pulchra Face Position VB Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        ],
        '2a29bb4e': [
            (log,                             ('2.2 - 3.1: Pulchra Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('75302f6a',)),
        ],
        '75302f6a': [
            (log,                             ('3.2: Pulchra Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7e443147': [
            (log,                             ('2.2 - 3.2: Pulchra Face Blend VB Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
        ],
        '1626aafe': [
            (log,                             ('2.2 - 3.2: Pulchra FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('32f923f1', 'Pulchra.FaceA.Diffuse.1024')),
        ],
        '32f923f1': [
            (log,                             ('2.2 - 3.2: Pulchra FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('62de5837', 'Pulchra.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1626aafe', 'Pulchra.FaceA.Diffuse.2048')),
        ],
        # Face has two identical Diffuse entries in its single object group and no other textures in any database version.

        # ==================== weapon - 左手 Component ====================
        '5b644956': [
            (log,                             ('2.2 - 3.2: Pulchra weapon - 左手 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # weapon - 左手 has no VB hashes in any database version and shares its textures with Mask; see that Component above.

        # ==================== weapon - 右手 Component ====================
        'bfc94dff': [
            (log,                             ('2.2 - 3.2: Pulchra weapon - 右手 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # weapon - 右手 has no VB hashes in any database version and shares its textures with Mask; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Pulchra',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
