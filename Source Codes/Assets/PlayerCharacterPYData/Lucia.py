"""
Lucia Character Hash Commands
ZZZ Mod Fixer v2.5
Auto-generated from hash.json
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Lucia's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === Hair Component ===
'340fc999': [(log, ('2.5: Lucia Hair IB Hash',)),           (add_ib_check_if_missing,)],
'78043df0': [(log, ('2.5: Lucia Hair Position Hash',))],
'97dde567': [(log, ('2.5: Lucia Hair Texcoord Hash',))],
'bfd60db5': [(log, ('2.5: Lucia Hair Blend Hash',))],

# === Body Component ===
'd39c304d': [(log, ('2.5: Lucia Body IB Hash',)),           (add_ib_check_if_missing,)],
'234c641a': [(log, ('2.5: Lucia Body Position Hash',))],
'0400f04f': [(log, ('2.5: Lucia Body Texcoord Hash',))],
'3f4f9fa9': [(log, ('2.5: Lucia Body Blend Hash',))],

# === Cape Component ===
'cd80d116': [(log, ('2.5: Lucia Cape IB Hash',)),           (add_ib_check_if_missing,)],
'08ae4b5d': [(log, ('2.5: Lucia Cape Position Hash',))],
'dd0e570f': [(log, ('2.5: Lucia Cape Texcoord Hash',))],
'b917fca5': [(log, ('2.5: Lucia Cape Blend Hash',))],

# === CapeExtra Component ===
'692a4e10': [(log, ('2.5: Lucia CapeExtra IB Hash',)),      (add_ib_check_if_missing,)],
'c035f6bd': [(log, ('2.5: Lucia CapeExtra Position Hash',))],
'90f30bc1': [(log, ('2.5: Lucia CapeExtra Texcoord Hash',))],
'946dc2ff': [(log, ('2.5: Lucia CapeExtra Blend Hash',))],

# === Face Component ===
'6986f28e': [(log, ('2.5: Lucia Face IB Hash',)),           (add_ib_check_if_missing,)],

# === Face Textures ===
'20a6224d': [
        (log,                           ('2.5: Lucia FaceA Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('12ec6e26', 'Lucia.FaceA.Diffuse.1024')),
    ],

'12ec6e26': [
        (log,                           ('2.5: Lucia FaceA Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('20a6224d', 'Lucia.FaceA.Diffuse.2048')),
    ],

# === Hair Textures (Shared between HairA and HairB) ===
'5b0b47c9': [
        (log,                           ('2.5: Lucia Hair Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('ab461f68', 'Lucia.HairA.Diffuse.1024')),
    ],

'ab461f68': [
        (log,                           ('2.5: Lucia Hair Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('5b0b47c9', 'Lucia.HairA.Diffuse.2048')),
    ],
'243feee8': [
        (log,                           ('2.5: Lucia Hair LightMap 2048p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('dda3939e', 'Lucia.HairA.LightMap.1024')),
    ],

'dda3939e': [
        (log,                           ('2.5: Lucia Hair LightMap 1024p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('243feee8', 'Lucia.HairA.LightMap.2048')),
    ],
'211a5700': [
        (log,                           ('2.5: Lucia Hair MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c09e5350', 'Lucia.HairA.MaterialMap.1024')),
    ],

'c09e5350': [
        (log,                           ('2.5: Lucia Hair MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('211a5700', 'Lucia.HairA.MaterialMap.2048')),
    ],
'ebac056e': [
        (log,                           ('2.5: Lucia NormalMap Hash (Shared across components)',)),
        (add_section_if_missing,        ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],

# === Body Textures (Shared between BodyA and BodyB) ===
'2ca45943': [
        (log,                           ('2.5: Lucia Body Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('614c9ad5', 'Lucia.BodyA.Diffuse.1024')),
    ],

'614c9ad5': [
        (log,                           ('2.5: Lucia Body Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('2ca45943', 'Lucia.BodyA.Diffuse.2048')),
    ],
'f117c868': [
        (log,                           ('2.5: Lucia Body LightMap 2048p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('30b94be9', 'Lucia.BodyA.LightMap.1024')),
    ],

'30b94be9': [
        (log,                           ('2.5: Lucia Body LightMap 1024p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('f117c868', 'Lucia.BodyA.LightMap.2048')),
    ],
'a16861d2': [
        (log,                           ('2.5: Lucia Body MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('c0fe7e43', 'Lucia.BodyA.MaterialMap.1024')),
    ],

'c0fe7e43': [
        (log,                           ('2.5: Lucia Body MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,        ('a16861d2', 'Lucia.BodyA.MaterialMap.2048')),
    ],

# === Cape Textures (Shares Hair textures) ===
# Note: Cape component uses the same textures as Hair (5b0b47c9, 243feee8, 211a5700)
# These are already defined in the Hair Textures section above and will apply to Cape as well

# === CapeExtra Textures (Shares Hair textures) ===
# Note: CapeExtra component uses the same textures as Hair (5b0b47c9, 243feee8, 211a5700)
# These are already defined in the Hair Textures section above and will apply to CapeExtra as well,
'7be43e2b': [(log, ('3.0: Lucia Hair Shadow IB Hash',)), (add_ib_check_if_missing,)],
'0695fa38': [
        (log, ('3.0: Lucia Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'82729474': [
        (log, ('3.0: Lucia Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'38f2daa7': [
        (log, ('3.0: Lucia Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'9662cc92': [
        (log, ('3.0: Lucia Hair Shadow VB Hash',)),
        (add_section_if_missing, ('7be43e2b', 'Lucia.Hair Shadow.IB', 'match_priority = 0\n')),
    ],
'6533c56a': [
        (log, ('3.0: Lucia Cape VB Hash',)),
        (add_section_if_missing, ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
    ],
'5f21562d': [
        (log, ('3.0: Lucia Cape VB Hash',)),
        (add_section_if_missing, ('cd80d116', 'Lucia.Cape.IB', 'match_priority = 0\n')),
    ],
'439208cc': [
        (log, ('3.0: Lucia CapeAccessory VB Hash',)),
        (add_section_if_missing, ('692a4e10', 'Lucia.CapeAccessory.IB', 'match_priority = 0\n')),
    ],
'b3a498b5': [
        (log, ('3.0: Lucia Body VB Hash',)),
        (add_section_if_missing, ('d39c304d', 'Lucia.Body.IB', 'match_priority = 0\n')),
    ],
'84eaa4c6': [(log, ('3.0: Lucia eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'f917cafc': [
        (log, ('3.0: Lucia eyebrow VB Hash',)),
        (add_section_if_missing, ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
    ],
'c30559bb': [
        (log, ('3.0: Lucia eyebrow VB Hash',)),
        (add_section_if_missing, ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
    ],
'05342ce9': [
        (log, ('3.0: Lucia eyebrow VB Hash',)),
        (add_section_if_missing, ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
    ],
'8893a84c': [
        (log, ('3.0: Lucia eyebrow VB Hash',)),
        (add_section_if_missing, ('84eaa4c6', 'Lucia.eyebrow.IB', 'match_priority = 0\n')),
    ],
'430748c4': [
        (log, ('3.0: Lucia Face VB Hash',)),
        (add_section_if_missing, ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
    ],
'9648c6d3': [
        (log, ('3.0: Lucia Face VB Hash',)),
        (add_section_if_missing, ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
    ],
'925947a7': [
        (log, ('3.0: Lucia Face VB Hash',)),
        (add_section_if_missing, ('6986f28e', 'Lucia.Face.IB', 'match_priority = 0\n')),
    ],
'5cca4239': [(log, ('3.0: Lucia weapon IB Hash',)), (add_ib_check_if_missing,)],
'adc940e0': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'9f2822c3': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'7a83c0d2': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'5a602448': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'e2e48852': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'74814017': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'ebc05d0c': [(log, ('3.0: Lucia weapon IB Hash',)), (add_ib_check_if_missing,)],
'0ee71df8': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('ebc05d0c', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'2d98213f': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('ebc05d0c', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'b1ebb25d': [
        (log, ('3.0: Lucia weapon VB Hash',)),
        (add_section_if_missing, ('ebc05d0c', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'08ecb686': [(log, ('3.0: Lucia misc hash',)),],
'73acb40f': [(log, ('3.0: Lucia misc hash',)),],
'7915db83': [(log, ('3.0: Lucia misc hash',)),],
'fed6eef6': [
        (log, ('3.0: Lucia Hair VB Hash',)),
        (add_section_if_missing, ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.0: Lucia Hair TEX Hash',)),
        (add_section_if_missing, ('340fc999', 'Lucia.Hair.IB', 'match_priority = 0\n')),
    ],
'8d72bc12': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'84e4fd19': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
'009caccb': [
        (log, ('3.0: Lucia weapon TEX Hash',)),
        (add_section_if_missing, ('5cca4239', 'Lucia.weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Lucia',
    'game_versions': ['2.5'],
    'notes': 'New character in version 2.5. Hair, Cape, and CapeExtra components share the same texture set.',
}
