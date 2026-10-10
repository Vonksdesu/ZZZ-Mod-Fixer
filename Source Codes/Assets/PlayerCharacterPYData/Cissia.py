"""
Cissia Character Hash Commands
ZZZ Mod Fixer v2.7
Game Version: 2.7 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Cissia's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        'e4785f80': [
            (log,                             ('2.7 - 3.2: Cissia Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '33b532e5': [
            (log,                             ('2.7 - 3.2: Cissia Hair Draw VB Hash',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        ],
        '639456c7': [
            (log,                             ('2.7 - 3.2: Cissia Hair Position VB Hash',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        ],
        'a36d2401': [
            (log,                             ('2.7 - 3.2: Cissia Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        ],
        'b93219f1': [
            (log,                             ('2.7 - 3.2: Cissia Hair Blend VB Hash',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
        ],
        'b39896c4': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9aa301f1', 'Cissia.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     ('9aa301f1', 'Cissia.BodyB.Diffuse.1024')),
        ],
        '9aa301f1': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b39896c4', 'Cissia.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     ('b39896c4', 'Cissia.BodyB.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.7 - 3.2: Cissia HairA, BodyA, BodyB, BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.BodyB.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.BodyC.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.SpearHandleA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.SpearHeadA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.SpearBarrelA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Cissia.Spear(changing form)A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.7 - 3.2: Cissia HairA, BodyA, BodyB, BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.BodyB.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.BodyC.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.SpearHandleA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.SpearHeadA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.SpearBarrelA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Cissia.Spear(changing form)A.NormalMap.2048')),
        ],
        '31674c56': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0c2d5ee2', 'Cissia.HairA.LightMap.1024')),
            (multiply_section_if_missing,     ('0c2d5ee2', 'Cissia.BodyB.LightMap.1024')),
        ],
        '0c2d5ee2': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('31674c56', 'Cissia.HairA.LightMap.2048')),
            (multiply_section_if_missing,     ('31674c56', 'Cissia.BodyB.LightMap.2048')),
        ],
        'abb852a0': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('64a85915', 'Cissia.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('64a85915', 'Cissia.BodyB.MaterialMap.1024')),
        ],
        '64a85915': [
            (log,                             ('2.7 - 3.2: Cissia HairA and BodyB MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e4785f80', 'Cissia.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('abb852a0', 'Cissia.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('abb852a0', 'Cissia.BodyB.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '8f34fc78': [
            (log,                             ('2.7 - 3.2: Cissia Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Tongue Component ====================
        'e5ced7d5': [
            (log,                             ('2.7 - 3.2: Cissia Tongue IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a3b04e84': [
            (log,                             ('2.7 - 3.2: Cissia Tongue Draw VB Hash',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        ],
        '3e82033f': [
            (log,                             ('2.7 - 3.2: Cissia Tongue Position VB Hash',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        ],
        '32f6d33a': [
            (log,                             ('2.7 - 3.2: Cissia Tongue Texcoord VB Hash',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        ],
        'c3082752': [
            (log,                             ('2.7 - 3.2: Cissia Tongue Blend VB Hash',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
        ],
        '8f55186a': [
            (log,                             ('2.7 - 3.2: Cissia TongueA, EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c72539cd', 'Cissia.TongueA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c72539cd', 'Cissia.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('c72539cd', 'Cissia.FaceA.Diffuse.1024')),
        ],
        'c72539cd': [
            (log,                             ('2.7 - 3.2: Cissia TongueA, EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('e5ced7d5', 'Cissia.Tongue.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8f55186a', 'Cissia.TongueA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8f55186a', 'Cissia.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('8f55186a', 'Cissia.FaceA.Diffuse.2048')),
        ],

        # ==================== Body Component ====================
        'ff2ec4d6': [
            (log,                             ('2.7 - 3.2: Cissia Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9645e284': [
            (log,                             ('2.7 - 3.2: Cissia Body Draw VB Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        ],
        '1a95227f': [
            (log,                             ('2.7 - 3.2: Cissia Body Position VB Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        ],
        'e6527ff0': [
            (log,                             ('2.7 - 3.2: Cissia Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        ],
        '3b944072': [
            (log,                             ('2.7 - 3.2: Cissia Body Blend VB Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
        ],
        'fcfeb117': [
            (log,                             ('2.7 - 3.2: Cissia BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2638fa23', 'Cissia.BodyA.Diffuse.1024')),
        ],
        '2638fa23': [
            (log,                             ('2.7 - 3.2: Cissia BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('fcfeb117', 'Cissia.BodyA.Diffuse.2048')),
        ],
        '2b6d5c26': [
            (log,                             ('2.7 - 3.2: Cissia BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4862ab5d', 'Cissia.BodyA.LightMap.1024')),
        ],
        '4862ab5d': [
            (log,                             ('2.7 - 3.2: Cissia BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2b6d5c26', 'Cissia.BodyA.LightMap.2048')),
        ],
        'e5edf7dd': [
            (log,                             ('2.7 - 3.2: Cissia BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b0a060f2', 'Cissia.BodyA.MaterialMap.1024')),
        ],
        'b0a060f2': [
            (log,                             ('2.7 - 3.2: Cissia BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e5edf7dd', 'Cissia.BodyA.MaterialMap.2048')),
        ],
        'f8739729': [
            (log,                             ('2.7 -> 2.8: Cissia BodyC Diffuse 2048p Hash',)),
            (update_hash,                     ('ec85e98d',)),
        ],
        'ec85e98d': [
            (log,                             ('2.8 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.BodyC.Diffuse.1024')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.TailA.Diffuse.1024')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.SpearHandleA.Diffuse.1024')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.SpearHeadA.Diffuse.1024')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.SpearBarrelA.Diffuse.1024')),
            (multiply_section_if_missing,     (('6d861173', 'f5ecd616'), 'Cissia.Spear(changing form)A.Diffuse.1024')),
        ],
        'f5ecd616': [
            (log,                             ('2.7 -> 2.8: Cissia BodyC Diffuse 1024p Hash',)),
            (update_hash,                     ('6d861173',)),
        ],
        '6d861173': [
            (log,                             ('2.8 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.BodyC.Diffuse.2048')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.TailA.Diffuse.2048')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.SpearHandleA.Diffuse.2048')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.SpearHeadA.Diffuse.2048')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.SpearBarrelA.Diffuse.2048')),
            (multiply_section_if_missing,     (('ec85e98d', 'f8739729'), 'Cissia.Spear(changing form)A.Diffuse.2048')),
        ],
        '6fadb6f5': [
            (log,                             ('2.7 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.BodyC.LightMap.1024')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.TailA.LightMap.1024')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.SpearHandleA.LightMap.1024')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.SpearHeadA.LightMap.1024')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.SpearBarrelA.LightMap.1024')),
            (multiply_section_if_missing,     ('090684bd', 'Cissia.Spear(changing form)A.LightMap.1024')),
        ],
        '090684bd': [
            (log,                             ('2.7 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.BodyC.LightMap.2048')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.TailA.LightMap.2048')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.SpearHandleA.LightMap.2048')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.SpearHeadA.LightMap.2048')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.SpearBarrelA.LightMap.2048')),
            (multiply_section_if_missing,     ('6fadb6f5', 'Cissia.Spear(changing form)A.LightMap.2048')),
        ],
        '1d5d53cd': [
            (log,                             ('2.7 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.BodyC.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.TailA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.SpearHandleA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.SpearHeadA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.SpearBarrelA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d59dc29c', 'Cissia.Spear(changing form)A.MaterialMap.1024')),
        ],
        'd59dc29c': [
            (log,                             ('2.7 - 3.2: Cissia BodyC, TailA, SpearHandleA, SpearHeadA, SpearBarrelA and Spear(changing form)A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('ff2ec4d6', 'Cissia.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('29123d5a', 'Cissia.SpearHead.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.BodyC.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.TailA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.SpearHandleA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.SpearHeadA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.SpearBarrelA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('1d5d53cd', 'Cissia.Spear(changing form)A.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '4c11c155': [
            (log,                             ('2.7 - 3.2: Cissia Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '3b4de0d1': [
            (log,                             ('2.7 - 3.2: Cissia Tail Draw VB Hash',)),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        ],
        'efed0e09': [
            (log,                             ('2.7 - 3.2: Cissia Tail Position VB Hash',)),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        ],
        '8f017202': [
            (log,                             ('2.7 - 3.2: Cissia Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        ],
        '90634c3b': [
            (log,                             ('2.7 - 3.2: Cissia Tail Blend VB Hash',)),
            (add_section_if_missing,          ('4c11c155', 'Cissia.Tail.IB', 'match_priority = 0\n')),
        ],
        # Tail shares all texture hashes with Body (set C); see Body Component above.

        # ==================== Eyebrow Component ====================
        '7c01dc6b': [
            (log,                             ('2.7 - 3.2: Cissia Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6e02f849': [
            (log,                             ('2.7: Cissia Eyebrow Draw VB Hash',)),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '8b927127': [
            (log,                             ('2.7: Cissia Eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        'cd87eb81': [
            (log,                             ('2.7: Cissia Eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        '09fa4349': [
            (log,                             ('2.7: Cissia Eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('7c01dc6b', 'Cissia.Eyebrow.IB', 'match_priority = 0\n')),
        ],
        # Eyebrow shares its Diffuse with Tongue and Face; see Tongue Component above.

        # ==================== Face Component ====================
        'd1a31f0b': [
            (log,                             ('2.7 - 3.2: Cissia Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'a2d2a224': [
            (log,                             ('2.7 - 3.2: Cissia Face Draw VB Hash',)),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        ],
        '98c03163': [
            (log,                             ('2.7 - 3.2: Cissia Face Position VB Hash',)),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        ],
        'dfc76798': [
            (log,                             ('2.7 - 3.1: Cissia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2bc69f3c',)),
        ],
        '2bc69f3c': [
            (log,                             ('3.2: Cissia Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ed3245f0': [
            (log,                             ('2.7 - 3.2: Cissia Face Blend VB Hash',)),
            (add_section_if_missing,          ('d1a31f0b', 'Cissia.Face.IB', 'match_priority = 0\n')),
        ],
        # Face shares its Diffuse with Tongue and Eyebrow; see Tongue Component above.

        # ==================== SpearHandle Component ====================
        '29b5b0b0': [
            (log,                             ('2.7 - 3.2: Cissia SpearHandle IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9af3bf00': [
            (log,                             ('2.7 - 3.2: Cissia SpearHandle Draw VB Hash',)),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        ],
        'dee92405': [
            (log,                             ('2.7 - 3.2: Cissia SpearHandle Position VB Hash',)),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        ],
        '880e958d': [
            (log,                             ('2.7 - 3.2: Cissia SpearHandle Texcoord VB Hash',)),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        ],
        '6354dee4': [
            (log,                             ('2.7 - 3.2: Cissia SpearHandle Blend VB Hash',)),
            (add_section_if_missing,          ('29b5b0b0', 'Cissia.SpearHandle.IB', 'match_priority = 0\n')),
        ],
        # SpearHandle shares all texture hashes with Body (set C); see Body Component above.

        # ==================== SpearHead Component ====================
        '29123d5a': [
            (log,                             ('2.7 - 3.2: Cissia SpearHead IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        # SpearHead shares all texture hashes with Body (set C); see Body Component above.

        # ==================== SpearBarrel Component ====================
        'bad668cc': [
            (log,                             ('2.7 - 3.2: Cissia SpearBarrel IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '19bac37e': [
            (log,                             ('2.7 - 3.2: Cissia SpearBarrel Draw VB Hash',)),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        ],
        '91e05512': [
            (log,                             ('2.7 - 3.2: Cissia SpearBarrel Position VB Hash',)),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        ],
        '2785fe49': [
            (log,                             ('2.7 - 3.2: Cissia SpearBarrel Texcoord VB Hash',)),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        ],
        'b813c97f': [
            (log,                             ('2.7 - 3.2: Cissia SpearBarrel Blend VB Hash',)),
            (add_section_if_missing,          ('bad668cc', 'Cissia.SpearBarrel.IB', 'match_priority = 0\n')),
        ],
        # SpearBarrel shares all texture hashes with Body (set C); see Body Component above.

        # ==================== Spear(changing form) Component ====================
        'd49a5866': [
            (log,                             ('2.7 - 3.2: Cissia Spear(changing form) IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '7647eba5': [
            (log,                             ('2.7 - 3.2: Cissia Spear(changing form) Draw VB Hash',)),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
        ],
        '5b71ede8': [
            (log,                             ('2.7 - 3.2: Cissia Spear(changing form) Position VB Hash',)),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
        ],
        'c37f63b8': [
            (log,                             ('2.7 - 3.2: Cissia Spear(changing form) Texcoord VB Hash',)),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
        ],
        '32b90f8b': [
            (log,                             ('2.7 - 3.2: Cissia Spear(changing form) Blend VB Hash',)),
            (add_section_if_missing,          ('d49a5866', 'Cissia.Spear(changing form).IB', 'match_priority = 0\n')),
        ],
        # Spear(changing form) shares all texture hashes with Body (set C); see Body Component above.
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Cissia',
    'game_versions': ['2.7', '2.8', '3.0', '3.1', '3.2'],
}
