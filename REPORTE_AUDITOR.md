# Reporte del Auditor — Iteración 2

Fecha: 8 de julio de 2026. El auditor lideró: identificó problemas reales (inspección en móvil), coordinó los arreglos y **validó cada cambio** en el navegador.

---

## Problemas identificados (con causa raíz)

| # | Problema | Causa real encontrada |
|---|---|---|
| 1 | **Móvil:** el eyebrow dorado ("ASESORA INMOBILIARIA · MANIZALES Y EJE CAFETERO") se **encimaba con el logo** IBONNE TORO | El hero centraba el contenido y el `padding-top` (90px) era menor que la altura del header (~102px) → el eyebrow quedaba debajo del logo. |
| 2 | **Botón "Hablemos" apretujado, sin padding** | Bug de **especificidad CSS**: `.nav a{padding:6px 0}` (0,1,1) le ganaba a `.nav-cta{padding}` (0,1,0). El botón nunca recibió su padding horizontal. |
| 3 | **Mapa fijo**, no cambiaba por sector | El mapa era un OpenStreetMap estático (una sola ubicación). |
| 4 | **Colores de portales** no eran los pedidos | Estaban en rojo/verde/turquesa. |
| 5 | **Copy postizo:** "Cuesta como ninguna capital grande" (y "se valoriza como pocas") | Frases armadas, poco naturales. |
| 6 | **Simulador:** copy pasivo, no invitaba a usarlo | Explicaba en vez de enganchar. |

## Cambios realizados (uno por uno)

1. **Overlap móvil** → en móvil el hero ahora alinea el contenido **arriba** (`align-items:flex-start`) y el `padding-top` sube a 120–132px. El eyebrow queda **claramente debajo del logo**.
2. **Botón "Hablemos"** → regla de mayor especificidad `.nav a.nav-cta{padding:14px 34px}`. Ahora respira.
3. **Mapa interactivo** → cada sector tiene **coordenadas reales** (geocodificadas con OpenStreetMap). Al tocar un sector, el mapa **se recentra** en esa zona y la foto cambia. Baja Suiza, Milán, El Cable, Expoferias y La Florida.
4. **Colores de portales** → Metrocuadrado **naranja** (#FF7A00), Fincaraíz **azul** (#0047AB), Properati **verde** (#00A24A).
5. **Copy** → título de datos ahora directo: *"Se valoriza rápido y todavía cuesta menos que Bogotá o Medellín."* Se quitó "como pocas / como ninguna capital grande".
6. **Simulador** → invita a interactuar: *"¿Cuánto tendrías en unos años? Elige el monto y el tiempo... Números, no promesas."*
7. **Extra:** cache-busting `?v=2` en CSS y JS (durante la revisión el navegador servía archivos viejos; esto asegura que los usuarios reciban siempre la versión nueva).

## Validación (auditor activo)

| Área | ¿Pasó? | Evidencia |
|---|---|---|
| Móvil: sin sobreposiciones | ✅ SÍ | Screenshot 375px: eyebrow debajo del logo, sin encimar. |
| Botón "Hablemos": padding | ✅ SÍ | `padding` computado = 14px 34px (antes 6px 0). |
| Mapa interactivo por sector | ✅ SÍ | Al tocar El Cable, el marcador cambió de 5.05536,-75.47960 a 5.05634,-75.48642. |
| Colores portales | ✅ SÍ | Metro naranja (255,122,0) · Finca azul (0,71,171) · Properati verde (0,162,74). |
| Copy sin frases postizas | ✅ SÍ | Reescrito el título de datos y el subtítulo del hero. |
| Simulador invita a usar | ✅ SÍ | Nuevo copy en pregunta directa. |
| Sin scroll horizontal (móvil) | ✅ SÍ | scrollWidth = viewport (375). |
| Sin errores de consola | ✅ SÍ | Consola limpia. |

## Testing

- **Móvil (375px):** hero sin overlap, tabs de sector con scroll horizontal, mapa y fotos cambian, sin desbordes.
- **Desktop:** layout de 2–4 columnas correcto; botón "Hablemos" con aire.
- **Interactividad:** mapa recentra + foto cambia en los 5 sectores; simulador calcula en vivo.

**Veredicto del auditor: APROBADO.**
