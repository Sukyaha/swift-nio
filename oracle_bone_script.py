"""
Oracle Bone Script Module
Copyright (c) 2025 Timothy Lewis

Provides mappings and utilities for ancient Chinese oracle bone scripts,
including astronomical, mythological, and numerical systems, with cross-cultural
integrations for Vedic cosmology and sacred geometry.

Bone Script (Oracle Bone Script) - The earliest known Chinese writing system (c. 1200 BCE).
This module provides mappings, metadata, and utilities for integrating ancient symbolic systems into Project Vasuki,
with extensions for cross-cultural connections to Vedic cosmology, sacred geometry, and modern physics.
"""

# --- Constants ---
BONE_SCRIPT_VERSION = "1.0.0"
SCRIPT_DATE_RANGE = "c. 1200-1050 BCE"
DEFAULT_EXPORT_PATH = "exports/"

# --- Imports ---
import random
import csv
import json
from typing import Dict, List, Set, Tuple, Optional
import math
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, solve, Rational

# --- Metadata ---
BONE_SCRIPT_METADATA = {
    "origin": "Oracle Bone Script, Shang Dynasty, c. 1200 BCE",
    "description": (
        "Earliest logographic Chinese script, used for divination, record-keeping, "
        "and communication with ancestors. Precursor to modern Chinese characters."
    ),
    "reference": "https://en.wikipedia.org/wiki/Oracle_bone_script",
    "notable_inscriptions": [
        "Records of royal divinations",
        "Genealogies of Shang kings",
        "Early astronomical observations"
    ],
    "writing_medium": [
        "Ox scapulae (shoulder blades)",
        "Turtle plastrons (underside shells)"
    ],
    "script_type": "Logographic",
    "unicode_range": "U+3400–U+4DBF (CJK Unified Ideographs Extension A)",
    "related_scripts": [
        "Bronze Script",
        "Seal Script",
        "Clerical Script"
    ],
    "regions": [
        "Anyang, Henan Province",
        "Central Plains of China"
    ],
    "script_evolution": [
        "Oracle Bone Script",
        "Bronze Script",
        "Large Seal Script",
        "Small Seal Script",
        "Clerical Script",
        "Regular Script"
    ],
    "notable_artifacts": [
        "Oracle bones from Yinxu",
        "Shang dynasty divination archives"
    ]
}

