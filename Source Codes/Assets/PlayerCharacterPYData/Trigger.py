"""
Trigger Character Hash Commands
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
    Returns Trigger's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '8e98ef9a': [
            (log,                             ('2.2 - 3.2: Trigger Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'b0625293': [
            (log,                             ('2.2 - 3.2: Trigger Hair Draw VB Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        ],
        'f066913d': [
            (log,                             ('2.2 - 3.2: Trigger Hair Position VB Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        ],
        'b12abbeb': [
            (log,                             ('2.2 - 3.2: Trigger Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        ],
        'acd25c98': [
            (log,                             ('2.2 - 3.2: Trigger Hair Blend VB Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
        ],
        'e826a564': [
            (log,                             ('2.2 - 3.2: Trigger HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('984e7896', 'Trigger.HairA.Diffuse.1024')),
        ],
        '984e7896': [
            (log,                             ('2.2 - 3.2: Trigger HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e826a564', 'Trigger.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.2 - 3.2: Trigger HairA, BodyA, weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Trigger.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Trigger.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Trigger.weapon - 枪身A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Trigger.weapon - 枪托A.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Trigger.weapon - 弹匣A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.2 - 3.2: Trigger HairA, BodyA, weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Trigger.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Trigger.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Trigger.weapon - 枪身A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Trigger.weapon - 枪托A.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Trigger.weapon - 弹匣A.NormalMap.2048')),
        ],
        '23f2a4cf': [
            (log,                             ('2.2 - 3.2: Trigger HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c321345c', 'Trigger.HairA.LightMap.1024')),
        ],
        'c321345c': [
            (log,                             ('2.2 - 3.2: Trigger HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('23f2a4cf', 'Trigger.HairA.LightMap.2048')),
        ],
        'b24f1752': [
            (log,                             ('2.2 - 3.2: Trigger HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ee3c3fe', 'Trigger.HairA.MaterialMap.1024')),
        ],
        '4ee3c3fe': [
            (log,                             ('2.2 - 3.2: Trigger HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('8e98ef9a', 'Trigger.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b24f1752', 'Trigger.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '69c27d44': [
            (log,                             ('2.2 - 3.2: Trigger Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Body Component ====================
        '7f32eeae': [
            (log,                             ('2.2 - 3.2: Trigger Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5fdaccd2': [
            (log,                             ('2.2 - 3.2: Trigger Body Draw VB Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        ],
        'e4ae41fd': [
            (log,                             ('2.2 - 3.2: Trigger Body Position VB Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        ],
        'b3c0a13c': [
            (log,                             ('2.2 - 3.2: Trigger Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        ],
        'e31a3b5f': [
            (log,                             ('2.2 - 3.2: Trigger Body Blend VB Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
        ],
        '6631eadc': [
            (log,                             ('2.2 - 3.2: Trigger BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8cffa733', 'Trigger.BodyA.Diffuse.1024')),
        ],
        '8cffa733': [
            (log,                             ('2.2 - 3.2: Trigger BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6631eadc', 'Trigger.BodyA.Diffuse.2048')),
        ],
        '05250215': [
            (log,                             ('2.2 - 3.2: Trigger BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2c72b961', 'Trigger.BodyA.LightMap.1024')),
        ],
        '2c72b961': [
            (log,                             ('2.2 - 3.2: Trigger BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('05250215', 'Trigger.BodyA.LightMap.2048')),
        ],
        '985c5f52': [
            (log,                             ('2.2 - 3.2: Trigger BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cd507047', 'Trigger.BodyA.MaterialMap.1024')),
        ],
        'cd507047': [
            (log,                             ('2.2 - 3.2: Trigger BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('7f32eeae', 'Trigger.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('985c5f52', 'Trigger.BodyA.MaterialMap.2048')),
        ],

        # ==================== Face Component ====================
        '40cd4182': [
            (log,                             ('2.2 - 3.2: Trigger Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8057c562': [
            (log,                             ('2.2 - 3.2: Trigger Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        ],
        'ba455625': [
            (log,                             ('2.0 -> 2.1: Trigger Face Position VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('dfc69ad0',)),
        ],
        'dfc69ad0': [
            (log,                             ('2.2 - 3.2: Trigger Face Position VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        ],
        'b9f0d595': [
            (log,                             ('2.2 -> 2.3: Trigger Face Texcoord Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d4a12ab7',)),
        ],
        'd4a12ab7': [
            (log,                             ('2.3 - 3.1: Trigger Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('1132301e',)),
        ],
        '1132301e': [
            (log,                             ('3.2: Trigger Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        '1a9a858c': [
            (log,                             ('2.2 - 3.2: Trigger Face Blend VB Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
        ],
        '88728785': [
            (log,                             ('2.2 - 3.2: Trigger FaceA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cffc4b09', 'Trigger.FaceA.Diffuse.1024')),
        ],
        'cffc4b09': [
            (log,                             ('2.2 - 3.2: Trigger FaceA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('40cd4182', 'Trigger.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('88728785', 'Trigger.FaceA.Diffuse.2048')),
        ],

        # ==================== weapon - 枪身 Component ====================
        'f05e3a4a': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fa2ee314': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
        ],
        'ac917a82': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身 Position VB Hash',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
        ],
        '60fcff00': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身 Texcoord VB Hash',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
        ],
        'ca8565b9': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身 Blend VB Hash',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
        ],
        '19515c67': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('748df67a', 'Trigger.weapon - 枪身A.Diffuse.1024')),
            (multiply_section_if_missing,     ('748df67a', 'Trigger.weapon - 枪托A.Diffuse.1024')),
            (multiply_section_if_missing,     ('748df67a', 'Trigger.weapon - 弹匣A.Diffuse.1024')),
        ],
        '748df67a': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('19515c67', 'Trigger.weapon - 枪身A.Diffuse.2048')),
            (multiply_section_if_missing,     ('19515c67', 'Trigger.weapon - 枪托A.Diffuse.2048')),
            (multiply_section_if_missing,     ('19515c67', 'Trigger.weapon - 弹匣A.Diffuse.2048')),
        ],
        '2236b80e': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c7377a02', 'Trigger.weapon - 枪身A.LightMap.1024')),
            (multiply_section_if_missing,     ('c7377a02', 'Trigger.weapon - 枪托A.LightMap.1024')),
            (multiply_section_if_missing,     ('c7377a02', 'Trigger.weapon - 弹匣A.LightMap.1024')),
        ],
        'c7377a02': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2236b80e', 'Trigger.weapon - 枪身A.LightMap.2048')),
            (multiply_section_if_missing,     ('2236b80e', 'Trigger.weapon - 枪托A.LightMap.2048')),
            (multiply_section_if_missing,     ('2236b80e', 'Trigger.weapon - 弹匣A.LightMap.2048')),
        ],
        'a6d2b50e': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('799820a8', 'Trigger.weapon - 枪身A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('799820a8', 'Trigger.weapon - 枪托A.MaterialMap.1024')),
            (multiply_section_if_missing,     ('799820a8', 'Trigger.weapon - 弹匣A.MaterialMap.1024')),
        ],
        '799820a8': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪身A, weapon - 枪托A and weapon - 弹匣A MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('f05e3a4a', 'Trigger.weapon - 枪身.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a6d2b50e', 'Trigger.weapon - 枪身A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a6d2b50e', 'Trigger.weapon - 枪托A.MaterialMap.2048')),
            (multiply_section_if_missing,     ('a6d2b50e', 'Trigger.weapon - 弹匣A.MaterialMap.2048')),
        ],

        # ==================== weapon - 枪托 Component ====================
        'bb079ba3': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪托 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0cdfa94a': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪托 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
        ],
        '570ffcdc': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪托 Position VB Hash',)),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
        ],
        '73555896': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪托 Texcoord VB Hash',)),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
        ],
        '7ab2b542': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 枪托 Blend VB Hash',)),
            (add_section_if_missing,          ('bb079ba3', 'Trigger.weapon - 枪托.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 弹匣 Component ====================
        'f61f6acd': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 弹匣 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '773c85f4': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 弹匣 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
        ],
        '988144a6': [
            (log,                             ('2.0 -> 2.1: Trigger weapon - 弹匣 Position Hash',)),
            (update_hash,                     ('862efc96',)),
        ],
        '862efc96': [
            (log,                             ('2.2: Trigger weapon - 弹匣 Position VB Hash',)),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
        ],
        'b6d507d9': [
            (log,                             ('2.0 -> 2.1: Trigger weapon - 弹匣 Texcoord Hash',)),
            (update_hash,                     ('a58b916d',)),
        ],
        'a58b916d': [
            (log,                             ('2.2: Trigger weapon - 弹匣 Texcoord VB Hash',)),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
        ],
        '89c48e15': [
            (log,                             ('2.2 - 3.2: Trigger weapon - 弹匣 Blend VB Hash',)),
            (add_section_if_missing,          ('f61f6acd', 'Trigger.weapon - 弹匣.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Trigger',
    'game_versions': ['2.2', '2.3', '2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
