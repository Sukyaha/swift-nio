"""
Ultimate Unified Hypercodex Vasuki Omniversal: Comprehensive Synthesis with OBS Omens |•|~
Author: Timothy Andrew Lewis, Cosmic Naga King |•|~
License: CC0 1.0 Universal (Public Domain Dedication)
Languages: Sanskrit, English, Français, Deutsch, عربي, Español, Русский, 日本語, Italiano, 中文, Esperanto, தமிழ், हिन्दी, বাংলা, తెలుగు, ಕನ್ನಡ, മലയാളം, ਪੰਜਾਬੀ, עִברִית
Description: This script extracts Oracle Bone Script glyphs and their multidimensional mappings from the Hypercodex, integrating Vedic cosmology, quantum recursion, Katapayadi encoding, and cross-cultural archetypes. All outputs are fractal, recursive, and maximally interconnected.
Provenance: Synthesized from 73+ conversational turns, PDF/JSON sources, and tool-assisted research as of July 2025.
"""

import json
import argparse

def extract_obs_glyphs(data):
    seen = set()
    obs = []
    try:
        char_list = data['projectVasuki']['linguistics_and_symbolic_systems']['cultural_and_mythic_narratives']['chinese_and_japanese_exemplars']['obs_character_linkages']['characters']
        for glyph in char_list:
            code = glyph.get("glyph")
            if code and code not in seen:
                obs.append({
                    "glyph": code,
                    "meaning": glyph.get("meaning"),
                    "geometry": glyph.get("geometric_data"),
                    "vedic_archetype": glyph.get("vedic_archetype"),
                    "related_sutra": glyph.get("related_sutra"),
                })
                seen.add(code)
    except Exception:
        pass
    try:
        char_dict = data['projectVasuki']['linguistics_and_symbolic_systems']['languages']['oracle_bone_script_details']['characters']
        for code, meta in char_dict.items():
            if code not in seen:
                obs.append({
                    "glyph": code,
                    "meaning": meta.get("meaning"),
                    "geometry": meta.get("geometric_data"),
                    "vedic_archetype": meta.get("vedic_archetype"),
                    "related_sutra": meta.get("related_sutra"),
                })
                seen.add(code)
    except Exception:
        pass
    obs.sort(key=lambda x: x["glyph"])
    return obs

def main():
    parser = argparse.ArgumentParser(description="Extract Oracle Bone Script glyphs from Hypercodex JSON (Vasuki Synthesis).")
    parser.add_argument("input", help="Input JSON file (e.g., h)")
    parser.add_argument("output", help="Output JSON file (e.g., snakyha_multi_dim.json)")
    args = parser.parse_args()

    with open(args.input, 'r', encoding='utf-8') as f:
        data = json.load(f)

    obs_glyphs = extract_obs_glyphs(data)

    # Add universal metadata to output
    output = {
        "metadata": {
            "hypercodex_id": "OMEGA-POINT-777",
            "version": "99.9.9-FINAL",
            "license": "CC0 1.0 Universal (Public Domain Dedication)",
            "author": "Timothy Andrew Lewis, Cosmic Naga King |•|~",
            "description": "OBS glyph multidimensional mapping, fractal synthesis, Katapayadi, Vedic, and Jungian archetypes.",
            "languages": ["Sanskrit", "English", "Français", "Deutsch", "Español", "中文", "日本語", "தமிழ்", "हिन्दी", "বাংলা", "తెలుగు", "ಕನ್ನಡ", "മലയാളം", "ਪੰਜਾਬੀ", "Esperanto", "Русский", "عربي", "Italiano", "עִברִית"]
        },
        "core_syntheses": {
            "oracle_bone_script": "Oldest Chinese script, astronomical omens, Vedic parallels.",
            "katapayadi_system": "Sanskrit number encoding, Pi recursion.",
            "shulba_sutras": "Vedic geometry, quantum knotting.",
            "jung_quaternity": "Trinity + matter = wholeness, archetype mapping."
        },
        "obs_glyphs": obs_glyphs
    }

    with open(args.output, 'w', encoding='utf-8') as out:
        json.dump(output, out, ensure_ascii=False, indent=2)

    print(f"Extracted {len(obs_glyphs)} unique OBS glyphs to {args.output} with Vasuki metadata.")

if __name__ == "__main__":
    main()