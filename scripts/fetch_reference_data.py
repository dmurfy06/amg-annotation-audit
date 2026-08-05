"""
fetch_reference_data.py — re-download every third-party file this project depends on.

WHY THIS EXISTS
    The reference data is deliberately NOT committed to the repository:

      - KEGG orthology (data/kegg_ko_list.tsv) is copyrighted by Kanehisa Laboratories.
        Academic use of the REST API is free; bulk REDISTRIBUTION is not permitted without
        a licence, so it must not be republished here.
      - DRAM and VIBRANT source (refs/dram_docs/) is GPL-3.0 and belongs to its authors.
        Vendoring it into an unrelated repo without the licence text would be sloppy at
        best. Fetching it on demand keeps attribution where it belongs.

    Everything below is public and free to download. This script makes the analysis fully
    reproducible without redistributing anyone else's data.

WHAT IT DOES NOT FETCH
    The three published AMG catalogues (ocean/wastewater/soil supplementary files) are
    large publisher-hosted downloads and are listed in PROVENANCE below with their DOIs.
    Retrieve those manually; see 06_project_brief.md.

Usage:
    .venv/Scripts/python.exe scripts/fetch_reference_data.py
    .venv/Scripts/python.exe scripts/fetch_reference_data.py --force   # re-download all
"""

import argparse
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "refs" / "dram_docs"

# PINNED to specific commits, deliberately.
# 07_flag_semantics.md cites this source BY LINE NUMBER (e.g. annotate_vgfs.py:320, where
# the F flag is assigned). Tracking `master` would silently break those citations the next
# time either project commits. Retrieved and verified 2026-08-05.
DRAM_SHA = "fe61d759303f30db058d5d505c448b28e41b03f1"
VIBRANT_SHA = "a718fba5b3b514d7999634ba5ba0a1e8652a9e51"

DRAM_RAW = f"https://raw.githubusercontent.com/WrightonLabCSU/DRAM/{DRAM_SHA}"
VIBRANT_RAW = f"https://raw.githubusercontent.com/AnantharamanLab/VIBRANT/{VIBRANT_SHA}"

# (destination, url, note)
TARGETS = [
    # --- KEGG: free academic REST endpoint, NOT redistributable -------------------
    (DATA / "kegg_ko_list.tsv",
     "https://rest.kegg.jp/list/ko",
     "KEGG orthology list. (c) Kanehisa Laboratories. Do not commit."),

    # --- The two tools' AMG definitions: the object of study ----------------------
    (DATA / "VIBRANT_AMGs.tsv",
     f"{VIBRANT_RAW}/files/VIBRANT_AMGs.tsv",
     "VIBRANT's AMG database: a flat list of KEGG KOs. GPL-3.0."),
    (DATA / "DRAM_amg_database.tsv",
     f"{DRAM_RAW}/data/amg_database.tsv",
     "DRAM's AMG database, with verified/reference columns. GPL-3.0."),

    # --- DRAM-v source: cited by line number in 07_flag_semantics.md -------------
    (DOCS / "annotate_vgfs.py",
     f"{DRAM_RAW}/mag_annotator/annotate_vgfs.py",
     "get_metabolic_flags() — where amg_flags, including F, are assigned."),
    (DOCS / "summarize_vgfs.py",
     f"{DRAM_RAW}/mag_annotator/summarize_vgfs.py",
     "filter_to_amgs() — the default potential-AMG filter."),
    (DOCS / "annotate_bins.py", f"{DRAM_RAW}/mag_annotator/annotate_bins.py", "shared annotation code."),
    (DOCS / "database_processing.py", f"{DRAM_RAW}/mag_annotator/database_processing.py", "database build."),
    (DOCS / "DRAM-v.py", f"{DRAM_RAW}/scripts/DRAM-v.py", "CLI: --remove_fs / --max_auxiliary_score defaults."),

    # --- VIBRANT source ----------------------------------------------------------
    (DOCS / "VIBRANT_annotation.py",
     f"{VIBRANT_RAW}/scripts/VIBRANT_annotation.py",
     "line ~1732: the entire AMG decision, a single list-membership test."),
    (DOCS / "VIBRANT_README.md", f"{VIBRANT_RAW}/README.md", "VIBRANT output description."),
]

