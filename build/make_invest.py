"""CARRUSEL 1 (MEJORADO) — 'Por qué invertir en Manizales con IBONNE TORO'.
Copy unchanged (validated). Premium clean photos, photo-as-hero templates,
bigger text, official social glyphs, redesigned data card."""
import os
from PIL import ImageDraw
import brandkit as bk
from slides import hero, story

DEL = os.path.join(bk.ROOT, "carruseles", "CARRUSELES_FINALES_CON_AJUSTES")
CUR = os.path.join(DEL, "FOTOS_CURADAS")
OUT = os.path.join(DEL, "carrusel_1_ajustado")
os.makedirs(OUT, exist_ok=True)

def S(n): return os.path.join(CUR, "estudio_ibonne", n + ".jpg")
def P(n): return os.path.join(CUR, "inmuebles", n + ".jpg")


def datacard():
    """Slide 4 — comparison bars over a darkened Manizales backdrop + takeaway."""
    base = bk.cover(P("c1_balcon_ciudad"), focus_y=0.40)
    base.alpha_composite(bk.vgradient(bk.AZUL, [(0.0, 206), (1.0, 234)]))
    d = ImageDraw.Draw(base)
    bk.place_logo(base, bk.LOGO_WHITE, 200, (bk.MX, 60), opacity=0.92, anchor="lt", shadow=True)
    bk.draw_tracked(d, (bk.MX, 188), "PUNTO DE ENTRADA", bk.F_semi(28), bk.DORADO, 4)
    f_t = bk.F_bold(49)
    y = 232
    for ln in bk.wrap(d, "Invertir aquí cuesta menos —y se valoriza igual o más.", f_t, bk.W - 2*bk.MX):
        bk.text_shadow(base, (bk.MX, y), ln, f_t, anchor="la", alpha=0.5, blur=4)
        d.text((bk.MX, y), ln, font=f_t, fill=bk.BLANCO, anchor="la")
        y += f_t.getmetrics()[0] + f_t.getmetrics()[1] - 6
    d.text((bk.MX, y + 8), "Precio del m² de vivienda nueva (millones COP)",
           font=bk.F_reg(25), fill=(222, 222, 222, 255), anchor="la")
    items = [("Bogotá", 6.19, False), ("Medellín", 5.76, False),
             ("Pereira", 5.33, False), ("Manizales", 4.42, True)]
    endy = bk.barchart(base, items, x0=bk.MX, y0=y + 104, w=560, row_h=104, gap=30, vmax=6.6, unit="$")
    bk.gold_chip(base, (bk.MX, endy + 8), "CASI 30% MÁS ACCESIBLE QUE BOGOTÁ", fs=25, tracking=2)
    d.text((bk.W - bk.MX, bk.H - bk.MB - 2), "Referencia m² vivienda nueva 2022 · La Haus",
           font=bk.F_reg(20), fill=(208, 208, 208, 235), anchor="rs")
    return base


SLIDES = [
    ("slide_01.png", lambda: hero(
        S("ibonne_portada_terraza"), "INVERSIÓN INMOBILIARIA",
        "Manizales: donde tu inversión crece segura",
        "El patrimonio que más se valoriza, con quien mejor la conoce",
        "Asesoría experta en el corazón del Eje Cafetero.", focus_y=0.14)),
    ("slide_02.png", lambda: story(
        P("c1_atardecer_manizales"), "Valorización 2025",
        "Manizales fue la 2ª ciudad de Colombia que más valorizó su vivienda.",
        stat="+10%", source="Banco de la República · vivienda usada, 2025", focus_y=0.45)),
    ("slide_03.png", lambda: story(
        P("c1_panoramica_ciudad"), "Tu patrimonio, al alza",
        "El avalúo de la vivienda subió aquí más que en cualquier otra ciudad del país.",
        stat="+6,48%", source="DANE–IGAC · IVP 2025", focus_y=0.40)),
    ("slide_04.png", datacard),
    ("slide_05.png", lambda: story(
        P("c1_campestre_terraza"), "Dónde invertir",
        "San Marcel, Bella Suiza, Expoferias y La Florida marcan el ritmo del mercado.",
        fact="Estratos 4 a 6 · desde el norte consolidado hasta lo campestre", focus_y=0.40)),
    ("slide_06.png", lambda: story(
        P("c1_cocina_lujo_piscina"), "Calidad que se nota",
        "Elegimos cada inmueble por sus acabados, su luz y su vista.", focus_y=0.50)),
    ("slide_07.png", lambda: story(
        P("c1_sala_vista_montana"), "Espacios con futuro",
        "No vendemos metros cuadrados: vendemos decisiones que se valorizan.", focus_y=0.45)),
    ("slide_08.png", lambda: story(
        S("ibonne_eje_cafetero_sentada"), "Respaldo experto",
        "Conocemos Manizales y el Eje Cafetero como nadie. Esa es tu ventaja.", focus_y=0.24)),
    ("slide_09.png", lambda: story(
        S("ibonne_asesoria_tablet"), "Decisiones seguras",
        "Estudiamos cada detalle para que inviertas con datos, no con corazonadas.", focus_y=0.22)),
    ("slide_10.png", lambda: story(
        P("c1_fachada_campestre"), "Visión de futuro",
        "Invertir en Manizales hoy es asegurar tu tranquilidad mañana.", focus_y=0.50)),
    ("slide_11.png", lambda: hero(
        S("ibonne_cta_maqueta"), "HABLEMOS", "Descubre tu próxima inversión",
        "Asesoría sin costo, decisiones con respaldo",
        "Te ayudamos a dar el siguiente paso con seguridad.", focus_y=0.14)),
]

if __name__ == "__main__":
    for name, fn in SLIDES:
        bk.save(fn(), os.path.join(OUT, name)); print("rendered", name)
    print("DONE ->", OUT)
