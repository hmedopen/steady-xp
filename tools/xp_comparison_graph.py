from pathlib import Path
import sys

W, H = 1400, 1000
COST = max(1, int(sys.argv[1])) if len(sys.argv) > 1 else 100
MAX_LEVEL = max(1, int(sys.argv[2])) if len(sys.argv) > 2 else 150

def total(n):
    return n*n + 6*n if n <= 16 else (2.5*n*n - 40.5*n + 360 if n <= 31 else 4.5*n*n - 162.5*n + 2220)

def next_xp(n):
    return 2*n + 7 if n <= 15 else (5*n - 38 if n <= 30 else 9*n - 158)

def points(values, left, top, width, height, ymax):
    return " ".join(f"{left + n/MAX_LEVEL*width:.1f},{top + height - v/ymax*height:.1f}" for n, v in enumerate(values))

levels = range(MAX_LEVEL + 1)
vanilla_total = [total(n) for n in levels]
steady_total = [COST*n for n in levels]
vanilla_next = [next_xp(n) for n in levels]
steady_next = [COST for _ in levels]
total_crossover = next(n for n in range(1, MAX_LEVEL + 1) if total(n) > COST*n)
next_crossover = next(n for n in range(MAX_LEVEL + 1) if next_xp(n) > COST)

left, width, height = 115, 1215, 315
total_max = ((max(vanilla_total + steady_total) + 999) // 1000) * 1000
next_max = ((max(vanilla_next + steady_next) + 99) // 100) * 100
panels = [(115, total_max, vanilla_total, steady_total, "Total XP required to reach each level", "Total XP from level 0"),
          (585, next_max, vanilla_next, steady_next, "XP needed to advance one level", "XP for next level")]

s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
     '<rect width="100%" height="100%" fill="#10151c"/>',
     '<style>text{font-family:Segoe UI,Arial,sans-serif;fill:#e6edf3}.axis{stroke:#8b949e;stroke-width:1}.grid{stroke:#52606d;stroke-opacity:.3}.orange{stroke:#ff9f43}.green{stroke:#55efc4}</style>',
     f'<text x="700" y="48" text-anchor="middle" font-size="28" font-weight="700">Vanilla XP vs Steady XP ({COST} XP per level)</text>']

for top, ymax, vanilla, steady, title, ylabel in panels:
    s.append(f'<rect x="70" y="{top-45}" width="1290" height="410" rx="12" fill="#151d27"/>')
    s.append(f'<text x="700" y="{top-12}" text-anchor="middle" font-size="20" font-weight="600">{title}</text>')
    tick_step = 5 if MAX_LEVEL <= 50 else 10
    for i in range(0, MAX_LEVEL + 1, tick_step):
        x = left + i/MAX_LEVEL*width
        s.append(f'<line class="grid" x1="{x}" y1="{top}" x2="{x}" y2="{top+height}"/><text x="{x}" y="{top+340}" text-anchor="middle" font-size="12">{i}</text>')
    for j in range(6):
        y = top + height - j/5*height
        val = int(ymax*j/5)
        s.append(f'<line class="grid" x1="{left}" y1="{y}" x2="{left+width}" y2="{y}"/><text x="{left-12}" y="{y+4}" text-anchor="end" font-size="12">{val:,}</text>')
    s.append(f'<polyline points="{points(vanilla,left,top,width,height,ymax)}" fill="none" class="orange" stroke-width="4"/>')
    s.append(f'<polyline points="{points(steady,left,top,width,height,ymax)}" fill="none" class="green" stroke-width="4"/>')
    s.append(f'<text x="{left+18}" y="{top+27}" class="orange" font-size="15">● Vanilla</text><text x="{left+120}" y="{top+27}" class="green" font-size="15">● Steady XP</text>')
    s.append(f'<text x="28" y="{top+height/2}" transform="rotate(-90 28 {top+height/2})" text-anchor="middle" font-size="14">{ylabel}</text>')

s += [f'<text x="722" y="965" text-anchor="middle" font-size="15">Current level (0–{MAX_LEVEL})</text>',
      f'<text x="970" y="270" font-size="15" fill="#e6edf3">Steady XP becomes cheaper overall at level {total_crossover}</text>',
      f'<text x="500" y="745" font-size="15" fill="#e6edf3">Vanilla next-level cost passes {COST} XP at level {next_crossover}</text>', '</svg>']

output = Path("docs/charts") / f"xp_comparison_{COST}xp_level_{MAX_LEVEL}.svg"
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text("\n".join(s), encoding="utf-8")
print(output)
