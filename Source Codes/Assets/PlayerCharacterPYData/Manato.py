"""
Manato Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from zzz-mod-fixer_2.5a_WIP.py
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Manato's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'de57398c': [(log, ('2.5: Manato Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Textures (shared with LowerBody)
'81a04fa6': [
        (log,                           ('2.5: Manato Hair, LowerBody Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('07353b33', 'Manato.HairA.Diffuse.1024')),
    ],

'07353b33': [
        (log,                           ('2.5: Manato Hair, LowerBody Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('81a04fa6', 'Manato.HairA.Diffuse.2048')),
    ],
'2bfdcb76': [
        (log,                           ('2.5: Manato Hair, LowerBody LightMap 2048p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('20447316', 'Manato.HairA.LightMap.1024')),
    ],

'20447316': [
        (log,                           ('2.5: Manato Hair, LowerBody LightMap 1024p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2bfdcb76', 'Manato.HairA.LightMap.2048')),
    ],
'b9654ab9': [
        (log,                           ('2.5: Manato Hair, LowerBody MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b8091cf0', 'Manato.HairA.MaterialMap.1024')),
    ],

'b8091cf0': [
        (log,                           ('2.5: Manato Hair, LowerBody MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('b9654ab9', 'Manato.HairA.MaterialMap.2048')),
    ],

# === UpperBody Component ===
'f4c1c6d9': [(log, ('2.5: Manato UpperBody IB Hash',)), (add_ib_check_if_missing,)],

# UpperBody Textures (shared with Accessories)
'9e78d2c7': [
        (log,                           ('2.5: Manato UpperBody, Accessories Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9c659f1a', 'Manato.BodyA.Diffuse.1024')),
    ],

'9c659f1a': [
        (log,                           ('2.5: Manato UpperBody, Accessories Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9e78d2c7', 'Manato.BodyA.Diffuse.2048')),
    ],
'53c85c6a': [
        (log,                           ('2.5: Manato UpperBody, Accessories LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a15d0289', 'Manato.BodyA.LightMap.1024')),
    ],

'a15d0289': [
        (log,                           ('2.5: Manato UpperBody, Accessories LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('53c85c6a', 'Manato.BodyA.LightMap.2048')),
    ],
'fdc49789': [
        (log,                           ('2.5: Manato UpperBody, Accessories MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('92336a2f', 'Manato.BodyA.MaterialMap.1024')),
    ],

'92336a2f': [
        (log,                           ('2.5: Manato UpperBody, Accessories MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fdc49789', 'Manato.BodyA.MaterialMap.2048')),
    ],

# === LowerBody Component ===
'c0425328': [(log, ('2.5: Manato LowerBody IB Hash',)), (add_ib_check_if_missing,)],

# === Accessories Component ===
'fe66c6d2': [(log, ('2.5: Manato Accessories IB Hash',)), (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: Manato Shared NormalMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'Manato.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'Manato.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'Manato.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Face Component ===
'f987f156': [(log, ('2.5: Manato Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'6d1343ec': [
        (log,                           ('2.5: Manato Face Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8de251ee', 'Manato.FaceA.Diffuse.1024')),
    ],

'8de251ee': [
        (log,                           ('2.5: Manato Face Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('6d1343ec', 'Manato.FaceA.Diffuse.2048')),
    ],
'4e68e014': [
        (log, ('3.0: Manato Hair VB Hash',)),
        (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
    ],
'9fe810ff': [
        (log, ('3.0: Manato Hair VB Hash',)),
        (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
    ],
'b882d0c8': [
        (log, ('3.0: Manato Hair VB Hash',)),
        (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
    ],
'734da350': [(log, ('3.0: Manato Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'18cf9af2': [
        (log, ('3.0: Manato Hair Shadow VB Hash',)),
        (add_section_if_missing, ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'0da604ca': [
        (log, ('3.0: Manato Hair Shadow VB Hash',)),
        (add_section_if_missing, ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ade3c45f': [
        (log, ('3.0: Manato Hair Shadow VB Hash',)),
        (add_section_if_missing, ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bee7126f': [
        (log, ('3.0: Manato Hair Shadow VB Hash',)),
        (add_section_if_missing, ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9e173c09': [
        (log, ('3.0: Manato Body VB Hash',)),
        (add_section_if_missing, ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
    ],
'7d36f969': [
        (log, ('3.0: Manato Body VB Hash',)),
        (add_section_if_missing, ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
    ],
'91048d22': [
        (log, ('3.0: Manato Body VB Hash',)),
        (add_section_if_missing, ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
    ],
'ff068e07': [
        (log, ('3.0: Manato Pendant VB Hash',)),
        (add_section_if_missing, ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
    ],
'007cd149': [
        (log, ('3.0: Manato Pendant VB Hash',)),
        (add_section_if_missing, ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
    ],
'835ffec6': [
        (log, ('3.0: Manato Pendant VB Hash',)),
        (add_section_if_missing, ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
    ],
'e9379036': [
        (log, ('3.0: Manato Pendant VB Hash',)),
        (add_section_if_missing, ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
    ],
'8fe3485a': [
        (log, ('3.0: Manato Leg VB Hash',)),
        (add_section_if_missing, ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
    ],
'918946ee': [
        (log, ('3.0: Manato Leg VB Hash',)),
        (add_section_if_missing, ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
    ],
'd81e178a': [
        (log, ('3.0: Manato Leg VB Hash',)),
        (add_section_if_missing, ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
    ],
'0fd41a37': [
        (log, ('3.0: Manato Face VB Hash',)),
        (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],
'e5c84069': [
        (log, ('3.0: Manato Face VB Hash',)),
        (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],
'c1f10814': [(log, ('3.0: Manato weapon IB Hash',)), (add_ib_check_if_missing,)],
'd4141703': [
        (log, ('3.0: Manato weapon VB Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'f693b9de': [
        (log, ('3.0: Manato weapon VB Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'34a20b76': [
        (log, ('3.0: Manato weapon VB Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'ea7d80ff': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'c52d4279': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'aef57b5d': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'84fa3702': [(log, ('3.0: Manato misc hash',)),],
'ef07f453': [(log, ('3.0: Manato misc hash',)),],
'0932100e': [
        (log, ('3.0: Manato Hair VB Hash',)),
        (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Manato Hair TEX Hash',)),
        (add_section_if_missing, ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
    ],
'bd8621a4': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'38f2e62a': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'bf621a3b': [
        (log, ('3.0: Manato weapon TEX Hash',)),
        (add_section_if_missing, ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
    ],
'd5156714': [
        (log, ('3.0: Manato Face VB Hash',)),
        (add_section_if_missing, ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
    ],
'2aa2324a': [
        (log, ('3.0: Manato Leg VB Hash',)),
        (add_section_if_missing, ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
    ],
'8524918a': [
        (log, ('3.0: Manato Body VB Hash',)),
        (add_section_if_missing, ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Manato',
    'game_versions': ['2.5'],
}
