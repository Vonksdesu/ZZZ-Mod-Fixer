#!/usr/bin/env python3
"""
check-database-sync.py - ZZZ Mod Fixer Database Synchronization Analyzer

Enhanced multi-signal detection (layers complement, not replace each other):

1. HASH-FIRST SCORING   : IB hashes (highest weight), VB hashes (medium), texture
                          hashes (low, globally-shared ones ignored) owned by each
                          module. Unique IB ownership gets a bonus.
2. COMPONENT FINGERPRINT: compares the JSON's component_name list against the
                          section titles inside the Python modules (e.g.
                          'Sunna.Hair.IB'), bridging characters whose names differ
                          completely (Chinatsu <-> Sunna).
3. NAME / ALIAS         : exact clean-name match (100), alias match from
                          CHARACTER_INFO['aliases'] or sync-aliases.json (95),
                          substring (50), common prefix (30).
4. TRANSITION LINKS     : a JSON hash that is a `new` target in the .txt change
                          logs links the JSON to the module that still owns the
                          `old` hash (hash-update scenario).
5. GLOBAL 1-to-1 ASSIGN : every JSON is assigned to at most one module and every
                          module to at most one JSON; strongest evidence wins.
                          This prevents an empty/new skin module from being
                          shadowed by its base character module.
6. LEFTOVER PAIRING     : unmatched JSONs are paired with unmatched modules by
                          order (database file order vs CHARACTERS order) and
                          flagged for manual VERIFY.
7. ORPHAN REPORT        : modules registered in __init__.py but matched by no
                          JSON in the current database.

PREPARATION FOR FUTURE ZZZ VERSIONS (totally different names, e.g. CN/JP name vs
Global name for a NEW character):
  * Edit sync-aliases.json and add a mapping, e.g. {"chinatsu": ["sunna"]}
  * or, when creating a new empty module stub, set CHARACTER_INFO['aliases']
    inside the file, e.g. CHARACTER_INFO = {'name': 'Sunna', 'aliases': ['Chinatsu', '千夏']}
"""

import os
import re
import json
import importlib
import sys
from pathlib import Path

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')

# DATABASE VERSION CONFIGURATION (Change this for future versions)
DATABASE_VERSION = "3.1"
RESOLUTION = "2048p"  # Options: "2048p" or "1024p"

# Alias memory file (see module docstring above)
ALIAS_FILE = Path(__file__).resolve().parent / 'sync-aliases.json'

# Minimum total score required to auto-assign a JSON to a module.
# Scores below this fall into the leftover pool (manual verify).
ASSIGN_MIN_SCORE = 50.0

# ANSI color codes for terminal output
class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

# Component keywords used for structural fingerprint matching
COMPONENT_KEYWORDS = [
    'hair', 'body', 'leg', 'legs', 'face', 'head', 'weapon', 'fan', 'eyebrows',
    'sensor', 'backpack', 'scabbard', 'blade', 'handguard', 'sword', 'shadow',
    'bow', 'ribbon', 'earring', 'skirt', 'jacket', 'glove', 'shoe', 'footwear',
    'necklace', 'tail', 'cape', 'scarf', 'crown', 'wings', 'belly', 'navel',
]
# The reference database sometimes labels a component differently than the
# Python modules do (e.g. JSON "Bow" == Python "Head").
COMPONENT_SYNONYMS = {
    'bow': 'head',
    'swordsheath': 'sword',
    'swordhandle': 'sword',
    'swordsoul': 'sword',
}

# Words that appear in section titles but are not components
COMPONENT_STRIP_WORDS = {
    'ib', 'vb', 'diffuse', 'lightmap', 'materialmap', 'normalmap', 'draw',
    'position', 'texcoord', 'blend', 'vertexlimit', 'shared', 'v2', 'v3',
    '2', '3', '2048', '1024', '2048p', '1024p',
}


def clean_name(name):
    name_no_ext = Path(name).stem
    # Extract only letters and digits (removing Chinese characters, spaces, and punctuation)
    latin_and_digits = "".join(re.findall(r'[a-zA-Z0-9]+', name_no_ext))
    return latin_and_digits.lower()


