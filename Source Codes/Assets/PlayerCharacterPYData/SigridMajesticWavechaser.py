"""
SigridMajesticWavechaser Character Hash Commands
ZZZ Mod Fixer v2.5
Game Version: 3.1 - 3.2
"""

def get_hash_commands(log, update_hash, comment_sections, comment_commandlists,
                      remove_section, remove_indexed_sections, capture_section,
                      create_new_section, transfer_indexed_sections,
                      multiply_section_if_missing, add_ib_check_if_missing,
                      add_section_if_missing, zzz_13_remap_texcoord,
                      zzz_12_shrink_texcoord_color, update_buffer_blend_indices,
                      **kwargs):
    """
    Returns SigridMajesticWavechaser's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '84618ee0': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '840c1713': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair Draw VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
        ],
        '53d5d966': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair Position VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
        ],
        '6b1c911c': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
        ],
        '380ee24b': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair Blend VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
        ],
        '0c4bea0f': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.TailA.Diffuse.1024')),
            (update_hash,                     ('f2896dcc',)),
        ],
        'f2896dcc': [
            (log,                             ('3.2: SigridMajesticWavechaser HairA, HairpinA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'SigridMajesticWavechaser.TailA.Diffuse.1024')),
        ],
        '66dbe05f': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.TailA.Diffuse.2048')),
            (update_hash,                     ('cb3525dc',)),
        ],
        'cb3525dc': [
            (log,                             ('3.2: SigridMajesticWavechaser HairA, HairpinA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'SigridMajesticWavechaser.TailA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA, BodyA, TailA, SpearA and RotorBearingA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.SpearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.RotorBearingA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA, BodyA, TailA, SpearA and RotorBearingA NormalMap 1024p Hash, also RotorA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.HairpinA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.SpearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'SigridMajesticWavechaser.RotorBearingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'SigridMajesticWavechaser.RotorA.NormalMap.1024')),
        ],
        'da6a6f0b': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.TailA.LightMap.1024')),
            (update_hash,                     ('16d72691',)),
        ],
        '16d72691': [
            (log,                             ('3.2: SigridMajesticWavechaser HairA, HairpinA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'SigridMajesticWavechaser.TailA.LightMap.1024')),
        ],
        'bc582555': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.TailA.LightMap.2048')),
            (update_hash,                     ('d7d68132',)),
        ],
        'd7d68132': [
            (log,                             ('3.2: SigridMajesticWavechaser HairA, HairpinA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'SigridMajesticWavechaser.TailA.LightMap.2048')),
        ],
        'f5da0fcd': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d055f8e9', 'SigridMajesticWavechaser.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'SigridMajesticWavechaser.HairpinA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'SigridMajesticWavechaser.TailA.MaterialMap.1024')),
        ],
        'd055f8e9': [
            (log,                             ('3.1: SigridMajesticWavechaser HairA, HairpinA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'SigridMajesticWavechaser.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f5da0fcd', 'SigridMajesticWavechaser.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'SigridMajesticWavechaser.HairpinA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'SigridMajesticWavechaser.TailA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '81e925ed': [
            (log,                             ('3.1: SigridMajesticWavechaser Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Hairpin Component ====================
        'b51bdd59': [
            (log,                             ('3.1: SigridMajesticWavechaser Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6a8ea608': [
            (log,                             ('3.1: SigridMajesticWavechaser Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '63981c38': [
            (log,                             ('3.1: SigridMajesticWavechaser Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '937473ae': [
            (log,                             ('3.1: SigridMajesticWavechaser Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '68bfe8f5': [
            (log,                             ('3.1: SigridMajesticWavechaser Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'SigridMajesticWavechaser.Hairpin.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'd9e49957': [
            (log,                             ('3.1: SigridMajesticWavechaser Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '5f83ec60': [
            (log,                             ('3.1: SigridMajesticWavechaser Body Draw VB Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
        ],
        '525d51d8': [
            (log,                             ('3.1: SigridMajesticWavechaser Body Position VB Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
        ],
        '9331668a': [
            (log,                             ('3.1: SigridMajesticWavechaser Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
        ],
        '4923328d': [
            (log,                             ('3.1: SigridMajesticWavechaser Body Blend VB Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
        ],
        'b07c43ef': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('8874c184',)),
        ],
        '82a7f32e': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('3a0cfbd4',)),
        ],
        '8874c184': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b97a77bf', '3a0cfbd4'), 'SigridMajesticWavechaser.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     (('b97a77bf', '3a0cfbd4'), 'SigridMajesticWavechaser.RotorBearingA.Diffuse.1024')),
            (update_hash,                     ('7c862ede',)),
        ],
        '7c862ede': [
            (log,                             ('3.2: SigridMajesticWavechaser BodyA and RotorBearingA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('b97a77bf', '3a0cfbd4'), 'SigridMajesticWavechaser.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     (('b97a77bf', '3a0cfbd4'), 'SigridMajesticWavechaser.RotorBearingA.Diffuse.1024')),
        ],
        '3a0cfbd4': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7c862ede', '8874c184'), 'SigridMajesticWavechaser.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     (('7c862ede', '8874c184'), 'SigridMajesticWavechaser.RotorBearingA.Diffuse.2048')),
            (update_hash,                     ('b97a77bf',)),
        ],
        'b97a77bf': [
            (log,                             ('3.2: SigridMajesticWavechaser BodyA and RotorBearingA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('7c862ede', '8874c184'), 'SigridMajesticWavechaser.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     (('7c862ede', '8874c184'), 'SigridMajesticWavechaser.RotorBearingA.Diffuse.2048')),
        ],
        '5e907c41': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('2772f644',)),
        ],
        '1b4edd7b': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('cfc4ac8a',)),
        ],
        '2772f644': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('cfc4ac8a', 'SigridMajesticWavechaser.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('cfc4ac8a', 'SigridMajesticWavechaser.RotorBearingA.LightMap.1024')),
        ],
        'cfc4ac8a': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2772f644', 'SigridMajesticWavechaser.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('2772f644', 'SigridMajesticWavechaser.RotorBearingA.LightMap.2048')),
        ],
        'e104d477': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('aa626489', 'SigridMajesticWavechaser.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('aa626489', 'SigridMajesticWavechaser.RotorBearingA.MaterialMap.1024')),
        ],
        'aa626489': [
            (log,                             ('3.1: SigridMajesticWavechaser BodyA and RotorBearingA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('d9e49957', 'SigridMajesticWavechaser.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e104d477', 'SigridMajesticWavechaser.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('e104d477', 'SigridMajesticWavechaser.RotorBearingA.MaterialMap.2048')),
        ],

        # ==================== Tail Component ====================
        'b30db54e': [
            (log,                             ('3.1: SigridMajesticWavechaser Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cb72b377': [
            (log,                             ('3.1: SigridMajesticWavechaser Tail Draw VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
        ],
        'b3aeb830': [
            (log,                             ('3.1: SigridMajesticWavechaser Tail Position VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
        ],
        '84ef2fb1': [
            (log,                             ('3.1: SigridMajesticWavechaser Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
        ],
        '710b43f7': [
            (log,                             ('3.1: SigridMajesticWavechaser Tail Blend VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'SigridMajesticWavechaser.Tail.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '454ff522': [
            (log,                             ('3.1: SigridMajesticWavechaser Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '18b20f06': [
            (log,                             ('3.1: SigridMajesticWavechaser EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('454ff522', 'SigridMajesticWavechaser.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f178a6f2', 'SigridMajesticWavechaser.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('f178a6f2', 'SigridMajesticWavechaser.FaceA.Diffuse.1024')),
        ],
        'f178a6f2': [
            (log,                             ('3.1: SigridMajesticWavechaser EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('454ff522', 'SigridMajesticWavechaser.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18b20f06', 'SigridMajesticWavechaser.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('18b20f06', 'SigridMajesticWavechaser.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '48625d6d': [
            (log,                             ('3.1: SigridMajesticWavechaser Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9b76d1d7': [
            (log,                             ('3.1: SigridMajesticWavechaser Face Draw VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
        ],
        'a1644290': [
            (log,                             ('3.1: SigridMajesticWavechaser Face Position VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
        ],
        'c90ff663': [
            (log,                             ('3.1: SigridMajesticWavechaser Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
        ],
        'e768b061': [
            (log,                             ('3.1: SigridMajesticWavechaser Face Blend VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'SigridMajesticWavechaser.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Spear Component ====================
        '285aa61f': [
            (log,                             ('3.1: SigridMajesticWavechaser Spear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cc9f0724': [
            (log,                             ('3.1: SigridMajesticWavechaser Spear Draw VB Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
        ],
        'f7f0b608': [
            (log,                             ('3.1: SigridMajesticWavechaser Spear Position VB Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
        ],
        '5ae0d9a1': [
            (log,                             ('3.1: SigridMajesticWavechaser Spear Texcoord VB Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
        ],
        '830f0c5c': [
            (log,                             ('3.1: SigridMajesticWavechaser Spear Blend VB Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
        ],
        'ec9c1ac4': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('98a57712', 'SigridMajesticWavechaser.SpearA.Diffuse.1024')),
        ],
        '98a57712': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ec9c1ac4', 'SigridMajesticWavechaser.SpearA.Diffuse.2048')),
        ],
        '3da2b650': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('6c9142f7', 'SigridMajesticWavechaser.SpearA.LightMap.1024')),
        ],
        '6c9142f7': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('3da2b650', 'SigridMajesticWavechaser.SpearA.LightMap.2048')),
        ],
        '1521edda': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('e1240523', 'SigridMajesticWavechaser.SpearA.MaterialMap.1024')),
        ],
        'e1240523': [
            (log,                             ('3.1: SigridMajesticWavechaser SpearA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('285aa61f', 'SigridMajesticWavechaser.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1521edda', 'SigridMajesticWavechaser.SpearA.MaterialMap.2048')),
        ],

        # ==================== Rotor Component ====================
        'd892c658': [
            (log,                             ('3.1: SigridMajesticWavechaser Rotor IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '914dcde9': [
            (log,                             ('3.1: SigridMajesticWavechaser Rotor Draw VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
        ],
        'fe91db45': [
            (log,                             ('3.1: SigridMajesticWavechaser Rotor Position VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
        ],
        'cd92341a': [
            (log,                             ('3.1: SigridMajesticWavechaser Rotor Texcoord VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
        ],
        '0bacf856': [
            (log,                             ('3.1: SigridMajesticWavechaser Rotor Blend VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
        ],
        '4fa99352': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a58912ea', 'SigridMajesticWavechaser.RotorA.Diffuse.1024')),
        ],
        'a58912ea': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4fa99352', 'SigridMajesticWavechaser.RotorA.Diffuse.2048')),
        ],
        'ffdc1ea7': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'SigridMajesticWavechaser.RotorA.NormalMap.2048')),
        ],
        '980d9016': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01f5701a', 'SigridMajesticWavechaser.RotorA.LightMap.1024')),
        ],
        '01f5701a': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('980d9016', 'SigridMajesticWavechaser.RotorA.LightMap.2048')),
        ],
        '1f036c21': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ba54e3f', 'SigridMajesticWavechaser.RotorA.MaterialMap.1024')),
        ],
        '4ba54e3f': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'SigridMajesticWavechaser.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1f036c21', 'SigridMajesticWavechaser.RotorA.MaterialMap.2048')),
        ],

        # ==================== RotorBearing Component ====================
        'b4f608f5': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorBearing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'efe37d81': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorBearing Draw VB Hash',)),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        '513d615a': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorBearing Position VB Hash',)),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        'f8153d33': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorBearing Texcoord VB Hash',)),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        '09f65e9d': [
            (log,                             ('3.1: SigridMajesticWavechaser RotorBearing Blend VB Hash',)),
            (add_section_if_missing,          ('b4f608f5', 'SigridMajesticWavechaser.RotorBearing.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'SigridMajesticWavechaser',
    'game_versions': ['3.1', '3.2'],
}
