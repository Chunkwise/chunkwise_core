import unicodedata
import re

# Maps for problematic typography → ASCII
QUOTE_MAP = {
    "\u2018": "'",  # ‘
    "\u2019": "'",  # ’
    "\u201a": "'",  # ‚
    "\u201b": "'",  # ‛
    "\u2032": "'",  # ′
    "\u2035": "'",  # ‵
    "\u201c": '"',  # “
    "\u201d": '"',  # ”
    "\u201e": '"',  # „
    "\u201f": '"',  # ‟
    "\u2033": '"',  # ″
    "\u2036": '"',  # ‶
    "\xab": '"',  # «
    "\xbb": '"',  # »
}

DASH_MAP = {
    "\u2010": "-",  # ‐
    "\u2011": "-",  # -
    "\u2012": "-",  # ‒
    "\u2013": "-",  # –
    "\u2014": "-",  # —
    "\u2015": "-",  # ―
}

OTHER_PUNCT_MAP = {
    "\u2026": "...",  # … ellipsis
    "\u00a0": " ",  # non-breaking space → regular space
}

INVISIBLE_CHARS = [
    "\u200b",  # zero width space
    "\u200c",  # zero width non-joiner
    "\u200d",  # zero width joiner
    "\ufeff",  # BOM / zero width no-break space
    "\u2060",  # word joiner
    "\u202a",
    "\u202b",
    "\u202c",
    "\u202d",
    "\u202e",  # bidi control
]


def normalize_document(content: str) -> str:
    """
    Normalize a document for stable token-based chunking:
    - Convert smart quotes, dashes, guillemets, ellipsis, NBSP → ASCII
    - Remove invisible/control characters
    - Preserve emojis and other meaningful Unicode characters
    """

    if not content:
        return content

    # 1) Unicode normalization: good for width/compat forms, doesn't break emojis
    content = unicodedata.normalize("NFKC", content)

    # 2) Map fancy quotes / dashes / misc punctuation to ASCII equivalents
    for src, dst in {**QUOTE_MAP, **DASH_MAP, **OTHER_PUNCT_MAP}.items():
        content = content.replace(src, dst)

    # 3) Remove specific invisible Unicode chars
    for ch in INVISIBLE_CHARS:
        content = content.replace(ch, "")

    # 4) Strip control characters except tab/newline/carriage return
    content = re.sub(r"[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]", "", content)

    # 5) Defensive: ensure the resulting string is valid UTF-8
    #    (drops any truly invalid surrogates if they slipped in)
    content = content.encode("utf-8", "ignore").decode("utf-8")

    return content
