"""
Manato Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.3 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Manato's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'de57398c': [
            (log,                             ('2.3 - 3.2: Manato Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0932100e': [
            (log,                             ('2.3 - 3.2: Manato Hair Draw VB Hash',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        ],
        '4e68e014': [
            (log,                             ('2.3 - 3.2: Manato Hair Position VB Hash',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        ],
        '9fe810ff': [
            (log,                             ('2.3 - 3.2: Manato Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        ],
        'b882d0c8': [
            (log,                             ('2.3 - 3.2: Manato Hair Blend VB Hash',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
        ],
        '81a04fa6': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('07353b33', 'Manato.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('07353b33', 'Manato.LegA.Diffuse.1024')),
        ],
        '07353b33': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('81a04fa6', 'Manato.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('81a04fa6', 'Manato.LegA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.3 - 3.2: Manato HairA, BodyA, PendantA, LegA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Manato.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Manato.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Manato.PendantA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Manato.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Manato.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.3 - 3.2: Manato HairA, BodyA, PendantA, LegA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Manato.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Manato.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Manato.PendantA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Manato.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Manato.weapon.NormalMap.2048')),
        ],
        '2bfdcb76': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('20447316', 'Manato.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('20447316', 'Manato.LegA.LightMap.1024')),
        ],
        '20447316': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2bfdcb76', 'Manato.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('2bfdcb76', 'Manato.LegA.LightMap.2048')),
        ],
        'b9654ab9': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b8091cf0', 'Manato.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('b8091cf0', 'Manato.LegA.MaterialMap.1024')),
        ],
        'b8091cf0': [
            (log,                             ('2.3 - 3.2: Manato HairA and LegA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('de57398c', 'Manato.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b9654ab9', 'Manato.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('b9654ab9', 'Manato.LegA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '734da350': [
            (log,                             ('2.3 - 3.2: Manato Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '18cf9af2': [
            (log,                             ('2.3 - 3.2: Manato Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '0da604ca': [
            (log,                             ('2.3 - 3.2: Manato Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'ade3c45f': [
            (log,                             ('2.3 - 3.2: Manato Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'bee7126f': [
            (log,                             ('2.3 - 3.2: Manato Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('734da350', 'Manato.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        # Hair Shadow has no texture hashes in the database.

        # ==================== Body Component ====================
        'f4c1c6d9': [
            (log,                             ('2.3 - 3.2: Manato Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8524918a': [
            (log,                             ('2.3 - 3.2: Manato Body Draw VB Hash',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
        ],
        '9e173c09': [
            (log,                             ('2.3 - 3.2: Manato Body Position VB Hash',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
        ],
        '7d36f969': [
            (log,                             ('2.3 - 3.2: Manato Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
        ],
        '91048d22': [
            (log,                             ('2.3 - 3.2: Manato Body Blend VB Hash',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
        ],
        '9e78d2c7': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9c659f1a', 'Manato.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9c659f1a', 'Manato.PendantA.Diffuse.1024')),
        ],
        '9c659f1a': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9e78d2c7', 'Manato.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('9e78d2c7', 'Manato.PendantA.Diffuse.2048')),
        ],
        '53c85c6a': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a15d0289', 'Manato.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('a15d0289', 'Manato.PendantA.LightMap.1024')),
        ],
        'a15d0289': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('53c85c6a', 'Manato.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('53c85c6a', 'Manato.PendantA.LightMap.2048')),
        ],
        'fdc49789': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('92336a2f', 'Manato.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('92336a2f', 'Manato.PendantA.MaterialMap.1024')),
        ],
        '92336a2f': [
            (log,                             ('2.3 - 3.2: Manato BodyA and PendantA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f4c1c6d9', 'Manato.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fdc49789', 'Manato.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('fdc49789', 'Manato.PendantA.MaterialMap.2048')),
        ],

        # ==================== Pendant Component ====================
        'fe66c6d2': [
            (log,                             ('2.3 - 3.2: Manato Pendant IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ff068e07': [
            (log,                             ('2.3 - 3.2: Manato Pendant Draw VB Hash',)),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
        ],
        '007cd149': [
            (log,                             ('2.3 - 3.2: Manato Pendant Position VB Hash',)),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
        ],
        '835ffec6': [
            (log,                             ('2.3 - 3.2: Manato Pendant Texcoord VB Hash',)),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
        ],
        'e9379036': [
            (log,                             ('2.3 - 3.2: Manato Pendant Blend VB Hash',)),
            (add_section_if_missing,          ('fe66c6d2', 'Manato.Pendant.IB', 'match_priority = 0\n')),
        ],
        # Pendant shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Body; see that Component above.

        # ==================== Leg Component ====================
        'c0425328': [
            (log,                             ('2.3 - 3.2: Manato Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2aa2324a': [
            (log,                             ('2.3 - 3.2: Manato Leg Draw VB Hash',)),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
        ],
        '8fe3485a': [
            (log,                             ('2.3 - 3.2: Manato Leg Position VB Hash',)),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
        ],
        '918946ee': [
            (log,                             ('2.3 - 3.2: Manato Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
        ],
        'd81e178a': [
            (log,                             ('2.3 - 3.2: Manato Leg Blend VB Hash',)),
            (add_section_if_missing,          ('c0425328', 'Manato.Leg.IB', 'match_priority = 0\n')),
        ],
        # Leg shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        'f987f156': [
            (log,                             ('2.3 - 3.2: Manato Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ef07f453': [
            (log,                             ('2.3 - 3.2: Manato Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
        ],
        'd5156714': [
            (log,                             ('2.3 - 3.2: Manato Face Position VB Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
        ],
        '0fd41a37': [
            (log,                             ('2.3 - 3.1: Manato Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('325bb10f',)),
        ],
        '325bb10f': [
            (log,                             ('3.2: Manato Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'e5c84069': [
            (log,                             ('2.3 - 3.2: Manato Face Blend VB Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
        ],
        '6d1343ec': [
            (log,                             ('2.3 - 3.2: Manato FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8de251ee', 'Manato.FaceA.Diffuse.1024')),
        ],
        '8de251ee': [
            (log,                             ('2.3 - 3.2: Manato FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('f987f156', 'Manato.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6d1343ec', 'Manato.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon Component ====================
        'c1f10814': [
            (log,                             ('2.3 - 3.2: Manato weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '84fa3702': [
            (log,                             ('2.3 - 3.2: Manato weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
        ],
        'd4141703': [
            (log,                             ('2.3 - 3.2: Manato weapon Position VB Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
        ],
        'f693b9de': [
            (log,                             ('2.3 - 3.2: Manato weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
        ],
        '34a20b76': [
            (log,                             ('2.3 - 3.2: Manato weapon Blend VB Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
        ],
        'ea7d80ff': [
            (log,                             ('2.3 - 3.2: Manato weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bd8621a4', 'Manato.weapon.Diffuse.1024')),
        ],
        'bd8621a4': [
            (log,                             ('2.3 - 3.2: Manato weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ea7d80ff', 'Manato.weapon.Diffuse.2048')),
        ],
        'c52d4279': [
            (log,                             ('2.3 - 3.2: Manato weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('38f2e62a', 'Manato.weapon.LightMap.1024')),
        ],
        '38f2e62a': [
            (log,                             ('2.3 - 3.2: Manato weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c52d4279', 'Manato.weapon.LightMap.2048')),
        ],
        'aef57b5d': [
            (log,                             ('2.3 - 3.2: Manato weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bf621a3b', 'Manato.weapon.MaterialMap.1024')),
        ],
        'bf621a3b': [
            (log,                             ('2.3 - 3.2: Manato weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('c1f10814', 'Manato.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aef57b5d', 'Manato.weapon.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Manato',
    'game_versions': ['2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
