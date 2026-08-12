import json
from pathlib import Path

PALETTE = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353", "#69f0a0"]

def render_heatmap() -> None:
    root = Path(__file__).resolve().parent.parent
    data_file = root / "data" / "contributions.json"
    out_file = root / "contrib-heatmap.svg"

    data = json.loads(data_file.read_text(encoding="utf-8"))
    days = data.get("days", [])
    if not days:
        raise ValueError("Contribution data is empty")

    width, height = 860, 180
    box_size, gap = 11, 4

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<title>GitHub contribution heatmap for Cherish Kumar Satpathy</title>',
        '<style>',
        '  .box { opacity: 0; animation: dropIn 0.8s ease-out forwards; }',
        '  @keyframes dropIn { from { opacity: 0; transform: translateY(-10px); } to { opacity: 1; transform: translateY(0); } }',
        '  .text { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif; font-size: 12px; fill: #8b949e; }',
        '</style>',
        '<rect width="100%" height="100%" fill="#0d1117" rx="10"/>',
        '<g transform="translate(30, 30)">',
    ]

    weeks = [days[i:i + 7] for i in range(0, len(days), 7)]
    for col_idx, week in enumerate(weeks[:53]):
        for row_idx, day in enumerate(week):
            level = max(0, min(int(day.get("level", 0)), len(PALETTE) - 1))
            x = col_idx * (box_size + gap)
            y = row_idx * (box_size + gap)
            delay = (col_idx + row_idx) * 0.02
            svg.append(
                f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" '
                f'fill="{PALETTE[level]}" rx="2" class="box" '
                f'style="animation-delay:{delay:.2f}s;" />'
            )

    svg.append('</g>')
    svg.append('<text x="30" y="150" class="text">Generated live via GitHub Actions | Cherish Kumar Satpathy</text>')
    svg.append('</svg>')
    out_file.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out_file}")

if __name__ == "__main__":
    render_heatmap()
