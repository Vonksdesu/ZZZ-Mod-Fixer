"""
Anton Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.2 - 3.2
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

        # ==================== Hair Component ====================
        '6b95c80d': [
            (log,                             ('1.0: Anton Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd46d8476': [
            (log,                             ('2.2: Anton Hair Draw VB Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        ],
        '8ab64867': [
            (log,                             ('2.2: Anton Hair Position VB Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        ],
        'bab585ea': [
            (log,                             ('2.2: Anton Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        ],
        '884e7cc3': [
            (log,                             ('2.2: Anton Hair Blend VB Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
        ],
        '571aa398': [
            (log,                             ('1.0: Anton HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4c4c604', 'Anton.HairA.Diffuse.1024')),
        ],
        'd4c4c604': [
            (log,                             ('1.0: Anton HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('571aa398', 'Anton.HairA.Diffuse.2048')),
        ],
        '21ee9a3f': [
            (log,                             ('1.7 -> 2.0: Anton HairA LightMap 1024p Hash',)),
            (update_hash,                     ('f6e280b0',)),
        ],
        'ee06579e': [
            (log,                             ('1.7 -> 2.0: Anton HairA LightMap 2048p Hash',)),
            (update_hash,                     ('41601dfa',)),
        ],
        '41601dfa': [
            (log,                             ('2.0: Anton HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f6e280b0', '21ee9a3f'), 'Anton.HairA.LightMap.1024')),
        ],
        'f6e280b0': [
            (log,                             ('2.0: Anton HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('41601dfa', 'ee06579e'), 'Anton.HairA.LightMap.2048')),
        ],
        '6fc654e1': [
            (log,                             ('1.7 -> 2.0: Anton HairA MaterialMap 1024p Hash',)),
            (update_hash,                     ('05bd454d',)),
        ],
        '24caeb1f': [
            (log,                             ('1.7 -> 2.0: Anton HairA MaterialMap 2048p Hash',)),
            (update_hash,                     ('d47c5823',)),
        ],
        'd47c5823': [
            (log,                             ('2.0: Anton HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('05bd454d', '6fc654e1'), 'Anton.HairA.MaterialMap.1024')),
        ],
        '05bd454d': [
            (log,                             ('2.0: Anton HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d47c5823', '24caeb1f'), 'Anton.HairA.MaterialMap.2048')),
        ],
        'ae3d5fb8': [
            (log,                             ('1.0 -> 2.0: Anton JacketA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        'd7517d0e': [
            (log,                             ('1.0 -> 2.0: Anton JacketA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '5b2ab0e0': [
            (log,                             ('1.0 -> 2.0: Anton BodyA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        '1b4ad5b7': [
            (log,                             ('1.0 -> 2.0: Anton BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '77ae203f': [
            (log,                             ('1.0 -> 2.0: Anton HairA NormalMap 1024p Hash',)),
            (update_hash,                     ('798adba3',)),
        ],
        'b216f758': [
            (log,                             ('1.0 -> 2.0: Anton HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('2.0: Anton HairA, BodyA and JacketA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Anton.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Anton.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Anton.JacketA.NormalMap.1024')),
        ],

        # ==================== Hair Shadow Component ====================
        '0112ffd6': [
            (log,                             ('2.2: Anton Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '52fa44ae': [
            (log,                             ('2.2: Anton Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '558ab813': [
            (log,                             ('2.2: Anton Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '1f1b89ae': [
            (log,                             ('2.2: Anton Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '8d0bcd2b': [
            (log,                             ('2.2: Anton Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('0112ffd6', 'Anton.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '653fb27c': [
            (log,                             ('1.0: Anton Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9f262894': [
            (log,                             ('2.2: Anton Body Draw VB Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        ],
        '339b1975': [
            (log,                             ('2.2: Anton Body Position VB Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        ],
        '66217473': [
            (log,                             ('2.2: Anton Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        ],
        '76bc385f': [
            (log,                             ('2.2: Anton Body Blend VB Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
        ],
        '00abcf22': [
            (log,                             ('1.0: Anton BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('581a0958', 'Anton.BodyA.Diffuse.1024')),
        ],
        '581a0958': [
            (log,                             ('1.0: Anton BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('00abcf22', 'Anton.BodyA.Diffuse.2048')),
        ],
        '8e5ba7d0': [
            (log,                             ('1.7 -> 2.0: Anton BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('a937bcee',)),
        ],
        '17cf1b74': [
            (log,                             ('1.7 -> 2.0: Anton BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('ed6f4199',)),
        ],
        'ed6f4199': [
            (log,                             ('2.0: Anton BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a937bcee', '8e5ba7d0'), 'Anton.BodyA.LightMap.1024')),
        ],
        'a937bcee': [
            (log,                             ('2.0: Anton BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ed6f4199', '17cf1b74'), 'Anton.BodyA.LightMap.2048')),
        ],
        'b7ce5f0b': [
            (log,                             ('1.7 -> 2.0: Anton BodyA MaterialMap 1024p Hash',)),
            (update_hash,                     ('bb25e0f0',)),
        ],
        '0238b0ff': [
            (log,                             ('1.7 -> 2.0: Anton BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('986c9716',)),
        ],
        '986c9716': [
            (log,                             ('2.0: Anton BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('bb25e0f0', 'b7ce5f0b'), 'Anton.BodyA.MaterialMap.1024')),
        ],
        'bb25e0f0': [
            (log,                             ('2.0: Anton BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('986c9716', '0238b0ff'), 'Anton.BodyA.MaterialMap.2048')),
        ],

        # ==================== Jacket Component ====================
        'a21fcee4': [
            (log,                             ('1.0: Anton Jacket IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '112ccbbd': [
            (log,                             ('2.2: Anton Jacket Draw VB Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        ],
        '9f0a8d2e': [
            (log,                             ('2.2: Anton Jacket Position VB Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        ],
        '1727e9e4': [
            (log,                             ('2.2: Anton Jacket Texcoord VB Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        ],
        '3edd7ceb': [
            (log,                             ('2.2: Anton Jacket Blend VB Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
        ],
        'd4b15508': [
            (log,                             ('1.0: Anton JacketA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f7831517', 'Anton.JacketA.Diffuse.1024')),
        ],
        'f7831517': [
            (log,                             ('1.0: Anton JacketA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d4b15508', 'Anton.JacketA.Diffuse.2048')),
        ],
        'c42628a5': [
            (log,                             ('1.7 -> 2.0: Anton JacketA LightMap 1024p Hash',)),
            (update_hash,                     ('edb33cec',)),
        ],
        '886a664a': [
            (log,                             ('1.7 -> 2.0: Anton JacketA LightMap 2048p Hash',)),
            (update_hash,                     ('ef7880e3',)),
        ],
        'ef7880e3': [
            (log,                             ('2.0: Anton JacketA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('edb33cec', 'c42628a5'), 'Anton.JacketA.LightMap.1024')),
        ],
        'edb33cec': [
            (log,                             ('2.0: Anton JacketA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ef7880e3', '886a664a'), 'Anton.JacketA.LightMap.2048')),
        ],
        'd36a2f7a': [
            (log,                             ('1.0: Anton JacketA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('75bccc40', 'Anton.JacketA.MaterialMap.1024')),
        ],
        '75bccc40': [
            (log,                             ('1.0: Anton JacketA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d36a2f7a', 'Anton.JacketA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'a0201907': [
            (log,                             ('1.0: Anton Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f7cda875': [
            (log,                             ('2.2: Anton Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
        ],
        'cddf3b32': [
            (log,                             ('2.2: Anton Face Position VB Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
        ],
        '144828a7': [
            (log,                             ('2.2: Anton Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('558c7001',)),
        ],
        '558c7001': [
            (log,                             ('3.2: Anton Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ec9763c1': [
            (log,                             ('2.2: Anton Face Blend VB Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
        ],
        '842119d6': [
            (log,                             ('1.0: Anton FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('15cb1aee', 'Anton.FaceA.Diffuse.1024')),
        ],
        '15cb1aee': [
            (log,                             ('1.0: Anton FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('842119d6', 'Anton.FaceA.Diffuse.2048')),
        ],
        'ac7fb2e2': [
            (log,                             ('1.0: Anton FaceA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('654134c1', 'Anton.FaceA.LightMap.1024')),
        ],
        '654134c1': [
            (log,                             ('1.0: Anton FaceA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a0201907', 'Anton.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ac7fb2e2', 'Anton.FaceA.LightMap.2048')),
        ],

        # ==================== Weapon Component ====================
        'a21ac290': [
            (log,                             ('2.2: Anton weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fa346a40': [
            (log,                             ('2.2: Anton weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
        ],
        '193b9ea3': [
            (log,                             ('2.2: Anton weapon Position VB Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
        ],
        '65b52652': [
            (log,                             ('2.2: Anton weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
        ],
        '2906a23f': [
            (log,                             ('2.2: Anton weapon Blend VB Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
        ],
        'dc3a9ef1': [
            (log,                             ('2.2: Anton weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('66f89e6e', 'Anton.WeaponA.Diffuse.1024')),
        ],
        '66f89e6e': [
            (log,                             ('2.2: Anton weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dc3a9ef1', 'Anton.WeaponA.Diffuse.2048')),
        ],
        '798adba3': [
            (log,                             ('2.0: Anton HairA, BodyA and JacketA NormalMap 1024p Hash, also Weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('6b95c80d', 'Anton.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('653fb27c', 'Anton.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a21fcee4', 'Anton.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Anton.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Anton.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Anton.JacketA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Anton.WeaponA.NormalMap.1024')),
        ],
        'ffdc1ea7': [
            (log,                             ('2.2: Anton weapon NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Anton.WeaponA.NormalMap.2048')),
        ],
        'cf503557': [
            (log,                             ('2.2: Anton weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3eba6997', 'Anton.WeaponA.LightMap.1024')),
        ],
        '3eba6997': [
            (log,                             ('2.2: Anton weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cf503557', 'Anton.WeaponA.LightMap.2048')),
        ],
        'bd257544': [
            (log,                             ('2.2: Anton weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9971d30', 'Anton.WeaponA.MaterialMap.1024')),
        ],
        'f9971d30': [
            (log,                             ('2.2: Anton weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('a21ac290', 'Anton.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd257544', 'Anton.WeaponA.MaterialMap.2048')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'Anton',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}