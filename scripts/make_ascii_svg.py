from pathlib import Path
import html

def generate_ascii() -> None:
    ascii_lines = [
        "       .-----------------------.",
        "       |  cherish@dev:~$ _     |",
        "       |                       |",
        "       |  > C O D E            |",
        "       |  > L O G I C          |",
        "       |  > C R E A T I O N    |",
        "       |                       |",
        "       '-----------------------'",
        "           /               \\",
        "          /                 \\",
        "         /                   \\",
        "        '---------------------'",
        "        [Cherish Kumar Satpathy]",
    ]

    svg = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="370" height="320" viewBox="0 0 370 320">',
        '<title>Animated ASCII terminal art for Cherish Kumar Satpathy</title>',
        '<style>',
        '  .bg { fill: #0d1117; }',
        '  .text { font-family: "Courier New", Courier, monospace; font-size: 13px; fill: #58a6ff; font-weight: bold; white-space: pre; }',
        '  .cursor { fill: #39d353; }',
        '</style>',
        '<rect width="100%" height="100%" class="bg" rx="10"/>',
        '<g transform="translate(25, 45)">',
    ]

    y = 0
    delay = 0.2
    for line in ascii_lines:
        safe = html.escape(line)
        svg.append(f'<text x="0" y="{y}" class="text">{safe}</text>')
        svg.append(
            f'<rect x="0" y="{y - 12}" width="320" height="18" fill="#0d1117">'
            f'<animate attributeName="x" from="0" to="320" dur="0.4s" begin="{delay:.2f}s" fill="freeze" />'
            f'</rect>'
        )
        y += 19
        delay += 0.12

    svg.append(
        '<rect x="304" y="1" width="7" height="16" class="cursor" opacity="0.9">'
        '<animate attributeName="opacity" values="1;0;1" dur="0.9s" repeatCount="indefinite" />'
        '</rect>'
    )
    svg.append('</g></svg>')

    out = Path(__file__).resolve().parent.parent / "cherish-ascii.svg"
    out.write_text("\n".join(svg), encoding="utf-8")
    print(f"Generated {out}")

if __name__ == "__main__":
    generate_ascii()
