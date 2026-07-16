"""
Norma Character Hash Commands
ZZZ Mod Fixer v3.0
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
    """
    return {
# === IB Hashes ===
'31178971': [(log, ('3.0: Norma Hair IB Hash',)),                      (add_ib_check_if_missing,)],
'0ae14c24': [(log, ('3.0: Norma Cloak IB Hash',)),                     (add_ib_check_if_missing,)],
'b386901d': [(log, ('3.0: Norma CloakChest IB Hash',)),            (add_ib_check_if_missing,)],
'10c77d62': [(log, ('3.0: Norma Chest IB Hash',)),                 (add_ib_check_if_missing,)],
'ec003379': [(log, ('3.0: Norma Legs IB Hash',)),                  (add_ib_check_if_missing,)],
'6cca89ab': [(log, ('2.7 -> 2.8: Norma Hair IB Hash [Legacy]',)), (update_hash, ('31178971',))],
'a633d5b7': [(log, ('2.8 -> 3.0: Norma CloakChest IB Hash [Legacy] 2',)), (update_hash, ('36e794ea',))],
'36e794ea': [(log, ('2.8 -> 3.0: Norma CloakChest IB Hash [Legacy]',)), (update_hash, ('b386901d',))],
'6abaa60a': [(log, ('2.8 -> 3.0: Norma Chest IB Hash [Legacy] 2',)), (update_hash, ('62a6b4bd',))],
'62a6b4bd': [(log, ('2.8 -> 3.0: Norma Chest IB Hash [Legacy]',)), (update_hash, ('10c77d62',))],
'68f34958': [(log, ('2.8 -> 3.0: Norma Cloak IB Hash [Legacy] 2',)), (update_hash, ('93f1f568',))],
'93f1f568': [(log, ('2.8 -> 3.0: Norma Cloak IB Hash [Legacy]',)), (update_hash, ('0ae14c24',))],
'21871660': [(log, ('2.8 -> 3.0: Norma Legs IB Hash [Legacy] 2',)), (update_hash, ('fd054d1d',))],
'fd054d1d': [(log, ('2.8 -> 3.0: Norma Legs IB Hash [Legacy]',)), (update_hash, ('ec003379',))],

# === IB Hashes (v3.0 Target) ===
'a2150d3b': [(log, ('3.0: Norma Hair IB Hash',)),                       (add_ib_check_if_missing,)],
'7517a03f': [(log, ('3.0: Norma HairShadow IB Hash',)),                  (add_ib_check_if_missing,)],
'bcc7e369': [(log, ('3.0: Norma Hat IB Hash',)),                        (add_ib_check_if_missing,)],
'773f390c': [(log, ('3.0: Norma Body IB Hash',)),                       (add_ib_check_if_missing,)],
'd3b2ed9a': [(log, ('3.0: Norma Eyebrow IB Hash',)),                     (add_ib_check_if_missing,)],
'4fafb136': [(log, ('3.0: Norma Face IB Hash',)),                        (add_ib_check_if_missing,)],
'ca38d6a1': [(log, ('3.0: Norma Weapon IB Hash',)),                      (add_ib_check_if_missing,)],
'85361021': [(log, ('3.0: Norma Shell IB Hash',)),                       (add_ib_check_if_missing,)],

# === VB Hashes ===
# Hair
'62c935b1': [(log, ('3.0: Norma Hair draw_vb',)),                       (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'be624ee3': [(log, ('3.0: Norma Hair position_vb',)),                   (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'18e12e3a': [(log, ('3.0: Norma Hair texcoord_vb',)),                   (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],
'0a09cb32': [(log, ('3.0: Norma Hair blend_vb',)),                      (add_section_if_missing, ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n'))],

# Hat
'152400a0': [(log, ('3.0: Norma Hat draw_vb',)),                        (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'80f2a2aa': [(log, ('3.0: Norma Hat position_vb',)),                    (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'6a8b4c03': [(log, ('3.0: Norma Hat texcoord_vb',)),                    (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],
'accaa8fd': [(log, ('3.0: Norma Hat blend_vb',)),                       (add_section_if_missing, ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n'))],

# Body
'ab21b245': [(log, ('3.0: Norma Body draw_vb',)),                       (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'c149712f': [(log, ('3.0: Norma Body position_vb',)),                   (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'52235615': [(log, ('3.0: Norma Body texcoord_vb',)),                   (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],
'b10a84f3': [(log, ('3.0: Norma Body blend_vb',)),                      (add_section_if_missing, ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n'))],

# Eyebrow
'b5bc1f91': [(log, ('3.0: Norma Eyebrow draw_vb',)),                    (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'15a1b43f': [(log, ('3.0: Norma Eyebrow position_vb',)),                (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'7acc7619': [(log, ('3.0: Norma Eyebrow texcoord_vb',)),                (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],
'11747958': [(log, ('3.0: Norma Eyebrow blend_vb',)),                   (add_section_if_missing, ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n'))],

# Face
'8294facc': [(log, ('3.0: Norma Face draw_vb',)),                       (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'b886698b': [(log, ('3.0: Norma Face position_vb',)),                   (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'b1412ed9': [(log, ('3.0: Norma Face texcoord_vb',)),                   (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],
'cf3ce0a2': [(log, ('3.0: Norma Face blend_vb',)),                      (add_section_if_missing, ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n'))],

# Weapon
'2ff62c6d': [(log, ('3.0: Norma Weapon draw_vb',)),                     (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n'))],
'38e511a4': [(log, ('3.0: Norma Weapon position_vb',)),                 (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n'))],
'89a25f1a': [(log, ('3.0: Norma Weapon texcoord_vb',)),                 (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n'))],
'd3a66db9': [(log, ('3.0: Norma Weapon blend_vb',)),                    (add_section_if_missing, ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n'))],

# Shell
'1b29ee19': [(log, ('3.0: Norma Shell draw_vb',)),                      (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n'))],
'e2a92567': [(log, ('3.0: Norma Shell position_vb',)),                  (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n'))],
'1d67e673': [(log, ('3.0: Norma Shell texcoord_vb',)),                  (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n'))],
'10d0bc6f': [(log, ('3.0: Norma Shell blend_vb',)),                     (add_section_if_missing, ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n'))],

# === Face & Eyebrow Shared Textures ===
'007dc9ec': [
        (log,                           ('3.0: Norma Face, Eyebrow Diffuse Hash',)),
        (add_section_if_missing,        ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
    ],

# === Hair & Hat Shared Textures ===
'9593fbbd': [
        (log,                           ('3.0: Norma Hair, Hat Diffuse Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'a0010ed7': [
        (log,                           ('3.0: Norma Hair, Hat LightMap Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
'6493d4d4': [
        (log,                           ('3.0: Norma Hair, Hat MaterialMap Hash',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],

# === Body Textures ===
'8dbb873b': [
        (log,                           ('3.0: Norma Body Diffuse Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'13e85378': [
        (log,                           ('3.0: Norma Body LightMap Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'fcb3bd07': [
        (log,                           ('3.0: Norma Body MaterialMap Hash',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],

# === Shared Normal Map ===
'798adba3': [
        (log,                           ('3.0: Norma Shared NormalMap Hash (Target)',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],
'fc98a89c': [
        (log,                           ('3.0: Norma Hair, Hat NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
    ],
    '37da98f5': [
        (log,                           ('3.0: Norma Body NormalMap Hash [Legacy]',)),
        (add_section_if_missing,        ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
    ],

# === Weapon/Shell Shared Textures ===
'23ba50e2': [
        (log,                           ('3.0: Norma Weapon/Shell Diffuse 2048p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('ff0137ae', 'Norma.WeaponShell.Diffuse.1024')),
    ],
'4050da0a': [
        (log,                           ('3.0: Norma Weapon/Shell NormalMap 2048p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('0139f54e', 'Norma.WeaponShell.NormalMap.1024')),
    ],
'00b13a4d': [
        (log,                           ('3.0: Norma Weapon/Shell LightMap 2048p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('9bb6a4c1', 'Norma.WeaponShell.LightMap.1024')),
    ],
'7ae5f4d6': [
        (log,                           ('3.0: Norma Weapon/Shell MaterialMap 2048p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('1db67ade', 'Norma.WeaponShell.MaterialMap.1024')),
    ],

# === Weapon/Shell Shared Textures 1024p ===
'ff0137ae': [
        (log,                           ('3.0: Norma Weapon/Shell Diffuse 1024p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('23ba50e2', 'Norma.WeaponShell.Diffuse.2048')),
    ],
'0139f54e': [
        (log,                           ('3.0: Norma Weapon/Shell NormalMap 1024p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('4050da0a', 'Norma.WeaponShell.NormalMap.2048')),
    ],
'9bb6a4c1': [
        (log,                           ('3.0: Norma Weapon/Shell LightMap 1024p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('00b13a4d', 'Norma.WeaponShell.LightMap.2048')),
    ],
'1db67ade': [
        (log,                           ('3.0: Norma Weapon/Shell MaterialMap 1024p Hash',)),
        (add_section_if_missing,        ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        (add_section_if_missing,        ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        (multiply_section_if_missing,   ('7ae5f4d6', 'Norma.WeaponShell.MaterialMap.2048')),
    ],

# === Legacy 3.0 Texture Hashes ===
    'a86b749d': [
        (log,                           ('3.0: Norma HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('a86b749d', 'Norma.HairA.Diffuse.1024')),
    ],
    '541008f2': [
        (log,                           ('3.0: Norma HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('541008f2', 'Norma.HairA.LightMap.1024')),
    ],
    '60152e0e': [
        (log,                           ('3.0: Norma HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,   ('60152e0e', 'Norma.HairA.MaterialMap.1024')),
    ],
    'ab235f8c': [
        (log,                           ('3.0: Norma BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('ab235f8c', 'Norma.BodyA.Diffuse.1024')),
    ],
    'becdc27c': [
        (log,                           ('3.0: Norma BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,   ('becdc27c', 'Norma.BodyA.LightMap.1024')),
    ],
    '0e22ca8e': [
        (log,                           ('3.0: Norma BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,   ('fcb3bd07', 'Norma.BodyA.MaterialMap.2048')),
    ],
    'c18a1af1': [
        (log,                           ('3.0: Norma FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,   ('c18a1af1', 'Norma.FaceA.Diffuse.1024')),
    ],
    'dc5bc6d9': [
        (log,                           ('3.0: Norma Hair, Hat NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('fc98a89c', 'Norma.Hair.NormalMap.2048')),
    ],
    '02cbd89d': [
        (log,                           ('3.0: Norma Body NormalMap 1024p Hash',)),
        (multiply_section_if_missing,   ('37da98f5', 'Norma.Body.NormalMap.2048')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Norma',
    'game_versions': ['3.0'],
}