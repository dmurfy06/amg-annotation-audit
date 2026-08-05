"""
inspect_explorenz_schema.py — does the official EC list record entry HISTORY?

Candidate A2 asks whether the twenty-year decline in orphan enzymes reflects orphans being
*solved* or merely *retired* from the EC classification. Answering that needs to know, per EC
number, when it was created and when (if ever) it was transferred or deleted.

The ENZYME flat file at Expasy carries no dates. ExplorEnz is the official IUBMB EC list and
publishes a full SQL dump. This checks whether that dump contains date/history fields.

This is a DATA CHECK, not the study.

Usage:
    python scripts/inspect_explorenz_schema.py
"""

import gzip
import io
import re
import urllib.request
from pathlib import Path

URL = "https://www.enzyme-database.org/downloads/enzyme-data.sql.gz"
CACHE = Path(__file__).resolve().parent.parent / "data" / "enzyme-data.sql"


def download() -> str:
    if CACHE.exists():
        print(f"using cached {CACHE} ({CACHE.stat().st_size:,} bytes)")
        return CACHE.read_text(encoding="utf-8", errors="replace")

    print(f"downloading {URL} ...")
    req = urllib.request.Request(URL, headers={"User-Agent": "research-project/0.1"})
    with urllib.request.urlopen(req, timeout=300) as r:
        blob = r.read()
    print(f"  compressed: {len(blob):,} bytes")

    text = gzip.decompress(blob).decode("utf-8", errors="replace")
    print(f"  decompressed: {len(text):,} characters")

    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(text, encoding="utf-8")
    return text


def main() -> None:
    sql = download()

    # Table definitions
    tables = re.findall(r"CREATE TABLE[^(]*?`?(\w+)`?\s*\(", sql, flags=re.I)
    print(f"\n=== {len(tables)} TABLES ===")
    for t in tables:
        print(f"  {t}")

    # Any column that looks like a date or history field
    print("\n=== DATE / HISTORY-LIKE COLUMNS ===")
    date_pat = re.compile(r"`(\w*(?:date|year|created|modif|hist|status|valid|delet|transfer)\w*)`",
                          flags=re.I)
    for block in re.finditer(r"CREATE TABLE[^(]*?`?(\w+)`?\s*\((.*?)\n\)", sql, flags=re.I | re.S):
        name, body = block.group(1), block.group(2)
        hits = sorted(set(date_pat.findall(body)))
        if hits:
            print(f"  {name}: {', '.join(hits)}")

    # Show the full definition of the main entry table
    print("\n=== SCHEMA OF THE MAIN ENTRY TABLE ===")
    for block in re.finditer(r"CREATE TABLE[^(]*?`?(\w+)`?\s*\((.*?)\n\)", sql, flags=re.I | re.S):
        if block.group(1).lower() in ("entry", "enzyme", "entries"):
            print(f"--- {block.group(1)} ---")
            for line in block.group(2).splitlines():
                line = line.strip().rstrip(",")
                if line.startswith("`"):
                    print(f"    {line}")
            break


if __name__ == "__main__":
    main()
