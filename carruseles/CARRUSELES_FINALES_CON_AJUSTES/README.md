# IBONNE TORO — Carruseles FINALES CON AJUSTES

*Ajustes de Ibonne aplicados sobre la versión mejorada. Junio 2026.*

## Estructura
```
CARRUSELES_FINALES_CON_AJUSTES/
├── _PREVIEW_carrusel_1.png / _PREVIEW_carrusel_2.png
├── carrusel_1_ajustado/   slide_01..11.png (1080x1350)
├── carrusel_2_ajustado/   slide_01..11.png (1080x1350)
├── FOTOS_CURADAS/  estudio_ibonne/ + inmuebles/
└── CONTROL/  Fotos_Usadas_Control_Actualizado.md
```

## Qué cambió en esta versión (7 sustituciones)
| Slide | Antes | Ahora |
|---|---|---|
| **C1 S8** | Ibonne de pie | **Ibonne SENTADA** con tablet frente al mural del Eje Cafetero |
| **C2 S3** (San Marcel) | Cocina blanda (985px) | **Cocina abovedada de lujo 4032px** (la más nítida) |
| **C2 S5** (Bella Suiza) | Foto 800×600 borrosa | **Comedor cálido amoblado, nítido** |
| **C2 S7** | Ibonne de pie | **Ibonne SENTADA con un profesional** (equipo) + copy nuevo |
| **C2 S8** (acabados) | Cocina mediocre | **Cocina luminosa con ventanal verde 4032px** |
| **C2 S9** (diseño y luz) | Foto blanda | **Espacios abiertos con isla de mármol 4032px** |
| **C2 S11** (CTA) | Ibonne de pie | **Ibonne SENTADA**, sonriente y cercana |

Todo lo demás (logos oficiales IG/WhatsApp, foto-protagonista, texto grande, tarjeta de datos del slide 4, copy aprobado) se mantiene de la versión mejorada.

## Método de auditoría de calidad
Se midió **nitidez objetiva** (varianza del Laplaciano) y **resolución nativa** de todas las fotos de C2. Las que quedaban por debajo del umbral —p. ej. la de Bella Suiza era de solo 800×600 px, por eso se veía borrosa al ampliarla a 1080— se reemplazaron por tomas **4032×3024 px nítidas**. Solo fotos "wow". Detalle y trazabilidad en `CONTROL/Fotos_Usadas_Control_Actualizado.md`.

## Pendiente de confirmar con Ivonne
Años de trayectoria · OK al precio real de San Marcel ($640M) · encuadre "La Florida = Villamaría campestre" · (opcional) validar $/m² con la Lonja de Caldas.

## Editar / regenerar
`build/make_invest.py` (C1) y `build/make_sectores.py` (C2) → salen a esta carpeta. Estrategia y datos: `../CARRUSELES_FINALES_V2_1/DOCUMENTOS_ESTRATEGIA/`.