# --- Main Glyph Map ---
BONE_SCRIPT_MAP = {
    # Nature & Elements
    "sun": "𠂉", "moon": "𠂆", "star": "星", "sky": "天", "earth": "土", "mountain": "山", "river": "川",
    "lake": "湖", "sea": "海", "water": "水", "fire": "火", "wind": "風", "rain": "雨", "cloud": "雲",
    "lightning": "電", "fog": "霧", "snow": "雪", "ice": "冰", "stone": "石", "tree": "木", "forest": "林",
    "field": "田", "grass": "草", "flower": "花", "fruit": "果", "grain": "禾", "sand": "沙", "soil": "壤",
    # Animals
    "horse": "馬", "ox": "牛", "sheep": "羊", "goat": "羊", "dog": "犬", "cat": "貓", "pig": "豬",
    "chicken": "雞", "duck": "鴨", "goose": "鵝", "fish": "魚", "bird": "鳥", "turtle": "龜", "snake": "蛇",
    "tiger": "虎", "lion": "獅", "rabbit": "兔", "monkey": "猴", "rat": "鼠", "dragon": "龍", "wolf": "狼",
    "bear": "熊", "elephant": "象", "deer": "鹿", "frog": "蛙", "insect": "蟲", "bee": "蜂", "ant": "蟻",
    # Body & People
    "person": "人", "man": "男", "woman": "女", "child": "子", "father": "父", "mother": "母", "elder": "老",
    "ancestor": "祖", "king": "王", "emperor": "帝", "prince": "君", "official": "臣", "soldier": "兵",
    "teacher": "師", "student": "生", "friend": "友", "enemy": "敵", "family": "家",
    "head": "首", "eye": "目", "ear": "耳", "nose": "鼻", "mouth": "口", "tooth": "齒", "tongue": "舌",
    "hand": "手", "arm": "臂", "foot": "足", "leg": "腿", "heart": "心", "liver": "肝", "bone": "骨",
    "spine": "脊", "blood": "血", "skin": "皮", "hair": "毛",
    # Society & Objects
    "city": "邑", "village": "村", "house": "屋", "gate": "門", "road": "道", "bridge": "橋", "market": "市",
    "shop": "店", "school": "學", "temple": "寺", "palace": "宮", "tower": "樓", "wall": "牆",
    "carriage": "車", "boat": "舟", "flag": "旗", "seal": "印", "book": "書", "scroll": "卷", "record": "記",
    "bell": "鐘", "drum": "鼓", "vessel": "皿", "tool": "器", "weapon": "兵", "knife": "刀", "bow": "弓",
    "arrow": "矢", "sword": "劍", "shield": "盾", "armor": "甲", "coin": "錢", "jade": "玉", "gold": "金",
    "silver": "銀", "bronze": "銅", "iron": "鐵", "copper": "銅", "pottery": "陶",
    # Food & Drink
    "food": "食", "rice": "米", "wheat": "麥", "millet": "黍", "vegetable": "菜", "meat": "肉", "egg": "卵",
    "salt": "鹽", "wine": "酒", "tea": "茶",
    # Abstract & Actions
    "life": "生", "death": "死", "birth": "生", "age": "年", "time": "時", "season": "季",
    "spring": "春", "summer": "夏", "autumn": "秋", "winter": "冬", "day": "日", "night": "夜",
    "morning": "晨", "evening": "夕", "dawn": "曉", "dusk": "暮",
    "war": "戰", "peace": "和", "love": "愛", "hate": "恨", "truth": "真", "false": "假",
    "good": "善", "evil": "惡", "fortune": "福", "misfortune": "禍", "question": "問", "answer": "答",
    "yes": "是", "no": "否", "order": "令", "law": "法", "justice": "義", "spirit": "神",
    "oracle": "卜", "divination": "卜", "sacrifice": "祭", "music": "樂", "dance": "舞", "song": "歌",
    "writing": "文", "speech": "言", "teach": "教", "learn": "學", "read": "讀", "write": "寫", "draw": "畫",
    "sing": "唱", "play": "玩", "run": "跑", "walk": "行", "jump": "跳", "see": "見", "hear": "聽",
    "speak": "說", "eat": "食", "drink": "飲", "sleep": "睡", "dream": "夢",
    # Numbers
    "one": "一", "two": "二", "three": "三", "four": "四", "five": "五",
    "six": "六", "seven": "七", "eight": "八", "nine": "九", "ten": "十",
    # Astronomy
    "orion": "𠂉",  # Shēn, the constellation Orion in Chinese astronomy
    "comet": "彗", "eclipse": "食", "guest_star": "客星", "milky_way": "天河", "north_star": "北極",
    "big_dipper": "斗", "pleiades": "昴", "antares": "心", "sirius": "天狼", "spica": "角",
    "sacred_tree": "桑", "world_tree": "木"
}
BONE_SCRIPT_MAP["note_orion_vs_ten"] = (
    "Note: '参' (shēn, Orion) and '十' (shí, ten) are unrelated in meaning and pronunciation. "
    "'参' refers to the constellation Orion in Chinese astronomy, while '十' is the number ten."
)

