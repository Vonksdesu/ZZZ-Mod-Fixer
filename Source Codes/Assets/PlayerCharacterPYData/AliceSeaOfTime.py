"""
AliceSeaOfTime Character Hash Commands
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
    Returns AliceSeaOfTime's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'd131acb1': [(log, ('2.5: AliceSeaOfTime Hair IB Hash',)), (add_ib_check_if_missing,)],
'cf8612e6': [(log, ('2.5: AliceSeaOfTime Body IB Hash',)), (add_ib_check_if_missing,)],
'2fcd160b': [(log, ('2.5: AliceSeaOfTime Backpack IB Hash',)), (add_ib_check_if_missing,)],
'24d07797': [(log, ('2.5: AliceSeaOfTime Sensor IB Hash',)), (add_ib_check_if_missing,)],
'b078ff22': [(log, ('2.5: AliceSeaOfTime Face IB Hash',)), (add_ib_check_if_missing,)],
'9f3e582c': [
        (log,                           ('2.5: AliceSeaOfTime FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'705caac9': [
        (log,                           ('2.5: AliceSeaOfTime HairA Diffuse Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log,                           ('2.5: AliceSeaOfTime HairA, BodyA, BackpackA NormalMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('2fcd160b', 'AliceSeaOfTime.Backpack.IB', 'match_priority = 0\n')),
    ],
'03543db2': [
        (log,                           ('2.5: AliceSeaOfTime HairA LightMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'508530fe': [
        (log,                           ('2.5: AliceSeaOfTime HairA MaterialMap Hash',)),
        (add_section_if_missing,        ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'18601d57': [
        (log,                           ('2.5: AliceSeaOfTime BodyA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7283db21', 'AliceSeaOfTime.BodyA.Diffuse.1024')),
    ],

'7283db21': [
        (log,                           ('2.5: AliceSeaOfTime BodyA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('18601d57', 'AliceSeaOfTime.BodyA.Diffuse.2048')),
    ],
'3409fcce': [
        (log,                           ('2.5: AliceSeaOfTime BodyA LightMap 2048p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('8087d734', 'AliceSeaOfTime.BodyA.LightMap.1024')),
    ],

'8087d734': [
        (log,                           ('2.5: AliceSeaOfTime BodyA LightMap 1024p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('3409fcce', 'AliceSeaOfTime.BodyA.LightMap.2048')),
    ],
'212fc22a': [
        (log,                           ('2.5: AliceSeaOfTime BodyA MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('e4f01bb0', 'AliceSeaOfTime.BodyA.MaterialMap.1024')),
    ],

'e4f01bb0': [
        (log,                           ('2.5: AliceSeaOfTime BodyA MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('212fc22a', 'AliceSeaOfTime.BodyA.MaterialMap.2048')),
    ],
'4eff9bd8': [
        (log,                           ('2.5: AliceSeaOfTime BackpackA Diffuse Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSeaOfTime.Backpack.IB', 'match_priority = 0\n')),
    ],
'2a09a850': [
        (log,                           ('2.5: AliceSeaOfTime BackpackA LightMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSeaOfTime.Backpack.IB', 'match_priority = 0\n')),
    ],
'1cd2807e': [
        (log,                           ('2.5: AliceSeaOfTime BackpackA MaterialMap Hash',)),
        (add_section_if_missing,        ('2fcd160b', 'AliceSeaOfTime.Backpack.IB', 'match_priority = 0\n')),
    ],
'ad686c31': [
        (log, ('3.0: AliceSeaOfTime Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'b86d14b0': [
        (log, ('3.0: AliceSeaOfTime Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'cf1202fd': [
        (log, ('3.0: AliceSeaOfTime Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'ebbe2894': [(log, ('3.0: AliceSeaOfTime Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'd482d732': [
        (log, ('3.0: AliceSeaOfTime Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a3fb836a': [
        (log, ('3.0: AliceSeaOfTime Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'85fb0c65': [
        (log, ('3.0: AliceSeaOfTime Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'14c96dd0': [
        (log, ('3.0: AliceSeaOfTime Hair Shadow VB Hash',)),
        (add_section_if_missing, ('ebbe2894', 'AliceSeaOfTime.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a7fbdddb': [
        (log, ('3.0: AliceSeaOfTime Body VB Hash',)),
        (add_section_if_missing, ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
    ],
'75218916': [
        (log, ('3.0: AliceSeaOfTime Body VB Hash',)),
        (add_section_if_missing, ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
    ],
'3c686494': [
        (log, ('3.0: AliceSeaOfTime Body VB Hash',)),
        (add_section_if_missing, ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
    ],
'7dc3bf5b': [
        (log, ('3.0: AliceSeaOfTime Body VB Hash',)),
        (add_section_if_missing, ('cf8612e6', 'AliceSeaOfTime.Body.IB', 'match_priority = 0\n')),
    ],
'6f724c8e': [
        (log, ('3.0: AliceSeaOfTime BeltAcc VB Hash',)),
        (add_section_if_missing, ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'3246b6ca': [
        (log, ('3.0: AliceSeaOfTime BeltAcc VB Hash',)),
        (add_section_if_missing, ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'a70f45bd': [
        (log, ('3.0: AliceSeaOfTime BeltAcc VB Hash',)),
        (add_section_if_missing, ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'ff4d1872': [
        (log, ('3.0: AliceSeaOfTime BeltAcc VB Hash',)),
        (add_section_if_missing, ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'bf0e4dab': [
        (log, ('3.0: AliceSeaOfTime BeltAcc TEX Hash',)),
        (add_section_if_missing, ('24d07797', 'AliceSeaOfTime.BeltAcc.IB', 'match_priority = 0\n')),
    ],
'f100ba28': [
        (log, ('3.0: AliceSeaOfTime BackAcc VB Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'65d035e4': [
        (log, ('3.0: AliceSeaOfTime BackAcc VB Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'4d910650': [
        (log, ('3.0: AliceSeaOfTime BackAcc VB Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'c715afa3': [
        (log, ('3.0: AliceSeaOfTime BackAcc VB Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'70088a4a': [
        (log, ('3.0: AliceSeaOfTime Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'4a1a190d': [
        (log, ('3.0: AliceSeaOfTime Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'7c9dbd4a': [
        (log, ('3.0: AliceSeaOfTime Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'2326355e': [
        (log, ('3.0: AliceSeaOfTime Face VB Hash',)),
        (add_section_if_missing, ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'2c37d8c9': [(log, ('3.0: AliceSeaOfTime sword IB Hash',)), (add_ib_check_if_missing,)],
'4d92da0d': [
        (log, ('3.0: AliceSeaOfTime sword VB Hash',)),
        (add_section_if_missing, ('2c37d8c9', 'AliceSeaOfTime.sword.IB', 'match_priority = 0\n')),
    ],
'91d2f9fd': [
        (log, ('3.0: AliceSeaOfTime Hair TEX Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: AliceSeaOfTime Hair TEX Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'6c957d8f': [
        (log, ('3.0: AliceSeaOfTime Hair TEX Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'bc4c87fd': [
        (log, ('3.0: AliceSeaOfTime Hair TEX Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],
'6775ef8d': [
        (log, ('3.0: AliceSeaOfTime BackAcc TEX Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'dbea86db': [
        (log, ('3.0: AliceSeaOfTime BackAcc TEX Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'21126e07': [
        (log, ('3.0: AliceSeaOfTime BackAcc TEX Hash',)),
        (add_section_if_missing, ('2fcd160b', 'AliceSeaOfTime.BackAcc.IB', 'match_priority = 0\n')),
    ],
'33fdeb6d': [
        (log, ('3.0: AliceSeaOfTime Face TEX Hash',)),
        (add_section_if_missing, ('b078ff22', 'AliceSeaOfTime.Face.IB', 'match_priority = 0\n')),
    ],
'd515e182': [
        (log, ('3.0: AliceSeaOfTime Hair VB Hash',)),
        (add_section_if_missing, ('d131acb1', 'AliceSeaOfTime.Hair.IB', 'match_priority = 0\n')),
    ],

# Historical hashes: sword state B (<=2.1 & 2.4) dan state A (2.2-2.3), ping-pong sesuai log transisi
'e52f08c3': [
        (log,                           ('2.1 -> 2.2: AliceSeaOfTime Sword Blend VB Hash',)),
        (update_hash,                   ('4fbccfe1',)),
    ],
'3136fbad': [
        (log,                           ('2.1 -> 2.2: AliceSeaOfTime Sword Texcoord VB Hash',)),
        (update_hash,                   ('c6899a42',)),
    ],
'5324c543': [
        (log,                           ('2.1 -> 2.2: AliceSeaOfTime Sword Position VB Hash',)),
        (update_hash,                   ('e3a50a16',)),
    ],
'4fbccfe1': [
        (log,                           ('2.3 -> 2.4: AliceSeaOfTime Sword Blend VB Hash',)),
        (update_hash,                   ('e52f08c3',)),
    ],
'c6899a42': [
        (log,                           ('2.3 -> 2.4: AliceSeaOfTime Sword Texcoord VB Hash',)),
        (update_hash,                   ('3136fbad',)),
    ],
'e3a50a16': [
        (log,                           ('2.3 -> 2.4: AliceSeaOfTime Sword Position VB Hash',)),
        (update_hash,                   ('5324c543',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AliceSeaOfTime',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
