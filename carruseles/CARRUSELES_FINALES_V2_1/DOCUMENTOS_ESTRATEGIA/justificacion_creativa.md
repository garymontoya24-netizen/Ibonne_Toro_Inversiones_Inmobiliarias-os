# Justificación Creativa y de Diseño

*Documento 7 de 7 — Junio 2026.*

## Principio rector
Mantener **el mismo patrón de calidad del carrusel anterior** (que funcionó) y extenderlo con componentes nuevos para soportar un mensaje **data-driven**. Todo se genera por código (Python/Pillow), no Canva → reproducible, exacto y escalable para la serie.

## Color — exacto, sin aproximaciones
- **Azul oscuro #2C3E50** (44,62,80): fondos, overlays, tarjeta de datos.
- **Dorado #D4AF37** (212,175,55): chips, títulos, estadística grande, acentos, barra destacada.
- **Blanco #FFFFFF**: titulares y cuerpo.
Codificados como constantes; cero "casi dorado".

## Tipografía — jerarquía
- **Poppins Bold** → títulos y la estadística grande (sustituye a Bukra Wide del design system, no disponible; Poppins es la decisión validada en el carrusel anterior).
- **Poppins SemiBold** → keywords (con *tracking* en mayúsculas) y titulares de slide.
- **Lexend Deca** → subtítulos de portada.
- **Open Sans / Poppins Regular** → cuerpo, fuente de datos, contacto.
Tamaños: título 58px · stat 150px · titular 40px · keyword 25px · fuente 20px.

## Componentes (sistema reutilizable)
1. **Portada/CTA (`hero`)** — foto + degradado azul vertical + chip dorado + título dorado + subtítulo + footer con logo y contacto (IG + WhatsApp). Igual que el patrón previo.
2. **Bloque inferior (`caption_block`)** — keyword dorado + titular blanco, con **barra de acento dorada** a la izquierda (motivo de marca). Ahora admite:
   - **Estadística gigante dorada** (slides de dato: +10%, +6,48%).
   - **Línea de dato** con viñeta dorada (precios, m², estrato).
   - **Línea de fuente** pequeña (transparencia: de dónde sale el número).
3. **Tarjeta de datos (`solid_card` + `barchart`)** — fondo azul sólido + barras horizontales; Manizales en dorado, las demás ciudades en blanco tenue. Rompe el ritmo de fotos y refuerza el tono analítico.
4. **Marca de agua (`watermark`)** — logo blanco arriba-izquierda + leve scrim superior para legibilidad.

## Tratamiento fotográfico
- **Recorte 4:5 inteligente** con punto de foco por slide: en retratos, foco alto (0.12–0.22) para no cortar el rostro y dejar el tercio inferior para el copy; en interiores, foco centrado.
- **Degradado azul** más fuerte cuando hay estadística (legibilidad sobre cielos/atardeceres brillantes).
- **Sombras suaves** en textos sobre foto.

## Dos decisiones que conviene conocer
1. **Doble marca de agua.** Las fotos de inmueble ya traen un watermark "IBONNE TORO" horneado por el cliente. Para no competir, **bajé la opacidad de nuestra marca a ~0,4** en esos slides (en los de estudio se mantiene ~0,5). Si Ivonne prefiere una sola marca, puedo entregar las fotos de inmueble sin nuestra marca superpuesta.
2. **VETO de fondo aplicado.** Una candidata de estudio (SRG00885) tenía grafiti de fondo → la reemplacé por SRG01142 (corredor de cristal, fondo limpio y premium). Es el tipo de criterio que el brief pedía respetar.

## Legibilidad y consistencia
- Márgenes laterales 70px; bloque de texto siempre sobre zona oscurecida.
- Contacto idéntico en ambos cierres: **@ibonne_toro · +57 310 497 33 36**.
- Misma rejilla, mismos colores y misma tipografía en los 22 slides → la serie se reconoce como una sola voz.

## Cómo regenerar / editar (para el equipo)
- Código en `build/`: `brandkit.py` (sistema), `slides.py` (plantillas hero/story), `make_invest.py` (C1), `make_sectores.py` (C2).
- Editar el texto/foto en la lista `SLIDES` del script y correr `python3 build/make_invest.py` o `make_sectores.py`.
- Las fotos están organizadas en `FOTOS_CURADAS/`; cambiar una imagen es cambiar una línea.

> Resultado: dos carruseles **coherentes con el patrón ganador**, con un nuevo lenguaje de datos que eleva el posicionamiento de IBONNE TORO de "publica inmuebles" a "explica el mercado".
