"""
pdf_to_text.py — extract text from a PDF into a plain .txt file, page by page.

Used throughout Phase 3 (novelty auditing), where papers arrive as PDFs and need to be
read and searched. Keeps page markers so anything quoted can be cited by page number.

Usage:
    python scripts/pdf_to_text.py <input.pdf> [output.txt]

If output.txt is omitted, writes alongside the PDF with a .txt extension.
"""

import sys
from pathlib import Path

from pypdf import PdfReader


def pdf_to_text(pdf_path: Path, out_path: Path) -> None:
    reader = PdfReader(str(pdf_path))
    n_pages = len(reader.pages)

    chunks: list[str] = []
    n_empty = 0

    for i, page in enumerate(reader.pages, start=1):
        # extract_text() returns None for pages with no extractable text layer
        # (e.g. a scanned image). Those need OCR, which this script does not do —
        # so count them and report, rather than silently producing a short file.
        text = page.extract_text() or ""
        if not text.strip():
            n_empty += 1
        chunks.append(f"\n\n===== PAGE {i} =====\n\n{text}")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text("".join(chunks), encoding="utf-8")

    print(f"source      : {pdf_path}")
    print(f"output      : {out_path}")
    print(f"pages       : {n_pages}")
    print(f"empty pages : {n_empty}  (>0 means a scanned PDF needing OCR)")
    print(f"characters  : {out_path.stat().st_size:,}")


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1

    pdf_path = Path(sys.argv[1])
    if not pdf_path.is_file():
        print(f"ERROR: no such file: {pdf_path}")
        return 1

    out_path = Path(sys.argv[2]) if len(sys.argv) > 2 else pdf_path.with_suffix(".txt")
    pdf_to_text(pdf_path, out_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
