# IBONNE TORO — Carruseles V2.1 (entrega)

*Junio 2026. El primero de una serie. Recurso fotográfico cuidado: solo 7 retratos de estudio impresos de los ~97.*

## Qué hay aquí

```
CARRUSELES_FINALES_V2_1/
├── _PREVIEW_carrusel_1.png            ← vista rápida de los 11 slides (C1)
├── _PREVIEW_carrusel_2.png            ← vista rápida de los 11 slides (C2)
├── carrusel_1_por_que_invertir_manizales_con_ibonne/   slide_01..11.png (1080x1350)
├── carrusel_2_sectores_premium_ibonne/                 slide_01..11.png (1080x1350)
├── FOTOS_CURADAS/        estudio_ibonne/ (12) + inmuebles/ (por propiedad)
├── FOTOS_RESERVADAS/     25 retratos + ~24 fotos de inmueble para la serie futura
└── DOCUMENTOS_ESTRATEGIA/
    ├── analisis_ibonne_toro.md
    ├── analisis_ejecutivo_inmobiliaria.md
    ├── datos_sectores_premium.md
    ├── curacion_fotos_explicada.md
    ├── fotos_de_sectores_encontradas.md
    ├── narrativa_y_estrategia.md
    └── justificacion_creativa.md
```

## Los dos carruseles
- **C1 — "Por qué invertir en Manizales con IBONNE TORO":** el argumento. Datos reales de mercado (valorización +10%, avalúo +6,48%, comparativa de precios) que posicionan a Ibonne como experta. Tono data-driven.
- **C2 — "Sectores Premium":** el deseo. La Florida, San Marcel, Bella Suiza y Expoferias con inventario real de Ibonne. Tono aspiracional.

## Antes de publicar (4 cosas a confirmar con Ivonne)
1. Años de trayectoria (para un slide de experiencia).
2. OK a mostrar el precio del listado real de San Marcel ($640M, ya público en Fincaraíz).
3. Encuadre "La Florida = campestre de Villamaría".
4. (Opcional) Validar $/m² de sector con la Lonja de Caldas.

## Cómo se hizo / cómo editar
Pipeline en `../build/`: `brandkit.py`, `slides.py`, `make_invest.py` (C1), `make_sectores.py` (C2).
Editar texto/foto en la lista `SLIDES` y correr `python3 build/make_invest.py` o `make_sectores.py`.

**Datos:** ver `DOCUMENTOS_ESTRATEGIA/` para fuentes, método (verificado vs inferencia) y la justificación de cada decisión.
