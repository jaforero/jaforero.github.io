# CV interactivo de Javier Forero — `cv.javierforero.co`

Sitio estático (GitHub Pages) que funciona como CV interactivo + plataforma de evidencia
profesional, con versión en inglés y CVs ejecutivos ATS descargables por macroperfil.

- **Repo / hosting:** `jaforero/jaforero.github.io` → GitHub Pages → dominio `cv.javierforero.co`
- **Stack:** HTML + CSS + JavaScript vanilla, todo en un solo archivo (`index.html`). Sin framework.
- **Idiomas:** español (página principal, con toggle ES/EN client-side) e inglés estático (`en.html`).

---

## 1. Estructura de archivos

### Sitio publicado (lo que sirve GitHub Pages)

| Archivo / carpeta | Qué es |
|---|---|
| `index.html` | Página principal (ES). Contiene HTML, CSS y JS embebidos, e IgraSans en base64. |
| `en.html` | Versión 100% estática en inglés (generada, no editar a mano). |
| `cv/` | CVs en PDF: 2 maestros (ES/EN) + 10 ejecutivos ATS (5 macroperfiles × ES/EN). |
| `sitemap.xml`, `robots.txt` | SEO. El sitemap incluye `/` y `/en.html` con `hreflang`. |
| `og-image.jpg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png`, `qr-cv.png`, `inflacion-latam-hero.jpg` | Assets referenciados por las páginas. |
| `CNAME` | Dominio personalizado (no borrar). |

### Tooling de mantenimiento (no afecta el render del sitio)

| Archivo | Qué hace |
|---|---|
| `regen-projects.js` | Regenera las tarjetas de proyecto estáticas + el JSON-LD desde el array `PROJECTS`. |
| `build-en.js` | Genera `en.html` desde `index.html` (usa `cheerio`). |
| `build-cvs.py` | Genera los 10 PDFs ATS en `cv/` (usa `weasyprint` + `IgraSans.woff2`). |
| `IgraSans.otf` | Fuente de marca **con ligaduras** (la usa `build-cvs.py`; en el HTML va embebida en base64). Ojo: `IgraSans.woff2` es un subset SIN la ligadura `F_O_R` — no usarlo para los PDFs. |

> `node_modules/` y `CV_ATS/` (carpeta vieja) NO se publican ni se versionan.

---

## 2. Arquitectura (claves para editar)

- **Fuente de verdad de proyectos:** el array `const PROJECTS = [...]` dentro del `<script>` de
  `index.html`. La capa inglesa está en `const PROJ_EN = {...}`. Todo lo demás se deriva de ahí.
- **Tarjetas de proyecto:** se renderizan por JS (`cardHTML`) **y** están pre-renderizadas en estático
  entre los marcadores `<!-- PROJECTS:START -->` / `<!-- PROJECTS:END -->` dentro de `#projGrid`
  (para crawlers/lectores sin JS). Si editas `PROJECTS`, corre `regen-projects.js`.
- **i18n:** atributos `data-en` / `data-en-html` / `data-en-attr` / `data-en-tip`. La función
  `applyLang('en')` los intercambia en vivo. `build-en.js` "hornea" ese intercambio en estático.
- **Vista rápida para reclutadores (`#reclutadores`):** selector de 5 rutas (objeto `RV`), con
  encaje + evidencia + skills (objeto `SK`) + descarga del PDF de la ruta (objeto `PDF`).
  Deep-links `?view=<slug>` (ai-data-leadership, genai-automation, data-products, consulting, education).
- **Descargas:** `downloadCV()` baja el CV maestro (`cv/...`); cada ruta baja su PDF de macroperfil
  (`cv/Javier_Forero_CV_<Perfil>_<ES|EN>.pdf`).
- **Marca:** morado `#4e00ff`, azul profundo `#041c59`, fuente IgraSans. El nombre "JAVIER FORERO"
  usa la ligadura `F_O_R` de IgraSans (requiere texto en mayúsculas, `font-feature-settings:"liga"`
  y sin `letter-spacing`).
- **Regla de honestidad en métricas:** nunca presentar objetivos/criterios de MVP como resultados
  cerrados (p. ej. Preflex se marca como "criterio objetivo del MVP").

---

## 3. Setup del entorno de build (una sola vez)

```bash
npm install cheerio          # para build-en.js
pip install weasyprint --break-system-packages   # para build-cvs.py
# build-cvs.py necesita IgraSans.otf en la misma carpeta (trae las ligaduras de marca)
```

---

## 4. Flujo de trabajo al editar contenido

1. Edita **`index.html`** (única fuente; nunca edites `en.html` a mano).
2. Corre los tres builds:

   ```bash
   node regen-projects.js     # tarjetas/JSON-LD ES sincronizados
   node build-en.js           # regenera en.html
   python3 build-cvs.py       # regenera los 10 PDFs en cv/
   ```

   Verificación rápida (no escriben si ya está sincronizado):

   ```bash
   node regen-projects.js --check
   node build-en.js --check
   ```

3. Publica (ver sección 5).

---

## 5. Publicar en GitHub Pages

> Respaldo: existe el Release **"Versión Estandar Inicial"** (tag `CV`) como punto de restauración.

```bash
git switch -c mejoras-AAAA-MM           # trabaja en una rama, no en main
git add index.html en.html sitemap.xml cv/
git commit -m "Actualizacion de contenido"
git push -u origin mejoras-AAAA-MM
# revisa y haz merge a main en GitHub (Pages despliega main)
```

**Verificar tras el deploy (1–2 min):**

- `https://cv.javierforero.co/` y `https://cv.javierforero.co/en.html`
- `https://cv.javierforero.co/?view=genai-automation` → selecciona ruta + descarga su PDF
- `https://cv.javierforero.co/cv/Javier_Forero_CV_AI_Data_Leadership_EN.pdf`

**No borrar** `CNAME` ni `.github/`. **No publicar** `node_modules/` ni `CV_ATS/`.

---

## 6. Los 5 macroperfiles de CV (en `cv/`)

| Perfil | Archivo (ES / EN) |
|---|---|
| AI & Data Strategy Leadership | `Javier_Forero_CV_AI_Data_Leadership_{ES,EN}.pdf` |
| GenAI & Automation | `Javier_Forero_CV_GenAI_Automation_{ES,EN}.pdf` |
| Analytics Products & BI | `Javier_Forero_CV_Analytics_Products_BI_{ES,EN}.pdf` |
| Senior Consulting & Advisory | `Javier_Forero_CV_Senior_Consulting_{ES,EN}.pdf` |
| Executive AI Education | `Javier_Forero_CV_Executive_Education_{ES,EN}.pdf` |

Los 5 comparten experiencia/educación reales; cambian título, perfil, casos y skills clave por
macroperfil. Una columna, A4, texto seleccionable (ATS), paleta de marca. Se editan en `build-cvs.py`
(diccionarios `L` para contenido común y `PROFILES` para el tailoring).
