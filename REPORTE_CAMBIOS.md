# Reporte de cambios — Versión final profesional (investigación integrada)

Fecha: 8 de julio de 2026. Objetivo: copy **profesional, natural y sin IA**, basado en datos reales de Manizales, manteniendo la frescura pero elevando el nivel.

---

## FASE 1 · Investigación (datos reales usados)

Fuentes: La Haus, vivienda.com.co, DANE, Banco de la República, Ciencuadras, Fincaraíz.

- **Valorización 2025:** Manizales +10% en vivienda usada → **2ª del país**, solo detrás de Pereira (+11%).
- **Metro cuadrado nuevo (comparativa dura):** Manizales **$4,42M** vs **Bogotá $6,1M · Medellín $5,7M · Pereira $5,3M**. → El más accesible de todas.
- **Motor del mercado:** migración de familias desde las grandes capitales + turismo sostenido + ciudad intermedia en crecimiento.
- **Arriendo (El Cable / Palermo):** demanda de estudiantes y profesionales todo el año; **"vacancia habitacional casi nula"**; arriendo promedio zona Palermo/El Cable ~$3,9M/mes.
- **Lenguaje/tono:** el inversionista de Manizales valora la seguridad patrimonial y la cercanía; responde mejor a un tono **cercano pero experto**, sin sonar vendedor ni corporativo.

## FASE 2 · Diagnóstico del copy anterior

- Hero **"Manizales sube. Y no es corazonada."** → sonaba casual/copiado. Poco profesional.
- Diferenciador **"ya recorrí el mercado y te digo cuál sí y cuál no"** → correcto pero informal.
- **"¿No me crees? Míralo tú mismo"** → defensivo, transmitía inseguridad.
- Mapa abstracto (montañas SVG) → bonito pero **"genérico", no un mapa real**.
- Sección Ibonne → demasiada primera persona seguida.

## FASE 3 · Copy nuevo (sección por sección)

- **Hero:** *"Invierte en Manizales sin equivocarte."* + subtítulo con dato real ("se valoriza como pocas y cuesta menos que Bogotá o Medellín").
- **¿Por qué Manizales?:** título *"Se valoriza como pocas. Cuesta como ninguna capital grande."* + lead de 3 ideas (dato · motor · oportunidad). Stat del m² ahora con **comparativa real** (Bogotá/Medellín/Pereira).
- **Diferenciador:** *"Los portales te dan opciones. Yo te doy criterio."* (profesional, no informal).
- **Simulador:** contexto ANTES ("Así funciona: elige cuánto y por cuántos años") + resultado narrado DESPUÉS ("En X años, tu inversión sería $Y — eso es +$Z más de lo que pusiste") + aviso "estimado con datos reales, no una promesa".
- **Sección Ibonne:** equilibrio 3ª + 1ª persona — P1 quién es (tercera persona), P2 por qué diferente (primera), P3 compromiso (primera).
- **Cómo funciona:** *"De la primera charla a las llaves."* con 4 pasos naturales (Conversamos · Analizo opciones · Visitamos · Cierras con respaldo).
- **Portales:** positivo, no defensivo → *"Todo lo que publico, verificado y a la vista."*
- **Sectores:** texto previo reducido → *"Conozco estos cinco a fondo."* + gancho breve por sector.

## FASE 4 · Diseño

- **Mapa REAL de Manizales:** reemplazado el mapa abstracto por **OpenStreetMap** (calles y barrios reales, interactivo, con marcador y botón "Ver Manizales en el mapa"). Se mantiene el **explorador con fotos que cambian** por sector (lo que más gustó).
  - *Nota técnica:* se intentó Google Maps pero bloquea la incrustación sin API key (X-Frame-Options); OpenStreetMap es libre, incrustable y no requiere clave.
- **Portales con foto + chip de marca** (Metrocuadrado rojo, Fincaraíz verde, Properati turquesa) + botón "Ver mis inmuebles".
- **Simulador** con resultado resaltado en tarjeta azul + número dorado.
- **Sección de contacto** (WhatsApp / Instagram) con más aire, botones claros.

## FASE 5 · Detalles visuales

- Tipografía de marca: persona = **ibonne Toro** (negrita); agencia = **IBONNE TORO INVERSIONES INMOBILIARIAS** (mayúsculas, negrita).
- Botones con **más padding** (16×34).
- **Logo más grande** (66px; 50px al hacer scroll).
- Más espaciado general.

## FASE 6 · Fotos

- Portales con foto de inmueble real (una distinta por tarjeta). Sin repeticiones en el sitio.
- *Pendiente opcional:* si Ibonne tiene los **logos oficiales** de los portales en PNG/SVG, se reemplazan los chips de texto por los logos reales.

## FASE 7 · Validación

- ✅ Copy natural y profesional; sin frases que suenen a IA.
- ✅ Propuesta clara ("criterio, no catálogo").
- ✅ Simulador con contexto y resultado resaltado.
- ✅ Mapa real de Manizales (OSM) funcionando.
- ✅ Portales con foto + chip + botón.
- ✅ Móvil sin scroll horizontal; sin errores de consola; imágenes y mapa cargan.
- ✅ CTAs a WhatsApp en varios puntos; flujo hacia agendar.

## Notas / pendientes

- Dato del m² ($4,42M) es de La Haus (análisis multianual); la comparativa Bogotá/Medellín/Pereira es de la misma fuente.
- El tercer portal del brief ("Profit") es **Properati** (perfil real).
- Logos oficiales de portales: se pueden integrar si se proveen los archivos.
