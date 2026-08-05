"""
inspect_explorenz_hist.py — what is actually recorded in ExplorEnz's history table?

Follow-up to inspect_explorenz_schema.py, which found a `hist` table and a `status` column
on `entry`. This checks whether those fields can answer candidate A2:

    Is the decline in orphan enzymes driven by orphans being SOLVED,
    or by orphans being RETIRED from the EC classification?

Needs, per EC number: a status (valid / transferred / deleted) and a date.

Usage:
    python scripts/inspect_explorenz_hist.py
"""

import re
from collections import Counter
from pathlib import Path

SQL = Path(__file__).resolve().parent.parent / "data" / "enzyme-data.sql"


def table_schema(sql: str, table: str) -> list[str]:
    m = re.search(rf"CREATE TABLE[^(]*?`{table}`\s*\((.*?)\n\)", sql, flags=re.I | re.S)
    if not m:
        return []
    return [ln.strip().rstrip(",") for ln in m.group(1).splitlines() if ln.strip().startswith("`")]


def insert_rows(sql: str, table: str, limit: int | None = None) -> list[str]:
    """Pull raw tuple strings out of INSERT INTO statements for one table."""
    rows: list[str] = []
    for m in re.finditer(rf"INSERT INTO `{table}` VALUES\s*(.*?);\n", sql, flags=re.I | re.S):
        payload = m.group(1)
        # split on '),(' boundaries without breaking strings containing commas
        for tup in re.findall(r"\((.*?)\)(?=,\(|\s*$)", payload, flags=re.S):
            rows.append(tup)
            if limit and len(rows) >= limit:
                return rows
    return rows


def main() -> None:
    sql = SQL.read_text(encoding="utf-8", errors="replace")

    for t in ("hist", "entry"):
        print(f"=== SCHEMA: {t} ===")
        for col in table_schema(sql, t):
            print(f"   {col}")
        print()

    print("=== SAMPLE ROWS FROM `hist` ===")
    for row in insert_rows(sql, "hist", limit=8):
        print(f"   {row[:400]}")
    print()

    # status codes on entry — how many EC numbers are valid / transferred / deleted?
    entry_rows = insert_rows(sql, "entry")
    print(f"=== `entry` rows parsed: {len(entry_rows):,} ===")

    # status is a 3-char code; find it by position using the schema order
    cols = [re.match(r"`(\w+)`", c).group(1) for c in table_schema(sql, "entry")]
    try:
        i_status = cols.index("status")
        i_ec = cols.index("ec_num")
    except ValueError:
        print("could not locate columns")
        return

    def split_tuple(t: str) -> list[str]:
        """Split a MySQL VALUES tuple on top-level commas, respecting quotes/escapes."""
        out, buf, q, esc = [], [], False, False
        for ch in t:
            if esc:
                buf.append(ch); esc = False; continue
            if ch == "\\":
                buf.append(ch); esc = True; continue
            if ch == "'":
                q = not q; buf.append(ch); continue
            if ch == "," and not q:
                out.append("".join(buf).strip()); buf = []; continue
            buf.append(ch)
        out.append("".join(buf).strip())
        return out

    statuses = Counter()
    ok = 0
    for r in entry_rows:
        parts = split_tuple(r)
        if len(parts) <= max(i_status, i_ec):
            continue
        ok += 1
        statuses[parts[i_status].strip("'")] += 1

    print(f"rows successfully split: {ok:,}")
    print("\n=== STATUS CODE DISTRIBUTION ===")
    for k, v in statuses.most_common():
        print(f"   {k!r:>10} : {v:>6,}")


if __name__ == "__main__":
    main()
