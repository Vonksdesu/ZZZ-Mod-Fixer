"""
Norma Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Norma's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'773f390c': [
        (log,                           ('3.0: Norma Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'4fafb136': [
        (log,                           ('3.0: Norma Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'a2150d3b': [
        (log,                           ('3.0: Norma Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'bcc7e369': [
        (log,                           ('3.0: Norma Hat IB Hash',)),
        (add_ib_check_if_missing,),
    ],

# === Norma Textures (FaceA) ===
'c18a1af1': [
        (log,                           ('3.0: Norma FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('007dc9ec', 'Norma.FaceA.Diffuse.2048')),
    ],
'007dc9ec': [
        (log,                           ('3.0: Norma FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('c18a1af1', 'Norma.FaceA.Diffuse.1024')),
    ],

# === Norma Textures (HairA) ===
'a86b749d': [
        (log,                           ('3.0: Norma HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('9593fbbd', 'Norma.HairA.Diffuse.2048')),
    ],
'9593fbbd': [
        (log,                           ('3.0: Norma HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('a86b749d', 'Norma.HairA.Diffuse.1024')),
    ],
'541008f2': [
        (log,                           ('3.0: Norma HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('a0010ed7', 'Norma.HairA.LightMap.2048')),
    ],
'a0010ed7': [
        (log,                           ('3.0: Norma HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('541008f2', 'Norma.HairA.LightMap.1024')),
    ],
'60152e0e': [
        (log,                           ('3.0: Norma HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('6493d4d4', 'Norma.HairA.MaterialMap.2048')),
    ],
'6493d4d4': [
        (log,                           ('3.0: Norma HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('60152e0e', 'Norma.HairA.MaterialMap.1024')),
    ],

# === Norma Textures (BodyA) ===
'ab235f8c': [
        (log,                           ('3.0: Norma BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('8dbb873b', 'Norma.BodyA.Diffuse.2048')),
    ],
'8dbb873b': [
        (log,                           ('3.0: Norma BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('ab235f8c', 'Norma.BodyA.Diffuse.1024')),
    ],
'becdc27c': [
        (log,                           ('3.0: Norma BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('13e85378', 'Norma.BodyA.LightMap.2048')),
    ],
'13e85378': [
        (log,                           ('3.0: Norma BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('becdc27c', 'Norma.BodyA.LightMap.1024')),
    ],
'0e22ca8e': [
        (log,                           ('3.0: Norma BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('fcb3bd07', 'Norma.BodyA.MaterialMap.2048')),
    ],
'fcb3bd07': [
        (log,                           ('3.0: Norma BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('0e22ca8e', 'Norma.BodyA.MaterialMap.1024')),
    ],
'be624ee3': [
        (log, ('3.0: Norma Hair VB Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
    ],
'18e12e3a': [
        (log, ('3.0: Norma Hair VB Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
    ],
'0a09cb32': [
        (log, ('3.0: Norma Hair VB Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
    ],
'fc98a89c': [
        (log, ('3.0 -> 3.1: Norma Hair TEX Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                        ('ebac056e',)),
    ],
'7517a03f': [(log, ('3.0: Norma HairShadow IB Hash',)), (add_ib_check_if_missing,)],
'152400a0': [
        (log, ('3.0: Norma Hat VB Hash',)),
        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'80f2a2aa': [
        (log, ('3.0: Norma Hat VB Hash',)),
        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'6a8b4c03': [
        (log, ('3.0: Norma Hat VB Hash',)),
        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'accaa8fd': [
        (log, ('3.0: Norma Hat VB Hash',)),
        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'c149712f': [
        (log, ('3.0: Norma Body VB Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'52235615': [
        (log, ('3.0: Norma Body VB Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'b10a84f3': [
        (log, ('3.0: Norma Body VB Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'37da98f5': [
        (log, ('3.0 -> 3.1: Norma Body TEX Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        (update_hash,                        ('ebac056e',)),
    ],
'd3b2ed9a': [(log, ('3.0: Norma Eyebrow IB Hash',)), (add_ib_check_if_missing,)],
'b5bc1f91': [
        (log, ('3.0: Norma Eyebrow VB Hash',)),
        (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'7acc7619': [
        (log, ('3.0: Norma Eyebrow VB Hash',)),
        (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'11747958': [
        (log, ('3.0: Norma Eyebrow VB Hash',)),
        (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
    ],
'b886698b': [
        (log, ('3.0: Norma Face VB Hash',)),
        (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
    ],
'b1412ed9': [
        (log, ('3.0: Norma Face VB Hash',)),
        (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
    ],
'cf3ce0a2': [
        (log, ('3.0: Norma Face VB Hash',)),
        (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
    ],
'ca38d6a1': [(log, ('3.0: Norma Weapon IB Hash',)), (add_ib_check_if_missing,)],
'2ff62c6d': [
        (log, ('3.0: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'38e511a4': [
        (log, ('3.0: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash, ('07e51b64',)),
    ],
'89a25f1a': [
        (log, ('3.0: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash, ('c4173b6e',)),
    ],
'd3a66db9': [
        (log, ('3.0: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash, ('aa195b0b',)),
    ],
'23ba50e2': [
        (log, ('3.0: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'4050da0a': [
        (log, ('3.0 -> 3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash,                        ('ebac056e',)),
    ],
'00b13a4d': [
        (log, ('3.0: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'7ae5f4d6': [
        (log, ('3.0 -> 3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash,                        ('79a583ad',)),
    ],
'85361021': [(log, ('3.0: Norma Shell IB Hash',)), (add_ib_check_if_missing,)],
'1b29ee19': [
        (log, ('3.0: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'e2a92567': [
        (log, ('3.0 -> 3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (update_hash,                        ('e3fafeeb',)),
    ],
'1d67e673': [
        (log, ('3.0 -> 3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (update_hash,                        ('44991f30',)),
    ],
'10d0bc6f': [
        (log, ('3.0: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'dc5bc6d9': [
        (log, ('3.0 -> 3.1: Norma Hair TEX Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (update_hash,                        ('798adba3',)),
    ],
'02cbd89d': [
        (log, ('3.0 -> 3.1: Norma Body TEX Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        (update_hash,                        ('798adba3',)),
    ],
'ff0137ae': [
        (log, ('3.0: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'0139f54e': [
        (log, ('3.0 -> 3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash,                        ('798adba3',)),
    ],
'9bb6a4c1': [
        (log, ('3.0: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'1db67ade': [
        (log, ('3.0 -> 3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (update_hash,                        ('b70b6037',)),
    ],
'8294facc': [
        (log, ('3.0: Norma Face VB Hash',)),
        (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
    ],
'ab21b245': [
        (log, ('3.0: Norma Body VB Hash',)),
        (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'62c935b1': [
        (log, ('3.0: Norma Hair VB Hash',)),
        (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
    ],
# === Norma Weapon & Shell (3.1) ===
'07e51b64': [
        (log, ('3.1: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'c4173b6e': [
        (log, ('3.1: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'aa195b0b': [
        (log, ('3.1: Norma Weapon VB Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'e3fafeeb': [
        (log, ('3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'44991f30': [
        (log, ('3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'8b699f2d': [
        (log, ('3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'bd112545': [
        (log, ('3.1: Norma Shell VB Hash',)),
        (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
    ],
'ebac056e': [
        (log, ('3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'798adba3': [
        (log, ('3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'79a583ad': [
        (log, ('3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
'b70b6037': [
        (log, ('3.1: Norma Weapon TEX Hash',)),
        (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Norma',
    'game_versions': ['3.0'],
}
