"""
Sigrid Character Hash Commands
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
    Returns Sigrid's hash commands dictionary.

    All command classes are passed as parameters to avoid circular imports.
    """
    return {

        # ==================== Hair Component ====================
        '84618ee0': [
            (log,                             ('3.1: Sigrid Hair IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '840c1713': [
            (log,                             ('3.1: Sigrid Hair Draw VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
        ],
        '53d5d966': [
            (log,                             ('3.1: Sigrid Hair Position VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
        ],
        '6b1c911c': [
            (log,                             ('3.1: Sigrid Hair Texcoord VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
        ],
        '380ee24b': [
            (log,                             ('3.1: Sigrid Hair Blend VB Hash',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
        ],
        '0c4bea0f': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairbandA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.LegA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.TailA.Diffuse.1024')),
            (update_hash,                     ('f2896dcc',)),
        ],
        'f2896dcc': [
            (log,                             ('3.2: Sigrid HairA, HairpinA, HairbandA, LegA and TailA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairpinA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.HairbandA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.LegA.Diffuse.1024')),
            (multiply_section_if_missing,     (('cb3525dc', '66dbe05f'), 'Sigrid.TailA.Diffuse.1024')),
        ],
        '66dbe05f': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairbandA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.LegA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.TailA.Diffuse.2048')),
            (update_hash,                     ('cb3525dc',)),
        ],
        'cb3525dc': [
            (log,                             ('3.2: Sigrid HairA, HairpinA, HairbandA, LegA and TailA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairpinA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.HairbandA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.LegA.Diffuse.2048')),
            (multiply_section_if_missing,     (('f2896dcc', '0c4bea0f'), 'Sigrid.TailA.Diffuse.2048')),
        ],
        'ebac056e': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, BodyA, LegA, TailA, SpearA and RotorBearingA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.HairA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.HairpinA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.HairbandA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.BodyA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.LegA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.TailA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.SpearA.NormalMap.1024')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.RotorBearingA.NormalMap.1024')),
        ],
        '798adba3': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, BodyA, LegA, TailA, SpearA and RotorBearingA NormalMap 1024p Hash, also RotorA NormalMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.HairA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.HairpinA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.HairbandA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.BodyA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.LegA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.TailA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.SpearA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ebac056e', 'Sigrid.RotorBearingA.NormalMap.2048')),
            (multiply_section_if_missing,     ('ffdc1ea7', 'Sigrid.RotorA.NormalMap.1024')),
        ],
        'da6a6f0b': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairbandA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.LegA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.TailA.LightMap.1024')),
            (update_hash,                     ('16d72691',)),
        ],
        '16d72691': [
            (log,                             ('3.2: Sigrid HairA, HairpinA, HairbandA, LegA and TailA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairpinA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.HairbandA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.LegA.LightMap.1024')),
            (multiply_section_if_missing,     (('d7d68132', 'bc582555'), 'Sigrid.TailA.LightMap.1024')),
        ],
        'bc582555': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairbandA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.LegA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.TailA.LightMap.2048')),
            (update_hash,                     ('d7d68132',)),
        ],
        'd7d68132': [
            (log,                             ('3.2: Sigrid HairA, HairpinA, HairbandA, LegA and TailA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairpinA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.HairbandA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.LegA.LightMap.2048')),
            (multiply_section_if_missing,     (('16d72691', 'da6a6f0b'), 'Sigrid.TailA.LightMap.2048')),
        ],
        'f5da0fcd': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('d055f8e9', 'Sigrid.HairA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'Sigrid.HairpinA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'Sigrid.HairbandA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'Sigrid.LegA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('d055f8e9', 'Sigrid.TailA.MaterialMap.1024')),
        ],
        'd055f8e9': [
            (log,                             ('3.1: Sigrid HairA, HairpinA, HairbandA, LegA and TailA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('84618ee0', 'Sigrid.Hair.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f5da0fcd', 'Sigrid.HairA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'Sigrid.HairpinA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'Sigrid.HairbandA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'Sigrid.LegA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('f5da0fcd', 'Sigrid.TailA.MaterialMap.2048')),
        ],

        # ==================== Hair Shadow Component ====================
        '81e925ed': [
            (log,                             ('3.1: Sigrid Hair Shadow IB Hash',)),
            (add_ib_check_if_missing,),
        ],

        # ==================== Hairpin Component ====================
        'b51bdd59': [
            (log,                             ('3.1: Sigrid Hairpin IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '6a8ea608': [
            (log,                             ('3.1: Sigrid Hairpin Draw VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '63981c38': [
            (log,                             ('3.1: Sigrid Hairpin Position VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '937473ae': [
            (log,                             ('3.1: Sigrid Hairpin Texcoord VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
        ],
        '68bfe8f5': [
            (log,                             ('3.1: Sigrid Hairpin Blend VB Hash',)),
            (add_section_if_missing,          ('b51bdd59', 'Sigrid.Hairpin.IB', 'match_priority = 0\n')),
        ],

        # ==================== Hairband Component ====================
        '64d7d56f': [
            (log,                             ('3.1: Sigrid Hairband IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '62a109a8': [
            (log,                             ('3.1: Sigrid Hairband Draw VB Hash',)),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
        ],
        '3412aeb6': [
            (log,                             ('3.1: Sigrid Hairband Position VB Hash',)),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
        ],
        '951e896a': [
            (log,                             ('3.1: Sigrid Hairband Texcoord VB Hash',)),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
        ],
        '228eb9d6': [
            (log,                             ('3.1: Sigrid Hairband Blend VB Hash',)),
            (add_section_if_missing,          ('64d7d56f', 'Sigrid.Hairband.IB', 'match_priority = 0\n')),
        ],

        # ==================== Body Component ====================
        'a23aa8a3': [
            (log,                             ('3.1: Sigrid Body IB Hash',)),
            (add_ib_check_if_missing,),
            (update_hash,                     ('38daef11',)),
        ],
        '38daef11': [
            (log,                             ('3.1: Sigrid Body IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '01b35c45': [
            (log,                             ('3.1: Sigrid Body Draw Hash',)),
            (add_section_if_missing,          ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('d0bf0e87',)),
        ],
        'd0bf0e87': [
            (log,                             ('3.1: Sigrid Body Draw VB Hash',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        ],
        '08c15b45': [
            (log,                             ('3.1: Sigrid Body Position Hash',)),
            (add_section_if_missing,          ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('e2a28287',)),
        ],
        'e2a28287': [
            (log,                             ('3.1: Sigrid Body Position VB Hash',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        ],
        'f6474154': [
            (log,                             ('3.1: Sigrid Body Texcoord Hash',)),
            (add_section_if_missing,          ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('08ddaed3',)),
        ],
        '08ddaed3': [
            (log,                             ('3.1: Sigrid Body Texcoord VB Hash',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        ],
        '8c0622d7': [
            (log,                             ('3.1: Sigrid Body Blend Hash',)),
            (add_section_if_missing,          ('a23aa8a3', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (update_hash,                     ('018ea72c',)),
        ],
        '018ea72c': [
            (log,                             ('3.1: Sigrid Body Blend VB Hash',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
        ],
        '5b733af8': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('037f456b', 'Sigrid.BodyA.Diffuse.1024')),
            (multiply_section_if_missing,     ('037f456b', 'Sigrid.RotorBearingA.Diffuse.1024')),
        ],
        '037f456b': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('5b733af8', 'Sigrid.BodyA.Diffuse.2048')),
            (multiply_section_if_missing,     ('5b733af8', 'Sigrid.RotorBearingA.Diffuse.2048')),
        ],
        '13775170': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA LightMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a73e5eea', 'Sigrid.BodyA.LightMap.1024')),
            (multiply_section_if_missing,     ('a73e5eea', 'Sigrid.RotorBearingA.LightMap.1024')),
        ],
        'a73e5eea': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA LightMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('13775170', 'Sigrid.BodyA.LightMap.2048')),
            (multiply_section_if_missing,     ('13775170', 'Sigrid.RotorBearingA.LightMap.2048')),
        ],
        'af950416': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA MaterialMap 2048p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('764b45ad', 'Sigrid.BodyA.MaterialMap.1024')),
            (multiply_section_if_missing,     ('764b45ad', 'Sigrid.RotorBearingA.MaterialMap.1024')),
        ],
        '764b45ad': [
            (log,                             ('3.1: Sigrid BodyA and RotorBearingA MaterialMap 1024p Hash (shared)',)),
            (add_section_if_missing,          ('38daef11', 'Sigrid.Body.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('af950416', 'Sigrid.BodyA.MaterialMap.2048')),
            (multiply_section_if_missing,     ('af950416', 'Sigrid.RotorBearingA.MaterialMap.2048')),
        ],

        # ==================== Leg Component ====================
        'b20f90ea': [
            (log,                             ('3.1: Sigrid Leg IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'dd9c8d5e': [
            (log,                             ('3.1: Sigrid Leg Draw VB Hash',)),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
        ],
        '122883aa': [
            (log,                             ('3.1: Sigrid Leg Position VB Hash',)),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
        ],
        '5c0fefda': [
            (log,                             ('3.1: Sigrid Leg Texcoord VB Hash',)),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
        ],
        'bf543990': [
            (log,                             ('3.1: Sigrid Leg Blend VB Hash',)),
            (add_section_if_missing,          ('b20f90ea', 'Sigrid.Leg.IB', 'match_priority = 0\n')),
        ],

        # ==================== Tail Component ====================
        'b30db54e': [
            (log,                             ('3.1: Sigrid Tail IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'cb72b377': [
            (log,                             ('3.1: Sigrid Tail Draw VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
        ],
        'b3aeb830': [
            (log,                             ('3.1: Sigrid Tail Position VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
        ],
        '84ef2fb1': [
            (log,                             ('3.1: Sigrid Tail Texcoord VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
        ],
        '710b43f7': [
            (log,                             ('3.1: Sigrid Tail Blend VB Hash',)),
            (add_section_if_missing,          ('b30db54e', 'Sigrid.Tail.IB', 'match_priority = 0\n')),
        ],

        # ==================== Eyebrow Component ====================
        '454ff522': [
            (log,                             ('3.1: Sigrid Eyebrow IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '18b20f06': [
            (log,                             ('3.1: Sigrid EyebrowA and FaceA Diffuse 2048p Hash (shared)',)),
            (add_section_if_missing,          ('454ff522', 'Sigrid.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f178a6f2', 'Sigrid.EyebrowA.Diffuse.1024')),
            (multiply_section_if_missing,     ('f178a6f2', 'Sigrid.FaceA.Diffuse.1024')),
        ],
        'f178a6f2': [
            (log,                             ('3.1: Sigrid EyebrowA and FaceA Diffuse 1024p Hash (shared)',)),
            (add_section_if_missing,          ('454ff522', 'Sigrid.Eyebrow.IB', 'match_priority = 0\n')),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('18b20f06', 'Sigrid.EyebrowA.Diffuse.2048')),
            (multiply_section_if_missing,     ('18b20f06', 'Sigrid.FaceA.Diffuse.2048')),
        ],

        # ==================== Face Component ====================
        '48625d6d': [
            (log,                             ('3.1: Sigrid Face IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '9b76d1d7': [
            (log,                             ('3.1: Sigrid Face Draw VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
        ],
        'a1644290': [
            (log,                             ('3.1: Sigrid Face Position VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
        ],
        'c90ff663': [
            (log,                             ('3.1: Sigrid Face Texcoord VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
        ],
        'e768b061': [
            (log,                             ('3.1: Sigrid Face Blend VB Hash',)),
            (add_section_if_missing,          ('48625d6d', 'Sigrid.Face.IB', 'match_priority = 0\n')),
        ],

        # ==================== Spear Component ====================
        '19086112': [
            (log,                             ('3.1: Sigrid Spear IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '0351cfca': [
            (log,                             ('3.1: Sigrid Spear Draw VB Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
        ],
        '72a71f98': [
            (log,                             ('3.1: Sigrid Spear Position VB Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
        ],
        '9365ad01': [
            (log,                             ('3.1: Sigrid Spear Texcoord VB Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
        ],
        '9c60a66e': [
            (log,                             ('3.1: Sigrid Spear Blend VB Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
        ],
        'f827c5f5': [
            (log,                             ('3.1: Sigrid SpearA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('2df6caf1', 'Sigrid.SpearA.Diffuse.1024')),
        ],
        '2df6caf1': [
            (log,                             ('3.1: Sigrid SpearA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f827c5f5', 'Sigrid.SpearA.Diffuse.2048')),
        ],
        '494a83dc': [
            (log,                             ('3.1: Sigrid SpearA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('b85d4c23', 'Sigrid.SpearA.LightMap.1024')),
        ],
        'b85d4c23': [
            (log,                             ('3.1: Sigrid SpearA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('494a83dc', 'Sigrid.SpearA.LightMap.2048')),
        ],
        'f30e1ce6': [
            (log,                             ('3.1: Sigrid SpearA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('648d17e4', 'Sigrid.SpearA.MaterialMap.1024')),
        ],
        '648d17e4': [
            (log,                             ('3.1: Sigrid SpearA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('19086112', 'Sigrid.Spear.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('f30e1ce6', 'Sigrid.SpearA.MaterialMap.2048')),
        ],

        # ==================== Rotor Component ====================
        'd892c658': [
            (log,                             ('3.1: Sigrid Rotor IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        '914dcde9': [
            (log,                             ('3.1: Sigrid Rotor Draw VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
        ],
        'fe91db45': [
            (log,                             ('3.1: Sigrid Rotor Position VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
        ],
        'cd92341a': [
            (log,                             ('3.1: Sigrid Rotor Texcoord VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
        ],
        '0bacf856': [
            (log,                             ('3.1: Sigrid Rotor Blend VB Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
        ],
        '4fa99352': [
            (log,                             ('3.1: Sigrid RotorA Diffuse 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('a58912ea', 'Sigrid.RotorA.Diffuse.1024')),
        ],
        'a58912ea': [
            (log,                             ('3.1: Sigrid RotorA Diffuse 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4fa99352', 'Sigrid.RotorA.Diffuse.2048')),
        ],
        'ffdc1ea7': [
            (log,                             ('3.1: Sigrid RotorA NormalMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('798adba3', 'Sigrid.RotorA.NormalMap.2048')),
        ],
        '980d9016': [
            (log,                             ('3.1: Sigrid RotorA LightMap 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('01f5701a', 'Sigrid.RotorA.LightMap.1024')),
        ],
        '01f5701a': [
            (log,                             ('3.1: Sigrid RotorA LightMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('980d9016', 'Sigrid.RotorA.LightMap.2048')),
        ],
        '1f036c21': [
            (log,                             ('3.1: Sigrid RotorA MaterialMap 2048p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('4ba54e3f', 'Sigrid.RotorA.MaterialMap.1024')),
        ],
        '4ba54e3f': [
            (log,                             ('3.1: Sigrid RotorA MaterialMap 1024p Hash',)),
            (add_section_if_missing,          ('d892c658', 'Sigrid.Rotor.IB', 'match_priority = 0\n')),
            (multiply_section_if_missing,     ('1f036c21', 'Sigrid.RotorA.MaterialMap.2048')),
        ],

        # ==================== RotorBearing Component ====================
        'add6ff13': [
            (log,                             ('3.1: Sigrid RotorBearing IB Hash',)),
            (add_ib_check_if_missing,),
        ],
        'fab82e2f': [
            (log,                             ('3.1: Sigrid RotorBearing Draw VB Hash',)),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        '3b09c896': [
            (log,                             ('3.1: Sigrid RotorBearing Position VB Hash',)),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        'ece3a3d2': [
            (log,                             ('3.1: Sigrid RotorBearing Texcoord VB Hash',)),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
        ],
        '098fd9e8': [
            (log,                             ('3.1: Sigrid RotorBearing Blend VB Hash',)),
            (add_section_if_missing,          ('add6ff13', 'Sigrid.RotorBearing.IB', 'match_priority = 0\n')),
        ],
    }


# Character metadata
CHARACTER_INFO = {
    'name': 'Sigrid',
    'game_versions': ['3.1', '3.2'],
}
