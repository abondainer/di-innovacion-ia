#!/usr/bin/env python3
"""Convierte prompts/*.md en assets/prompts.js (fuente única para el curso web)."""
import json, re, pathlib
root = pathlib.Path(__file__).resolve().parent.parent
out = {}
pat = re.compile(r"^### \[(prompt|agente)\] ([\w-]+) · (.+?)\n(?:> (.+?)\n)?\s*```txt\n(.*?)\n```", re.S | re.M)
for f in sorted((root / "prompts").glob("*.md")):
    mod = f.stem
    for m in pat.finditer(f.read_text(encoding="utf-8")):
        kind, pid, title, note, body = m.groups()
        out[pid] = {"tipo": kind, "titulo": title.strip(), "nota": (note or "").strip(),
                    "texto": body, "archivo": f"prompts/{f.name}", "modulo": mod}
(root / "assets" / "prompts.js").write_text("window.DI_PROMPTS = " + json.dumps(out, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
print(f"{len(out)} prompts/agentes → assets/prompts.js")
