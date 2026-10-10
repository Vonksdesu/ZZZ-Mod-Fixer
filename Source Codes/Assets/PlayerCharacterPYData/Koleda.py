"""
Koleda Character Hash Commands
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
    Returns Koleda's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '242a8d48': [
            (log,                             ('2.2 - 3.2: Koleda Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '366e92ac': [
            (log,                             ('2.2 - 3.2: Koleda Hair Draw VB Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        'e5de61e4': [
            (log,                             ('2.2 - 3.2: Koleda Hair Position VB Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        'e35571a9': [
            (log,                             ('2.2 - 3.2: Koleda Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        '1a9b182a': [
            (log,                             ('1.2 -> 1.3: Koleda Hair Texcoord Hash',)),
            (update_hash,                     ('e35571a9',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_13_remap_texcoord,           (
                '13_koleda_hair',
                ('4B', '2e', '2f', '2e'),
                ('4B', '2f', '2f', '2f'),
            )),
        ],
        'c6b75898': [
            (log,                             ('2.2 - 3.2: Koleda Hair Blend VB Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        'e8e89f00': [
            (log,                             ('2.2 - 3.2: Koleda HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b0046e5a', 'Koleda.HairA.Diffuse.1024')),
        ],
        'b0046e5a': [
            (log,                             ('2.2 - 3.2: Koleda HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e8e89f00', 'Koleda.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Koleda HairA, BodyA and weapon NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('798adba3', '7a46b52a'), 'Koleda.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     (('798adba3', '0914d3d3'), 'Koleda.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Koleda.weapon.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Koleda HairA, BodyA and weapon NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ebac056e', 'd1aac666'), 'Koleda.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     (('ebac056e', 'e71d134f'), 'Koleda.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Koleda.weapon.NormalMap.2048')),
        ],
        'd1aac666': [
            (log,                             ('1.0 -> 2.5: Koleda HairA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '7a46b52a': [
            (log,                             ('1.0: Koleda HairA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        'a451ca03': [
            (log,                             ('2.2 - 3.2: Koleda HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('1b33709a', '144ab293'), 'Koleda.HairA.LightMap.1024')),
        ],
        '1b33709a': [
            (log,                             ('2.2 - 3.2: Koleda HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a451ca03', '8042506d'), 'Koleda.HairA.LightMap.2048')),
        ],
        '8042506d': [
            (log,                             ('1.0 -> 2.5: Koleda HairA LightMap 2048p Hash',)),
            (update_hash,                     ('a451ca03',)),
        ],
        '144ab293': [
            (log,                             ('1.0: Koleda HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],
        '058d85b5': [
            (log,                             ('2.5: Koleda HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('242a8d48', 'Koleda.Hair.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hair Shadow Component ====================
        '67230c9f': [
            (log,                             ('2.2 - 3.2: Koleda Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '231aab5a': [
            (log,                             ('2.2 - 3.2: Koleda Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('67230c9f', 'Koleda.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '7c0d67d5': [
            (log,                             ('2.2 - 3.2: Koleda Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('67230c9f', 'Koleda.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '4a06c423': [
            (log,                             ('2.2 - 3.2: Koleda Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('67230c9f', 'Koleda.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '2d32c8fd': [
            (log,                             ('2.2 - 3.2: Koleda Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('67230c9f', 'Koleda.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '3afb3865': [
            (log,                             ('2.2 - 3.2: Koleda Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2c856fbc': [
            (log,                             ('2.2 - 3.2: Koleda Body Draw VB Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        '28b188d4': [
            (log,                             ('2.2 - 3.2: Koleda Body Position VB Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        '38b31082': [
            (log,                             ('2.2 - 3.2: Koleda Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        'e3021a32': [
            (log,                             ('1.2 -> 1.3: Koleda Body Texcoord Hash',)),
            (update_hash,                     ('38b31082',)),
            (log,                             ('+ Remapping texcoord buffer',)),
            (zzz_13_remap_texcoord,           (
                '13_koleda_body',
                ('4B', '2e', '2f', '2e'),
                ('4B', '2f', '2f', '2f'),
            )),
        ],
        'ad8e1d95': [
            (log,                             ('2.2 - 3.2: Koleda Body Blend VB Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        '337fd6a2': [
            (log,                             ('2.2 - 3.2: Koleda BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ce10237d', 'Koleda.BodyA.Diffuse.1024')),
        ],
        'ce10237d': [
            (log,                             ('2.2 - 3.2: Koleda BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('337fd6a2', 'Koleda.BodyA.Diffuse.2048')),
        ],
        'e71d134f': [
            (log,                             ('1.0 -> 2.5: Koleda BodyA NormalMap 2048p Hash',)),
            (update_hash,                     ('ebac056e',)),
        ],
        '0914d3d3': [
            (log,                             ('1.0: Koleda BodyA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        '7c1bce32': [
            (log,                             ('2.2 - 3.2: Koleda BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('a1087d61', 'db58787e'), 'Koleda.BodyA.LightMap.1024')),
        ],
        'a1087d61': [
            (log,                             ('2.2 - 3.2: Koleda BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7c1bce32', '78e0f9f5'), 'Koleda.BodyA.LightMap.2048')),
        ],
        '78e0f9f5': [
            (log,                             ('1.0 -> 2.5: Koleda BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('7c1bce32',)),
        ],
        'db58787e': [
            (log,                             ('1.0: Koleda BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        'b60ace0c': [
            (log,                             ('2.2 - 3.2: Koleda BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('1c162e9c', '02e6cb95'), 'Koleda.BodyA.MaterialMap.1024')),
        ],
        '1c162e9c': [
            (log,                             ('2.2 - 3.2: Koleda BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b60ace0c', '6f34885f'), 'Koleda.BodyA.MaterialMap.2048')),
        ],
        '6f34885f': [
            (log,                             ('1.0 -> 2.5: Koleda BodyA MaterialMap 2048p Hash',)),
            (update_hash,                     ('b60ace0c',)),
        ],
        '02e6cb95': [
            (log,                             ('1.0: Koleda BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('3afb3865', 'Koleda.Body.IB', 'match_priority = 0\n')),
        ],
        # Body shares its NormalMap hashes with Hair; see that Component above.

        # ==================== Face Component ====================
        '0e74656e': [
            (log,                             ('2.2 - 3.2: Koleda Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '78e1fa18': [
            (log,                             ('2.2 - 3.2: Koleda Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
        ],
        '42f3695f': [
            (log,                             ('2.2 - 3.2: Koleda Face Position VB Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
        ],
        'f41b27e6': [
            (log,                             ('2.2 - 3.1: Koleda Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('57994826',)),
        ],
        '57994826': [
            (log,                             ('3.2: Koleda Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'a5539a26': [
            (log,                             ('1.2 -> 1.3: Koleda Head Texcoord Hash',)),
            (update_hash,                     ('f41b27e6',)),
        ],
        'cd9babc2': [
            (log,                             ('2.2 - 3.2: Koleda Face Blend VB Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
        ],
        '200db5c4': [
            (log,                             ('2.2 - 3.2: Koleda FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f1045670', 'Koleda.FaceA.Diffuse.1024')),
        ],
        'f1045670': [
            (log,                             ('2.2 - 3.2: Koleda FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('0e74656e', 'Koleda.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('200db5c4', 'Koleda.FaceA.Diffuse.2048')),
        ],

        # ==================== Weapon Component ====================
        '2f2167a0': [
            (log,                             ('2.2 - 3.2: Koleda weapon IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'e22c571d': [
            (log,                             ('2.2 - 3.2: Koleda weapon VertexLimit VB Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
        ],
        '897140f5': [
            (log,                             ('2.2 - 3.2: Koleda weapon Position VB Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
        ],
        '6d2ee590': [
            (log,                             ('2.2 - 3.2: Koleda weapon Texcoord VB Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
        ],
        '5ef33d0a': [
            (log,                             ('2.2 - 3.2: Koleda weapon Blend VB Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
        ],
        '9ccded50': [
            (log,                             ('2.2 - 3.2: Koleda weapon Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1fe2b399', 'Koleda.weapon.Diffuse.1024')),
        ],
        '1fe2b399': [
            (log,                             ('2.2 - 3.2: Koleda weapon Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9ccded50', 'Koleda.weapon.Diffuse.2048')),
        ],
        '0c993237': [
            (log,                             ('2.2 - 3.2: Koleda weapon LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1da699e7', 'Koleda.weapon.LightMap.1024')),
        ],
        '1da699e7': [
            (log,                             ('2.2 - 3.2: Koleda weapon LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0c993237', 'Koleda.weapon.LightMap.2048')),
        ],
        'af1fbaa3': [
            (log,                             ('2.2 - 3.2: Koleda weapon MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('12f1688d', 'Koleda.weapon.MaterialMap.1024')),
        ],
        '12f1688d': [
            (log,                             ('2.2 - 3.2: Koleda weapon MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2f2167a0', 'Koleda.weapon.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('af1fbaa3', 'Koleda.weapon.MaterialMap.2048')),
        ],
        # weapon shares its NormalMap hashes with Hair; see that Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Koleda',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
