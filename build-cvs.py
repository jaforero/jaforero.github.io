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
  "teach": "Universidad del Rosario — Rosario GSB (curso ejecutivo &quot;IA para el Liderazgo&quot;, 3 de 8 módulos, evaluación docente 4,6/5), Universidad de los Andes (educación continua corporativa en IA y analítica avanzada), Universidad Militar Nueva Granada (IA generativa, Legal Tech, ética), Collective Academy (AI Productivity Tools, NPS 70/60; BI &amp; Data Analytics MBA), Crehana (Business Analytics con Python) y Asuntos Digitales (NPS 85–95; Programa de Certificación de Claude: agentes y MCP). Talleres ejecutivos con Connect (Impulso IA 360), SEC (analítica para microempresarios), agencias y gremios.",
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
  "teach": "Universidad del Rosario — Rosario GSB (executive program &quot;AI for Leadership&quot;, 3 of 8 modules, 4.6/5 teaching score), Universidad de los Andes (corporate continuing education in AI and advanced analytics), Universidad Militar Nueva Granada (generative AI, Legal Tech, ethics), Collective Academy (AI Productivity Tools, NPS 70/60; BI &amp; Data Analytics MBA), Crehana (Business Analytics with Python) and Asuntos Digitales (NPS 85–95; Claude Certification program: agents and MCP). Executive AI workshops with Connect (Impulso IA 360), SEC (analytics for micro-entrepreneurs), agencies and industry guilds.",
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
                   ("Pintacomex (México) — Estrategia Data &amp; AI","diagnóstico, arquitectura objetivo y roadmap en 3 fases para pasar de un entorno legacy C/MySQL a una plataforma de datos gobernada, lista para analítica avanzada e IA."),
                   ("Impulso IA 360 — Connect Bogotá","consultoría y formación por áreas para identificar, priorizar y prototipar casos de uso de IA.")],
             "en":[("Johnson &amp; Johnson — Corporate Business Technology","co-led advanced analytics, AI and automation for global corporate functions; strategic business–data bridge; responsible AI and GenAI adoption."),
                   ("J&amp;J — Procurement Shared Services Americas","led BI, predictive and prescriptive analytics for the region; standardized reporting and automated analyses."),
                   ("NEICON (Postobón, Efecty)","corporate analytics solutions, data architecture and scalable pipelines focused on quality and adoption."),
                   ("Pintacomex (Mexico) — Data &amp; AI strategy","assessment, target architecture and 3-phase roadmap to move a legacy C/MySQL environment to a governed data platform ready for advanced analytics and AI."),
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
                   ("B&amp;Optimos — Diseño muestral Encuesta de Movilidad 2026","diseño probabilístico para la Cámara de Comercio de Bogotá, con trazabilidad condición → parámetro → precisión y marco muestral construido en Python."),
                   ("J&amp;J — Procurement Analytics Americas","BI, analítica predictiva y prescriptiva con reporting estandarizado para el liderazgo regional."),
                   ("SEC / Asoanei — Modelo de datos y Power BI","modelo de datos unificado, visión 360° del productor, gobernanza y roadmap Microsoft Fabric."),
                   ("Databricks — Análisis por industria (BNA)","análisis de ventas, precio y drop size con Pareto y series temporales en PySpark.")],
             "en":[("RAC Evolution","brand-intelligence product: longitudinal base 2003–2025, 12 analytical modules, AI narratives and a TARGET-segment evolution."),
                   ("B&amp;Optimos — Sample design, 2026 Mobility Survey","probability design for the Bogotá Chamber of Commerce, tracing each condition to a parameter and its precision, with a sampling frame built in Python."),
                   ("J&amp;J — Procurement Analytics Americas","BI, predictive and prescriptive analytics with standardized reporting for regional leadership."),
                   ("SEC / Asoanei — Data model & Power BI","unified data model, 360° producer view, governance and a Microsoft Fabric roadmap."),
                   ("Databricks — industry analysis (BNA)","sales, price and drop-size analysis with Pareto and time series in PySpark.")]},
   "skills": "Business Intelligence · Power BI · Tableau · Predictive Analytics · Prescriptive Analytics · Decision Intelligence · Data Products · Forecasting · Databricks · PySpark · SQL · Python · Data Visualization · Statistical Modeling · Microsoft Fabric",
 },
 "Senior_Consulting": {
   "title": {"es":"Consultor Senior en IA y Datos · Advisory &amp; Transformación","en":"Senior AI &amp; Data Consultant · Advisory &amp; Transformation"},
   "summary": {"es":"Consultor senior y advisor en IA, datos y transformación, con 25+ años y experiencia multisectorial (industria, sector público, economía circular, pyme). Entrego de extremo a extremo: diagnóstico, roadmap, arquitectura de solución, gobernanza y transferencia de capacidades, con foco en creación de valor. Trayectoria como trusted advisor en Johnson &amp; Johnson, GroupM y clientes independientes.",
               "en":"Senior consultant and advisor in AI, data and transformation, with 25+ years and multi-sector experience (industry, public sector, circular economy, SMEs). I deliver end-to-end: diagnosis, roadmap, solution architecture, governance and capability transfer, focused on value creation. Trusted-advisor track record at Johnson &amp; Johnson, GroupM and independent clients."},
   "cases": {"es":[("Pintacomex (México) — Modernización Data &amp; AI","diagnóstico del entorno legacy C/MySQL, arquitectura objetivo por capas, Fabric vs. best-of-breed, gobierno/FinOps y roadmap en 3 fases (metas = impacto esperado)."),
                   ("Preflex — Consultoría técnica GenAI","diseño de solución, arquitectura y definición de MVP para automatización P2P."),
                   ("NEICON — Arquitectura de datos, BI e IA","asesoría en arquitecturas modernas y despliegue de IA en producción."),
                   ("SEC / Asoanei — Modelo de datos y gobernanza","modelo unificado, visión 360° y roadmap escalable con Microsoft Fabric y Purview."),
                   ("Impulso IA 360 — Connect Bogotá","diagnóstico, priorización y prototipado de casos de uso de IA por área.")],
             "en":[("Pintacomex (Mexico) — Data &amp; AI modernization","assessment of a legacy C/MySQL environment, layered target architecture, Fabric vs. best-of-breed, governance/FinOps and a 3-phase roadmap (targets = expected impact)."),
                   ("Preflex — GenAI technical consulting","solution design, architecture and MVP definition for P2P automation."),
                   ("NEICON — Data architecture, BI and AI","advisory on modern architectures and AI deployment to production."),
                   ("SEC / Asoanei — Data model and governance","unified model, 360° view and scalable roadmap with Microsoft Fabric and Purview."),
                   ("Impulso IA 360 — Connect Bogotá","diagnosis, prioritization and prototyping of AI use cases by area.")]},
   "skills": "AI &amp; Data Advisory · Business Transformation · Solution Architecture · Data Governance · Diagnosis &amp; Roadmap · Capability Building · Stakeholder Management · Microsoft Fabric · Power BI · Discovery Workshops · Value Creation · Operating Model · Pre-sales",
 },
 "Executive_Education": {
   "title": {"es":"Educador Ejecutivo en IA · Adopción y Alfabetización","en":"Executive AI Educator · Adoption &amp; Literacy"},
   "summary": {"es":"Educador y facilitador en IA aplicada con 25+ años en datos e IA, especializado en llevar audiencias técnicas y no técnicas a la adopción real. Diseño y dicto programas de IA generativa, productividad, BI y data storytelling —desde 5 diplomados y especializaciones B2B (7 clases/módulos, NPS 85–95) hasta talleres para comités directivos y microempresarios (Connect · Impulso IA 360; SEC)—, con foco en cambio cultural y adopción medible. Mi experiencia docente es evidencia de una capacidad crítica: traducir complejidad técnica en adopción organizacional.",
               "en":"Educator and facilitator in applied AI with 25+ years in data and AI, specialized in taking technical and non-technical audiences to real adoption. I design and deliver programs in generative AI, productivity, BI and data storytelling —from 5 B2B diplomas and specializations (7 classes/modules, NPS 85–95) to workshops for leadership committees and micro-entrepreneurs (Connect · Impulso IA 360; SEC)—, focused on cultural change and measurable adoption. My teaching experience is evidence of a critical capability: translating technical complexity into organizational adoption."},
   "cases": {"es":[("Collective Academy — AI Productivity Tools","2 cohortes (40+ participantes) en GenAI, automatización y datos. NPS 70 y 60."),
                   ("Asuntos Digitales — Docente en 5 diplomados/especializaciones B2B","7 clases/módulos: Dirección Comercial (Métricas comerciales y reporting, NPS 85–95), IA para Negocios (KPIs financieros, 4 cohortes), Marketing (chatbots, 2 cohortes), Operaciones B2B y sesiones pregrabadas."),
                   ("Talleres ejecutivos — Connect (Impulso IA 360) &amp; SEC","IA aplicada para comités directivos y microempresarios; adopción práctica con foco en resultados de negocio."),
                   ("Universidad Militar Nueva Granada","diplomados de IA generativa, Legal Tech, ética e investigación aplicada."),
                   ("Crehana — Business Analytics con Python","curso publicado de analítica aplicada con Excel y Python.")],
             "en":[("Collective Academy — AI Productivity Tools","2 cohorts (40+ participants) in GenAI, automation and data. NPS 70 and 60."),
                   ("Asuntos Digitales — Lecturer across 5 B2B diplomas/specializations","7 classes/modules: Commercial Management (Commercial metrics &amp; reporting, NPS 85–95), AI for Business (financial KPIs, 4 cohorts), Marketing (chatbots, 2 cohorts), B2B Operations and pre-recorded sessions."),
                   ("Executive workshops — Connect (Impulso IA 360) &amp; SEC","applied AI for leadership committees and micro-entrepreneurs; hands-on adoption focused on business outcomes."),
                   ("Universidad Militar Nueva Granada","diplomas in generative AI, Legal Tech, ethics and applied research."),
                   ("Crehana — Business Analytics with Python","published applied-analytics course with Excel and Python.")]},
   "skills": "AI Literacy · Executive Education · Graduate Teaching · Curriculum Design · Challenge-Based Learning · Corporate Training · Change Management · AI Adoption · Data Storytelling · Public Speaking · Non-technical Enablement · NPS · Generative AI · Prompt Engineering",
   "kpis": {"es":[("25+","Años en datos, analítica e IA"),("4,6/5","Evaluación docente — la más alta del equipo (Rosario GSB)"),
                  ("NPS 85–95","Clases de Asuntos Digitales (cohortes 2026)"),("6","Instituciones académicas donde enseño"),
                  ("100s","Profesionales formados en IA"),("7","Clases/módulos B2B diseñados y dictados"),("48 h","Curso ejecutivo de IA (Rosario GSB · ABR)")],
            "en":[("25+","Years in data, analytics &amp; AI"),("4.6/5","Teaching score — highest on the faculty (Rosario GSB)"),
                  ("NPS 85–95","Asuntos Digitales classes (2026 cohorts)"),("6","Academic institutions where I teach"),
                  ("100s","Professionals trained in AI"),("7","B2B classes/modules designed &amp; delivered"),("48 h","Executive AI course (Rosario GSB · CBL)")]},
   "teach_detail": {"es":[
       ("Universidad del Rosario — Rosario GSB · Advance (educación ejecutiva / posgrado)","Profesor invitado del curso de formación ejecutiva &quot;IA para el Liderazgo&quot; (48 h, Aprendizaje Basado en Retos): 3 de los 8 módulos, incluidos los dos de cierre y la retroalimentación de los retos finales. Evaluación docente <b>4,6/5 — la más alta del equipo de 4 profesores</b>; 8,2/10 en aprendizaje percibido del curso."),
       ("Universidad de los Andes — Educación Continua","Profesor invitado en un programa corporativo de la Academia de Inteligencia Aplicada (&quot;IA y Analítica avanzada para resolver retos estratégicos&quot;), en tres módulos técnicos: Analítica de Datos Avanzada, Construcción de Prototipos Analíticos y Dominio Técnico Avanzado con IA. Cliente corporativo confidencial."),
       ("Asuntos Digitales — diplomados y especializaciones B2B","Diseño y docencia de 7 clases/módulos en 5 programas: Dirección Comercial y Ventas con IA (clase &quot;Métricas comerciales, reporting y toma de decisiones con IA&quot;, <b>NPS 85–95</b> en cohortes jul–sep 2026), IA Aplicada a los Negocios (KPIs financieros, 5 cohortes), IA para Marketing (chatbots de venta, 2 cohortes) y Operaciones B2B. Además, Programa de Certificación de Claude: Live de métricas de negocio y sesión de agentes con MCP. NPS público institucional &gt;85."),
       ("Collective Academy — educación ejecutiva y MBA","Mentor en AI Productivity Tools (2 cohortes, 40+ participantes; NPS 70 y 60) y en Business Intelligence &amp; Data Analytics para cohortes MBA (NPS 40 y 50)."),
       ("Universidad Militar Nueva Granada — docencia universitaria","Docente y conferencista en diplomados de IA generativa, Legal Tech, análisis documental, investigación aplicada y uso responsable/ética de la IA. Nueva generación 2026-II: curso &quot;Herramientas Tecnológicas al servicio del Derecho&quot; (5 sesiones de 4 h — 20 h)."),
       ("Crehana — curso publicado","Profesor del curso &quot;Business Analytics with Python and Excel&quot;: analítica aplicada para audiencias masivas."),
       ("Talleres ejecutivos y gremiales","IA para comités directivos y microempresarios: Connect (Programa de Impulso IA 360), SEC (analítica para microempresarios), agencias creativas (Bumerang, Performer, La Mediática) y gremios (ACIA/ASOPESAJE).")],
     "en":[
       ("Universidad del Rosario — Rosario GSB · Advance (executive / graduate education)","Guest professor of the executive course &quot;AI for Leadership&quot; (48 h, Challenge-Based Learning): 3 of the 8 modules, including both closing modules and the final-challenge feedback. Teaching score <b>4.6/5 — the highest of the 4-professor faculty</b>; 8.2/10 in perceived learning."),
       ("Universidad de los Andes — Continuing Education","Guest professor in a corporate program of the Applied Intelligence Academy (&quot;AI and advanced analytics to solve strategic challenges&quot;), across three technical modules: Advanced Data Analytics, Building Analytical Prototypes and Advanced Technical Mastery with AI. Confidential corporate client."),
       ("Asuntos Digitales — B2B diplomas and specializations","Design and teaching of 7 classes/modules across 5 programs: Commercial Management &amp; Sales with AI (class &quot;Commercial metrics, reporting &amp; decision-making with AI&quot;, <b>NPS 85–95</b> across Jul–Sep 2026 cohorts), AI Applied to Business (financial KPIs, 5 cohorts), AI for Marketing (sales chatbots, 2 cohorts) and B2B Operations. Also a Claude Certification program: business-metrics Live and an MCP agents session. Public institutional NPS &gt;85."),
       ("Collective Academy — executive education and MBA","Mentor in AI Productivity Tools (2 cohorts, 40+ participants; NPS 70 and 60) and in Business Intelligence &amp; Data Analytics for MBA cohorts (NPS 40 and 50)."),
       ("Universidad Militar Nueva Granada — university teaching","Lecturer and speaker in diploma programs on generative AI, Legal Tech, document analysis, applied research and responsible/ethical AI use. New 2026-II cohort: course &quot;Technology Tools Serving Law&quot; (5 sessions of 4 h — 20 h)."),
       ("Crehana — published course","Instructor of &quot;Business Analytics with Python and Excel&quot;: applied analytics for mass audiences."),
       ("Executive &amp; industry workshops","Applied AI for leadership committees and micro-entrepreneurs: Connect (Impulso IA 360 program), SEC (analytics for micro-entrepreneurs), creative agencies (Bumerang, Performer, La Mediática) and industry guilds (ACIA/ASOPESAJE).")]},
   "acad": {"es":[
       ("Metodologías y diseño curricular","Aprendizaje Basado en Retos (70% práctico / 30% teórico), diseño de currículo, rúbricas y evaluación; data storytelling y framework propio &quot;5 niveles de analítica de datos&quot;; prototipos y casos aplicados con ChatGPT, Claude, Gemini, Copilot, Perplexity y NotebookLM."),
       ("Base académica","Estadístico, Universidad Nacional de Colombia. Participación recurrente en el Simposio Internacional de Estadística de la UNAL (Estadística No Paramétrica, Control de Calidad, Investigación Social y Ciencia de Datos)."),
       ("Contenido y liderazgo de pensamiento","Charlas como &quot;IA en Acción: De la Atención a la Conversión&quot;; canal de YouTube sobre IA y datos; materiales y recursos entregados en los portales de alumnos.")],
     "en":[
       ("Methodologies and curriculum design","Challenge-Based Learning (70% hands-on / 30% theory), curriculum design, rubrics and assessment; data storytelling and a proprietary &quot;5 levels of data analytics&quot; framework; prototypes and applied cases with ChatGPT, Claude, Gemini, Copilot, Perplexity and NotebookLM."),
       ("Academic foundation","Statistician, Universidad Nacional de Colombia. Recurring participation in the UNAL International Statistics Symposium (Nonparametric Statistics, Quality Control, Social Research and Data Science)."),
       ("Content and thought leadership","Talks such as &quot;AI in Action: From Attention to Conversion&quot;; a YouTube channel on AI and data; materials and resources delivered through student portals.")]},
   "catalog": {"es":[
       ("Estrategia, liderazgo y gobierno de IA","IA para el liderazgo; diagnóstico de madurez y hoja de ruta de adopción a 90 días; gobernanza, ética y uso responsable; futuro del trabajo, upskilling/reskilling e impacto de la IA en LATAM."),
       ("IA generativa aplicada","Prompt engineering avanzado; asistentes y agentes de IA; automatización con GenAI (comprensión documental, reglas y excepciones); RAG para negocio y multimodalidad."),
       ("Analítica, métricas y decisión","Métricas comerciales, reporting y toma de decisiones con IA; KPIs financieros; BI y dashboards; data storytelling; framework &quot;5 niveles de analítica de datos&quot;."),
       ("Productividad y operaciones B2B","ChatGPT, Claude, Gemini, Copilot y NotebookLM aplicados al trabajo; organización y gestión inteligente de información; &quot;análisis y síntesis de datos sin ser analista&quot;.")],
     "en":[
       ("AI strategy, leadership and governance","AI for leadership; maturity assessment and 90-day adoption roadmap; governance, ethics and responsible use; future of work, upskilling/reskilling and AI's impact in LATAM."),
       ("Applied generative AI","Advanced prompt engineering; AI assistants and agents; automation with GenAI (document understanding, rules and exceptions); business RAG and multimodality."),
       ("Analytics, metrics and decision-making","Commercial metrics, reporting and decision-making with AI; financial KPIs; BI and dashboards; data storytelling; the &quot;5 levels of data analytics&quot; framework."),
       ("Productivity and B2B operations","ChatGPT, Claude, Gemini, Copilot and NotebookLM applied to work; smart information organization and management; &quot;data analysis and synthesis without being an analyst&quot;.")]},
   "certs": {"es":[
       ("IA, GenAI, LLMs &amp; ML","5-Day Gen AI Intensive (Google/Kaggle, 2025) · Generative AI with LLMs (DeepLearning.AI/AWS) · Building Agentic RAG with LlamaIndex · LangChain for LLM App Development · Multimodal Llama 3.2 · ChatGPT Prompt Engineering · GenAI for Business Leaders · Deep Learning · Reinforcement Learning · NLP con Python."),
       ("Ciencia de datos, analítica &amp; cloud","Data Science in Stratified Healthcare — Edinburgh · Data Science for All (DS4A) 375 h — Correlation One / MinTIC · Python for Everybody — Michigan · Data Science Specialization — Johns Hopkins · Microsoft Azure Relational Databases."),
       ("Producto, agile &amp; liderazgo","Agentic AI for Leadership — LinkedIn · Product Management Foundations &amp; Metrics · Agile &amp; Design Thinking · Digital Leadership Program — Google (INALDE Business School).")],
     "en":[
       ("AI, GenAI, LLMs &amp; ML","5-Day Gen AI Intensive (Google/Kaggle, 2025) · Generative AI with LLMs (DeepLearning.AI/AWS) · Building Agentic RAG with LlamaIndex · LangChain for LLM App Development · Multimodal Llama 3.2 · ChatGPT Prompt Engineering · GenAI for Business Leaders · Deep Learning · Reinforcement Learning · NLP with Python."),
       ("Data science, analytics &amp; cloud","Data Science in Stratified Healthcare — Edinburgh · Data Science for All (DS4A) 375 h — Correlation One / MinTIC · Python for Everybody — Michigan · Data Science Specialization — Johns Hopkins · Microsoft Azure Relational Databases."),
       ("Product, agile &amp; leadership","Agentic AI for Leadership — LinkedIn · Product Management Foundations &amp; Metrics · Agile &amp; Design Thinking · Digital Leadership Program — Google (INALDE Business School).")]},
   "edu": {"es":["<b>Estadístico</b> — Universidad Nacional de Colombia.",
                 "<b>Idiomas:</b> español (nativo) · inglés (profesional / C1).",
                 "<b>Reconocimientos:</b> 14 Johnson &amp; Johnson Inspire Awards y 1 Encore Award."],
           "en":["<b>Statistician</b> — Universidad Nacional de Colombia.",
                 "<b>Languages:</b> Spanish (native) · English (professional / C1).",
                 "<b>Recognition:</b> 14 Johnson &amp; Johnson Inspire Awards and 1 Encore Award."]},
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
    kpi_data = p["kpis"][lang] if "kpis" in p else d["kpis"]
    kpis = "".join(f'<div class="kpi"><b>{n}</b>{t}</div>' for n,t in kpi_data)
    cases = "".join(f'<div class="proj"><b>{t}.</b> {desc}</div>' for t,desc in p["cases"][lang])
    exp = ""
    for t,org,dt,bul in d["exp"]:
        lis = "".join(f"<li>{b}</li>" for b in bul)
        exp += f'<div class="item"><div class="h"><span class="t">{t}</span><span class="d">{dt}</span></div><div class="org">{org}</div><ul>{lis}</ul></div>'
    prev = "".join(f"<li>{x}</li>" for x in d["prev"])
    edu = "".join(f"<li>{x}</li>" for x in d["edu"])
    head = f"""<!DOCTYPE html><html lang="{lang}"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<h1>JAVIER FORERO</h1>
<div class="role">{p['title'][lang]}</div>
<div class="contact">{CONTACT}</div>
<h2>{d['title_html']}</h2><div class="summary">{p['summary'][lang]}</div>
<h2>{d['kpis_h']}</h2><div class="snap">{kpis}</div>"""
    foot = '<div class="foot">Javier Forero <span class="sep">·</span> <a href="https://javierforero.co">javierforero.co</a></div>\n</body></html>'
    # Perfil con capa académica profunda (p.ej. Educación Ejecutiva): docencia primero, 2 páginas.
    if "teach_detail" in p:
        H = {"es":("Trayectoria docente y académica","Metodologías, diseño curricular y base académica","Programas y temas que diseño e imparto","Certificaciones y formación (selección · 71 credenciales)"),
             "en":("Teaching &amp; academic track record","Methodologies, curriculum design &amp; academic foundation","Programs &amp; topics I design and teach","Certifications &amp; training (selected · 71 credentials)")}[lang]
        tdet = "".join(f'<div class="proj"><b>{t}.</b> {desc}</div>' for t,desc in p["teach_detail"][lang])
        acad = "".join(f'<div class="proj"><b>{t}.</b> {desc}</div>' for t,desc in p["acad"][lang])
        catalog = "".join(f'<div class="proj"><b>{t}:</b> {desc}</div>' for t,desc in p["catalog"][lang])
        certs = "".join(f'<div class="proj"><b>{t}:</b> {desc}</div>' for t,desc in p["certs"][lang])
        edu2 = "".join(f"<li>{x}</li>" for x in (p["edu"][lang] if "edu" in p else d["edu"]))
        return head + f"""
<h2>{H[0]}</h2>{tdet}
<h2>{H[1]}</h2>{acad}
<h2>{H[2]}</h2>{catalog}
<h2>{d['exp_h']}</h2>{exp}
<h2>{d['prev_h']}</h2><ul class="prev">{prev}</ul>
<h2>{H[3]}</h2>{certs}
<h2>{d['skills_h']}</h2><div class="stack">{p['skills']}</div>
<h2>{d['edu_h']}</h2><ul>{edu2}</ul>
""" + foot
    return head + f"""
<h2>{d['cases_h']}</h2>{cases}
<h2>{d['exp_h']}</h2>{exp}
<h2>{d['prev_h']}</h2><ul class="prev">{prev}</ul>
<h2>{d['teach_h']}</h2><div class="summary">{d['teach']}</div>
<h2>{d['skills_h']}</h2><div class="stack">{p['skills']}</div>
<h2>{d['edu_h']}</h2><ul>{edu}</ul>
""" + foot

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
