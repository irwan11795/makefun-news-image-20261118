#!/usr/bin/env python3
"""Generator for news-image-20261118 entry.png (v3 — elderly-readable revision).
'The World's News in One Picture' — Wednesday 18 November 2026 front page.
Drawn with PIL only. Deterministic: identical bytes on every run.

v3 changes (user revision 19 Nov 2026 ~08:10 WIB):
- Bottom fixed: the map + ALSO list no longer cramped at 10px. The ALSO
  list is now 15px with 18px leading in 3 columns; the map is a compact
  band beside the DATE CHECK box instead of eating the whole bottom.
- More stories: 42 -> 55 (13 new briefs, all real 18 Nov 2026 news,
  multi-outlet verified; see NOTES.md). DATE CHECK kept: 17 Nov stories
  stay out.
- Elderly-readable throughout: no tiny text. Grid headlines 13->15px,
  grid summaries 10->12px, lead summaries 12->13px, DATE CHECK 10->12px,
  footer 9->10px, list 10->15px. Grid illustration bands removed (the
  decoration that cost the most space) — a 5px colour bar marks each cell;
  the 3 lead illustrations stay.
Layout follows the proven front-page formula (big serif masthead, stat
strip, 3 illustrated leads, 10 grid stories, schematic world map with
numbered pins, numbered ALSO list, DATE CHECK box, sources footer),
adapted to a 1024x1024 square. All news copy is original wording from web
research of 18 November 2026 (Reuters, AP, AFP, Al Jazeera, NASA, WHO, UN
via multiple outlets) cross-checked against the day's leaderboard feed for
story selection only — no competitor text or code was copied.
"""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1024, 1024
CREAM = (246, 241, 227)
PAPER = (250, 246, 235)
INK = (24, 24, 24)
RED = (176, 32, 32)
NAVY = (16, 36, 74)
BLUE = (31, 78, 156)
GREEN = (30, 122, 52)
ORANGE = (198, 108, 14)
PURPLE = (122, 58, 150)
TEAL = (13, 120, 108)
GREY = (96, 96, 96)
SEA = (168, 200, 220)
SEA_D = (127, 179, 213)
LAND = (233, 221, 193)
SAND = (238, 226, 200)
DARKBAND = (24, 24, 24)
SPACE = (10, 16, 40)

F_DISPLAY = "/usr/share/fonts/truetype/noto/NotoSerifDisplay-Black.ttf"
F_SERIF_B = "/usr/share/fonts/truetype/noto/NotoSerif-Bold.ttf"
F_SERIF = "/usr/share/fonts/truetype/noto/NotoSerif-Regular.ttf"
F_SANS_B = "/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf"
F_SANS = "/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap_text(d, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(d, xy, text, fnt, max_w, fill=INK, leading=None, max_lines=None):
    x, y = xy
    lh = leading or int(fnt.size * 1.18)
    lines = wrap_text(d, text, fnt, max_w)
    if max_lines:
        lines = lines[:max_lines]
    for ln in lines:
        d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def fit_font(path, text, start, max_w, min_size=10):
    """Largest size <= start that fits text in max_w."""
    s = start
    while s > min_size:
        f = font(path, s)
        if ImageDraw.Draw(Image.new("RGB", (8, 8))).textlength(text, font=f) <= max_w:
            return f
        s -= 1
    return font(path, min_size)


def tag_chip(d, x, y, num, label, color):
    """Numbered circle + coloured category tag."""
    r = 8
    d.ellipse([x, y, x + 2 * r, y + 2 * r], fill=color)
    t = str(num)
    f = font(F_SANS_B, 10)
    tw = d.textlength(t, font=f)
    d.text((x + r - tw / 2, y + r - 5), t, font=f, fill=(255, 255, 255))
    f2 = font(F_SANS_B, 12)
    d.text((x + 2 * r + 5, y + 2), label, font=f2, fill=color)
    return 2 * r + 5 + d.textlength(label, font=f2)


# ---------------------------------------------------------------- data
REGIONS = [
    ("EUROPE", 9, BLUE),
    ("MIDDLE EAST", 5, RED),
    ("ASIA", 12, ORANGE),
    ("AFRICA", 6, GREEN),
    ("AMERICAS", 14, PURPLE),
    ("OCEANIA", 5, TEAL),
    ("WORLD", 4, INK),
]