# --- Astronomical Inscriptions ---
ASTRONOMICAL_INSCRIPTIONS = {
    "summary": (
        "Oracle bone inscriptions include records of eclipses, comets (broom stars), and unusual celestial events. "
        "These were interpreted as omens and often linked to royal divination."
    ),
    "examples": [
        {"event": "Solar eclipse", "glyph": "食", "description": "Recorded as omens; questions about their meaning for the king."},
        {"event": "Comet", "glyph": "彗", "description": "Described as 'broom stars' sweeping the sky."},
        {"event": "Guest star", "glyph": "客星", "description": "Unusual new stars, possibly novae or supernovae."},
        {"event": "Planet", "glyph": "辰", "description": "Sometimes refers to planets or heavenly bodies."},
        {"event": "Orion (Shēn)", "glyph": "参", "description": "Orion's Belt, the 'Three Stars' asterism in Chinese astronomy."},
        {"event": "Big Dipper (Dǒu)", "glyph": "斗", "description": "The Big Dipper, a key asterism for timekeeping and navigation."},
        {"event": "Pleiades (Mǎo)", "glyph": "昴", "description": "The Pleiades cluster, important in agricultural calendars."},
        {"event": "Sirius (Tiānláng)", "glyph": "天狼", "description": "Sirius, the 'Heavenly Wolf' star."},
        {"event": "Vega (Zhīnǚ)", "glyph": "織女", "description": "Vega, the 'Weaving Girl' in the Qixi myth."},
        {"event": "Altair (Niúláng)", "glyph": "牛郎", "description": "Altair, the 'Cowherd' in the Qixi myth."},
        {"event": "Milky Way (Tiānhé)", "glyph": "天河", "description": "The Milky Way, 'Heavenly River'."},
        {"event": "Polaris (Běijí)", "glyph": "北極", "description": "Polaris, the North Star."},
        {"event": "Antares (Xīnxiù)", "glyph": "心宿", "description": "Antares, heart of the Scorpion."},
        {"event": "Betelgeuse (Shēnxiù Sì)", "glyph": "参宿四", "description": "Betelgeuse, Orion's shoulder."},
        {"event": "Bellatrix (Shēnxiù Wǔ)", "glyph": "参宿五", "description": "Bellatrix, Orion's other shoulder."}
    ],
    "references": [
        "https://en.wikipedia.org/wiki/Oracle_bone_script#Astronomical_records",
        "https://en.wikipedia.org/wiki/Chinese_astronomy#Oracle_bones"
    ]
}

# --- Sri Yantra Mapping ---
SRI_YANTRA_MAP = {
    "bindu": {
        "glyph": "•",
        "description": "Cosmic center, source of energy, point of expansion",
        "sanskrit": "बिंदु",
        "quantity": 1
    },
    "upward_triangle": {
        "glyph": "△",
        "description": "Masculine principle (Shiva), unmanifest power of cosmos",
        "sanskrit": "ऊर्ध्व त्रिकोण",
        "quantity": 4
    },
    "downward_triangle": {
        "glyph": "▽",
        "description": "Feminine principle (Shakti), manifest aspect of the world",
        "sanskrit": "अधस्त्रिकोण",
        "quantity": 5
    },
    "smaller_triangles": {
        "glyph": "▴",
        "description": "Totality of the cosmos, Advaita (non-duality), womb of creation",
        "sanskrit": "लघु त्रिकोण",
        "quantity": 43
    },
    "ashtadal_lotus": {
        "glyph": "⚘",
        "description": "Lotus of creation, fertile life force",
        "sanskrit": "अष्टदल कमल",
        "quantity": 8
    },
    "shodashdal_lotus": {
        "glyph": "⚘",
        "description": "Lotus of creation, fertile life force",
        "sanskrit": "षोडशदल कमल",
        "quantity": 16
    },
    "bhupura": {
        "glyph": "□",
        "description": "A temple, four doors to the regions of the universe",
        "sanskrit": "भूपुर",
        "quantity": 1
    }
}

# --- Pronunciation Mapping ---
ORACLE_BONE_PRONUNCIATION = {
    "sun": {"pinyin": "rì", "ipa": "ʐɻ̩˥˩", "sanskrit": "सूर्य", "english": "sun"},
    "moon": {"pinyin": "yuè", "ipa": "yɛ˥˩", "sanskrit": "चन्द्र", "english": "moon"},
    "star": {"pinyin": "xīng", "ipa": "ɕiŋ˥", "sanskrit": "तारा", "english": "star"},
    "orion": {"pinyin": "shēn", "ipa": "ʂən˥", "sanskrit": "मृगशिरा", "english": "orion"},
    "world_tree": {"pinyin": "mù", "ipa": "mu˥˩", "sanskrit": "विश्ववृक्ष", "english": "world tree"},
}

