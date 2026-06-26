# IBONNE TORO — Carruseles MEJORADOS (entrega final)

*Revisión sobre la V2.1, con el feedback de Gary aplicado. Junio 2026.*

## Estructura
```
CARRUSELES_MEJORADOS_FINAL/
├── _PREVIEW_carrusel_1.png         ← vista rápida de los 11 slides (C1)
├── _PREVIEW_carrusel_2.png         ← vista rápida de los 11 slides (C2)
├── carrusel_1_mejorado/            slide_01..11.png (1080x1350)
├── carrusel_2_mejorado/            slide_01..11.png (1080x1350)
├── FOTOS_CURADAS/
│   ├── estudio_ibonne/  (6 retratos usados)
│   └── inmuebles/       (16 fotos premium limpias usadas)
└── CONTROL/
    ├── Fotos_Usadas_Control.md     trazabilidad foto→slide, sin repeticiones
    └── Notas_de_Mejora.md          qué cambió y por qué (checklist del feedback)
```

## Lo que cambió frente a la V2.1
- **Logos reales** de Instagram y WhatsApp (siluetas blancas oficiales), en portada y CTA.
- **Foto protagonista**: nítida y limpia; solo se oscurece la franja del texto.
- **Texto más grande** y legible en preview de Instagram.
- **Fotos premium nuevas y limpias** (sin marca de agua), curadas de las 202 clasificadas.
- **Sin repeticiones** entre C1 y C2; fotos **distribuidas** (no en bloque).
- **Coherencia foto–texto** en cada slide.
- **Gráfica del slide 4** rediseñada (ya no se ve vacía): barras sobre panorámica de Manizales + conclusión en dorado.

## Antes de publicar (confirmar con Ivonne)
1. Años de trayectoria · 2. OK al precio real de San Marcel ($640M) · 3. Encuadre "La Florida = Villamaría campestre" · 4. (opcional) validar $/m² con la Lonja de Caldas.

## Editar / regenerar
`build/make_invest.py` (C1) y `build/make_sectores.py` (C2). Cambiar foto/texto en la lista `SLIDES` y correr `python3 build/make_invest.py`. Estrategia y datos completos: ver `../CARRUSELES_FINALES_V2_1/DOCUMENTOS_ESTRATEGIA/`.
