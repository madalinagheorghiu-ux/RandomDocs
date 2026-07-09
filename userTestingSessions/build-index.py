#!/usr/bin/env python3
"""Regenerate index.html from sessions.json.
To add a session: append an entry to sessions.json, then run:  python3 build-index.py
Entry fields: id, title, date, participant, feature, insights, file
"""
import json, datetime, pathlib, re
here = pathlib.Path(__file__).parent
sessions = json.loads((here/"sessions.json").read_text(encoding="utf-8"))
tpl = (here/".index-template.html").read_text(encoding="utf-8")
gen = datetime.date.today().isoformat()
html = tpl.replace("/*__SESSIONS__*/[]", json.dumps(sessions, ensure_ascii=False))
html = html.replace("/*__GENERATED__*/", gen)
(here/"index.html").write_text(html, encoding="utf-8")
print(f"index.html regenerated · {len(sessions)} session(s) · {gen}")