STATS = [
    ("141", "drones fired at Ukraine", INK),
    ("25.9bn km", "Voyager 1's distance out", INK),
    ("55", "factories shut in Bangladesh", RED),
    ("\u20ac45bn", "EU loan for Ukraine", INK),
    ("11,300+", "Ebola cases, DR Congo", RED),
    ("$3,742", "gold settles, a 14-month low", INK),
]

LEADS = [
    dict(n=1, tag="MIDDLE EAST \u00b7 IRAN WAR", color=RED,
         head="Kuwait and Bahrain intercept Iranian drones",
         summ="Iran says it aimed at US forces at Ali Al Salem; US jets struck Qeshm first.",
         ill="gulf", cap="THE GULF \u00b7 DRONES DOWNED, NO HIT REPORTED"),
    dict(n=2, tag="ASIA \u00b7 APEC, CHINA", color=ORANGE,
         head="Xi greets Trump as APEC opens in Shenzhen",
         summ="A first three-way meeting with Putin is set for Thursday.",
         ill="apec", cap="SHENZHEN \u00b7 TRUMP\u2013XI\u2013PUTIN ON THURSDAY"),
    dict(n=3, tag="WORLD \u00b7 SPACE", color=TEAL,
         head="Voyager 1 is one light-day from Earth",
         summ="The first human-made object that far: 25.9bn km, 49 years on.",
         ill="voyager", cap="10:16 GMT \u00b7 A SIGNAL NOW TAKES A DAY"),
]

SMALLS = [
    dict(n=4, tag="GLOBAL \u00b7 CLIMATE", color=TEAL,
         head="COP31 splits over a fossil-fuel phase-out",
         summ="Draft seeks a phase-out; EU envoy warns it may sink talks."),
    dict(n=5, tag="EUROPE \u00b7 UKRAINE AID", color=BLUE,
         head="EU proposes a \u20ac45bn loan for Ukraine in 2027",
         summ="Kyiv repays only if Russia pays reparations, EU says."),
    dict(n=6, tag="MIDDLE EAST \u00b7 GAZA", color=RED,
         head="Board of Peace: Gaza truce may collapse",
         summ="Israeli tanks cross the line; Hamas calls it a breach."),
    dict(n=7, tag="EUROPE \u00b7 UKRAINE WAR", color=BLUE,
         head="Russia fires 141 drones at Ukraine overnight",
         summ="Air force says 126 downed; strikes on Odesa kill four."),
    dict(n=8, tag="ASIA \u00b7 LABOUR", color=ORANGE,
         head="Bangladesh protests shut 55 factories",
         summ="A highway is blocked; police report about 300 arrests."),
    dict(n=9, tag="AFRICA \u00b7 CONFLICT", color=GREEN,
         head="Ethiopia, Eritrea mass troops at border",
         summ="Both armies within striking distance, Reuters sources say."),
    dict(n=10, tag="ASIA \u00b7 WEATHER", color=ORANGE,
         head="Cyclone Akvan nears India's east coast",
         summ="Landfall in Andhra Pradesh due Friday."),
    dict(n=11, tag="OCEANIA \u00b7 CULTURE", color=TEAL,
         head="GTA VI goes on sale at midnight",
         summ="The launch rolls west by time zone, New Zealand first."),
    dict(n=12, tag="OCEANIA \u00b7 DIPLOMACY", color=TEAL,
         head="Australia sanctions settler leader Weiss",
         summ="With the UK, it targets West Bank settler violence."),
    dict(n=13, tag="EUROPE \u00b7 ECONOMY", color=BLUE,
         head="UK inflation climbs to 3.6%, a one-year high",
         summ="Fuel lifts the UK to 3.6%; euro area 4.0%."),
]

