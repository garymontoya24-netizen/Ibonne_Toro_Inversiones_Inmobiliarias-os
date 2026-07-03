# build/ — pipeline de carruseles

Generación de carruseles de IBONNE TORO con Python/Pillow (no Canva). Reproducible y exacto.

## Pipeline activo
| Archivo | Rol |
|---|---|
| `brandkit.py` | Sistema de marca: colores exactos (#2C3E50, #D4AF37, #FFFFFF), fuentes (Poppins/Lexend/Open Sans en `fonts/`), y componentes (`cover`, `hero`/`caption_block`, `gold_chip`, `barchart`, `footer` con glifos oficiales, `watermark`). |
| `slides.py` | Plantillas `hero` (portada/CTA) y `story` (interiores: foto-protagonista + bloque de texto inferior). |
| `make_invest.py` | **Carrusel 1** — "Por qué invertir en Manizales". |
| `make_sectores.py` | **Carrusel 2** — "Sectores premium". |
| `curate3.py` | Copia la selección final de fotos (con nombres legibles) a la entrega vigente. |
| `svg_raster.py` / `raster_icons.py` | Rasterizan los glifos oficiales de Instagram/WhatsApp (SVG → PNG blanco) a `assets/social/`. |

## Cómo regenerar
```bash
python3 build/make_invest.py
python3 build/make_sectores.py
```
Requiere Pillow + numpy. Editar la lista `SLIDES` del script para cambiar foto o texto. Las fotos curadas viven en `carruseles/CARRUSELES_FINALES_CON_AJUSTES/FOTOS_CURADAS/`.

## Rutas
Las fotos fuente están en `fotos_fuente/` y las entregas en `carruseles/` (raíz del repo). Los scripts usan esas rutas.

## Auxiliares / históricos
`montage.py`, `montage2.py` (hojas de contacto para curar), `curate.py`, `curate2.py`, `make_carousel.py` son de rondas anteriores; algunos referencian carpetas que ya no existen (p. ej. `Ejemplos Inmuebles`). Se conservan como historial. Las salidas de revisión (`review*/`, `out/`) son scratch y no se versionan.
