"""
PanYinhuCulinaryJewel Character Hash Commands
ZZZ Mod Fixer v2.6
Game Version: 2.6
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns PanYinhuCulinaryJewel's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'b518e540': [
        (log,                           ('2.6: PanYinhuCulinaryJewel Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === PanYinhuCulinaryJewel Textures (BodyA) ===
'0cab7a7b': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('e9a912e7', 'PanYinhuCulinaryJewel.BodyA.Diffuse.2048')),
    ],
'e9a912e7': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('0cab7a7b', 'PanYinhuCulinaryJewel.BodyA.Diffuse.1024')),
    ],
'91bfe5cd': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('54c0f79a', 'PanYinhuCulinaryJewel.BodyA.LightMap.2048')),
    ],
'54c0f79a': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('91bfe5cd', 'PanYinhuCulinaryJewel.BodyA.LightMap.1024')),
    ],
'78cbb2e4': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('7498bd49', 'PanYinhuCulinaryJewel.BodyA.MaterialMap.2048')),
    ],
'7498bd49': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('78cbb2e4', 'PanYinhuCulinaryJewel.BodyA.MaterialMap.1024')),
    ],

# === PanYinhuCulinaryJewel Textures (BodyB) ===
'b3775104': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('8459c5e8', 'PanYinhuCulinaryJewel.BodyB.Diffuse.2048')),
    ],
'8459c5e8': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('b3775104', 'PanYinhuCulinaryJewel.BodyB.Diffuse.1024')),
    ],
'240da72f': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c7bdc86b', 'PanYinhuCulinaryJewel.BodyB.LightMap.2048')),
    ],
'c7bdc86b': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('240da72f', 'PanYinhuCulinaryJewel.BodyB.LightMap.1024')),
    ],
'bf25d6f7': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('c50582f7', 'PanYinhuCulinaryJewel.BodyB.MaterialMap.2048')),
    ],
'c50582f7': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyB MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('bf25d6f7', 'PanYinhuCulinaryJewel.BodyB.MaterialMap.1024')),
    ],

# === PanYinhuCulinaryJewel Textures (BodyC) ===
'48c0fbcc': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('10e8bc53', 'PanYinhuCulinaryJewel.BodyC.Diffuse.2048')),
    ],
'10e8bc53': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('48c0fbcc', 'PanYinhuCulinaryJewel.BodyC.Diffuse.1024')),
    ],
'eceb77a3': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('1da6b5bf', 'PanYinhuCulinaryJewel.BodyC.LightMap.2048')),
    ],
'1da6b5bf': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('eceb77a3', 'PanYinhuCulinaryJewel.BodyC.LightMap.1024')),
    ],
'40dea057': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('eb5755d6', 'PanYinhuCulinaryJewel.BodyC.MaterialMap.2048')),
    ],
'eb5755d6': [
        (log,                           ('2.6: PanYinhuCulinaryJewel BodyC MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('40dea057', 'PanYinhuCulinaryJewel.BodyC.MaterialMap.1024')),
    ],
'db608bcf': [
        (log, ('3.0: PanYinhuCulinaryJewel Body VB Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'f5b6e5b5': [
        (log, ('3.0: PanYinhuCulinaryJewel Body VB Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'06f47d71': [
        (log, ('3.0: PanYinhuCulinaryJewel Body VB Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.0: PanYinhuCulinaryJewel Body TEX Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'ebb6a59b': [(log, ('3.0: PanYinhuCulinaryJewel Face IB Hash',)), (add_ib_check_if_missing,)],
'682e8e8d': [
        (log, ('3.0: PanYinhuCulinaryJewel Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'1eee2121': [
        (log, ('3.0: PanYinhuCulinaryJewel Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'4aae3329': [
        (log, ('3.0: PanYinhuCulinaryJewel Face VB Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'ed361b8f': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'96280008': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'57446a22': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'ca72c1f0': [(log, ('3.0: PanYinhuCulinaryJewel weapon IB Hash',)), (add_ib_check_if_missing,)],
'9f8e2d91': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'f6855ee8': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'f29f44e5': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'644a4506': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('ca72c1f0', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'12d52f05': [(log, ('3.0: PanYinhuCulinaryJewel weapon IB Hash',)), (add_ib_check_if_missing,)],
'759a4b9f': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'7e980f75': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'7353a8ed': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'c39d130e': [
        (log, ('3.0: PanYinhuCulinaryJewel weapon VB Hash',)),
        (add_section_if_missing, ('12d52f05', 'PanYinhuCulinaryJewel.weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: PanYinhuCulinaryJewel Body TEX Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
'452a0918': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'3744882e': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'18dd19bf': [
        (log, ('3.0: PanYinhuCulinaryJewel Face TEX Hash',)),
        (add_section_if_missing, ('ebb6a59b', 'PanYinhuCulinaryJewel.Face.IB', 'match_priority = 0\n')),
    ],
'56b1d7f1': [
        (log, ('3.0: PanYinhuCulinaryJewel Body VB Hash',)),
        (add_section_if_missing, ('b518e540', 'PanYinhuCulinaryJewel.Body.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'PanYinhuCulinaryJewel',
    'game_versions': ['2.6'],
}
