"""
Hugo Character Hash Commands
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
    Returns Hugo's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '45ae7079': [
            (log,                             ('2.2 - 3.2: Hugo Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ab8eb2e6': [
            (log,                             ('2.2 - 3.2: Hugo Hair Draw VB Hash',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        ],
        '5ca107db': [
            (log,                             ('2.2 - 3.2: Hugo Hair Position VB Hash',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        ],
        '6815370e': [
            (log,                             ('2.2 - 3.2: Hugo Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        ],
        '192f512e': [
            (log,                             ('2.2 - 3.2: Hugo Hair Blend VB Hash',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
        ],
        'f50ebb37': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bab642c6', 'Hugo.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bab642c6', 'Hugo.HatA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bab642c6', 'Hugo.AccessoriesA.Diffuse.1024')),
            (multiply_section_if_missing,     ('bab642c6', 'Hugo.weapon - 镰刀C.Diffuse.1024')),
        ],
        'bab642c6': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f50ebb37', 'Hugo.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f50ebb37', 'Hugo.HatA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f50ebb37', 'Hugo.AccessoriesA.Diffuse.2048')),
            (multiply_section_if_missing,     ('f50ebb37', 'Hugo.weapon - 镰刀C.Diffuse.2048')),
        ],
        '94daa8f7': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dcf7c209', 'Hugo.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('dcf7c209', 'Hugo.HatA.LightMap.1024')),
            (multiply_section_if_missing,     ('dcf7c209', 'Hugo.AccessoriesA.LightMap.1024')),
            (multiply_section_if_missing,     ('dcf7c209', 'Hugo.weapon - 镰刀C.LightMap.1024')),
        ],
        'dcf7c209': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('94daa8f7', 'Hugo.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('94daa8f7', 'Hugo.HatA.LightMap.2048')),
            (multiply_section_if_missing,     ('94daa8f7', 'Hugo.AccessoriesA.LightMap.2048')),
            (multiply_section_if_missing,     ('94daa8f7', 'Hugo.weapon - 镰刀C.LightMap.2048')),
        ],
        '9614f191': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('144c15d0', 'Hugo.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('144c15d0', 'Hugo.HatA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('144c15d0', 'Hugo.AccessoriesA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('144c15d0', 'Hugo.weapon - 镰刀C.MaterialMap.1024')),
        ],
        '144c15d0': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA and weapon - 镰刀C MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9614f191', 'Hugo.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9614f191', 'Hugo.HatA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9614f191', 'Hugo.AccessoriesA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('9614f191', 'Hugo.weapon - 镰刀C.MaterialMap.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA, BodyA, JacketA, weapon - 镰刀A, weapon - 镰刀B, weapon - 镰刀C and weapon - 匕首 NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.HatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.AccessoriesA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.JacketA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.weapon - 镰刀A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.weapon - 镰刀B.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.weapon - 镰刀C.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Hugo.weapon - 匕首.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Hugo HairA, HatA, AccessoriesA, BodyA, JacketA, weapon - 镰刀A, weapon - 镰刀B, weapon - 镰刀C and weapon - 匕首 NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('45ae7079', 'Hugo.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.HatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.AccessoriesA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.JacketA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.weapon - 镰刀A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.weapon - 镰刀B.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.weapon - 镰刀C.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Hugo.weapon - 匕首.NormalMap.2048')),
        ],

        # ==================== Forehead shadow Component ====================
        'b10cd0cb': [
            (log,                             ('2.2 - 3.2: Hugo Forehead shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f62bd189': [
            (log,                             ('2.2 - 3.2: Hugo Forehead shadow Draw VB Hash',)),
            (add_section_if_missing,          ('b10cd0cb', 'Hugo.Forehead shadow.IB', 'match_priority = 0\n')),
        ],
        'a02f2bed': [
            (log,                             ('2.2 - 3.2: Hugo Forehead shadow Position VB Hash',)),
            (add_section_if_missing,          ('b10cd0cb', 'Hugo.Forehead shadow.IB', 'match_priority = 0\n')),
        ],
        'd3e741e2': [
            (log,                             ('2.2 - 3.2: Hugo Forehead shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('b10cd0cb', 'Hugo.Forehead shadow.IB', 'match_priority = 0\n')),
        ],
        '75b5daef': [
            (log,                             ('2.2 - 3.2: Hugo Forehead shadow Blend VB Hash',)),
            (add_section_if_missing,          ('b10cd0cb', 'Hugo.Forehead shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hat Component ====================
        '502e3af7': [
            (log,                             ('2.2 - 3.2: Hugo Hat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '03d866ee': [
            (log,                             ('2.2 - 3.2: Hugo Hat Draw VB Hash',)),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
        ],
        '5f316f49': [
            (log,                             ('2.2 - 3.2: Hugo Hat Position VB Hash',)),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
        ],
        '8c6ea40f': [
            (log,                             ('2.2 - 3.2: Hugo Hat Texcoord VB Hash',)),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
        ],
        '8b6d72a3': [
            (log,                             ('2.2 - 3.2: Hugo Hat Blend VB Hash',)),
            (add_section_if_missing,          ('502e3af7', 'Hugo.Hat.IB', 'match_priority = 0\n')),
        ],
        # Hat shares its Diffuse/LightMap/MaterialMap with Hair, and NormalMap with Hair; see that Component above.

        # ==================== Accessories Component ====================
        '5db95af3': [
            (log,                             ('2.2 - 3.2: Hugo Accessories IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dceadf77': [
            (log,                             ('2.2 - 3.2: Hugo Accessories Draw VB Hash',)),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
        ],
        'e150860c': [
            (log,                             ('2.2 - 3.2: Hugo Accessories Position VB Hash',)),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
        ],
        '62081bb7': [
            (log,                             ('2.2 - 3.2: Hugo Accessories Texcoord VB Hash',)),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
        ],
        'f591ad1a': [
            (log,                             ('2.2 - 3.2: Hugo Accessories Blend VB Hash',)),
            (add_section_if_missing,          ('5db95af3', 'Hugo.Accessories.IB', 'match_priority = 0\n')),
        ],
        # Accessories shares its Diffuse/LightMap/MaterialMap with Hair, and NormalMap with Hair; see that Component above.

        # ==================== Body Component ====================
        'b4765894': [
            (log,                             ('2.2 - 3.2: Hugo Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9557af37': [
            (log,                             ('2.2 - 3.2: Hugo Body Draw VB Hash',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        ],
        '78c37814': [
            (log,                             ('2.2 - 3.2: Hugo Body Position VB Hash',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        ],
        'ff82a5c5': [
            (log,                             ('2.2 - 3.2: Hugo Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        ],
        '757285ba': [
            (log,                             ('2.2 - 3.2: Hugo Body Blend VB Hash',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
        ],
        '7fa5eb2e': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2841b582', 'Hugo.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('2841b582', 'Hugo.weapon - 镰刀B.Diffuse.1024')),
        ],
        '2841b582': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7fa5eb2e', 'Hugo.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('7fa5eb2e', 'Hugo.weapon - 镰刀B.Diffuse.2048')),
        ],
        'f9911f83': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9fd99d99', 'Hugo.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('9fd99d99', 'Hugo.weapon - 镰刀B.LightMap.1024')),
        ],
        '9fd99d99': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f9911f83', 'Hugo.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('f9911f83', 'Hugo.weapon - 镰刀B.LightMap.2048')),
        ],
        'c6fa84c9': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e2333ede', 'Hugo.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('e2333ede', 'Hugo.weapon - 镰刀B.MaterialMap.1024')),
        ],
        'e2333ede': [
            (log,                             ('2.2 - 3.2: Hugo BodyA and weapon - 镰刀B MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('b4765894', 'Hugo.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c6fa84c9', 'Hugo.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('c6fa84c9', 'Hugo.weapon - 镰刀B.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Jacket Component ====================
        'ed26c53d': [
            (log,                             ('2.2 - 3.2: Hugo Jacket IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '78d1f45f': [
            (log,                             ('2.2 - 3.2: Hugo Jacket Draw VB Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
        ],
        '38efb2af': [
            (log,                             ('2.2 - 3.2: Hugo Jacket Position VB Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
        ],
        '0e149ed0': [
            (log,                             ('2.2 - 3.2: Hugo Jacket Texcoord VB Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
        ],
        '06bf72ed': [
            (log,                             ('2.2 - 3.2: Hugo Jacket Blend VB Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
        ],
        '348bc40f': [
            (log,                             ('2.2 - 3.2: Hugo JacketA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('481e8fe0', 'Hugo.JacketA.Diffuse.1024')),
        ],
        '481e8fe0': [
            (log,                             ('2.2 - 3.2: Hugo JacketA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('348bc40f', 'Hugo.JacketA.Diffuse.2048')),
        ],
        '0db80414': [
            (log,                             ('2.2 - 3.2: Hugo JacketA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a951a0cf', 'Hugo.JacketA.LightMap.1024')),
        ],
        'a951a0cf': [
            (log,                             ('2.2 - 3.2: Hugo JacketA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0db80414', 'Hugo.JacketA.LightMap.2048')),
        ],
        '25b33389': [
            (log,                             ('2.2 - 3.2: Hugo JacketA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ec648dcb', 'Hugo.JacketA.MaterialMap.1024')),
        ],
        'ec648dcb': [
            (log,                             ('2.2 - 3.2: Hugo JacketA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ed26c53d', 'Hugo.Jacket.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('25b33389', 'Hugo.JacketA.MaterialMap.2048')),
        ],
        # Jacket shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        '66b936fc': [
            (log,                             ('2.2 - 3.2: Hugo Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '144bd078': [
            (log,                             ('2.2 - 3.2: Hugo Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        ],
        '2e59433f': [
            (log,                             ('2.2 - 3.2: Hugo Face Position VB Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        ],
        '99d2733a': [
            (log,                             ('2.2 - 3.1: Hugo Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('0aacc89a',)),
        ],
        '0aacc89a': [
            (log,                             ('3.2: Hugo Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '7c087817': [
            (log,                             ('2.2 - 3.2: Hugo Face Blend VB Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
        ],
        'a3064b0e': [
            (log,                             ('2.2 - 3.2: Hugo FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0f344a22', 'Hugo.FaceA.Diffuse.1024')),
        ],
        '0f344a22': [
            (log,                             ('2.2 - 3.2: Hugo FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('66b936fc', 'Hugo.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a3064b0e', 'Hugo.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon - 镰刀 Component ====================
        '3876e8d9': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5fce83ff': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '62ab3ad8': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀 Position VB Hash',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '932eb21c': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀 Texcoord VB Hash',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '7ed2b256': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀 Blend VB Hash',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
        ],
        '46b26208': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('effd8352', 'Hugo.weapon - 镰刀A.Diffuse.1024')),
            (multiply_section_if_missing,     ('effd8352', 'Hugo.weapon - 匕首.Diffuse.1024')),
        ],
        'effd8352': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('46b26208', 'Hugo.weapon - 镰刀A.Diffuse.2048')),
            (multiply_section_if_missing,     ('46b26208', 'Hugo.weapon - 匕首.Diffuse.2048')),
        ],
        'bc142031': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('636f292d', 'Hugo.weapon - 镰刀A.LightMap.1024')),
            (multiply_section_if_missing,     ('636f292d', 'Hugo.weapon - 匕首.LightMap.1024')),
        ],
        '636f292d': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc142031', 'Hugo.weapon - 镰刀A.LightMap.2048')),
            (multiply_section_if_missing,     ('bc142031', 'Hugo.weapon - 匕首.LightMap.2048')),
        ],
        '8f82f802': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('171b6643', 'Hugo.weapon - 镰刀A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('171b6643', 'Hugo.weapon - 匕首.MaterialMap.1024')),
        ],
        '171b6643': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 镰刀A and weapon - 匕首 MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('3876e8d9', 'Hugo.weapon - 镰刀.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8f82f802', 'Hugo.weapon - 镰刀A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('8f82f802', 'Hugo.weapon - 匕首.MaterialMap.2048')),
        ],
        # weapon - 镰刀 shares its NormalMap hashes with Hair, its second object texture set with Body, and its third object texture set with Hair; see those Components above.

        # ==================== Weapon - 匕首 Component ====================
        'c36d55cf': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 匕首 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '247b5b66': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 匕首 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
        ],
        '8c936c4b': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 匕首 Position VB Hash',)),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
        ],
        '849665ce': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 匕首 Texcoord VB Hash',)),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
        ],
        'b64e3c83': [
            (log,                             ('2.2 - 3.2: Hugo weapon - 匕首 Blend VB Hash',)),
            (add_section_if_missing,          ('c36d55cf', 'Hugo.weapon - 匕首.IB', 'match_priority = 0\n')),
        ],
        # weapon - 匕首 shares its Diffuse/LightMap/MaterialMap with weapon - 镰刀A, and NormalMap with Hair; see those Components above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Hugo',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