# (number, region colour, text) — one line each at 15px, 3 columns x 14 rows.
BRIEFS = [
    (14, PURPLE, "Fed minutes signal more rate rises"),
    (15, PURPLE, "Gold sinks below $3,800 an ounce"),
    (16, RED, "Riyadh downs a Houthi cruise missile"),
    (17, BLUE, "UK sanctions eight settler builders"),
    (18, BLUE, "Berlin: coalition to cut power tax"),
    (19, ORANGE, "Tokyo: sixth trade deficit in a row"),
    (20, ORANGE, "Seoul: Lee seeks China's help on North"),
    (21, ORANGE, "Manila: Trump hails Philippine trade deal"),
    (22, ORANGE, "Beijing: Tencent revenue rises 8%"),
    (23, PURPLE, "Washington: NSA outage, no attack seen"),
    (24, PURPLE, "Ottawa: Carney plays down Trump row"),
    (25, PURPLE, "Lima: M5.9 quake, no damage reported"),
    (26, GREEN, "Amnesty: RSF drones killed 37 in El Obeid"),
    (27, GREEN, "Sudan: dig reaches Old Dongola church"),
    (28, GREEN, "Pretoria: inflation jumps to 5.2%"),
    (29, RED, "Baghdad: militia refuses to leave base"),
    (30, PURPLE, "Caracas: Hegseth seals defence pact"),
    (31, ORANGE, "Da Nang: Russian bombers park at base"),
    (32, TEAL, "Port Moresby: M6.0 quake strikes PNG"),
    (33, TEAL, "Sydney: Tame Impala sweeps ARIAs"),
    (34, BLUE, "Bucharest: M5.3 quake shakes Romania"),
    (35, BLUE, "Skopje: Mossad tip foils 'Iran plot'"),
    (36, ORANGE, "Bangkok: director jailed over tower fall"),
    (37, ORANGE, "Lahore: world's most polluted city again"),
    (38, ORANGE, "Kuala Lumpur: ringgit at five-month low"),
    (39, PURPLE, "Cincinnati: USA beat Haiti 2-0"),
    (40, PURPLE, "Monterrey: Mexico edge Jamaica 2-1"),
    (41, GREEN, "Johannesburg: water curbs tighten"),
    (42, INK, "Oil: Brent falls 1.4% to $91.82"),
    (43, PURPLE, "US loses measles-free status"),
    (44, PURPLE, "Waymo pulls cars off US freeways"),
    (45, PURPLE, "Waller floats a 50bp December hike"),
    (46, PURPLE, "Dow falls 1.11%, a third straight loss"),
    (47, PURPLE, "Target posts best sales in five years"),
    (48, PURPLE, "Anthropic IPO prices on strong demand"),
    (49, INK, "Dollar hits a 19-month high"),
    (50, TEAL, "Cat 5 Cyclone Xavier hits Cook Islands"),
    (51, GREEN, "EU states plan migrant hubs in Rwanda"),
    (52, BLUE, "UK energy price cap to rise 26% in Jan"),
    (53, BLUE, "EU approves Indonesia trade deal"),
    (54, ORANGE, "Kospi jumps 1.99%, leads Asian markets"),
    (55, RED, "WHO: 950,000 Gazans face floods"),
]

# Map pins: (story n, lon, lat, region colour). Equirectangular.
# Pin 3 (Voyager 1) is off the map — noted in the legend instead.
PINS = [
    (1, 47.9, 29.3, RED), (2, 114.1, 22.5, ORANGE),
    (4, 30.7, 36.9, TEAL), (5, 4.35, 50.85, BLUE),
    (6, 34.45, 31.5, RED), (7, 30.5, 50.45, BLUE),
    (8, 90.4, 23.8, ORANGE), (9, 38.9, 15.3, GREEN),
    (10, 82.0, 16.0, ORANGE), (11, 174.8, -36.8, TEAL),
    (12, 149.1, -35.3, TEAL), (13, -0.1, 51.5, BLUE),
]

DATE_CHECK = ("DATE CHECK \u2014 Left out on purpose because they were first reported on "
              "Tuesday 17 November, not today: the Kerch Bridge road span collapse, "
              "Nvidia's $115.8bn quarter, Peltola's Alaska Senate win, Mongolia's "
              "president resigning, the Prague train crash, the Knesset speaker vote.")

# ------------------------------------------------------- illustrations
def _label(d, x, y, text, size=9, fill=INK, bold=True, bg=None):
    f = font(F_SANS_B if bold else F_SANS, size)
    if bg is not None:
        w = d.textlength(text, font=f) + 8
        d.rectangle([x, y, x + w, y + size + 6], fill=bg)
        d.text((x + 4, y + 3), text, font=f, fill=fill)
    else:
        d.text((x, y), text, font=f, fill=fill)