# --- Nakshatra and Chinese Mansion Comparison ---
CHINESE_MANSIONS_NAKSHATRA_COMPARISON = {
    "昴": {"nakshatra": "Krittika", "vedic": "कृत्तिका", "notes": "Pleiades cluster, associated with fire and transformation"},
    "参": {"nakshatra": "Mrigashira", "vedic": "मृगशिरा", "notes": "Orion's Belt, linked to searching and pursuit"},
    "心": {"nakshatra": "Anuradha", "vedic": "अनुराधा", "notes": "Antares, symbolizing devotion and friendship"},
    "天河": {"nakshatra": "Magha", "vedic": "मघा", "notes": "Milky Way, connected to ancestry and power"},
    "北極": {"nakshatra": "Uttara Bhadrapada", "vedic": "उत्तर भाद्रपदा", "notes": "Polaris, associated with wisdom and stability"},
    "number_108": {
        "nakshatra": "All Nakshatras",
        "vedic": "सभी नक्षत्र",
        "notes": "108 padas (27 Nakshatras x 4 padas), symbolizing cosmic harmony; also tied to cosmic distances (Sun, Moon, Earth)"
    }
}

# --- Helper Tables for Grouping ---
# (Expand these as you add more glyphs and cross-language data)
OBS_GROUPS = {
    "celestial": [
        "sun", "moon", "star", "orion", "comet", "eclipse", "guest_star", "milky_way", "north_star",
        "big_dipper", "pleiades", "antares", "sirius", "spica"
    ],
    "animal": [
        "horse", "ox", "sheep", "goat", "dog", "cat", "pig", "chicken", "duck", "goose", "fish", "bird",
        "turtle", "snake", "tiger", "lion", "rabbit", "monkey", "rat", "dragon", "wolf", "bear", "elephant",
        "deer", "frog", "insect", "bee", "ant"
    ],
    "body": [
        "person", "man", "woman", "child", "father", "mother", "elder", "ancestor", "king", "emperor",
        "prince", "official", "soldier", "teacher", "student", "friend", "enemy", "family", "head", "eye",
        "ear", "nose", "mouth", "tooth", "tongue", "hand", "arm", "foot", "leg", "heart", "liver", "bone",
        "spine", "blood", "skin", "hair"
    ],
    "number": [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"
    ],
    "element": [
        "earth", "mountain", "river", "lake", "sea", "water", "fire", "wind", "rain", "cloud", "lightning",
        "fog", "snow", "ice", "stone", "tree", "forest", "field", "grass", "flower", "fruit", "grain", "sand", "soil"
    ],
    # Add more as needed...
}

# --- Cross-Language/Astrological Table ---
# Each entry: OBS concept, glyph, modern Chinese, Sanskrit, English, Nakshatra, etc.
OBS_CROSSLANG = [
    {
        "concept": "sun",
        "glyph": BONE_SCRIPT_MAP.get("sun"),
        "chinese": "日",
        "sanskrit": "सूर्य",
        "english": "sun",
        "nakshatra": "Krittika",
        "vedic": "कृत्तिका"
    },
    {
        "concept": "moon",
        "glyph": BONE_SCRIPT_MAP.get("moon"),
        "chinese": "月",
        "sanskrit": "चन्द्र",
        "english": "moon",
        "nakshatra": "Rohini",
        "vedic": "रोहिणी"
    },
    {
        "concept": "orion",
        "glyph": BONE_SCRIPT_MAP.get("orion"),
        "chinese": "参",
        "sanskrit": "मृगशिरा",
        "english": "Orion",
        "nakshatra": "Mrigashira",
        "vedic": "मृगशिरा"
    },
    {
        "concept": "pleiades",
        "glyph": BONE_SCRIPT_MAP.get("pleiades"),
        "chinese": "昴",
        "sanskrit": "कृत्तिका",
        "english": "Pleiades",
        "nakshatra": "Krittika",
        "vedic": "कृत्तिका"
    },
    {
        "concept": "antares",
        "glyph": BONE_SCRIPT_MAP.get("antares"),
        "chinese": "心",
        "sanskrit": "अनुराधा",
        "english": "Antares",
        "nakshatra": "Anuradha",
        "vedic": "अनुराधा"
    },
    # ...add more celestial/animal/body/number mappings...
]

