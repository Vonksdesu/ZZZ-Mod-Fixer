"""
PanYinhuCulinaryJewel Character Hash Commands
ZZZ Mod Fixer v2.6
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
    Returns PanYinhuCulinaryJewel's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Body Component ====================
        'b518e540': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '56b1d7f1': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Body Draw VB Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        ],
        'db608bcf': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Body Position VB Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        ],
        'f5b6e5b5': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        ],
        '06f47d71': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Body Blend VB Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
        ],
        'e9a912e7': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0cab7a7b', 'PanYinhuCulinaryJewel.BodyA.Diffuse.1024')),
        ],
        '0cab7a7b': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e9a912e7', 'PanYinhuCulinaryJewel.BodyA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA, FaceA, weapon - 炒勺A and weapon - 炒锅A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhuCulinaryJewel.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhuCulinaryJewel.FaceA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhuCulinaryJewel.weapon - 炒勺A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhuCulinaryJewel.weapon - 炒锅A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA, FaceA, weapon - 炒勺A and weapon - 炒锅A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhuCulinaryJewel.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhuCulinaryJewel.FaceA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhuCulinaryJewel.weapon - 炒勺A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhuCulinaryJewel.weapon - 炒锅A.NormalMap.2048')),
        ],
        '54c0f79a': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91bfe5cd', 'PanYinhuCulinaryJewel.BodyA.LightMap.1024')),
        ],
        '91bfe5cd': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('54c0f79a', 'PanYinhuCulinaryJewel.BodyA.LightMap.2048')),
        ],
        '7498bd49': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('78cbb2e4', 'PanYinhuCulinaryJewel.BodyA.MaterialMap.1024')),
        ],
        '78cbb2e4': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7498bd49', 'PanYinhuCulinaryJewel.BodyA.MaterialMap.2048')),
        ],
        '8459c5e8': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b3775104', 'PanYinhuCulinaryJewel.BodyB.Diffuse.1024')),
        ],
        'b3775104': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8459c5e8', 'PanYinhuCulinaryJewel.BodyB.Diffuse.2048')),
        ],
        'c7bdc86b': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB LightMap 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('240da72f', 'PanYinhuCulinaryJewel.BodyB.LightMap.1024')),
        ],
        '240da72f': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB LightMap 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7bdc86b', 'PanYinhuCulinaryJewel.BodyB.LightMap.2048')),
        ],
        'c50582f7': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf25d6f7', 'PanYinhuCulinaryJewel.BodyB.MaterialMap.1024')),
        ],
        'bf25d6f7': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyB MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c50582f7', 'PanYinhuCulinaryJewel.BodyB.MaterialMap.2048')),
        ],
        '10e8bc53': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('48c0fbcc', 'PanYinhuCulinaryJewel.BodyC.Diffuse.1024')),
            (multiply_section_if_missing,     ('48c0fbcc', 'PanYinhuCulinaryJewel.weapon - 炒勺A.Diffuse.1024')),
            (multiply_section_if_missing,     ('48c0fbcc', 'PanYinhuCulinaryJewel.weapon - 炒锅A.Diffuse.1024')),
        ],
        '48c0fbcc': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('10e8bc53', 'PanYinhuCulinaryJewel.BodyC.Diffuse.2048')),
            (multiply_section_if_missing,     ('10e8bc53', 'PanYinhuCulinaryJewel.weapon - 炒勺A.Diffuse.2048')),
            (multiply_section_if_missing,     ('10e8bc53', 'PanYinhuCulinaryJewel.weapon - 炒锅A.Diffuse.2048')),
        ],
        '1da6b5bf': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eceb77a3', 'PanYinhuCulinaryJewel.BodyC.LightMap.1024')),
            (multiply_section_if_missing,     ('eceb77a3', 'PanYinhuCulinaryJewel.weapon - 炒勺A.LightMap.1024')),
            (multiply_section_if_missing,     ('eceb77a3', 'PanYinhuCulinaryJewel.weapon - 炒锅A.LightMap.1024')),
        ],
        'eceb77a3': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1da6b5bf', 'PanYinhuCulinaryJewel.BodyC.LightMap.2048')),
            (multiply_section_if_missing,     ('1da6b5bf', 'PanYinhuCulinaryJewel.weapon - 炒勺A.LightMap.2048')),
            (multiply_section_if_missing,     ('1da6b5bf', 'PanYinhuCulinaryJewel.weapon - 炒锅A.LightMap.2048')),
        ],
        'eb5755d6': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('40dea057', 'PanYinhuCulinaryJewel.BodyC.MaterialMap.1024')),
            (multiply_section_if_missing,     ('40dea057', 'PanYinhuCulinaryJewel.weapon - 炒勺A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('40dea057', 'PanYinhuCulinaryJewel.weapon - 炒锅A.MaterialMap.1024')),
        ],
        '40dea057': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel BodyC, weapon - 炒勺A and weapon - 炒锅A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eb5755d6', 'PanYinhuCulinaryJewel.BodyC.MaterialMap.2048')),
            (multiply_section_if_missing,     ('eb5755d6', 'PanYinhuCulinaryJewel.weapon - 炒勺A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('eb5755d6', 'PanYinhuCulinaryJewel.weapon - 炒锅A.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'ebb6a59b': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '682e8e8d': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Face Draw VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
        ],
        '1eee2121': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
        ],
        '4aae3329': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel Face Blend VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
        ],
        'ed361b8f': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('452a0918', 'PanYinhuCulinaryJewel.FaceA.Diffuse.1024')),
        ],
        '452a0918': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed361b8f', 'PanYinhuCulinaryJewel.FaceA.Diffuse.2048')),
        ],
        '96280008': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3744882e', 'PanYinhuCulinaryJewel.FaceA.LightMap.1024')),
        ],
        '3744882e': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96280008', 'PanYinhuCulinaryJewel.FaceA.LightMap.2048')),
        ],
        '57446a22': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18dd19bf', 'PanYinhuCulinaryJewel.FaceA.MaterialMap.1024')),
        ],
        '18dd19bf': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel FaceA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57446a22', 'PanYinhuCulinaryJewel.FaceA.MaterialMap.2048')),
        ],

        # ==================== weapon - 炒勺 Component ====================
        'ca72c1f0': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒勺 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f8e2d91': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒勺 Draw VB Hash',)),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        'f6855ee8': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒勺 Position VB Hash',)),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        'f29f44e5': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒勺 Texcoord VB Hash',)),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        '644a4506': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒勺 Blend VB Hash',)),
            (add_section_if_missing,          ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        # weapon - 炒勺 shares its textures with Body's C group; see the Body Component above.

        # ==================== weapon - 炒锅 Component ====================
        '12d52f05': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒锅 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '759a4b9f': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒锅 Draw VB Hash',)),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        '7e980f75': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒锅 Position VB Hash',)),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        '7353a8ed': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒锅 Texcoord VB Hash',)),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        'c39d130e': [
            (log,                             ('2.6 - 3.2: PanYinhuCulinaryJewel weapon - 炒锅 Blend VB Hash',)),
            (add_section_if_missing,          ('12d52f05', 'PanYinhuCulinaryJewel.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        # weapon - 炒锅 shares its textures with Body's C group; see the Body Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhuCulinaryJewel',
    'game_versions': ['2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
