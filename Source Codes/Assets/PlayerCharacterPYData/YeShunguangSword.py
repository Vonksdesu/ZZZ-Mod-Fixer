"""
YeShunguangSword Character Hash Commands
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
    Returns YeShunguangSword's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'93c3c2b7': [(log, ('2.5: YeShunguangSword Sword IB Hash',)),         (add_ib_check_if_missing,)],

# === Shared NormalMap ===
'ebac056e': [
        (log,                           ('2.5: YeShunguangSword Shared NormalMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Shared.NormalMap', 'match_priority = 0\n')),
    ],

# === Sword Textures ===
'7eb1ca38': [
        (log,                           ('2.5: YeShunguangSword SwordA Diffuse Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'90250152': [
        (log,                           ('2.5: YeShunguangSword SwordA LightMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'a355e13d': [
        (log,                           ('2.5: YeShunguangSword SwordA MaterialMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
'3304ca16': [
        (log,                           ('2.5: YeShunguangSword SwordA EffectMap Hash',)),
        (add_section_if_missing,        ('93c3c2b7', 'YeShunguangSword.Sword.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YeShunguangSword',
    'game_versions': ['2.5'],
}
