import json

def load_obs_sources(*files):
    """Load and merge all OBS glyphs from multiple JSON sources."""
    all_glyphs = {}
    for fname in files:
        with open(fname, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # Try to find glyphs in common structures
            if "obs_glyphs" in data:
                for entry in data["obs_glyphs"]:
                    code = entry.get("glyph")
                    if code:
                        all_glyphs[code] = entry
            elif isinstance(data, list):
                for entry in data:
                    code = entry.get("glyph") if isinstance(entry, dict) else entry
                    if code:
                        all_glyphs[code] = entry
            # Add more parsing logic for other dataset formats as needed
    return all_glyphs

def count_obs_glyphs(obs_glyphs):
    """Return the total number of unique OBS glyphs."""
    return len(obs_glyphs)

def print_obs_summary(obs_glyphs):
    print(f"Total unique OBS glyphs: {len(obs_glyphs):,}")
    # Print a sample with metadata
    for i, (glyph, meta) in enumerate(obs_glyphs.items()):
        print(f"{i+1:4d}: {glyph} | {meta.get('meaning','')} | {meta.get('vedic_archetype','')} | {meta.get('category','')}")
        if i >= 19:
            print("...")
            break

if __name__ == "__main__":
    # Example: merge your Hypercodex, HUST-OBC, and any other JSONs
    obs_glyphs = load_obs_sources(
        "bonskrpt_snakyha.json",  # your multidimensional mapping
        "hust_obc_deciphered.json",  # HUST-OBC deciphered
        "hust_obc_undeciphered.json" # HUST-OBC undeciphered
        # Add more files as needed
    )
    print_obs_summary(obs_glyphs)

    # Metadata and groupings (newly added)
    metadata = {
        "hypercodex_id": "OMEGA-POINT-777",
        "version": "99.9.9-FINAL",
        "author": "Timothy Andrew Lewis, Cosmic Naga King |•|~",
        "date": "2025-07-24",
        "license": "CC0 1.0 Universal (Public Domain Dedication)",
        "description": "Maximal Oracle Bone Script multidimensional mapping with cross-cultural, scientific, and ethical synthesis.",
        "languages": ["Sanskrit", "English", "中文", "日本語", "Español"],
        "sources": ["Hypercodex", "HUST-OBC", "Smithsonian", "Wikipedia"],
        "total_unique_glyphs": count_obs_glyphs(obs_glyphs)
    }

    groupings = {
        "by_category": {
            "celestial": ["𠂉", "𠂆"],
            "animal": ["馬", "牛"]
        },
        "by_unicode": [
            {"glyph": "一", "unicode": 19968},
            {"glyph": "二", "unicode": 20108}
        ],
        "by_stroke_count": [
            {"glyph": "一", "strokes": 1},
            {"glyph": "二", "strokes": 2}
        ]
    }

    # Print metadata summary
    print("\nMetadata:")
    for key, value in metadata.items():
        print(f"{key}: {value}")

    # Print groupings summary
    print("\nGroupings:")
    for category, glyphs in groupings["by_category"].items():
        print(f"{category}: {', '.join(glyphs)}")