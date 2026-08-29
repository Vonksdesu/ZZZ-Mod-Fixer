"""
ManatoWhiteHeartSilhouette Character Hash Commands
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
    Returns ManatoWhiteHeartSilhouette's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'de57398c': [(log, ('2.5: ManatoWhiteHeartSilhouette Hair IB Hash',)), (add_ib_check_if_missing,)],

# Hair Textures (shared with LowerBody)
'c11e3a48': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette Hair, LowerBody Diffuse Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhiteHeartSilhouette.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhiteHeartSilhouette.LowerBody.IB', 'match_priority = 0\n')),
    ],
'a886faaf': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette Hair, LowerBody LightMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhiteHeartSilhouette.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhiteHeartSilhouette.LowerBody.IB', 'match_priority = 0\n')),
    ],
'd97b73ec': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette Hair, LowerBody MaterialMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhiteHeartSilhouette.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhiteHeartSilhouette.LowerBody.IB', 'match_priority = 0\n')),
    ],

# === UpperBody Component ===
'f4c1c6d9': [(log, ('2.5: ManatoWhiteHeartSilhouette UpperBody IB Hash',)), (add_ib_check_if_missing,)],

# UpperBody Textures (shared with Accessories)
'efd9e33e': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette UpperBody, Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhiteHeartSilhouette.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhiteHeartSilhouette.Accessories.IB', 'match_priority = 0\n')),
    ],
'43b47f20': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette UpperBody, Accessories LightMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhiteHeartSilhouette.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhiteHeartSilhouette.Accessories.IB', 'match_priority = 0\n')),
    ],
'b467ed79': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette UpperBody, Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhiteHeartSilhouette.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhiteHeartSilhouette.Accessories.IB', 'match_priority = 0\n')),
    ],

# === LowerBody Component ===
'c0425328': [(log, ('2.5: ManatoWhiteHeartSilhouette LowerBody IB Hash',)), (add_ib_check_if_missing,)],

# === Accessories Component ===
'fe66c6d2': [(log, ('2.5: ManatoWhiteHeartSilhouette Accessories IB Hash',)), (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette Shared NormalMap Hash',)),
        (add_section_if_missing,        ('de57398c', 'ManatoWhiteHeartSilhouette.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('f4c1c6d9', 'ManatoWhiteHeartSilhouette.UpperBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('c0425328', 'ManatoWhiteHeartSilhouette.LowerBody.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('fe66c6d2', 'ManatoWhiteHeartSilhouette.Accessories.IB', 'match_priority = 0\n')),
    ],

# === Face Component ===
'f987f156': [(log, ('2.5: ManatoWhiteHeartSilhouette Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'6d1343ec': [
        (log,                           ('2.5: ManatoWhiteHeartSilhouette Face Diffuse Hash',)),
        (add_section_if_missing,        ('f987f156', 'ManatoWhiteHeartSilhouette.Face.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'ManatoWhiteHeartSilhouette',
    'game_versions': ['2.5'],
}