# Substrings that mark a line as technical noise instead of a character section
# header in the .txt change logs (e.g. 'IB:', 'texcoord_vb:', '版本更新说明', ...).
NON_CHAR_SUBSTRINGS = (
    "铃泳装/皮肤", "身体", "【】", "【", "】", "以下", "新增", "头发", "版本", "作者", "声明", "网址", "说明", "热更新",
    "模型结构", "更新这些", "踩蘑菇", "如果有错误", "普罗米娅", "NormalMap", "Diffuse",
    "LightMap", "MaterialMap", "Position", "Texcoord", "Blend", "blend_vb",
    "draw_vb", "position_vb", "texcoord_vb", "object_indexes", "VertexLimit",
    "VertexLimitRaise", "MatchFirstIndex", "IB", "VB", "===", "---", "http",
    "Alice", "AliceSkin", "Anby", "Anton", "Arie", "ArieAgent",
    "ArieAgentSkin", "ArieSkin", "AstraSkin", "AstraYao", "Banyue",
    "Belle", "BelleSchoolUniform", "BelleSkin", "BellesWimwear", "Ben",
    "Billy", "Burnice", "Caesar", "Chinatsu", "ChinatsuSkin", "Cissia",
    "Corin", "Dialyn", "Ellen", "EllenSkin", "Evelyn", "Grace",
    "Harumasa", "Hugo", "Jane", "JaneSkin", "JuFufu", "Koleda",
    "Lighter", "Lucia", "Lucy", "LucySkin", "Lycaon", "Manato",
    "Miyabi", "MiyabiSkin", "Nanyu", "NanyuSkin", "Nekomata", "Nicole",
    "NicoleSkin", "Norma", "Orphie", "PanYinhu", "PanYinhuSkin", "Piper",
    "Promeia", "Pulchra", "Pyrois", "Qingyi", "Remielle",
    "RemielleSkinBlack", "RemielleSkinWhite", "Rina", "Seed", "seed", "Seth",
    "Sigrid", "SigridSkin", "Soldier0", "Soldier11", "Soukaku",
    "StarlightBilly", "Trigger", "Velina", "VelinaSkin", "Vivian",
    "VivianSkin", "Wise", "WiseSchoolUniform", "WiseSkin", "Wiseswimwear",
    "Yanagi", "YeShunguang", "YeShunguangSkin", "YeShunguangWrite",
    "YiXuan", "YiXuanSkin", "Yidhair", "Yuzuha", "YuzuhaSkin",
    "Zhao", "ZhuYuan",
)
CJK_RE = re.compile(r'[\u3400-\u4dbf\u4e00-\u9fff]')


def is_character_header(token):
    """True if a log line's first token looks like a character section header."""
    if not token:
        return False
    if any(s in token for s in NON_CHAR_SUBSTRINGS):
        return False
    if token.startswith('\u3010') or CJK_RE.search(token):
        return True
    return False


def hint_matches_module(char_hint, mod_name):
    """
    Does a log section header refer to this module?
    True when the module's clean name contains the header's clean name (or
    vice versa), or when a CamelCase token of the header (e.g. 'WiseSwimwear'
    inside a multi-character group header) matches the module by containment.
    """
    hint_clean = clean_name(char_hint)
    if not hint_clean:
        return None
    mod_clean = clean_name(mod_name)
    if not mod_clean:
        return False
    if hint_clean in mod_clean or mod_clean in hint_clean:
        return True
    tokens = {t.lower() for t in re.findall(r'[A-Z][a-z]+|\d+', char_hint)}
    tokens = {t for t in tokens if len(t) >= 2 and t in hint_clean}
    if not tokens:
        return False
    return any(t in mod_clean or mod_clean in t for t in tokens)


def token_to_components(token):
    """Turn a raw token (e.g. 'HairA', 'WeaponMiyabi', 'Weapon, Fan') into a set of normalized components."""
    t = token.lower()
    for w in ('2048p', '1024p', '2048', '1024', '.dds'):
        t = t.replace(w, '')
    parts = re.split(r'[.,\s\-/\\]+', t)
    out = set()
    for p in parts:
        if not p or p in COMPONENT_STRIP_WORDS:
            continue
        found = False
        for kw in COMPONENT_KEYWORDS:
            if kw in p:
                out.add(COMPONENT_SYNONYMS.get(kw, kw))
                found = True
        if not found and len(p) >= 3:
            out.add(p)
    return out


def extract_module_components(py_commands, module_name):
    """Extract the set of body-part components referenced by a module's section titles."""
    comps = set()
    mc = clean_name(module_name)
    for commands in py_commands.values():
        for cmd in commands:
            if not isinstance(cmd, tuple) or len(cmd) < 2:
                continue
            fname = getattr(cmd[0], '__name__', '')
            if fname not in ('add_section_if_missing', 'multiply_section_if_missing'):
                continue
            args = cmd[1]
            if not isinstance(args, tuple) or len(args) < 2 or not isinstance(args[1], str):
                continue
            title = args[1]
            parts = title.split('.')
            if parts and mc and clean_name(parts[0]) == mc:
                parts = parts[1:]
            for part in parts:
                comps.update(token_to_components(part))
    return comps


def components_similarity(json_components, module_components):
    """Fraction of the JSON's components that the module also describes (0.0 - 1.0)."""
    if not json_components:
        return 0.0
    jc = set()
    for c in json_components:
        jc.update(token_to_components(str(c)))
    mc = set()
    for c in module_components:
        mc.update(token_to_components(str(c)))
    if not jc:
        return 0.0
    return len(jc & mc) / len(jc)


