"""
Burnice Character Hash Commands
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
    Returns Burnice's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'f779fb81': [(log, ('1.2 - 2.5: Burnice Hair IB Hash',)), (add_ib_check_if_missing,)],
'af63e974': [(log, ('1.2 - 2.5: Burnice Body IB Hash',)), (add_ib_check_if_missing,)],
'b3f6fcb3': [(log, ('1.2 - 2.5: Burnice Head IB Hash',)), (add_ib_check_if_missing,)],
'c9c87bb1': [(log, ('1.3 -> 1.4: Burnice HeadA Diffuse 1024p Hash',)), (update_hash, ('68f0fb19',)),],
'68f0fb19': [
        (log,                           ('1.4 - 2.5: Burnice HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('c4b6bb10', 'e338bb82'), 'Burnice.HeadA.Diffuse.2048')),
    ],
'e338bb82': [(log, ('1.3 -> 1.4: Burnice HeadA Diffuse 2048p Hash',)), (update_hash, ('c4b6bb10',)),],
'c4b6bb10': [
        (log,                           ('1.4 - 2.5: Burnice HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b3f6fcb3', 'Burnice.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   (('68f0fb19', 'c9c87bb1'), 'Burnice.HeadA.Diffuse.1024')),
    ],
'609b50a9': [
        (log,                           ('1.2 - 2.5: Burnice HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4568c6b3', 'Burnice.HairA.Diffuse.1024')),
    ],
'4568c6b3': [
        (log,                           ('1.2 - 2.5: Burnice HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('609b50a9', 'Burnice.HairA.Diffuse.2048')),
    ],
'bf0042b9': [
        (log,                           ('1.2 - 2.5: Burnice HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('08770e8c', 'Burnice.HairA.LightMap.1024')),
    ],
'08770e8c': [
        (log,                           ('1.2 - 2.5: Burnice HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bf0042b9', 'Burnice.HairA.LightMap.2048')),
    ],
'5f2840f1': [
        (log,                           ('1.2 - 2.5: Burnice HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('3ae3ea20', 'Burnice.HairA.MaterialMap.1024')),
    ],
'3ae3ea20': [
        (log,                           ('1.2 - 2.5: Burnice HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('5f2840f1', 'Burnice.HairA.MaterialMap.2048')),
    ],
'438cf629': [(log, ('1.2 -> 2.5: Burnice HairA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'0050e0d2': [
        (log,                           ('1.2 - 2.5: Burnice HairA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Burnice.HairA.NormalMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Burnice HairA/BodyA NormalMap 2048p Hash (Shared)',)),
        (add_section_if_missing,        ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0050e0d2', 'Burnice.HairA.NormalMap.1024')),
    ],
'50bf6521': [
        (log,                           ('1.2 - 2.5: Burnice BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f0e67001', 'Burnice.BodyA.Diffuse.1024')),
    ],
'f0e67001': [
        (log,                           ('1.2 - 2.5: Burnice BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('50bf6521', 'Burnice.BodyA.Diffuse.2048')),
    ],
'f4e05ee7': [
        (log,                           ('1.2 - 2.5: Burnice BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0a3ba8ac', 'Burnice.BodyA.LightMap.1024')),
    ],
'0a3ba8ac': [
        (log,                           ('1.2 - 2.5: Burnice BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f4e05ee7', 'Burnice.BodyA.LightMap.2048')),
    ],
'c321481d': [
        (log,                           ('1.2 - 2.5: Burnice BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e37e7622', 'Burnice.BodyA.MaterialMap.1024')),
    ],
'e37e7622': [
        (log,                           ('1.2 - 2.5: Burnice BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c321481d', 'Burnice.BodyA.MaterialMap.2048')),
    ],
'0f2c69e2': [(log, ('1.2 -> 2.5: Burnice BodyA NormalMap 2048p Hash',)), (update_hash, ('ebac056e',)),],
'0c4f338a': [
        (log,                           ('1.2 - 2.5: Burnice BodyA NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ebac056e', 'Burnice.BodyA.NormalMap.2048')),
    ],
'511006ba': [
        (log, ('3.0: Burnice Hair VB Hash',)),
        (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
    ],
'c882e6eb': [
        (log, ('3.0: Burnice Hair VB Hash',)),
        (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
    ],
'68027115': [
        (log, ('3.0: Burnice Hair VB Hash',)),
        (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
    ],
'40aa11a7': [(log, ('3.0: Burnice Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'164e3024': [
        (log, ('3.0: Burnice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'831534e5': [
        (log, ('3.0: Burnice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'4d570d70': [
        (log, ('3.0: Burnice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9d6bbd22': [
        (log, ('3.0: Burnice Hair Shadow VB Hash',)),
        (add_section_if_missing, ('40aa11a7', 'Burnice.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'be10c4bb': [
        (log, ('3.0: Burnice Body VB Hash',)),
        (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
    ],
'208d5e15': [
        (log, ('3.0: Burnice Body VB Hash',)),
        (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
    ],
'35826de5': [
        (log, ('3.0: Burnice Body VB Hash',)),
        (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
    ],
'c705bf55': [
        (log, ('3.0: Burnice Body VB Hash',)),
        (add_section_if_missing, ('af63e974', 'Burnice.Body.IB', 'match_priority = 0\n')),
    ],
'23f842f0': [
        (log, ('3.0: Burnice Face VB Hash',)),
        (add_section_if_missing, ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
    ],
'14b70725': [
        (log, ('3.0: Burnice Face VB Hash',)),
        (add_section_if_missing, ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
    ],
'12c38959': [
        (log, ('3.0: Burnice Face VB Hash',)),
        (add_section_if_missing, ('b3f6fcb3', 'Burnice.Face.IB', 'match_priority = 0\n')),
    ],
'6b08674c': [(log, ('3.0: Burnice weapon IB Hash',)), (add_ib_check_if_missing,)],
'36821275': [
        (log, ('3.0: Burnice weapon VB Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'2981a076': [
        (log, ('3.0: Burnice weapon VB Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'a5ca368d': [
        (log, ('3.0: Burnice weapon VB Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'5f6615b0': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'5ef426d0': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'9b7dfc16': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'19ead1b7': [(log, ('3.0: Burnice misc hash',)),],
'c7e24774': [(log, ('3.0: Burnice misc hash',)),],
'c22b4efe': [
        (log, ('3.0: Burnice Hair VB Hash',)),
        (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Burnice Hair TEX Hash',)),
        (add_section_if_missing, ('f779fb81', 'Burnice.Hair.IB', 'match_priority = 0\n')),
    ],
'78876ed2': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'1ae23adc': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
'b5cb92b3': [
        (log, ('3.0: Burnice weapon TEX Hash',)),
        (add_section_if_missing, ('6b08674c', 'Burnice.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Burnice',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
