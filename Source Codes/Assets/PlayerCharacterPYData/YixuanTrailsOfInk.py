"""
YixuanTrailsOfInk Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json data
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YixuanTrailsOfInk's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'ac8e9ee3': [(log, ('2.5: YixuanTrailsOfInk Hair IB Hash',)),      (add_ib_check_if_missing,)],
'95de0d39': [(log, ('2.5: YixuanTrailsOfInk Body IB Hash',)),      (add_ib_check_if_missing,)],
'064cd7d3': [(log, ('2.5: YixuanTrailsOfInk Bottle IB Hash',)),    (add_ib_check_if_missing,)],
'0fdae851': [(log, ('2.5: YixuanTrailsOfInk Ink IB Hash',)),       (add_ib_check_if_missing,)],
'8b067f99': [(log, ('2.5: YixuanTrailsOfInk Face IB Hash',)),      (add_ib_check_if_missing,)],

# Shared Texture Hash - NormalMap (used across Hair, Body, Bottle)
'ebac056e': [
        (log,                           ('2.5: YixuanTrailsOfInk Shared NormalMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],

# Hair Textures
'7e38b38b': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair Diffuse Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'086ac064': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair LightMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'83b02982': [
        (log,                           ('2.5: YixuanTrailsOfInk Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures - Object A
'fe2cc6f3': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse 2048p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5460dbe4', 'YixuanTrailsOfInk.BodyA.Diffuse.1024')),
    ],

'5460dbe4': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse 1024p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fe2cc6f3', 'YixuanTrailsOfInk.BodyA.Diffuse.2048')),
    ],
'867e3b95': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap 2048p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7369431b', 'YixuanTrailsOfInk.BodyA.LightMap.1024')),
    ],

'7369431b': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap 1024p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('867e3b95', 'YixuanTrailsOfInk.BodyA.LightMap.2048')),
    ],
'c72a2356': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap 2048p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2d535255', 'YixuanTrailsOfInk.BodyA.MaterialMap.1024')),
    ],

'2d535255': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap 1024p Hash (Object A)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c72a2356', 'YixuanTrailsOfInk.BodyA.MaterialMap.2048')),
    ],

# Body/Bottle Textures - Object B/C
'487db3e0': [(log, ('2.0 -> 2.1: YiXuanSkin BodyB Diffuse 2048p Hash',)), (update_hash, ('7683c132',))],
'7683c132': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse 2048p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('c13cac2c', '89509335'), 'YixuanTrailsOfInk.BodyB.Diffuse.1024')),
    ],

'c13cac2c': [(log, ('2.0 -> 2.1: YiXuanSkin BodyB Diffuse 1024p Hash',)), (update_hash, ('89509335',))],
'89509335': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle Diffuse 1024p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('487db3e0', '7683c132'), 'YixuanTrailsOfInk.BodyB.Diffuse.2048')),
    ],
'a22695c9': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap 2048p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ed7abe1d', 'YixuanTrailsOfInk.BodyB.LightMap.1024')),
    ],

'ed7abe1d': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle LightMap 1024p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a22695c9', 'YixuanTrailsOfInk.BodyB.LightMap.2048')),
    ],
'16a1fb10': [(log, ('2.0 -> 2.1: YiXuanSkin BodyB MaterialMap 2048p Hash',)), (update_hash, ('7e6747ac',))],
'7e6747ac': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap 2048p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('9a79cf64', '229c5b0f'), 'YixuanTrailsOfInk.BodyB.MaterialMap.1024')),
    ],

'9a79cf64': [(log, ('2.0 -> 2.1: YiXuanSkin BodyB MaterialMap 1024p Hash',)), (update_hash, ('229c5b0f',))],
'229c5b0f': [
        (log,                           ('2.5: YixuanTrailsOfInk Body/Bottle MaterialMap 1024p Hash (Object B/C)',)),
        (add_section_if_missing,        ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('16a1fb10', '7e6747ac'), 'YixuanTrailsOfInk.BodyB.MaterialMap.2048')),
    ],

# Face Textures
'7d9ee001': [
        (log,                           ('2.5: YixuanTrailsOfInk Face Diffuse Hash',)),
        (add_section_if_missing,        ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],
'cc898b44': [
        (log, ('3.0: YixuanTrailsOfInk Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'd4841137': [
        (log, ('3.0: YixuanTrailsOfInk Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'd7eb400e': [
        (log, ('3.0: YixuanTrailsOfInk Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'd28b9c82': [(log, ('3.0: YixuanTrailsOfInk Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'7f5aba6c': [
        (log, ('3.0: YixuanTrailsOfInk Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'c7748cbd': [
        (log, ('3.0: YixuanTrailsOfInk Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a07eb5cf': [
        (log, ('3.0: YixuanTrailsOfInk Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'07c7e48f': [
        (log, ('3.0: YixuanTrailsOfInk Hair Shadow VB Hash',)),
        (add_section_if_missing, ('d28b9c82', 'YixuanTrailsOfInk.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4e321bef': [
        (log, ('3.0: YixuanTrailsOfInk Body VB Hash',)),
        (add_section_if_missing, ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'd1e95221': [
        (log, ('3.0: YixuanTrailsOfInk Body VB Hash',)),
        (add_section_if_missing, ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'6c57cdb1': [
        (log, ('3.0: YixuanTrailsOfInk Body VB Hash',)),
        (add_section_if_missing, ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'b5c70816': [
        (log, ('3.0: YixuanTrailsOfInk Body VB Hash',)),
        (add_section_if_missing, ('95de0d39', 'YixuanTrailsOfInk.Body.IB', 'match_priority = 0\n')),
    ],
'e0a315c0': [
        (log, ('3.0: YixuanTrailsOfInk Bottle VB Hash',)),
        (add_section_if_missing, ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'f6564b67': [
        (log, ('3.0: YixuanTrailsOfInk Bottle VB Hash',)),
        (add_section_if_missing, ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'ee08ae2a': [
        (log, ('3.0: YixuanTrailsOfInk Bottle VB Hash',)),
        (add_section_if_missing, ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'4df43644': [
        (log, ('3.0: YixuanTrailsOfInk Bottle VB Hash',)),
        (add_section_if_missing, ('064cd7d3', 'YixuanTrailsOfInk.Bottle.IB', 'match_priority = 0\n')),
    ],
'892858fd': [(log, ('3.0: YixuanTrailsOfInk Hairpin IB Hash',)), (add_ib_check_if_missing,)],
'ba017cf3': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'3194141e': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'b3123168': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'de9d3ab7': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin VB Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'2a4f37a6': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'5a291e85': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'd28370ec': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'972e4b6d': [
        (log, ('3.0: YixuanTrailsOfInk Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],
'2e04aac2': [
        (log, ('3.0: YixuanTrailsOfInk Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],
'4466e7ea': [
        (log, ('3.0: YixuanTrailsOfInk Face VB Hash',)),
        (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],
'ce38ac3b': [(log, ('3.0: YixuanTrailsOfInk weapon IB Hash',)), (add_ib_check_if_missing,)],
'9052084b': [
        (log, ('3.0: YixuanTrailsOfInk weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'f45313a0': [
        (log, ('3.0: YixuanTrailsOfInk weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'3ac6dfc7': [
        (log, ('3.0: YixuanTrailsOfInk weapon VB Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'920caf66': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'771d52eb': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'dc3c5667': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'ad3cd82a': [(log, ('3.0: YixuanTrailsOfInk misc hash',)),],
'ccbbb7ea': [(log, ('3.0: YixuanTrailsOfInk misc hash',)),],
'36a68b27': [
        (log, ('3.0: YixuanTrailsOfInk Hair VB Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'84fe943d': [
        (log, ('3.0: YixuanTrailsOfInk Hair TEX Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: YixuanTrailsOfInk Hair TEX Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'5574ca9f': [
        (log, ('3.0: YixuanTrailsOfInk Hair TEX Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'f4ac690c': [
        (log, ('3.0: YixuanTrailsOfInk Hair TEX Hash',)),
        (add_section_if_missing, ('ac8e9ee3', 'YixuanTrailsOfInk.Hair.IB', 'match_priority = 0\n')),
    ],
'd7db2bc6': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'96f754a7': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'aa1056a5': [
        (log, ('3.0: YixuanTrailsOfInk Hairpin TEX Hash',)),
        (add_section_if_missing, ('892858fd', 'YixuanTrailsOfInk.Hairpin.IB', 'match_priority = 0\n')),
    ],
'9efd1605': [
        (log, ('3.0: YixuanTrailsOfInk Face TEX Hash',)),
        (add_section_if_missing, ('8b067f99', 'YixuanTrailsOfInk.Face.IB', 'match_priority = 0\n')),
    ],
'677893d2': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'd1ee41dc': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
'23d4f666': [
        (log, ('3.0: YixuanTrailsOfInk weapon TEX Hash',)),
        (add_section_if_missing, ('ce38ac3b', 'YixuanTrailsOfInk.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YixuanTrailsOfInk',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Bottle', 'Ink', 'Face'],
}

