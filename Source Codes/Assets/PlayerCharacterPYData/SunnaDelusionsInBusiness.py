"""
SunnaDelusionsInBusiness Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns SunnaDelusionsInBusiness's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd1e30827': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '20a4edef': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
        ],
        '3f76f9c3': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Hair Position VB Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
        ],
        '97a6b567': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
        ],
        'a7fc2b98': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
        ],
        '2fcfee64': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e85201e7', 'SunnaDelusionsInBusiness.HairA.Diffuse.1024')),
        ],
        'e85201e7': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2fcfee64', 'SunnaDelusionsInBusiness.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA, BodyA and BodyB NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'SunnaDelusionsInBusiness.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SunnaDelusionsInBusiness.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SunnaDelusionsInBusiness.BodyB.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA, BodyA and BodyB NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'SunnaDelusionsInBusiness.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SunnaDelusionsInBusiness.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SunnaDelusionsInBusiness.BodyB.NormalMap.2048')),
        ],
        '8cd786f7': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a2b36369', 'SunnaDelusionsInBusiness.HairA.LightMap.1024')),
        ],
        'a2b36369': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8cd786f7', 'SunnaDelusionsInBusiness.HairA.LightMap.2048')),
        ],
        '3f11dfd9': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab3c12c0', 'SunnaDelusionsInBusiness.HairA.MaterialMap.1024')),
        ],
        'ab3c12c0': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d1e30827', 'SunnaDelusionsInBusiness.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3f11dfd9', 'SunnaDelusionsInBusiness.HairA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '3ab6d438': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8d301b5f': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairShadow Draw VB Hash',)),
            (add_section_if_missing,          ('3ab6d438', 'SunnaDelusionsInBusiness.HairShadow.IB', 'match_priority = 0\n')),
        ],
        'adec0a9a': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairShadow Position VB Hash',)),
            (add_section_if_missing,          ('3ab6d438', 'SunnaDelusionsInBusiness.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '45044c29': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairShadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('3ab6d438', 'SunnaDelusionsInBusiness.HairShadow.IB', 'match_priority = 0\n')),
        ],
        '66523cc4': [
            (log,                             ('3.2: SunnaDelusionsInBusiness HairShadow Blend VB Hash',)),
            (add_section_if_missing,          ('3ab6d438', 'SunnaDelusionsInBusiness.HairShadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '7efbdabd': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e085bc47': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Body Draw VB Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
        ],
        'a0ea50ef': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Body Position VB Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
        ],
        '85f8b8c0': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
        ],
        '89e781e6': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Body Blend VB Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
        ],
        '92795007': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cfc369ad', 'SunnaDelusionsInBusiness.BodyA.Diffuse.1024')),
        ],
        'cfc369ad': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('92795007', 'SunnaDelusionsInBusiness.BodyA.Diffuse.2048')),
        ],
        '6193ed20': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c534187b', 'SunnaDelusionsInBusiness.BodyA.LightMap.1024')),
        ],
        'c534187b': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6193ed20', 'SunnaDelusionsInBusiness.BodyA.LightMap.2048')),
        ],
        'a9bf33e2': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e323c61a', 'SunnaDelusionsInBusiness.BodyA.MaterialMap.1024')),
        ],
        'e323c61a': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9bf33e2', 'SunnaDelusionsInBusiness.BodyA.MaterialMap.2048')),
        ],
        '6ca38b24': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0ee62260', 'SunnaDelusionsInBusiness.BodyB.Diffuse.1024')),
        ],
        '0ee62260': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6ca38b24', 'SunnaDelusionsInBusiness.BodyB.Diffuse.2048')),
        ],
        '4aca364a': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3987c8c2', 'SunnaDelusionsInBusiness.BodyB.LightMap.1024')),
        ],
        '3987c8c2': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4aca364a', 'SunnaDelusionsInBusiness.BodyB.LightMap.2048')),
        ],
        'f3f8895c': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d459d73', 'SunnaDelusionsInBusiness.BodyB.MaterialMap.1024')),
        ],
        '1d459d73': [
            (log,                             ('3.2: SunnaDelusionsInBusiness BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7efbdabd', 'SunnaDelusionsInBusiness.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f3f8895c', 'SunnaDelusionsInBusiness.BodyB.MaterialMap.2048')),
        ],

        # ==================== Eyebrow Component ====================
        '30ea5791': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f0ab8cd': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'a5182b8a': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'fd41220d': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'f5daa764': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'c9b5c6ce': [
            (log,                             ('3.2: SunnaDelusionsInBusiness EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ef66a60', 'SunnaDelusionsInBusiness.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('1ef66a60', 'SunnaDelusionsInBusiness.FaceA.Diffuse.1024')),
        ],
        '1ef66a60': [
            (log,                             ('3.2: SunnaDelusionsInBusiness EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('30ea5791', 'SunnaDelusionsInBusiness.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c9b5c6ce', 'SunnaDelusionsInBusiness.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('c9b5c6ce', 'SunnaDelusionsInBusiness.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '1a2c8573': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9679c257': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Face Draw VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
        ],
        'ac6b5110': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Face Position VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
        ],
        'f5ce8320': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '21299f88': [
            (log,                             ('3.2: SunnaDelusionsInBusiness Face Blend VB Hash',)),
            (add_section_if_missing,          ('1a2c8573', 'SunnaDelusionsInBusiness.Face.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'SunnaDelusionsInBusiness',
    'game_versions': ['3.2'],
}
