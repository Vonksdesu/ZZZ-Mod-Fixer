"""
Yanagi Character Hash Commands
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
    Returns Yanagi's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'9e12899f': [(log, ('2.5: Yanagi Hair IB Hash',)),    (add_ib_check_if_missing,)],
'13c75775': [(log, ('2.5: Yanagi Ring IB Hash',)),    (add_ib_check_if_missing,)],
'f478ee4c': [(log, ('2.5: Yanagi Body IB Hash',)),    (add_ib_check_if_missing,)],
'44d9123b': [(log, ('2.5: Yanagi Glasses IB Hash',)),    (add_ib_check_if_missing,)],
'0817204c': [(log, ('2.5: Yanagi Face IB Hash',)),    (add_ib_check_if_missing,)],

# === Hash Updates ===
'fd363c76': [(log, ('2.5: Yanagi Body blend (old hash)',)), (update_hash, ('b558d482',))],
'2e92fc77': [(log, ('2.5: Yanagi Glasses ib (old hash)',)), (update_hash, ('44d9123b',))],
'b558d482': [(log, ('2.5: Yanagi Body blend',)),    (add_ib_check_if_missing,)],

# === Face Textures ===
'cfe7ab46': [
        (log,                           ('2.5: Yanagi FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('95d9e92e', 'Yanagi.FaceA.Diffuse.2048')),
    ],
'95d9e92e': [
        (log,                           ('2.5: Yanagi FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('cfe7ab46', 'Yanagi.FaceA.Diffuse.1024')),
    ],

# === Hair Textures ===
'4edb5c79': [
        (log,                           ('2.5: Yanagi HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac5f6d76', 'Yanagi.HairA.Diffuse.2048')),
    ],
'5a43d985': [
        (log,                           ('2.5: Yanagi HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('99cfa935', 'Yanagi.HairA.LightMap.2048')),
    ],
'486e3c42': [
        (log,                           ('2.5: Yanagi HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f80b57f0', 'Yanagi.HairA.MaterialMap.2048')),
    ],
'ac5f6d76': [
        (log,                           ('2.5: Yanagi HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4edb5c79', 'Yanagi.HairA.Diffuse.1024')),
    ],
'99cfa935': [
        (log,                           ('2.5: Yanagi HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5a43d985', 'Yanagi.HairA.LightMap.1024')),
    ],
'f80b57f0': [
        (log,                           ('2.5: Yanagi HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('486e3c42', 'Yanagi.HairA.MaterialMap.1024')),
    ],

# === Body Textures ===
'c119dbd7': [
        (log,                           ('2.5: Yanagi BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c7c4f5c5', 'Yanagi.BodyA.Diffuse.2048')),
    ],
'f60602ec': [
        (log,                           ('2.5: Yanagi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('616200aa', 'Yanagi.BodyA.LightMap.2048')),
    ],
'b29f0188': [
        (log,                           ('2.5: Yanagi BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c2ae5d2b', 'Yanagi.BodyA.MaterialMap.2048')),
    ],
'c7c4f5c5': [
        (log,                           ('2.5: Yanagi BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c119dbd7', 'Yanagi.BodyA.Diffuse.1024')),
    ],
'08933e28': [(log, ('1.7 -> 2.0: Yanagi BodyA LightMap 2048p Hash',)), (update_hash, ('616200aa',))],
'616200aa': [
        (log,                           ('2.5: Yanagi BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f60602ec', 'Yanagi.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('3ffcef9e', 'f60602ec'), 'Yanagi.BodyA.LightMap.1024')),
    ],

'3ffcef9e': [
        (log,                           ('2.5: Yanagi BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f60602ec', 'Yanagi.BodyA.LightMap.1024')),
        (multiply_section_if_missing,        (('616200aa', '08933e28'), 'Yanagi.BodyA.LightMap.2048')),
    ],
'c2ae5d2b': [
        (log,                           ('2.5: Yanagi BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('b29f0188', 'Yanagi.BodyA.MaterialMap.1024')),
    ],

# === Ring Textures (shares Hair textures) ===
# Ring uses same texture hashes as Hair: ac5f6d76, 99cfa935, f80b57f0

# === Glasses Textures (shares Hair textures) ===
# Glasses uses same texture hashes as Hair: ac5f6d76, 99cfa935, f80b57f0,
'0e52a354': [
        (log, ('3.0: Yanagi Hair VB Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'42ca0c9b': [
        (log, ('3.0: Yanagi Hair VB Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'0bbe1d7d': [
        (log, ('3.0: Yanagi Hair VB Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: Yanagi Hair TEX Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'c1628e55': [(log, ('3.0: Yanagi Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'de0bb6f9': [
        (log, ('3.0: Yanagi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9c8be112': [
        (log, ('3.0: Yanagi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bb35cc80': [
        (log, ('3.0: Yanagi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'eb448ade': [
        (log, ('3.0: Yanagi Hair Shadow VB Hash',)),
        (add_section_if_missing, ('c1628e55', 'Yanagi.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'01864eed': [
        (log, ('3.0: Yanagi Hair accessories VB Hash',)),
        (add_section_if_missing, ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
    ],
'fe235fbb': [
        (log, ('3.0: Yanagi Hair accessories VB Hash',)),
        (add_section_if_missing, ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
    ],
'49188dc8': [
        (log, ('3.0: Yanagi Hair accessories VB Hash',)),
        (add_section_if_missing, ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
    ],
'07a1d434': [
        (log, ('3.0: Yanagi Hair accessories VB Hash',)),
        (add_section_if_missing, ('13c75775', 'Yanagi.Hair accessories.IB', 'match_priority = 0\n')),
    ],
'2fe26340': [
        (log, ('3.0: Yanagi Body VB Hash',)),
        (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
    ],
'7ff000de': [
        (log, ('3.0: Yanagi Body VB Hash',)),
        (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
    ],
'f4fbc5c0': [
        (log, ('3.0: Yanagi Body VB Hash',)),
        (add_section_if_missing, ('f478ee4c', 'Yanagi.Body.IB', 'match_priority = 0\n')),
    ],
'178a1ff8': [
        (log, ('3.0: Yanagi lens VB Hash',)),
        (add_section_if_missing, ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
    ],
'8e3cf210': [
        (log, ('3.0: Yanagi lens VB Hash',)),
        (add_section_if_missing, ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
    ],
'6b5d6e39': [
        (log, ('3.0: Yanagi lens VB Hash',)),
        (add_section_if_missing, ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
    ],
'dd32963a': [
        (log, ('3.0: Yanagi lens VB Hash',)),
        (add_section_if_missing, ('44d9123b', 'Yanagi.lens.IB', 'match_priority = 0\n')),
    ],
'7d20a437': [
        (log, ('3.0: Yanagi Face VB Hash',)),
        (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
    ],
'69c75b70': [
        (log, ('3.0: Yanagi Face VB Hash',)),
        (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
    ],
'4cb3e0ea': [
        (log, ('3.0: Yanagi Face VB Hash',)),
        (add_section_if_missing, ('0817204c', 'Yanagi.Face.IB', 'match_priority = 0\n')),
    ],
'27d49f0b': [(log, ('3.0: Yanagi weapon IB Hash',)), (add_ib_check_if_missing,)],
'a07928b5': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'c6d97eb4': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'74491025': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'b2aca818': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'e4891108': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'240ee9dc': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'2d7f2223': [(log, ('3.0: Yanagi weapon IB Hash',)), (add_ib_check_if_missing,)],
'03634f2c': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('2d7f2223', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'61f72721': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('2d7f2223', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'14b8daf0': [
        (log, ('3.0: Yanagi weapon VB Hash',)),
        (add_section_if_missing, ('2d7f2223', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'47323770': [(log, ('3.0: Yanagi misc hash',)),],
'9e8cddbf': [(log, ('3.0: Yanagi misc hash',)),],
'b680db32': [(log, ('3.0: Yanagi misc hash',)),],
'daba2b23': [
        (log, ('3.0: Yanagi Hair VB Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Yanagi Hair TEX Hash',)),
        (add_section_if_missing, ('9e12899f', 'Yanagi.Hair.IB', 'match_priority = 0\n')),
    ],
'9ab64737': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'd9ac4e1e': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
'd18079e5': [
        (log, ('3.0: Yanagi weapon TEX Hash',)),
        (add_section_if_missing, ('27d49f0b', 'Yanagi.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yanagi',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}

