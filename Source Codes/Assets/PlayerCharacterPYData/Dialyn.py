"""
Dialyn Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.4 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Dialyn's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '68f00074': [
            (log,                             ('2.4 - 3.2: Dialyn Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '00e453e9': [
            (log,                             ('2.4 - 3.2: Dialyn Hair Draw VB Hash',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
        ],
        'a486f1bb': [
            (log,                             ('2.4 - 3.2: Dialyn Hair Position VB Hash',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
        ],
        '46019c5e': [
            (log,                             ('2.4 - 3.2: Dialyn Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
        ],
        '339f41eb': [
            (log,                             ('2.4 - 3.2: Dialyn Hair Blend VB Hash',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
        ],
        '4f8d9492': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4dfbd393', 'Dialyn.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('4dfbd393', 'Dialyn.TelephoneLineA.Diffuse.1024')),
        ],
        '4dfbd393': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f8d9492', 'Dialyn.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('4f8d9492', 'Dialyn.TelephoneLineA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.4 - 3.2: Dialyn HairA, BodyA, TelephoneLineA, WeaponGripA, WeaponChakramA and WeaponChakramB NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.TelephoneLineA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.WeaponGripA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.WeaponChakramA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Dialyn.WeaponChakramB.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.4 - 3.2: Dialyn HairA, BodyA, TelephoneLineA, WeaponGripA, WeaponChakramA and WeaponChakramB NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.TelephoneLineA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.WeaponGripA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.WeaponChakramA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Dialyn.WeaponChakramB.NormalMap.2048')),
        ],
        'a3f74f7d': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('df9b8ecd', 'Dialyn.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('df9b8ecd', 'Dialyn.TelephoneLineA.LightMap.1024')),
        ],
        'df9b8ecd': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a3f74f7d', 'Dialyn.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('a3f74f7d', 'Dialyn.TelephoneLineA.LightMap.2048')),
        ],
        '17aadaf6': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e6d6607', 'Dialyn.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('5e6d6607', 'Dialyn.TelephoneLineA.MaterialMap.1024')),
        ],
        '5e6d6607': [
            (log,                             ('2.4 - 3.2: Dialyn HairA and TelephoneLineA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('68f00074', 'Dialyn.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('17aadaf6', 'Dialyn.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('17aadaf6', 'Dialyn.TelephoneLineA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '59390f5a': [
            (log,                             ('2.4 - 3.2: Dialyn Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3c007110': [
            (log,                             ('2.4: Dialyn Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('59390f5a', 'Dialyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '42501c05': [
            (log,                             ('2.4: Dialyn Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('59390f5a', 'Dialyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a935146f': [
            (log,                             ('2.4: Dialyn Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('59390f5a', 'Dialyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '923b7623': [
            (log,                             ('2.4: Dialyn Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('59390f5a', 'Dialyn.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'af39a873': [
            (log,                             ('2.4 - 3.2: Dialyn Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2e77bd1d': [
            (log,                             ('2.4 - 3.2: Dialyn Body Draw VB Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
        ],
        'ff36809b': [
            (log,                             ('2.4 - 3.2: Dialyn Body Position VB Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
        ],
        '3f2079bc': [
            (log,                             ('2.4 - 3.2: Dialyn Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
        ],
        '6ff0e4ad': [
            (log,                             ('2.4: Dialyn Body Blend VB Hash',)),
            (update_hash,                     ('3d7e53cf',)),
        ],
        '3d7e53cf': [
            (log,                             ('2.5 - 3.2: Dialyn Body Blend VB Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
        ],
        '52ea588e': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76ca930e', 'Dialyn.BodyA.Diffuse.1024')),
        ],
        '76ca930e': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('52ea588e', 'Dialyn.BodyA.Diffuse.2048')),
        ],
        '5cc175fe': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8c2fea9f', 'Dialyn.BodyA.LightMap.1024')),
        ],
        '8c2fea9f': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5cc175fe', 'Dialyn.BodyA.LightMap.2048')),
        ],
        '28a10401': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2425ea0', 'Dialyn.BodyA.MaterialMap.1024')),
        ],
        'a2425ea0': [
            (log,                             ('2.4 - 3.2: Dialyn BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('af39a873', 'Dialyn.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('28a10401', 'Dialyn.BodyA.MaterialMap.2048')),
        ],

        # ==================== TelephoneLine Component ====================
        'cd519abe': [
            (log,                             ('2.4 - 3.2: Dialyn TelephoneLine IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '38ce65ff': [
            (log,                             ('2.4 - 3.2: Dialyn TelephoneLine Draw VB Hash',)),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
        ],
        'd0470351': [
            (log,                             ('2.4 - 3.2: Dialyn TelephoneLine Position VB Hash',)),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
        ],
        '2e6484db': [
            (log,                             ('2.4 - 3.2: Dialyn TelephoneLine Texcoord VB Hash',)),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
        ],
        '312b6e12': [
            (log,                             ('2.4 - 3.2: Dialyn TelephoneLine Blend VB Hash',)),
            (add_section_if_missing,          ('cd519abe', 'Dialyn.TelephoneLine.IB', 'match_priority = 0\n')),
        ],
        # TelephoneLine shares all texture hashes with Hair; see that Component above.

        # ==================== Eyebrow Component ====================
        'd860525e': [
            (log,                             ('2.4 - 3.2: Dialyn Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fecc9606': [
            (log,                             ('2.4 - 3.2: Dialyn Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'c4de0541': [
            (log,                             ('2.4 - 3.2: Dialyn Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'd90368ed': [
            (log,                             ('2.4 - 3.1: Dialyn Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('27fd9193',)),
        ],
        '27fd9193': [
            (log,                             ('3.2: Dialyn Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7ec67741': [
            (log,                             ('2.4 - 3.2: Dialyn Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'ad65abbf': [
            (log,                             ('2.4 - 3.2: Dialyn EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('56bc2921', 'Dialyn.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('56bc2921', 'Dialyn.FaceA.Diffuse.1024')),
        ],
        '56bc2921': [
            (log,                             ('2.4 - 3.2: Dialyn EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d860525e', 'Dialyn.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ad65abbf', 'Dialyn.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('ad65abbf', 'Dialyn.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'facb2461': [
            (log,                             ('2.4 - 3.2: Dialyn Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fe5fb676': [
            (log,                             ('2.4 - 3.2: Dialyn Face Draw VB Hash',)),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
        ],
        'c44d2531': [
            (log,                             ('2.4 - 3.2: Dialyn Face Position VB Hash',)),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
        ],
        'f6c5296e': [
            (log,                             ('2.4 - 3.1: Dialyn Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('dafc9647',)),
        ],
        'dafc9647': [
            (log,                             ('3.2: Dialyn Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '08923d3e': [
            (log,                             ('2.4 - 3.2: Dialyn Face Blend VB Hash',)),
            (add_section_if_missing,          ('facb2461', 'Dialyn.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hash with Eyebrow; see that Component above.

        # ==================== WeaponGrip Component ====================
        '1d8f8de6': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGrip IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '25f309c9': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGrip Draw VB Hash',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        ],
        '79fc6a95': [
            (log,                             ('2.4: Dialyn WeaponGrip Position VB Hash',)),
            (update_hash,                     ('fd32eb72',)),
        ],
        'fd32eb72': [
            (log,                             ('2.5 - 2.7: Dialyn WeaponGrip Position VB Hash',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        ],
        'c0f5d550': [
            (log,                             ('2.4: Dialyn WeaponGrip Texcoord VB Hash',)),
            (update_hash,                     ('5455d3c6',)),
        ],
        '5455d3c6': [
            (log,                             ('2.5 - 2.7: Dialyn WeaponGrip Texcoord VB Hash',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        ],
        '35709db4': [
            (log,                             ('2.4: Dialyn WeaponGrip Blend VB Hash',)),
            (update_hash,                     ('8fe19cc1',)),
        ],
        '8fe19cc1': [
            (log,                             ('2.5 - 2.7: Dialyn WeaponGrip Blend VB Hash',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
        ],
        '236576ee': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('87d209c3', 'Dialyn.WeaponGripA.Diffuse.1024')),
            (multiply_section_if_missing,     ('87d209c3', 'Dialyn.WeaponChakramA.Diffuse.1024')),
            (multiply_section_if_missing,     ('87d209c3', 'Dialyn.WeaponChakramB.Diffuse.1024')),
        ],
        '87d209c3': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('236576ee', 'Dialyn.WeaponGripA.Diffuse.2048')),
            (multiply_section_if_missing,     ('236576ee', 'Dialyn.WeaponChakramA.Diffuse.2048')),
            (multiply_section_if_missing,     ('236576ee', 'Dialyn.WeaponChakramB.Diffuse.2048')),
        ],
        '036f72b3': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2264d99', 'Dialyn.WeaponGripA.LightMap.1024')),
            (multiply_section_if_missing,     ('a2264d99', 'Dialyn.WeaponChakramA.LightMap.1024')),
            (multiply_section_if_missing,     ('a2264d99', 'Dialyn.WeaponChakramB.LightMap.1024')),
        ],
        'a2264d99': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('036f72b3', 'Dialyn.WeaponGripA.LightMap.2048')),
            (multiply_section_if_missing,     ('036f72b3', 'Dialyn.WeaponChakramA.LightMap.2048')),
            (multiply_section_if_missing,     ('036f72b3', 'Dialyn.WeaponChakramB.LightMap.2048')),
        ],
        '4f0dc4f4': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7b07624c', 'Dialyn.WeaponGripA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7b07624c', 'Dialyn.WeaponChakramA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('7b07624c', 'Dialyn.WeaponChakramB.MaterialMap.1024')),
        ],
        '7b07624c': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponGripA, WeaponChakramA and WeaponChakramB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1d8f8de6', 'Dialyn.WeaponGrip.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f0dc4f4', 'Dialyn.WeaponGripA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4f0dc4f4', 'Dialyn.WeaponChakramA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('4f0dc4f4', 'Dialyn.WeaponChakramB.MaterialMap.2048')),
        ],

        # ==================== WeaponChakramA Component ====================
        'caa3c4ef': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponChakramA IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '257c4603': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponChakramA and WeaponChakramB Draw VB Hash (shared)',)),
            (add_section_if_missing,          ('caa3c4ef', 'Dialyn.WeaponChakramA.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('aae47bf3', 'Dialyn.WeaponChakramB.IB', 'match_priority = 0\n')),
        ],
        # WeaponChakramA shares all texture hashes with WeaponGrip; see that Component above.

        # ==================== WeaponChakramB Component ====================
        'aae47bf3': [
            (log,                             ('2.4 - 3.2: Dialyn WeaponChakramB IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # WeaponChakramB shares all hashes with WeaponGrip and WeaponChakramA; see those Components above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Dialyn',
    'game_versions': ['2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
