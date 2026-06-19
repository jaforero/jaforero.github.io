#!/usr/bin/env node
/*
 * build-en.js
 * --------------------------------------------------------------------------
 * Genera en.html (versión ESTÁTICA en inglés) a partir de index.html.
 * Objetivo: paridad de rastreabilidad en inglés (crawlers, parsers e IA leen
 * el perfil en inglés sin depender de JavaScript).
 *
 * Qué hace:
 *   1. Hornea el i18n: replica applyLang('en') de forma estática
 *      (data-en -> innerHTML, data-en-attr -> atributo, data-en-html, data-en-tip)
 *      y elimina esos atributos para que la página quede en inglés "de fábrica".
 *   2. lang="en", title/description/canonical/og/hreflang en inglés.
 *   3. Tarjetas de proyecto y JSON-LD ItemList regenerados en inglés (PROJ_EN).
 *   4. Fija LANG='en' en el JS y hace que el botón "ES" navegue a la home (/).
 *
 * Se publica en la RAÍZ como en.html (no /en/) para no romper rutas relativas
 * de assets (PDFs, imágenes, etc.).
 *
 * Uso:  node build-en.js          (escribe en.html)
 *       node build-en.js --check  (informa si en.html quedaría desfasada)
 *
 * Ejecutar cada vez que cambie index.html para mantener en.html sincronizada.
 * --------------------------------------------------------------------------
 */
'use strict';
const fs = require('fs');
const path = require('path');
const cheerio = require('cheerio');

const SRC = path.join(__dirname, 'index.html');
const OUT = path.join(__dirname, 'en.html');
const CHECK = process.argv.includes('--check');

let html = fs.readFileSync(SRC, 'utf8');

/* ---- 1. Extraer datos de la página ---- */
function grab(re, label) {
  const m = html.match(re);
  if (!m) { console.error('✗ No se pudo localizar ' + label + ' en index.html'); process.exit(1); }
  return m[1];
}
const EV       = eval('(' + grab(/const EV=(\{.*?\});/, 'EV') + ')');
const EV_EN    = eval('(' + grab(/const EV_EN=(\{.*?\});/, 'EV_EN') + ')');
const PROJECTS = eval('(' + grab(/const PROJECTS=(\[[\s\S]*?\n\]);/, 'PROJECTS') + ')');
const PROJ_EN  = eval('(' + grab(/const PROJ_EN=(\{[\s\S]*?\n\});/, 'PROJ_EN') + ')');
const UI       = eval('(' + grab(/const UI=(\{[\s\S]*?\n\});/, 'UI') + ')');

/* ---- 2. Transformaciones de DOM (cheerio) ---- */
const $ = cheerio.load(html, { decodeEntities: false });
$('html').attr('lang', 'en');

/* Hornear i18n = applyLang('en') estático */
$('[data-en]').each((i, el) => {
  const $e = $(el);
  const v = $e.attr('data-en');
  const attr = $e.attr('data-en-attr');
  if (attr) { $e.attr(attr, v); } else { $e.html(v); }
});
$('[data-en-html]').each((i, el) => { $(el).html($(el).attr('data-en-html')); });
$('[data-en-tip]').each((i, el) => { $(el).attr('data-tip', $(el).attr('data-en-tip')); });
$('[data-en]').removeAttr('data-en').removeAttr('data-en-attr');
$('[data-en-html]').removeAttr('data-en-html');
$('[data-en-tip]').removeAttr('data-en-tip');

/* Selector de idioma: marcar EN como activo */
$('#langSeg .seg-btn').removeClass('active');
$('#langSeg .seg-btn[data-lang="en"]').addClass('active');

/* Head: metadatos en inglés */
$('title').first().text('Javier Forero · CV — AI, Data & Analytics Consultant');
$('meta[name="description"]').attr('content', 'AI, Data Science and Digital Transformation consultant with 25+ years. Explore projects, impact cases and download my executive CV.');
$('link[rel="canonical"]').attr('href', 'https://cv.javierforero.co/en.html');
$('meta[property="og:url"]').attr('content', 'https://cv.javierforero.co/en.html');
$('meta[property="og:locale"]').attr('content', 'en_US');
$('meta[property="og:locale:alternate"]').attr('content', 'es_CO');

/* hreflang cruzado */
$('link[rel="alternate"][hreflang]').remove();
$('head').append(
  '\n<link rel="alternate" hreflang="en" href="https://cv.javierforero.co/en.html">' +
  '\n<link rel="alternate" hreflang="es" href="https://cv.javierforero.co/">' +
  '\n<link rel="alternate" hreflang="x-default" href="https://cv.javierforero.co/">'
);

