#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build-cvs.py — Generador de CVs ejecutivos ATS de Javier Forero.

Produce 10 PDFs (5 macroperfiles x ES/EN) en CV_ATS/, una columna, texto
seleccionable (ATS-friendly), con la paleta de marca e IgraSans.

Diseño honesto: la EXPERIENCIA y la EDUCACIÓN son las mismas en todos los
perfiles (no se inventan trayectorias). Lo que cambia por macroperfil es el
título, el perfil ejecutivo, los casos destacados y las skills clave — el
mismo set de keywords que alimenta la sección "Reclutadores" del sitio.

Uso:  python3 build-cvs.py
Requiere: weasyprint, IgraSans.woff2 en esta carpeta.
"""
import os, weasyprint

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "cv")
os.makedirs(OUT, exist_ok=True)

# ---------------------------------------------------------------- contenido común
CONTACT = ("Bogotá, Colombia · Remoto LATAM &nbsp;|&nbsp; +57 320 838 3457 &nbsp;|&nbsp; "
           '<a href="mailto:mail@javierforero.com">mail@javierforero.com</a> &nbsp;|&nbsp; '
           '<a href="https://linkedin.com/in/jforero">linkedin.com/in/jforero</a> &nbsp;|&nbsp; '
           '<a href="https://cv.javierforero.co">cv.javierforero.co</a>')

L = {
 "es": {
  "title_html": "Perfil ejecutivo", "kpis_h": "Impacto en cifras", "cases_h": "Casos destacados",
  "exp_h": "Experiencia profesional", "prev_h": "Trayectoria previa", "teach_h": "Docencia, mentoría y liderazgo de pensamiento",
  "skills_h": "Skills clave", "edu_h": "Educación, idiomas y reconocimientos", "present": "Presente",
  "kpis": [("25+","Años en datos, analítica e IA"),("8","Países / hubs globales"),
           ("14 + 1","Premios J&amp;J (Inspire + Encore)"),("10–15+","Colaboradores liderados en equipos de data, digital y analítica"),
           ("3","Nubes: AWS · Azure · GCP"),("100s","Profesionales formados en IA"),("30+","Proyectos de IA y analítica")],
  "exp": [
    ("Consultor Independiente — Data, Analítica, IA &amp; Transformación Digital","Práctica independiente · Bogotá / Remoto LATAM","Nov 2024 – Presente",
     ["Diseño hojas de ruta de adopción de IA, diagnósticos y métodos de priorización de casos de uso con criterios claros de valor de negocio.",
      "Estructuro automatización inteligente con GenAI (comprensión documental, reglas, excepciones, KPIs) e integración con SAP Business One y cloud.",
      "Asesoro arquitecturas de datos modernas (Microsoft Fabric, Power BI, gobierno y calidad) y facilito workshops y programas de IA aplicada."]),
    ("Consultor — Data Science &amp; Analítica Avanzada","NEICON (clientes Postobón, Efecty) · Bogotá","Ene 2025 – Jul 2025",
     ["Diseñé y entregué soluciones analíticas corporativas, traduciendo requerimientos de negocio en modelos de datos, dashboards y soporte a la decisión.",
      "Apoyé decisiones de arquitectura de datos y pipelines escalables con foco en calidad, trazabilidad y adopción efectiva por el negocio."]),
    ("Senior Manager — Data Science, Corporate Business Technology","Johnson &amp; Johnson · Funciones corporativas globales (remoto)","Ago 2021 – Oct 2024",
     ["Co-lideré analítica avanzada, IA y automatización para funciones corporativas globales (Finanzas, Procurement, HR, Legal).",
      "Actué como puente estratégico negocio–datos: enmarqué problemas, definí métricas de éxito y traduje requerimientos en soluciones analíticas.",
      "Promoví la adopción responsable de IA, GenAI y automatización en equipos no técnicos mediante formación, gobierno y documentación.",
      "Lideré y coordiné equipos analíticos y de consultoría (5–6 analistas y 3–4 consultores), articulando negocio, tecnología, datos y adopción."]),
    ("Senior Manager — Data Science &amp; Analytics, Procurement Americas","Johnson &amp; Johnson · Región Américas · Bogotá","May 2018 – Ago 2021",
     ["Lideré BI, analítica predictiva y prescriptiva para Procurement Americas, entregando insights prospectivos para la decisión.",
      "Integré fuentes heterogéneas en dashboards y reporting; automaticé análisis recurrentes y estandaricé entregables del liderazgo regional.",
      "Construí capacidades analíticas regionales desde cero y gestioné stakeholders en mercados LATAM."]),
  ],
  "prev": [
    "<b>Director Digital &amp; Data — Wavemaker / GroupM</b> · Bogotá · Dic 2017 – May 2018",
    "<b>Director Digital &amp; Data — MEC / GroupM (Holding WPP)</b> · Bogotá · Abr 2013 – Dic 2017 · equipos de 10–15+ colaboradores",
    "<b>Managing Partner, Analytics &amp; Insight LATAM — MEC / GroupM</b> · Miami / Fort Lauderdale, EE.UU. · Oct 2010 – Mar 2013",
    "<b>Director, Analytics &amp; Insight Global Solutions — MEC / GroupM</b> · Londres, Reino Unido · Ago 2008 – Sep 2010",
    "<b>Research Director — MEC / Mediaedge:cia</b> · Bogotá · Abr 2000 – Jul 2008",
  ],
  "teach": "Universidad Militar Nueva Granada (IA generativa, Legal Tech, ética), Universidad El Bosque, Collective Academy (AI Productivity Tools, NPS 70/60; BI &amp; Data Analytics MBA), Crehana (Business Analytics con Python) y Asuntos Digitales. Talleres ejecutivos de IA para directivos, agencias y gremios.",
  "edu": ["<b>Estadístico</b> — Universidad Nacional de Colombia.",
          "<b>Certificaciones seleccionadas (71 en total):</b> 5-Day Gen AI Intensive — Google/Kaggle (2025) · Generative AI with LLMs — DeepLearning.AI/AWS · LangChain for LLM Application Development · Building Agentic RAG with LlamaIndex · Agentic AI for Leadership — LinkedIn · ChatGPT Prompt Engineering for Developers · Microsoft Azure Relational Databases.",
          "<b>Idiomas:</b> español (nativo) · inglés (profesional).",
          "<b>Reconocimientos:</b> 14 Johnson &amp; Johnson Inspire Awards y 1 Encore Award."],
 },
 "en": {
  "title_html": "Executive profile", "kpis_h": "Impact in numbers", "cases_h": "Signature cases",
  "exp_h": "Professional experience", "prev_h": "Earlier career", "teach_h": "Teaching, mentoring and thought leadership",
  "skills_h": "Key skills", "edu_h": "Education, languages and recognition", "present": "Present",
  "kpis": [("25+","Years in data, analytics &amp; AI"),("8","Countries / global hubs"),
           ("14 + 1","J&amp;J awards (Inspire + Encore)"),("10–15+","Collaborators led across data, digital and analytics teams"),
           ("3","Clouds: AWS · Azure · GCP"),("100s","Professionals trained in AI"),("30+","AI &amp; analytics projects")],
  "exp": [
    ("Independent Consultant — Data, Analytics, AI &amp; Digital Transformation","Independent practice · Bogotá / Remote LATAM","Nov 2024 – Present",
     ["Design AI adoption roadmaps, assessments and use-case prioritization methods with clear business-value criteria.",
      "Architect intelligent automation with GenAI (document understanding, business rules, exceptions, KPIs) integrated with SAP Business One and cloud.",
      "Advise modern data architectures (Microsoft Fabric, Power BI, governance and quality) and facilitate applied-AI workshops and programs."]),
    ("Consultant — Data Science &amp; Advanced Analytics","NEICON (clients Postobón, Efecty) · Bogotá","Jan 2025 – Jul 2025",
     ["Designed and delivered corporate analytics solutions, translating business requirements into data models, dashboards and decision support.",
      "Supported data architecture decisions and scalable pipelines focused on quality, traceability and effective business adoption."]),
    ("Senior Manager — Data Science, Corporate Business Technology","Johnson &amp; Johnson · Global corporate functions (remote)","Aug 2021 – Oct 2024",
     ["Co-led advanced analytics, AI and automation for global corporate functions (Finance, Procurement, HR, Legal).",
      "Acted as a strategic business–data bridge: framed problems, defined success metrics and translated requirements into analytical solutions.",
      "Drove responsible adoption of AI, GenAI and automation across non-technical teams through training, governance and documentation.",
      "Led and coordinated analytics and consulting teams (5–6 analysts and 3–4 consultants), bridging business, technology, data and adoption."]),
    ("Senior Manager — Data Science &amp; Analytics, Procurement Americas","Johnson &amp; Johnson · Americas region · Bogotá","May 2018 – Aug 2021",
     ["Led BI, predictive and prescriptive analytics for Procurement Americas, delivering forward-looking insight for decisions.",
      "Integrated heterogeneous sources into dashboards and reporting; automated recurring analyses and standardized regional leadership deliverables.",
      "Built regional analytics capabilities from the ground up and managed stakeholders across LATAM markets."]),
  ],
  "prev": [
    "<b>Digital &amp; Data Director — Wavemaker / GroupM</b> · Bogotá · Dec 2017 – May 2018",
    "<b>Digital &amp; Data Director — MEC / GroupM (WPP group)</b> · Bogotá · Apr 2013 – Dec 2017 · teams of 10–15+ collaborators",
    "<b>Managing Partner, Analytics &amp; Insight LATAM — MEC / GroupM</b> · Miami / Fort Lauderdale, USA · Oct 2010 – Mar 2013",
    "<b>Director, Analytics &amp; Insight Global Solutions — MEC / GroupM</b> · London, UK · Aug 2008 – Sep 2010",
    "<b>Research Director — MEC / Mediaedge:cia</b> · Bogotá · Apr 2000 – Jul 2008",
  ],
  "teach": "Universidad Militar Nueva Granada (generative AI, Legal Tech, ethics), Universidad El Bosque, Collective Academy (AI Productivity Tools, NPS 70/60; BI &amp; Data Analytics MBA), Crehana (Business Analytics with Python) and Asuntos Digitales. Executive AI workshops for leaders, agencies and industry guilds.",
  "edu": ["<b>Statistician</b> — Universidad Nacional de Colombia.",
          "<b>Selected certifications (71 total):</b> 5-Day Gen AI Intensive — Google/Kaggle (2025) · Generative AI with LLMs — DeepLearning.AI/AWS · LangChain for LLM Application Development · Building Agentic RAG with LlamaIndex · Agentic AI for Leadership — LinkedIn · ChatGPT Prompt Engineering for Developers · Microsoft Azure Relational Databases.",
          "<b>Languages:</b> Spanish (native) · English (professional).",
          "<b>Recognition:</b> 14 Johnson &amp; Johnson Inspire Awards and 1 Encore Award."],
 },
}

# ---------------------------------------------------------------- perfiles (tailoring)
PROFILES = {
 "AI_Data_Leadership": {
   "title": {"es":"AI &amp; Data Strategy Leader · Head of AI / Data &amp; Analytics",
             "en":"AI &amp; Data Strategy Leader · Head of AI / Data &amp; Analytics"},
   "summary": {"es":"Líder senior en estrategia de IA, datos y analítica con 25+ años llevando a organizaciones globales y regionales de la oportunidad de datos e IA a capacidades de negocio escalables. Especialista en hojas de ruta de adopción de IA, gobierno, operating models, automatización inteligente y gestión de stakeholders ejecutivos C-level. Experiencia construida en Johnson &amp; Johnson, GroupM / Wavemaker y consultoría independiente, con roles ejecutados desde Londres, Miami/LATAM y Colombia.",
               "en":"Senior AI, data and analytics strategy leader with 25+ years moving global and regional organizations from data and AI opportunity to scalable business capabilities. Specialist in AI adoption roadmaps, governance, operating models, intelligent automation and C-level stakeholder management. Background built at Johnson &amp; Johnson, GroupM / Wavemaker and independent consulting, with roles delivered from London, Miami/LATAM and Colombia."},
   "cases": {"es":[("Johnson &amp; Johnson — Corporate Business Technology","co-liderazgo de analítica avanzada, IA y automatización para funciones corporativas globales; puente estratégico negocio–datos; adopción responsable de IA y GenAI."),
                   ("J&amp;J — Procurement Shared Services Americas","liderazgo de BI, analítica predictiva y prescriptiva para la región; estandarización de reporting y automatización de análisis."),
                   ("NEICON (Postobón, Efecty)","soluciones analíticas corporativas, arquitectura de datos y pipelines escalables con foco en calidad y adopción."),
                   ("Impulso IA 360 — Connect Bogotá","consultoría y formación por áreas para identificar, priorizar y prototipar casos de uso de IA.")],
             "en":[("Johnson &amp; Johnson — Corporate Business Technology","co-led advanced analytics, AI and automation for global corporate functions; strategic business–data bridge; responsible AI and GenAI adoption."),
                   ("J&amp;J — Procurement Shared Services Americas","led BI, predictive and prescriptive analytics for the region; standardized reporting and automated analyses."),
                   ("NEICON (Postobón, Efecty)","corporate analytics solutions, data architecture and scalable pipelines focused on quality and adoption."),
                   ("Impulso IA 360 — Connect Bogotá","consulting and area-by-area training to identify, prioritize and prototype AI use cases.")]},
   "skills": "AI Strategy · AI Governance · Data &amp; Analytics Leadership · Target Operating Model · Responsible AI · Change Adoption · Digital Transformation · AI Roadmap · C-level Stakeholders · Machine Learning · Generative AI · Business Intelligence · Power BI · Tableau · AWS · Microsoft Azure · Google Cloud · Microsoft Fabric · Databricks · SQL · Python",
 },
 "GenAI_Automation": {
   "title": {"es":"GenAI &amp; Automation Lead · Adopción de IA","en":"GenAI &amp; Automation Lead · AI Adoption"},
   "summary": {"es":"Especialista en IA generativa, automatización inteligente y adopción, con 25+ años en datos e IA. Llevo casos de uso de la idea a la ejecución: asistentes con RAG, automatización de procesos (Procure-to-Pay), productividad con IA y habilitación de usuarios no técnicos, con comunicación ejecutiva del valor. Experiencia en Johnson &amp; Johnson, consultoría y MVPs propios.",
               "en":"Specialist in generative AI, intelligent automation and adoption, with 25+ years in data and AI. I move use cases from idea to execution: RAG assistants, process automation (Procure-to-Pay), AI productivity and non-technical user enablement, with executive value communication. Experience at Johnson &amp; Johnson, consulting and own MVPs."},
   "cases": {"es":[("Preflex — Automatización inteligente de facturas","solución E2E Procure-to-Pay con GenAI, SAP Business One y Google Gemini (criterios objetivo del MVP, no resultados cerrados)."),
                   ("GenAI para Emprendedores","MVP con RAG y Gemini que resume documentos oficiales y genera planes de negocio."),
                   ("J&amp;J — IA corporativa global","adopción responsable de IA y GenAI en equipos no técnicos mediante formación y gobierno."),
                   ("Collective Academy — AI Productivity Tools","mentoría de 2 cohortes (40+ participantes) en productividad con IA. NPS 70 y 60.")],
             "en":[("Preflex — Intelligent invoice automation","E2E Procure-to-Pay solution with GenAI, SAP Business One and Google Gemini (MVP target criteria, not closed results)."),
                   ("GenAI for Entrepreneurs","RAG + Gemini MVP that summarizes official documents and generates business plans."),
                   ("J&amp;J — global corporate AI","responsible AI and GenAI adoption across non-technical teams through training and governance."),
                   ("Collective Academy — AI Productivity Tools","mentored 2 cohorts (40+ participants) in AI productivity. NPS 70 and 60.")]},
   "skills": "Generative AI · LLMs · RAG · Prompt Engineering · Intelligent Automation · Process Automation (P2P) · AI Adoption · Copilot · ChatGPT · Google Gemini · Productivity AI · SAP Business One · Python · Change Adoption · Executive Communication",
 },
 "Analytics_Products_BI": {
   "title": {"es":"Analytics Products &amp; BI Lead · Decision Intelligence","en":"Analytics Products &amp; BI Lead · Decision Intelligence"},
   "summary": {"es":"Líder de productos analíticos, BI e inteligencia de decisión con 25+ años y criterio estadístico. Construyo productos analíticos longitudinales, BI ejecutivo, analítica predictiva/prescriptiva y arquitecturas cloud que sostienen la decisión. Experiencia en Johnson &amp; Johnson (Procurement Analytics Americas) y productos analíticos de mercado.",
               "en":"Leader of analytics products, BI and decision intelligence with 25+ years and statistical rigor. I build longitudinal analytics products, executive BI, predictive/prescriptive analytics and cloud architectures that sustain decisions. Experience at Johnson &amp; Johnson (Procurement Analytics Americas) and market analytics products."},
   "cases": {"es":[("RAC Evolution","producto de inteligencia de marca: base longitudinal 2003–2025, 12 módulos analíticos, narrativas con IA y evolución con filtro TARGET por segmento."),
                   ("J&amp;J — Procurement Analytics Americas","BI, analítica predictiva y prescriptiva con reporting estandarizado para el liderazgo regional."),
                   ("SEC / Asoanei — Modelo de datos y Power BI","modelo de datos unificado, visión 360° del productor, gobernanza y roadmap Microsoft Fabric."),
                   ("Databricks — Análisis por industria (BNA)","análisis de ventas, precio y drop size con Pareto y series temporales en PySpark.")],
             "en":[("RAC Evolution","brand-intelligence product: longitudinal base 2003–2025, 12 analytical modules, AI narratives and a TARGET-segment evolution."),
                   ("J&amp;J — Procurement Analytics Americas","BI, predictive and prescriptive analytics with standardized reporting for regional leadership."),
                   ("SEC / Asoanei — Data model & Power BI","unified data model, 360° producer view, governance and a Microsoft Fabric roadmap."),
                   ("Databricks — industry analysis (BNA)","sales, price and drop-size analysis with Pareto and time series in PySpark.")]},
   "skills": "Business Intelligence · Power BI · Tableau · Predictive Analytics · Prescriptive Analytics · Decision Intelligence · Data Products · Forecasting · Databricks · PySpark · SQL · Python · Data Visualization · Statistical Modeling · Microsoft Fabric",
 },
 "Senior_Consulting": {
   "title": {"es":"Consultor Senior en IA y Datos · Advisory &amp; Transformación","en":"Senior AI &amp; Data Consultant · Advisory &amp; Transformation"},
   "summary": {"es":"Consultor senior y advisor en IA, datos y transformación, con 25+ años y experiencia multisectorial (industria, sector público, economía circular, pyme). Entrego de extremo a extremo: diagnóstico, roadmap, arquitectura de solución, gobernanza y transferencia de capacidades, con foco en creación de valor. Trayectoria como trusted advisor en Johnson &amp; Johnson, GroupM y clientes independientes.",
               "en":"Senior consultant and advisor in AI, data and transformation, with 25+ years and multi-sector experience (industry, public sector, circular economy, SMEs). I deliver end-to-end: diagnosis, roadmap, solution architecture, governance and capability transfer, focused on value creation. Trusted-advisor track record at Johnson &amp; Johnson, GroupM and independent clients."},
   "cases": {"es":[("Preflex — Consultoría técnica GenAI","diseño de solución, arquitectura y definición de MVP para automatización P2P."),
                   ("NEICON — Arquitectura de datos, BI e IA","asesoría en arquitecturas modernas y despliegue de IA en producción."),
                   ("SEC / Asoanei — Modelo de datos y gobernanza","modelo unificado, visión 360° y roadmap escalable con Microsoft Fabric y Purview."),
                   ("Impulso IA 360 — Connect Bogotá","diagnóstico, priorización y prototipado de casos de uso de IA por área.")],
             "en":[("Preflex — GenAI technical consulting","solution design, architecture and MVP definition for P2P automation."),
                   ("NEICON — Data architecture, BI and AI","advisory on modern architectures and AI deployment to production."),
                   ("SEC / Asoanei — Data model and governance","unified model, 360° view and scalable roadmap with Microsoft Fabric and Purview."),
                   ("Impulso IA 360 — Connect Bogotá","diagnosis, prioritization and prototyping of AI use cases by area.")]},
   "skills": "AI &amp; Data Advisory · Business Transformation · Solution Architecture · Data Governance · Diagnosis &amp; Roadmap · Capability Building · Stakeholder Management · Microsoft Fabric · Power BI · Discovery Workshops · Value Creation · Operating Model · Pre-sales",
 },
 "Executive_Education": {
   "title": {"es":"Educador Ejecutivo en IA · Adopción y Alfabetización","en":"Executive AI Educator · Adoption &amp; Literacy"},
   "summary": {"es":"Educador y facilitador en IA aplicada con 25+ años en datos e IA, especializado en llevar audiencias técnicas y no técnicas a la adopción real. Diseño y dicto programas de IA generativa, productividad, BI y data storytelling, con foco en cambio cultural y NPS verificable. Mi experiencia docente es evidencia de una capacidad crítica: traducir complejidad técnica en adopción organizacional.",
               "en":"Educator and facilitator in applied AI with 25+ years in data and AI, specialized in taking technical and non-technical audiences to real adoption. I design and deliver programs in generative AI, productivity, BI and data storytelling, focused on cultural change and verifiable NPS. My teaching experience is evidence of a critical capability: translating technical complexity into organizational adoption."},
   "cases": {"es":[("Collective Academy — AI Productivity Tools","2 cohortes (40+ participantes) en GenAI, automatización y datos. NPS 70 y 60."),
                   ("Asuntos Digitales — IA aplicada para negocios","diseño y dictado de módulos de IA para productividad, marketing, operaciones y ventas (audiencias LATAM)."),
                   ("Universidad Militar Nueva Granada","diplomados de IA generativa, Legal Tech, ética e investigación aplicada."),
                   ("Crehana — Business Analytics con Python","curso publicado de analítica aplicada con Excel y Python.")],
             "en":[("Collective Academy — AI Productivity Tools","2 cohorts (40+ participants) in GenAI, automation and data. NPS 70 and 60."),
                   ("Asuntos Digitales — applied AI for business","design and delivery of AI modules for productivity, marketing, operations and sales (LATAM audiences)."),
                   ("Universidad Militar Nueva Granada","diplomas in generative AI, Legal Tech, ethics and applied research."),
                   ("Crehana — Business Analytics with Python","published applied-analytics course with Excel and Python.")]},
   "skills": "AI Literacy · Executive Education · Corporate Training · Change Management · AI Adoption · Curriculum Design · Workshops · Data Storytelling · Public Speaking · Non-technical Enablement · NPS · Generative AI · Prompt Engineering",
 },
}

CSS = """
@font-face{font-family:'IgraSans';src:url(IgraSans.otf) format('opentype');font-weight:400;}
:root{--purple:#4e00ff;--deep:#041c59;--text:#1f2937;--muted:#5f6b7a;--link:#0048ff;--border:#e3e8f5;--lila:#f6f3ff;}
*{box-sizing:border-box}
@page{size:A4;margin:0.55cm 0.95cm;}
body{font-family:'IgraSans',Aptos,Helvetica,Arial,sans-serif;color:var(--text);font-size:9.7px;line-height:1.26;margin:0;}
h1{font-size:22.5px;color:var(--deep);margin:0;font-weight:800;font-feature-settings:"liga" 1,"ss01" 1;font-variant-ligatures:common-ligatures;}
.role{color:var(--purple);font-weight:700;font-size:10.7px;margin:2px 0 4px;}
.contact{font-size:8.8px;color:var(--muted);margin-bottom:6px;}
.contact a{color:var(--link);text-decoration:none;}
h2{font-size:10.2px;color:var(--deep);text-transform:uppercase;letter-spacing:.09em;font-weight:800;border-left:3px solid var(--purple);padding-left:7px;margin:8px 0 4px;}
.summary{font-size:9.7px;margin-bottom:2px;text-align:justify;}
.snap{display:flex;flex-wrap:wrap;gap:5px;margin:1px 0;}
.kpi{background:var(--lila);border:1px solid var(--border);border-radius:7px;padding:3px 8px;font-size:8.7px;color:var(--deep);}
.kpi b{color:var(--purple);font-size:11.2px;display:block;}
.proj{margin-bottom:3px;} .proj b{color:var(--deep);}
.item{margin-bottom:4px;}
.item .h{display:flex;justify-content:space-between;gap:10px;}
.item .t{font-weight:800;color:var(--deep);font-size:9.7px;}
.item .d{color:var(--muted);font-size:8.5px;white-space:nowrap;}
.item .org{color:var(--purple);font-weight:700;font-size:9px;margin:0 0 1px;}
ul{margin:1px 0 0;padding-left:14px;} li{margin-bottom:1px;}
.prev li{margin-bottom:2px;color:var(--text);}
.stack{background:var(--lila);border:1px solid var(--border);border-radius:9px;padding:6px 10px;font-size:9.1px;color:var(--deep);line-height:1.5;}
.foot{margin-top:8px;border-top:1px solid var(--border);padding-top:5px;text-align:center;font-size:8.2px;color:var(--muted);}
.foot .sep{color:var(--purple);} .foot a{color:var(--link);text-decoration:none;}
"""

def render(profile_key, lang):
    p = PROFILES[profile_key]; d = L[lang]
    kpis = "".join(f'<div class="kpi"><b>{n}</b>{t}</div>' for n,t in d["kpis"])
    cases = "".join(f'<div class="proj"><b>{t}.</b> {desc}</div>' for t,desc in p["cases"][lang])
    exp = ""
    for t,org,dt,bul in d["exp"]:
        lis = "".join(f"<li>{b}</li>" for b in bul)
        exp += f'<div class="item"><div class="h"><span class="t">{t}</span><span class="d">{dt}</span></div><div class="org">{org}</div><ul>{lis}</ul></div>'
    prev = "".join(f"<li>{x}</li>" for x in d["prev"])
    edu = "".join(f"<li>{x}</li>" for x in d["edu"])
    return f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<h1>JAVIER FORERO</h1>
<div class="role">{p['title'][lang]}</div>
<div class="contact">{CONTACT}</div>
<h2>{d['title_html']}</h2><div class="summary">{p['summary'][lang]}</div>
<h2>{d['kpis_h']}</h2><div class="snap">{kpis}</div>
<h2>{d['cases_h']}</h2>{cases}
<h2>{d['exp_h']}</h2>{exp}
<h2>{d['prev_h']}</h2><ul class="prev">{prev}</ul>
<h2>{d['teach_h']}</h2><div class="summary">{d['teach']}</div>
<h2>{d['skills_h']}</h2><div class="stack">{p['skills']}</div>
<h2>{d['edu_h']}</h2><ul>{edu}</ul>
<div class="foot">Javier Forero <span class="sep">·</span> <a href="https://javierforero.co">javierforero.co</a></div>
</body></html>"""

if __name__ == "__main__":
    n = 0
    for key in PROFILES:
        for lang in ("es","en"):
            html = render(key, lang)
            out = os.path.join(OUT, f"Javier_Forero_CV_{key}_{lang.upper()}.pdf")
            weasyprint.HTML(string=html, base_url=BASE).write_pdf(out)
            n += 1
            print(f"  ✓ {os.path.basename(out)}")
    print(f"{n} PDFs generados en CV_ATS/")