WIKI_REPO = "https://github.com/WrightonLabCSU/DRAM.wiki.git"
WIKI_DIR = DOCS / "wiki"


def fetch(dest: Path, url: str, note: str, force: bool) -> str:
    if dest.exists() and not force:
        return f"  skip   {dest.relative_to(ROOT)}  ({dest.stat().st_size:,} bytes)"
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "ProjectAuxiliary/1.0"})
        with urllib.request.urlopen(req, timeout=120) as r:
            body = r.read()
    except (urllib.error.URLError, TimeoutError) as e:
        return f"  FAIL   {dest.relative_to(ROOT)}  <- {url}\n         {e}"
    if not body:
        # An empty 200 is not success. This project has been bitten by that before.
        return f"  FAIL   {dest.relative_to(ROOT)}  <- empty body (HTTP 200 but no content)"
    dest.write_bytes(body)
    return f"  got    {dest.relative_to(ROOT)}  ({len(body):,} bytes)  {note}"


def _force_rmtree(path: Path) -> None:
    """Delete a tree, including git's read-only object files.

    On Windows, git marks files under .git/objects read-only, and shutil.rmtree
    raises PermissionError on them. With ignore_errors=True it fails SILENTLY and
    leaves .git behind, so the subsequent clone dies with 'destination path already
    exists'. Clear the read-only bit and retry instead of ignoring the error.
    """
    import os
    import shutil
    import stat

    def on_error(func, p, _exc):
        os.chmod(p, stat.S_IWRITE)
        func(p)

    if not path.exists():
        return
    try:  # onexc replaced onerror in 3.12
        shutil.rmtree(path, onexc=on_error)
    except TypeError:
        shutil.rmtree(path, onerror=lambda f, p, e: on_error(f, p, e))


def fetch_wiki(force: bool) -> str:
    """DRAM's wiki is a git repo. Clone it, then strip its .git so it does not
    become an embedded repository inside this one (which would make its files
    invisible to anyone cloning Project Auxiliary).

    Note: the wiki has no commit pinning available via a raw URL, so unlike the
    source files above it tracks the wiki's current state. The prose definitions
    quoted in 07_flag_semantics.md are stable; the source line numbers are the
    part that needed pinning.
    """
    import shutil
    import subprocess
    import tempfile

    if WIKI_DIR.exists() and not force:
        return f"  skip   {WIKI_DIR.relative_to(ROOT)}/"

    WIKI_DIR.parent.mkdir(parents=True, exist_ok=True)
    # Clone to a temp dir first, so a failed clone cannot leave the existing
    # copy destroyed and the replacement missing.
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / "wiki"
        try:
            subprocess.run(["git", "clone", "-q", "--depth", "1", WIKI_REPO, str(staged)],
                           check=True, capture_output=True, timeout=180)
        except (subprocess.CalledProcessError, FileNotFoundError, subprocess.TimeoutExpired) as e:
            detail = getattr(e, "stderr", b"") or b""
            return f"  FAIL   wiki clone: {e}\n         {detail.decode(errors='replace').strip()}"
        _force_rmtree(staged / ".git")
        _force_rmtree(WIKI_DIR)
        shutil.move(str(staged), str(WIKI_DIR))

    n = len(list(WIKI_DIR.glob("*.md")))
    return f"  got    {WIKI_DIR.relative_to(ROOT)}/  ({n} pages)  DRAM wiki; flag definitions"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="re-download even if present")
    args = ap.parse_args()

    print("Fetching third-party reference data (not redistributed in this repo).\n")
    results = [fetch(d, u, n, args.force) for d, u, n in TARGETS]
    results.append(fetch_wiki(args.force))
    print("\n".join(results))

    failed = [r for r in results if r.strip().startswith("FAIL")]
    print(f"\n{len(results) - len(failed)}/{len(results)} ok.")
    if failed:
        print("\nSome downloads failed. The analysis scripts will not run without them.")
        return 1
    print("\nLicensing: KEGG data is (c) Kanehisa Laboratories and must not be committed or")
    print("redistributed. DRAM and VIBRANT are GPL-3.0, (c) their respective authors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
