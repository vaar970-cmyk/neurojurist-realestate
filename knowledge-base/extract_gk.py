import pypdf
import sys

reader = pypdf.PdfReader("raw-sources/gk_polnyi_tekst.pdf")
n = len(reader.pages)
with open("extract_log.txt", "w", encoding="utf-8") as log:
    log.write(f"Total pages: {n}\n")

with open("raw-sources/gk_polnyi_tekst_extracted.txt", "w", encoding="utf-8") as f:
    for i, page in enumerate(reader.pages):
        try:
            txt = page.extract_text() or ""
        except Exception as e:
            txt = f"[ERROR extracting page {i+1}: {e}]"
        f.write(f"\n===PAGE {i+1}===\n")
        f.write(txt)

with open("extract_log.txt", "a", encoding="utf-8") as log:
    log.write("Extraction complete.\n")
