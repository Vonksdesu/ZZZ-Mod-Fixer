"""
Rina Character Hash Commands
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
    Returns Rina's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'cdb2cc7d': [
            (log,                             ('2.2 - 3.2: Rina Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8ca7dc4b': [
            (log,                             ('2.2 - 3.2: Rina Hair Draw VB Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        ],
        '06c78cb0': [
            (log,                             ('2.2 - 3.2: Rina Hair Position VB Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        ],
        '0dda44b1': [
            (log,                             ('2.2 - 3.2: Rina Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        ],
        'fef908be': [
            (log,                             ('2.2 - 3.2: Rina Hair Blend VB Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        ],
        'eb5d9d1c': [
            (log,                             ('2.2 - 3.2: Rina HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4b005a79', 'Rina.HairA.Diffuse.1024')),
        ],
        '4b005a79': [
            (log,                             ('2.2 - 3.2: Rina HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('eb5d9d1c', 'Rina.HairA.Diffuse.2048')),
        ],
        '83ac7993': [
            (log,                             ('1.0 -> 2.5: Rina HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
            (log,                             ('+ Updated to shared NormalMap hash',)),
        ],
        'fa3c40e9': [
            (log,                             ('1.0: Rina HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Rina HairA, BodyA, weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Rina.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Rina.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Rina.weapon - 1 - 棕发安娜塔莎A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Rina.weapon - 2 - 金发杜苏拉A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Rina HairA, BodyA, weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', '83ac7993'), 'Rina.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', '97637a8f'), 'Rina.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Rina.weapon - 1 - 棕发安娜塔莎A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Rina.weapon - 2 - 金发杜苏拉A.NormalMap.2048')),
        ],
        '1145d2b8': [
            (log,                             ('2.2 - 3.2: Rina HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fb61499f', 'Rina.HairA.LightMap.1024')),
        ],
        'fb61499f': [
            (log,                             ('2.2 - 3.2: Rina HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1145d2b8', 'Rina.HairA.LightMap.2048')),
        ],
        '82153e28': [
            (log,                             ('2.2 - 3.2: Rina HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ea08fd96', 'Rina.HairA.MaterialMap.1024')),
        ],
        'ea08fd96': [
            (log,                             ('2.2 - 3.2: Rina HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('cdb2cc7d', 'Rina.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('82153e28', 'Rina.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '5116f2cb': [
            (log,                             ('2.2 - 3.2: Rina Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8119483f': [
            (log,                             ('2.2 - 3.2: Rina Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '112f8365': [
            (log,                             ('2.2 - 3.2: Rina Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bd58eaab': [
            (log,                             ('2.2 - 3.2: Rina Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '950dc06c': [
            (log,                             ('2.2 - 3.2: Rina Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('5116f2cb', 'Rina.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '2825da1e': [
            (log,                             ('2.2 - 3.2: Rina Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '03e8990d': [
            (log,                             ('2.2 - 3.2: Rina Body Draw VB Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        ],
        '41149c54': [
            (log,                             ('2.2 - 3.2: Rina Body Position VB Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        ],
        '4c259bf3': [
            (log,                             ('2.2 - 3.2: Rina Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        ],
        '17471aea': [
            (log,                             ('2.2 - 3.2: Rina Body Blend VB Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        ],
        'bf44bf67': [
            (log,                             ('2.2 - 3.2: Rina BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a23e2e14', 'Rina.BodyA.Diffuse.1024')),
        ],
        'a23e2e14': [
            (log,                             ('2.2 - 3.2: Rina BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf44bf67', 'Rina.BodyA.Diffuse.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.
        '97637a8f': [
            (log,                             ('1.0 -> 2.5: Rina BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
            (log,                             ('+ Updated to shared NormalMap hash',)),
        ],
        'd6b20159': [
            (log,                             ('1.0: Rina BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
        ],
        '95f4e9c8': [
            (log,                             ('2.2 - 3.2: Rina BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fad76987', 'Rina.BodyA.LightMap.1024')),
        ],
        'fad76987': [
            (log,                             ('2.2 - 3.2: Rina BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('95f4e9c8', 'Rina.BodyA.LightMap.2048')),
        ],
        'ed47722f': [
            (log,                             ('2.2 - 3.2: Rina BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9fa6dfd3', 'Rina.BodyA.MaterialMap.1024')),
        ],
        '9fa6dfd3': [
            (log,                             ('2.2 - 3.2: Rina BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2825da1e', 'Rina.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ed47722f', 'Rina.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '9f90cfaa': [
            (log,                             ('2.2 - 3.2: Rina Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c32482a8': [
            (log,                             ('2.2 - 3.2: Rina Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
        ],
        'f93611ef': [
            (log,                             ('2.2 - 3.2: Rina Face Position VB Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
        ],
        '1866cf6a': [
            (log,                             ('2.2 - 3.1: Rina Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('a79912e2',)),
        ],
        'a79912e2': [
            (log,                             ('3.2: Rina Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '3124a1db': [
            (log,                             ('2.2 - 3.2: Rina Face Blend VB Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
        ],
        '802a3281': [
            (log,                             ('2.2 - 3.2: Rina FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7ecc44ce', 'Rina.FaceA.Diffuse.1024')),
        ],
        '7ecc44ce': [
            (log,                             ('2.2 - 3.2: Rina FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('9f90cfaa', 'Rina.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('802a3281', 'Rina.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 1 - 棕发安娜塔莎 Component ====================
        '4f795827': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'c9174fa5': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
        ],
        'e28891a4': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎 Position VB Hash',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
        ],
        '9be6ba46': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
        ],
        'bc04a8d9': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎 Blend VB Hash',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
        ],
        '7aa85409': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('203a9fa8', 'Rina.weapon - 1 - 棕发安娜塔莎A.Diffuse.1024')),
            (multiply_section_if_missing,     ('203a9fa8', 'Rina.weapon - 2 - 金发杜苏拉A.Diffuse.1024')),
        ],
        '203a9fa8': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7aa85409', 'Rina.weapon - 1 - 棕发安娜塔莎A.Diffuse.2048')),
            (multiply_section_if_missing,     ('7aa85409', 'Rina.weapon - 2 - 金发杜苏拉A.Diffuse.2048')),
        ],
        # weapon - 1 - 棕发安娜塔莎 shares its NormalMap hashes with Hair; see that Component above.
        '6aec8cd9': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c99753e0', 'Rina.weapon - 1 - 棕发安娜塔莎A.LightMap.1024')),
            (multiply_section_if_missing,     ('c99753e0', 'Rina.weapon - 2 - 金发杜苏拉A.LightMap.1024')),
        ],
        'c99753e0': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6aec8cd9', 'Rina.weapon - 1 - 棕发安娜塔莎A.LightMap.2048')),
            (multiply_section_if_missing,     ('6aec8cd9', 'Rina.weapon - 2 - 金发杜苏拉A.LightMap.2048')),
        ],
        '6d3db8fe': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('76939bab', 'Rina.weapon - 1 - 棕发安娜塔莎A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('76939bab', 'Rina.weapon - 2 - 金发杜苏拉A.MaterialMap.1024')),
        ],
        '76939bab': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 棕发安娜塔莎A and weapon - 2 - 金发杜苏拉A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('4f795827', 'Rina.weapon - 1 - 棕发安娜塔莎.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d3db8fe', 'Rina.weapon - 1 - 棕发安娜塔莎A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('6d3db8fe', 'Rina.weapon - 2 - 金发杜苏拉A.MaterialMap.2048')),
        ],

        # ==================== weapon - 1 - 安娜塔莎 - 双眼 Component ====================
        '8ebe259d': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '11d72670': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
        ],
        '941f67ec': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼 Position VB Hash',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
        ],
        '34a3b201': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼 Texcoord VB Hash',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
        ],
        '6fecdfb7': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼 Blend VB Hash',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
        ],
        '5b418f07': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9a76e68e', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.Diffuse.1024')),
            (multiply_section_if_missing,     ('9a76e68e', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.Diffuse.1024')),
        ],
        '9a76e68e': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b418f07', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.Diffuse.2048')),
            (multiply_section_if_missing,     ('5b418f07', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.Diffuse.2048')),
        ],
        'b8f3b02a': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1864c72', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.NormalMap.1024')),
            (multiply_section_if_missing,     ('e1864c72', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.NormalMap.1024')),
        ],
        'e1864c72': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8f3b02a', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.NormalMap.2048')),
            (multiply_section_if_missing,     ('b8f3b02a', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.NormalMap.2048')),
        ],
        '1d68e5ac': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f3653e23', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.LightMap.1024')),
            (multiply_section_if_missing,     ('f3653e23', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.LightMap.1024')),
        ],
        'f3653e23': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d68e5ac', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.LightMap.2048')),
            (multiply_section_if_missing,     ('1d68e5ac', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.LightMap.2048')),
        ],
        'b990fcb9': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2f1e005f', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('2f1e005f', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.MaterialMap.1024')),
        ],
        '2f1e005f': [
            (log,                             ('2.2 - 3.2: Rina weapon - 1 - 安娜塔莎 - 双眼A and weapon - 2 - 杜苏拉 - 独眼A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8ebe259d', 'Rina.weapon - 1 - 安娜塔莎 - 双眼.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b990fcb9', 'Rina.weapon - 1 - 安娜塔莎 - 双眼A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b990fcb9', 'Rina.weapon - 2 - 杜苏拉 - 独眼A.MaterialMap.2048')),
        ],

        # ==================== weapon - 2 - 金发杜苏拉 Component ====================
        '4fba8b69': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 金发杜苏拉 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7a72d77f': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 金发杜苏拉 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
        ],
        'd4492a43': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 金发杜苏拉 Position VB Hash',)),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
        ],
        '8bcd9f92': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 金发杜苏拉 Texcoord VB Hash',)),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
        ],
        'a59d40f4': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 金发杜苏拉 Blend VB Hash',)),
            (add_section_if_missing,          ('4fba8b69', 'Rina.weapon - 2 - 金发杜苏拉.IB', 'match_priority = 0\n')),
        ],
        # weapon - 2 - 金发杜苏拉 shares its Diffuse, LightMap and MaterialMap hashes with
        # weapon - 1 - 棕发安娜塔莎, and its NormalMap hashes are shared with Hair; see those Components above.

        # ==================== weapon - 2 - 杜苏拉 - 独眼 Component ====================
        'a6bfc370': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 杜苏拉 - 独眼 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '16399986': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 杜苏拉 - 独眼 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
        ],
        '187daa68': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 杜苏拉 - 独眼 Position VB Hash',)),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
        ],
        'a1695dc5': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 杜苏拉 - 独眼 Texcoord VB Hash',)),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
        ],
        'cc1203fa': [
            (log,                             ('2.2 - 3.2: Rina weapon - 2 - 杜苏拉 - 独眼 Blend VB Hash',)),
            (add_section_if_missing,          ('a6bfc370', 'Rina.weapon - 2 - 杜苏拉 - 独眼.IB', 'match_priority = 0\n')),
        ],
        # weapon - 2 - 杜苏拉 - 独眼 shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with
        # weapon - 1 - 安娜塔莎 - 双眼; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Rina',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
