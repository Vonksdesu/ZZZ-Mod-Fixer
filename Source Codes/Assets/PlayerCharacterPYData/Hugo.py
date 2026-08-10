"""
Hugo Character Hash Commands
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
    Returns Hugo's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'45ae7079': [(log, ('1.7: Hugo Hair IB Hash',)), (add_ib_check_if_missing,)],
'b4765894': [(log, ('1.7: Hugo Body IB Hash',)), (add_ib_check_if_missing,)],
'ed26c53d': [(log, ('1.7: Hugo Coat IB Hash',)), (add_ib_check_if_missing,)],
'5db95af3': [(log, ('1.7: Hugo Badge IB Hash',)), (add_ib_check_if_missing,)],
'66b936fc': [(log, ('1.7: Hugo Face IB Hash',)), (add_ib_check_if_missing,)],
'a3064b0e': [
        (log,                           ('1.7: Hugo FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0f344a22', 'Hugo.FaceA.Diffuse.1024')),
    ],
'0f344a22': [
        (log,                           ('1.7: Hugo FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a3064b0e', 'Hugo.FaceA.Diffuse.2048')),
    ],
'f50ebb37': [
        (log,                           ('1.7: Hugo HairA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bab642c6', 'Hugo.HairA.Diffuse.1024')),
    ],
'bab642c6': [
        (log,                           ('1.7: Hugo HairA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f50ebb37', 'Hugo.HairA.Diffuse.2048')),
    ],
'94daa8f7': [
        (log,                           ('1.7: Hugo HairA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('dcf7c209', 'Hugo.HairA.LightMap.1024')),
    ],
'dcf7c209': [
        (log,                           ('1.7: Hugo HairA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('94daa8f7', 'Hugo.HairA.LightMap.2048')),
    ],
'9614f191': [
        (log,                           ('1.7: Hugo HairA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('144c15d0', 'Hugo.HairA.MaterialMap.1024')),
    ],
'144c15d0': [
        (log,                           ('1.7: Hugo HairA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9614f191', 'Hugo.HairA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('1.7: Hugo Shared NormalMap Hash',)),
        (add_section_if_missing,        ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('5db95af3', 'Hugo.Badge.IB', 'match_priority = 0\n')),
    ],
'7fa5eb2e': [
        (log,                           ('1.7: Hugo BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('2841b582', 'Hugo.BodyA.Diffuse.1024')),
    ],
'2841b582': [
        (log,                           ('1.7: Hugo BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7fa5eb2e', 'Hugo.BodyA.Diffuse.2048')),
    ],
'f9911f83': [
        (log,                           ('1.7: Hugo BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9fd99d99', 'Hugo.BodyA.LightMap.1024')),
    ],
'9fd99d99': [
        (log,                           ('1.7: Hugo BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('f9911f83', 'Hugo.BodyA.LightMap.2048')),
    ],
'c6fa84c9': [
        (log,                           ('1.7: Hugo BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('e2333ede', 'Hugo.BodyA.MaterialMap.1024')),
    ],
'e2333ede': [
        (log,                           ('1.7: Hugo BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('c6fa84c9', 'Hugo.BodyA.MaterialMap.2048')),
    ],
'348bc40f': [
        (log,                           ('1.7: Hugo CoatA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('481e8fe0', 'Hugo.CoatA.Diffuse.1024')),
    ],
'481e8fe0': [
        (log,                           ('1.7: Hugo CoatA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('348bc40f', 'Hugo.CoatA.Diffuse.2048')),
    ],
'0db80414': [
        (log,                           ('1.7: Hugo CoatA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('a951a0cf', 'Hugo.CoatA.LightMap.1024')),
    ],
'a951a0cf': [
        (log,                           ('1.7: Hugo CoatA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0db80414', 'Hugo.CoatA.LightMap.2048')),
    ],
'25b33389': [
        (log,                           ('1.7: Hugo CoatA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ec648dcb', 'Hugo.CoatA.MaterialMap.1024')),
    ],
'ec648dcb': [
        (log,                           ('1.7: Hugo CoatA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('ed26c53d', 'Hugo.Coat.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('25b33389', 'Hugo.CoatA.MaterialMap.2048')),
    ],
'5ca107db': [
        (log, ('3.0: Hugo Hair VB Hash',)),
        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
    ],
'6815370e': [
        (log, ('3.0: Hugo Hair VB Hash',)),
        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
    ],
'192f512e': [
        (log, ('3.0: Hugo Hair VB Hash',)),
        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
    ],
'b10cd0cb': [(log, ('3.0: Hugo Forehead shadow  IB Hash',)), (add_ib_check_if_missing,)],
'f62bd189': [
        (log, ('3.0: Hugo Forehead shadow  VB Hash',)),
        (add_section_if_missing, ('b10cd0cb', 'Hugo.Forehead shadow .IB', 'match_priority = 0\n')),
    ],
'a02f2bed': [
        (log, ('3.0: Hugo Forehead shadow  VB Hash',)),
        (add_section_if_missing, ('b10cd0cb', 'Hugo.Forehead shadow .IB', 'match_priority = 0\n')),
    ],
'd3e741e2': [
        (log, ('3.0: Hugo Forehead shadow  VB Hash',)),
        (add_section_if_missing, ('b10cd0cb', 'Hugo.Forehead shadow .IB', 'match_priority = 0\n')),
    ],
'75b5daef': [
        (log, ('3.0: Hugo Forehead shadow  VB Hash',)),
        (add_section_if_missing, ('b10cd0cb', 'Hugo.Forehead shadow .IB', 'match_priority = 0\n')),
    ],
'502e3af7': [(log, ('3.0: Hugo Hat IB Hash',)), (add_ib_check_if_missing,)],
'03d866ee': [
        (log, ('3.0: Hugo Hat VB Hash',)),
        (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
    ],
'5f316f49': [
        (log, ('3.0: Hugo Hat VB Hash',)),
        (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
    ],
'8c6ea40f': [
        (log, ('3.0: Hugo Hat VB Hash',)),
        (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
    ],
'8b6d72a3': [
        (log, ('3.0: Hugo Hat VB Hash',)),
        (add_section_if_missing, ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
    ],
'dceadf77': [
        (log, ('3.0: Hugo Accessories VB Hash',)),
        (add_section_if_missing, ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
    ],
'e150860c': [
        (log, ('3.0: Hugo Accessories VB Hash',)),
        (add_section_if_missing, ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
    ],
'62081bb7': [
        (log, ('3.0: Hugo Accessories VB Hash',)),
        (add_section_if_missing, ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
    ],
'f591ad1a': [
        (log, ('3.0: Hugo Accessories VB Hash',)),
        (add_section_if_missing, ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
    ],
'9557af37': [
        (log, ('3.0: Hugo Body VB Hash',)),
        (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
    ],
'78c37814': [
        (log, ('3.0: Hugo Body VB Hash',)),
        (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
    ],
'ff82a5c5': [
        (log, ('3.0: Hugo Body VB Hash',)),
        (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
    ],
'757285ba': [
        (log, ('3.0: Hugo Body VB Hash',)),
        (add_section_if_missing, ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
    ],
'78d1f45f': [
        (log, ('3.0: Hugo Jacket VB Hash',)),
        (add_section_if_missing, ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
    ],
'38efb2af': [
        (log, ('3.0: Hugo Jacket VB Hash',)),
        (add_section_if_missing, ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
    ],
'0e149ed0': [
        (log, ('3.0: Hugo Jacket VB Hash',)),
        (add_section_if_missing, ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
    ],
'06bf72ed': [
        (log, ('3.0: Hugo Jacket VB Hash',)),
        (add_section_if_missing, ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
    ],
'2e59433f': [
        (log, ('3.0: Hugo Face VB Hash',)),
        (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
    ],
'99d2733a': [
        (log, ('3.0: Hugo Face VB Hash',)),
        (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
    ],
'7c087817': [
        (log, ('3.0: Hugo Face VB Hash',)),
        (add_section_if_missing, ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
    ],
'3876e8d9': [(log, ('3.0: Hugo weapon IB Hash',)), (add_ib_check_if_missing,)],
'62ab3ad8': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'932eb21c': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'7ed2b256': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'46b26208': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'bc142031': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'8f82f802': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'c36d55cf': [(log, ('3.0: Hugo weapon IB Hash',)), (add_ib_check_if_missing,)],
'8c936c4b': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('c36d55cf', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'849665ce': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('c36d55cf', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'b64e3c83': [
        (log, ('3.0: Hugo weapon VB Hash',)),
        (add_section_if_missing, ('c36d55cf', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'144bd078': [(log, ('3.0: Hugo misc hash',)),],
'247b5b66': [(log, ('3.0: Hugo misc hash',)),],
'5fce83ff': [(log, ('3.0: Hugo misc hash',)),],
'ab8eb2e6': [
        (log, ('3.0: Hugo Hair VB Hash',)),
        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Hugo Hair TEX Hash',)),
        (add_section_if_missing, ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
    ],
'effd8352': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'636f292d': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
'171b6643': [
        (log, ('3.0: Hugo weapon TEX Hash',)),
        (add_section_if_missing, ('3876e8d9', 'Hugo.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Hugo',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
