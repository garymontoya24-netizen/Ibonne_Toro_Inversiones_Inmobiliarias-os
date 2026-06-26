"""Build labeled contact sheets so photos can be reviewed many-at-once."""
import os, sys, math
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = os.path.join(ROOT, "build", "fonts")
OUT = os.path.join(ROOT, "build", "review")
os.makedirs(OUT, exist_ok=True)

def font(size):
    return ImageFont.truetype(os.path.join(FONTS, "OpenSans-Var.ttf"), size)

def collect(folder, exts=(".jpg", ".jpeg", ".png")):
    files = []
    for f in sorted(os.listdir(folder)):
        if f.startswith("."):
            continue
        if f.lower().endswith(exts):
            files.append(os.path.join(folder, f))
    return files

def sheet(files, out_name, cols=5, cell=360, label_h=46, per_sheet=20, title=""):
    chunks = [files[i:i+per_sheet] for i in range(0, len(files), per_sheet)]
    paths = []
    for ci, chunk in enumerate(chunks):
        rows = math.ceil(len(chunk) / cols)
        cw, chh = cell, int(cell * 1.25) + label_h
        top = 56 if title else 0
        W = cols * cw
        H = rows * chh + top
        canvas = Image.new("RGB", (W, H), (24, 28, 34))
        d = ImageDraw.Draw(canvas)
        if title:
            d.text((16, 16), f"{title}  (hoja {ci+1}/{len(chunks)})", font=font(28), fill=(255, 215, 120))
        for i, path in enumerate(chunk):
            r, c = divmod(i, cols)
            x, y = c * cw, top + r * chh
            try:
                im = Image.open(path).convert("RGB")
            except Exception:
                continue
            iw, ih = im.size
            target_h = int(cell * 1.25)
            scale = min(cw / iw, target_h / ih)
            nw, nh = int(iw * scale), int(ih * scale)
            im = im.resize((nw, nh), Image.LANCZOS)
            ox, oy = x + (cw - nw) // 2, y + (target_h - nh) // 2
            canvas.paste(im, (ox, oy))
            name = os.path.basename(path)
            d.rectangle([x, y + target_h, x + cw, y + target_h + label_h], fill=(12, 14, 18))
            d.text((x + 8, y + target_h + 10), name, font=font(20), fill=(235, 235, 235))
            d.rectangle([x, y, x + cw, y + target_h + label_h], outline=(60, 66, 74), width=1)
        op = os.path.join(OUT, f"{out_name}_{ci+1}.png")
        canvas.save(op)
        paths.append(op)
    return paths

if __name__ == "__main__":
    jobs = []
    # studio personal-brand shoot
    fi = os.path.join(ROOT, "FOTOS IBONNE", "Ibonne Toro")
    srg = [f for f in collect(fi) if os.path.basename(f).startswith("SRG")]
    wa  = [f for f in collect(fi) if "WhatsApp" in os.path.basename(f) or "Diseño" in os.path.basename(f)]
    jobs += sheet(srg, "studio_SRG", per_sheet=24, cols=6, cell=300, title="ESTUDIO IBONNE (SRG)")
    jobs += sheet(wa,  "studio_WA",  per_sheet=24, cols=6, cell=300, title="ESTUDIO IBONNE (WhatsApp/Diseno)")
    # property folders
    ei = os.path.join(ROOT, "Ejemplos Inmuebles")
    for d in sorted(os.listdir(ei)):
        fp = os.path.join(ei, d)
        if os.path.isdir(fp):
            fl = collect(fp)
            safe = d.replace(" ", "_").replace(".", "")
            jobs += sheet(fl, f"prop_{safe}", per_sheet=24, cols=6, cell=300, title=d)
    print("\n".join(jobs))