def ill_gulf(d, x, y, w, h):
    """The Gulf: Iran top-right, Kuwait/Bahrain left, dashed drone route,
    smoking tanker in Hormuz."""
    d.rectangle([x, y, x + w, y + h], fill=SAND)
    d.polygon([(x, y + int(h * 0.34)), (x + w, y + int(h * 0.16)),
               (x + w, y + int(h * 0.78)), (x, y + int(h * 0.90))], fill=SEA)
    # dashed red route Iran -> Kuwait
    rx0, ry0, rx1, ry1 = x + int(w * 0.58), y + 12, x + int(w * 0.24), y + int(h * 0.58)
    steps = 9
    for i in range(steps):
        t0, t1 = i / steps, (i + 0.55) / steps
        d.line([rx0 + (rx1 - rx0) * t0, ry0 + (ry1 - ry0) * t0,
                rx0 + (rx1 - rx0) * t1, ry0 + (ry1 - ry0) * t1], fill=RED, width=2)
    d.text((x + int(w * 0.22), y + int(h * 0.40)), "X", font=font(F_SANS_B, 14), fill=RED)
    d.text((x + int(w * 0.34), y + int(h * 0.52)), "X", font=font(F_SANS_B, 14), fill=RED)
    # drone silhouettes
    for dx, dy in ((x + int(w * 0.48), y + 22), (x + int(w * 0.38), y + 34)):
        d.polygon([(dx, dy), (dx + 18, dy + 3), (dx, dy + 6)], fill=INK)
    # tanker bottom-right, smoking
    tx, ty = x + int(w * 0.78), y + int(h * 0.62)
    d.rectangle([tx, ty, tx + 46, ty + 12], fill=(40, 40, 40))
    d.rectangle([tx + 8, ty - 8, tx + 16, ty], fill=(40, 40, 40))
    for ox, oy, r in ((0, -14, 6), (7, -20, 8), (15, -14, 6)):
        d.ellipse([tx + 18 + ox - r, ty + oy - r, tx + 18 + ox + r, ty + oy + r], fill=(120, 120, 120))
    _label(d, x + int(w * 0.44), y + 4, "IRAN", 9, INK)
    _label(d, x + 6, y + int(h * 0.60), "KUWAIT", 9, INK)
    _label(d, x + 6, y + int(h * 0.74), "BAHRAIN", 9, INK)
    _label(d, x + int(w * 0.60), y + int(h * 0.28), "QESHM", 9, INK)
    _label(d, x + w - 56, y + h - 16, "HORMUZ", 9, INK)
    _label(d, x + 6, y + 4, "DRONES DOWNED", 9, (255, 255, 255), bg=RED)


