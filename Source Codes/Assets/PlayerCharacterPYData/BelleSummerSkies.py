"""
BelleSummerSkies Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json extraction
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns BelleSummerSkies's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'43ed3c22': [(log, ('2.5: BelleSummerSkies Body IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('619c5c94',))],
'69148073': [(log, ('2.5: BelleSummerSkies Top IB Hash',)), (add_ib_check_if_missing,)],
'93f38bdd': [(log, ('2.5: BelleSummerSkies Hat IB Hash',)), (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.5: BelleSummerSkies Face IB Hash (Shared with Belle)',)), (add_ib_check_if_missing,)],
'ea055cac': [(log, ('2.5: BelleSummerSkies Hair IB Hash',)), (add_ib_check_if_missing,), (update_hash, ('a7683988',))],
'619c5c94': [(log, ('3.0: BelleSummerSkies Body IB Hash',)), (add_ib_check_if_missing,)],
'a7683988': [(log, ('3.0: BelleSummerSkies Hair IB Hash',)), (add_ib_check_if_missing,)],
'fba5908c': [(log, ('2.8: BelleSummerSkies Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],

# === Face Textures ===
'75ec3614': [
        (log,                           ('2.5: BelleSummerSkies FaceA Diffuse Hash (Shared with Belle)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
    ],

# === Hair Textures ===
'20954729': [
        (log,                           ('2.5: BelleSummerSkies HairA, TopA, HatA Diffuse 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummerSkies.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('afe23695', 'BelleSummerSkies.BodyA.Diffuse.1024')),
    ],

'afe23695': [
        (log,                           ('2.5: BelleSummerSkies HairA, TopA, HatA Diffuse 1024p Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummerSkies.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('20954729', 'BelleSummerSkies.BodyA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: BelleSummerSkies HairA, TopA, HatA NormalMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummerSkies.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
    ],
'e0a86379': [
        (log,                           ('2.8 -> 3.0: BelleSummerSkies BodyA LightMap 2048p Hash',)),
        (update_hash,                        ('60250d24',)),
    ],
'60250d24': [
        (log,                           ('2.0: BelleSummerSkies BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        (('a189eccd', '5978a2ca'), 'BelleSummerSkies.BodyA.LightMap.1024')),
    ],

'a189eccd': [
        (log,                           ('2.8 -> 3.0: BelleSummerSkies BodyA LightMap 1024p Hash',)),
        (update_hash,                        ('5978a2ca',)),
    ],
'5978a2ca': [
        (log,                           ('2.0: BelleSummerSkies BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        (('e0a86379', '60250d24'), 'BelleSummerSkies.BodyA.LightMap.2048')),
    ],
'0298fba2': [
        (log,                           ('2.5: BelleSummerSkies HairA, TopA, HatA, FaceA MaterialMap 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummerSkies.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('fbaaeb92', 'BelleSummerSkies.BodyA.MaterialMap.1024')),
    ],

'fbaaeb92': [
        (log,                           ('2.5: BelleSummerSkies HairA, TopA, HatA, FaceA MaterialMap 1024p Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummerSkies.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('0298fba2', 'BelleSummerSkies.BodyA.MaterialMap.2048')),
    ],

# === Body Textures (Classification A/B) ===
# Body Classifications A and B share the same texture set as Hair/Top/Hat
# These are already covered by the hash entries above: 20954729, ebac056e, e0a86379, 0298fba2

# === Body Textures (Classification C) ===
'24639b77': [
        (log,                           ('2.5: BelleSummerSkies BodyC Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'7947679c': [
        (log,                           ('2.5: BelleSummerSkies BodyC LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'33f28c6d': [
        (log,                           ('2.5: BelleSummerSkies BodyC MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification D) ===
'1ce58567': [
        (log,                           ('2.5: BelleSummerSkies BodyD Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('2.5: BelleSummerSkies BodyD LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('2.5: BelleSummerSkies BodyD MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'898f40fc': [
        (log, ('3.0: BelleSummerSkies Hair VB Hash',)),
        (add_section_if_missing, ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'd440bcc9': [
        (log, ('3.0: BelleSummerSkies Hair VB Hash',)),
        (add_section_if_missing, ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'b536d9e6': [
        (log, ('3.0: BelleSummerSkies Hair VB Hash',)),
        (add_section_if_missing, ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'4bb8fccc': [
        (log, ('3.0: BelleSummerSkies Hair VB Hash',)),
        (add_section_if_missing, ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'403eace9': [(log, ('3.0: BelleSummerSkies Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'd077170c': [
        (log, ('3.0: BelleSummerSkies Hair Shadow VB Hash',)),
        (add_section_if_missing, ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f2298f2e': [
        (log, ('3.0: BelleSummerSkies Hair Shadow VB Hash',)),
        (add_section_if_missing, ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'43f15315': [
        (log, ('3.0: BelleSummerSkies Hair Shadow VB Hash',)),
        (add_section_if_missing, ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'288df448': [
        (log, ('3.0: BelleSummerSkies Hair Shadow VB Hash',)),
        (add_section_if_missing, ('403eace9', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'07920753': [(log, ('3.0: BelleSummerSkies EarPendant IB Hash',)), (add_ib_check_if_missing,)],
'c4e3b1e8': [
        (log, ('3.0: BelleSummerSkies EarPendant VB Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'66a4bab6': [
        (log, ('3.0: BelleSummerSkies EarPendant VB Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'a2ee3518': [
        (log, ('3.0: BelleSummerSkies EarPendant VB Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'28720ee7': [
        (log, ('3.0: BelleSummerSkies EarPendant VB Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'3acf9aea': [(log, ('3.0: BelleSummerSkies HairPin IB Hash',)), (add_ib_check_if_missing,)],
'84a9dfca': [
        (log, ('3.0: BelleSummerSkies HairPin VB Hash',)),
        (add_section_if_missing, ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
    ],
'a678dff4': [
        (log, ('3.0: BelleSummerSkies HairPin VB Hash',)),
        (add_section_if_missing, ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
    ],
'1196668a': [
        (log, ('3.0: BelleSummerSkies HairPin VB Hash',)),
        (add_section_if_missing, ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
    ],
'6e583c52': [
        (log, ('3.0: BelleSummerSkies HairPin VB Hash',)),
        (add_section_if_missing, ('3acf9aea', 'BelleSummerSkies.HairPin.IB', 'match_priority = 0\n')),
    ],
'051d5424': [
        (log, ('3.0: BelleSummerSkies Body VB Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'b95ddd01': [
        (log, ('3.0: BelleSummerSkies Body VB Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'91cdde70': [
        (log, ('3.0: BelleSummerSkies Body VB Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'b36f6834': [
        (log, ('3.0: BelleSummerSkies Body VB Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'a1de68c0': [
        (log, ('3.0: BelleSummerSkies Tshirt VB Hash',)),
        (add_section_if_missing, ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
    ],
'324d9d21': [
        (log, ('3.0: BelleSummerSkies Tshirt VB Hash',)),
        (add_section_if_missing, ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
    ],
'881514bf': [(log, ('2.8 -> 3.0: BellesWimwear Tshirt Texcoord',)), (update_hash, ('325b4a1c',))],
'325b4a1c': [
        (log, ('3.0: BelleSummerSkies Tshirt VB Hash',)),
        (add_section_if_missing, ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
    ],
'65481194': [(log, ('2.1 -> 2.2: BellesWimwear Tshirt Blend',)), (update_hash, ('0139f7e8',))],
'0139f7e8': [(log, ('2.8 -> 3.0: BellesWimwear Tshirt Blend',)), (update_hash, ('0a00d846',))],
'0a00d846': [
        (log, ('3.0: BelleSummerSkies Tshirt VB Hash',)),
        (add_section_if_missing, ('69148073', 'BelleSummerSkies.Tshirt.IB', 'match_priority = 0\n')),
    ],
'04abceb5': [
        (log, ('3.0: BelleSummerSkies Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
    ],
'3eb95df2': [
        (log, ('3.0: BelleSummerSkies Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
    ],
'359e4502': [
        (log, ('3.0: BelleSummerSkies Face VB Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: BelleSummerSkies Hair TEX Hash',)),
        (add_section_if_missing, ('a7683988', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'08f04d95': [
        (log, ('3.0: BelleSummerSkies EarPendant TEX Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'f44f330b': [
        (log, ('3.0: BelleSummerSkies EarPendant TEX Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'7542ef4b': [
        (log, ('3.0: BelleSummerSkies EarPendant TEX Hash',)),
        (add_section_if_missing, ('07920753', 'BelleSummerSkies.EarPendant.IB', 'match_priority = 0\n')),
    ],
'b9c7f71b': [
        (log, ('3.0: BelleSummerSkies Body TEX Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'a4d3687d': [
        (log, ('3.0: BelleSummerSkies Body TEX Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'b1abe877': [
        (log, ('3.0: BelleSummerSkies Body TEX Hash',)),
        (add_section_if_missing, ('619c5c94', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'77eef7e8': [
        (log, ('3.0: BelleSummerSkies Face TEX Hash',)),
        (add_section_if_missing, ('9a9780a7', 'BelleSummerSkies.Face.IB', 'match_priority = 0\n')),
    ],
'6af00597': [(log, ('2.1 -> 2.2: BellesWimwear Body Blend',)), (update_hash, ('4f3ddd5c',))],
# =============================================================================
# BelleSummerSkies 2.8 VB Hashes (Dual-Key: 2.8 -> 3.0, active in 1024p)
# =============================================================================
'0fba192e': [
        (log, ('2.8: BelleSummerSkies Hair Shadow blend_vb Hash',)),
        (add_section_if_missing, ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'2ceb44ef': [
        (log, ('2.8: BelleSummerSkies Body draw_vb Hash',)),
        (add_section_if_missing, ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'4f3ddd5c': [
        (log, ('2.8: BelleSummerSkies Body blend_vb Hash',)),
        (add_section_if_missing, ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'537d9b9b': [
        (log, ('2.8: BelleSummerSkies Body position_vb Hash',)),
        (add_section_if_missing, ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'8823a09a': [
        (log, ('2.8: BelleSummerSkies Hair blend_vb Hash',)),
        (add_section_if_missing, ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'8c70a1df': [
        (log, ('2.8: BelleSummerSkies Hair Shadow draw_vb Hash',)),
        (add_section_if_missing, ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a8b3bbab': [
        (log, ('2.8: BelleSummerSkies Hat texcoord_vb Hash',)),
        (add_section_if_missing, ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
    ],
'af566e38': [
        (log, ('2.8: BelleSummerSkies Hair texcoord_vb Hash',)),
        (add_section_if_missing, ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'b7061769': [
        (log, ('2.8: BelleSummerSkies Hat blend_vb Hash',)),
        (add_section_if_missing, ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
    ],
'bd2cf1bc': [
        (log, ('2.8: BelleSummerSkies Hat draw_vb Hash',)),
        (add_section_if_missing, ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
    ],
'c6b1cd55': [
        (log, ('2.8: BelleSummerSkies Hat position_vb Hash',)),
        (add_section_if_missing, ('93f38bdd', 'BelleSummerSkies.Hat.IB', 'match_priority = 0\n')),
    ],
'ddf97ec8': [
        (log, ('2.8: BelleSummerSkies Hair Shadow texcoord_vb Hash',)),
        (add_section_if_missing, ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'f0740488': [
        (log, ('2.8: BelleSummerSkies Hair position_vb Hash',)),
        (add_section_if_missing, ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
'f5e62ded': [
        (log, ('2.8: BelleSummerSkies Body texcoord_vb Hash',)),
        (add_section_if_missing, ('43ed3c22', 'BelleSummerSkies.Body.IB', 'match_priority = 0\n')),
    ],
'f98fb7ca': [
        (log, ('2.8: BelleSummerSkies Hair Shadow position_vb Hash',)),
        (add_section_if_missing, ('fba5908c', 'BelleSummerSkies.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'ff8f2723': [
        (log, ('2.8: BelleSummerSkies Hair draw_vb Hash',)),
        (add_section_if_missing, ('ea055cac', 'BelleSummerSkies.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleSummerSkies',
    'game_versions': ['2.5', '3.0'],
}

