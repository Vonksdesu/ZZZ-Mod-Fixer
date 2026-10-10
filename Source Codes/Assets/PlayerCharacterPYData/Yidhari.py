"""
Yidhari Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 2.4 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns Yidhari's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '2022936e': [
            (log,                             ('2.4 - 3.2: Yidhari Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '2736d089': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Draw VB Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        ],
        '4512a51e': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Position VB Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        ],
        '028c0d28': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        ],
        '6a65d55c': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Blend VB Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
        ],
        'd0587bc2': [
            (log,                             ('2.4 - 3.2: Yidhari HairA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aefe5860', 'Yidhari.HairA.Diffuse.1024')),
        ],
        'aefe5860': [
            (log,                             ('2.4 - 3.2: Yidhari HairA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d0587bc2', 'Yidhari.HairA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('2.4 - 3.2: Yidhari HairA, BodyA, TailA and weapon - 武器A NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Yidhari.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yidhari.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yidhari.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Yidhari.weapon - 武器A.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('2.4 - 3.2: Yidhari HairA, BodyA, TailA and weapon - 武器A NormalMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Yidhari.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yidhari.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yidhari.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Yidhari.weapon - 武器A.NormalMap.2048')),
        ],
        '42ef8882': [
            (log,                             ('2.4 - 3.2: Yidhari HairA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('222b6f58', 'Yidhari.HairA.LightMap.1024')),
        ],
        '222b6f58': [
            (log,                             ('2.4 - 3.2: Yidhari HairA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('42ef8882', 'Yidhari.HairA.LightMap.2048')),
        ],
        'bc5d6f24': [
            (log,                             ('2.4 - 3.2: Yidhari HairA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('527ac41b', 'Yidhari.HairA.MaterialMap.1024')),
        ],
        '527ac41b': [
            (log,                             ('2.4 - 3.2: Yidhari HairA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('2022936e', 'Yidhari.Hair.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('bc5d6f24', 'Yidhari.HairA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        'a5a5654d': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '225ffc91': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Shadow Draw VB Hash',)),
            (add_section_if_missing,          ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'e13a4a8c': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Shadow Position VB Hash',)),
            (add_section_if_missing,          ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        'a74fecc6': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Shadow Texcoord VB Hash',)),
            (add_section_if_missing,          ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
        ],
        '7d881667': [
            (log,                             ('2.4 - 3.2: Yidhari Hair Shadow Blend VB Hash',)),
            (add_section_if_missing,          ('a5a5654d', 'Yidhari.Hair Shadow.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        '12251f42': [
            (log,                             ('2.4 - 3.2: Yidhari Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '471aa92a': [
            (log,                             ('2.4 - 3.2: Yidhari Body Draw VB Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        ],
        '74f07fc5': [
            (log,                             ('2.4 - 3.2: Yidhari Body Position VB Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        ],
        '2abc67fb': [
            (log,                             ('2.4 - 3.2: Yidhari Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        ],
        'eff05950': [
            (log,                             ('2.4 - 3.2: Yidhari Body Blend VB Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
        ],
        'ca51f269': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('89bec19d', 'Yidhari.BodyA.Diffuse.1024')),
        ],
        '89bec19d': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ca51f269', 'Yidhari.BodyA.Diffuse.2048')),
        ],
        '5b985a6f': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('381e8e5a', 'Yidhari.BodyA.LightMap.1024')),
        ],
        '2ae9bee8': [
            (log,                             ('2.3 -> 2.4: Yidhari BodyA LightMap 2048p Hash',)),
            (update_hash,                     ('5b985a6f',)),
        ],
        '381e8e5a': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b985a6f', 'Yidhari.BodyA.LightMap.2048')),
        ],
        '9ad20501': [
            (log,                             ('2.3 -> 2.4: Yidhari BodyA LightMap 1024p Hash',)),
            (update_hash,                     ('381e8e5a',)),
        ],
        '0e91ed54': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('9af65de7', 'Yidhari.BodyA.MaterialMap.1024')),
        ],
        '9af65de7': [
            (log,                             ('2.4 - 3.2: Yidhari BodyA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('12251f42', 'Yidhari.Body.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0e91ed54', 'Yidhari.BodyA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        '4cb99618': [
            (log,                             ('2.4 - 3.2: Yidhari Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'bf5562d4': [
            (log,                             ('2.4 - 3.2: Yidhari Tail Draw VB Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
        ],
        'c9dab2d3': [
            (log,                             ('2.4 - 3.2: Yidhari Tail Position VB Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
        ],
        '344e456e': [
            (log,                             ('2.4 - 3.2: Yidhari Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
        ],
        '9b99674d': [
            (log,                             ('2.4 - 3.2: Yidhari Tail Blend VB Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
        ],
        '2156a161': [
            (log,                             ('2.4 - 3.2: Yidhari TailA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('067b0a15', 'Yidhari.TailA.Diffuse.1024')),
        ],
        '067b0a15': [
            (log,                             ('2.4 - 3.2: Yidhari TailA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2156a161', 'Yidhari.TailA.Diffuse.2048')),
        ],
        '8bf59f48': [
            (log,                             ('2.4 - 3.2: Yidhari TailA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6b99432e', 'Yidhari.TailA.LightMap.1024')),
        ],
        '6b99432e': [
            (log,                             ('2.4 - 3.2: Yidhari TailA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('8bf59f48', 'Yidhari.TailA.LightMap.2048')),
        ],
        'e0bb4de9': [
            (log,                             ('2.4 - 3.2: Yidhari TailA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('0bf712a3', 'Yidhari.TailA.MaterialMap.1024')),
        ],
        '0bf712a3': [
            (log,                             ('2.4 - 3.2: Yidhari TailA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('4cb99618', 'Yidhari.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e0bb4de9', 'Yidhari.TailA.MaterialMap.2048')),
        ],

        # ==================== eyebrow Component ====================
        '02072970': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '534c2f9b': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrow VertexLimit VB Hash',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
        ],
        '695ebcdc': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrow Position VB Hash',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
        ],
        'cf1a7297': [
            (log,                             ('2.4 - 3.1: Yidhari eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
            (update_hash,                     ('baf394c7',)),
        ],
        'baf394c7': [
            (log,                             ('3.2: Yidhari eyebrow Texcoord VB Hash',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'ee532c5b': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrow Blend VB Hash',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
        ],
        'c6e0cfbe': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4753db8f', 'Yidhari.eyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('4753db8f', 'Yidhari.FaceA.Diffuse.1024')),
        ],
        '4753db8f': [
            (log,                             ('2.4 - 3.2: Yidhari eyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('02072970', 'Yidhari.eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('c6e0cfbe', 'Yidhari.eyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('c6e0cfbe', 'Yidhari.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        'a2406060': [
            (log,                             ('2.4 - 3.2: Yidhari Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '8abeb827': [
            (log,                             ('2.4 - 3.2: Yidhari Face VertexLimit VB Hash',)),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        ],
        'b0ac2b60': [
            (log,                             ('2.4 - 3.2: Yidhari Face Position VB Hash',)),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        ],
        '08316415': [
            (log,                             ('2.4 - 3.1: Yidhari Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
            (update_hash,                     ('40cdb80f',)),
        ],
        '40cdb80f': [
            (log,                             ('3.2: Yidhari Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
            (log,                             ('+ Remapping face texcoord buffer from stride 36 to 48',)),
            (zzz_13_remap_texcoord,           ('3.2_face', ('4B', '2f', '2f', '2f', '2f'), ('4f', '2f', '2f', '2f', '2f'))),
        ],
        'de712ebf': [
            (log,                             ('2.4 - 3.2: Yidhari Face Blend VB Hash',)),
            (add_section_if_missing,          ('a2406060', 'Yidhari.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== weapon - 武器 Component ====================
        'bc96ab6e': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器 IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6bc320f0': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器 VertexLimit VB Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        '09c65b14': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器 Position VB Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        '5a6fe39e': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器 Texcoord VB Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        'f98b369d': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器 Blend VB Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
        ],
        '48889652': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('85b7643e', 'Yidhari.weapon - 武器A.Diffuse.1024')),
        ],
        '85b7643e': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('48889652', 'Yidhari.weapon - 武器A.Diffuse.2048')),
        ],
        'e6728419': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A LightMap 2048p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cbb02c28', 'Yidhari.weapon - 武器A.LightMap.1024')),
        ],
        'cbb02c28': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A LightMap 1024p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e6728419', 'Yidhari.weapon - 武器A.LightMap.2048')),
        ],
        '42666703': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d17095b0', 'Yidhari.weapon - 武器A.MaterialMap.1024')),
        ],
        'd17095b0': [
            (log,                             ('2.4 - 3.2: Yidhari weapon - 武器A MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('bc96ab6e', 'Yidhari.weapon - 武器.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('42666703', 'Yidhari.weapon - 武器A.MaterialMap.2048')),
        ],

        # ==================== RgbBars Component (legacy, not in DB 2.2 - 3.1) ====================
        '1c164f7f': [
            (log,                             ('2.5: Yidhari RgbBars IB Hash',)),
            (add_ib_check_if_missing,),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Yidhari',
    'game_versions': ['2.4', '2.5', '2.6', '2.7', '2.8', '3.0', '3.1', '3.2'],
}
