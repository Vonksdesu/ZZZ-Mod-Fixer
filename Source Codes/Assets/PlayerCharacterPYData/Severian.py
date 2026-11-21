"""
Severian Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.3
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      skip_unfixable_update, check_indexed_sections,
                      **kwargs):
    """
    Returns Severian's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'dfc9cd38': [
            (log,                             ('3.3: Severian Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2a6a2bc1': [
            (log,                             ('3.3: Severian Hair Draw VB Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
        ],
        '6283ffb6': [
            (log,                             ('3.3: Severian Hair Position VB Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
        ],
        '68708848': [
            (log,                             ('3.3: Severian Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
        ],
        'd82ee988': [
            (log,                             ('3.3: Severian Hair Blend VB Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
        ],
        '3179efd7': [
            (log,                             ('3.3: Severian HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('533dc2f3', 'Severian.HairA.Diffuse.1024')),
        ],
        '533dc2f3': [
            (log,                             ('3.3: Severian HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3179efd7', 'Severian.HairA.Diffuse.2048')),
        ],
        '22f1396d': [
            (log,                             ('3.3: Severian HairA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b21f2b6d', 'Severian.HairA.NormalMap.1024')),
        ],
        'b21f2b6d': [
            (log,                             ('3.3: Severian HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('22f1396d', 'Severian.HairA.NormalMap.2048')),
        ],
        'e0183196': [
            (log,                             ('3.3: Severian HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0d298bc0', 'Severian.HairA.LightMap.1024')),
        ],
        '0d298bc0': [
            (log,                             ('3.3: Severian HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e0183196', 'Severian.HairA.LightMap.2048')),
        ],
        'ae5b72a8': [
            (log,                             ('3.3: Severian HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a4661cdd', 'Severian.HairA.MaterialMap.1024')),
        ],
        'a4661cdd': [
            (log,                             ('3.3: Severian HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('dfc9cd38', 'Severian.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ae5b72a8', 'Severian.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        'b3fdc4d0': [
            (log,                             ('3.3: Severian HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '92dc10a0': [
            (log,                             ('3.3: Severian HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('b3fdc4d0', 'Severian.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '7c997231': [
            (log,                             ('3.3: Severian HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('b3fdc4d0', 'Severian.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'dd0ea903': [
            (log,                             ('3.3: Severian HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3fdc4d0', 'Severian.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '4f9bc0dd': [
            (log,                             ('3.3: Severian HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('b3fdc4d0', 'Severian.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '1a786493': [
            (log,                             ('3.3: Severian Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5e5ca9a0': [
            (log,                             ('3.3: Severian Body Draw VB Hash',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
        ],
        'c88da165': [
            (log,                             ('3.3: Severian Body Position VB Hash',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
        ],
        '8b6c4fbd': [
            (log,                             ('3.3: Severian Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
        ],
        'cff0d638': [
            (log,                             ('3.3: Severian Body Blend VB Hash',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
        ],
        'e8d1f2f1': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b32307bb', 'Severian.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b32307bb', 'Severian.LeftArm(normal form)A.Diffuse.1024')),
        ],
        'b32307bb': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8d1f2f1', 'Severian.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('e8d1f2f1', 'Severian.LeftArm(normal form)A.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.3: Severian BodyA, TrenchCoatA, weaponA, HandcuffsA, LeftArm(combat form)A and LeftArm(normal form)A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.TrenchCoatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.weaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.HandcuffsA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.LeftArm(combat form)A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Severian.LeftArm(normal form)A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.3: Severian BodyA, TrenchCoatA, weaponA, HandcuffsA, LeftArm(combat form)A and LeftArm(normal form)A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.TrenchCoatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.weaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.HandcuffsA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.LeftArm(combat form)A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Severian.LeftArm(normal form)A.NormalMap.2048')),
        ],
        '8dcebaeb': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('10bfb436', 'Severian.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('10bfb436', 'Severian.LeftArm(normal form)A.LightMap.1024')),
        ],
        '10bfb436': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8dcebaeb', 'Severian.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('8dcebaeb', 'Severian.LeftArm(normal form)A.LightMap.2048')),
        ],
        '851c5988': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('43458cec', 'Severian.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('43458cec', 'Severian.LeftArm(normal form)A.MaterialMap.1024')),
        ],
        '43458cec': [
            (log,                             ('3.3: Severian BodyA and LeftArm(normal form)A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('1a786493', 'Severian.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('851c5988', 'Severian.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('851c5988', 'Severian.LeftArm(normal form)A.MaterialMap.2048')),
        ],

        # ==================== TrenchCoat Component ====================
        'b12e74cc': [
            (log,                             ('3.3: Severian TrenchCoat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '65fdcbab': [
            (log,                             ('3.3: Severian TrenchCoat Draw VB Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
        ],
        '46069b10': [
            (log,                             ('3.3: Severian TrenchCoat Position VB Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
        ],
        'b16bb167': [
            (log,                             ('3.3: Severian TrenchCoat Texcoord VB Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
        ],
        '804fffa7': [
            (log,                             ('3.3: Severian TrenchCoat Blend VB Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
        ],
        '518ec152': [
            (log,                             ('3.3: Severian TrenchCoatA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eb4fe1f8', 'Severian.TrenchCoatA.Diffuse.1024')),
        ],
        'eb4fe1f8': [
            (log,                             ('3.3: Severian TrenchCoatA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('518ec152', 'Severian.TrenchCoatA.Diffuse.2048')),
        ],
        'eaedd9dd': [
            (log,                             ('3.3: Severian TrenchCoatA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a755598a', 'Severian.TrenchCoatA.LightMap.1024')),
        ],
        'a755598a': [
            (log,                             ('3.3: Severian TrenchCoatA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eaedd9dd', 'Severian.TrenchCoatA.LightMap.2048')),
        ],
        '1d807f45': [
            (log,                             ('3.3: Severian TrenchCoatA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('37be3d1b', 'Severian.TrenchCoatA.MaterialMap.1024')),
        ],
        '37be3d1b': [
            (log,                             ('3.3: Severian TrenchCoatA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b12e74cc', 'Severian.TrenchCoat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d807f45', 'Severian.TrenchCoatA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '0087bea2': [
            (log,                             ('3.3: Severian Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8ff324f1': [
            (log,                             ('3.3: Severian Tail Draw VB Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
        ],
        '5aacb85b': [
            (log,                             ('3.3: Severian Tail Position VB Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
        ],
        '6641252c': [
            (log,                             ('3.3: Severian Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
        ],
        '09f672f0': [
            (log,                             ('3.3: Severian Tail Blend VB Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
        ],
        'b4a0d995': [
            (log,                             ('3.3: Severian TailA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ec1b60ce', 'Severian.TailA.Diffuse.1024')),
        ],
        'ec1b60ce': [
            (log,                             ('3.3: Severian TailA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b4a0d995', 'Severian.TailA.Diffuse.2048')),
        ],
        'eabc5807': [
            (log,                             ('3.3: Severian TailA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('421b905c', 'Severian.TailA.NormalMap.1024')),
        ],
        '421b905c': [
            (log,                             ('3.3: Severian TailA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eabc5807', 'Severian.TailA.NormalMap.2048')),
        ],
        '23677d43': [
            (log,                             ('3.3: Severian TailA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('deaf3723', 'Severian.TailA.LightMap.1024')),
        ],
        'deaf3723': [
            (log,                             ('3.3: Severian TailA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('0087bea2', 'Severian.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23677d43', 'Severian.TailA.LightMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        '65e63a74': [
            (log,                             ('3.3: Severian Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '63552833': [
            (log,                             ('3.3: Severian Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '2cb553d5': [
            (log,                             ('3.3: Severian Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'e05a094d': [
            (log,                             ('3.3: Severian Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'b8f29b7c': [
            (log,                             ('3.3: Severian Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '0ea1de92': [
            (log,                             ('3.3: Severian EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd8344d5', 'Severian.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bd8344d5', 'Severian.FaceA.Diffuse.1024')),
        ],
        'bd8344d5': [
            (log,                             ('3.3: Severian EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('65e63a74', 'Severian.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0ea1de92', 'Severian.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('0ea1de92', 'Severian.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '1c78c21e': [
            (log,                             ('3.3: Severian Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cc5ad373': [
            (log,                             ('3.3: Severian Face Draw VB Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
        ],
        'f6484034': [
            (log,                             ('3.3: Severian Face Position VB Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
        ],
        '0ce4e45f': [
            (log,                             ('3.3: Severian Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
        ],
        'e37d8ce1': [
            (log,                             ('3.3: Severian Face Blend VB Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
        ],
        'f0d3dadb': [
            (log,                             ('3.3: Severian FaceB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5f31dd89', 'Severian.FaceB.Diffuse.1024')),
        ],
        '5f31dd89': [
            (log,                             ('3.3: Severian FaceB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('1c78c21e', 'Severian.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f0d3dadb', 'Severian.FaceB.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        '4e7b90e1': [
            (log,                             ('3.3: Severian weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3642f351': [
            (log,                             ('3.3: Severian weapon Draw VB Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
        ],
        '5cba67ba': [
            (log,                             ('3.3: Severian weapon Position VB Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
        ],
        'd4d68aa2': [
            (log,                             ('3.3: Severian weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
        ],
        '6b4aad2b': [
            (log,                             ('3.3: Severian weapon Blend VB Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
        ],
        '64918699': [
            (log,                             ('3.3: Severian weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('138681d2', 'Severian.weaponA.Diffuse.1024')),
        ],
        '138681d2': [
            (log,                             ('3.3: Severian weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('64918699', 'Severian.weaponA.Diffuse.2048')),
        ],
        '8dcf2b61': [
            (log,                             ('3.3: Severian weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d0690982', 'Severian.weaponA.LightMap.1024')),
        ],
        'd0690982': [
            (log,                             ('3.3: Severian weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8dcf2b61', 'Severian.weaponA.LightMap.2048')),
        ],
        '4f148670': [
            (log,                             ('3.3: Severian weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('69f72b01', 'Severian.weaponA.MaterialMap.1024')),
        ],
        '69f72b01': [
            (log,                             ('3.3: Severian weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4e7b90e1', 'Severian.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4f148670', 'Severian.weaponA.MaterialMap.2048')),
        ],

        # ==================== Handcuffs Component ====================
        'b95f6269': [
            (log,                             ('3.3: Severian Handcuffs IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '05a2e40d': [
            (log,                             ('3.3: Severian Handcuffs Draw VB Hash',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
        ],
        'dc19f5f5': [
            (log,                             ('3.3: Severian Handcuffs Position VB Hash',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
        ],
        '5b11a7ca': [
            (log,                             ('3.3: Severian Handcuffs Texcoord VB Hash',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
        ],
        '3cbd2e7c': [
            (log,                             ('3.3: Severian Handcuffs Blend VB Hash',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
        ],
        '4ff8724c': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f3890756', 'Severian.HandcuffsA.Diffuse.1024')),
            (multiply_section_if_missing,     ('f3890756', 'Severian.LeftArm(combat form)A.Diffuse.1024')),
        ],
        'f3890756': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ff8724c', 'Severian.HandcuffsA.Diffuse.2048')),
            (multiply_section_if_missing,     ('4ff8724c', 'Severian.LeftArm(combat form)A.Diffuse.2048')),
        ],
        '3fde6ee9': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('563de7e6', 'Severian.HandcuffsA.LightMap.1024')),
            (multiply_section_if_missing,     ('563de7e6', 'Severian.LeftArm(combat form)A.LightMap.1024')),
        ],
        '563de7e6': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3fde6ee9', 'Severian.HandcuffsA.LightMap.2048')),
            (multiply_section_if_missing,     ('3fde6ee9', 'Severian.LeftArm(combat form)A.LightMap.2048')),
        ],
        'bd135b6e': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1f163242', 'Severian.HandcuffsA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('1f163242', 'Severian.LeftArm(combat form)A.MaterialMap.1024')),
        ],
        '1f163242': [
            (log,                             ('3.3: Severian HandcuffsA and LeftArm(combat form)A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b95f6269', 'Severian.Handcuffs.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd135b6e', 'Severian.HandcuffsA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('bd135b6e', 'Severian.LeftArm(combat form)A.MaterialMap.2048')),
        ],

        # ==================== LeftArm(combat form) Component ====================
        'c1196eee': [
            (log,                             ('3.3: Severian LeftArm(combat form) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '117fd2d1': [
            (log,                             ('3.3: Severian LeftArm(combat form) Draw VB Hash',)),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
        ],
        'a0033f00': [
            (log,                             ('3.3: Severian LeftArm(combat form) Position VB Hash',)),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
        ],
        '5374f505': [
            (log,                             ('3.3: Severian LeftArm(combat form) Texcoord VB Hash',)),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
        ],
        '20b505f8': [
            (log,                             ('3.3: Severian LeftArm(combat form) Blend VB Hash',)),
            (add_section_if_missing,          ('c1196eee', 'Severian.LeftArm(combat form).IB', 'match_priority = 0\n')),
        ],

        # ==================== LeftArm(normal form) Component ====================
        '425e096c': [
            (log,                             ('3.3: Severian LeftArm(normal form) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7449d16f': [
            (log,                             ('3.3: Severian LeftArm(normal form) Draw VB Hash',)),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
        ],
        'f3b040e4': [
            (log,                             ('3.3: Severian LeftArm(normal form) Position VB Hash',)),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
        ],
        'fe0d2d9b': [
            (log,                             ('3.3: Severian LeftArm(normal form) Texcoord VB Hash',)),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
        ],
        '21d53f78': [
            (log,                             ('3.3: Severian LeftArm(normal form) Blend VB Hash',)),
            (add_section_if_missing,          ('425e096c', 'Severian.LeftArm(normal form).IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Severian',
    'game_versions': ['3.3'],
}
