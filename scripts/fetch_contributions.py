import json
import re
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

USERNAME = "Cherish01-spec"

def fetch_contributions(username: str) -> None:
    url = f"https://github.com/users/{username}/contributions"
    request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

    out_file = Path(__file__).resolve().parent.parent / "data" / "contributions.json"
    out_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        with urlopen(request, timeout=20) as response:
            text = response.read().decode("utf-8", errors="replace")

        days = []
        for match in re.finditer(r'data-date="([^"]+)"\s+data-level="([^"]+)"', text):
            days.append({
                "date": match.group(1),
                "level": int(match.group(2)),
            })

        if not days:
            raise ValueError("No contribution cells found")

        payload = {
            "username": username,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "days": days,
        }
        out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print("Contributions fetched successfully.")
    except Exception as exc:
        print(f"Fetch error: {exc}")
        payload = {
            "username": username,
            "fetched_at": datetime.now(timezone.utc).isoformat(),
            "days": [{"date": f"2026-01-{(i % 28) + 1:02d}", "level": i % 5} for i in range(364)],
            "error": str(exc),
        }
        out_file.write_text(json.dumps(payload, indent=2), encoding="utf-8")

if __name__ == "__main__":
    fetch_contributions(USERNAME)
