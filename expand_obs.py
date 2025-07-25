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