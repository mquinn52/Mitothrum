#!/usr/bin/env python3
"""Render one vertical (1080x1920) social video per product from products.json.
Text-and-motion only (no product imagery), brand colors, platform safe areas,
an on-screen affiliate disclosure for the whole video, and a silent audio
track so every platform accepts the upload. Usage: render.py OUTDIR [slug...]"""
import json, math, os, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont

W, H, FPS = 1080, 1920, 30
ESPRESSO = np.array([23, 17, 12], float); AMBER = np.array([201, 160, 92], float)
CREAM = (247, 241, 230); AMBER_T = (228, 203, 147); MUTED = (185, 168, 136)
F = "/usr/share/fonts/opentype/inter/"
def font(name, size): return ImageFont.truetype(F + name, size)
EYE = font("Inter-SemiBold.otf", 34); BIG = font("InterDisplay-Bold.otf", 92)
MID = font("InterDisplay-SemiBold.otf", 66); BODY = font("Inter-Medium.otf", 56)
SMALL = font("Inter-Medium.otf", 30); DISC = font("Inter-SemiBold.otf", 34); WORD = font("InterDisplay-Bold.otf", 40)
X0, X1 = 90, 900            # keep clear of right-side platform buttons
TOP, BOTTOM = 330, 1430     # keep clear of top bars and bottom captions

# timeline (seconds)
SCENES = [("hook", 0, 3.2), ("name", 3.2, 6.4), ("f0", 6.4, 10.0), ("f1", 10.0, 13.6),
          ("f2", 13.6, 17.2), ("skip", 17.2, 20.8), ("cta", 20.8, 25.0)]
DUR = SCENES[-1][2]

