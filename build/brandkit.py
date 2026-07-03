"""
Brand kit + rendering helpers for IBONNE TORO carousels.
Colors and rules extracted from material_apoyo/files/1_DESIGN_SYSTEM_IBONNE_TORO.md
and the reference pieces in material_apoyo/Referencias/.
"""
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "build", "fonts")
ASSETS = os.path.join(ROOT, "build", "assets")

# ---- Canvas (Instagram 4:5) ----
W, H = 1080, 1350
MX = 70          # side margin
MB = 70          # bottom margin

# ---- Palette (exact, no approximations) ----
AZUL   = (44, 62, 80)      # #2C3E50
DORADO = (212, 175, 55)    # #D4AF37
BLANCO = (255, 255, 255)   # #FFFFFF

# ---- Fonts ----
def font(name, size):
    return ImageFont.truetype(os.path.join(FONTS, name), size)

def F_bold(s):  return font("Poppins-Bold.ttf", s)
def F_semi(s):  return font("Poppins-SemiBold.ttf", s)
def F_med(s):   return font("Poppins-Medium.ttf", s)
def F_reg(s):   return font("Poppins-Regular.ttf", s)
def F_sub(s):   return font("LexendDeca-Var.ttf", s)

# ---- Logo assets ----
LOGO_WHITE = Image.open(os.path.join(ASSETS, "logo_white.png")).convert("RGBA")
LOGO_GOLD  = Image.open(os.path.join(ASSETS, "logo_gold.png")).convert("RGBA")

# ---- Official social glyphs (rendered from brand SVGs -> white) ----
_SOCIAL = os.path.join(ASSETS, "social")
IG_GLYPH = Image.open(os.path.join(_SOCIAL, "instagram_white.png")).convert("RGBA")
WA_GLYPH = Image.open(os.path.join(_SOCIAL, "whatsapp_white.png")).convert("RGBA")


# ---------------------------------------------------------------- image utils
def cover(path, focus_y=0.5, focus_x=0.5, sharpen=True):
    """Scale + crop a photo to fill WxH (4:5), biasing the crop window. A light
    unsharp mask keeps detail crisp at IG compression."""
    im = Image.open(path).convert("RGB")
    iw, ih = im.size
    scale = max(W / iw, H / ih)
    nw, nh = round(iw * scale), round(ih * scale)
    im = im.resize((nw, nh), Image.LANCZOS)
    x = round((nw - W) * focus_x)
    y = round((nh - H) * focus_y)
    im = im.crop((x, y, x + W, y + H))
    if sharpen:
        im = im.filter(ImageFilter.UnsharpMask(radius=2.4, percent=90, threshold=2))
    return im.convert("RGBA")


def vgradient(color, stops):
    """Vertical gradient overlay (H tall). stops = [(frac, alpha0-255), ...]."""
    fr = np.array([s[0] for s in stops])
    al = np.array([s[1] for s in stops], dtype=float)
    ys = np.linspace(0, 1, H)
    a = np.interp(ys, fr, al)
    layer = np.zeros((H, W, 4), dtype=np.uint8)
    layer[:, :, 0] = color[0]; layer[:, :, 1] = color[1]; layer[:, :, 2] = color[2]
    layer[:, :, 3] = a[:, None].astype(np.uint8)
    return Image.fromarray(layer, "RGBA")


def place_logo(base, logo, width, xy, opacity=1.0, anchor="lt", shadow=False):
    r = width / logo.width
    lg = logo.resize((width, round(logo.height * r)), Image.LANCZOS)
    if opacity < 1.0:
        a = lg.split()[3].point(lambda p: int(p * opacity))
        lg.putalpha(a)
    x, y = xy
    if "r" in anchor: x -= lg.width
    if "c" in anchor: x -= lg.width // 2
    if "b" in anchor: y -= lg.height
    if "m" in anchor: y -= lg.height // 2
    if shadow:
        sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
        smask = lg.split()[3].point(lambda p: int(p * 0.55))
        blk = Image.new("RGBA", lg.size, (0, 0, 0, 255)); blk.putalpha(smask)
        sh.alpha_composite(blk, (x + 3, y + 4))
        sh = sh.filter(ImageFilter.GaussianBlur(7))
        base.alpha_composite(sh)
    base.alpha_composite(lg, (x, y))
    return lg.width, lg.height


