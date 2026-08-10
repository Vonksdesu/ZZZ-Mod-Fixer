"""
YuzuhaTanukiInBroadDaylight Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.5
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns YuzuhaTanukiInBroadDaylight's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# IB Hashes
'7a504287': [(log, ('2.5: YuzuhaTanukiInBroadDaylight Hair IB Hash',)), (add_ib_check_if_missing,)],
'f34fdc84': [(log, ('2.1 -> 2.11: YuzuhaSkin Body IB Hash',)),       (update_hash, ('b298482d',))],
'b298482d': [(log, ('2.5: YuzuhaTanukiInBroadDaylight Body IB Hash',)), (add_ib_check_if_missing,)],
'a8de520e': [(log, ('2.5: YuzuhaTanukiInBroadDaylight Accessories IB Hash',)), (add_ib_check_if_missing,)],
'14ac0d52': [(log, ('2.5: YuzuhaTanukiInBroadDaylight Kama IB Hash',)), (add_ib_check_if_missing,)],
'507384ea': [(log, ('2.5: YuzuhaTanukiInBroadDaylight Face IB Hash',)), (add_ib_check_if_missing,)],

# Face Textures
'd394bc13': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight FaceA Diffuse Hash',)),
        (add_section_if_missing,        ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
    ],

# Hair Textures
'521a3242': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Hair Diffuse Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'c400f5b7': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Hair LightMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'3f70d124': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Hair MaterialMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],

# Body Textures (shared between Body and Kama components)
'4f4c2b65': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('7fc53810', 'YuzuhaTanukiInBroadDaylight.BodyA.Diffuse.1024')),
    ],

'7fc53810': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('4f4c2b65', 'YuzuhaTanukiInBroadDaylight.BodyA.Diffuse.2048')),
    ],
'c3e64779': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama LightMap 2048p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ac06a4c8', 'YuzuhaTanukiInBroadDaylight.BodyA.LightMap.1024')),
    ],

'ac06a4c8': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama LightMap 1024p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c3e64779', 'YuzuhaTanukiInBroadDaylight.BodyA.LightMap.2048')),
    ],
'ac2f3dcb': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('58fd94ec', 'YuzuhaTanukiInBroadDaylight.BodyA.MaterialMap.1024')),
    ],

'58fd94ec': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Body/Kama MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ac2f3dcb', 'YuzuhaTanukiInBroadDaylight.BodyA.MaterialMap.2048')),
    ],

# Accessories Textures
'54591ef6': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('9f387d35', 'YuzuhaTanukiInBroadDaylight.AccA.Diffuse.1024')),
    ],

'9f387d35': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('54591ef6', 'YuzuhaTanukiInBroadDaylight.AccA.Diffuse.2048')),
    ],
'a78340ed': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories LightMap 2048p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('00bcfe90', 'YuzuhaTanukiInBroadDaylight.AccA.LightMap.1024')),
    ],

'00bcfe90': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories LightMap 1024p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a78340ed', 'YuzuhaTanukiInBroadDaylight.AccA.LightMap.2048')),
    ],
'1d0dabdb': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c2c76575', 'YuzuhaTanukiInBroadDaylight.AccA.MaterialMap.1024')),
    ],

'c2c76575': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Accessories MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('1d0dabdb', 'YuzuhaTanukiInBroadDaylight.AccA.MaterialMap.2048')),
    ],

# Shared NormalMap (used across Hair, Body, Accessories, and Kama)
'ebac056e': [
        (log,                           ('2.5: YuzuhaTanukiInBroadDaylight Shared NormalMap Hash',)),
        (add_section_if_missing,        ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.Kama.IB', 'match_priority = 0\n')),
    ],
'051f9657': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'dc2821dc': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'606c88ae': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'afb6117a': [(log, ('3.0: YuzuhaTanukiInBroadDaylight Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'8a540628': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'3a4533fc': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'a39c4806': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9fc9b6f8': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair Shadow VB Hash',)),
        (add_section_if_missing, ('afb6117a', 'YuzuhaTanukiInBroadDaylight.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'cf3319f6': [(log, ('2.1 -> 2.11: YuzuhaSkin Body Draw Hash',)), (update_hash, ('07437c27',))],
'07437c27': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Body VB Hash',)),
        (add_section_if_missing, ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
    ],
'a3b56c9b': [(log, ('2.1 -> 2.11: YuzuhaSkin Body Position Hash',)), (update_hash, ('2a7b9144',))],
'2a7b9144': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Body VB Hash',)),
        (add_section_if_missing, ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
    ],
'3d3199c5': [(log, ('2.1 -> 2.11: YuzuhaSkin Body Texcoord Hash',)), (update_hash, ('0c9062c5',))],
'0c9062c5': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Body VB Hash',)),
        (add_section_if_missing, ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
    ],
'be70426a': [(log, ('2.1 -> 2.11: YuzuhaSkin Body Blend Hash',)), (update_hash, ('523cf99d',))],
'523cf99d': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Body VB Hash',)),
        (add_section_if_missing, ('b298482d', 'YuzuhaTanukiInBroadDaylight.Body.IB', 'match_priority = 0\n')),
    ],
'ca3209f7': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Accessories VB Hash',)),
        (add_section_if_missing, ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
    ],
'f271d524': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Accessories VB Hash',)),
        (add_section_if_missing, ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
    ],
'ce14b4b7': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Accessories VB Hash',)),
        (add_section_if_missing, ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
    ],
'294d341c': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Accessories VB Hash',)),
        (add_section_if_missing, ('a8de520e', 'YuzuhaTanukiInBroadDaylight.Accessories.IB', 'match_priority = 0\n')),
    ],
'b6e62152': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'9d4425e5': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'a7394f34': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'2a45c137': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight LeopardCat1 VB Hash',)),
        (add_section_if_missing, ('14ac0d52', 'YuzuhaTanukiInBroadDaylight.LeopardCat1.IB', 'match_priority = 0\n')),
    ],
'0f6a425b': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
    ],
'9d0f7ef5': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
    ],
'52400cce': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Face VB Hash',)),
        (add_section_if_missing, ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
    ],
'b34a880c': [(log, ('3.0: YuzuhaTanukiInBroadDaylight weapon IB Hash',)), (add_ib_check_if_missing,)],
'79849b37': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon VB Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'd5283f28': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon VB Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'd7204982': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon VB Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'caeee529': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'f74f81e8': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'6657efd2': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'3578d11c': [(log, ('3.0: YuzuhaTanukiInBroadDaylight misc hash',)),],
'b36355ab': [(log, ('3.0: YuzuhaTanukiInBroadDaylight misc hash',)),],
'630debc9': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair VB Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'c9115930': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair TEX Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair TEX Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'a9730519': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair TEX Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'4f5639e2': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Hair TEX Hash',)),
        (add_section_if_missing, ('7a504287', 'YuzuhaTanukiInBroadDaylight.Hair.IB', 'match_priority = 0\n')),
    ],
'59f9e66f': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight Face TEX Hash',)),
        (add_section_if_missing, ('507384ea', 'YuzuhaTanukiInBroadDaylight.Face.IB', 'match_priority = 0\n')),
    ],
'c8cb308c': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'dc683116': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
'114dafdf': [
        (log, ('3.0: YuzuhaTanukiInBroadDaylight weapon TEX Hash',)),
        (add_section_if_missing, ('b34a880c', 'YuzuhaTanukiInBroadDaylight.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'YuzuhaTanukiInBroadDaylight',
    'game_versions': ['2.5'],
    'components': ['Hair', 'Body', 'Accessories', 'Kama', 'Face'],
}

