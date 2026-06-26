"""Index + contact-sheet the flat 'Fotos inmuebles' folder for premium curation.
Assigns stable short IDs F001.. (sorted) and writes a mapping TSV."""
import os, math
from PIL import Image, ImageDraw, ImageFont

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "Fotos inmuebles")
OUT = os.path.join(ROOT, "build", "review2")
os.makedirs(OUT, exist_ok=True)
FONTS = os.path.join(ROOT, "build", "fonts")

def font(s): return ImageFont.truetype(os.path.join(FONTS, "OpenSans-Var.ttf"), s)

def collect():
    fs = [f for f in os.listdir(SRC) if f.lower().endswith((".jpg", ".jpeg", ".png"))
          and not f.startswith(".")]
    return sorted(fs)

def build():
    files = collect()
    mapping = []
    ids = []
    for i, f in enumerate(files, 1):
        fid = f"F{i:03d}"
        mapping.append(f"{fid}\t{f}")
        ids.append((fid, f))
    with open(os.path.join(OUT, "index.tsv"), "w") as fh:
        fh.write("\n".join(mapping))
    per = 30; cols = 6; cw = 300; th = int(cw * 1.0); chh = th + 30; top = 50
    chunks = [ids[i:i+per] for i in range(0, len(ids), per)]
    for ci, chunk in enumerate(chunks):
        rows = math.ceil(len(chunk) / cols)
        canvas = Image.new("RGB", (cols * cw, rows * chh + top), (22, 24, 30))
        d = ImageDraw.Draw(canvas)
        d.text((14, 14), f"FOTOS INMUEBLES — hoja {ci+1}/{len(chunks)}", font=font(26), fill=(255, 215, 120))
        for i, (fid, f) in enumerate(chunk):
            r, c = divmod(i, cols); x, y = c * cw, top + r * chh
            try:
                im = Image.open(os.path.join(SRC, f)).convert("RGB")
            except Exception:
                continue
            iw, ih = im.size
            sc = min(cw / iw, th / ih); nw, nh = int(iw*sc), int(ih*sc)
            im = im.resize((nw, nh), Image.LANCZOS)
            canvas.paste(im, (x + (cw-nw)//2, y + (th-nh)//2))
            d.rectangle([x, y+th, x+cw, y+th+30], fill=(10, 12, 16))
            d.text((x+6, y+th+5), fid, font=font(20), fill=(255, 230, 150))
            d.rectangle([x, y, x+cw, y+th+30], outline=(64, 70, 78), width=1)
        op = os.path.join(OUT, f"sheet_{ci+1:02d}.png")
        canvas.save(op); print(op)
    print("total", len(files))

if __name__ == "__main__":
    build()
