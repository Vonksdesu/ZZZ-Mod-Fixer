"""
Soukaku Character Hash Commands
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
    Returns Soukaku's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'fe70c7a3': [
            (log,                             ('2.2 - 3.2: Soukaku Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5432bbb8': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Draw VB Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        'beac45e4': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Position VB Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        '43fb429d': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        'f65883f3': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Blend VB Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        '32ea0d00': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('34a3ff5b', 'Soukaku.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('34a3ff5b', 'Soukaku.MaskA.Diffuse.1024')),
        ],
        '34a3ff5b': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('32ea0d00', 'Soukaku.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('32ea0d00', 'Soukaku.MaskA.Diffuse.2048')),
        ],
        '8498ee4d': [
            (log,                             ('1.0 - 1.7: Soukaku HairA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '0003126a': [
            (log,                             ('1.0 - 1.7: Soukaku HairA NormalMap 1024p Hash (deprecated)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Soukaku HairA, BodyA, MaskA and weaponA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Soukaku.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soukaku.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soukaku.MaskA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Soukaku.weaponA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Soukaku HairA, BodyA, MaskA and weaponA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Soukaku.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soukaku.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soukaku.MaskA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Soukaku.weaponA.NormalMap.2048')),
        ],
        '04654e94': [
            (log,                             ('1.0 - 1.7: Soukaku HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (update_hash,                     ('a70e24a2',)),
        ],
        '7bbb3d02': [
            (log,                             ('1.0 - 1.7: Soukaku HairA LightMap 1024p Hash (deprecated)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
        ],
        'a70e24a2': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5966c5e3', 'Soukaku.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('5966c5e3', 'Soukaku.MaskA.LightMap.1024')),
        ],
        '5966c5e3': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a70e24a2', 'Soukaku.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('a70e24a2', 'Soukaku.MaskA.LightMap.2048')),
        ],
        'd1444c52': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('218689cf', 'Soukaku.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('218689cf', 'Soukaku.MaskA.MaterialMap.1024')),
        ],
        '218689cf': [
            (log,                             ('2.2 - 3.2: Soukaku HairA and MaskA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('fe70c7a3', 'Soukaku.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d1444c52', 'Soukaku.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('d1444c52', 'Soukaku.MaskA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'c0ef468f': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4ece0220': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bbcd9e5a': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '9ab82a7f': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'd586de2b': [
            (log,                             ('2.2 - 3.2: Soukaku Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('c0ef468f', 'Soukaku.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'ced49ff8': [
            (log,                             ('2.2 - 3.2: Soukaku Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ff00994d': [
            (log,                             ('2.2 - 3.2: Soukaku Body Draw VB Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        ],
        'a426e353': [
            (log,                             ('2.2 - 3.2: Soukaku Body Position VB Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        ],
        '176fb4d5': [
            (log,                             ('2.2 - 3.2: Soukaku Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        ],
        'dbbbafef': [
            (log,                             ('2.2 - 3.2: Soukaku Body Blend VB Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        ],
        'ee31954b': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6f5d31fc', 'Soukaku.BodyA.Diffuse.1024')),
        ],
        '6f5d31fc': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ee31954b', 'Soukaku.BodyA.Diffuse.2048')),
        ],
        '363e3d70': [
            (log,                             ('1.0 - 1.7: Soukaku BodyA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '77c48d32': [
            (log,                             ('1.0 - 1.7: Soukaku BodyA NormalMap 1024p Hash (deprecated)',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
        ],
        '112a36a4': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c0f0bb74', 'Soukaku.BodyA.LightMap.1024')),
        ],
        'c0f0bb74': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('112a36a4', 'Soukaku.BodyA.LightMap.2048')),
        ],
        'd638ddf9': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1ec28297', 'Soukaku.BodyA.MaterialMap.1024')),
        ],
        '1ec28297': [
            (log,                             ('2.2 - 3.2: Soukaku BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ced49ff8', 'Soukaku.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d638ddf9', 'Soukaku.BodyA.MaterialMap.2048')),
        ],

        # ==================== Mask Component ====================
        '1315178e': [
            (log,                             ('2.2 - 3.2: Soukaku Mask IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ddd3fb88': [
            (log,                             ('2.2 - 3.2: Soukaku Mask Draw VB Hash',)),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        ],
        '3a6a6326': [
            (log,                             ('2.2 - 3.2: Soukaku Mask Position VB Hash',)),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        ],
        'e261ddc0': [
            (log,                             ('2.2 - 3.2: Soukaku Mask Texcoord VB Hash',)),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        ],
        '5c5d1e7c': [
            (log,                             ('2.2 - 3.2: Soukaku Mask Blend VB Hash',)),
            (add_section_if_missing,          ('1315178e', 'Soukaku.Mask.IB', 'match_priority = 0\n')),
        ],

        # ==================== Face Component ====================
        '01f7369e': [
            (log,                             ('1.0 - 1.1: Soukaku Face IB Hash',)),
            (update_hash,                     ('020f9ac6',)),
        ],
        '020f9ac6': [
            (log,                             ('2.2 - 3.2: Soukaku Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd06e95fd': [
            (log,                             ('2.2 - 3.2: Soukaku Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
        ],
        'ea7c06ba': [
            (log,                             ('2.2 - 3.2: Soukaku Face Position VB Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
        ],
        'ad41e2f6': [
            (log,                             ('1.0 - 1.1: Soukaku Face Texcoord Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c2db08f0',)),
        ],
        'c2db08f0': [
            (log,                             ('2.2 - 3.1: Soukaku Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b3f1b714',)),
        ],
        'b3f1b714': [
            (log,                             ('3.2: Soukaku Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '2d187d8f': [
            (log,                             ('2.2 - 3.2: Soukaku Face Blend VB Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
        ],
        '427b39a4': [
            (log,                             ('2.2 - 3.2: Soukaku FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2ceacde6', 'Soukaku.FaceA.Diffuse.1024')),
        ],
        '2ceacde6': [
            (log,                             ('2.2 - 3.2: Soukaku FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('020f9ac6', 'Soukaku.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('427b39a4', 'Soukaku.FaceA.Diffuse.2048')),
        ],
        '17110d01': [
            (log,                             ('1.0 - 1.7: Soukaku FaceA LightMap 2048p Hash (deprecated in 2.5)',)),
            (add_section_if_missing,          (('020f9ac6', '01f7369e'), 'Soukaku.Face.IB', 'match_priority = 0\n')),
        ],
        'c20a8c82': [
            (log,                             ('1.0 - 1.7: Soukaku FaceA LightMap 1024p Hash (deprecated in 2.5)',)),
            (add_section_if_missing,          (('020f9ac6', '01f7369e'), 'Soukaku.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon Component ====================
        '931476f6': [
            (log,                             ('2.2 - 3.2: Soukaku weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '66f9d07c': [
            (log,                             ('2.2 - 3.2: Soukaku weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
        ],
        '6b63687a': [
            (log,                             ('2.2 - 3.2: Soukaku weapon Position VB Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
        ],
        'c18afef0': [
            (log,                             ('2.2 - 3.2: Soukaku weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
        ],
        '6bf775f7': [
            (log,                             ('2.2 - 3.2: Soukaku weapon Blend VB Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
        ],
        '67177563': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d148b6b9', 'Soukaku.weaponA.Diffuse.1024')),
        ],
        'd148b6b9': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('67177563', 'Soukaku.weaponA.Diffuse.2048')),
        ],
        '7c4efb96': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a9ddf03d', 'Soukaku.weaponA.LightMap.1024')),
        ],
        'a9ddf03d': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7c4efb96', 'Soukaku.weaponA.LightMap.2048')),
        ],
        'd0796da7': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('39d92e17', 'Soukaku.weaponA.MaterialMap.1024')),
        ],
        '39d92e17': [
            (log,                             ('2.2 - 3.2: Soukaku weaponA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('931476f6', 'Soukaku.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d0796da7', 'Soukaku.weaponA.MaterialMap.2048')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Soukaku',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