# --- Unicode and Stroke Utilities ---
def _get_unicode_decimal(glyph: str) -> int:
    if not glyph or not isinstance(glyph, str):
        return -1
    return ord(glyph[0])

def _estimate_stroke_count(glyph: str) -> int:
    # Minimal hardcoded strokes for common glyphs (expand as needed)
    stroke_table = {
        "一": 1, "二": 2, "三": 3, "十": 2, "口": 3, "日": 4, "月": 4, "木": 4, "水": 4, "火": 4, "田": 5,
        "目": 5, "心": 4, "山": 3, "川": 3, "天": 4, "王": 4, "土": 3, "人": 2, "女": 3, "子": 3, "馬": 10,
        "魚": 11, "鳥": 11, "龜": 16, "参": 8, "星": 9, "雨": 8, "雲": 12, "風": 9, "雪": 11, "電": 13,
        "龍": 16, "虎": 8, "羊": 6, "牛": 4, "犬": 4, "豬": 11, "骨": 10, "血": 6,
        # Add more as needed...
    }
    ch = glyph[0] if glyph else ""
    return stroke_table.get(ch, 0)

def print_obs_grouped(by="unicode"):
    """
    Print all OBS glyphs grouped by 'unicode', 'stroke', or 'category'.
    """
    # Only single-char glyphs for unicode/stroke sorting
    items = [(concept, glyph) for concept, glyph in BONE_SCRIPT_MAP.items() if isinstance(glyph, str) and len(glyph) == 1]
    if by == "unicode":
        sorted_items = sorted(items, key=lambda x: _get_unicode_decimal(x[1]))
        print("OBS glyphs sorted by Unicode decimal:")
        for concept, glyph in sorted_items:
            print(f"{concept:15} | {glyph} | U+{ord(glyph):04X} | {ord(glyph)}")
    elif by == "stroke":
        sorted_items = sorted(items, key=lambda x: (_estimate_stroke_count(x[1]), _get_unicode_decimal(x[1])))
        print("OBS glyphs sorted by estimated stroke count:")
        for concept, glyph in sorted_items:
            print(f"{concept:15} | {glyph} | strokes: {_estimate_stroke_count(glyph)} | U+{ord(glyph):04X}")
    elif by == "category":
        for cat, concepts in OBS_GROUPS.items():
            print(f"\nCategory: {cat}")
            for concept in concepts:
                glyph = BONE_SCRIPT_MAP.get(concept)
                if glyph:
                    print(f"  {concept:15} | {glyph} | U+{ord(glyph):04X}")
    else:
        print("Unknown grouping. Use 'unicode', 'stroke', or 'category'.")

def print_obs_crosslang_table():
    """
    Print cross-language/astrological table for all mapped concepts.
    """
    print(f"{'Concept':<10} | {'OBS':<4} | {'Chinese':<4} | {'Sanskrit':<10} | {'English':<10} | {'Nakshatra':<10} | {'Vedic':<10}")
    print("-" * 70)
    for entry in OBS_CROSSLANG:
        print(f"{entry['concept']:<10} | {entry['glyph']:<4} | {entry['chinese']:<4} | {entry['sanskrit']:<10} | {entry['english']:<10} | {entry['nakshatra']:<10} | {entry['vedic']:<10}")

# --- Example CLI Usage ---
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Oracle Bone Script Grouping/Unification Tools")
    parser.add_argument("--group", choices=["unicode", "stroke", "category"], help="Group OBS glyphs by this method")
    parser.add_argument("--crosslang", action="store_true", help="Show cross-language/astrological table")
    args = parser.parse_args()
    if args.group:
        print_obs_grouped(by=args.group)
    if args.crosslang:
        print_obs_crosslang_table()

# --- Summary of Unique OBS Glyphs ---
TOTAL_UNIQUE_GLYPHS = 2345
print(f"\nTotal unique OBS glyphs: {TOTAL_UNIQUE_GLYPHS}")
for i, (concept, glyph) in enumerate(BONE_SCRIPT_MAP.items(), 1):
    if isinstance(glyph, str) and len(glyph) == 1:  # Only single-char glyphs
        print(f"   {i}: {glyph} | {concept} | {glyph} | celestial")