def parse_json_structure(json_path):
    """
    Extract from a database .json:
      ib_hashes   : hashes of key 'ib'
      vb_hashes   : hashes of keys draw_vb/position_vb/blend_vb/texcoord_vb
      other_hashes: all other 8-hex hashes (textures, etc.)
      components  : all 'component_name' values
    """
    ib_hashes = set()
    vb_hashes = set()
    other_hashes = set()
    components = set()
    hex_pattern = re.compile(r'^[a-f0-9]{8}$', re.IGNORECASE)
    vb_keys = {'draw_vb', 'position_vb', 'blend_vb', 'texcoord_vb'}

    def walk(d):
        if isinstance(d, dict):
            for k, v in d.items():
                kl = k.lower()
                if kl == 'ib' and isinstance(v, str) and hex_pattern.match(v):
                    ib_hashes.add(v.lower())
                elif kl in vb_keys and isinstance(v, str) and hex_pattern.match(v):
                    vb_hashes.add(v.lower())
                elif kl == 'component_name' and isinstance(v, str):
                    components.add(v)
                elif isinstance(v, str) and hex_pattern.match(v):
                    other_hashes.add(v.lower())
                else:
                    walk(v)
        elif isinstance(d, list):
            for item in d:
                if isinstance(item, str) and hex_pattern.match(item):
                    other_hashes.add(item.lower())
                else:
                    walk(item)

    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            walk(data)
    except Exception as e:
        print(f"{Colors.RED}Failed to read {json_path}: {e}{Colors.RESET}")
    return ib_hashes, vb_hashes, other_hashes, components


def parse_txt_transitions(txt_path):
    transitions = []
    try:
        content = txt_path.read_text(encoding='utf-8')
    except Exception:
        try:
            content = txt_path.read_text(encoding='gb2312')
        except Exception:
            return []

    lines = content.splitlines()
    current_char = ""
    for line in lines:
        char_match = re.match(r'^\s*([^,:\s]+)', line)
        if char_match:
            potential_char = char_match.group(1)
            if is_character_header(potential_char):
                current_char = potential_char

        matches = re.findall(r'([a-f0-9]{8})\s*->\s*([a-f0-9]{8})', line, re.IGNORECASE)
        for old_h, new_h in matches:
            transitions.append({
                'char_hint': current_char,
                'old': old_h.lower(),
                'new': new_h.lower(),
                'line': line.strip()
            })
    return transitions


def parse_all_txt_transitions(json_folder, hash_to_module):
    """
    Pre-parse all .txt change logs once.
    Returns:
      transition_targets : set of all `new` hashes
      transition_new_owners : new_hash -> set of modules owning the `old` hash
      all_transitions   : [(txt_name, [transitions...]), ...] for the report section
    """
    transition_targets = set()
    transition_new_owners = {}
    all_transitions = []
    for txt_file in sorted(json_folder.glob('*.txt')):
        if "说明" in txt_file.name or "readme" in txt_file.name.lower():
            continue
        transitions = parse_txt_transitions(txt_file)
        if not transitions:
            continue
        seen = set()
        unique = []
        for trans in transitions:
            key = (trans['old'], trans['new'])
            if key in seen:
                continue
            seen.add(key)
            unique.append(trans)
        all_transitions.append((txt_file.name, transitions, unique))
        for trans in unique:
            new_h = trans['new']
            transition_targets.add(new_h)
            owners = set()
            for mod in hash_to_module.get(trans['old'], ()):
                owners.add(mod)
            transition_new_owners.setdefault(new_h, set()).update(owners)
    return transition_targets, transition_new_owners, all_transitions


def load_sync_aliases():
    """Load user-maintained alias mappings from sync-aliases.json."""
    data = {'aliases': {}}
    if not ALIAS_FILE.exists():
        return data
    try:
        raw = json.loads(ALIAS_FILE.read_text(encoding='utf-8'))
        if not isinstance(raw, dict):
            return data
        aliases = raw.get('aliases', {})
        if isinstance(aliases, dict):
            for k, v in aliases.items():
                if isinstance(v, list):
                    data['aliases'][str(k)] = [str(x) for x in v]
                else:
                    data['aliases'][str(k)] = [str(v)]
    except Exception as e:
        print(f"{Colors.YELLOW}Warning: failed to read {ALIAS_FILE.name}: {e}{Colors.RESET}")
    return data


