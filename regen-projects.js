#!/usr/bin/env node
/*
 * regen-projects.js
 * --------------------------------------------------------------------------
 * Regenera el contenido ESTÁTICO de proyectos en index.html a partir del
 * array `PROJECTS` (única fuente de verdad, definida en el <script> de la
 * página). Mantiene la rastreabilidad: los proyectos quedan en el HTML inicial
 * para crawlers, lectores de pantalla y navegación sin JavaScript.
 *
 * Regenera dos cosas:
 *   1. Las tarjetas <article> entre los marcadores PROJECTS:START / PROJECTS:END
 *      dentro de #projGrid (versión en español = capa base de PROJECTS).
 *   2. El bloque JSON-LD ItemList (@id .../#proyectos) para buscadores e IA.
 *
 * Uso:
 *   node regen-projects.js            # aplica los cambios a index.html
 *   node regen-projects.js --check    # solo informa si hay diferencias (no escribe)
 *
 * Ejecutar SIEMPRE que se edite el array PROJECTS para no dejar desfasada la
 * versión estática.
 * --------------------------------------------------------------------------
 */
'use strict';
const fs = require('fs');
const path = require('path');

const FILE = path.join(__dirname, 'index.html');
const CHECK = process.argv.includes('--check');

let html = fs.readFileSync(FILE, 'utf8');
const before = html;

/* ---- 1. Extraer datos de la página (PROJECTS, EV, UI) ---- */
function grab(re, label) {
  const m = html.match(re);
  if (!m) { console.error(`✗ No se pudo localizar ${label} en index.html`); process.exit(1); }
  return m[1];
}
const EV       = eval('(' + grab(/const EV=(\{.*?\});/, 'EV') + ')');
const PROJECTS = eval('(' + grab(/const PROJECTS=(\[[\s\S]*?\n\]);/, 'PROJECTS') + ')');
const UI       = eval('(' + grab(/const UI=(\{[\s\S]*?\n\});/, 'UI') + ')');

/* ---- 2. Construir las tarjetas (réplica de cardHTML, capa base ES) ---- */
const badges = t => t.map(x => `<span class="badge">${x}</span>`).join('');
const evTag  = k => `<span class="ev ${EV[k][1]}">${EV[k][0]}</span>`;
const card = p =>
`      <article class="proj card" data-cat="${p.cat}" data-id="${p.id}" tabindex="0" role="button" aria-label="${p.title}">
        <div class="ptype">${p.type}</div>
        <h3>${p.title}</h3>
        <div class="proj-field pf-prob"><span class="pf-label">Problema</span><span class="pf-val">${p.challenge}</span></div>
        <div class="proj-field pf-role"><span class="pf-label">Mi rol</span><span class="pf-val">${p.role}</span></div>
        <div class="tags">${badges(p.tags.slice(0, 3))}</div>
        <div class="proj-foot">${evTag(p.ev)}<span class="more">${UI.es.more}</span></div>
      </article>`;
const cards = PROJECTS.map(card).join('\n');

html = html.replace(
  /(<!-- PROJECTS:START[^>]*-->\n)[\s\S]*?(\n<!-- PROJECTS:END -->)/,
  (_, a, b) => a + cards + b
);

/* ---- 3. Construir el JSON-LD ItemList ---- */
const dec = s => String(s)
  .replace(/&amp;/g, '&').replace(/&lt;/g, '<').replace(/&gt;/g, '>')
  .replace(/&#39;/g, "'").replace(/&quot;/g, '"');
const ld = {
  "@context": "https://schema.org",
  "@type": "ItemList",
  "@id": "https://cv.javierforero.co/#proyectos",
  "name": "Proyectos y casos · Javier Forero",
  "numberOfItems": PROJECTS.length,
  "itemListOrder": "https://schema.org/ItemListUnordered",
  "itemListElement": PROJECTS.map((p, i) => ({
    "@type": "ListItem", "position": i + 1,
    "item": {
      "@type": "CreativeWork",
      "name": dec(p.title), "about": dec(p.type), "description": dec(p.summary),
      "creator": { "@id": "https://javierforero.co/#person" },
      "dateCreated": String(p.period),
      "url": "https://cv.javierforero.co/#proyectos"
    }
  }))
};
const ldStr = JSON.stringify(ld, null, 2);
/* Reemplazo confinado a UN solo bloque <script> (no cruza </script>) */
html = html.replace(
  /<script type="application\/ld\+json">(?:(?!<\/script>)[\s\S])*?"ItemList"(?:(?!<\/script>)[\s\S])*?<\/script>/,
  `<script type="application/ld+json">\n${ldStr}\n</script>`
);

/* ---- 4. Escribir o informar ---- */
if (html === before) {
  console.log('✓ Sin cambios: la versión estática ya está sincronizada con PROJECTS (' + PROJECTS.length + ' proyectos).');
  process.exit(0);
}
if (CHECK) {
  console.log('⚠ Hay diferencias: la versión estática está DESFASADA. Ejecuta `node regen-projects.js` para actualizar.');
  process.exit(1);
}
fs.writeFileSync(FILE, html);
console.log('✓ index.html actualizado: ' + PROJECTS.length + ' tarjetas + JSON-LD ItemList regenerados.');
