import html
from pathlib import Path

def esc(value: str) -> str:
    return html.escape(value, quote=True)

def generate_info_card() -> None:
    lines = [
        {"color": "#c9d1d9", "text": "cherish@github ~ $ neofetch"},
        {"color": "#8b949e", "text": "---------------------------"},
        {"label": "Role", "value": "Full Stack Web Developer & AI Enthusiast"},
        {"label": "Stack", "value": "Java, JavaScript, Python"},
        {"label": "Web Dev", "value": "HTML, CSS, Modern Frameworks"},
        {"label": "AI/Vision", "value": "YOLO, OpenCV, Tkinter"},
        {"label": "Education", "value": "B.Tech CSE @ GIET Bhubaneswar"},
        {"label": "Location", "value": "Bhubaneswar, India"},
        {"label": "Portfolio", "value": "genuine-douhua-26c032.netlify.app"},
        {"label": "Quote", "value": '"Not just writing code, but creating experiences that last."'},
    ]

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="490" height="320" viewBox="0 0 490 320">',
        '<title>Cherish Kumar Satpathy neofetch profile</title>',
        '<style>',
        '  .text { font-family: "Courier New", Courier, monospace; font-size: 14px; }',
        '  .label { fill: #58a6ff; font-weight: bold; }',
        '  .value { fill: #c9d1d9; }',
        '  .line { opacity: 0; animation: slideIn 0.5s ease-out forwards; }',
        '  @keyframes slideIn { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: translateX(0); } }',
        '</style>',
        '<rect width="490" height="320" fill="#0d1117" rx="10"/>',
        '<g transform="translate(20, 40)">',
    ]

    y = 0
    delay = 0.1
    for line in lines:
        if "label" in line:
            svg.append(
                f'<text x="0" y="{y}" class="text line" '
                f'style="animation-delay:{delay:.2f}s;">'
                f'<tspan class="label">{esc(line["label"])}:</tspan> '
                f'<tspan class="value">{esc(line["value"])}</tspan></text>'
            )
        else:
            svg.append(
                f'<text x="0" y="{y}" class="text line" fill="{line["color"]}" '
                f'style="animation-delay:{delay:.2f}s;">{esc(line["text"])}</text>'
            )
        y += 25
        delay += 0.15

    svg.append('</g></svg>')
    out = Path(__file__).resolve().parent.parent / "info-card.svg"
    out.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out}")

if __name__ == "__main__":
    generate_info_card()