def wrap(draw, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= width: cur = t
        else: lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def spaced(text, n=4): return (" " * 0).join(text.upper())  # tracking via draw below

def background(t):
    # small field, upscaled: warm amber glow drifting slowly over espresso
    w, h = 135, 240
    yy, xx = np.mgrid[0:h, 0:w].astype(float)
    cx = w * (0.62 + 0.18 * math.sin(t * 0.35)); cy = h * (0.30 + 0.10 * math.cos(t * 0.27))
    d = np.sqrt((xx - cx) ** 2 + ((yy - cy) * 0.8) ** 2) / (w * 0.95)
    g = np.clip(1 - d, 0, 1) ** 2.2 * 0.55
    cx2 = w * (0.25 + 0.1 * math.cos(t * 0.21)); cy2 = h * (0.85 + 0.05 * math.sin(t * 0.3))
    d2 = np.sqrt((xx - cx2) ** 2 + ((yy - cy2) * 0.8) ** 2) / (w * 0.8)
    g += np.clip(1 - d2, 0, 1) ** 2.4 * 0.25
    img = ESPRESSO[None, None, :] * (1 - g[..., None]) + AMBER[None, None, :] * g[..., None] * 0.9 + ESPRESSO * g[..., None] * 0.1
    return Image.fromarray(img.clip(0, 255).astype(np.uint8)).resize((W, H), Image.BILINEAR)

def tracked(draw, xy, text, fnt, fill, track=6):
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + track

def ease(p): return 1 - (1 - p) ** 3

def scene_alpha(t, a, b):
    if t < a or t >= b: return 0, 0
    fin = min(1, (t - a) / 0.45); fout = min(1, (b - t) / 0.3)
    return min(ease(fin), fout), (1 - ease(fin)) * 46

def draw_block(img, t, a, b, items):
    """items: list of (kind, text, font, color, gap_after) laid out top-down from TOP+60."""
    alpha, dy = scene_alpha(t, a, b)
    if alpha <= 0: return
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(layer)
    def height():
        h = 0
        for kind, text, fnt, color, gap in items:
            if kind == "eyebrow": h += fnt.size + gap
            elif kind == "rule": h += 6 + gap
            else: h += int(fnt.size * 1.18) * len(wrap(d, text, fnt, X1 - X0)) + gap
        return h
    area_top, area_bottom = TOP + 20, BOTTOM - 130
    y = area_top + max(0, (area_bottom - area_top - height()) // 2) + dy
    for kind, text, fnt, color, gap in items:
        if kind == "eyebrow":
            tracked(d, (X0, y), text.upper(), fnt, color); y += fnt.size + gap
        elif kind == "rule":
            d.rectangle([X0, y, X0 + 120, y + 6], fill=color); y += 6 + gap
        else:
            for line in wrap(d, text, fnt, X1 - X0):
                d.text((X0, y), line, font=fnt, fill=color); y += int(fnt.size * 1.18)
            y += gap
    a8 = layer.getchannel("A").point(lambda v: int(v * alpha))
    layer.putalpha(a8); img.alpha_composite(layer)

def frame(p, t, total_facts=3):
    img = background(t).convert("RGBA"); d = ImageDraw.Draw(img)
    # persistent chrome: wordmark, progress bar, disclosure
    tracked(d, (X0, TOP - 70), "MITOTHRUM", WORD, AMBER_T, track=10)
    d.rectangle([X0, TOP - 14, X1, TOP - 10], fill=(70, 55, 40))
    d.rectangle([X0, TOP - 14, X0 + int((X1 - X0) * min(1, t / DUR)), TOP - 10], fill=tuple(AMBER.astype(int)))
    for i, line in enumerate(["Affiliate links on mitothrum.com:", "I may earn a commission, at no", "extra cost to you."]):
        d.text((X0, BOTTOM - 110 + i * 42), line, font=DISC, fill=(222, 208, 180))
    S = {k: (a, b) for k, a, b in SCENES}
    draw_block(img, t, *S["hook"], [("eyebrow", p["ritual"], EYE, AMBER_T, 34), ("rule", "", None, AMBER_T, 40),
                                    ("text", p["hook"], BIG, CREAM, 0)])
    draw_block(img, t, *S["name"], [("eyebrow", "The pick", EYE, AMBER_T, 34), ("rule", "", None, AMBER_T, 40),
                                    ("text", p["name"], MID, CREAM, 30),
                                    ("text", f"One of our {p['ritual'].lower()} picks", BODY, MUTED, 0)])
    for i in range(3):
        draw_block(img, t, *S[f"f{i}"], [("eyebrow", f"Fact {i+1} of 3", EYE, AMBER_T, 34),
                                         ("rule", "", None, AMBER_T, 40), ("text", p["facts"][i], MID, CREAM, 0)])
    draw_block(img, t, *S["skip"], [("eyebrow", "Who should skip it", EYE, AMBER_T, 34), ("rule", "", None, AMBER_T, 40),
                                    ("text", p["skip"], BODY, CREAM, 50),
                                    ("text", "Educational content — not medical advice.", SMALL, MUTED, 0)])
    draw_block(img, t, *S["cta"], [("eyebrow", "The full, honest breakdown", EYE, AMBER_T, 34), ("rule", "", None, AMBER_T, 40),
                                   ("text", p["page_label"], MID, CREAM, 36), ("text", "mitothrum.com", BIG, AMBER_T, 40),
                                   ("text", "Link in bio or in the description.", SMALL, MUTED, 0)])
    return img.convert("RGB")

def render(p, out):
    path = os.path.join(out, p["slug"] + ".mp4")
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
           "-shortest", "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-movflags", "+faststart",
           "-c:a", "aac", "-b:a", "96k", path]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    n = int(DUR * FPS)
    for i in range(n):
        im = frame(p, i / FPS)
        if i == int(1.6 * FPS): im.save(os.path.join(out, p["slug"] + "-cover.jpg"), quality=90)
        proc.stdin.write(im.tobytes())
    proc.stdin.close(); proc.wait()
    return path

if __name__ == "__main__":
    out = sys.argv[1]; os.makedirs(out, exist_ok=True)
    products = json.load(open(os.path.join(os.path.dirname(__file__), "products.json")))
    want = set(sys.argv[2:])
    for p in products:
        if not want or p["slug"] in want:
            print("rendered", render(p, out), flush=True)
