"""
Evelyn Character Hash Commands
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
    Returns Evelyn's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
'10a5bde2': [(log, ('2.5: Evelyn Hair IB Hash',)),      (add_ib_check_if_missing,)],
'04b53ecd': [(log, ('2.5: Evelyn Body IB Hash',)),      (add_ib_check_if_missing,)],
'bb6d1023': [(log, ('2.5: Evelyn Jacket IB Hash',)),    (add_ib_check_if_missing,)],
'b3eaedb0': [(log, ('2.5: Evelyn Shoulders IB Hash',)), (add_ib_check_if_missing,)],
'ddf4efa6': [(log, ('2.5: Evelyn Face IB Hash',)),      (add_ib_check_if_missing,)],
'8e1d1a6f': [
        (log,                           ('2.5: Evelyn FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('bc090438', 'Evelyn.FaceA.Diffuse.1024')),
    ],
'bc090438': [
        (log,                           ('2.5: Evelyn FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('8e1d1a6f', 'Evelyn.FaceA.Diffuse.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Evelyn Shared NormalMap Hash (Hair, Jacket, Body, Shoulder)',)),
        (add_section_if_missing,        ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b3eaedb0', 'Evelyn.Shoulders.IB', 'match_priority = 0\n')),
    ],
'0e5c3c97': [
        (log,                           ('2.5: Evelyn Hair, Jacket Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('65a7592d', 'Evelyn.Hair.Diffuse.1024')),
    ],
'e1434e0d': [
        (log,                           ('2.5: Evelyn Hair, Jacket LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('eb414a98', 'Evelyn.Hair.LightMap.1024')),
    ],
'b2718585': [
        (log,                           ('2.5: Evelyn Hair, Jacket MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('e680f0c7', 'Evelyn.Hair.MaterialMap.1024')),
    ],
'65a7592d': [
        (log,                           ('2.5: Evelyn Hair, Jacket Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('0e5c3c97', 'Evelyn.Hair.Diffuse.2048')),
    ],
'eb414a98': [
        (log,                           ('2.5: Evelyn Hair, Jacket LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('e1434e0d', 'Evelyn.Hair.LightMap.2048')),
    ],
'e680f0c7': [
        (log,                           ('2.5: Evelyn Hair, Jacket MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('b2718585', 'Evelyn.Hair.MaterialMap.2048')),
    ],
'a59b14c0': [
        (log,                           ('2.5: Evelyn Body, Shoulder Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('93033898', 'Evelyn.Body.Diffuse.1024')),
    ],
'd022d32c': [
        (log,                           ('2.5: Evelyn Body, Shoulder LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('16aab2ab', 'Evelyn.Body.LightMap.1024')),
    ],
'8624e4e4': [
        (log,                           ('2.5: Evelyn Body, Shoulder MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('716561f0', 'Evelyn.Body.MaterialMap.1024')),
    ],
'93033898': [
        (log,                           ('2.5: Evelyn Body, Shoulder Diffuse 1024p Hash',)),
        (multiply_section_if_missing,   ('a59b14c0', 'Evelyn.Body.Diffuse.2048')),
    ],
'16aab2ab': [
        (log,                           ('2.5: Evelyn Body, Shoulder LightMap 1024p Hash',)),
        (multiply_section_if_missing,   ('d022d32c', 'Evelyn.Body.LightMap.2048')),
    ],
'716561f0': [
        (log,                           ('2.5: Evelyn Body, Shoulder MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('8624e4e4', 'Evelyn.Body.MaterialMap.2048')),
    ],
'c2fe4e27': [
        (log, ('3.0: Evelyn Hair VB Hash',)),
        (add_section_if_missing, ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
    ],
'066f6115': [
        (log, ('3.0: Evelyn Hair VB Hash',)),
        (add_section_if_missing, ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
    ],
'b43809d2': [
        (log, ('3.0: Evelyn Hair VB Hash',)),
        (add_section_if_missing, ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
    ],
'8ed17e5a': [(log, ('3.0: Evelyn Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'28913abf': [
        (log, ('3.0: Evelyn Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'1251bc38': [
        (log, ('3.0: Evelyn Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'bf111b37': [
        (log, ('3.0: Evelyn Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'94ce70dd': [
        (log, ('3.0: Evelyn Hair Shadow VB Hash',)),
        (add_section_if_missing, ('8ed17e5a', 'Evelyn.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'2488810a': [(log, ('3.0: Evelyn Hairpin IB Hash',)), (add_ib_check_if_missing,)],
'98a87a48': [
        (log, ('3.0: Evelyn Hairpin VB Hash',)),
        (add_section_if_missing, ('2488810a', 'Evelyn.Hairpin.IB', 'match_priority = 0\n')),
    ],
'f1076f2a': [
        (log, ('3.0: Evelyn Hairpin VB Hash',)),
        (add_section_if_missing, ('2488810a', 'Evelyn.Hairpin.IB', 'match_priority = 0\n')),
    ],
'63d18ae4': [
        (log, ('3.0: Evelyn Hairpin VB Hash',)),
        (add_section_if_missing, ('2488810a', 'Evelyn.Hairpin.IB', 'match_priority = 0\n')),
    ],
'35070aca': [
        (log, ('3.0: Evelyn Hairpin VB Hash',)),
        (add_section_if_missing, ('2488810a', 'Evelyn.Hairpin.IB', 'match_priority = 0\n')),
    ],
'1fb9dfe2': [
        (log, ('3.0: Evelyn Jacket VB Hash',)),
        (add_section_if_missing, ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
    ],
'4edb27d5': [
        (log, ('3.0: Evelyn Jacket VB Hash',)),
        (add_section_if_missing, ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
    ],
'8b3ed55f': [
        (log, ('3.0: Evelyn Jacket VB Hash',)),
        (add_section_if_missing, ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
    ],
'022d390f': [
        (log, ('3.0: Evelyn Jacket VB Hash',)),
        (add_section_if_missing, ('bb6d1023', 'Evelyn.Jacket.IB', 'match_priority = 0\n')),
    ],
'356f6430': [
        (log, ('3.0: Evelyn Shoulder VB Hash',)),
        (add_section_if_missing, ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
    ],
'2b77b077': [
        (log, ('3.0: Evelyn Shoulder VB Hash',)),
        (add_section_if_missing, ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
    ],
'3cecd299': [
        (log, ('3.0: Evelyn Shoulder VB Hash',)),
        (add_section_if_missing, ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
    ],
'a6b42907': [
        (log, ('3.0: Evelyn Shoulder VB Hash',)),
        (add_section_if_missing, ('b3eaedb0', 'Evelyn.Shoulder.IB', 'match_priority = 0\n')),
    ],
'02b04234': [
        (log, ('3.0: Evelyn Body VB Hash',)),
        (add_section_if_missing, ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
    ],
'67eafa06': [
        (log, ('3.0: Evelyn Body VB Hash',)),
        (add_section_if_missing, ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
    ],
'26f9ba95': [
        (log, ('3.0: Evelyn Body VB Hash',)),
        (add_section_if_missing, ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
    ],
'5ea06832': [
        (log, ('3.0: Evelyn Body VB Hash',)),
        (add_section_if_missing, ('04b53ecd', 'Evelyn.Body.IB', 'match_priority = 0\n')),
    ],
'fcbd52cb': [
        (log, ('3.0: Evelyn Face VB Hash',)),
        (add_section_if_missing, ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
    ],
'aa2f560e': [
        (log, ('3.0: Evelyn Face VB Hash',)),
        (add_section_if_missing, ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
    ],
'f9fc3c8b': [
        (log, ('3.0: Evelyn Face VB Hash',)),
        (add_section_if_missing, ('ddf4efa6', 'Evelyn.Face.IB', 'match_priority = 0\n')),
    ],
'78699e6c': [(log, ('3.0: Evelyn weapon IB Hash',)), (add_ib_check_if_missing,)],
'7fb7467f': [(log, ('3.0: Evelyn weapon IB Hash',)), (add_ib_check_if_missing,)],
'af10bd11': [(log, ('3.0: Evelyn silk string IB Hash',)), (add_ib_check_if_missing,)],
'3ae20915': [(log, ('3.0: Evelyn misc hash',)),],
'4ff726df': [(log, ('3.0: Evelyn misc hash',)),],
'c6afc18c': [(log, ('3.0: Evelyn misc hash',)),],
'798bc78b': [
        (log, ('3.0: Evelyn Hair VB Hash',)),
        (add_section_if_missing, ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Evelyn Hair TEX Hash',)),
        (add_section_if_missing, ('10a5bde2', 'Evelyn.Hair.IB', 'match_priority = 0\n')),
    ],
'99c7c611': [
        (log, ('3.0: Evelyn weapon VB Hash',)),
        (add_section_if_missing, ('78699e6c', 'Evelyn.weapon.IB', 'match_priority = 0\n')),
    ],
'33d2866e': [
        (log, ('3.0: Evelyn weapon2 position_vb Hash',)),
        (add_section_if_missing, ('7fb7467f', 'Evelyn.weapon2.IB', 'match_priority = 0\n')),
    ],
'040993a0': [
        (log, ('3.0: Evelyn weapon2 texcoord_vb Hash',)),
        (add_section_if_missing, ('7fb7467f', 'Evelyn.weapon2.IB', 'match_priority = 0\n')),
    ],

# Historical hashes (2.2-2.3): silk string & weapon open (tanpa penerus)
'06c6a436': [
        (log,                           ('2.2-2.3: Evelyn Silk String Position 2048p Hash',)),
    ],
'2c5dcebd': [
        (log,                           ('2.2-2.3: Evelyn Silk String Texcoord 2048p Hash',)),
    ],
'99555cf2': [
        (log,                           ('2.2-2.3: Evelyn Silk String Blend 2048p Hash',)),
    ],
'3e2abfae': [
        (log,                           ('2.2: Evelyn Weapon Open Position Hash',)),
    ],
'691f1157': [
        (log,                           ('2.2: Evelyn Weapon Open Texcoord Hash',)),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Evelyn',
    'game_versions': ['1.0', '1.1', '1.2', '1.3', '1.4', '1.5', '1.6', '1.7', '2.5'],
}
