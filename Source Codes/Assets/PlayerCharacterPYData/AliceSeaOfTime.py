"""
AliceSeaOfTime Character Hash Commands
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
    Returns AliceSeaOfTime's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'd131acb1': [
            (log,                             ('2.1: AliceSeaOfTime Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd515e182': [
            (log,                             ('2.2: AliceSeaOfTime Hair Draw VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
        ],
        'ad686c31': [
            (log,                             ('2.2: AliceSeaOfTime Hair Position VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
        ],
        'b86d14b0': [
            (log,                             ('2.2: AliceSeaOfTime Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
        ],
        'cf1202fd': [
            (log,                             ('2.2: AliceSeaOfTime Hair Blend VB Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
        ],
        '705caac9': [
            (log,                             ('2.1: AliceSeaOfTime HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('91d2f9fd', 'AliceSeaOfTime.HairA.Diffuse.1024')),
        ],
        'ebac056e': [
            (log,                             ('2.2: AliceSeaOfTime HairA, BodyA, BackAccA and sword NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'AliceSeaOfTime.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AliceSeaOfTime.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AliceSeaOfTime.BackAccA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'AliceSeaOfTime.sword.NormalMap.1024')),
        ],
        '03543db2': [
            (log,                             ('2.1: AliceSeaOfTime HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c957d8f', 'AliceSeaOfTime.HairA.LightMap.1024')),
        ],
        '508530fe': [
            (log,                             ('2.1: AliceSeaOfTime HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc4c87fd', 'AliceSeaOfTime.HairA.MaterialMap.1024')),
        ],
        '91d2f9fd': [
            (log,                             ('2.1: AliceSeaOfTime HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('705caac9', 'AliceSeaOfTime.HairA.Diffuse.2048')),
        ],
        '798adba3': [
            (log,                             ('2.2: AliceSeaOfTime HairA, BodyA, BackAccA and sword NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'AliceSeaOfTime.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AliceSeaOfTime.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AliceSeaOfTime.BackAccA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'AliceSeaOfTime.sword.NormalMap.2048')),
        ],
        '6c957d8f': [
            (log,                             ('2.1: AliceSeaOfTime HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('03543db2', 'AliceSeaOfTime.HairA.LightMap.2048')),
        ],
        'bc4c87fd': [
            (log,                             ('2.1: AliceSeaOfTime HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('508530fe', 'AliceSeaOfTime.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'ebbe2894': [
            (log,                             ('2.2: AliceSeaOfTime Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'd482d732': [
            (log,                             ('2.2: AliceSeaOfTime Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a3fb836a': [
            (log,                             ('2.2: AliceSeaOfTime Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '85fb0c65': [
            (log,                             ('2.2: AliceSeaOfTime Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '14c96dd0': [
            (log,                             ('2.2: AliceSeaOfTime Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'cf8612e6': [
            (log,                             ('2.1: AliceSeaOfTime Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a7fbdddb': [
            (log,                             ('2.2: AliceSeaOfTime Body Draw VB Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        ],
        '75218916': [
            (log,                             ('2.2: AliceSeaOfTime Body Position VB Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        ],
        '3c686494': [
            (log,                             ('2.2: AliceSeaOfTime Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        ],
        '7dc3bf5b': [
            (log,                             ('2.2: AliceSeaOfTime Body Blend VB Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        ],
        '18601d57': [
            (log,                             ('2.1: AliceSeaOfTime BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('7283db21', 'AliceSeaOfTime.BodyA.Diffuse.1024')),
        ],
        '7283db21': [
            (log,                             ('2.1: AliceSeaOfTime BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18601d57', 'AliceSeaOfTime.BodyA.Diffuse.2048')),
        ],
        '3409fcce': [
            (log,                             ('2.1: AliceSeaOfTime BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8087d734', 'AliceSeaOfTime.BodyA.LightMap.1024')),
        ],
        '8087d734': [
            (log,                             ('2.1: AliceSeaOfTime BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3409fcce', 'AliceSeaOfTime.BodyA.LightMap.2048')),
        ],
        '212fc22a': [
            (log,                             ('2.1: AliceSeaOfTime BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e4f01bb0', 'AliceSeaOfTime.BodyA.MaterialMap.1024')),
        ],
        'e4f01bb0': [
            (log,                             ('2.1: AliceSeaOfTime BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('212fc22a', 'AliceSeaOfTime.BodyA.MaterialMap.2048')),
        ],

        # ==================== BeltAcc Component ====================
        '24d07797': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6f724c8e': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc Draw VB Hash',)),
            (add_section_if_missing,          ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        '3246b6ca': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc Position VB Hash',)),
            (add_section_if_missing,          ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'a70f45bd': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'ff4d1872': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc Blend VB Hash',)),
            (add_section_if_missing,          ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
        ],
        'bf0e4dab': [
            (log,                             ('2.2: AliceSeaOfTime BeltAcc Diffuse 1024p & 2048p Hash',)),
            (add_section_if_missing,          ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
        ],

        # ==================== BackAcc Component ====================
        '2fcd160b': [
            (log,                             ('2.2: AliceSeaOfTime BackAcc IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'f100ba28': [
            (log,                             ('2.2: AliceSeaOfTime BackAcc Draw VB Hash',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '65d035e4': [
            (log,                             ('2.2: AliceSeaOfTime BackAcc Position VB Hash',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '4d910650': [
            (log,                             ('2.2: AliceSeaOfTime BackAcc Texcoord VB Hash',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
        ],
        'c715afa3': [
            (log,                             ('2.2: AliceSeaOfTime BackAcc Blend VB Hash',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
        ],
        '4eff9bd8': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6775ef8d', 'AliceSeaOfTime.BackAccA.Diffuse.1024')),
            (multiply_section_if_missing,     ('6775ef8d', 'AliceSeaOfTime.sword.Diffuse.1024')),
        ],
        '2a09a850': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('dbea86db', 'AliceSeaOfTime.BackAccA.LightMap.1024')),
            (multiply_section_if_missing,     ('dbea86db', 'AliceSeaOfTime.sword.LightMap.1024')),
        ],
        '1cd2807e': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('21126e07', 'AliceSeaOfTime.BackAccA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('21126e07', 'AliceSeaOfTime.sword.MaterialMap.1024')),
        ],
        '6775ef8d': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4eff9bd8', 'AliceSeaOfTime.BackAccA.Diffuse.2048')),
            (multiply_section_if_missing,     ('4eff9bd8', 'AliceSeaOfTime.sword.Diffuse.2048')),
        ],
        'dbea86db': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2a09a850', 'AliceSeaOfTime.BackAccA.LightMap.2048')),
            (multiply_section_if_missing,     ('2a09a850', 'AliceSeaOfTime.sword.LightMap.2048')),
        ],
        '21126e07': [
            (log,                             ('2.2: AliceSeaOfTime BackAccA and sword MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1cd2807e', 'AliceSeaOfTime.BackAccA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1cd2807e', 'AliceSeaOfTime.sword.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        'b078ff22': [
            (log,                             ('2.1: AliceSeaOfTime Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '70088a4a': [
            (log,                             ('2.2: AliceSeaOfTime Face Draw VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
        ],
        '4a1a190d': [
            (log,                             ('2.2: AliceSeaOfTime Face Position VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
        ],
        '7c9dbd4a': [
            (log,                             ('2.2: AliceSeaOfTime Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('0749a6d7',)),
        ],
        '0749a6d7': [
            (log,                             ('3.2: AliceSeaOfTime Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '2326355e': [
            (log,                             ('2.2: AliceSeaOfTime Face Blend VB Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
        ],
        '9f3e582c': [
            (log,                             ('2.1: AliceSeaOfTime FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('33fdeb6d', 'AliceSeaOfTime.FaceA.Diffuse.1024')),
        ],
        '33fdeb6d': [
            (log,                             ('2.1: AliceSeaOfTime FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9f3e582c', 'AliceSeaOfTime.FaceA.Diffuse.2048')),
        ],

        # ==================== Sword Component ====================
        '2c37d8c9': [
            (log,                             ('2.2: AliceSeaOfTime sword IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '4d92da0d': [
            (log,                             ('2.2: AliceSeaOfTime sword Draw VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
        ],
        '4fbccfe1': [
            (log,                             ('2.2 -> 2.4: AliceSeaOfTime sword Blend VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e52f08c3',)),
        ],
        'c6899a42': [
            (log,                             ('2.2 -> 2.4: AliceSeaOfTime sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (update_hash,                     ('3136fbad',)),
        ],
        'e3a50a16': [
            (log,                             ('2.2 -> 2.4: AliceSeaOfTime sword Position VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
            (update_hash,                     ('5324c543',)),
        ],
        'e52f08c3': [
            (log,                             ('2.4: AliceSeaOfTime sword Blend VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
        ],
        '3136fbad': [
            (log,                             ('2.4: AliceSeaOfTime sword Texcoord VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
        ],
        '5324c543': [
            (log,                             ('2.4: AliceSeaOfTime sword Position VB Hash',)),
            (add_section_if_missing,          ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
        ],
    }

# Character metadata
CHARACTER_INFO = {
    'name': 'AliceSeaOfTime',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}