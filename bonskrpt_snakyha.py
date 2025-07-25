import json

# Load the Hypercodex JSON
with open('h', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Helper: flatten both list-based and dict-based OBS character sources
def extract_obs_glyphs(data):
    obs = []
    # List-based (decoded/linked glyphs)
    try:
        char_list = data['projectVasuki']['cultural_and_mythic_narratives']['chinese_and_japanese_exemplars']['obs_character_linkages']['characters']
        for glyph in char_list:
            obs.append(glyph)
    except Exception:
        pass
    # Dict-based (remaining/undecoded glyphs)
    try:
        char_dict = data['projectVasuki']['linguistics_and_symbolic_systems']['languages']['oracle_bone_script_details']['characters']
        for glyph, meta in char_dict.items():
            entry = {
                "glyph": glyph,
                "related_sutra": meta.get("related_sutra"),
                # Add more fields if present in meta
            }
            obs.append(entry)
    except Exception:
        pass
    return obs

# Build multi-dimensional mapping for snakyha
obs_glyphs = extract_obs_glyphs(data)
multi_dim_snakyha = []
for glyph in obs_glyphs:
    entry = {
        "glyph": glyph.get("glyph", glyph) if isinstance(glyph, dict) else glyph,
        "meaning": glyph.get("meaning") if isinstance(glyph, dict) else None,
        "geometry": glyph.get("geometric_data") if isinstance(glyph, dict) else None,
        "vedic_archetype": glyph.get("vedic_archetype") if isinstance(glyph, dict) else None,
        "related_sutra": glyph.get("related_sutra") if isinstance(glyph, dict) else None,
        # Add more dimensions as needed
    }
    multi_dim_snakyha.append(entry)

# Output to JSON
with open('bonskrpt_snakyha.json', 'w', encoding='utf-8') as out:
    json.dump(multi_dim_snakyha, out, ensure_ascii=False, indent=2)

print(f"Extracted {len(multi_dim_snakyha)} OBS glyphs for snakyha multi-dimensional mapping.")