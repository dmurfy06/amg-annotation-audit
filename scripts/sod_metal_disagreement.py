"""
sod_metal_disagreement.py — do independent structures of the SAME protein disagree
about which metal it contains?

Sharpened form of candidate E1. The earlier probe (sod_metal_sites.py) showed that in the
SOD family:

  * Cu and Zn are cleanly separable by ligand set (Cu almost never has Asp; Zn almost always
    does), so the original Cu/Zn framing was wrong.
  * Mn and Fe are NOT separable: identical dominant signature (1ASP+3HIS+1HOH), identical
    coordination-number distribution, same Pfam domains, and one electron apart (Z=25 vs 26).

Fe/Mn ambiguity is biologically real — "cambialistic" SODs bind either metal. But that is
documented protein by protein. The question here is about the *structural record itself*:

    For a given protein (same UniProt accession), do different PDB depositions
    assign different metals to the equivalent site?

Disagreement between independent redeterminations of the same thing is a direct measure of
how much the deposited metal identity can be trusted.

Usage:
    python scripts/sod_metal_disagreement.py
"""

import json
from collections import Counter, defaultdict
from pathlib import Path

CACHE = Path(__file__).resolve().parent.parent / "data" / "metalpdb_sod.json"

# Metals that are plausibly catalytic in this family. Everything else (Na, K, Ca, Cd, Pt, U…)
# is far more likely to be a crystallisation additive or heavy-atom derivative.
CATALYTIC = {"Cu", "Zn", "Mn", "Fe", "Ni"}


def main() -> None:
    sites = json.loads(CACHE.read_text(encoding="utf-8"))
    print(f"sites loaded: {len(sites):,}\n")

    # protein -> set of metals seen, and which PDB entries carried them
    by_uniprot: dict[str, dict[str, set[str]]] = defaultdict(lambda: defaultdict(set))
    organism: dict[str, str] = {}
    noncatalytic = Counter()

    for s in sites:
        acc = (s.get("uniprot") or "").strip()
        if not acc:
            continue
        organism.setdefault(acc, s.get("organism", "?"))
        for m in s.get("metals", []):
            sym = m.get("symbol", "?")
            if sym in CATALYTIC:
                by_uniprot[acc][sym].add(s["pdb"])
            else:
                noncatalytic[sym] += 1

    print(f"proteins (UniProt accessions) with catalytic metals: {len(by_uniprot):,}")

    # --- the headline check ---
    conflicts = []
    for acc, metals in by_uniprot.items():
        # only meaningful if the protein has more than one PDB entry
        entries = set().union(*metals.values())
        if len(entries) < 2:
            continue
        # Cu+Zn together is EXPECTED (Cu,Zn-SOD is a two-metal enzyme), not a conflict.
        core = set(metals) - {"Cu", "Zn"} if {"Cu", "Zn"} <= set(metals) else set(metals)
        if len(core) > 1:
            conflicts.append((acc, organism.get(acc, "?"), {k: sorted(v) for k, v in metals.items()}))

    print(f"proteins with >=2 PDB entries: "
          f"{sum(1 for a, m in by_uniprot.items() if len(set().union(*m.values())) >= 2):,}")
    print(f"\n=== PROTEINS WHERE DEPOSITIONS DISAGREE ON THE METAL: {len(conflicts)} ===\n")

    for acc, org, metals in sorted(conflicts, key=lambda x: -sum(len(v) for v in x[2].values())):
        total = sum(len(v) for v in metals.values())
        print(f"  {acc}  ({org})  — {total} entries")
        for sym, pdbs in sorted(metals.items(), key=lambda x: -len(x[1])):
            shown = ", ".join(pdbs[:8]) + (f" … +{len(pdbs)-8}" if len(pdbs) > 8 else "")
            print(f"       {sym:<3} n={len(pdbs):<3} {shown}")
        print()

    # --- Fe/Mn specifically ---
    femn = [(a, o, m) for a, o, m in conflicts if {"Fe", "Mn"} <= set(m)]
    print(f"=== of those, Fe/Mn disagreements: {len(femn)} ===")
    for acc, org, m in femn:
        print(f"   {acc} ({org}): Fe in {len(m['Fe'])}, Mn in {len(m['Mn'])}")

    # --- non-catalytic metals, the adventitious-metal angle ---
    print(f"\n=== non-catalytic metals modelled in SOD sites: {sum(noncatalytic.values())} atoms ===")
    for sym, n in noncatalytic.most_common():
        print(f"   {sym:<3} {n:>4}")


if __name__ == "__main__":
    main()