let out = $.html();

/* ---- 3. Reemplazos sobre el HTML serializado ---- */
/* 3a. Idioma fijo en inglés */
out = out.replace(
  /let LANG=\(function\(\)\{try\{return localStorage\.getItem\('jf_lang'\)\|\|'es'\}catch\(e\)\{return 'es'\}\}\)\(\);/,
  "let LANG='en';/* en.html: idioma fijo */"
);
/* 3b. El botón ES navega a la home en español */
out = out.replace(
  "document.querySelectorAll('#langSeg .seg-btn').forEach(b=>b.addEventListener('click',()=>applyLang(b.dataset.lang)));",
  "document.querySelectorAll('#langSeg .seg-btn').forEach(b=>b.addEventListener('click',function(){if(b.dataset.lang==='es')location.href='/';}));"
);

/* 3c. Tarjetas de proyecto en inglés */
const badges = t => t.map(x => `<span class="badge">${x}</span>`).join('');
const evTag  = k => `<span class="ev ${EV[k][1]}">${EV_EN[k]}</span>`;
const PVe    = p => Object.assign({}, p, PROJ_EN[p.id] || {});
const card = p => { const v = PVe(p); return `      <article class="proj card" data-cat="${p.cat}" data-id="${p.id}" tabindex="0" role="button" aria-label="${v.title}">
        <div class="ptype">${v.type}</div>
        <h3>${v.title}</h3>
        <div class="proj-field pf-prob"><span class="pf-label">Problem</span><span class="pf-val">${v.challenge}</span></div>
        <div class="proj-field pf-role"><span class="pf-label">My role</span><span class="pf-val">${v.role}</span></div>
        <div class="tags">${badges(p.tags.slice(0, 3))}</div>
        <div class="proj-foot">${evTag(p.ev)}<span class="more">${UI.en.more}</span></div>
      </article>`; };
out = out.replace(/(<!-- PROJECTS:START[^>]*-->\n)[\s\S]*?(\n<!-- PROJECTS:END -->)/, (m, a, b) => a + PROJECTS.map(card).join('\n') + b);

/* 3d. JSON-LD ItemList en inglés */
const dec = s => String(s).replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&#39;/g, "'").replace(/&quot;/g, '"');
const ld = {
  "@context": "https://schema.org", "@type": "ItemList",
  "@id": "https://cv.javierforero.co/en.html#projects",
  "name": "Projects & cases · Javier Forero",
  "numberOfItems": PROJECTS.length,
  "itemListOrder": "https://schema.org/ItemListUnordered",
  "itemListElement": PROJECTS.map((p, i) => { const v = PVe(p); return {
    "@type": "ListItem", "position": i + 1,
    "item": { "@type": "CreativeWork", "name": dec(v.title), "about": dec(v.type), "description": dec(v.summary),
      "creator": { "@id": "https://javierforero.co/#person" }, "dateCreated": String(p.period),
      "url": "https://cv.javierforero.co/en.html#proyectos" } }; })
};
out = out.replace(
  /<script type="application\/ld\+json">(?:(?!<\/script>)[\s\S])*?"ItemList"(?:(?!<\/script>)[\s\S])*?<\/script>/,
  '<script type="application/ld+json">\n' + JSON.stringify(ld, null, 2) + '\n</script>'
);

/* 3e. JSON-LD Person/ProfilePage: idioma y textos en inglés */
out = out.replace(/"inLanguage": "es"/g, '"inLanguage": "en"');
out = out.replace(
  '"name": "Javier Forero · CV — Consultor en IA, Datos y Analítica",',
  '"name": "Javier Forero · CV — AI, Data & Analytics Consultant",'
);
out = out.replace(
  '"description": "Científico de Datos Senior, Estadístico y Consultor en Analítica, Inteligencia Artificial y Transformación Digital, con más de 25 años de experiencia conectando datos, IA y decisiones de negocio.",',
  '"description": "Senior Data Scientist, Statistician and consultant in Analytics, Artificial Intelligence and Digital Transformation, with 25+ years connecting data, AI and business decisions.",'
);

/* ---- 4. Escribir / verificar ---- */
const prev = fs.existsSync(OUT) ? fs.readFileSync(OUT, 'utf8') : null;
if (prev === out) { console.log('✓ Sin cambios: en.html ya está sincronizada con index.html.'); process.exit(0); }
if (CHECK) { console.log('⚠ en.html está DESFASADA. Ejecuta `node build-en.js` para regenerarla.'); process.exit(1); }
fs.writeFileSync(OUT, out);
console.log('✓ en.html generado (' + out.length + ' bytes, ' + PROJECTS.length + ' proyectos en inglés).');
