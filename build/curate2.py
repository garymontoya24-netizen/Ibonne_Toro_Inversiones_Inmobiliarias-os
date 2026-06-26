"""Copy the improved premium selection (clean, no-watermark) into the new
delivery folder with friendly names, and emit the photo-control records."""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRCP = os.path.join(ROOT, "Fotos inmuebles")
SRCS = os.path.join(ROOT, "FOTOS IBONNE", "Ibonne Toro")
DEL  = os.path.join(ROOT, "CARRUSELES_MEJORADOS_FINAL")
CURP = os.path.join(DEL, "FOTOS_CURADAS", "inmuebles")
CURS = os.path.join(DEL, "FOTOS_CURADAS", "estudio_ibonne")

# F-id -> filename
IDX = {}
for line in open(os.path.join(ROOT, "build", "review2", "index.tsv")):
    fid, f = line.rstrip("\n").split("\t"); IDX[fid] = f

# friendly name -> (F-id, carousel, slide, why)
PROP = {
    "c1_atardecer_manizales":   ("F142", "C1", "S2", "Atardecer sobre Manizales (Cerro Sancancio + skyline) — dato +10%"),
    "c1_panoramica_ciudad":     ("F126", "C1", "S3", "Panorámica del valle desde balcón — dato +6,48%"),
    "c1_balcon_ciudad":         ("F160", "C1", "S4", "Balcón con panorámica ciudad — fondo de tarjeta de datos"),
    "c1_campestre_terraza":     ("F150", "C1", "S5", "Terraza con vista a colinas verdes — sectores"),
    "c1_cocina_lujo_piscina":   ("F104", "C1", "S6", "Cocina de lujo con piscina y jardín — calidad que se nota"),
    "c1_sala_vista_montana":    ("F161", "C1", "S7", "Sala con ventanal a montaña — espacios con futuro"),
    "c1_fachada_campestre":     ("F120", "C1", "S10", "Fachada moderna campestre con jardín — visión de futuro"),
    "c2_sala_panoramica":       ("F166", "C2", "S1", "Sala con panorámica de ciudad — portada"),
    "c2_aerea_campestre":       ("F121", "C2", "S2", "Vista aérea verde + montañas — La Florida campestre"),
    "c2_cocina_diseno":         ("F113", "C2", "S3", "Cocina isla verde de diseño — San Marcel lujo"),
    "c2_apto_vista":            ("F172", "C2", "S4", "Apto moderno con vista verde — Expoferias"),
    "c2_sala_familiar":         ("F141", "C2", "S5", "Sala-comedor familiar amoblada — Bella Suiza"),
    "c2_terraza_panoramica":    ("F162", "C2", "S6", "Terraza con panorámica — portafolio/rango"),
    "c2_cocina_jardin":         ("F006", "C2", "S8", "Cocina con muro de vidrio a jardín — acabados"),
    "c2_comedor_diseno":        ("F184", "C2", "S9", "Comedor de diseño cálido — diseño y luz"),
    "c2_sala_verde":            ("F202", "C2", "S10", "Sala con ventanal verde — entorno que suma"),
}
STUDIO = {
    "ibonne_portada_terraza":   ("SRG00768", "C1", "S1", "Ibonne en terraza con Catedral — portada"),
    "ibonne_experta_corredor":  ("SRG01155", "C1", "S8", "Corredor de cristal, confianza — respaldo experto"),
    "ibonne_asesoria_tablet":   ("SRG01210", "C1", "S9", "Con tablet — decisiones seguras"),
    "ibonne_cta_maqueta":       ("SRG01040", "C1", "S11", "Maqueta de casa en la palma — CTA"),
    "ibonne_especialista":      ("SRG01142", "C2", "S7", "Arquitectura moderna, autoridad — especialista premium"),
    "ibonne_cta_sonrisa":       ("SRG01120", "C2", "S11", "Sonriente presentando — CTA"),
}

def run():
    os.makedirs(CURP, exist_ok=True); os.makedirs(CURS, exist_ok=True)
    rows = []
    for name, (fid, car, slide, why) in PROP.items():
        src = os.path.join(SRCP, IDX[fid]); dst = os.path.join(CURP, name + ".jpg")
        shutil.copy2(src, dst); rows.append((car, slide, name + ".jpg", fid, why))
        print("ok", name)
    for name, (sid, car, slide, why) in STUDIO.items():
        src = os.path.join(SRCS, sid + ".jpg"); dst = os.path.join(CURS, name + ".jpg")
        shutil.copy2(src, dst); rows.append((car, slide, name + ".jpg", sid, why))
        print("ok", name)
    rows.sort()
    with open(os.path.join(DEL, "CONTROL", "_rows.tsv"), "w") as fh:
        for r in rows: fh.write("\t".join(r) + "\n")
    print("DONE", len(rows), "photos")

if __name__ == "__main__":
    os.makedirs(os.path.join(DEL, "CONTROL"), exist_ok=True)
    run()
