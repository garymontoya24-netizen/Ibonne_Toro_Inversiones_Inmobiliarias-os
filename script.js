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
