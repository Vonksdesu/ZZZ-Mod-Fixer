"""
PanYinhu Character Hash Commands
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
    Returns PanYinhu's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Body Component ====================
        'cb1a6db9': [
            (log,                             ('2.2 - 3.2: PanYinhu Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b375f26b': [
            (log,                             ('2.2 - 3.2: PanYinhu Body Draw VB Hash',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        ],
        'aba31d2e': [
            (log,                             ('2.2 - 3.2: PanYinhu Body Position VB Hash',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        ],
        'cc541390': [
            (log,                             ('2.2 - 3.2: PanYinhu Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        ],
        '4727992f': [
            (log,                             ('2.2 - 3.2: PanYinhu Body Blend VB Hash',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
        ],
        'c0928025': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b20c7e8b', 'PanYinhu.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('b20c7e8b', 'PanYinhu.weapon - 馒头A.Diffuse.1024')),
            (multiply_section_if_missing,     ('b20c7e8b', 'PanYinhu.weapon - 炒锅B.Diffuse.1024')),
        ],
        'b20c7e8b': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c0928025', 'PanYinhu.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('c0928025', 'PanYinhu.weapon - 馒头A.Diffuse.2048')),
            (multiply_section_if_missing,     ('c0928025', 'PanYinhu.weapon - 炒锅B.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, FaceA, weapon - 馒头A, weapon - 炒勺A and weapon - 炒锅A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhu.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhu.FaceA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhu.weapon - 馒头A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhu.weapon - 炒勺A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'PanYinhu.weapon - 炒锅A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, FaceA, weapon - 馒头A, weapon - 炒勺A and weapon - 炒锅A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhu.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhu.FaceA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhu.weapon - 馒头A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhu.weapon - 炒勺A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'PanYinhu.weapon - 炒锅A.NormalMap.2048')),
        ],
        '7d3c4c3d': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7967c15f', 'PanYinhu.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('7967c15f', 'PanYinhu.weapon - 馒头A.LightMap.1024')),
            (multiply_section_if_missing,     ('7967c15f', 'PanYinhu.weapon - 炒锅B.LightMap.1024')),
        ],
        '7967c15f': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7d3c4c3d', 'PanYinhu.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('7d3c4c3d', 'PanYinhu.weapon - 馒头A.LightMap.2048')),
            (multiply_section_if_missing,     ('7d3c4c3d', 'PanYinhu.weapon - 炒锅B.LightMap.2048')),
        ],
        '42fc25f0': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2daeed33', 'PanYinhu.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2daeed33', 'PanYinhu.weapon - 馒头A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2daeed33', 'PanYinhu.weapon - 炒锅B.MaterialMap.1024')),
        ],
        '2daeed33': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyA, weapon - 馒头A and weapon - 炒锅B MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('42fc25f0', 'PanYinhu.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('42fc25f0', 'PanYinhu.weapon - 馒头A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('42fc25f0', 'PanYinhu.weapon - 炒锅B.MaterialMap.2048')),
        ],
        'f2433e17': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf6afa84', 'PanYinhu.BodyB.Diffuse.1024')),
            (multiply_section_if_missing,     ('cf6afa84', 'PanYinhu.weapon - 炒勺A.Diffuse.1024')),
            (multiply_section_if_missing,     ('cf6afa84', 'PanYinhu.weapon - 炒锅A.Diffuse.1024')),
        ],
        'cf6afa84': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f2433e17', 'PanYinhu.BodyB.Diffuse.2048')),
            (multiply_section_if_missing,     ('f2433e17', 'PanYinhu.weapon - 炒勺A.Diffuse.2048')),
            (multiply_section_if_missing,     ('f2433e17', 'PanYinhu.weapon - 炒锅A.Diffuse.2048')),
        ],
        'ddeaa4c3': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('26454e30', 'PanYinhu.BodyB.LightMap.1024')),
            (multiply_section_if_missing,     ('26454e30', 'PanYinhu.weapon - 炒勺A.LightMap.1024')),
            (multiply_section_if_missing,     ('26454e30', 'PanYinhu.weapon - 炒锅A.LightMap.1024')),
        ],
        '26454e30': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ddeaa4c3', 'PanYinhu.BodyB.LightMap.2048')),
            (multiply_section_if_missing,     ('ddeaa4c3', 'PanYinhu.weapon - 炒勺A.LightMap.2048')),
            (multiply_section_if_missing,     ('ddeaa4c3', 'PanYinhu.weapon - 炒锅A.LightMap.2048')),
        ],
        'de553410': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e0433c18', 'PanYinhu.BodyB.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e0433c18', 'PanYinhu.weapon - 炒勺A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e0433c18', 'PanYinhu.weapon - 炒锅A.MaterialMap.1024')),
        ],
        'e0433c18': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyB, weapon - 炒勺A and weapon - 炒锅A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('de553410', 'PanYinhu.BodyB.MaterialMap.2048')),
            (multiply_section_if_missing,     ('de553410', 'PanYinhu.weapon - 炒勺A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('de553410', 'PanYinhu.weapon - 炒锅A.MaterialMap.2048')),
        ],
        'ed361b8f': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('452a0918', 'PanYinhu.BodyC.Diffuse.1024')),
            (multiply_section_if_missing,     ('452a0918', 'PanYinhu.FaceA.Diffuse.1024')),
        ],
        '452a0918': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed361b8f', 'PanYinhu.BodyC.Diffuse.2048')),
            (multiply_section_if_missing,     ('ed361b8f', 'PanYinhu.FaceA.Diffuse.2048')),
        ],
        '96280008': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3744882e', 'PanYinhu.BodyC.LightMap.1024')),
            (multiply_section_if_missing,     ('3744882e', 'PanYinhu.FaceA.LightMap.1024')),
        ],
        '3744882e': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('96280008', 'PanYinhu.BodyC.LightMap.2048')),
            (multiply_section_if_missing,     ('96280008', 'PanYinhu.FaceA.LightMap.2048')),
        ],
        '57446a22': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18dd19bf', 'PanYinhu.BodyC.MaterialMap.1024')),
            (multiply_section_if_missing,     ('18dd19bf', 'PanYinhu.FaceA.MaterialMap.1024')),
        ],
        '18dd19bf': [
            (log,                             ('2.2 - 3.2: PanYinhu BodyC and FaceA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cb1a6db9', 'PanYinhu.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('57446a22', 'PanYinhu.BodyC.MaterialMap.2048')),
            (multiply_section_if_missing,     ('57446a22', 'PanYinhu.FaceA.MaterialMap.2048')),
        ],

        # ==================== weapon - 馒头 Component ====================
        'b3556f6e': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 馒头 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '534c2f9b': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 馒头 Draw VB Hash',)),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
        ],
        '4864dcdd': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 馒头 Position VB Hash',)),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
        ],
        'a6f599e3': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 馒头 Texcoord VB Hash',)),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
        ],
        'b88cf297': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 馒头 Blend VB Hash',)),
            (add_section_if_missing,          ('b3556f6e', 'PanYinhu.weapon - 馒头.IB', 'match_priority = 0\n')),
        ],
        # weapon - 馒头 shares its textures with Body's A/B groups; see the Body Component above.

        # ==================== Face Component ====================
        'ebb6a59b': [
            (log,                             ('2.2 - 3.2: PanYinhu Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '682e8e8d': [
            (log,                             ('2.2 - 3.2: PanYinhu Face Draw VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        ],
        '1eee2121': [
            (log,                             ('2.2 - 3.2: PanYinhu Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        ],
        '4aae3329': [
            (log,                             ('2.2 - 3.2: PanYinhu Face Blend VB Hash',)),
            (add_section_if_missing,          ('ebb6a59b', 'PanYinhu.Face.IB', 'match_priority = 0\n')),
        ],
        # Face has no Position VB hash in any database version and shares its textures with Body's D group; see the Body Component above.

        # ==================== weapon - 炒勺 Component ====================
        '45a8cd1b': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒勺 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2a45b03d': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒勺 Draw VB Hash',)),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        'e56ae11f': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒勺 Position VB Hash',)),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        '1a769e88': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒勺 Texcoord VB Hash',)),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        'cd763e6d': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒勺 Blend VB Hash',)),
            (add_section_if_missing,          ('45a8cd1b', 'PanYinhu.weapon - 炒勺.IB', 'match_priority = 0\n')),
        ],
        # weapon - 炒勺 shares its textures with Body's C group; see the Body Component above.

        # ==================== weapon - 炒锅 Component ====================
        'ff7e9b40': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒锅 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2e2d67ae': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒锅 Draw VB Hash',)),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        '0ee4a87c': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒锅 Position VB Hash',)),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        'd569d88e': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒锅 Texcoord VB Hash',)),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        'd141908c': [
            (log,                             ('2.2 - 3.2: PanYinhu weapon - 炒锅 Blend VB Hash',)),
            (add_section_if_missing,          ('ff7e9b40', 'PanYinhu.weapon - 炒锅.IB', 'match_priority = 0\n')),
        ],
        # weapon - 炒锅 has two object groups: group A shares Body's C group textures and group B shares Body's A/B group textures; see the Body Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhu',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
