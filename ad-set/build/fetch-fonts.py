#!/usr/bin/env python3
"""Download Google Fonts webfonts locally so ad renders don't depend on network at paint time."""
import hashlib
import os
import re
import subprocess
import sys

UA = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

FAMILIES = [
    "Oswald:wght@400;500;600;700",
    "Barlow+Condensed:wght@400;500;600;700",
    "Archivo+Black",
    "Inter:wght@400;500;600;700",
]

HERE = os.path.dirname(os.path.abspath(__file__))
FONTDIR = os.path.join(HERE, "fonts")


def curl(url: str, binary: bool):
    out = subprocess.run(
        ["curl", "-sS", "-A", UA, "-m", "30", "--retry", "3", "--retry-delay", "2", url],
        capture_output=True, check=True,
    )
    return out.stdout if binary else out.stdout.decode("utf-8")


def main() -> int:
    os.makedirs(FONTDIR, exist_ok=True)
    css_parts = []
    for fam in FAMILIES:
        css = curl(f"https://fonts.googleapis.com/css2?family={fam}&display=swap", False)
        # Keep only the latin + latin-ext subsets; drop cyrillic/vietnamese to save weight.
        blocks = re.findall(r"(/\*[^*]*\*/\s*)?@font-face\s*\{[^}]*\}", css)
        kept = []
        for block in re.finditer(r"(?:/\*\s*([\w-]+)\s*\*/\s*)?(@font-face\s*\{[^}]*\})", css):
            subset, body = m_sub(block)
            if subset and subset not in ("latin", "latin-ext"):
                continue
            kept.append(body)
        css_parts.append("\n".join(kept) if kept else css)
        print(f"  {fam}: kept {len(kept)}/{len(blocks)} faces", file=sys.stderr)

    combined = "\n".join(css_parts)

    urls = sorted(set(re.findall(r"https://fonts\.gstatic\.com/[^)\s]+", combined)))
    for url in urls:
        name = hashlib.sha1(url.encode()).hexdigest()[:12] + ".woff2"
        path = os.path.join(FONTDIR, name)
        if not os.path.exists(path):
            with open(path, "wb") as fh:
                fh.write(curl(url, True))
        combined = combined.replace(url, f"fonts/{name}")
    print(f"  downloaded {len(urls)} font files", file=sys.stderr)

    with open(os.path.join(HERE, "fonts.css"), "w") as fh:
        fh.write(combined)
    return 0


def m_sub(match):
    return match.group(1), match.group(2)


if __name__ == "__main__":
    raise SystemExit(main())
