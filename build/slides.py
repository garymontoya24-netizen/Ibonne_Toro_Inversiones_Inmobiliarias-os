"""Shared slide builders for the IBONNE TORO carousels (build on brandkit)."""
from PIL import ImageDraw
import brandkit as bk


def hero(path, chip, title, sub, support, focus_y=0.5, focus_x=0.5):
    """Cover / CTA slide: photo + dark gradient, gold chip, gold title, white
    sub + support line, footer lockup. (Same recipe as the validated carousel.)"""
    base = bk.cover(path, focus_y=focus_y, focus_x=focus_x)
    base.alpha_composite(bk.vgradient(bk.AZUL, [(0.0, 40), (0.34, 0), (0.56, 120), (1.0, 252)]))
    d = ImageDraw.Draw(base)
    f_title = bk.F_bold(62)
    f_sub   = bk.F_sub(34)
    f_sup   = bk.F_reg(24)
    title_lines = bk.wrap(d, title, f_title, bk.W - bk.MX * 2)
    sup_lines   = bk.wrap(d, support, f_sup, bk.W - bk.MX * 2 - 10)
    tlh = f_title.getmetrics(); t_h = tlh[0] + tlh[1] - 8
    slh = f_sup.getmetrics();   s_h = slh[0] + slh[1] + 2
    chip_h = bk.F_semi(27).getmetrics(); chip_h = chip_h[0] + chip_h[1] + 32
    block = chip_h + 22 + t_h * len(title_lines) + 10 + 46 + 18 + s_h * len(sup_lines)
    y = (bk.H - 245) - block
    bk.gold_chip(base, (bk.MX, y), chip)
    y += chip_h + 22
    for ln in title_lines:
        bk.text_shadow(base, (bk.MX, y), ln, f_title, anchor="la", alpha=0.5, blur=5)
        d.text((bk.MX, y), ln, font=f_title, fill=bk.DORADO, anchor="la")
        y += t_h
    y += 10
    bk.text_shadow(base, (bk.MX, y), sub, f_sub, anchor="la", alpha=0.45, blur=4)
    d.text((bk.MX, y), sub, font=f_sub, fill=bk.BLANCO, anchor="la")
    y += 46 + 18
    for ln in sup_lines:
        d.text((bk.MX, y), ln, font=f_sup, fill=(235, 235, 235, 255), anchor="la")
        y += s_h
    bk.footer(base)
    return base


def story(path, keyword, headline, *, focus_y=0.5, focus_x=0.5, wm_op=0.85,
          stat=None, fact=None, source=None, hl_size=47):
    """Interior slide: clean sharp photo + small top-left logo + lower-third
    caption block (text zone darkened only)."""
    base = bk.cover(path, focus_y=focus_y, focus_x=focus_x)
    bk.watermark(base, width=190, opacity=wm_op)
    bk.caption_block(base, keyword, headline, stat=stat, fact=fact,
                     source=source, hl_size=hl_size)
    return base
