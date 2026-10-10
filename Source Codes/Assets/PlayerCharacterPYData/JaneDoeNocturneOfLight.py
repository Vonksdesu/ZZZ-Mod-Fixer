"""
JaneDoeNocturneOfLight Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns JaneDoeNocturneOfLight's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '3275b812': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '74bc0b7f': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Hair Draw VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
        ],
        '33a09cfe': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Hair Position VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
        ],
        'fa617c9a': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
        ],
        'e42171df': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Hair Blend VB Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
        ],
        'f7ef1a53': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b33a9770', 'JaneDoeNocturneOfLight.HairA.Diffuse.1024')),
        ],
        'b33a9770': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f7ef1a53', 'JaneDoeNocturneOfLight.HairA.Diffuse.2048')),
        ],
        '9ec4cd4f': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e12acc1', 'JaneDoeNocturneOfLight.HairA.LightMap.1024')),
        ],
        '5e12acc1': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ec4cd4f', 'JaneDoeNocturneOfLight.HairA.LightMap.2048')),
        ],
        '5e34e275': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('40fca454', 'JaneDoeNocturneOfLight.HairA.MaterialMap.1024')),
        ],
        '40fca454': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5e34e275', 'JaneDoeNocturneOfLight.HairA.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA, BodyA and weapon - 手刀 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoeNocturneOfLight.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoeNocturneOfLight.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'JaneDoeNocturneOfLight.weapon - 手刀.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HairA, BodyA and weapon - 手刀 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoeNocturneOfLight.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoeNocturneOfLight.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'JaneDoeNocturneOfLight.weapon - 手刀.NormalMap.2048')),
        ],

        # ==================== HeHair Shadowad Component ====================
        '27805144': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HeHair Shadowad IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '759a4b9f': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HeHair Shadowad Draw VB Hash',)),
            (add_section_if_missing,          ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
        ],
        '7c08cd53': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HeHair Shadowad Position VB Hash',)),
            (add_section_if_missing,          ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
        ],
        '93c5b49a': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HeHair Shadowad Texcoord VB Hash',)),
            (add_section_if_missing,          ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
        ],
        '6af472f5': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight HeHair Shadowad Blend VB Hash',)),
            (add_section_if_missing,          ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'ac900322': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3f009560': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Body Draw VB Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
        ],
        '4544dca7': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Body Position VB Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
        ],
        '6845e991': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
        ],
        '44071a5e': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Body Blend VB Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
        ],
        'a47bf989': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('be442045', 'JaneDoeNocturneOfLight.BodyA.Diffuse.1024')),
        ],
        'be442045': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a47bf989', 'JaneDoeNocturneOfLight.BodyA.Diffuse.2048')),
        ],
        'dd1b5520': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f655d62e', 'JaneDoeNocturneOfLight.BodyA.LightMap.1024')),
        ],
        'f655d62e': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dd1b5520', 'JaneDoeNocturneOfLight.BodyA.LightMap.2048')),
        ],
        '389d9c67': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('13eafbbd', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.1024')),
        ],
        '13eafbbd': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('389d9c67', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== LegRingGemstone Component ====================
        'ca887a07': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight LegRingGemstone IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '65c0f994': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight LegRingGemstone Draw VB Hash',)),
            (add_section_if_missing,          ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
        ],
        'ad125746': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight LegRingGemstone Position VB Hash',)),
            (add_section_if_missing,          ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
        ],
        '7c6a8591': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight LegRingGemstone Texcoord VB Hash',)),
            (add_section_if_missing,          ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
        ],
        '370c397a': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight LegRingGemstone Blend VB Hash',)),
            (add_section_if_missing,          ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
        ],
        'e108fa5b': [
            (log,                             ('2.5 - 3.0: JaneDoeNocturneOfLight LegRingGemstoneA Diffuse 1024p & 2048p Hash',)),
            (add_section_if_missing,          ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        'ef86fc9f': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5661afc3': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
        ],
        '6c733c84': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Face Position VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
        ],
        '1fa404c1': [
            (log,                             ('2.5 - 3.0: JaneDoeNocturneOfLight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('3c32a411',)),
        ],
        '3c32a411': [
            (log,                             ('3.1: JaneDoeNocturneOfLight Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
        ],
        '91846a84': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight Face Blend VB Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
        ],
        '3b75aa2c': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d823ac80', 'JaneDoeNocturneOfLight.FaceA.Diffuse.1024')),
        ],
        'd823ac80': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3b75aa2c', 'JaneDoeNocturneOfLight.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 手刀 Component ====================
        '602c545a': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'be378e74': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
        ],
        '59c18114': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0158a68f', 'JaneDoeNocturneOfLight.weapon - 手刀.Diffuse.1024')),
        ],
        '0158a68f': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('59c18114', 'JaneDoeNocturneOfLight.weapon - 手刀.Diffuse.2048')),
        ],
        '76cda993': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 LightMap 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('655a0c17', 'JaneDoeNocturneOfLight.weapon - 手刀.LightMap.1024')),
        ],
        '655a0c17': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 LightMap 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76cda993', 'JaneDoeNocturneOfLight.weapon - 手刀.LightMap.2048')),
        ],
        'd83ad325': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9f30a0e', 'JaneDoeNocturneOfLight.weapon - 手刀.MaterialMap.1024')),
        ],
        'f9f30a0e': [
            (log,                             ('2.5 - 3.2: JaneDoeNocturneOfLight weapon - 手刀 MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('602c545a', 'JaneDoeNocturneOfLight.weapon - 手刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d83ad325', 'JaneDoeNocturneOfLight.weapon - 手刀.MaterialMap.2048')),
        ],
        # weapon - 手刀 shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoeNocturneOfLight',
    'game_versions': ['2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
