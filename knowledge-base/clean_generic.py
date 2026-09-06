import re
import sys

FOOTER_RE = re.compile(r'^\d{2}\.\d{2}\.\d{4} Система ГАРАНТ \d+\s*$')
GARANT_NOTE_RE = re.compile(r'^ГАРАНТ:')
GK_HEADER_RE = re.compile(r'^Гражданский кодекс Российской Федерации \(ГК РФ\)')

def clean(path, header_prefix=None):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    out = []
    for line in lines:
        stripped = line.rstrip("\n")
        if FOOTER_RE.match(stripped):
            continue
        if GARANT_NOTE_RE.match(stripped):
            continue
        if GK_HEADER_RE.match(stripped):
            continue
        if header_prefix and stripped.startswith(header_prefix):
            continue
        if stripped.strip() in ("(с", ""):
            # keep blank lines mostly, but drop stray "(с" continuation
            if stripped.strip() == "(с":
                continue
        out.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    return len(lines), len(out)

if __name__ == "__main__":
    path = sys.argv[1]
    header_prefix = sys.argv[2] if len(sys.argv) > 2 else None
    before, after = clean(path, header_prefix)
    print(f"{before} -> {after}")
