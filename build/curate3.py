"""Final adjusted selection (Ibonne's feedback): seated portraits + sharper,
higher-native-resolution premium photos. Copies the complete final set into
CARRUSELES_FINALES_CON_AJUSTES/FOTOS_CURADAS/ with friendly names."""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRCP = os.path.join(ROOT, "fotos_fuente", "Fotos inmuebles")
SRCS = os.path.join(ROOT, "fotos_fuente", "FOTOS IBONNE", "Ibonne Toro")
DEL  = os.path.join(ROOT, "carruseles", "CARRUSELES_FINALES_CON_AJUSTES")
CURP = os.path.join(DEL, "FOTOS_CURADAS", "inmuebles")
CURS = os.path.join(DEL, "FOTOS_CURADAS", "estudio_ibonne")

IDX = {}
for line in open(os.path.join(ROOT, "build", "review2", "index.tsv")):
    fid, f = line.rstrip("\n").split("\t"); IDX[fid] = f

# friendly -> (origin-id, carousel, slide, change?, why)
PROP = {
    "c1_atardecer_manizales": ("F142", "C1", "S2", "", "Atardecer sobre Manizales — dato +10%"),
    "c1_panoramica_ciudad":   ("F126", "C1", "S3", "", "Panorámica del valle — dato +6,48%"),
    "c1_balcon_ciudad":       ("F160", "C1", "S4", "", "Balcón panorámica — fondo tarjeta de datos"),
    "c1_campestre_terraza":   ("F150", "C1", "S5", "", "Terraza vista verde — sectores"),
    "c1_cocina_lujo_piscina": ("F104", "C1", "S6", "", "Cocina de lujo con piscina — calidad"),
    "c1_sala_vista_montana":  ("F161", "C1", "S7", "", "Sala con ventanal a montaña — espacios"),
    "c1_fachada_campestre":   ("F120", "C1", "S10", "", "Fachada campestre — visión de futuro"),
    "c2_sala_panoramica":     ("F166", "C2", "S1", "", "Sala panorámica ciudad — portada"),
    "c2_aerea_campestre":     ("F121", "C2", "S2", "", "Aérea verde + montañas — La Florida"),
    "c2_cocina_diseno":       ("F106", "C2", "S3", "CAMBIO", "Cocina abovedada de lujo 4032px (reemplaza F113 blanda) — San Marcel"),
    "c2_apto_vista":          ("F172", "C2", "S4", "", "Apto vista verde — Expoferias"),
    "c2_sala_familiar":       ("F201", "C2", "S5", "CAMBIO", "Comedor cálido amoblado, nítido (reemplaza F141 800x600 borrosa) — Bella Suiza"),
    "c2_terraza_panoramica":  ("F162", "C2", "S6", "", "Terraza panorámica — portafolio"),
    "c2_cocina_jardin":       ("F084", "C2", "S8", "CAMBIO", "Cocina luminosa con ventanal verde 4032px (reemplaza F006 mediocre) — acabados"),
    "c2_espacios_luz":        ("F102", "C2", "S9", "CAMBIO", "Espacios abiertos con luz 4032px (reemplaza F184 blanda) — diseño y luz"),
    "c2_sala_verde":          ("F202", "C2", "S10", "", "Sala ventanal verde — entorno que suma"),
}
STUDIO = {
    "ibonne_portada_terraza":     ("SRG00768", "C1", "S1", "", "Terraza con Catedral — portada"),
    "ibonne_eje_cafetero_sentada":("SRG00949", "C1", "S8", "CAMBIO", "SENTADA en mesa con mural Eje Cafetero (reemplaza de pie) — respaldo experto"),
    "ibonne_asesoria_tablet":     ("SRG01210", "C1", "S9", "", "Sentada con tablet — decisiones seguras"),
    "ibonne_cta_maqueta":         ("SRG01040", "C1", "S11", "", "Maqueta de casa en la palma — CTA"),
    "ibonne_equipo_traje_azul":   ("SRG01012", "C2", "S7", "CAMBIO", "SENTADA con profesional (traje azul) en reunión (reemplaza de pie) — equipo que respalda"),
    "ibonne_cta_sentada":         ("SRG01045", "C2", "S11", "CAMBIO", "SENTADA sonriente, cercana (reemplaza de pie) — CTA"),
}

def run():
    os.makedirs(CURP, exist_ok=True); os.makedirs(CURS, exist_ok=True)
    os.makedirs(os.path.join(DEL, "CONTROL"), exist_ok=True)
    rows = []
    for name, (fid, car, slide, chg, why) in PROP.items():
        shutil.copy2(os.path.join(SRCP, IDX[fid]), os.path.join(CURP, name + ".jpg"))
        rows.append((car, slide, name + ".jpg", fid, IDX[fid], chg, why)); print("ok", name, chg)
    for name, (sid, car, slide, chg, why) in STUDIO.items():
        shutil.copy2(os.path.join(SRCS, sid + ".jpg"), os.path.join(CURS, name + ".jpg"))
        rows.append((car, slide, name + ".jpg", sid, sid + ".jpg", chg, why)); print("ok", name, chg)
    with open(os.path.join(DEL, "CONTROL", "_rows.tsv"), "w") as fh:
        for r in rows: fh.write("\t".join(r) + "\n")
    print("DONE", len(rows))

if __name__ == "__main__":
    run()
