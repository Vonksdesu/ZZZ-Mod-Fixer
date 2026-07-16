"""
BelleSummer Character Hash Commands
ZZZ Mod Fixer v3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns BelleSummer's hash commands dictionary.
    """
    return {

# === IB Hashes ===
'69148073': [(log, ('2.8: BelleSummer Top IB Hash',)),                  (add_ib_check_if_missing,)],
'9a9780a7': [(log, ('2.8: BelleSummer Face IB Hash',)),                 (add_ib_check_if_missing,)],

# === IB Hashes (v3.0 Target) ===
'a7683988': [(log, ('3.0: BelleSummer Hair IB Hash',)),                 (add_ib_check_if_missing,)],
'403eace9': [(log, ('3.0: BelleSummer Hair Shadow IB Hash',)),          (add_ib_check_if_missing,)],
'07920753': [(log, ('3.0: BelleSummer EarPendant IB Hash',)),           (add_ib_check_if_missing,)],
'3acf9aea': [(log, ('3.0: BelleSummer HairPin IB Hash',)),              (add_ib_check_if_missing,)],
'619c5c94': [(log, ('3.0: BelleSummer Body IB Hash',)),                 (add_ib_check_if_missing,)],

# === IB Hashes (BelleSkin v2.0 Historical) ===

# === VB Hashes ===
# Hair

# Hair Shadow

# Hat

# Body

# Tshirt

# Face

# === 3.0 Database Updates (Strict Sync) ===
# Hair VBs

# Hair Shadow VBs

# EarPendant VBs

# HairPin VBs

# Body VBs

# Tshirt VBs

# Face VBs

# === Legacy Hash Updates ===

# === Face Textures ===
'75ec3614': [
        (log,                           ('2.8: BelleSummer FaceA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===

# === Hair, Top, Hat Shared Textures ===
'20954729': [
        (log,                           ('2.8 -> 3.0: BelleSummer HairA, TopA, HatA Diffuse Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.8 -> 3.0: BelleSummer HairA, TopA, HatA NormalMap Hash (Shared) [Legacy]',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'60250d24': [
        (log,                           ('3.0: BelleSummer Hair, Top, Hat, Body LightMap Hash',)),
        (add_section_if_missing,        ('a7683988', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'0298fba2': [
        (log,                           ('2.8: BelleSummer HairA, TopA, HatA, FaceA MaterialMap Hash (Shared)',)),
        (add_section_if_missing,        ('ea055cac', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('69148073', 'BelleSummer.Top.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('93f38bdd', 'BelleSummer.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification C) ===
'24639b77': [
        (log,                           ('2.8: BelleSummer BodyC Diffuse Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'7947679c': [
        (log,                           ('2.8: BelleSummer BodyC LightMap Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],
'33f28c6d': [
        (log,                           ('2.8: BelleSummer BodyC MaterialMap Hash 1024p',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Classification D) ===
'1ce58567': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories Diffuse Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'7d562f53': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories LightMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],
'34bdb036': [
        (log,                           ('2.8 -> 3.0: BelleSummer BodyD / Accessories MaterialMap Hash',)),
        (add_section_if_missing,        ('43ed3c22', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('619c5c94', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('3acf9aea', 'BelleSummer.HairPin.IB', 'match_priority = 0\n')),
    ],

# === BelleSkin Body Textures (v2.0 Historical) ===
    '04abceb5': [(log, ('2.8: BelleTemple Face draw_vb',)),                 (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],
    '28720ee7': [(log, ('3.0: Belle EarPendant blend_vb',)),                  (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
    '359e4502': [(log, ('3.0: BelleTemple Face blend_vb',)),                 (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],
    '3eb95df2': [(log, ('2.8: BelleTemple Face position_vb',)),             (add_section_if_missing, ('9a9780a7', 'BelleSummer.Face.IB', 'match_priority = 0\n'))],
    '66a4bab6': [(log, ('3.0: Belle EarPendant position_vb',)),               (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
    '6e583c52': [(log, ('3.0: Belle Hair blend_vb',)),                        (add_section_if_missing, ('3acf9aea', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
    '84a9dfca': [(log, ('3.0: Belle Hair draw_vb',)),                         (add_section_if_missing, ('3acf9aea', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
    'a2ee3518': [(log, ('3.0: Belle EarPendant texcoord_vb',)),               (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
    'a678dff4': [(log, ('3.0: Belle Hair position_vb',)),                     (add_section_if_missing, ('3acf9aea', 'BelleSummer.Hair.IB', 'match_priority = 0\n'))],
    'c4e3b1e8': [(log, ('3.0: Belle EarPendant draw_vb',)),                   (add_section_if_missing, ('07920753', 'BelleSummer.EarPendant.IB', 'match_priority = 0\n'))],
    '051d5424': [(log, ('3.0: BelleSummer Body draw_vb',)), (add_section_if_missing, ('051d5424', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '0a00d846': [(log, ('3.0: BelleSummer Tshirt blend_vb',)), (add_section_if_missing, ('0a00d846', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '1196668a': [(log, ('3.0: BelleSummer HairPin texcoord_vb',)), (add_section_if_missing, ('1196668a', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '288df448': [(log, ('3.0: BelleSummer Hair Shadow blend_vb',)), (add_section_if_missing, ('288df448', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '324d9d21': [(log, ('3.0: BelleSummer Tshirt position_vb',)), (add_section_if_missing, ('324d9d21', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '325b4a1c': [(log, ('3.0: BelleSummer Tshirt texcoord_vb',)), (add_section_if_missing, ('325b4a1c', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '43f15315': [(log, ('3.0: BelleSummer Hair Shadow texcoord_vb',)), (add_section_if_missing, ('43f15315', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '4bb8fccc': [(log, ('3.0: BelleSummer Hair blend_vb',)), (add_section_if_missing, ('4bb8fccc', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '898f40fc': [(log, ('3.0: BelleSummer Hair draw_vb',)), (add_section_if_missing, ('898f40fc', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '91cdde70': [(log, ('3.0: BelleSummer Body texcoord_vb',)), (add_section_if_missing, ('91cdde70', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'a1de68c0': [(log, ('3.0: BelleSummer Tshirt draw_vb',)), (add_section_if_missing, ('a1de68c0', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'b36f6834': [(log, ('3.0: BelleSummer Body blend_vb',)), (add_section_if_missing, ('b36f6834', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'b536d9e6': [(log, ('3.0: BelleSummer Hair texcoord_vb',)), (add_section_if_missing, ('b536d9e6', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'b95ddd01': [(log, ('3.0: BelleSummer Body position_vb',)), (add_section_if_missing, ('b95ddd01', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'd077170c': [(log, ('3.0: BelleSummer Hair Shadow draw_vb',)), (add_section_if_missing, ('d077170c', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'd440bcc9': [(log, ('3.0: BelleSummer Hair position_vb',)), (add_section_if_missing, ('d440bcc9', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    'f2298f2e': [(log, ('3.0: BelleSummer Hair Shadow position_vb',)), (add_section_if_missing, ('f2298f2e', 'BelleSummer.Unknown.IB', 'match_priority = 0\n'))],
    '0139f7e8': [(log, ('2.8 -> 3.0: BelleSummer Tshirt Blend',)), (update_hash, ('0a00d846',))],
    '43ed3c22': [(log, ('2.1 -> 2.2: BelleSummer Body IB Hash [Legacy]',)), (update_hash, ('619c5c94',))],
    '881514bf': [(log, ('2.8 -> 3.0: BelleSummer Tshirt Texcoord',)), (update_hash, ('325b4a1c',))],
    'bea4a483': [(log, ('2.0 -> 2.1: Belle Hair IB Hash [Legacy]',)), (update_hash, ('3acf9aea',))],
    'e0a86379': [(log, ('2.4 -> 2.5: BelleSummer LightMap 2048p Hash [Legacy]',)), (update_hash, ('60250d24',))],
    'ea055cac': [(log, ('2.1 -> 2.2: BelleSummer Hair IB Hash [Legacy]',)), (update_hash, ('a7683988',))],
    '0c9a075b': [(log, ('2.8 -> 3.0: Belle Face blend_vb Hash [Legacy]',)), (update_hash, ('359e4502',))],
    '65481194': [(log, ('2.1 -> 2.2: Belle blend_vb Hash [Legacy]',)), (update_hash, ('0139f7e8',))],
    '0fba192e': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('0fba192e', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '2ceb44ef': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('2ceb44ef', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '4f3ddd5c': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('4f3ddd5c', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '537d9b9b': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('537d9b9b', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '8823a09a': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('8823a09a', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '8c70a1df': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('8c70a1df', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '93f38bdd': [(log, ('2.0: BelleSummer Hat IB Hash',)), (add_ib_check_if_missing,)],
    'a8b3bbab': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('a8b3bbab', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'af566e38': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('af566e38', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'b7061769': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('b7061769', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'bd2cf1bc': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('bd2cf1bc', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'c6b1cd55': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('c6b1cd55', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'ddf97ec8': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('ddf97ec8', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'f0740488': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('f0740488', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'f5e62ded': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('f5e62ded', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'f98fb7ca': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('f98fb7ca', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'fba5908c': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('fba5908c', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    'ff8f2723': [(log, ('3.0: BelleSummer Unknown Component Hash',)), (add_section_if_missing, ('ff8f2723', 'BelleSummer.py.Unknown.IB', 'match_priority = 0\n'))],
    '08f04d95': [(log,                           ('1.0: Belle HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1ce58567', 'BelleSummer.HairA.Diffuse.2048')),],
    '5978a2ca': [(log,                           ('2.0: BelleSummer BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,   (('e0a86379','60250d24'), 'BelleSummer.BodyA.LightMap.2048')),],
    '7542ef4b': [(log,                           ('1.0: Belle HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('34bdb036', '24c47ca5'), 'BelleSummer.HairA.MaterialMap.2048')),],
    '77eef7e8': [(log,                           ('1.0: Belle HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9a9780a7', 'BelleSummer.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75ec3614', 'BelleSummer.HeadA.Diffuse.2048')),],
    '798adba3': [(log,                           ('1.0: BelleSummer HairA NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('21e98aeb', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('27185819', 'BelleSummer.HairA.NormalMap.1024')),],
    'a4d3687d': [(log,                           ('1.0: Belle BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7947679c', 'bf286c84'), 'BelleSummer.BodyA.LightMap.2048')),],
    'afe23695': [(log,                           ('2.0: BelleSummer BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('20954729', 'BelleSummer.BodyA.Diffuse.2048')),],
    'b1abe877': [(log,                           ('1.0: Belle BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('33f28c6d', 'BelleSummer.BodyA.MaterialMap.2048')),],
    'b9c7f71b': [(log,                           ('1.0: Belle BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('1817f3ca', 'BelleSummer.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('24639b77', 'd2960560'), 'BelleSummer.BodyA.Diffuse.2048')),],
    'f44f330b': [(log,                           ('2.0: Belle HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('bea4a483', 'BelleSummer.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('7d562f53', 'f1ee2105'), 'BelleSummer.HairA.LightMap.2048')),],
    'fbaaeb92': [(log,                           ('2.0: BelleSummer BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('0298fba2', 'BelleSummer.BodyA.MaterialMap.2048')),],
    '6af00597': [(log, ('2.1 -> 2.2: BelleSummer Body Blend',)), (update_hash, ('4f3ddd5c',))],
    'a189eccd': [(log, ('2.4 -> 2.5: Belle LightMap 1024p Hash [Legacy]',)), (update_hash, ('5978a2ca',))],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'BelleSummer',
    'game_versions': ['2.0', '2.1', '2.2', '2.8', '3.0'],
}