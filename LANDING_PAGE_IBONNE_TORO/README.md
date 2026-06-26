# Landing Page · IBONNE TORO Inversiones Inmobiliarias

Página web de una sola pantalla (landing) para **IBONNE TORO**, asesora inmobiliaria en
Manizales y el Eje Cafetero. Construida para transmitir **confianza, seguridad y
tranquilidad**, con el sistema de marca (azul `#2C3E50` · dorado `#D4AF37` · blanco) y
copy sintetizado de los materiales existentes. Sin frameworks: HTML + CSS + JS puro.

---

## 📁 Estructura

```
LANDING_PAGE_IBONNE_TORO/
├── index.html              Página completa (todas las secciones)
├── styles.css              Estilos (design system + responsive)
├── script.js               Interacciones (menú, scroll, formulario→WhatsApp)
├── favicon.svg             Ícono de marca (casa dorada sobre azul)
├── images/                 Fotos optimizadas para web (~3,3 MB total)
├── Análisis_Marca_Ibonne.md   Investigación de marca (FASE 1)
└── README.md               Este archivo
```

### Secciones de la página
1. **Hero** — atardecer sobre Manizales + titular + CTA a WhatsApp
2. **Por qué Manizales** — 4 cifras de mercado verificadas (con fuente)
3. **Quiénes somos** — propuesta + 3 pilares de confianza
4. **Sectores** — San Marcel · Expoferias · Bella Suiza · La Florida
5. **Proceso** — 4 pasos (Conversamos → Analizamos → Proponemos → Acompañamos)
6. **Ibonne** — retrato profesional + bio + datos
7. **Portafolio** — galería de inmuebles premium
8. **Contacto** — CTA final + formulario que abre WhatsApp
9. **Footer** — logo, redes, portales, contacto

---

## 🚀 Cómo verla

**Opción rápida (doble clic):** abre `index.html` en cualquier navegador.

**Opción recomendada (servidor local)** — evita restricciones de algunos navegadores:

```bash
cd LANDING_PAGE_IBONNE_TORO
python3 -m http.server 8000
# luego abre http://localhost:8000
```

Funciona 100 % offline; solo las fuentes (Google Fonts) requieren internet. Si no hay
conexión, el navegador usa fuentes del sistema sin romper el diseño.

---

## 🌐 Cómo publicarla (gratis)

La página es 100 % estática, así que se sube tal cual:

- **Netlify** → arrastra la carpeta `LANDING_PAGE_IBONNE_TORO/` a netlify.com/drop.
- **Vercel** → `vercel` desde la carpeta, o conéctala a un repositorio.
- **GitHub Pages** → sube la carpeta a un repo y activa Pages.
- **Hosting propio** → copia la carpeta a `public_html/`.

Dominio sugerido para el futuro: `ibonnetoro.com` (hoy no existe sitio web; esta es la
oportunidad de ocuparlo — ver `Análisis_Marca_Ibonne.md`).

---

## ✏️ Cómo editar lo más común

| Quiero cambiar… | Dónde |
|---|---|
| **Número de WhatsApp** | `script.js` → variable `WHATSAPP_NUMBER` (y los enlaces `wa.me/...` en `index.html`) |
| **Textos / titulares** | `index.html` (todo el copy está en español, inline) |
| **Colores / tipografía** | `styles.css` → bloque `:root` (variables) |
| **Fotos** | reemplaza los archivos en `images/` con el mismo nombre |
| **Sectores / cifras** | secciones `#sectores` y `#manizales` en `index.html` |

### El formulario de contacto
No requiere servidor: al enviar, **arma un mensaje de WhatsApp prellenado** con los datos
y abre el chat de Ibonne. Es la vía más confiable sin backend.

> Si más adelante hay **correo propio** o un servicio de formularios (Formspree, Netlify
> Forms, etc.), está documentado en `script.js` dónde conectarlo (variable `CONTACT_EMAIL`).

---

## ⚠️ Datos a confirmar con Ibonne antes de publicar

1. **WhatsApp.** Se usó el número **verificado** en todos los materiales del proyecto:
   **+57 310 497 33 36** (`573104973336`). *El brief traía `+573014973338`, que difiere —
   confirmar cuál es el correcto antes de publicar.*
2. **Correo electrónico.** No existe correo propio verificado; el formulario va por WhatsApp.
   Si hay correo, agrégalo (ver arriba).
3. **Años de trayectoria.** No se afirma ninguna cifra de años porque no es pública. Si Ibonne
   confirma el dato, puede añadirse a la sección "Ibonne".
4. **$/m² por sector.** Las referencias de sector son descriptivas; validar con la **Lonja de
   Caldas** si se quieren publicar cifras duras.

---

## 🎨 Sistema de marca aplicado

- **Colores:** `#2C3E50` (azul) · `#D4AF37` (dorado) · `#FFFFFF` · `#F5F5F5` (gris claro).
- **Tipografía:** Poppins (títulos) · Open Sans (cuerpo) · Lexend Deca (acentos).
- **Responsive:** móvil, tablet y escritorio (menú hamburguesa en móvil).
- **Rendimiento:** imágenes optimizadas y comprimidas, carga diferida (`lazy`), animaciones
  ligeras que respetan `prefers-reduced-motion`.
- **Fotos:** estudio de marca personal de Ibonne + set premium de inmuebles, ya curados.

---

*Construido a partir de la investigación y los activos existentes del proyecto. Toda cifra de
mercado cita su fuente; ver `Análisis_Marca_Ibonne.md` para el detalle de qué es verificado y
qué es inferido.*
