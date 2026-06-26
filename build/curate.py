"""Copy the curated + reserved photo selections into the delivery folders.
Studio shoot = the constrained '97' asset (use few). Property photos = the
'7 inmuebles' asset (separate; show 2-3 per property)."""
import os, shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEL  = os.path.join(ROOT, "CARRUSELES_FINALES_V2_1")
STUDIO = os.path.join(ROOT, "FOTOS IBONNE", "Ibonne Toro")
PROP   = os.path.join(ROOT, "Ejemplos Inmuebles")

CUR = os.path.join(DEL, "FOTOS_CURADAS")
RES = os.path.join(DEL, "FOTOS_RESERVADAS")

def ensure(*paths):
    for p in paths: os.makedirs(p, exist_ok=True)

def cp(src, dstdir, newname=None):
    if not os.path.exists(src):
        print("  !! MISSING:", src); return
    ensure(dstdir)
    base = newname or os.path.basename(src)
    shutil.copy2(src, os.path.join(dstdir, base))
    print("  ok", os.path.relpath(os.path.join(dstdir, base), DEL))

def srg(n): return os.path.join(STUDIO, f"SRG0{n}.jpg")
def prop(folder, f): return os.path.join(PROP, folder, f)

# ---------------- CURATED (used in the two carousels) ----------------
# Studio (Ibonne, the expert) — ~12 of the 97
STUDIO_CUR = {
    "0768": "terraza catedral Manizales, blusa verde (PORTADA C1)",
    "0765": "terraza vista ciudad, blusa verde",
    "0789": "cafe tablet, asesoria cercana",
    "0885": "blazer negro brazos cruzados, autoridad",
    "0949": "mural Eje Cafetero, identidad local",
    "0990": "duo con socio, respaldo de equipo",
    "1028": "blazer negro arquitectura moderna",
    "1040": "mano abierta presentando (CTA)",
    "1120": "sonriente presentando tablet (CTA)",
    "1142": "corredor de cristal, premium (PORTADA C2)",
    "1155": "corredor de cristal, sonrisa confiada",
    "1210": "sentada interior con tablet, asesoria",
}
# Property (real inventory) — 2-3 per property
PROP_CUR = {
    "Apto. Niza":                 [("9.png","atardecer skyline Manizales"),("3.png","cocina premium isla"),("8.png","vista montana ventanal"),("10.png","bano marmol")],
    "Apto. Av. Santander 570":    [("5.png","sala amoblada luz calida"),("2.png","cocina moderna madera"),("7.png","balcon vista verde")],
    "Casa SectoExpoferias":       [("14.png","habitacion con vista verde"),("17.png","jardin sendero verde"),("2.png","cocina moderna")],
    "Casa en San Marcel":         [("6.png","escalera flotante"),("3.png","cocina con isla")],
    "Apto. Cipres de Bella Suiza":[("3.png","sala amoblada"),("4.png","balcon vista")],
    "CASA LA FLORIDA 640":        [("6.jpg","patio trasero verde")],
}

# ---------------- RESERVED (future carousels / web / reels) ----------------
STUDIO_RES = ["0760","0772","0792","0871","0876","0905","0938","0945","0954",
              "0958","0962","0970","1023","1045","1056","1063","1073","1089",
              "1093","1100","1158","1186","1206","1250","1256"]
PROP_RES = {
    "Apto. Niza":                 ["4.png","5.png","6.png","11.png"],
    "Apto. Av. Santander 570":    ["3.png","4.png","6.png","8.png","9.png"],
    "Casa SectoExpoferias":       ["10.png","13.png","18.png","19.png","3.png","15.png","16.png"],
    "Casa en San Marcel":         ["5.png","7.png","14.png","16.png","12.png"],
    "Apto. Cipres de Bella Suiza":["5.png","14.png","2.png"],
}

if __name__ == "__main__":
    print("== CURATED studio ==")
    for n, why in STUDIO_CUR.items():
        cp(srg(n), os.path.join(CUR, "estudio_ibonne"), f"SRG0{n}.jpg")
    print("== CURATED inmuebles ==")
    for folder, items in PROP_CUR.items():
        safe = folder.replace(" ", "_").replace(".", "")
        for f, why in items:
            cp(prop(folder, f), os.path.join(CUR, "inmuebles", safe), f)
    print("== RESERVED studio ==")
    for n in STUDIO_RES:
        cp(srg(n), os.path.join(RES, "estudio_ibonne"), f"SRG0{n}.jpg")
    print("== RESERVED inmuebles ==")
    for folder, items in PROP_RES.items():
        safe = folder.replace(" ", "_").replace(".", "")
        for f in items:
            cp(prop(folder, f), os.path.join(RES, "inmuebles", safe), f)
    print("DONE")
