# Landing IBONNE TORO — Rediseño con Sistema de Agentes

Documento de los cambios aplicados a la landing en vivo (`index.html`, `styles.css`, `script.js`, `images/`).
Fecha: 8 de julio de 2026. Método: Sistema de Agentes (Director → Copywriter → Auditor) definido en `/SISTEMA_AGENTES_LANDING_PAGES`.

---

## 1. Estrategia (Director)

- **Ángulo narrativo:** *"el anti-portal"* — no vendemos abundancia de anuncios; vendemos criterio: una persona que ya recorrió el mercado y te dice cuál **no** comprar.
- **Posicionamiento:** *criterio sobre catálogo*. Marca personal con rostro frente al portal anónimo.
- **CTA único** en todos los puntos: escribir por WhatsApp / "Hablemos" (+57 310 497 33 36).

## 2. Copy (Copywriter + 3 auditorías anti-IA / CTA / flujo)

Reescrito **todo** el texto en primera persona de Ibonne, humano y conversacional:
- **Hero:** "En Manizales no te faltan anuncios. Te falta alguien que ya los revisó por ti."
- **Por qué Manizales:** 4 cifras verificadas con su fuente (Banco de la República, DANE–IGAC, La Haus, inventario propio).
- **Quiénes somos + 3 pilares**, **Proceso (4 pasos)**, **Bio de Ibonne** (con la objeción resuelta: *"trabajar conmigo no te encarece la propiedad"*).
- CTAs intermedios en los picos de intención (tras datos, tras pilares, tras proceso).

**Reglas de marca respetadas (nada inventado):** sin testimonios, sin % de ROI/rentabilidad, sin "años de experiencia", sin $/m² por barrio como dato duro.

## 3. Diseño e interactividad (Diseñador)

- **Explorador de sectores interactivo** — mapa/guía de Manizales con 5 pines + pestañas; al hacer clic cambia foto y ficha del sector. Sectores: **Baja Suiza, Milán, El Cable, Expoferias, La Florida**.
- **Simulador de valorización** — 3 deslizadores (monto, años, % anual); calcula el valor estimado en vivo y arma un WhatsApp con el escenario. Con **aviso de que es un estimado**, no una promesa (base +10% Banco de la República, ajustable).
- **Contadores animados** en la banda de datos.
- **Animaciones sutiles** al hacer scroll (reveal) — ya existían, se mantienen; respetan `prefers-reduced-motion`.

## 4. Nueva sección — "Mis inmuebles en Manizales"

Tres tarjetas con enlace a los **perfiles reales**:
- Metrocuadrado — `metrocuadrado.com/inmobiliaria/ibonne-toro/8578`
- Fincaraíz — `fincaraiz.com.co/inmobiliarias/perfil/174601569-ibonne-toro-inversiones-inmobiliarias`
- Properati — `properati.com.co/inmobiliaria/01915696-c834-7dd4-92cb-7de9c9280d8a`

Enmarcadas como *prueba* ("lo público está en los portales; lo mejor lo agendamos"), no como invitación a irse a navegar.

## 5. Detalles visuales

- **Logo más grande** (46→60px; 38→46px al hacer scroll).
- **Botón "Hablemos"** con más padding/aire.
- **Convención tipográfica:** empresa = **IBONNE TORO** (mayúsculas, `.brand-name`); persona/handle = **ibonnetoro** (minúsculas, `.brand-handle`).
- **Foto de Ibonne** reemplazada por el retrato profesional en la terraza con la Torre del Cable.
- Fotos nuevas de sector optimizadas para web (<450 KB c/u), sin repeticiones.

## 6. Mobile

- Verificado a 375px: **sin scroll horizontal**, pestañas de sector con scroll horizontal propio, CTAs largos que envuelven, tarjetas apiladas, botón flotante de WhatsApp.

## 7. Validación (Auditor)

- ✅ Sin elementos prohibidos (testimonios/ROI/años).
- ✅ WhatsApp idéntico en las 16 referencias; CTA coherente.
- ✅ Propuesta de valor clara en 5 segundos.
- ✅ Sin errores de consola; imágenes cargan; overflow horizontal nulo.
- Ajustes de pulido aplicados: copy del formulario alineado a su comportamiento real (abre WhatsApp), tildes en mensajes prellenados, dato del m² sin "todavía", "5 sectores" sin "premium".

## 8. Para publicar

El sitio se sirve por **GitHub Pages** con dominio `ibonnetoroinversionesinmobiliarias.com`.
Para que los cambios salgan en vivo hay que hacer commit y push de `index.html`, `styles.css`, `script.js` e `images/` a la rama que publica Pages. Los archivos duplicados en `LANDING_PAGE_IBONNE_TORO/` (copia fuente) pueden actualizarse aparte si se desea mantener el espejo.
