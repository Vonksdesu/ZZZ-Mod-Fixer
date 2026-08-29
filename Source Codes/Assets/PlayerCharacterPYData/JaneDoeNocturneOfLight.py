"""
JaneDoeNocturneOfLight Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
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
# === IB Hashes ===
'ac900322': [
        (log,                           ('1.4 - 2.5: JaneDoeNocturneOfLight Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'3275b812': [
        (log,                           ('1.4 - 2.5: JaneDoeNocturneOfLight Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Body Textures (BodyA) ===
'be442045': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('a47bf989', 'JaneDoeNocturneOfLight.BodyA.Diffuse.2048')),
    ],
'a47bf989': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('be442045', 'JaneDoeNocturneOfLight.BodyA.Diffuse.1024')),
    ],
'f655d62e': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('dd1b5520', 'JaneDoeNocturneOfLight.BodyA.LightMap.2048')),
    ],
'dd1b5520': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('f655d62e', 'JaneDoeNocturneOfLight.BodyA.LightMap.1024')),
    ],
'13eafbbd': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('389d9c67', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.2048')),
    ],
'389d9c67': [
        (log,                           ('1.1 - 2.5: JaneDoeNocturneOfLight BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('13eafbbd', 'JaneDoeNocturneOfLight.BodyA.MaterialMap.1024')),
    ],
'33a09cfe': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair VB Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'fa617c9a': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair VB Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'e42171df': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair VB Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'f7ef1a53': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'9ec4cd4f': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'5e34e275': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'27805144': [(log, ('3.0: JaneDoeNocturneOfLight HeHair Shadowad IB Hash',)), (add_ib_check_if_missing,)],
'759a4b9f': [
        (log, ('3.0: JaneDoeNocturneOfLight HeHair Shadowad VB Hash',)),
        (add_section_if_missing, ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
    ],
'7c08cd53': [
        (log, ('3.0: JaneDoeNocturneOfLight HeHair Shadowad VB Hash',)),
        (add_section_if_missing, ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
    ],
'93c5b49a': [
        (log, ('3.0: JaneDoeNocturneOfLight HeHair Shadowad VB Hash',)),
        (add_section_if_missing, ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
    ],
'6af472f5': [
        (log, ('3.0: JaneDoeNocturneOfLight HeHair Shadowad VB Hash',)),
        (add_section_if_missing, ('27805144', 'JaneDoeNocturneOfLight.HeHair Shadowad.IB', 'match_priority = 0\n')),
    ],
'4544dca7': [
        (log, ('3.0: JaneDoeNocturneOfLight Body VB Hash',)),
        (add_section_if_missing, ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
    ],
'6845e991': [
        (log, ('3.0: JaneDoeNocturneOfLight Body VB Hash',)),
        (add_section_if_missing, ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
    ],
'44071a5e': [
        (log, ('3.0: JaneDoeNocturneOfLight Body VB Hash',)),
        (add_section_if_missing, ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
    ],
'ca887a07': [(log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone IB Hash',)), (add_ib_check_if_missing,)],
'65c0f994': [
        (log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone VB Hash',)),
        (add_section_if_missing, ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
'ad125746': [
        (log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone VB Hash',)),
        (add_section_if_missing, ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
'7c6a8591': [
        (log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone VB Hash',)),
        (add_section_if_missing, ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
'370c397a': [
        (log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone VB Hash',)),
        (add_section_if_missing, ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
'e108fa5b': [
        (log, ('3.0: JaneDoeNocturneOfLight LegRingGemstone TEX Hash',)),
        (add_section_if_missing, ('ca887a07', 'JaneDoeNocturneOfLight.LegRingGemstone.IB', 'match_priority = 0\n')),
    ],
'ef86fc9f': [(log, ('3.0: JaneDoeNocturneOfLight Face IB Hash',)), (add_ib_check_if_missing,)],
'6c733c84': [
        (log, ('3.0: JaneDoeNocturneOfLight Face VB Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
    ],
'1fa404c1': [
        (log, ('3.0: JaneDoeNocturneOfLight Face VB Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
        (update_hash, ('3c32a411',)),
    ],
'3c32a411': [
        (log, ('3.1: JaneDoeNocturneOfLight Face VB Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
    ],
'91846a84': [
        (log, ('3.0: JaneDoeNocturneOfLight Face VB Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
    ],
'3b75aa2c': [
        (log, ('3.0: JaneDoeNocturneOfLight Face TEX Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
    ],
'602c545a': [(log, ('3.0: JaneDoeNocturneOfLight weapon IB Hash',)), (add_ib_check_if_missing,)],
'59c18114': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
'76cda993': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
'd83ad325': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
'5661afc3': [(log, ('3.0: JaneDoeNocturneOfLight misc hash',)),],
'be378e74': [(log, ('3.0: JaneDoeNocturneOfLight misc hash',)),],
'74bc0b7f': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair VB Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'b33a9770': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'5e12acc1': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'40fca454': [
        (log, ('3.0: JaneDoeNocturneOfLight Hair TEX Hash',)),
        (add_section_if_missing, ('3275b812', 'JaneDoeNocturneOfLight.Hair.IB', 'match_priority = 0\n')),
    ],
'd823ac80': [
        (log, ('3.0: JaneDoeNocturneOfLight Face TEX Hash',)),
        (add_section_if_missing, ('ef86fc9f', 'JaneDoeNocturneOfLight.Face.IB', 'match_priority = 0\n')),
    ],
'655a0c17': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
'f9f30a0e': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
'3f009560': [
        (log, ('3.0: JaneDoeNocturneOfLight Body VB Hash',)),
        (add_section_if_missing, ('ac900322', 'JaneDoeNocturneOfLight.Body.IB', 'match_priority = 0\n')),
    ],
'0158a68f': [
        (log, ('3.0: JaneDoeNocturneOfLight weapon TEX Hash',)),
        (add_section_if_missing, ('602c545a', 'JaneDoeNocturneOfLight.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'JaneDoeNocturneOfLight',
    'game_versions': ['1.1', '1.4', '2.5'],
}
