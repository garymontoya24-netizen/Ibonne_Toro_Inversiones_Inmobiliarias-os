"""Minimal SVG single-path rasterizer (no cairo). Flattens M/L/H/V/C/S/A/Z
to polylines and fills subpaths with the even-odd rule (XOR) at supersampled
resolution. Used to render the official Instagram + WhatsApp glyphs to white."""
import re, math, os
from PIL import Image, ImageDraw, ImageChops

_NUMRE = re.compile(r'[-+]?(?:\d*\.\d+|\d+\.?)(?:[eE][-+]?\d+)?')

class _Scan:
    """Char scanner that respects SVG arc-flag quirks (glued single-digit flags)."""
    def __init__(self, d): self.s = d; self.i = 0; self.n = len(d)
    def _skip(self):
        while self.i < self.n and self.s[self.i] in " ,\t\n\r": self.i += 1
    def peek_cmd(self):
        self._skip()
        return self.s[self.i] if self.i < self.n and self.s[self.i].isalpha() else None
    def read_cmd(self):
        c = self.s[self.i]; self.i += 1; return c
    def num(self):
        self._skip(); m = _NUMRE.match(self.s, self.i); self.i = m.end(); return float(m.group())
    def flag(self):
        self._skip(); c = self.s[self.i]; self.i += 1; return int(c)
    def eof(self):
        self._skip(); return self.i >= self.n

def _cubic(p0, p1, p2, p3, n=28):
    out = []
    for k in range(1, n + 1):
        t = k / n; u = 1 - t
        x = u*u*u*p0[0] + 3*u*u*t*p1[0] + 3*u*t*t*p2[0] + t*t*t*p3[0]
        y = u*u*u*p0[1] + 3*u*u*t*p1[1] + 3*u*t*t*p2[1] + t*t*t*p3[1]
        out.append((x, y))
    return out

def _arc(p0, rx, ry, phi_deg, laf, sf, p1, n=40):
    if rx == 0 or ry == 0:
        return [p1]
    phi = math.radians(phi_deg)
    x0, y0 = p0; x1, y1 = p1
    dx2 = (x0 - x1) / 2; dy2 = (y0 - y1) / 2
    cp, sp = math.cos(phi), math.sin(phi)
    x1p = cp*dx2 + sp*dy2; y1p = -sp*dx2 + cp*dy2
    rx, ry = abs(rx), abs(ry)
    lam = x1p*x1p/(rx*rx) + y1p*y1p/(ry*ry)
    if lam > 1:
        s = math.sqrt(lam); rx *= s; ry *= s
    sign = -1 if laf == sf else 1
    num = rx*rx*ry*ry - rx*rx*y1p*y1p - ry*ry*x1p*x1p
    den = rx*rx*y1p*y1p + ry*ry*x1p*x1p
    co = sign * math.sqrt(max(0, num/den)) if den else 0
    cxp = co*rx*y1p/ry; cyp = -co*ry*x1p/rx
    cx = cp*cxp - sp*cyp + (x0+x1)/2
    cy = sp*cxp + cp*cyp + (y0+y1)/2
    def ang(ux, uy, vx, vy):
        dot = ux*vx + uy*vy; ln = math.hypot(ux, uy)*math.hypot(vx, vy)
        a = math.acos(max(-1, min(1, dot/ln))) if ln else 0
        return -a if ux*vy - uy*vx < 0 else a
    th1 = ang(1, 0, (x1p-cxp)/rx, (y1p-cyp)/ry)
    dth = ang((x1p-cxp)/rx, (y1p-cyp)/ry, (-x1p-cxp)/rx, (-y1p-cyp)/ry)
    if sf == 0 and dth > 0: dth -= 2*math.pi
    if sf == 1 and dth < 0: dth += 2*math.pi
    out = []
    for k in range(1, n + 1):
        th = th1 + dth*k/n
        x = cp*rx*math.cos(th) - sp*ry*math.sin(th) + cx
        y = sp*rx*math.cos(th) + cp*ry*math.sin(th) + cy
        out.append((x, y))
    return out

def parse_path(d):
    sc = _Scan(d)
    cur = (0.0, 0.0); start = (0.0, 0.0); cmd = None; pcc = None
    subs = []; pts = []
    def flush():
        nonlocal pts
        if len(pts) >= 2: subs.append(pts)
        pts = []
    while not sc.eof():
        c = sc.peek_cmd()
        if c is not None:
            cmd = sc.read_cmd()
        rel = cmd.islower(); C = cmd.upper()
        if C == 'M':
            x, y = sc.num(), sc.num()
            if rel: x += cur[0]; y += cur[1]
            flush(); cur = (x, y); start = (x, y); pts = [cur]
            cmd = 'l' if rel else 'L'; pcc = None
        elif C == 'L':
            x, y = sc.num(), sc.num()
            if rel: x += cur[0]; y += cur[1]
            cur = (x, y); pts.append(cur); pcc = None
        elif C == 'H':
            x = sc.num(); x = x + cur[0] if rel else x
            cur = (x, cur[1]); pts.append(cur); pcc = None
        elif C == 'V':
            y = sc.num(); y = y + cur[1] if rel else y
            cur = (cur[0], y); pts.append(cur); pcc = None
        elif C == 'C':
            x1, y1, x2, y2, x, y = sc.num(), sc.num(), sc.num(), sc.num(), sc.num(), sc.num()
            if rel: x1+=cur[0];y1+=cur[1];x2+=cur[0];y2+=cur[1];x+=cur[0];y+=cur[1]
            pts.extend(_cubic(cur, (x1, y1), (x2, y2), (x, y))); pcc = (x2, y2); cur = (x, y)
        elif C == 'S':
            x2, y2, x, y = sc.num(), sc.num(), sc.num(), sc.num()
            if rel: x2+=cur[0];y2+=cur[1];x+=cur[0];y+=cur[1]
            x1, y1 = (2*cur[0]-pcc[0], 2*cur[1]-pcc[1]) if pcc else cur
            pts.extend(_cubic(cur, (x1, y1), (x2, y2), (x, y))); pcc = (x2, y2); cur = (x, y)
        elif C == 'A':
            rx, ry, rot = sc.num(), sc.num(), sc.num()
            laf, sf = sc.flag(), sc.flag()
            x, y = sc.num(), sc.num()
            if rel: x += cur[0]; y += cur[1]
            pts.extend(_arc(cur, rx, ry, rot, laf, sf, (x, y))); cur = (x, y); pcc = None
        elif C == 'Z':
            pts.append(start); cur = start; flush(); pcc = None
    flush()
    return subs

def rasterize_white(svg_path, out_path, viewbox=24, target=512, ss=3):
    d = re.search(r'd="([^"]+)"', open(svg_path).read()).group(1)
    subs = parse_path(d)
    size = target * ss; sc = size / viewbox
    acc = Image.new("1", (size, size), 0)
    for sp in subs:
        m = Image.new("1", (size, size), 0)
        ImageDraw.Draw(m).polygon([(x*sc, y*sc) for x, y in sp], fill=1)
        acc = ImageChops.logical_xor(acc, m)
    alpha = acc.convert("L").resize((target, target), Image.LANCZOS)
    white = Image.new("RGBA", (target, target), (255, 255, 255, 255))
    white.putalpha(alpha)
    white.save(out_path)
    return white.size

if __name__ == "__main__":
    A = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "social")
    print("instagram", rasterize_white(os.path.join(A, "instagram.svg"), os.path.join(A, "instagram_white.png")))
    print("whatsapp", rasterize_white(os.path.join(A, "whatsapp.svg"), os.path.join(A, "whatsapp_white.png")))
