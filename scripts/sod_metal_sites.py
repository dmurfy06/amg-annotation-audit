"""
sod_metal_sites.py — feasibility probe for candidate E1.

E1 asks: across the superoxide dismutase family, how often is the modelled metal identity
inconsistent with the observed coordination environment?

Why this family. Cu (Z=29) and Zn (Z=30) differ by ONE electron, so they are close to
indistinguishable in X-ray electron density. Cu,Zn-SOD is the one abundant family that puts
both in a single active site. Mn-SOD and Fe-SOD sit in the same EC class as internal controls:
mononuclear, no confusable partner.

The biochemistry gives a testable expectation. In this family:
    Cu site  : ~4 His
    Zn site  : ~3 His + 1 Asp
    Mn / Fe  : 3 His + 1 Asp + solvent

So each assigned metal has an expected ligand signature, and departures are checkable.

Data source: MetalPDB REST API (Andreini et al.), which supplies coordination geometry already
computed by an established, citable tool — not reimplemented here.

Usage:
    python scripts/sod_metal_sites.py
"""

import json
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

API = "https://metalpdb.cerm.unifi.it/api?query=ec_number:1.15.1.1"
CACHE = Path(__file__).resolve().parent.parent / "data" / "metalpdb_sod.json"


def fetch() -> list[dict]:
    if CACHE.exists():
        print(f"using cached {CACHE} ({CACHE.stat().st_size:,} bytes)")
        return json.loads(CACHE.read_text(encoding="utf-8"))
    print(f"querying {API} ...")
    req = urllib.request.Request(API, headers={"User-Agent": "research-project/0.1"})
    with urllib.request.urlopen(req, timeout=180) as r:
        data = json.loads(r.read().decode("utf-8"))
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    CACHE.write_text(json.dumps(data), encoding="utf-8")
    print(f"  cached {len(data):,} sites -> {CACHE}")
    return data


def main() -> None:
    sites = fetch()
    print(f"\nMetalPDB sites for EC 1.15.1.1 : {len(sites):,}")
    print(f"distinct PDB entries           : {len({s['pdb'] for s in sites}):,}")
    print(f"distinct UniProt accessions    : {len({s.get('uniprot') for s in sites} - {None, ''}):,}")

    print("\n--- site type ---")
    for k, v in Counter(s.get("site_type", "?") for s in sites).most_common():
        print(f"   {k:<16} {v:>6,}")

    # flatten to one row per modelled metal atom
    rows = []
    for s in sites:
        for m in s.get("metals", []):
            resid = Counter(l["residue"] for l in m.get("ligands", []))
            rows.append({
                "pdb": s["pdb"],
                "site_type": s.get("site_type", "?"),
                "organism": s.get("organism", "?"),
                "metal": m.get("symbol", "?"),
                "geometry": m.get("geometry", "?"),
                "coordination": m.get("coordination"),
                "his": resid.get("HIS", 0),
                "asp": resid.get("ASP", 0),
                "hoh": resid.get("HOH", 0),
                "sig": "+".join(f"{n}{r}" for r, n in sorted(resid.items())),
            })

    print(f"\nmodelled metal atoms           : {len(rows):,}")
    print("\n--- metals present ---")
    for k, v in Counter(r["metal"] for r in rows).most_common(12):
        print(f"   {k:<6} {v:>6,}")

    print("\n--- coordination number by metal (the discrimination signal) ---")
    by_metal = defaultdict(Counter)
    for r in rows:
        by_metal[r["metal"]][r["coordination"]] += 1
    for metal in ("Cu", "Zn", "Mn", "Fe", "Ni"):
        if metal in by_metal:
            tot = sum(by_metal[metal].values())
            spread = ", ".join(f"{c}:{n}" for c, n in sorted(by_metal[metal].items(), key=lambda x: (x[0] is None, x[0])))
            print(f"   {metal:<3} (n={tot:>4})  {spread}")

    print("\n--- His/Asp ligand signature by metal (expected: Cu~4His, Zn~3His+Asp, Mn/Fe 3His+Asp+HOH) ---")
    print(f"   {'metal':<6} {'n':>5} {'mean His':>9} {'mean Asp':>9} {'mean HOH':>9}")
    for metal in ("Cu", "Zn", "Mn", "Fe"):
        sub = [r for r in rows if r["metal"] == metal]
        if not sub:
            continue
        n = len(sub)
        print(f"   {metal:<6} {n:>5} {sum(r['his'] for r in sub)/n:>9.2f} "
              f"{sum(r['asp'] for r in sub)/n:>9.2f} {sum(r['hoh'] for r in sub)/n:>9.2f}")

    print("\n--- most common exact ligand signatures, per metal ---")
    for metal in ("Cu", "Zn", "Mn", "Fe"):
        sub = [r for r in rows if r["metal"] == metal]
        if not sub:
            continue
        print(f"   {metal}  (n={len(sub)})")
        for sig, n in Counter(r["sig"] for r in sub).most_common(5):
            print(f"       {n:>5}  {sig}")

    print("\n--- geometry classes seen ---")
    for k, v in Counter(r["geometry"] for r in rows).most_common(10):
        print(f"   {v:>5}  {k}")


if __name__ == "__main__":
    main()
