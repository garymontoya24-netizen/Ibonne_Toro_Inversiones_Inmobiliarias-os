# IBONNE TORO — Inversiones Inmobiliarias

Repositorio de **marketing y contenido** de Ibonne Toro (asesora inmobiliaria, Manizales / Eje Cafetero): carruseles para Instagram, fotografía fuente, material de apoyo, el pipeline que genera las piezas y la landing page.

## Estructura

```
.
├── carruseles/            ← ENTREGABLES (piezas para Instagram, 1080×1350)
│   ├── CARRUSELES_FINALES_CON_AJUSTES/   ← ★ VERSIÓN VIGENTE (la más reciente)
│   ├── CARRUSELES_MEJORADOS_FINAL/        versión intermedia (logos reales, foto-protagonista)
│   └── CARRUSELES_FINALES_V2_1/           versión inicial + DOCUMENTOS_ESTRATEGIA/
│
├── fotos_fuente/          ← FOTOGRAFÍA FUENTE (materia prima, no publicar en crudo)
│   ├── FOTOS IBONNE/        estudio de marca personal (retratos de Ibonne)
│   ├── Fotos inmuebles/     ~202 fotos de inmuebles clasificables
│   ├── Fotos/               vistas y balcones (lote julio 2026)
│   └── FOTOS ESPECIFICAS/   fotos puntuales (p. ej. portadas)
│
├── material_apoyo/        ← REFERENCIAS Y DISEÑO
│   ├── files/              design system (1_DESIGN_SYSTEM_IBONNE_TORO.md)
│   ├── Referencias/        logo, ejemplos de piezas, referencias visuales
│   └── Videos/             videos de propiedades
│
├── build/                 ← PIPELINE (Python/Pillow que genera los carruseles) — ver build/README.md
│
├── LANDING_PAGE_IBONNE_TORO/   copia fuente de la landing
└── index.html · styles.css · script.js · favicon.svg · images/   ← LANDING PAGE en vivo (GitHub Pages)
```

## Carruseles (lo importante)
- La **versión vigente** está en [`carruseles/CARRUSELES_FINALES_CON_AJUSTES/`](carruseles/CARRUSELES_FINALES_CON_AJUSTES). Ahí están los dos carruseles finales (`carrusel_1_ajustado/`, `carrusel_2_ajustado/`), las fotos curadas y el control de fotos.
- La **estrategia, investigación y datos** (análisis de Ibonne, sectores premium de Manizales, fuentes) están en [`carruseles/CARRUSELES_FINALES_V2_1/DOCUMENTOS_ESTRATEGIA/`](carruseles/CARRUSELES_FINALES_V2_1/DOCUMENTOS_ESTRATEGIA).

## Regenerar los carruseles
Requiere Python con Pillow + numpy.
```bash
python3 build/make_invest.py     # Carrusel 1 — "Por qué invertir en Manizales"
python3 build/make_sectores.py   # Carrusel 2 — "Sectores premium"
```
Para cambiar una foto o un texto: editar la lista `SLIDES` del script correspondiente. Detalle del sistema en [`build/README.md`](build/README.md).

## Landing page
El sitio en vivo se sirve por **GitHub Pages**. Los archivos de la raíz (`index.html`, `styles.css`, `script.js`, `favicon.svg`, `images/`) y la rama `gh-pages` **no deben moverse** sin revisar la configuración de Pages, para no romper el sitio.

## Nota
La fotografía en `fotos_fuente/` es materia prima curada por proyecto; no se publica en crudo. Cada entrega documenta qué fotos usó en su carpeta `CONTROL/`.