def name_score(json_filename, mod_name, module_to_char_info, aliases_data):
    """
    Name/alias based score (0..100):
      100 = module clean name equals json clean name
       95 = alias match (CHARACTER_INFO['aliases'] or sync-aliases.json)
       50 = one clean name is substring of the other
       30 = common prefix of >= 3 chars
    """
    c1 = clean_name(json_filename)
    if not c1:
        return 0

    info = module_to_char_info.get(mod_name, {})
    candidates = [mod_name]
    for k in ('name', 'display_name'):
        v = info.get(k)
        if isinstance(v, str) and v:
            candidates.append(v)

    best = 0
    for cand in candidates:
        c2 = clean_name(cand)
        if not c2:
            continue
        if c1 == c2:
            best = max(best, 100)
        elif c1 in c2 or c2 in c1:
            best = max(best, 50)
        else:
            pref = 0
            for i in range(min(len(c1), len(c2))):
                if c1[i] == c2[i]:
                    pref += 1
                else:
                    break
            if pref >= min(3, min(len(c1), len(c2))):
                best = max(best, 30)

    aliases = info.get('aliases', [])
    if isinstance(aliases, str):
        aliases = [aliases]
    elif not isinstance(aliases, list):
        aliases = []
    for alias in aliases:
        ca = clean_name(alias)
        if not ca:
            # raw (e.g. Chinese) alias found verbatim in the filename
            if alias and alias in json_filename:
                best = max(best, 95)
            continue
        if ca == c1:
            best = max(best, 95)
        elif ca in c1 or c1 in ca:
            best = max(best, 60)

    # sync-aliases.json entries
    mc = clean_name(mod_name)
    for key, vals in aliases_data.get('aliases', {}).items():
        if key == c1 or (key and key in json_filename):
            if mc in {clean_name(v) for v in vals}:
                best = max(best, 95)

    return best


def score_module(json_filename, json_ib, json_vb, json_tex, json_comps,
                 mod_name, mod_hashes, mod_comps, hash_to_module,
                 module_to_char_info, aliases_data, transition_new_owners):
    """Compute the total match score between a JSON and one module."""
    score = 0.0
    tags = []

    ib_hits = json_ib & mod_hashes
    score += 10.0 * len(ib_hits)
    unique_ib = {h for h in ib_hits if len(hash_to_module.get(h, ())) == 1}
    score += 5.0 * len(unique_ib)
    if ib_hits or unique_ib:
        tags.append(f'IB:{len(ib_hits)}(+{len(unique_ib)}uniq)')

    vb_hits = json_vb & mod_hashes
    score += 4.0 * len(vb_hits)
    if vb_hits:
        tags.append(f'VB:{len(vb_hits)}')

    # Texture hashes owned by many modules (shared NormalMap etc.) add noise
    tex_hits = {h for h in (json_tex & mod_hashes) if len(hash_to_module.get(h, ())) <= 3}
    score += 1.0 * len(tex_hits)
    if tex_hits:
        tags.append(f'TEX:{len(tex_hits)}')

    cs = components_similarity(json_comps, mod_comps)
    score += 20.0 * cs
    if cs > 0:
        tags.append(f'COMP:{cs:.0%}')

    ns = name_score(json_filename, mod_name, module_to_char_info, aliases_data)
    score += ns
    if ns >= 60:
        tags.append(f'NAME:{ns:.0f}')

    links = 0
    for h in (json_ib | json_vb) & set(transition_new_owners.keys()):
        if mod_name in transition_new_owners.get(h, ()):
            links += 1
    score += 8.0 * links
    if links:
        tags.append(f'LINK:{links}')

    return round(score, 2), tags


def build_py_hash_index(py_data_path, mock_command_classes):
    init_file = py_data_path / '__init__.py'
    if not init_file.exists():
        return {}, {}, {}, {}, []

    try:
        content = init_file.read_text(encoding='utf-8')
    except Exception:
        content = init_file.read_text(encoding='gb2312')

    characters_match = re.search(r'CHARACTERS\s*=\s*\[(.*?)\]', content, re.DOTALL)
    if not characters_match:
        return {}, {}, {}, {}, []

    registered_chars = re.findall(r"['\"](.*?)['\"]", characters_match.group(1))

    hash_to_module = {}
    module_to_hashes = {}
    module_to_char_info = {}
    module_to_components = {}
    module_order = []

    sys.path.insert(0, str(py_data_path.parent))
    try:
        for character_name in registered_chars:
            module_order.append(character_name)
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                py_commands = module.get_hash_commands(**mock_command_classes)
                py_hashes = {h.lower() for h in py_commands.keys()}

                module_to_hashes[character_name] = py_hashes
                for h in py_hashes:
                    if h not in hash_to_module:
                        hash_to_module[h] = []
                    hash_to_module[h].append(character_name)

                module_to_components[character_name] = extract_module_components(py_commands, character_name)

                char_info = getattr(module, 'CHARACTER_INFO', None)
                if char_info and isinstance(char_info, dict):
                    module_to_char_info[character_name] = char_info
                else:
                    module_to_char_info[character_name] = {}
            except Exception:
                module_to_hashes[character_name] = set()
                module_to_char_info[character_name] = {}
                module_to_components[character_name] = set()
                continue
    finally:
        sys.path.remove(str(py_data_path.parent))

    return hash_to_module, module_to_hashes, module_to_char_info, module_to_components, module_order