def _flag_cn(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
    cx, cy = x + int(w * 0.22), y + int(h * 0.28)
    for ox, oy, r in ((0, 0, 5), (12, 3, 2), (10, 9, 2), (3, 11, 2), (-3, 6, 2)):
        d.ellipse([cx + ox - r, cy + oy - r, cx + ox + r, cy + oy + r], fill=(255, 222, 0))


def _flag_us(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    for i in range(0, 7, 2):
        d.rectangle([x, y + i * h // 7, x + w, y + (i + 1) * h // 7], fill=(176, 32, 32))
    d.rectangle([x, y, x + int(w * 0.42), y + int(h * 0.57)], fill=NAVY)


def _flag_ru(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h // 3], fill=(255, 255, 255))
    d.rectangle([x, y + h // 3, x + w, y + 2 * h // 3], fill=(0, 57, 166))
    d.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(213, 0, 50))


def ill_apec(d, x, y, w, h):
    """APEC Shenzhen: skyline, plane on the tarmac, three flags."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 228, 240))
    # skyline
    for bx, bw, bh in ((0, 34, 44), (40, 26, 60), (72, 30, 38), (108, 22, 52),
                       (136, 34, 70), (176, 26, 46), (208, 30, 58), (244, 28, 40),
                       (278, 34, 48)):
        d.rectangle([x + bx, y + h - 34 - bh, x + bx + bw, y + h - 34], fill=(70, 95, 130))
        for wy in range(y + h - 34 - bh + 6, y + h - 38, 12):
            for wx in range(x + bx + 5, x + bx + bw - 4, 9):
                d.rectangle([wx, wy, wx + 4, wy + 5], fill=(255, 235, 150))
    # tarmac
    d.rectangle([x, y + h - 34, x + w, y + h], fill=(90, 90, 90))
    d.rectangle([x, y + h - 34, x + w, y + h - 30], fill=(255, 255, 255))
    # plane
    px, py = x + 18, y + h - 66
    d.ellipse([px, py, px + 92, py + 16], fill=(255, 255, 255))
    d.polygon([(px + 88, py + 4), (px + 118, py + 8), (px + 88, py + 12)], fill=(255, 255, 255))
    d.polygon([(px + 20, py - 12), (px + 34, py - 12), (px + 30, py + 2)], fill=(200, 40, 40))
    d.rectangle([px + 8, py + 4, px + 40, py + 8], fill=NAVY)
    # three flags on poles, right
    for i, (fn, name) in enumerate([(_flag_cn, "CHINA"), (_flag_us, "USA"), (_flag_ru, "RUSSIA")]):
        fx = x + w - 150 + i * 50
        d.rectangle([fx, y + 10, fx + 2, y + 52], fill=(60, 60, 60))
        fn(d, fx + 2, y + 10, 40, 26)
        nf = font(F_SANS_B, 8)
        d.text((fx + 2, y + 40), name, font=nf, fill=INK)
    _label(d, x + 6, y + 4, "APEC \u00b7 SHENZHEN", 9, (255, 255, 255), bg=ORANGE)


def ill_voyager(d, x, y, w, h):
    """Deep space: Earth bottom-left, dashed light-day line, Voyager probe."""
    d.rectangle([x, y, x + w, y + h], fill=SPACE)
    for sx, sy, r in ((20, 14, 1), (60, 8, 2), (110, 20, 1), (160, 10, 1), (210, 16, 2),
                      (260, 8, 1), (300, 22, 1), (40, 44, 1), (140, 40, 2), (240, 44, 1),
                      (90, 60, 1), (190, 58, 1), (280, 60, 2), (30, 80, 2), (120, 84, 1)):
        d.ellipse([x + sx - r, y + sy - r, x + sx + r, y + sy + r], fill=(255, 255, 255))
    # Earth
    ex, ey, er = x + 34, y + h - 26, 22
    d.ellipse([ex - er, ey - er, ex + er, ey + er], fill=(40, 110, 200))
    d.ellipse([ex - 12, ey - 14, ex + 2, ey - 2], fill=(40, 160, 90))
    d.ellipse([ex - 2, ey + 4, ex + 14, ey + 14], fill=(40, 160, 90))
    d.ellipse([ex - er, ey - er, ex + er, ey + er], outline=(140, 190, 240), width=1)
    # dashed light-day line Earth -> probe
    px0, py0 = ex + 16, ey - 14
    px1, py1 = x + w - 52, y + 26
    steps = 14
    for i in range(steps):
        t0, t1 = i / steps, (i + 0.5) / steps
        d.line([px0 + (px1 - px0) * t0, py0 + (py1 - py0) * t0,
                px0 + (px1 - px0) * t1, py0 + (py1 - py0) * t1], fill=(255, 220, 100), width=2)
    # Voyager probe: bus + dish + boom
    qx, qy = x + w - 52, y + 26
    d.rectangle([qx - 6, qy - 4, qx + 6, qy + 4], fill=(200, 200, 200))
    d.polygon([(qx + 6, qy - 10), (qx + 22, qy - 2), (qx + 6, qy + 6)], fill=(230, 230, 230))
    d.line([qx - 6, qy, qx - 24, qy - 8], fill=(180, 180, 180), width=2)
    d.ellipse([qx - 27, qy - 11, qx - 21, qy - 5], fill=(255, 220, 100))
    _label(d, x + 6, y + 4, "EARTH", 9, (255, 255, 255), bg=NAVY)
    _label(d, x + w - 108, y + h - 20, "1 LIGHT-DAY", 9, (255, 255, 255), bg=TEAL)


# ------------------------------------------------------------- map
CONTINENTS = [
    [(3, 18), (12, 8), (28, 6), (38, 12), (40, 22), (30, 26), (28, 34), (18, 36), (8, 32), (2, 26)],
    [(40, 6), (46, 4), (48, 10), (42, 12)],
    [(28, 40), (36, 38), (42, 44), (40, 56), (34, 66), (28, 58), (26, 48)],
    [(46, 16), (54, 10), (62, 12), (60, 20), (52, 22), (46, 20)],
    [(46, 30), (58, 28), (64, 34), (62, 48), (56, 62), (50, 58), (46, 44), (44, 36)],
    [(62, 10), (85, 8), (98, 14), (96, 26), (88, 30), (84, 38), (76, 36), (70, 28), (64, 22)],
    [(84, 40), (90, 42), (88, 46)],
    [(82, 52), (94, 50), (96, 58), (88, 62), (82, 58)],
]


def draw_map(d, box):
    x0, y0, x1, y1 = box
    d.rectangle(box, fill=(214, 228, 238))
    w, h = x1 - x0, y1 - y0
    for poly in CONTINENTS:
        pts = [(x0 + px / 100 * w, y0 + py / 100 * h) for px, py in poly]
        d.polygon(pts, fill=LAND, outline=(170, 155, 120))
    for gx in (25, 50, 75):
        d.line([x0 + gx / 100 * w, y0, x0 + gx / 100 * w, y1], fill=(190, 205, 220), width=1)
    for n, lon, lat, color in PINS:
        px = x0 + (lon + 180) / 360 * w
        py = y0 + (90 - lat) / 180 * h
        r = 7 if n <= 2 else 6
        fill = RED if n <= 2 else NAVY
        d.ellipse([px - r, py - r, px + r, py + r], fill=fill, outline=(255, 255, 255), width=1)
        f = font(F_SANS_B, 8 if n <= 2 else 7)
        t = str(n)
        tw = d.textlength(t, font=f)
        th = 8 if n <= 2 else 7
        d.text((px - tw / 2, py - th / 2 - 1), t, font=f, fill=(255, 255, 255))

# ------------------------------------------------------------- layout
def build():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([8, 8, W - 9, H - 9], fill=PAPER, outline=INK, width=2)
    X0, X1 = 22, W - 22  # content margins
    dbg = {}

    # ---- kicker row
    f_kick = font(F_SANS_B, 13)
    d.text((X0, 16), "THE WORLD\u2019S NEWS IN ONE PICTURE", font=f_kick, fill=RED)
    f_kick2 = font(F_SANS_B, 11)
    t2 = "55 STORIES \u00b7 6 CONTINENTS \u00b7 ALL FROM WEDNESDAY"
    d.text((X1 - d.textlength(t2, font=f_kick2), 18), t2, font=f_kick2, fill=INK)

    # ---- masthead
    title = "Wednesday 18 November 2026"
    f_title = fit_font(F_DISPLAY, title, 52, X1 - X0)
    tw = d.textlength(title, font=f_title)
    d.text(((W - tw) / 2, 28), title, font=f_title, fill=INK)
    d.line([X0, 88, X1, 88], fill=INK, width=3)
    d.line([X0, 93, X1, 93], fill=INK, width=1)

    # ---- region strip (widths proportional to story counts)
    y_reg, reg_h = 99, 19
    total = sum(c for _, c, _ in REGIONS)
    rx = X0
    f_reg = font(F_SANS_B, 11)
    for name, cnt, col in REGIONS:
        seg_w = (X1 - X0) * cnt / total
        d.rectangle([rx, y_reg, rx + seg_w, y_reg + reg_h], fill=col)
        lab = "%s %d" % (name, cnt)
        lw = d.textlength(lab, font=f_reg)
        d.text((rx + (seg_w - lw) / 2, y_reg + 3), lab, font=f_reg, fill=(255, 255, 255))
        rx += seg_w

    # ---- stats strip
    y_stats = 124
    cell_w = (X1 - X0) / 6
    f_num = font(F_SERIF_B, 18)
    f_lab = font(F_SANS, 10)
    for i, (num, lab, col) in enumerate(STATS):
        cx = X0 + i * cell_w
        nw = d.textlength(num, font=f_num)
        d.text((cx + (cell_w - nw) / 2, y_stats), num, font=f_num, fill=col)
        lw = d.textlength(lab, font=f_lab)
        d.text((cx + (cell_w - lw) / 2, y_stats + 23), lab, font=f_lab, fill=GREY)
        if i:
            d.line([cx, y_stats + 2, cx, y_stats + 36], fill=(200, 190, 170), width=1)
    d.line([X0, 164, X1, 164], fill=(200, 190, 170), width=1)

    # ---- 3 lead stories
    lead_y, lead_h_ill = 172, 100
    col_w = (X1 - X0 - 2 * 10) / 3
    for i, s in enumerate(LEADS):
        cx = X0 + i * (col_w + 10)
        globals()["ill_" + s["ill"]](d, int(cx), lead_y, int(col_w), lead_h_ill)
        d.rectangle([cx, lead_y + lead_h_ill, cx + col_w, lead_y + lead_h_ill + 14], fill=DARKBAND)
        f_cap = font(F_SANS_B, 10)
        ct = s["cap"]
        d.text((cx + (col_w - d.textlength(ct, font=f_cap)) / 2, lead_y + lead_h_ill + 2),
               ct, font=f_cap, fill=(255, 255, 255))
        ty = lead_y + lead_h_ill + 20
        tag_chip(d, int(cx), int(ty), s["n"], s["tag"], s["color"])
        hy = ty + 22
        hy = draw_wrapped(d, (cx, hy), s["head"], font(F_SERIF_B, 20), col_w,
                          leading=22, max_lines=2)
        draw_wrapped(d, (cx, hy + 4), s["summ"], font(F_SERIF, 13), col_w,
                     fill=(60, 60, 60), leading=15, max_lines=2)
    dbg["leads_end"] = lead_y + lead_h_ill + 20 + 22 + 44 + 4 + 30

    # ---- grid stories 4-13 (5 cols x 2 rows, no illustration bands in v3)
    grid_y = 398
    gcol = (X1 - X0 - 4 * 8) / 5
    grow_h, grow_gap = 94, 6
    for i, s in enumerate(SMALLS):
        r, c = divmod(i, 5)
        cx = X0 + c * (gcol + 8)
        cy = grid_y + r * (grow_h + grow_gap)
        d.rectangle([cx, cy, cx + gcol, cy + 5], fill=s["color"])
        ty = cy + 9
        rr = 7
        d.ellipse([cx, ty, cx + 2 * rr, ty + 2 * rr], fill=s["color"])
        f_n = font(F_SANS_B, 9)
        t = str(s["n"])
        d.text((cx + rr - d.textlength(t, font=f_n) / 2, ty + rr - 5), t, font=f_n,
               fill=(255, 255, 255))
        f_t = font(F_SANS_B, 11)
        d.text((cx + 2 * rr + 4, ty + 2), s["tag"], font=f_t, fill=s["color"])
        hy = ty + 18
        hy = draw_wrapped(d, (cx, hy), s["head"], font(F_SERIF_B, 15), gcol,
                          leading=17, max_lines=2)
        draw_wrapped(d, (cx, hy + 2), s["summ"], font(F_SANS, 12), gcol,
                     fill=(60, 60, 60), leading=14, max_lines=2)
    dbg["grid_end"] = grid_y + 2 * grow_h + grow_gap

    # ---- band: DATE CHECK (left) + compact map (right)
    band_y = 596
    dc_x1 = 630
    f_dc = font(F_SANS, 12)
    f_dcb = font(F_SANS_B, 12)
    lab = "DATE CHECK \u2014 "
    rest = DATE_CHECK[len("DATE CHECK \u2014 "):]
    lines = wrap_text(d, rest, f_dc, (dc_x1 - X0 - 16 - d.textlength(lab, font=f_dcb)))
    dc_h = 10 + len(lines) * 15 + 4
    # re-wrap first line to sit beside the bold label
    first = wrap_text(d, rest, f_dc, (dc_x1 - X0 - 16 - d.textlength(lab, font=f_dcb)))
    dc_lines = first
    dc_h = 8 + 15 * len(dc_lines) + 6
    d.rectangle([X0, band_y, dc_x1, band_y + dc_h], outline=RED, width=1)
    d.rectangle([X0, band_y, X0 + 4, band_y + dc_h], fill=RED)
    dx, dy = X0 + 10, band_y + 4
    d.text((dx, dy), lab, font=f_dcb, fill=RED)
    lw = d.textlength(lab, font=f_dcb)
    for j, ln in enumerate(dc_lines):
        if j == 0:
            d.text((dx + lw, dy), ln, font=f_dc, fill=INK)
        else:
            d.text((dx, dy + j * 15), ln, font=f_dc, fill=INK)
    # legend under the DATE CHECK box
    f_leg = font(F_SANS, 11)
    leg_y = band_y + dc_h + 8
    d.text((X0, leg_y), "Red 1\u20132 leads \u00b7 Navy 4\u201313 \u00b7 3 Voyager 1: off the map",
           font=f_leg, fill=GREY)
    # compact map, right side, header chip overlaid
    map_box = (646, band_y, X1, band_y + 100)
    draw_map(d, map_box)
    _label(d, map_box[0] + 6, map_box[1] + 4, "WHERE IT HAPPENED", 9,
           (255, 255, 255), bg=RED)
    dbg["band_end"] = max(band_y + dc_h, map_box[3])

    # ---- ALSO list: 3 columns x 14 rows, 15px (v3 — was 10px in v1)
    f_sec = font(F_SANS_B, 14)
    also_y = 708
    d.text((X0, also_y), "ALSO ON WEDNESDAY 18 NOVEMBER", font=f_sec, fill=RED)
    f_bnum = font(F_SANS_B, 15)
    f_btxt = font(F_SANS, 15)
    col_w2 = (X1 - X0 - 2 * 14) / 3
    list_y0 = also_y + 22
    list_lead = 18
    for i, (n, color, text) in enumerate(BRIEFS):
        col = i // 14
        row = i % 14
        bx = X0 + col * (col_w2 + 14)
        by = list_y0 + row * list_lead
        d.text((bx, by), str(n), font=f_bnum, fill=color)
        d.text((bx + 26, by), text, font=f_btxt, fill=INK)
    dbg["list_end"] = list_y0 + 14 * list_lead

    # ---- footer
    foot_y = dbg["list_end"] + 8
    d.line([X0, foot_y, X1, foot_y], fill=INK, width=1)
    f_f = font(F_SANS, 10)
    left = "Every story here happened or was first reported on Wednesday 18 November 2026. Contested claims are attributed."
    right = "Sources: Reuters, AP, AFP, Al Jazeera, NASA, WHO, UN. Original drawings."
    d.text((X0, foot_y + 6), left, font=f_f, fill=GREY)
    d.text((X1 - d.textlength(right, font=f_f), foot_y + 6), right, font=f_f, fill=GREY)
    dbg["footer_end"] = foot_y + 6 + 10
    return img, dbg


if __name__ == "__main__":
    import os
    img, dbg = build()
    print("sections:", dbg)
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, optimize=True)
    print("saved", out, os.path.getsize(out), "bytes", img.size)
    prev = os.path.join(os.path.dirname(os.path.abspath(__file__)), "preview-300.png")
    img.resize((300, 300), Image.LANCZOS).save(prev, optimize=True)
    print("preview", prev, os.path.getsize(prev), "bytes")
    # ---- fit checks: every wrapped block must fit its allotted lines
    d = ImageDraw.Draw(Image.new("RGB", (8, 8)))
    gcol = (1002 - 22 - 4 * 8) / 5
    bad = 0
    for s in SMALLS:
        hl = wrap_text(d, s["head"], font(F_SERIF_B, 15), gcol)
        sl = wrap_text(d, s["summ"], font(F_SANS, 12), gcol)
        if len(hl) > 2 or len(sl) > 2:
            print("OVERFLOW grid", s["n"], "head", len(hl), "summ", len(sl))
            bad += 1
    col_w2 = (1002 - 22 - 2 * 14) / 3
    for n, color, text in BRIEFS:
        w = d.textlength(str(n), font=font(F_SANS_B, 15)) + 8 + d.textlength(text, font=font(F_SANS, 15))
        if w > col_w2:
            print("OVERFLOW brief", n, round(w), ">", round(col_w2), text)
            bad += 1
    print("fit check:", "OK" if bad == 0 else "%d OVERFLOW(S)" % bad)
