"""
AriaAgent Character Hash Commands
ZZZ Mod Fixer v2.6
Game Version: 2.6
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns AriaAgent's hash commands dictionary.
    
    All command classes are passed as parameters to avoid circular imports.
    """
    return {
# === IB Hashes ===
'046400d3': [
        (log,                           ('2.6: AriaAgent Body IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'ffa703e8': [
        (log,                           ('2.6: AriaAgent Face IB Hash',)),
        (add_ib_check_if_missing,),
    ],
'1173ff78': [
        (log,                           ('2.6: AriaAgent Hair IB Hash',)),
        (add_ib_check_if_missing,),
    ],


# === AriaAgent Textures (FaceA) ===
'6611eaa1': [
        (log,                           ('2.6: AriaAgent FaceA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('741d7c8f', 'AriaAgent.FaceA.Diffuse.2048')),
    ],
'741d7c8f': [
        (log,                           ('2.6: AriaAgent FaceA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('6611eaa1', 'AriaAgent.FaceA.Diffuse.1024')),
    ],

# === AriaAgent Textures (HairA) ===
'f0aec120': [
        (log,                           ('2.6: AriaAgent HairA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('be70c507', 'AriaAgent.HairA.Diffuse.2048')),
    ],
'be70c507': [
        (log,                           ('2.6: AriaAgent HairA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('f0aec120', 'AriaAgent.HairA.Diffuse.1024')),
    ],
'9e2e56b3': [
        (log,                           ('2.6: AriaAgent HairA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('41124010', 'AriaAgent.HairA.LightMap.2048')),
    ],
'41124010': [
        (log,                           ('2.6: AriaAgent HairA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('9e2e56b3', 'AriaAgent.HairA.LightMap.1024')),
    ],
'002360e1': [
        (log,                           ('2.6: AriaAgent HairA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('01087a99', 'AriaAgent.HairA.MaterialMap.2048')),
    ],
'01087a99': [
        (log,                           ('2.6: AriaAgent HairA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('002360e1', 'AriaAgent.HairA.MaterialMap.1024')),
    ],

# === AriaAgent Textures (BodyA) ===
'702063c7': [
        (log,                           ('2.6: AriaAgent BodyA Diffuse 1024p Hash',)),
        (multiply_section_if_missing,        ('859bb461', 'AriaAgent.BodyA.Diffuse.2048')),
    ],
'859bb461': [
        (log,                           ('2.6: AriaAgent BodyA Diffuse 2048p Hash',)),
        (multiply_section_if_missing,        ('702063c7', 'AriaAgent.BodyA.Diffuse.1024')),
    ],
'a588ea59': [
        (log,                           ('2.6: AriaAgent BodyA LightMap 1024p Hash',)),
        (multiply_section_if_missing,        ('ba534b39', 'AriaAgent.BodyA.LightMap.2048')),
    ],
'ba534b39': [
        (log,                           ('2.6: AriaAgent BodyA LightMap 2048p Hash',)),
        (multiply_section_if_missing,        ('a588ea59', 'AriaAgent.BodyA.LightMap.1024')),
    ],
'0a8badcd': [
        (log,                           ('2.6: AriaAgent BodyA MaterialMap 1024p Hash',)),
        (multiply_section_if_missing,        ('14aa84e5', 'AriaAgent.BodyA.MaterialMap.2048')),
    ],
'14aa84e5': [
        (log,                           ('2.6: AriaAgent BodyA MaterialMap 2048p Hash',)),
        (multiply_section_if_missing,        ('0a8badcd', 'AriaAgent.BodyA.MaterialMap.1024')),
    ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'AriaAgent',
    'game_versions': ['2.6'],
}