# ---------------------------------------------------------------- text utils
def tracked_width(draw, text, fnt, tracking):
    return sum(draw.textlength(c, font=fnt) for c in text) + tracking * (len(text) - 1)

def draw_tracked(draw, xy, text, fnt, fill, tracking=0, anchor_x="l"):
    x, y = xy
    tw = tracked_width(draw, text, fnt, tracking)
    if anchor_x == "c": x -= tw / 2
    if anchor_x == "r": x -= tw
    for c in text:
        draw.text((x, y), c, font=fnt, fill=fill)
        x += draw.textlength(c, font=fnt) + tracking
    return tw

def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(), [], ""
    for w_ in words:
        t = (cur + " " + w_).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur: lines.append(cur)
            cur = w_
    if cur: lines.append(cur)
    return lines

def text_shadow(base, xy, text, fnt, anchor="la", blur=4, alpha=0.5):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    d.text((xy[0] + 2, xy[1] + 3), text, font=fnt, fill=(0, 0, 0, int(255 * alpha)), anchor=anchor)
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(blur)))


# ---------------------------------------------------------------- icons
def ig_icon(size, color=BLANCO):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sw = max(2, round(size * 0.09))
    pad = round(size * 0.10)
    rad = round(size * 0.28)
    d.rounded_rectangle([pad, pad, size - pad, size - pad], radius=rad, outline=color, width=sw)
    c = size / 2; r = size * 0.22
    d.ellipse([c - r, c - r, c + r, c + r], outline=color, width=sw)
    dot = size * 0.07; dx = size - pad - size * 0.17
    d.ellipse([dx - dot, pad + size * 0.10 - dot, dx + dot, pad + size * 0.10 + dot], fill=color)
    return im

def wa_icon(size, color=BLANCO):
    """WhatsApp-style: speech circle + phone handset."""
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sw = max(2, round(size * 0.08))
    d.ellipse([sw, sw, size - sw, size - sw], outline=color, width=sw)
    # tail
    d.polygon([(size * 0.18, size * 0.86), (size * 0.30, size * 0.70), (size * 0.40, size * 0.82)], fill=color)
    # handset built on its own layer then rotated
    hs = max(2, round(size * 0.30))
    layer = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    dl = ImageDraw.Draw(layer)
    cx = size * 0.5
    dl.line([(cx, size * 0.34), (cx, size * 0.66)], fill=color, width=hs, joint="curve")
    er = size * 0.085
    dl.ellipse([cx - er, size * 0.30 - er, cx + er, size * 0.30 + er], fill=color)
    dl.ellipse([cx - er, size * 0.70 - er, cx + er, size * 0.70 + er], fill=color)
    layer = layer.rotate(-35, resample=Image.BICUBIC, center=(size / 2, size / 2))
    im.alpha_composite(layer)
    return im

def pin_icon(size, color=BLANCO):
    im = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    sw = max(2, round(size * 0.09))
    w = size * 0.62; cx = size / 2; top = size * 0.06
    d.ellipse([cx - w / 2, top, cx + w / 2, top + w], outline=color, width=sw)
    r = w * 0.20
    d.ellipse([cx - r, top + w / 2 - r, cx + r, top + w / 2 + r], fill=color)
    d.polygon([(cx - w * 0.34, top + w * 0.72), (cx + w * 0.34, top + w * 0.72), (cx, size * 0.96)], fill=color)
    return im


# ---------------------------------------------------------------- components
CONTACT_IG = "@ibonne_toro"
CONTACT_WA = "+57 310 497 33 36"

def _glyph(g, size):
    """Resize an official social glyph, with a soft dark shadow for legibility."""
    ic = g.resize((size, size), Image.LANCZOS)
    sh = Image.new("RGBA", (size + 12, size + 12), (0, 0, 0, 0))
    blk = Image.new("RGBA", ic.size, (0, 0, 0, 255)); blk.putalpha(ic.split()[3].point(lambda p: int(p * 0.55)))
    sh.alpha_composite(blk, (6, 7)); sh = sh.filter(ImageFilter.GaussianBlur(4))
    out = Image.new("RGBA", (size + 12, size + 12), (0, 0, 0, 0))
    out.alpha_composite(sh); out.alpha_composite(ic, (0, 0))
    return out, size

