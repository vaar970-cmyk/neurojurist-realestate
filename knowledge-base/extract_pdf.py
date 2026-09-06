import pypdf
import sys

def extract(pdf_path, out_path):
    reader = pypdf.PdfReader(pdf_path)
    n = len(reader.pages)
    with open(out_path, "w", encoding="utf-8") as f:
        for i, page in enumerate(reader.pages):
            try:
                txt = page.extract_text() or ""
            except Exception as e:
                txt = f"[ERROR extracting page {i+1}: {e}]"
            f.write(f"\n===PAGE {i+1}===\n")
            f.write(txt)
    return n

if __name__ == "__main__":
    pdf_path, out_path = sys.argv[1], sys.argv[2]
    n = extract(pdf_path, out_path)
    with open("extract_log.txt", "a", encoding="utf-8") as log:
        log.write(f"{pdf_path}: {n} pages -> {out_path}\n")
    print(n)