def check_sync():
    base_path = Path('.')
    py_data_path = base_path / 'Assets' / 'PlayerCharacterPYData'
    json_folder = base_path / 'ZZZHashIDCharactersDatabase' / RESOLUTION / f'Database_{DATABASE_VERSION}'

    if not json_folder.exists():
        print(f"{Colors.RED}Error: Database folder not found at: {json_folder.resolve()}{Colors.RESET}")
        print(f"{Colors.YELLOW}Make sure the folder structure is: ZZZHashIDCharactersDatabase/{RESOLUTION}/Database_{DATABASE_VERSION}/{Colors.RESET}")
        return

    def log(*args, **kwargs): pass
    def update_hash(*args, **kwargs): pass
    def comment_sections(*args, **kwargs): pass
    def comment_commandlists(*args, **kwargs): pass
    def remove_section(*args, **kwargs): pass
    def remove_indexed_sections(*args, **kwargs): pass
    def capture_section(*args, **kwargs): pass
    def create_new_section(*args, **kwargs): pass
    def transfer_indexed_sections(*args, **kwargs): pass
    def multiply_section_if_missing(*args, **kwargs): pass
    def add_ib_check_if_missing(*args, **kwargs): pass
    def add_section_if_missing(*args, **kwargs): pass
    def zzz_13_remap_texcoord(*args, **kwargs): pass
    def zzz_12_shrink_texcoord_color(*args, **kwargs): pass
    def update_buffer_blend_indices(*args, **kwargs): pass

    command_classes = {
        'log': log,
        'update_hash': update_hash,
        'comment_sections': comment_sections,
        'comment_commandlists': comment_commandlists,
        'remove_section': remove_section,
        'remove_indexed_sections': remove_indexed_sections,
        'capture_section': capture_section,
        'create_new_section': create_new_section,
        'transfer_indexed_sections': transfer_indexed_sections,
        'multiply_section_if_missing': multiply_section_if_missing,
        'add_ib_check_if_missing': add_ib_check_if_missing,
        'add_section_if_missing': add_section_if_missing,
        'zzz_13_remap_texcoord': zzz_13_remap_texcoord,
        'zzz_12_shrink_texcoord_color': zzz_12_shrink_texcoord_color,
        'update_buffer_blend_indices': update_buffer_blend_indices
    }

    print(f"{Colors.BOLD}{Colors.CYAN}============================================================================================{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Database Synchronization Analysis {DATABASE_VERSION} with {RESOLUTION} Resolution (MULTI-SIGNAL){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}============================================================================================{Colors.RESET}")

    hash_to_module, module_to_hashes, module_to_char_info, module_to_components, module_order = build_py_hash_index(py_data_path, command_classes)
    aliases_data = load_sync_aliases()
    transition_targets, transition_new_owners, all_transitions = parse_all_txt_transitions(json_folder, hash_to_module)

    # ---------------------------------------------------------------
    # Parse all JSON database files
    # ---------------------------------------------------------------
    json_entries = []
    for json_file in sorted(json_folder.glob('*.json')):
        ib_hashes, vb_hashes, tex_hashes, components = parse_json_structure(json_file)
        json_entries.append({
            'file': json_file,
            'name': json_file.name,
            'ib': ib_hashes,
            'vb': vb_hashes,
            'tex': tex_hashes,
            'comps': components,
        })

    active_hashes = set()
    for entry in json_entries:
        active_hashes.update(entry['ib'])
        active_hashes.update(entry['vb'])
        active_hashes.update(entry['tex'])

    # Modules are combined across both resolutions (2048p + 1024p in one file).
    # A hash that is still active in the SIBLING resolution must not require
    # update_hash: updating it would corrupt the mods for the other resolution.
    sibling_res = '1024p' if RESOLUTION == '2048p' else '2048p'
    sibling_folder = base_path / 'ZZZHashIDCharactersDatabase' / sibling_res / f'Database_{DATABASE_VERSION}'
    other_res_hashes = set()
    if sibling_folder.is_dir():
        for json_file in sibling_folder.glob('*.json'):
            ib, vb, tex, _ = parse_json_structure(json_file)
            other_res_hashes.update(ib)
            other_res_hashes.update(vb)
            other_res_hashes.update(tex)

    # ---------------------------------------------------------------
    # Global scoring + 1-to-1 assignment (strongest evidence wins)
    # ---------------------------------------------------------------
    candidates = []
    for idx, entry in enumerate(json_entries):
        for mod_name in module_order:
            score, tags = score_module(
                entry['name'], entry['ib'], entry['vb'], entry['tex'], entry['comps'],
                mod_name,
                module_to_hashes.get(mod_name, set()),
                module_to_components.get(mod_name, set()),
                hash_to_module, module_to_char_info, aliases_data, transition_new_owners,
            )
            if score > 0:
                candidates.append((score, idx, mod_name, tags))

    candidates.sort(key=lambda x: -x[0])

    assigned_json = [None] * len(json_entries)  # idx -> (mod_name, score, tags)
    taken_modules = set()
    for score, idx, mod_name, tags in candidates:
        if assigned_json[idx] is not None:
            continue
        if mod_name in taken_modules:
            continue
        if score < ASSIGN_MIN_SCORE:
            continue
        assigned_json[idx] = (mod_name, score, tags)
        taken_modules.add(mod_name)

    weak_candidates = {}
    for score, idx, mod_name, tags in candidates:
        if assigned_json[idx] is None:
            weak_candidates.setdefault(idx, []).append((score, mod_name, tags))
    for idx in weak_candidates:
        weak_candidates[idx].sort(key=lambda x: -x[0])

    # ---------------------------------------------------------------
    # Reporting per JSON file
    # ---------------------------------------------------------------
    critical_errors = 0
    serious_errors = 0
    missing_hashes_count = 0
    flagged_swapped_modules = set()
    unassigned_indices = []

    for idx, entry in enumerate(json_entries):
        filename = entry['name']
        all_json_hashes = entry['ib'] | entry['vb'] | entry['tex']

        if assigned_json[idx] is None:
            critical_errors += 1
            unassigned_indices.append(idx)

            unowned_ib = entry['ib'] - set(hash_to_module.keys())
            hint = ""
            if not all_json_hashes:
                hint = " (empty/unreadable JSON content?)"
            elif unowned_ib and unowned_ib <= transition_targets:
                hint = f" ({len(unowned_ib)} unowned IB hash(es) are transition targets - likely a hash-updated character whose module is out of sync)"
            elif unowned_ib:
                hint = f" ({len(unowned_ib)} IB hash(es) not owned by any module - likely a NEW character/skin without a Python module)"

            print(f"{Colors.RED}[✖ MISSING MODULE OR EMPTY FILE] Database file: '{filename}'{Colors.RESET}")
            print(f"{Colors.YELLOW}                                                     No matching Python module could be identified{hint}{Colors.RESET}")
            if weak_candidates.get(idx):
                tops = weak_candidates[idx][:3]
                cand_str = ", ".join(f"{m}.py (score {s:.0f})" for s, m, _ in tops)
                print(f"{Colors.YELLOW}                                                     Weak candidates: {cand_str}{Colors.RESET}")
            print()
            continue

        mod_name, match_score, tags = assigned_json[idx]
        char_info = module_to_char_info.get(mod_name, {})
        declared_name = char_info.get('name')
        safe_modules_in_group = []

        if declared_name:
            if mod_name.lower() != declared_name.lower():
                if mod_name not in flagged_swapped_modules:
                    flagged_swapped_modules.add(mod_name)
                    serious_errors += 1
                    print(f"{Colors.RED}[✖ CHARACTER FILE HASH CONTENT SWAPPED WITH ANOTHER CHARACTER] Module: {mod_name}.py{Colors.RESET}")
                    print(f"                                                                Name in file: '{mod_name}'")
                    print(f"                                                                Name in CHARACTER_INFO: '{declared_name}'")
                    print(f"{Colors.YELLOW}                                                                Please fix the content of your Python file first!\n{Colors.RESET}")
                continue
        safe_modules_in_group.append(mod_name)

        total_hashes = sum(len(module_to_hashes.get(m, set())) for m in safe_modules_in_group)
        if total_hashes == 0:
            critical_errors += 1
            print(f"{Colors.RED}[✖ MISSING MODULE OR EMPTY CHARACTER PYTHON FILE] Database file: '{filename}'{Colors.RESET}")
            print(f"{Colors.YELLOW}                                                     Matched module '{mod_name}.py' is EMPTY - fill in its hashes!{Colors.RESET}")
            print(f"                                                         Match evidence: {', '.join(tags) if tags else 'name'}")
            print()
            continue

        combined_py_hashes = set()
        for m in safe_modules_in_group:
            if m in module_to_hashes:
                combined_py_hashes.update(module_to_hashes[m])

        missing_hashes = all_json_hashes - combined_py_hashes
        if missing_hashes:
            expanded_modules = set(safe_modules_in_group)
            for h in missing_hashes:
                if h in hash_to_module:
                    for m in hash_to_module[h]:
                        m_info = module_to_char_info.get(m, {})
                        m_declared = m_info.get('name')
                        if not m_declared or m.lower() == m_declared.lower():
                            expanded_modules.add(m)
            if expanded_modules != set(safe_modules_in_group):
                safe_modules_in_group = [m for m in expanded_modules if m in module_to_hashes and module_to_hashes[m]]
                combined_py_hashes = set()
                for m in safe_modules_in_group:
                    combined_py_hashes.update(module_to_hashes[m])
                missing_hashes = all_json_hashes - combined_py_hashes

        if missing_hashes:
            missing_hashes_count += 1
            modules_display = ", ".join([f"{m}.py" for m in sorted(safe_modules_in_group)])
            module_type_label = "Group Module" if len(safe_modules_in_group) > 1 else "Individual Module"

            print(f"{Colors.RED}[✖ UNSYNCHRONIZED HASH] {module_type_label}: {modules_display}{Colors.RESET}")
            print(f"                        Matches with: {filename} (score {match_score:.0f}, {', '.join(tags) if tags else 'name'})")
            print(f"                        Found {Colors.YELLOW}{len(missing_hashes)}{Colors.RESET} hashes missing from your Python file group:")
            for h in sorted(missing_hashes):
                print(f"                        - {Colors.YELLOW}{h}{Colors.RESET}")
            print()

    # ---------------------------------------------------------------
    # Leftover pairing suggestions (order-based, verify manually)
    # ---------------------------------------------------------------
    if unassigned_indices:
        unmatched_modules = [m for m in module_order if m not in taken_modules]
        unassigned_names = [json_entries[i]['name'] for i in unassigned_indices]
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- LEFTOVER PAIRING SUGGESTIONS (verify manually) ---{Colors.RESET}")
        print(f"Unmatched JSON files ({len(unassigned_names)}): {', '.join(unassigned_names)}")
        if unmatched_modules:
            print(f"Unmatched modules ({len(unmatched_modules)}): {', '.join(f'{m}.py' for m in unmatched_modules)}")
            if len(unassigned_names) == len(unmatched_modules):
                print(f"{Colors.YELLOW}  Candidate pairs by order (JSON order vs CHARACTERS order) - VERIFY:{Colors.RESET}")
                for jname, mname in zip(unassigned_names, unmatched_modules):
                    print(f"{Colors.YELLOW}    ? {jname}  <->  {mname}.py{Colors.RESET}")
            print(f"{Colors.CYAN}  Tip: add a mapping to sync-aliases.json to make these deterministic.{Colors.RESET}")
        else:
            print("No unmatched modules left - you may need to create new Python files.")
        print()

    # ---------------------------------------------------------------
    # Orphan module report (registered but matched by no JSON)
    # ---------------------------------------------------------------
    orphans = []
    for m in module_order:
        if m in taken_modules:
            continue
        h = module_to_hashes.get(m, set())
        if h:
            orphans.append(m)
    if orphans:
        print(f"{Colors.CYAN}[i] ORPHAN MODULES (registered in __init__.py but matched by no JSON in this database):{Colors.RESET}")
        for m in orphans:
            print(f"{Colors.CYAN}    - {m}.py ({len(module_to_hashes.get(m, set()))} hashes){Colors.RESET}")
        print()

    if os.environ.get('ZZZ_SYNC_DEBUG'):
        print(f"\n{Colors.BOLD}{Colors.CYAN}--- ASSIGNMENT DEBUG (ZZZ_SYNC_DEBUG=1) ---{Colors.RESET}")
        for idx, entry in enumerate(json_entries):
            a = assigned_json[idx]
            if a:
                print(f"  {entry['name']}  ->  {a[0]}.py  (score {a[1]:.0f})  [{', '.join(a[2])}]")
            else:
                print(f"  {entry['name']}  ->  <NONE>")
        print()

    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[[V]] JSON VERIFICATION SUCCESS: All model database .json files are synchronized and secure with your Python files!\n{Colors.RESET}")

    # ---------------------------------------------------------------
    # Change log (.txt) synchronization analysis
    # ---------------------------------------------------------------
    print(f"\n{Colors.BOLD}{Colors.CYAN}============================================================{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN} ZZZ Mod Fixer - Change Log Synchronization Analysis (.txt){Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}============================================================{Colors.RESET}")

    txt_errors = 0
    skipped_transitions = 0
    commands_cache = {}

    def get_commands(character_name):
        if character_name not in commands_cache:
            sys.path.insert(0, str(py_data_path.parent))
            try:
                module = importlib.import_module(f'PlayerCharacterPYData.{character_name}')
                commands_cache[character_name] = module.get_hash_commands(**command_classes)
            except Exception as e:
                print(f"{Colors.RED}[✖] Failed to analyze module {character_name} for transition: {e}{Colors.RESET}")
                commands_cache[character_name] = {}
            finally:
                sys.path.remove(str(py_data_path.parent))
        return commands_cache[character_name]

    for txt_name, transitions, unique_transitions in all_transitions:
        print(f"\nAnalyzing transition log: {Colors.BLUE}'{txt_name}'{Colors.RESET} ({Colors.BOLD}{len(transitions)}{Colors.RESET} transitions found, {Colors.BOLD}{len(unique_transitions)}{Colors.RESET} unique)")

        for trans in unique_transitions:
            old_h = trans['old']
            new_h = trans['new']

            if old_h in active_hashes or old_h in other_res_hashes:
                skipped_transitions += 1
                continue

            target_mods = set()
            if old_h in hash_to_module:
                target_mods.update(hash_to_module[old_h])
                if trans['char_hint']:
                    kept = set()
                    excluded = []
                    for m in target_mods:
                        res = hint_matches_module(trans['char_hint'], m)
                        if res is True:
                            kept.add(m)
                        else:
                            excluded.append((m, res))
                    if kept:
                        target_mods = kept
                    else:
                        print(f"{Colors.YELLOW}[i] char_hint '{trans['char_hint']}' matches none of the {len(excluded)} owner(s) of {old_h}; checking all owners{Colors.RESET}")

            if not target_mods:
                continue

            for character_name in target_mods:
                try:
                    py_commands = get_commands(character_name)

                    if old_h not in py_commands:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ MISSING TRANSITION] Module: {character_name}.py{Colors.RESET}")
                        print(f"                     Old hash '{Colors.YELLOW}{old_h}{Colors.RESET}' not found in Python file!")
                        print(f"                     Log: {trans['line']}")
                        continue

                    commands_list = py_commands[old_h]
                    has_update_call = False
                    correct_target = False
                    actual_target = None

                    for cmd in commands_list:
                        if isinstance(cmd, tuple) and len(cmd) >= 1:
                            func = cmd[0]
                            if hasattr(func, '__name__') and func.__name__ == 'update_hash':
                                has_update_call = True
                                if len(cmd) >= 2 and isinstance(cmd[1], tuple) and len(cmd[1]) >= 1:
                                    actual_target = cmd[1][0].lower()
                                    if actual_target == new_h:
                                        correct_target = True
                                        break

                    if not has_update_call:
                        if new_h in py_commands:
                            print(f"{Colors.YELLOW}[i] Transition {old_h}->{new_h} in {character_name}.py: no update_hash, but new hash registered as own key (model-change pattern){Colors.RESET}")
                        elif new_h not in active_hashes and new_h not in other_res_hashes:
                            print(f"{Colors.YELLOW}[i] Transition {old_h}->{new_h} in {character_name}.py: target hash inactive in both resolutions (obsolete transition){Colors.RESET}")
                        else:
                            txt_errors += 1
                            print(f"{Colors.RED}[✖ INCORRECT TRANSITION] Module: {character_name}.py{Colors.RESET}")
                            print(f"                     Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' is registered, but does not have 'update_hash' command!")
                            print(f"                     Log: {trans['line']}")
                    elif not correct_target:
                        txt_errors += 1
                        print(f"{Colors.RED}[✖ INCORRECT TARGET] Module: {character_name}.py{Colors.RESET}")
                        print(f"                   Hash '{Colors.YELLOW}{old_h}{Colors.RESET}' updates to '{Colors.RED}{actual_target}{Colors.RESET}',")
                        print(f"                   should point to '{Colors.GREEN}{new_h}{Colors.RESET}' according to log!")
                        print(f"                   Log: {trans['line']}")

                except Exception as e:
                    print(f"{Colors.RED}[✖] Failed to analyze module {character_name} for transition: {e}{Colors.RESET}")

    if skipped_transitions:
        print(f"{Colors.CYAN}[i] {skipped_transitions} transition(s) skipped: old hash still active in this database (rolled-back/obsolete direction){Colors.RESET}")

    if txt_errors == 0:
        print(f"\n{Colors.BOLD}{Colors.GREEN}[[V]] TXT VERIFICATION SUCCESS: All transition logs .txt are successfully validated in your Python files!\n{Colors.RESET}")

    # ---------------------------------------------------------------
    # Conclusion
    # ---------------------------------------------------------------
    print(f"\n{Colors.BOLD}{Colors.CYAN}=========================== CONCLUSION ============================={Colors.RESET}")
    if critical_errors == 0 and serious_errors == 0 and missing_hashes_count == 0 and txt_errors == 0:
        print(f"{Colors.BOLD}{Colors.GREEN}[[V]] SYNCHRONIZATION SUCCESS: All your Python modules are perfectly synchronized with the JSON & .txt logs!{Colors.RESET}")
    else:
        print(f"{Colors.BOLD}{Colors.RED}[✖] SYNCHRONIZATION FAILED:{Colors.RESET}")
        if critical_errors > 0:
            print(f"    - Found {Colors.RED}{critical_errors}{Colors.RESET} cases of Missing Module or Empty Python file.")
        if serious_errors > 0:
            print(f"    - Found {Colors.RED}{serious_errors}{Colors.RESET} cases of Python file hash content swapped with another character.")
        if missing_hashes_count > 0:
            print(f"    - Found {Colors.RED}{missing_hashes_count}{Colors.RESET} groups of Python modules with hashes out of sync with the JSON database.")
        if txt_errors > 0:
            print(f"    - Found {Colors.RED}{txt_errors}{Colors.RESET} transition synchronization errors in .txt log.")
        print(f"\n    {Colors.YELLOW}Please fix the mismatches listed above for successful synchronization.{Colors.RESET}")
    print(f"{Colors.BOLD}{Colors.CYAN}===================================================================={Colors.RESET}")


if __name__ == '__main__':
    check_sync()
