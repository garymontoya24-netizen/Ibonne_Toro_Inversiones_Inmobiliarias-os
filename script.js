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

  // ---- Año dinámico en el footer ----
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

  // ---- Header al hacer scroll + botón flotante ----
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    if (header) header.classList.toggle('scrolled', y > 40);
    if (waFloat) waFloat.classList.toggle('show', y > 600);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // ---- Menú móvil (con manejo de foco e inert del fondo) ----
  var main = document.querySelector('main');
  var footer = document.querySelector('.site-footer');

  // Marca el fondo como inerte para que el teclado/lector de pantalla
  // no salgan del menú abierto. El header NO se inerta (contiene el botón).
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
  // Cerrar menú al navegar
  if (nav) {
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeMenu);
    });
  }
  // Cerrar con Escape (y devolver el foco al botón)
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && nav && nav.classList.contains('open')) closeMenu();
  });

  // ---- Reveal al hacer scroll ----
  var revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          // pequeño retardo escalonado entre hermanos
          var siblings = Array.prototype.slice.call(entry.target.parentNode.children)
            .filter(function (el) { return el.classList.contains('reveal'); });
          var idx = siblings.indexOf(entry.target);
          entry.target.style.transitionDelay = Math.min(idx, 5) * 80 + 'ms';
          entry.target.classList.add('in');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach(function (el) { io.observe(el); });
  } else {
    revealEls.forEach(function (el) { el.classList.add('in'); });
  }

  // ---- Contadores animados (banda de datos) ----
  // Cada <span data-count="10" data-decimals="0" data-prefix="+" data-suffix="%">
  // se anima de 0 al valor final cuando entra en pantalla.
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
      var eased = 1 - Math.pow(1 - p, 3); // easeOutCubic
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

  // ---- Explorador de sectores (mapa + pestañas → panel) ----
  var sectorTabs  = document.querySelectorAll('.sector-tab');
  var sectorPins  = document.querySelectorAll('.map-pin');
  var sectorViews = document.querySelectorAll('.sector-view');

  function selectSector(i) {
    sectorTabs.forEach(function (t) {
      var on = parseInt(t.getAttribute('data-sector'), 10) === i;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.setAttribute('tabindex', on ? '0' : '-1');
    });
    sectorPins.forEach(function (p) {
      p.classList.toggle('is-active', parseInt(p.getAttribute('data-sector'), 10) === i);
    });
    sectorViews.forEach(function (v) {
      v.classList.toggle('is-active', parseInt(v.getAttribute('data-index'), 10) === i);
    });
    // Recentrar el mapa real de Manizales en las coordenadas del sector
    var activeTab = document.querySelector('.sector-tab[data-sector="' + i + '"]');
    var mapFrame = document.getElementById('sectorMap');
    if (activeTab && mapFrame) {
      var lat = parseFloat(activeTab.getAttribute('data-lat'));
      var lon = parseFloat(activeTab.getAttribute('data-lon'));
      if (!isNaN(lat) && !isNaN(lon)) {
        var dLat = 0.010, dLon = 0.014;
        var bbox = (lon - dLon).toFixed(5) + ',' + (lat - dLat).toFixed(5) + ',' +
                   (lon + dLon).toFixed(5) + ',' + (lat + dLat).toFixed(5);
        mapFrame.src = 'https://www.openstreetmap.org/export/embed.html?bbox=' + bbox +
                       '&layer=mapnik&marker=' + lat.toFixed(5) + ',' + lon.toFixed(5);
        var mapOpen = document.getElementById('mapOpen');
        if (mapOpen) {
          mapOpen.href = 'https://www.openstreetmap.org/?mlat=' + lat.toFixed(5) +
                         '&mlon=' + lon.toFixed(5) + '#map=15/' + lat.toFixed(5) + '/' + lon.toFixed(5);
        }
      }
    }
  }
  if (sectorTabs.length && sectorViews.length) {
    sectorTabs.forEach(function (t) {
      t.addEventListener('click', function () { selectSector(parseInt(t.getAttribute('data-sector'), 10)); });
    });
    sectorPins.forEach(function (p) {
      p.addEventListener('click', function () {
        var i = parseInt(p.getAttribute('data-sector'), 10);
        selectSector(i);
        // llevar el foco a la pestaña equivalente para lectores de pantalla
        var tab = document.querySelector('.sector-tab[data-sector="' + i + '"]');
        if (tab) tab.focus();
      });
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

    // actualizar el enlace de WhatsApp con el escenario del cliente
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
      'Interés: ' + data.interest,
      data.message ? 'Mensaje: ' + data.message : null
    ].filter(Boolean);
    return lines.join('\n');
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

      if (!data.name) {
        note.textContent = 'Por favor escribe tu nombre.';
        note.className = 'form-note err';
        form.name.setAttribute('aria-invalid', 'true');
        form.name.focus();
        return;
      }

      var text = encodeURIComponent(buildMessage(data));
      var url = 'https://wa.me/' + WHATSAPP_NUMBER + '?text=' + text;

      form.name.removeAttribute('aria-invalid');
      note.textContent = 'Abriendo WhatsApp con tu mensaje…';
      note.className = 'form-note ok';

      var win = window.open(url, '_blank');
      // Si el navegador bloquea el popup, redirigimos en la misma pestaña.
      if (!win) window.location.href = url;

      form.reset();
    });
  }
})();
