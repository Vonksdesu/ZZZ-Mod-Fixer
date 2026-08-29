"""
Anton Character Hash Commands
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
    Returns Anton's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'6b95c80d': [(log, ('1.0: Anton Hair IB Hash',)),   (add_ib_check_if_missing,)],
'653fb27c': [(log, ('1.0: Anton Body IB Hash',)),   (add_ib_check_if_missing,)],
'a21fcee4': [(log, ('1.0: Anton Jacket IB Hash',)), (add_ib_check_if_missing,)],
'a0201907': [(log, ('1.0: Anton Head IB Hash',)),   (add_ib_check_if_missing,)],
'15cb1aee': [
        (log,                           ('1.0: Anton HeadA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('842119d6', 'Anton.HeadA.Diffuse.2048')),
    ],
'654134c1': [
        (log,                           ('1.0: Anton HeadA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ac7fb2e2', 'Anton.HeadA.LightMap.2048')),
    ],
'842119d6': [
        (log,                           ('1.0: Anton HeadA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('15cb1aee', 'Anton.HeadA.Diffuse.1024')),
    ],
'ac7fb2e2': [
        (log,                           ('1.0: Anton HeadA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a0201907', 'Anton.Head.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('654134c1', 'Anton.HeadA.LightMap.1024')),
    ],
'571aa398': [
        (log,                           ('1.0: Anton HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4c4c604', 'Anton.HairA.Diffuse.1024')),
    ],
'd4c4c604': [
        (log,                           ('1.0: Anton HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('571aa398', 'Anton.HairA.Diffuse.2048')),
    ],
'ee06579e': [
        (log,                           ('1.0→2.5: Anton HairA LightMap 2048p Hash',)),
        (update_hash,                   ('41601dfa',)),
    ],
'21ee9a3f': [
        (log,                           ('1.0→2.5: Anton HairA LightMap 1024p Hash',)),
        (update_hash,                   ('41601dfa',)),
    ],
'41601dfa': [
        (log,                           ('2.5: Anton HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('f6e280b0', '21ee9a3f'), 'Anton.HairA.LightMap.1024')),
    ],

'f6e280b0': [
        (log,                           ('2.5: Anton HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('41601dfa', 'ee06579e'), 'Anton.HairA.LightMap.2048')),
    ],
'24caeb1f': [
        (log,                           ('1.0→2.5: Anton HairA MaterialMap 2048p Hash',)),
        (update_hash,                   ('d47c5823',)),
    ],
'6fc654e1': [
        (log,                           ('1.0→2.5: Anton HairA MaterialMap 1024p Hash',)),
        (update_hash,                   ('d47c5823',)),
    ],
'd47c5823': [
        (log,                           ('2.5: Anton HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('05bd454d', '6fc654e1'), 'Anton.HairA.MaterialMap.1024')),
    ],

'05bd454d': [
        (log,                           ('2.5: Anton HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('d47c5823', '24caeb1f'), 'Anton.HairA.MaterialMap.2048')),
    ],
'b216f758': [
        (log,                           ('1.0→2.5: Anton HairA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'77ae203f': [
        (log,                           ('1.0→2.5: Anton HairA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ebac056e': [
        (log,                           ('2.5: Anton Shared NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'00abcf22': [
        (log,                           ('1.0: Anton BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('581a0958', 'Anton.BodyA.Diffuse.1024')),
    ],
'581a0958': [
        (log,                           ('1.0: Anton BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('00abcf22', 'Anton.BodyA.Diffuse.2048')),
    ],
'17cf1b74': [
        (log,                           ('1.0→2.5: Anton BodyA LightMap 2048p Hash',)),
        (update_hash,                   ('ed6f4199',)),
    ],
'8e5ba7d0': [
        (log,                           ('1.0→2.5: Anton BodyA LightMap 1024p Hash',)),
        (update_hash,                   ('ed6f4199',)),
    ],
'ed6f4199': [
        (log,                           ('2.5: Anton BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('a937bcee', '8e5ba7d0'), 'Anton.BodyA.LightMap.1024')),
    ],

'a937bcee': [
        (log,                           ('2.5: Anton BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('ed6f4199', '17cf1b74'), 'Anton.BodyA.LightMap.2048')),
    ],
'0238b0ff': [
        (log,                           ('1.0→2.5: Anton BodyA MaterialMap 2048p Hash',)),
        (update_hash,                   ('986c9716',)),
    ],
'b7ce5f0b': [
        (log,                           ('1.0→2.5: Anton BodyA MaterialMap 1024p Hash',)),
        (update_hash,                   ('986c9716',)),
    ],
'986c9716': [
        (log,                           ('2.5: Anton BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('bb25e0f0', 'b7ce5f0b'), 'Anton.BodyA.MaterialMap.1024')),
    ],

'bb25e0f0': [
        (log,                           ('2.5: Anton BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('986c9716', '0238b0ff'), 'Anton.BodyA.MaterialMap.2048')),
    ],
'1b4ad5b7': [
        (log,                           ('1.0→2.5: Anton BodyA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'5b2ab0e0': [
        (log,                           ('1.0→2.5: Anton BodyA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'd4b15508': [
        (log,                           ('1.0: Anton JacketA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f7831517', 'Anton.JacketA.Diffuse.1024')),
    ],
'f7831517': [
        (log,                           ('1.0: Anton JacketA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d4b15508', 'Anton.JacketA.Diffuse.2048')),
    ],
'886a664a': [
        (log,                           ('1.0→2.5: Anton JacketA LightMap 2048p Hash',)),
        (update_hash,                   ('ef7880e3',)),
    ],
'c42628a5': [
        (log,                           ('1.0→2.5: Anton JacketA LightMap 1024p Hash',)),
        (update_hash,                   ('ef7880e3',)),
    ],
'ef7880e3': [
        (log,                           ('2.5: Anton JacketA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('edb33cec', 'c42628a5'), 'Anton.JacketA.LightMap.1024')),
    ],

'edb33cec': [
        (log,                           ('2.5: Anton JacketA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        (('ef7880e3', '886a664a'), 'Anton.JacketA.LightMap.2048')),
    ],
'd36a2f7a': [
        (log,                           ('1.0: Anton JacketA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('75bccc40', 'Anton.JacketA.MaterialMap.1024')),
    ],
'75bccc40': [
        (log,                           ('1.0: Anton JacketA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('d36a2f7a', 'Anton.JacketA.MaterialMap.2048')),
    ],
'd7517d0e': [
        (log,                           ('1.0→2.5: Anton JacketA NormalMap 2048p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'ae3d5fb8': [
        (log,                           ('1.0→2.5: Anton JacketA NormalMap 1024p Hash',)),
        (update_hash,                   ('ebac056e',)),
    ],
'8ab64867': [
        (log, ('3.0: Anton Hair VB Hash',)),
        (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'bab585ea': [
        (log, ('3.0: Anton Hair VB Hash',)),
        (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'884e7cc3': [
        (log, ('3.0: Anton Hair VB Hash',)),
        (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
'0112ffd6': [(log, ('3.0: Anton Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'52fa44ae': [
        (log, ('3.0: Anton Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'558ab813': [
        (log, ('3.0: Anton Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'1f1b89ae': [
        (log, ('3.0: Anton Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'8d0bcd2b': [
        (log, ('3.0: Anton Hair Shadow VB Hash',)),
        (add_section_if_missing, ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9f262894': [
        (log, ('3.0: Anton Body VB Hash',)),
        (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'339b1975': [
        (log, ('3.0: Anton Body VB Hash',)),
        (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'66217473': [
        (log, ('3.0: Anton Body VB Hash',)),
        (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'76bc385f': [
        (log, ('3.0: Anton Body VB Hash',)),
        (add_section_if_missing, ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
    ],
'112ccbbd': [
        (log, ('3.0: Anton Jacket VB Hash',)),
        (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'9f0a8d2e': [
        (log, ('3.0: Anton Jacket VB Hash',)),
        (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'1727e9e4': [
        (log, ('3.0: Anton Jacket VB Hash',)),
        (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'3edd7ceb': [
        (log, ('3.0: Anton Jacket VB Hash',)),
        (add_section_if_missing, ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
    ],
'cddf3b32': [
        (log, ('3.0: Anton Face VB Hash',)),
        (add_section_if_missing, ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
    ],
'144828a7': [
        (log, ('3.0: Anton Face VB Hash',)),
        (add_section_if_missing, ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
    ],
'ec9763c1': [
        (log, ('3.0: Anton Face VB Hash',)),
        (add_section_if_missing, ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
    ],
'a21ac290': [(log, ('3.0: Anton weapon IB Hash',)), (add_ib_check_if_missing,)],
'193b9ea3': [
        (log, ('3.0: Anton weapon VB Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'65b52652': [
        (log, ('3.0: Anton weapon VB Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'2906a23f': [
        (log, ('3.0: Anton weapon VB Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'dc3a9ef1': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'cf503557': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'bd257544': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'f7cda875': [(log, ('3.0: Anton misc hash',)),],
'fa346a40': [(log, ('3.0: Anton misc hash',)),],
'66f89e6e': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'ffdc1ea7': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'3eba6997': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'f9971d30': [
        (log, ('3.0: Anton weapon TEX Hash',)),
        (add_section_if_missing, ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
    ],
'd46d8476': [
        (log, ('3.0: Anton Hair VB Hash',)),
        (add_section_if_missing, ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Anton',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
