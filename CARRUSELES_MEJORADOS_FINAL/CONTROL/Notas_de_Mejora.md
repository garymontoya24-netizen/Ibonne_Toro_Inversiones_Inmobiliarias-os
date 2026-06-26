# Notas de Mejora — Qué cambió y por qué

*Revisión sobre los carruseles V2.1. El contenido/copy de C1 se mantuvo (estaba aprobado); el trabajo fue visual y de selección.*

## Checklist de feedback → resuelto

| # | Problema | Solución aplicada |
|---|---|---|
| 1 | **Logos IG/WhatsApp feos/pixelados** | Reemplazados por los **glifos oficiales** de Instagram y WhatsApp (descargados de simple-icons, rasterizados a silueta blanca 512px con sombra suave). Aparecen junto a @ibonne_toro y al número en portada y CTA. |
| 2 | **Fotos opacas / overlay invasivo** | Rediseño "foto protagonista": se eliminó el velo superior; la foto queda limpia y **nítida** (se aplicó *unsharp mask* suave). Solo se oscurece la **franja inferior** donde va el texto. |
| 3 | **Texto pequeño / poco legible** | Tamaños subidos: titular 40→47px, keyword 25→28px, estadística 150→178px, contacto 26→28px, título de portada 58→62px. Sombra para contraste. |
| 4 | **Marca de agua en fotos** | Se cambió a la **carpeta nueva de fotos limpias** ("Fotos inmuebles/"), sin marca de agua horneada. Cero fotos con watermark ajeno. |
| 5 | **Calidad no siempre premium** | Curaduría estricta sobre 202 fotos: solo tomas "wow" (cocinas de lujo, vistas panorámicas, atardecer, comedores de diseño, fachadas campestres). Se descartaron fotos con gente (p. ej. F147, lobby con operario). |
| 6 | **Fotos repetidas (C2)** | **Cero repeticiones**: cada carrusel usa fotos distintas. Ver `Fotos_Usadas_Control.md`. |
| 7 | **Fotos en bloque** | En C2 se insertó el retrato de Ibonne ("especialista") en el **slide 7**, partiendo la secuencia; cada slide combina **foto + dato/copy** (no fotos desnudas). |
| 8 | **Coherencia foto–texto** | Cada foto refuerza su mensaje: campestre→casa con jardín y montaña; estrato 6/lujo→cocina de diseño "supercasota"; cocina premium→cocina real premium; vista→panorámica real. |
| + | **Gráfica (C1 S4) vacía** | Rediseñada: barras sobre una **panorámica real de Manizales oscurecida**, con conclusión en dorado *"Casi 30% más accesible que Bogotá"* y fuente citada. Ya no se ve vacía. |

## Jerarquía visual aplicada en cada slide
1. **Foto (60–70%)** — nítida, premium, protagonista (limpia arriba).
2. **Texto (30–40%)** — grande y legible, en la franja inferior oscurecida (dorado + blanco).
3. **Logo/contacto** — discretos (marca de agua pequeña arriba-izq.; logos oficiales en portada/CTA).

## Detalles técnicos (para el equipo)
- Glifos sociales: `build/svg_raster.py` (rasterizador SVG propio, sin dependencias de cairo) → `build/assets/social/*_white.png`.
- Plantillas: `build/slides.py` (`hero`, `story`) y `build/brandkit.py` (`caption_block`, `barchart`, `footer` con glifos).
- Scripts: `build/make_invest.py` (C1) y `build/make_sectores.py` (C2) → renderizan a `CARRUSELES_MEJORADOS_FINAL/`.
- Curaduría: `build/curate2.py` copia las fotos premium con nombres legibles a `FOTOS_CURADAS/`.

## Pendiente de confirmar con Ivonne (igual que antes)
1. Años de trayectoria (para un slide de experiencia).
2. OK a publicar el precio real del listado de San Marcel ($640M, público en Fincaraíz).
3. Encuadre "La Florida = campestre de Villamaría".
4. Validar $/m² de sector con la Lonja de Caldas si se publican como dato duro.

## Nota de honestidad sobre los sectores
Las 202 fotos vienen sin etiqueta de sector. Las fotos de los slides de sector **ilustran el carácter** de cada zona (campestre, estrato 6, familiar), no se afirma que cada toma sea exactamente esa dirección. Si Ivonne tiene la foto del inmueble real de cada sector, se sustituye en un minuto (basta cambiar un nombre de archivo en el script).
