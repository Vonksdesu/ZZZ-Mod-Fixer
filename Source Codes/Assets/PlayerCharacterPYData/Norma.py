"""
Norma Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.0 - 3.2
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

        # ==================== Hair Component ====================
        'a2150d3b': [
            (log,                             ('3.0 - 3.2: Norma Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '62c935b1': [
            (log,                             ('3.0 - 3.2: Norma Hair Draw VB Hash',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        ],
        'be624ee3': [
            (log,                             ('3.0 - 3.2: Norma Hair Position VB Hash',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        ],
        '18e12e3a': [
            (log,                             ('3.0 - 3.2: Norma Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        ],
        '0a09cb32': [
            (log,                             ('3.0 - 3.2: Norma Hair Blend VB Hash',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
        ],
        '9593fbbd': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a86b749d', 'Norma.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('a86b749d', 'Norma.HatA.Diffuse.1024')),
        ],
        'a86b749d': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9593fbbd', 'Norma.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('9593fbbd', 'Norma.HatA.Diffuse.2048')),
        ],
        'fc98a89c': [
            (log,                             ('3.0 -> 3.1: Norma HairA and HatA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        'ebac056e': [
            (log,                             ('3.1: Norma HairA, HatA, BodyA, WeaponA and ShellA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Norma.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Norma.HatA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Norma.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Norma.WeaponA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Norma.ShellA.NormalMap.1024')),
        ],
        'dc5bc6d9': [
            (log,                             ('3.0 -> 3.1: Norma HairA and HatA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (update_hash,                     ('798adba3',)),
        ],
        '798adba3': [
            (log,                             ('3.1: Norma HairA, HatA, BodyA, WeaponA and ShellA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Norma.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Norma.HatA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Norma.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Norma.WeaponA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Norma.ShellA.NormalMap.2048')),
        ],
        'a0010ed7': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('541008f2', 'Norma.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('541008f2', 'Norma.HatA.LightMap.1024')),
        ],
        '541008f2': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a0010ed7', 'Norma.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('a0010ed7', 'Norma.HatA.LightMap.2048')),
        ],
        '6493d4d4': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('60152e0e', 'Norma.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('60152e0e', 'Norma.HatA.MaterialMap.1024')),
        ],
        '60152e0e': [
            (log,                             ('3.0 - 3.2: Norma HairA and HatA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('a2150d3b', 'Norma.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6493d4d4', 'Norma.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('6493d4d4', 'Norma.HatA.MaterialMap.2048')),
        ],

        # ==================== HairShadow Component ====================
        '7517a03f': [
            (log,                             ('3.0 - 3.2: Norma HairShadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # HairShadow has no VB or texture hashes in the database.

        # ==================== Hat Component ====================
        'bcc7e369': [
            (log,                             ('3.0 - 3.2: Norma Hat IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '152400a0': [
            (log,                             ('3.0 - 3.2: Norma Hat Draw VB Hash',)),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        ],
        '80f2a2aa': [
            (log,                             ('3.0 - 3.2: Norma Hat Position VB Hash',)),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        ],
        '6a8b4c03': [
            (log,                             ('3.0 - 3.2: Norma Hat Texcoord VB Hash',)),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        ],
        'accaa8fd': [
            (log,                             ('3.0 - 3.2: Norma Hat Blend VB Hash',)),
            (add_section_if_missing,          ('bcc7e369', 'Norma.Hat.IB', 'match_priority = 0\n')),
        ],
        # Hat shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Hair; see that Component above.

        # ==================== Body Component ====================
        '773f390c': [
            (log,                             ('3.0 - 3.2: Norma Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'ab21b245': [
            (log,                             ('3.0 - 3.2: Norma Body Draw VB Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        ],
        'c149712f': [
            (log,                             ('3.0 - 3.2: Norma Body Position VB Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        ],
        '52235615': [
            (log,                             ('3.0 - 3.2: Norma Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        ],
        'b10a84f3': [
            (log,                             ('3.0 - 3.2: Norma Body Blend VB Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
        ],
        '8dbb873b': [
            (log,                             ('3.0 - 3.2: Norma BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ab235f8c', 'Norma.BodyA.Diffuse.1024')),
        ],
        'ab235f8c': [
            (log,                             ('3.0 - 3.2: Norma BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8dbb873b', 'Norma.BodyA.Diffuse.2048')),
        ],
        '37da98f5': [
            (log,                             ('3.0 -> 3.1: Norma BodyA NormalMap 2048p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '02cbd89d': [
            (log,                             ('3.0 -> 3.1: Norma BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('798adba3',)),
        ],
        '13e85378': [
            (log,                             ('3.0 - 3.2: Norma BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('becdc27c', 'Norma.BodyA.LightMap.1024')),
        ],
        'becdc27c': [
            (log,                             ('3.0 - 3.2: Norma BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('13e85378', 'Norma.BodyA.LightMap.2048')),
        ],
        'fcb3bd07': [
            (log,                             ('3.0 - 3.2: Norma BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e22ca8e', 'Norma.BodyA.MaterialMap.1024')),
        ],
        '0e22ca8e': [
            (log,                             ('3.0 - 3.2: Norma BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('773f390c', 'Norma.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fcb3bd07', 'Norma.BodyA.MaterialMap.2048')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Eyebrow Component ====================
        'd3b2ed9a': [
            (log,                             ('3.0 - 3.2: Norma Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b5bc1f91': [
            (log,                             ('3.0 - 3.2: Norma Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '7acc7619': [
            (log,                             ('3.0 - 3.1: Norma Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d2e41266',)),
        ],
        'd2e41266': [
            (log,                             ('3.2: Norma Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '11747958': [
            (log,                             ('3.0 - 3.2: Norma Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '007dc9ec': [
            (log,                             ('3.0 - 3.2: Norma EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c18a1af1', 'Norma.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c18a1af1', 'Norma.FaceA.Diffuse.1024')),
        ],
        'c18a1af1': [
            (log,                             ('3.0 - 3.2: Norma EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d3b2ed9a', 'Norma.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('007dc9ec', 'Norma.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('007dc9ec', 'Norma.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '4fafb136': [
            (log,                             ('3.0 - 3.2: Norma Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8294facc': [
            (log,                             ('3.0 - 3.2: Norma Face Draw VB Hash',)),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
        ],
        'b886698b': [
            (log,                             ('3.0 - 3.2: Norma Face Position VB Hash',)),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
        ],
        'b1412ed9': [
            (log,                             ('3.0 - 3.1: Norma Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c1bd84e7',)),
        ],
        'c1bd84e7': [
            (log,                             ('3.2: Norma Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'cf3ce0a2': [
            (log,                             ('3.0 - 3.2: Norma Face Blend VB Hash',)),
            (add_section_if_missing,          ('4fafb136', 'Norma.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse hashes with Eyebrow; see that Component above.

        # ==================== Weapon Component ====================
        'ca38d6a1': [
            (log,                             ('3.0 - 3.2: Norma Weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2ff62c6d': [
            (log,                             ('3.0: Norma Weapon Draw VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        ],
        '38e511a4': [
            (log,                             ('3.0: Norma Weapon Position VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('07e51b64',)),
        ],
        '89a25f1a': [
            (log,                             ('3.0: Norma Weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('c4173b6e',)),
        ],
        'd3a66db9': [
            (log,                             ('3.0: Norma Weapon Blend VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (update_hash,                     ('aa195b0b',)),
        ],
        '07e51b64': [
            (log,                             ('3.1: Norma Weapon VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        ],
        'c4173b6e': [
            (log,                             ('3.1: Norma Weapon VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        ],
        'aa195b0b': [
            (log,                             ('3.1: Norma Weapon VB Hash',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
        ],
        '23ba50e2': [
            (log,                             ('3.0 - 3.2: Norma WeaponA and ShellA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ff0137ae', 'Norma.WeaponA.Diffuse.1024')),
            (multiply_section_if_missing,     ('ff0137ae', 'Norma.ShellA.Diffuse.1024')),
        ],
        'ff0137ae': [
            (log,                             ('3.0 - 3.2: Norma WeaponA and ShellA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23ba50e2', 'Norma.WeaponA.Diffuse.2048')),
            (multiply_section_if_missing,     ('23ba50e2', 'Norma.ShellA.Diffuse.2048')),
        ],
        '4050da0a': [
            (log,                             ('3.0 -> 3.1: Norma WeaponA and ShellA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('ebac056e',)),
        ],
        '0139f54e': [
            (log,                             ('3.0 -> 3.1: Norma WeaponA and ShellA NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('798adba3',)),
        ],
        '00b13a4d': [
            (log,                             ('3.0 - 3.2: Norma WeaponA and ShellA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9bb6a4c1', 'Norma.WeaponA.LightMap.1024')),
            (multiply_section_if_missing,     ('9bb6a4c1', 'Norma.ShellA.LightMap.1024')),
        ],
        '9bb6a4c1': [
            (log,                             ('3.0 - 3.2: Norma WeaponA and ShellA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('00b13a4d', 'Norma.WeaponA.LightMap.2048')),
            (multiply_section_if_missing,     ('00b13a4d', 'Norma.ShellA.LightMap.2048')),
        ],
        '7ae5f4d6': [
            (log,                             ('3.0 -> 3.1: Norma WeaponA and ShellA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('79a583ad',)),
        ],
        '79a583ad': [
            (log,                             ('3.1: Norma WeaponA and ShellA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b70b6037', 'Norma.WeaponA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('b70b6037', 'Norma.ShellA.MaterialMap.1024')),
        ],
        '1db67ade': [
            (log,                             ('3.0 -> 3.1: Norma WeaponA and ShellA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('b70b6037',)),
        ],
        'b70b6037': [
            (log,                             ('3.1: Norma WeaponA and ShellA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ca38d6a1', 'Norma.Weapon.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('79a583ad', 'Norma.WeaponA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('79a583ad', 'Norma.ShellA.MaterialMap.2048')),
        ],
        # Weapon shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Shell Component ====================
        '85361021': [
            (log,                             ('3.0 - 3.2: Norma Shell IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '1b29ee19': [
            (log,                             ('3.0: Norma Shell Draw VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        'e2a92567': [
            (log,                             ('3.0: Norma Shell Position VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e3fafeeb',)),
        ],
        '1d67e673': [
            (log,                             ('3.0: Norma Shell Texcoord VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
            (update_hash,                     ('44991f30',)),
        ],
        '10d0bc6f': [
            (log,                             ('3.0: Norma Shell Blend VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        'e3fafeeb': [
            (log,                             ('3.1: Norma Shell VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        '44991f30': [
            (log,                             ('3.1: Norma Shell VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        '8b699f2d': [
            (log,                             ('3.1: Norma Shell VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        'bd112545': [
            (log,                             ('3.1: Norma Shell VB Hash',)),
            (add_section_if_missing,          ('85361021', 'Norma.Shell.IB', 'match_priority = 0\n')),
        ],
        # Shell shares its Diffuse, NormalMap, LightMap and MaterialMap hashes with Weapon; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Norma',
    'game_versions': ['3.0', '3.1', '3.2'],
}
