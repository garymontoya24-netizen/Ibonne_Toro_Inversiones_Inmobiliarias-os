"""Render the 11-slide IBONNE TORO brand/services carousel."""
import os
from PIL import Image, ImageDraw
import brandkit as bk

ROOT = bk.ROOT
PH = os.path.join(ROOT, "FOTOS IBONNE")
OUT = os.path.join(ROOT, "build", "out")
os.makedirs(OUT, exist_ok=True)

def p(name): return os.path.join(PH, name)

# photo map
COVER     = p("Diseño sin título.jpg")
B1        = p("WhatsApp Image 2026-06-22 at 16.39.33.jpeg")        # full body, tablet, mural
C_LAUGH   = p("WhatsApp Image 2026-06-22 at 16.39.32 (4).jpeg")    # coffee client, laughing
B2        = p("WhatsApp Image 2026-06-22 at 16.39.34 (2).jpeg")    # seated, tablet, mural
DUO       = p("WhatsApp Image 2026-06-22 at 16.39.33 (2).jpeg")    # duo portrait
MEET      = p("WhatsApp Image 2026-06-22 at 16.39.33 (4).jpeg")    # collaborating at tablet
C_ATT     = p("WhatsApp Image 2026-06-22 at 16.39.32 (2).jpeg")    # coffee client, attentive
PHONE     = p("WhatsApp Image 2026-06-22 at 16.39.34 (4).jpeg")    # phone + tablet indoor
CITY      = p("WhatsApp Image 2026-06-22 at 16.39.35.jpeg")        # city + flowers
HANDSHAKE = p("WhatsApp Image 2026-06-22 at 16.39.34.jpeg")        # handshake
MODEL_ALT = p("WhatsApp Image 2026-06-22 at 16.39.34 (1).jpeg")    # house model in palm


# ----------------------------------------------------------- cover / CTA
def hero(path, chip, title, sub, support, focus_y=0.5, focus_x=0.5):
    base = bk.cover(path, focus_y=focus_y, focus_x=focus_x)
    base.alpha_composite(bk.vgradient(bk.AZUL, [(0.0, 30), (0.30, 0), (0.55, 110), (1.0, 250)]))
    d = ImageDraw.Draw(base)

    # measure text block (built top->down): chip, title, sub, support
    f_title = bk.F_bold(58)
    f_sub   = bk.F_sub(33)
    f_sup   = bk.F_reg(23)
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


# ----------------------------------------------------------- story slide
def story(path, keyword, headline, focus_y=0.5, focus_x=0.5, wm_op=0.55):
    base = bk.cover(path, focus_y=focus_y, focus_x=focus_x)
    bk.watermark(base, width=215, opacity=wm_op)
    bk.caption(base, keyword, headline)
    return base


SLIDES = [
    ("01.png", lambda: hero(
        COVER, "ASESORÍA INMOBILIARIA", "Compra, vende o invierte",
        "con total tranquilidad",
        "Acompañamiento experto en cada paso, en el corazón del Eje Cafetero.",
        focus_y=0.50)),
    ("02.png", lambda: story(
        B1, "Quiénes somos",
        "Más que vender inmuebles, construimos confianza.", focus_y=0.16)),
    ("03.png", lambda: story(
        C_LAUGH, "Asesoría cercana",
        "Te escuchamos para entender lo que de verdad buscas.", focus_y=0.10)),
    ("04.png", lambda: story(
        B2, "Experiencia local",
        "Conocemos Manizales y el Eje Cafetero como nadie.", focus_y=0.12)),
    ("05.png", lambda: story(
        DUO, "Respaldo profesional",
        "Un equipo que te acompaña de principio a fin.", focus_y=0.08)),
    ("06.png", lambda: story(
        MEET, "Análisis experto",
        "Estudiamos cada detalle para que decidas con seguridad.", focus_y=0.16)),
    ("07.png", lambda: story(
        C_ATT, "Confianza real",
        "Relaciones que nacen del trato honesto y cercano.", focus_y=0.12)),
    ("08.png", lambda: story(
        PHONE, "Respuesta ágil",
        "Resolvemos tus dudas con rapidez, cuando lo necesitas.", focus_y=0.16)),
    ("09.png", lambda: story(
        CITY, "Siempre contigo",
        "Disponibles donde estés, en cada momento del proceso.", focus_y=0.30)),
    ("10.png", lambda: story(
        HANDSHAKE, "Cierre seguro",
        "Cerramos cada negocio con respaldo y transparencia.", focus_y=0.20)),
    ("11.png", lambda: hero(
        MODEL_ALT, "Contáctanos", "Tu próximo hogar te espera",
        "Escríbenos hoy y te asesoramos",
        "Estamos listos para ayudarte a dar el siguiente paso.",
        focus_y=0.16)),
]

if __name__ == "__main__":
    for name, fn in SLIDES:
        img = fn()
        bk.save(img, os.path.join(OUT, name))
        print("rendered", name)
    print("DONE ->", OUT)
