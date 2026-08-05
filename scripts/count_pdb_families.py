"""
count_pdb_families.py — how many PDB structures exist per candidate enzyme family?

Niche N5 proposes auditing the modelling quality (metals, ligands, geometry) of the
deposited structures of ONE enzyme family. That only works if the family has enough
structures to say anything, and few enough to audit on a laptop.

This asks the RCSB PDB search API for entry counts by EC number, plus how many of those
carry a given metal. Counts only — no structures downloaded.

Usage:
    python scripts/count_pdb_families.py
"""

import json
import time
import urllib.request

SEARCH_URL = "https://search.rcsb.org/rcsbsearch/v2/query"

# EC number -> human-readable family name
FAMILIES = {
    "3.5.2.6": "beta-lactamases (incl. metallo-beta-lactamases) - AMR",
    "4.2.1.1": "carbonic anhydrases - Zn",
    "1.15.1.1": "superoxide dismutases - Cu/Zn, Mn, Fe",
    "3.1.3.1": "alkaline phosphatases - Zn/Mg",
    "1.1.1.1": "alcohol dehydrogenases - Zn",
    "3.4.24.-": "metalloendopeptidases - Zn",
    "3.1.3.48": "protein tyrosine phosphatases",
    "2.7.11.1": "protein Ser/Thr kinases (PKA family - ALREADY AUDITED)",
    "3.2.1.17": "lysozyme (ALREADY AUDITED - 1200+ structures)",
    "3.4.23.-": "aspartic proteinases",
    "1.11.1.6": "catalases - haem/Mn",
    "4.6.1.1": "adenylate cyclases",
}

METALS = ["ZN", "MG", "MN", "FE", "CU", "CA", "NI", "CO"]


def rcsb_count(query: dict) -> int:
    """POST a query to the RCSB search API and return the total match count."""
    payload = {
        "query": query,
        "return_type": "entry",
        "request_options": {"return_counts": True},
    }
    req = urllib.request.Request(
        SEARCH_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            body = r.read().decode("utf-8").strip()
    except urllib.error.HTTPError as e:
        if e.code in (204, 404):
            return 0
        raise

    # RCSB answers a zero-match query with 204 No Content and an EMPTY BODY.
    # urllib treats 204 as success, so this never raises — it just returns "".
    # json.loads("") then fails with "Expecting value: line 1 column 1".
    if not body:
        return 0
    return json.loads(body).get("total_count", 0)


def ec_query(ec: str) -> dict:
    return {
        "type": "terminal",
        "service": "text",
        "parameters": {
            "attribute": "rcsb_polymer_entity.rcsb_ec_lineage.id",
            "operator": "exact_match",
            "value": ec,
        },
    }


def ec_with_metal_query(ec: str, metal: str) -> dict:
    return {
        "type": "group",
        "logical_operator": "and",
        "nodes": [
            ec_query(ec),
            {
                "type": "terminal",
                "service": "text",
                "parameters": {
                    "attribute": "rcsb_nonpolymer_entity_container_identifiers.nonpolymer_comp_id",
                    "operator": "exact_match",
                    "value": metal,
                },
            },
        ],
    }


def main() -> None:
    print(f"{'EC':<10} {'entries':>8}   family")
    print("-" * 78)
    results = {}
    for ec, name in FAMILIES.items():
        n = rcsb_count(ec_query(ec))
        results[ec] = n
        print(f"{ec:<10} {n:>8}   {name}")
        time.sleep(0.3)

    print("\n--- metal content of the most promising mid-sized families ---")
    # audit-sized = big enough for statistics, small enough for one person
    candidates = [ec for ec, n in results.items() if 80 <= n <= 1500]
    for ec in candidates:
        parts = []
        for metal in METALS:
            n = rcsb_count(ec_with_metal_query(ec, metal))
            if n:
                parts.append(f"{metal}={n}")
            time.sleep(0.2)
        print(f"{ec:<10} ({results[ec]} entries)  {', '.join(parts) if parts else 'no metals found'}")
        print(f"           {FAMILIES[ec]}")


if __name__ == "__main__":
    main()
