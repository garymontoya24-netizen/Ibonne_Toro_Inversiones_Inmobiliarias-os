/* ============================================================
   IBONNE TORO · Landing Page — interacciones
   ============================================================ */
(function () {
  'use strict';

  // ---- CONFIGURACIÓN DE CONTACTO ----
  // Número de WhatsApp verificado de IBONNE TORO (formato internacional, sin "+").
  var WHATSAPP_NUMBER = '573104973336'; // +57 310 497 33 36
  // Si en el futuro hay correo propio, defínelo aquí para activar el envío por email.
  var CONTACT_EMAIL = ''; // p. ej. 'contacto@ibonnetoro.com'

  var header   = document.getElementById('header');
  var nav      = document.getElementById('nav');
  var toggle   = document.getElementById('navToggle');
  var waFloat  = document.querySelector('.wa-float');

  // ---- Analítica lista para usar (sin cookies ni llamadas externas) ----
  // Empuja eventos a window.dataLayer. Si el cliente conecta GA4 / Google Tag
  // Manager / Meta Pixel, los eventos fluyen solos. Sin herramienta conectada,
  // es un no-op silencioso (no envía nada, respeta la privacidad).
  window.dataLayer = window.dataLayer || [];
  function track(event, params) {
    try { window.dataLayer.push(Object.assign({ event: event }, params || {})); } catch (e) {}
  }
  // Rastreo de todos los CTAs de contacto sin tener que anotar cada enlace.
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    var href = a.getAttribute('href') || '';
    var isWa = href.indexOf('wa.me') !== -1;
    var isTel = href.indexOf('tel:') === 0;
    if (!isWa && !isTel) return;
    var section = a.closest('section');
    track('cta_contacto', {
      canal: isWa ? 'whatsapp' : 'telefono',
      origen: a.getAttribute('data-cta') || (section ? section.id : 'desconocido')
    });
  });

  // ---- Año dinámico en el footer ----
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- Header al hacer scroll + botón flotante ----
  var contacto = document.getElementById('contacto');
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('scrolled', y > 40);
    // El flotante aparece tras 600px, pero se oculta si el usuario ya está en
    // la sección de contacto (evita que tape el botón "Enviar" del formulario).
    if (waFloat) {
      var inContact = false;
      if (contacto) {
        var r = contacto.getBoundingClientRect();
        inContact = r.top < window.innerHeight && r.bottom > 0;
      }
      waFloat.classList.toggle('show', y > 600 && !inContact);
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- Menú móvil (con manejo de foco e inert del fondo) ----
  var main = document.querySelector('main');
  var footer = document.querySelector('.site-footer');

  function setBackgroundInert(on) {
    [main, footer, waFloat].forEach(function (el) {
      if (!el) return;
      if (on) el.setAttribute('inert', '');
      else el.removeAttribute('inert');
    });
  }
  function openMenu() {
    if (!nav) return;
    nav.classList.add('open');
    toggle.classList.add('open');
    toggle.setAttribute('aria-expanded', 'true');
    toggle.setAttribute('aria-label', 'Cerrar menú');
    setBackgroundInert(true);
    var first = nav.querySelector('a');
    if (first) first.focus();
  }
  function closeMenu() {
    if (!nav) return;
    var wasOpen = nav.classList.contains('open');
    nav.classList.remove('open');
    toggle.classList.remove('open');
    toggle.setAttribute('aria-expanded', 'false');
    toggle.setAttribute('aria-label', 'Abrir menú');
    setBackgroundInert(false);
    if (wasOpen) toggle.focus();
  }
  if (toggle) {
    toggle.addEventListener('click', function () {
      if (nav.classList.contains('open')) closeMenu();
      else openMenu();
    });
  }
  if (nav) {
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
  }
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav && nav.classList.contains('open')) closeMenu();
  });

  // ---- Reveal al hacer scroll ----
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          var siblings = Array.prototype.slice.call(entry.target.parentNode.children)
            .filter(function (el) { return el.classList.contains('reveal'); });
          var idx = siblings.indexOf(entry.target);
          entry.target.style.transitionDelay = Math.min(idx, 5) * 80 + 'ms';
          entry.target.classList.add('in');
          // Limpiar el delay inline una vez terminada la entrada: así no
          // contamina las transiciones :hover posteriores de la tarjeta.
          entry.target.addEventListener('transitionend', function clear() {
            entry.target.style.transitionDelay = '';
            entry.target.removeEventListener('transitionend', clear);
          });
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  // ---- Scroll-spy: marca en la navegación la sección visible ----
  var navLinks = nav ? Array.prototype.slice.call(nav.querySelectorAll('a[href^="#"]')) : [];
  var spySections = navLinks
    .map(function (a) { return document.getElementById(a.getAttribute('href').slice(1)); })
    .filter(Boolean);
  if (spySections.length && 'IntersectionObserver' in window) {
    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var id = entry.target.id;
        navLinks.forEach(function (a) {
          a.classList.toggle('is-current', a.getAttribute('href') === '#' + id);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    spySections.forEach(function (s) { spy.observe(s); });
  }

  // ---- Contadores animados (banda de datos) ----
  var counters = document.querySelectorAll('[data-count]');
  var reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function formatCount(value, decimals) {
    return value.toLocaleString('es-CO', {
      minimumFractionDigits: decimals,
      maximumFractionDigits: decimals
    });
  }
  function animateCounter(el) {
    var target = parseFloat(el.getAttribute('data-count'));
    var decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
    var prefix = el.getAttribute('data-prefix') || '';
    var suffix = el.getAttribute('data-suffix') || '';
    if (isNaN(target)) return;
    if (reduceMotion) { el.textContent = prefix + formatCount(target, decimals) + suffix; return; }
    var duration = 1400, start = null;
    function step(ts) {
      if (start === null) start = ts;
      var p = Math.min((ts - start) / duration, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = prefix + formatCount(target * eased, decimals) + suffix;
      if (p < 1) requestAnimationFrame(step);
      else el.textContent = prefix + formatCount(target, decimals) + suffix;
    }
    requestAnimationFrame(step);
  }
  if (counters.length && 'IntersectionObserver' in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { animateCounter(entry.target); cio.unobserve(entry.target); }
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { cio.observe(el); });
  } else {
    counters.forEach(function (el) {
      el.textContent = (el.getAttribute('data-prefix') || '')
        + formatCount(parseFloat(el.getAttribute('data-count')), parseInt(el.getAttribute('data-decimals') || '0', 10))
        + (el.getAttribute('data-suffix') || '');
    });
  }

  // ---- Explorador de sectores (pestañas → panel + mapa) ----
  var sectorTabs  = document.querySelectorAll('.sector-tab');
  var sectorViews = document.querySelectorAll('.sector-view');

  function selectSector(i) {
    sectorTabs.forEach(function (t) {
      var on = parseInt(t.getAttribute('data-sector'), 10) === i;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.setAttribute('tabindex', on ? '0' : '-1');
    });
    sectorViews.forEach(function (v) {
      v.classList.toggle('is-active', parseInt(v.getAttribute('data-index'), 10) === i);
    });
    // Resaltar en el mapa el marcador del sector seleccionado (dorado)
    if (typeof highlightSectorMarker === 'function') highlightSectorMarker(i);
  }
  if (sectorTabs.length && sectorViews.length) {
    sectorTabs.forEach(function (t) {
      t.addEventListener('click', function () { selectSector(parseInt(t.getAttribute('data-sector'), 10)); });
    });
    // Navegación por flechas entre pestañas (patrón tablist)
    var tabList = document.querySelector('.sector-tabs');
    if (tabList) {
      tabList.addEventListener('keydown', function (e) {
        if (e.key !== 'ArrowRight' && e.key !== 'ArrowLeft') return;
        var current = document.querySelector('.sector-tab.is-active');
        var i = current ? parseInt(current.getAttribute('data-sector'), 10) : 0;
        var n = sectorTabs.length;
        i = e.key === 'ArrowRight' ? (i + 1) % n : (i - 1 + n) % n;
        selectSector(i);
        var next = document.querySelector('.sector-tab[data-sector="' + i + '"]');
        if (next) next.focus();
        e.preventDefault();
      });
    }
  }

  // ---- Mapa Leaflet: carga diferida (solo cuando el usuario se acerca) ----
  var _sectorMarkers = [];
  var _mapInit = false;

  function sectorMarkerIcon(num, active) {
    return L.divIcon({
      className: 'mkr-wrap',
      html: '<span class="mkr' + (active ? ' mkr-on' : '') + '">' + num + '</span>',
      iconSize: [30, 30], iconAnchor: [15, 15], tooltipAnchor: [0, -14]
    });
  }
  function highlightSectorMarker(i) {
    _sectorMarkers.forEach(function (m, idx) {
      m.setIcon(sectorMarkerIcon(idx + 1, idx === i));
      m.setZIndexOffset(idx === i ? 1000 : 0);
    });
  }
  function initSectorMap() {
    var el = document.getElementById('sectorMap');
    if (!el || _mapInit) return;
    if (typeof L === 'undefined') return mapFallback(el);
    if (!sectorTabs.length) return;
    _mapInit = true;
    var pts = [];
    sectorTabs.forEach(function (t) {
      var la = parseFloat(t.getAttribute('data-lat')), lo = parseFloat(t.getAttribute('data-lon'));
      if (!isNaN(la) && !isNaN(lo)) pts.push([la, lo]);
    });
    if (!pts.length) return;
    var map = L.map(el, { scrollWheelZoom: false, zoomControl: true });
    // En pantallas táctiles desactivamos el arrastre del mapa para que el dedo
    // haga scroll de la página y no quede "atrapado" paneando el mapa.
    var coarse = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;
    if (coarse && map.dragging) map.dragging.disable();
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19, attribution: '&copy; OpenStreetMap'
    }).addTo(map);
    pts.forEach(function (p, idx) {
      var m = L.marker(p, { icon: sectorMarkerIcon(idx + 1, idx === 0) }).addTo(map);
      m.bindTooltip(sectorTabs[idx].textContent, { direction: 'top' });
      m.on('click', function () {
        selectSector(idx);
        var tab = document.querySelector('.sector-tab[data-sector="' + idx + '"]');
        if (tab) tab.focus();
      });
      _sectorMarkers.push(m);
    });
    map.fitBounds(pts, { padding: [45, 45] });
    setTimeout(function () { map.invalidateSize(); map.fitBounds(pts, { padding: [45, 45] }); }, 450);
  }
  function mapFallback(el) {
    _mapInit = true;
    el.innerHTML = '<iframe title="Mapa de Manizales" style="width:100%;height:100%;border:0" ' +
      'loading="lazy" src="https://www.openstreetmap.org/export/embed.html?bbox=-75.5300,5.0200,-75.4400,5.0900&layer=mapnik"></iframe>';
  }

  // Carga de Leaflet bajo demanda, con Subresource Integrity (SRI).
  function loadLeaflet(done) {
    if (window.L) return done();
    var css = document.createElement('link');
    css.rel = 'stylesheet';
    css.href = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css';
    css.integrity = 'sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=';
    css.crossOrigin = '';
    document.head.appendChild(css);
    var js = document.createElement('script');
    js.src = 'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js';
    js.integrity = 'sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=';
    js.crossOrigin = '';
    js.onload = done;
    js.onerror = function () { mapFallback(document.getElementById('sectorMap')); };
    document.head.appendChild(js);
  }
  (function watchMap() {
    var host = document.getElementById('sectorMap');
    if (!host) return;
    function go() { loadLeaflet(initSectorMap); }
    if ('IntersectionObserver' in window) {
      var mio = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) { go(); mio.disconnect(); }
        });
      }, { rootMargin: '400px 0px' });
      mio.observe(host);
    } else {
      go();
    }
  })();

  // ---- Simulador de valorización ----
  var simMonto = document.getElementById('simMonto');
  var simYears = document.getElementById('simYears');
  var simRate  = document.getElementById('simRate');

  function money(n) { return '$' + Math.round(n).toLocaleString('es-CO'); }
  function setRangeFill(el) {
    if (!el) return;
    var min = parseFloat(el.min), max = parseFloat(el.max), val = parseFloat(el.value);
    var pct = ((val - min) / (max - min)) * 100;
    el.style.setProperty('--fill', pct + '%');
  }
  function calcSim() {
    if (!simMonto || !simYears || !simRate) return;
    var monto = parseFloat(simMonto.value);
    var years = parseFloat(simYears.value);
    var rate  = parseFloat(simRate.value);
    var valor = monto * Math.pow(1 + rate / 100, years);

    var montoOut = document.getElementById('simMontoOut');
    var yearsOut = document.getElementById('simYearsOut');
    var rateOut  = document.getElementById('simRateOut');
    var valorEl  = document.getElementById('simValor');
    var gainEl   = document.getElementById('simGain');

    var yearsLabel = years + (years === 1 ? ' año' : ' años');
    if (montoOut) montoOut.textContent = money(monto);
    if (yearsOut) yearsOut.textContent = yearsLabel;
    var yearsBadge = document.getElementById('simYearsBadge');
    if (yearsBadge) yearsBadge.textContent = yearsLabel;
    if (rateOut)  rateOut.textContent  = rate.toLocaleString('es-CO') + '% / año';
    if (valorEl)  valorEl.textContent  = money(valor);
    if (gainEl)   gainEl.textContent   = '+' + money(valor - monto);

    [simMonto, simYears, simRate].forEach(setRangeFill);

    var simCta = document.getElementById('simCta');
    if (simCta) {
      var msg = 'Hola Ibonne, usé el simulador: si invierto ' + money(monto)
        + ' con una valorización del ' + rate.toLocaleString('es-CO') + '% podría llegar a ' + money(valor)
        + ' en ' + years + (years === 1 ? ' año' : ' años') + '. Me gustaría ver opciones reales.';
      simCta.href = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + encodeURIComponent(msg);
    }
  }
  if (simMonto && simYears && simRate) {
    [simMonto, simYears, simRate].forEach(function (el) {
      el.addEventListener('input', calcSim);
    });
    calcSim();
  }

  // ---- Formulario de contacto → WhatsApp ----
  var form = document.getElementById('contactForm');
  var note = document.getElementById('formNote');

  function buildMessage(data) {
    var lines = [
      'Hola Ibonne, quiero solicitar una asesoría.',
      '',
      'Nombre: ' + data.name,
      data.contact ? 'Contacto: ' + data.contact : null,
      data.interest ? 'Interés: ' + data.interest : null,
      data.message ? 'Mensaje: ' + data.message : null
    ].filter(Boolean);
    return lines.join('\n');
  }

  // Guarda el lead en el propio dispositivo como red de seguridad: si el salto
  // a WhatsApp falla o el usuario no lo completa, sus datos no se pierden del
  // todo y pueden recuperarse. (Un CRM/endpoint real sería el paso siguiente.)
  function persistLead(data) {
    try {
      var key = 'it_leads';
      var arr = JSON.parse(localStorage.getItem(key) || '[]');
      arr.push({ ts: new Date().toISOString(), name: data.name, contact: data.contact, interest: data.interest, message: data.message });
      localStorage.setItem(key, JSON.stringify(arr.slice(-50)));
    } catch (e) {}
  }

  function fieldError(field, msg) {
    note.textContent = msg;
    note.className = 'form-note err';
    if (field) { field.setAttribute('aria-invalid', 'true'); field.focus(); }
  }

  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var data = {
        name: form.name.value.trim(),
        contact: form.contact.value.trim(),
        interest: form.interest.value,
        message: form.message.value.trim()
      };

      form.name.removeAttribute('aria-invalid');
      form.contact.removeAttribute('aria-invalid');

      if (!data.name) return fieldError(form.name, 'Por favor escribe tu nombre.');
      if (!data.contact) return fieldError(form.contact, 'Déjame un WhatsApp o correo para poder responderte.');
      if (form.consent && !form.consent.checked) {
        note.textContent = 'Necesito tu autorización para tratar tus datos y poder contactarte.';
        note.className = 'form-note err';
        form.consent.focus();
        return;
      }

      persistLead(data);
      track('lead_formulario', { interes: data.interest || 'no_indicado' });

      var text = encodeURIComponent(buildMessage(data));
      var url = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + text;

      note.textContent = 'Abriendo WhatsApp con tu mensaje… Si no se abre, escríbenos al +57 310 497 33 36.';
      note.className = 'form-note ok';

      var win = window.open(url, '_blank');
      if (!win) window.location.href = url;
      // No reseteamos de inmediato: si el salto falla, el usuario conserva lo
      // que escribió. Limpiamos tras unos segundos, ya asegurado el envío.
      setTimeout(function () { form.reset(); calcConsentReset(); }, 4000);
    });
  }
  // Al resetear, el checkbox required vuelve a vacío; nada más que hacer.
  function calcConsentReset() {}
})();
