#!/usr/bin/env python3
"""Update the small JSON payload consumed by the homepage citation card."""
import datetime as dt
import json
import re
import sys
import urllib.request
from pathlib import Path

SCHOLAR_ID = "_eZWcIMAAAAJ"
out = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
data_file = out / "gs_data.json"
try:
    data = json.loads(data_file.read_text())
except Exception:
    data = {"publications": {}}

url = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en&pagesize=100"
request = urllib.request.Request(url, headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/124 Safari/537.36"
})
try:
    html = urllib.request.urlopen(request, timeout=25).read().decode("utf-8", "replace")
    stats = [int(x) for x in re.findall(r'gsc_rsb_std">\s*([0-9,]+)', html)[:6]]
    if len(stats) < 5:
        raise RuntimeError("Scholar metrics were not present")
    years = re.findall(r'class="gsc_g_t"[^>]*>\s*(\d{4})', html)
    counts = re.findall(r'class="gsc_g_al"[^>]*>\s*([0-9,]+)', html)
    data.update({
        "name": "Zhekai Chen",
        "citedby": stats[0],
        "hindex": stats[2],
        "i10index": stats[4],
        "cites_per_year": {year: int(value.replace(",", "")) for year, value in zip(years, counts)},
        "updated": dt.datetime.now(dt.timezone.utc).date().isoformat(),
    })
except Exception as exc:
    print(f"Scholar refresh skipped; keeping last published data: {exc}")

out.mkdir(parents=True, exist_ok=True)
data_file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
(out / "gs_data_shieldsio.json").write_text(json.dumps({
    "schemaVersion": 1, "label": "citations", "message": str(data.get("citedby", "—"))
}) + "\n")

history_file = out / "gs_data_history.json"
try:
    history_payload = json.loads(history_file.read_text())
except Exception:
    history_payload = {"history": []}
today = dt.datetime.now(dt.timezone.utc).date().isoformat()
history = [x for x in history_payload.get("history", []) if x.get("date") != today]
if isinstance(data.get("citedby"), int):
    history.append({"date": today, "citations": data["citedby"]})
history_file.write_text(json.dumps({"history": sorted(history, key=lambda x: x["date"]), "updated": today}, indent=2) + "\n")
