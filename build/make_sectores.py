"""CARRUSEL 2 (MEJORADO) — 'Sectores Premium de Manizales que maneja IBONNE TORO'.
New premium clean photos (no repeats with C1), distributed (person slide breaks
the sequence), each photo matched to its sector's character."""
import os
import brandkit as bk
from slides import hero, story

DEL = os.path.join(bk.ROOT, "carruseles", "CARRUSELES_FINALES_CON_AJUSTES")
CUR = os.path.join(DEL, "FOTOS_CURADAS")
OUT = os.path.join(DEL, "carrusel_2_ajustado")
os.makedirs(OUT, exist_ok=True)

def S(n): return os.path.join(CUR, "estudio_ibonne", n + ".jpg")
def P(n): return os.path.join(CUR, "inmuebles", n + ".jpg")


SLIDES = [
    ("slide_01.png", lambda: hero(
        P("c2_portada_atardecer"), "SECTORES PREMIUM",
        "La Florida · San Marcel · Bella Suiza · Expoferias",
        "Baja Suiza · Milán · El Cable",
        "Donde Manizales vive mejor — y donde IBONNE TORO te abre la puerta.", focus_y=0.45)),
    ("slide_02.png", lambda: story(
        P("c2_aerea_campestre"), "La Florida · Villamaría",
        "Vida campestre con vista al Nevado, a minutos de la ciudad.",
        fact="Casas y condominios desde ~$540M · exclusividad rodeada de verde", focus_y=0.50)),
    ("slide_03.png", lambda: story(
        P("c2_cocina_diseno"), "San Marcel",
        "Estrato 6 en el oriente: conjuntos con amenidades y plusvalía sostenida.",
        fact="Apto 89 m², 3 hab — $640M · listado real IBONNE TORO", focus_y=0.50)),
    ("slide_04.png", lambda: story(
        P("c2_vista_ciudad_panoramica"), "Expoferias",
        "El corazón universitario y clínico: la renta más sólida de Manizales.",
        fact="Estrato 6 · demanda de arriendo todo el año", focus_y=0.50)),
    ("slide_05.png", lambda: story(
        P("c2_sala_familiar"), "Bella Suiza",
        "Tranquilidad, topografía plana y conjuntos familiares consolidados.",
        fact="≈ $6,7M/m² · estrato 4–5 · club house y zonas verdes", focus_y=0.50)),
    ("slide_06.png", lambda: story(
        P("c2_terraza_panoramica"), "Un portafolio para cada meta",
        "Desde la entrada más inteligente hasta la finca de los sueños.",
        fact="Inventario IBONNE TORO: desde $228M hasta fincas de $3.900M", focus_y=0.42)),
    # 7 — Ibonne SENTADA con un profesional (equipo) — rompe la secuencia
    ("slide_07.png", lambda: story(
        S("ibonne_equipo_traje_azul"), "Equipo que te respalda",
        "Estudiamos cada proceso junto a un equipo de profesionales.", focus_y=0.30)),
    ("slide_08.png", lambda: story(
        P("c2_cocina_jardin"), "Acabados premium",
        "Cocinas que enamoran. Detalles que valorizan.", focus_y=0.50)),
    ("slide_09.png", lambda: story(
        P("c2_espacios_luz"), "Diseño y luz",
        "Espacios pensados para vivir bien y para invertir mejor.", focus_y=0.50)),
    ("slide_10.png", lambda: story(
        P("c2_balcon_terraza_verde"), "El entorno que suma",
        "Vistas verdes, naturaleza y ciudad: el lujo silencioso de Manizales.", focus_y=0.42)),
    ("slide_11.png", lambda: hero(
        S("ibonne_cta_sentada"), "¿CUÁL ES TU SECTOR?", "Tu lugar en Manizales te espera",
        "Escríbenos y te asesoramos sin costo",
        "IBONNE TORO · Inversiones Inmobiliarias.", focus_y=0.18)),
]

if __name__ == "__main__":
    for name, fn in SLIDES:
        bk.save(fn(), os.path.join(OUT, name)); print("rendered", name)
    print("DONE ->", OUT)
