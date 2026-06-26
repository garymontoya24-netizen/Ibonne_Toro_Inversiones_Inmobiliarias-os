"""Rasterize the official Instagram + WhatsApp brand glyphs (simple-icons,
single-path SVGs) to crisp WHITE silhouette PNGs with transparent background."""
import os
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPM
from PIL import Image, ImageOps

ASSETS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets", "social")

def raster(name, target=1024):
    d = svg2rlg(os.path.join(ASSETS, name + ".svg"))
    s = target / max(d.width, d.height)
    d.scale(s, s); d.width *= s; d.height *= s
    blk = os.path.join(ASSETS, name + "_blk.png")
    renderPM.drawToFile(d, blk, fmt="PNG", bg=0xFFFFFF)   # black shape on white
    im = Image.open(blk).convert("L")
    alpha = ImageOps.invert(im)                            # shape -> opaque
    white = Image.new("RGBA", im.size, (255, 255, 255, 255))
    white.putalpha(alpha)
    out = os.path.join(ASSETS, name + "_white.png")
    white.save(out)
    os.remove(blk)
    print("ok", name, white.size)

if __name__ == "__main__":
    raster("instagram")
    raster("whatsapp")