def footer(base, logo_w=300):
    """Bottom lockup: white logo left, IG + WhatsApp right (official glyphs)."""
    d = ImageDraw.Draw(base)
    by = H - MB
    place_logo(base, LOGO_WHITE, logo_w, (MX, by), anchor="lb", shadow=True)
    fc = F_med(28)
    isz = 40
    row_gap = 54
    y2 = by - 12
    y1 = y2 - row_gap
    for (glyph, txt, yy) in [(IG_GLYPH, CONTACT_IG, y1), (WA_GLYPH, CONTACT_WA, y2)]:
        tw = d.textlength(txt, font=fc)
        tx = W - MX
        text_shadow(base, (tx, yy), txt, fc, anchor="rs", alpha=0.55)
        d.text((tx, yy), txt, font=fc, fill=BLANCO, anchor="rs")
        icon, s = _glyph(glyph, isz)
        ix = tx - tw - 16 - s
        base.alpha_composite(icon, (round(ix), round(yy - s + 2)))

def watermark(base, width=200, opacity=0.85):
    """Small top-left logo for interior/story slides. NO heavy scrim — the photo
    stays clean/sharp; the logo's own drop shadow keeps it legible."""
    place_logo(base, LOGO_WHITE, width, (MX, 54), opacity=opacity, anchor="lt", shadow=True)

