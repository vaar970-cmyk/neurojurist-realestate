import re
import sys

FOOTER_RE = re.compile(r'^\d{2}\.\d{2}\.\d{4} Система ГАРАНТ \d+\s*$')
HEADER_RE = re.compile(r'^Гражданский кодекс Российской Федерации \(ГК РФ\)')
GARANT_NOTE_RE = re.compile(r'^ГАРАНТ:')

def clean(path):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()
    out = []
    for line in lines:
        stripped = line.rstrip("\n")
        if FOOTER_RE.match(stripped):
            continue
        if HEADER_RE.match(stripped):
            continue
        if GARANT_NOTE_RE.match(stripped):
            continue
        if stripped.strip() == "(с":
            continue
        out.append(line)
    with open(path, "w", encoding="utf-8") as f:
        f.writelines(out)
    return len(lines), len(out)

for p in sys.argv[1:]:
    before, after = clean(p)
    print(f"{p}: {before} -> {after} строк")