def gold_chip(base, xy, label, fs=27, tracking=4, pad_x=30, pad_y=16):
    """Filled gold rounded chip with dark-blue tracked uppercase label."""
    d = ImageDraw.Draw(base)
    fnt = F_semi(fs)
    tw = tracked_width(d, label, fnt, tracking)
    asc, desc = fnt.getmetrics()
    th = asc + desc
    x, y = xy
    box = [x, y, x + tw + pad_x * 2, y + th + pad_y * 2]
    # soft shadow
    sh = Image.new("RGBA", base.size, (0, 0, 0, 0))
    ds = ImageDraw.Draw(sh)
    ds.rounded_rectangle([box[0], box[1] + 4, box[2], box[3] + 4], radius=(box[3] - box[1]) // 2,
                         fill=(0, 0, 0, 90))
    base.alpha_composite(sh.filter(ImageFilter.GaussianBlur(7)))
    d.rounded_rectangle(box, radius=(box[3] - box[1]) // 2, fill=DORADO)
    draw_tracked(d, (x + pad_x, y + pad_y - 1), label, fnt, AZUL, tracking)
    return box

def caption(base, keyword, headline, accent=True):
    """Bottom caption band for story slides: gold keyword + white headline,
    with a gold vertical accent bar (brand motif from Ejemplo 1)."""
    base.alpha_composite(vgradient(AZUL, [(0.0, 0), (0.45, 0), (0.72, 120), (1.0, 235)]))
    d = ImageDraw.Draw(base)
    fk = F_semi(25)
    fh = F_semi(40)
    lines = wrap(d, headline, fh, W - MX * 2 - 26)
    lh = fh.getmetrics(); line_h = lh[0] + lh[1] - 6
    block_h = 34 + 14 + line_h * len(lines)
    y0 = H - MB - block_h + 6
    bar_x = MX
    tx = MX + 26
    # keyword
    draw_tracked(d, (tx, y0), keyword.upper(), fk, DORADO, 4)
    yy = y0 + 34 + 14
    for ln in lines:
        text_shadow(base, (tx, yy), ln, fh, anchor="la", alpha=0.45, blur=3)
        d.text((tx, yy), ln, font=fh, fill=BLANCO, anchor="la")
        yy += line_h
    if accent:
        d.rounded_rectangle([bar_x, y0 + 4, bar_x + 6, yy - 12], radius=3, fill=DORADO)


def caption_block(base, keyword, headline, *, stat=None, fact=None, source=None,
                  hl_size=47, accent=True):
    """Lower-third info block over a photo. Stacks (top->down):
    gold keyword · optional huge gold stat · white headline · optional gold
    fact line · optional small source line. Auto-measured and bottom-anchored."""
    if stat:
        base.alpha_composite(vgradient(AZUL, [(0.0, 0), (0.40, 0), (0.60, 150), (1.0, 252)]))
    else:
        base.alpha_composite(vgradient(AZUL, [(0.0, 0), (0.54, 0), (0.72, 140), (1.0, 248)]))
    d = ImageDraw.Draw(base)
    fk    = F_semi(28)
    fh    = F_semi(hl_size)
    fstat = F_bold(178)
    ffact = F_med(27)
    fsrc  = F_reg(21)
    maxw  = W - MX * 2 - 26

    hl_lines = wrap(d, headline, fh, maxw)
    lh = fh.getmetrics(); line_h = lh[0] + lh[1] - 6
    kk = fk.getmetrics(); k_h = kk[0] + kk[1]
    elems = [("kw", k_h, 0)]
    if stat:
        sb = d.textbbox((0, 0), stat, font=fstat)
        stat_h = sb[3] - sb[1]
        elems.append(("stat", stat_h, 6))
    elems.append(("hl", line_h * len(hl_lines), 12 if not stat else 8))
    fact_lines = []
    if fact:
        fact_lines = wrap(d, fact, ffact, maxw)
        fm = ffact.getmetrics(); fact_lh = fm[0] + fm[1] + 2
        elems.append(("fact", fact_lh * len(fact_lines), 18))
    if source:
        sm = fsrc.getmetrics(); src_h = sm[0] + sm[1]
        elems.append(("src", src_h, 14))

    total = sum(h for _, h, _ in elems) + sum(g for _, _, g in elems)
    y = H - MB - total + 4
    tx = MX + 26
    top_y = y

    for kind, h, gap in elems:
        y += gap
        if kind == "kw":
            draw_tracked(d, (tx, y), keyword.upper(), fk, DORADO, 4)
        elif kind == "stat":
            sb = d.textbbox((0, 0), stat, font=fstat)
            text_shadow(base, (tx - sb[0], y - sb[1]), stat, fstat, anchor="la", alpha=0.5, blur=6)
            d.text((tx - sb[0], y - sb[1]), stat, font=fstat, fill=DORADO, anchor="la")
        elif kind == "hl":
            yy = y
            for ln in hl_lines:
                text_shadow(base, (tx, yy), ln, fh, anchor="la", alpha=0.45, blur=3)
                d.text((tx, yy), ln, font=fh, fill=BLANCO, anchor="la")
                yy += line_h
        elif kind == "fact":
            yy = y
            for i, ln in enumerate(fact_lines):
                if i == 0:
                    d.ellipse([tx, yy + 11, tx + 9, yy + 20], fill=DORADO)
                d.text((tx + 20, yy), ln, font=ffact, fill=(232, 232, 232, 255), anchor="la")
                yy += ffact.getmetrics()[0] + ffact.getmetrics()[1] + 2
        elif kind == "src":
            d.text((tx, y), source, font=fsrc, fill=(206, 206, 206, 235), anchor="la")
        y += h

    if accent:
        d.rounded_rectangle([MX, top_y + 4, MX + 6, top_y + (k_h)], radius=3, fill=DORADO)


def solid_card(top_rule=True):
    """Solid dark-blue brand canvas for clean data slides."""
    base = Image.new("RGBA", (W, H), AZUL + (255,))
    if top_rule:
        d = ImageDraw.Draw(base)
        d.rectangle([MX, 150, MX + 90, 156], fill=DORADO)
    return base


def barchart(base, items, x0, y0, w, row_h=92, gap=30, vmax=None, unit=""):
    """Horizontal bars. items = [(label, value, highlight_bool)]. Highlighted
    rows draw in gold, the rest in muted white."""
    d = ImageDraw.Draw(base)
    vmax = vmax or max(v for _, v, _ in items)
    flab = F_med(28); fval = F_semi(30)
    y = y0
    bar_x = x0
    bar_max = w
    for label, value, hot in items:
        col = DORADO if hot else (255, 255, 255, 150)
        txtcol = BLANCO if hot else (225, 225, 225, 240)
        d.text((x0, y - 36), label, font=flab, fill=txtcol, anchor="la")
        bw = max(8, round(bar_max * (value / vmax)))
        d.rounded_rectangle([bar_x, y, bar_x + bw, y + row_h - 38], radius=8, fill=col)
        vtxt = f"{unit}{value:.2f}".replace(".", ",") + "M" if isinstance(value, float) else f"{unit}{value}"
        d.text((bar_x + bw + 16, y - 2), vtxt, font=fval, fill=txtcol, anchor="lm")
        y += row_h + gap
    return y


def save(base, path):
    base.convert("RGB").save(path, "PNG")
