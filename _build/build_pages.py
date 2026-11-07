"""Generate project case-study pages and service pages for shamsullah01.github.io.

Run from the repo root:   python _build/build_pages.py
Edit the PROJECTS / SERVICES data below, re-run, commit and push.
GitHub Pages (Jekyll) ignores folders starting with "_", so this script is not published.
"""
import json
import os
from datetime import date
from html import escape, unescape

SITE = "https://shamsullah01.github.io"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TODAY = date.today().isoformat()
PERSON_ID = f"{SITE}/#person"
EMAIL = "shamsullahbaig999@gmail.com"
WHATSAPP = "https://wa.me/923179292371"
LINKEDIN = "https://www.linkedin.com/in/shams-ullah-baig-8312a018b/"
GITHUB = "https://github.com/shamsullah01"
X_URL = "https://x.com/Shamsullah999"

# --------------------------------------------------------------------------------------
# Projects. Keep claims factual: only what the CV states or the live site shows.
# --------------------------------------------------------------------------------------
PROJECTS = [
    {
        "slug": "agentra-ai-agents",
        "name": "Agentra by Valour AI",
        "short": "Agentra",
        "kind": "AI agent platform",
        "tag": "AI",
        "shot": "agentra",
        "url": "https://agents.valour.ai/",
        "c": ("#16365f", "#05101d"),
        "title": "Agentra AI Business Agents | AI Engineer Case Study",
        "desc": "Case study: Agentra by Valour AI, a platform that builds custom AI agents trained on a business's own documents to answer customers, qualify leads and book appointments 24/7.",
        "lead": "Custom AI agents that learn a business's own documents and handle customer conversations around the clock: answering questions, screening prospects and booking appointments straight into the calendar.",
        "client": "ValourAI (international client)",
        "role": "Developer, ValourAI team",
        "industry": "AI / SaaS",
        "stack": ["AI Agents", "LLMs", "React", "TypeScript", "Node.js", "NestJS", "REST APIs"],
        "overview": [
            "Agentra builds an AI agent for a business, trained on its own material: price lists, opening hours, policies and FAQs. The agent works 24/7 across channels, so small businesses such as clinics and service providers stop missing enquiries outside office hours.",
            "I worked on Agentra as part of the remote ValourAI team, collaborating with international stakeholders through code reviews, async standups and agile sprints.",
        ],
        "built": [
            "Interfaces for setting up and previewing a business's AI agent, built in React",
            "Conversation flows for the agent's core jobs: answering questions, capturing leads and booking appointments",
            "API work connecting the front end to the agent and booking back end",
            "Responsive, fast-loading pages for the product and marketing site",
        ],
        "features": [
            "AI agent trained on the business's own documents",
            "Appointment booking directly into the calendar",
            "Answers about services, hours, insurance and location",
            "Lead capture so no enquiry is missed, 24/7",
        ],
        "results": [
            "Live product serving businesses at agents.valour.ai",
            "Agents answer and book without staff involvement, around the clock",
        ],
    },
    {
        "slug": "dts-gilgit-baltistan-tourism-portal",
        "name": "DTS Gilgit-Baltistan Tourism Portal",
        "short": "DTS GB",
        "kind": "Government licensing portal",
        "tag": "GovTech",
        "shot": "dts",
        "url": "https://app.dtsgb.gog.pk/",
        "c": ("#1d4d2c", "#04110a"),
        "title": "DTS Gilgit-Baltistan Tourism Portal | Full-Stack Developer Case Study",
        "desc": "Case study: the DTS Gilgit-Baltistan government portal for licensing tour operators, hotels and tourist guides, with online payments, renewals, certificates and mountaineering permits.",
        "lead": "A government portal that moves tourism licensing in Gilgit-Baltistan online: tour operators, hotels, camping sites and tourist guides register, pay, renew and receive official certificates in one place.",
        "client": "Government of Gilgit-Baltistan (via uExel Foundation)",
        "role": "Front-end owner (React)",
        "industry": "Government / Tourism",
        "stack": ["React", "TypeScript", "NestJS", "REST APIs", "Online Payments", "AWS"],
        "overview": [
            "DTS is the Gilgit-Baltistan portal for tourism licensing. It replaces paper-based applications with an online system for every licence type the department issues, plus permits for mountaineering and trekking in restricted areas.",
            "I owned the React front end of this production system for a public-sector user base, working within the uExel Foundation team that also delivered PROMIS, IMS and UXL POS.",
        ],
        "built": [
            "The React front end: sign-in, account creation and applicant dashboards",
            "Application flows for each licence type: tour operators, hotels and camping sites, and tourist guides",
            "Registration, renewal and status tracking screens",
            "Integration with the NestJS back end and the online payment step",
        ],
        "features": [
            "Licensing for tour operators, hotels/camping sites and tourist guides",
            "Streamlined online registration with renewal reminders",
            "Secure online payments with multiple options",
            "Official digital certificates and credentials",
            "Mountaineering permits (peaks above 6,000 m) and trekking permits for restricted zones",
        ],
        "results": [
            "Production government system in daily use",
            "Licensing processed online in 3 to 14 days, with licences valid for a renewable year",
        ],
    },
    {
        "slug": "promis-product-management-system",
        "name": "PROMIS",
        "short": "PROMIS",
        "kind": "Product management information system",
        "tag": "HealthTech",
        "shot": "promis",
        "url": "https://promis.precipiodx.com/",
        "c": ("#0f4c5c", "#04121a"),
        "title": "PROMIS Healthcare Product Management System | Full-Stack Case Study",
        "desc": "Case study: PROMIS, a product management information system for a diagnostics company, built with React and NestJS, with full module ownership of products, orders and clinical data workflows.",
        "lead": "A one-stop Product Management Information System for a diagnostics company, used to manage products, access order details and run clinical data workflows.",
        "client": "Precipio Diagnostics (via uExel Foundation)",
        "role": "Full-stack developer, module owner",
        "industry": "Healthcare / Diagnostics",
        "stack": ["React", "TypeScript", "NestJS", "Node.js", "REST APIs", "SQL"],
        "overview": [
            "PROMIS gives a diagnostics company one system for its product catalogue, orders and the clinical data that flows around them.",
            "I had full ownership of modules covering clinical data workflows, from the NestJS API to the React screens.",
        ],
        "built": [
            "End-to-end modules for clinical data workflows: data model, NestJS APIs and React UI",
            "Product and order management screens",
            "Authenticated dashboard with role-appropriate views",
            "Reusable UI components shared across modules",
        ],
        "features": [
            "Product management in one place",
            "Order details and status for each customer",
            "Clinical data workflows owned end to end",
            "Secure sign-in with remember-me and password recovery",
        ],
        "results": [
            "Live production system for a healthcare client",
            "Full module ownership, from database to UI",
        ],
    },
    {
        "slug": "ims-ai-enterprise-platform",
        "name": "IMS for USS Group",
        "short": "IMS",
        "kind": "AI-integrated enterprise platform",
        "tag": "AI + ERP",
        "shot": None,
        "url": "https://ims.ussgroup.pk/",
        "c": ("#3a2a66", "#0a0716"),
        "title": "IMS AI Enterprise Platform for USS Group | AI Engineer Case Study",
        "desc": "Case study: IMS, an AI-integrated enterprise platform for USS Group built with React and NestJS. Its AI data processing cut manual data entry by about 30%.",
        "lead": "An enterprise information management platform for USS Group, with AI data processing that takes repetitive data entry off staff.",
        "client": "USS Group (via uExel Foundation)",
        "role": "Full-stack developer, AI integration",
        "industry": "Enterprise",
        "stack": ["React", "NestJS", "Node.js", "AI Data Processing", "REST APIs", "AWS"],
        "overview": [
            "IMS is USS Group's internal platform for managing operational data across the business.",
            "I built features across the React front end and NestJS back end, including the AI data processing that reads and structures information so staff no longer type it in by hand.",
        ],
        "built": [
            "AI-assisted data processing that turns incoming information into structured records",
            "React dashboards and data-entry screens",
            "NestJS APIs and database models behind them",
            "Deployment on AWS",
        ],
        "features": [
            "AI data processing for intake",
            "Central dashboard for operational data",
            "Role-based access for staff",
        ],
        "results": [
            "Manual data entry reduced by about 30%",
            "Live production platform for an enterprise client",
        ],
    },
    {
        "slug": "uxl-pos-point-of-sale",
        "name": "UXL POS",
        "short": "UXL POS",
        "kind": "Multi-tenant point-of-sale SaaS",
        "tag": "SaaS",
        "shot": "pos",
        "url": "https://app.uxlpos.com/",
        "c": ("#5c1f2a", "#14050a"),
        "title": "UXL POS Multi-Tenant Point-of-Sale System | Full-Stack Case Study",
        "desc": "Case study: UXL POS, a multi-tenant point-of-sale SaaS with real-time transactions, inventory and invoicing, built with React and NestJS, with payment-gateway integration.",
        "lead": "A multi-tenant point-of-sale system where each business gets its own space for sales, inventory and invoices, updated in real time.",
        "client": "uExel Foundation (SaaS product)",
        "role": "Full-stack developer",
        "industry": "Retail / SaaS",
        "stack": ["React", "NestJS", "Node.js", "MySQL", "Payment Gateway", "AWS"],
        "overview": [
            "UXL POS is a SaaS point-of-sale product. Many businesses run on one platform, each with its own isolated data, staff and settings.",
            "I worked across the stack on transactions, inventory and invoicing. The uExel team also integrated a third-party payment gateway, which cut manual billing overhead by about 40%.",
        ],
        "built": [
            "Multi-tenant architecture so each business's data stays separate",
            "Real-time sales transactions and stock updates",
            "Inventory management and invoicing",
            "Payment-gateway integration for online transactions",
        ],
        "features": [
            "Separate workspace per business (multi-tenant)",
            "Real-time transactions and inventory",
            "Invoice generation",
            "Online payments",
        ],
        "results": [
            "Live SaaS product at app.uxlpos.com",
            "Payment-gateway integration cut manual billing overhead by about 40% (uExel Foundation)",
            "Hosted on AWS with 99%+ uptime",
        ],
    },
    {
        "slug": "elham-asia-tour-operator-website",
        "name": "Elham Asia",
        "short": "Elham Asia",
        "kind": "Tour operator website",
        "tag": "Travel",
        "shot": "elham",
        "url": "https://www.elhamasia.com/",
        "c": ("#5b3d10", "#140c03"),
        "title": "Elham Asia Tour Operator Website | Web Developer Case Study",
        "desc": "Case study: the website for Elham Asia, a licensed Islamabad tour operator offering K2 Base Camp treks, 8,000 m expeditions, festival tours and all-inclusive holidays in Pakistan.",
        "lead": "The website for a licensed Islamabad tour operator that runs guided holidays, treks and expeditions across Pakistan and Asia.",
        "client": "Elham Asia",
        "role": "Web developer",
        "industry": "Travel / Tourism",
        "stack": ["Web Development", "Responsive UI", "UI/UX", "SEO"],
        "overview": [
            "Elham Asia has run guided holidays, treks and expeditions since 2020: K2 Base Camp and Gondogoro La treks, expeditions up to 8,000-metre peaks, festival tours, bike tours and corporate retreats.",
            "The site has to show a large catalogue of trips clearly on any device and turn visitors into enquiries.",
        ],
        "built": [
            "Responsive pages for destinations, tours, treks and expeditions",
            "Clear navigation across a large trip catalogue",
            "Enquiry paths such as WhatsApp and tour customisation",
            "Performance and on-page SEO for travel searches",
        ],
        "features": [
            "Destinations, tours, trekking, expeditions and corporate retreats",
            "Customise-your-trip option",
            "Blog, dark mode and quick WhatsApp contact",
        ],
        "results": [
            "Live website for a licensed tour operator",
        ],
    },
    {
        "slug": "evraah-ev-charger-locator",
        "name": "EVRAAH",
        "short": "EVRAAH",
        "kind": "EV charger locator & route planner",
        "tag": "Personal product",
        "shot": "evraah",
        "url": "https://evraah.com/",
        "c": ("#123e66", "#03070d"),
        "title": "EVRAAH EV Charger Locator & Route Planner for Pakistan | Case Study",
        "desc": "Case study: EVRAAH, Shams Ullah Baig's own product, Pakistan's EV charger locator and route planner. Find compatible stations, compare networks and plan charging stops.",
        "lead": "My own product: Pakistan's EV charger locator and route planner. Drivers find compatible public charging stations, compare networks and plan charging stops before they set off.",
        "client": "Personal project",
        "role": "Founder & full-stack developer",
        "industry": "Mobility / EV",
        "stack": ["Full-Stack", "React", "Node.js", "Maps", "Route Planning"],
        "overview": [
            "Electric cars are new in Pakistan and public chargers are spread across different networks. EVRAAH brings them into one map and adds a route planner that accounts for the car and its battery.",
            "I designed and built it end to end, from data collection and the station database to the map, route planner and UI.",
        ],
        "built": [
            "Charger map of stations across Pakistan, tracked by hand",
            "Route planner that takes origin, destination, EV model, battery level and connector type",
            "Filters by network, city and connector (for example CCS2)",
            "Responsive web app, with Android and iOS apps on the way",
        ],
        "features": [
            "69 stations, 6 networks, 12 cities, 3 provinces",
            "Route planning by EV model, battery and connector",
            "Network comparison",
            "City guides",
        ],
        "results": [
            "Live at evraah.com",
            "Covers 69 stations across 12 cities",
        ],
    },
]

# --------------------------------------------------------------------------------------
# Service pages
# --------------------------------------------------------------------------------------
SERVICES = [
    {
        "slug": "hire-full-stack-developer",
        "nav": "Full-Stack",
        "name": "Full-Stack Web Development",
        "title": "Hire a Full-Stack Developer in Pakistan (Remote) | Shams Ullah Baig",
        "desc": "Hire Shams Ullah Baig, a full-stack developer in Islamabad, Pakistan, for React, Node.js and NestJS web apps, SaaS, dashboards, APIs and payment integration. Remote, freelance or full-time.",
        "eyebrow": "Service · Full-Stack Developer",
        "h1": "Hire a Full-Stack Developer in Pakistan",
        "lead": "I build complete web applications end to end, from database and API to a fast React front end and cloud deployment. 3+ years shipping production systems for government, healthcare, SaaS and retail clients. Available remotely worldwide.",
        "offer_title": "What I build",
        "offer": [
            ("SaaS & multi-tenant platforms", "Products where many customers share one platform with separate data, like UXL POS."),
            ("Business systems & dashboards", "Admin panels, internal tools and data-heavy dashboards, like PROMIS and IMS."),
            ("Government & enterprise portals", "Secure portals with applications, approvals and payments, like the DTS Gilgit-Baltistan portal."),
            ("REST APIs & integrations", "NestJS/Express APIs, JWT authentication, third-party APIs and payment gateways."),
            ("Websites that convert", "Fast, responsive, SEO-ready sites, like Elham Asia."),
            ("Performance & security fixes", "Speeding up and hardening existing React/Node apps."),
        ],
        "stack": ["React", "Next.js", "TypeScript", "JavaScript", "Node.js", "NestJS", "Express", "Python", "MongoDB", "PostgreSQL", "MySQL", "REST APIs", "JWT", "AWS (EC2, S3)", "Azure", "Docker", "Git & CI/CD"],
        "process": [
            ("Discover", "A short call to understand the goal, users and must-haves. You get a clear scope and estimate."),
            ("Design the system", "Data model, API plan and screens agreed before code, so there are no surprises."),
            ("Build in sprints", "Working software every week or two, with demos, code on GitHub and async updates."),
            ("Launch & support", "Deployment on AWS or your host, handover docs and support after launch."),
        ],
        "projects": ["uxl-pos-point-of-sale", "promis-product-management-system", "dts-gilgit-baltistan-tourism-portal", "ims-ai-enterprise-platform"],
        "faq": [
            ("How much experience do you have as a full-stack developer?", "Over 3 years of professional full-stack work: at uExel Foundation (DTS, PROMIS, IMS and UXL POS), at ValourAI for an international client, and at Execudea. I hold a B.S. in Computer Science from SZABIST University, Islamabad."),
            ("Which stack do you use?", "Mainly React and TypeScript on the front end, Node.js with NestJS or Express on the back end, MongoDB or MySQL for data, and AWS for hosting. I pick what fits the project rather than forcing one stack."),
            ("Do you work remotely with clients outside Pakistan?", "Yes. I have worked remotely with an international client across time zones, using code reviews, async standups and agile sprints. I'm available for remote, freelance and full-time roles."),
            ("Can you take over or improve an existing app?", "Yes. I regularly debug, refactor and speed up existing React and Node.js codebases, fix cross-browser issues and harden security."),
            ("Can you also add AI features?", f"Yes. I'm also an AI engineer and can add AI agents, chatbots or AI data processing to the same product. See <a href=\"/ai-agent-development/\">AI agent development</a>."),
            ("How do I start?", f"Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or message me on <a href=\"{WHATSAPP}\">WhatsApp</a> with a short description of what you need, and I'll reply with next steps."),
        ],
        "service_type": "Full-stack web development",
    },
    {
        "slug": "ai-agent-development",
        "nav": "AI Agents",
        "name": "AI Agent & Chatbot Development",
        "title": "AI Engineer for AI Agents, RAG & Chatbots in Pakistan | Shams Ullah Baig",
        "desc": "Shams Ullah Baig is an AI engineer in Islamabad, Pakistan who builds LLM apps, RAG systems (LangChain, LlamaIndex, OpenAI, Claude) and AI agents and chatbots trained on your documents to answer customers, qualify leads and book appointments, and adds AI automation to business software.",
        "eyebrow": "Service · AI Engineer",
        "h1": "AI Agents & Chatbots for Your Business",
        "lead": "I'm an AI engineer who builds AI agents trained on your own documents. They answer customers, qualify leads and book appointments 24/7, and they plug into the software you already run.",
        "offer_title": "What I build",
        "offer": [
            ("Customer-service AI agents", "Agents that answer questions about your services, prices, hours and policies, trained on your own documents."),
            ("Lead qualification & booking", "Agents that screen prospects and book appointments directly into your calendar, like Agentra."),
            ("AI chatbots for websites", "On-brand chat widgets that hand off to a human when needed."),
            ("RAG systems & document Q&A", "Retrieval-augmented generation with LangChain or LlamaIndex over vector databases (Pinecone, FAISS, Chroma), so answers come from your own data."),
            ("AI data processing", "Turning documents, forms and messages into structured data, which cut manual entry by about 30% on IMS."),
            ("AI inside your product", "LLM features added to an existing React/Node.js app: search, summaries, drafting and automation."),
            ("Workflow automation", "Connecting AI to your CRM, calendar, email and internal tools."),
        ],
        "stack": ["OpenAI", "Claude", "LangChain", "LlamaIndex", "RAG", "Pinecone", "FAISS", "Chroma", "AI Agents", "Prompt Engineering", "Python", "Node.js", "NestJS", "Next.js", "React", "TypeScript", "AWS", "Azure", "Docker"],
        "process": [
            ("Map the conversations", "We list the questions and tasks the agent should handle, and when it should hand over to a person."),
            ("Load your knowledge", "Your documents (price lists, hours, policies, FAQs) become the agent's source of truth."),
            ("Build & connect", "The agent is built and connected to your website, calendar and tools, then tested on real questions."),
            ("Launch & improve", "Go live, review conversations and keep improving answers over time."),
        ],
        "projects": ["agentra-ai-agents", "ims-ai-enterprise-platform", "evraah-ev-charger-locator"],
        "faq": [
            ("What does an AI engineer like you actually build?", "AI agents and chatbots that work on top of large language models, trained on a business's own information, plus the full-stack software around them: the chat interface, the API, integrations with calendars and CRMs, and deployment."),
            ("Do you build RAG systems with LangChain or LlamaIndex?", "Yes. I build retrieval-augmented generation (RAG) pipelines with LangChain or LlamaIndex, store embeddings in vector databases such as Pinecone, FAISS or Chroma, and use OpenAI or Claude models, so the AI answers from your own documents."),
            ("Can the AI agent book appointments?", "Yes. On Agentra by Valour AI, agents check availability and book appointments directly into the business's calendar, alongside answering questions and capturing leads."),
            ("Will the agent make things up?", "The agent is grounded in your own documents and set up to say it doesn't know, or hand off to a person, when a question is outside that material."),
            ("Can you add AI to software we already have?", "Yes. As a full-stack developer I can add AI features to an existing React/Node.js or NestJS application, for example AI data processing like the IMS platform, where it reduced manual entry by about 30%."),
            ("Do you work with clients outside Pakistan?", "Yes. I work remotely across time zones and am open to freelance, contract and full-time roles."),
            ("How do I start an AI project with you?", f"Email <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or message me on <a href=\"{WHATSAPP}\">WhatsApp</a> describing what you want the agent to do, and I'll suggest the simplest setup that works."),
        ],
        "service_type": "AI agent and chatbot development",
    },
]

PROJ = {p["slug"]: p for p in PROJECTS}


# --------------------------------------------------------------------------------------
# HTML helpers
# --------------------------------------------------------------------------------------
def head(title, desc, path, image, ld):
    url = f"{SITE}{path}"
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)}</title>
<meta name="description" content="{escape(desc)}">
<meta name="author" content="Shams Ullah Baig">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="theme-color" content="#03070d">
<link rel="canonical" href="{url}">
<meta property="og:type" content="article">
<meta property="og:site_name" content="Shams Ullah Baig">
<meta property="og:title" content="{escape(title)}">
<meta property="og:description" content="{escape(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{escape(title)}">
<meta name="twitter:description" content="{escape(desc)}">
<meta name="twitter:image" content="{image}">
<link rel="icon" href="/favicon.ico?v=3" sizes="48x48">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon-32.png?v=3">
<link rel="icon" type="image/png" sizes="192x192" href="/assets/icon-192.png?v=3">
<link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png?v=3">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Montserrat:wght@400;500;600;700&family=Oswald:wght@500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css?v=3">
<script type="application/ld+json">
{json.dumps(ld, indent=2, ensure_ascii=False)}
</script>
</head>
<body>
"""


def topbar(active=""):
    def link(href, label, key):
        cls = ' class="active"' if key == active else ""
        return f'<li><a href="{href}"{cls}>{label}</a></li>'
    return f"""<header class="topbar">
  <div class="topbar-in">
    <a class="brand" href="/"><img src="/assets/logo.png?v=2" alt="Shams Ullah Baig" width="36" height="36"><span>Shams Ullah Baig</span></a>
    <ul class="topnav">
      {link("/about/", "About", "about")}
      {link("/#projects", "Projects", "projects")}
      {link("/hire-full-stack-developer/", "Full-Stack", "hire-full-stack-developer")}
      {link("/ai-agent-development/", "AI Agents", "ai-agent-development")}
      {link("/#contact", "Contact", "contact")}
    </ul>
  </div>
</header>
"""


def footer():
    projects = "".join(f'<li><a href="/projects/{p["slug"]}/">{escape(p["short"])}</a></li>' for p in PROJECTS)
    return f"""<footer>
  <div class="foot">
    <div>
      <h2>Shams Ullah Baig</h2>
      <p>Full-Stack Developer &amp; AI Engineer in Islamabad, Pakistan. Available for remote, freelance and full-time work.</p>
    </div>
    <div>
      <h2>Services</h2>
      <ul>
        <li><a href="/hire-full-stack-developer/">Hire a full-stack developer</a></li>
        <li><a href="/ai-agent-development/">AI agents &amp; chatbots</a></li>
        <li><a href="/about/">About Shams Ullah Baig</a></li>
      </ul>
    </div>
    <div>
      <h2>Projects</h2>
      <ul>{projects}</ul>
    </div>
    <div>
      <h2>Contact</h2>
      <ul>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp +92 317 929 2371</a></li>
        <li><a href="{LINKEDIN}" target="_blank" rel="noopener">LinkedIn</a></li>
        <li><a href="{GITHUB}" target="_blank" rel="noopener">GitHub</a></li>
        <li><a href="{X_URL}" target="_blank" rel="noopener">X (Twitter)</a></li>
      </ul>
    </div>
  </div>
  <p class="copy">© SHAMS ULLAH BAIG · FULL-STACK DEVELOPER &amp; AI ENGINEER · ISLAMABAD</p>
</footer>
<script src="/assets/mail.js?v=1" defer></script>
</body>
</html>
"""


def crumbs(items):
    parts = []
    for i, (label, href) in enumerate(items):
        if href and i < len(items) - 1:
            parts.append(f'<a href="{href}">{escape(label)}</a>')
        else:
            parts.append(f'<span aria-current="page" style="margin:0;opacity:1">{escape(label)}</span>')
    return '<nav class="crumbs" aria-label="Breadcrumb">' + '<span>/</span>'.join(parts) + "</nav>"


def breadcrumb_ld(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": label, "item": f"{SITE}{href}"}
            for i, (label, href) in enumerate(items)
        ],
    }


def thumb(p):
    if p["shot"]:
        return f'<img loading="lazy" decoding="async" src="/assets/shots/{p["shot"]}.webp" alt="{escape(p["name"])} screenshot" width="1280" height="860">'
    return escape(p["short"])


def card(p):
    return (f'<a class="card" href="/projects/{p["slug"]}/" style="--c1:{p["c"][0]};--c2:{p["c"][1]}">'
            f'<div class="thumb">{thumb(p)}</div>'
            f'<div class="body"><strong>{escape(p["name"])}</strong><small>{escape(p["kind"])}</small></div></a>')


def ul(items):
    return "<ul>" + "".join(f"<li>{escape(i)}</li>" for i in items) + "</ul>"


def write(path, html):
    full = os.path.join(ROOT, path.strip("/").replace("/", os.sep), "index.html")
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)
    return path


# --------------------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------------------
def project_page(p):
    path = f"/projects/{p['slug']}/"
    image = f"{SITE}/assets/shots/{p['shot']}.jpg" if p["shot"] else f"{SITE}/assets/og.jpg"
    trail = [("Home", "/"), ("Projects", "/#projects"), (p["name"], path)]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "CreativeWork",
                "@id": f"{SITE}{path}#work",
                "name": p["name"],
                "headline": p["title"],
                "description": p["desc"],
                "url": f"{SITE}{path}",
                "image": image,
                "genre": p["kind"],
                "keywords": ", ".join(p["stack"]),
                "creator": {"@id": PERSON_ID, "@type": "Person", "name": "Shams Ullah Baig", "url": f"{SITE}/"},
                "sameAs": p["url"],
                "dateModified": TODAY,
            },
            breadcrumb_ld(trail),
        ],
    }
    others = [q for q in PROJECTS if q["slug"] != p["slug"]][:3]
    service = "ai-agent-development" if p["tag"] in ("AI", "AI + ERP") else "hire-full-stack-developer"
    service_label = "AI agent development" if service == "ai-agent-development" else "full-stack development"
    shot = (f'<img fetchpriority="high" src="/assets/shots/{p["shot"]}.webp" alt="Screenshot of {escape(p["name"])}, a {escape(p["kind"])} by Shams Ullah Baig" width="1280" height="860">'
            if p["shot"] else f'<div class="ph">{escape(p["short"])}</div>')
    body = f"""{topbar("projects")}
<main>
  {crumbs(trail)}
  <section class="hero">
    <span class="eyebrow">{escape(p["tag"])} · Case study</span>
    <h1 class="title-font metal">{escape(p["name"])}</h1>
    <p class="lead">{escape(p["lead"])}</p>
    <div class="cta-row">
      <a class="btn primary" href="{p["url"]}" target="_blank" rel="noopener">Visit live site ↗</a>
      <a class="btn ghost" href="/#contact">Hire me for a similar project</a>
    </div>
  </section>

  <div class="shot" style="--c1:{p["c"][0]};--c2:{p["c"][1]}">{shot}</div>

  <div class="grid">
    <article class="content">
      <h2>Overview</h2>
      {"".join(f"<p>{escape(x)}</p>" for x in p["overview"])}
      <h2>What I built</h2>
      {ul(p["built"])}
      <h2>Key features</h2>
      {ul(p["features"])}
      <h2>Results</h2>
      {ul(p["results"])}
      <p>Need something like this? See my <a href="/{service}/">{service_label}</a> service, or <a href="/#contact">get in touch</a>.</p>
    </article>
    <aside class="side">
      <div class="box">
        <h2>Project facts</h2>
        <dl class="facts">
          <div><dt>Client</dt><dd>{escape(p["client"])}</dd></div>
          <div><dt>My role</dt><dd>{escape(p["role"])}</dd></div>
          <div><dt>Industry</dt><dd>{escape(p["industry"])}</dd></div>
          <div><dt>Type</dt><dd>{escape(p["kind"])}</dd></div>
        </dl>
      </div>
      <div class="box">
        <h2>Tech stack</h2>
        <div class="chips">{"".join(f"<span>{escape(t)}</span>" for t in p["stack"])}</div>
      </div>
      <div class="box">
        <h2>Work with me</h2>
        <p>Full-Stack Developer &amp; AI Engineer, available remotely.</p>
        <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
      </div>
    </aside>
  </div>

  <section class="content" style="margin-top:46px">
    <h2>More projects</h2>
    <div class="cards">{"".join(card(q) for q in others)}</div>
    <p><a href="/#projects">See all projects →</a></p>
  </section>
</main>
"""
    return write(path, head(f"{p['title']}", p["desc"], path, image, ld) + body + footer())


def service_page(s):
    path = f"/{s['slug']}/"
    trail = [("Home", "/"), (s["name"], path)]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Service",
                "@id": f"{SITE}{path}#service",
                "name": s["name"],
                "serviceType": s["service_type"],
                "description": s["desc"],
                "url": f"{SITE}{path}",
                "provider": {"@id": PERSON_ID, "@type": "Person", "name": "Shams Ullah Baig", "url": f"{SITE}/",
                             "jobTitle": ["Full-Stack Developer", "AI Engineer"]},
                "areaServed": [{"@type": "Country", "name": "Pakistan"}, {"@type": "Place", "name": "Worldwide (remote)"}],
                "availableChannel": {"@type": "ServiceChannel", "serviceUrl": f"{SITE}/#contact"},
            },
            {"@type": "WebPage", "@id": f"{SITE}{path}#page", "url": f"{SITE}{path}", "name": s["title"],
             "dateModified": TODAY, "about": {"@id": f"{SITE}{path}#service"}, "isPartOf": {"@id": f"{SITE}/#website"}},
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q,
                     "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                    for q, a in s["faq"]
                ],
            },
            breadcrumb_ld(trail),
        ],
    }
    offers = "".join(
        f'<div class="step offer"><strong>{escape(t)}</strong><span>{escape(d)}</span></div>'
        for t, d in s["offer"])
    steps = "".join(f'<div class="step"><strong>{escape(t)}</strong><span>{escape(d)}</span></div>' for t, d in s["process"])
    faqs = "".join(
        f'<details class="faq"{" open" if i == 0 else ""}><summary><h3>{escape(q)}</h3></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(s["faq"]))
    body = f"""{topbar(s["slug"])}
<main>
  {crumbs(trail)}
  <section class="hero">
    <span class="eyebrow">{escape(s["eyebrow"])}</span>
    <h1 class="title-font metal">{escape(s["h1"])}</h1>
    <p class="lead">{escape(s["lead"])}</p>
    <div class="cta-row">
      <a class="btn primary" href="mailto:{EMAIL}">Start a project</a>
      <a class="btn ghost" href="{WHATSAPP}" target="_blank" rel="noopener">WhatsApp me</a>
      <a class="btn ghost" href="/assets/Shams_Ullah_Baig_CV.pdf" download>Download CV</a>
    </div>
  </section>

  <div class="grid">
    <article class="content">
      <h2>{escape(s["offer_title"])}</h2>
      <div class="steps">{offers}</div>
      <h2>How we'll work</h2>
      <div class="steps">{steps}</div>
      <h2>Projects I've delivered</h2>
      <div class="cards">{"".join(card(PROJ[x]) for x in s["projects"])}</div>
      <h2>Frequently asked questions</h2>
      {faqs}
    </article>
    <aside class="side">
      <div class="box">
        <h2>Tech I use</h2>
        <div class="chips">{"".join(f"<span>{escape(t)}</span>" for t in s["stack"])}</div>
      </div>
      <div class="box">
        <h2>At a glance</h2>
        <dl class="facts">
          <div><dt>Experience</dt><dd>3+ years</dd></div>
          <div><dt>Live platforms</dt><dd>7</dd></div>
          <div><dt>Based in</dt><dd>Islamabad, PK</dd></div>
          <div><dt>Work</dt><dd>Remote · Freelance · Full-time</dd></div>
        </dl>
      </div>
      <div class="box">
        <h2>Talk to me</h2>
        <p>Tell me what you want to build and I'll reply with next steps.</p>
        <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
      </div>
    </aside>
  </div>

  <section class="band">
    <h2 class="title-font metal">Let's build it</h2>
    <p>Full-Stack Developer &amp; AI Engineer · Islamabad, Pakistan · Remote worldwide</p>
    <div class="cta-row">
      <a class="btn primary" href="mailto:{EMAIL}">{EMAIL}</a>
      <a class="btn ghost" href="/">View portfolio</a>
    </div>
  </section>
</main>
"""
    return write(path, head(s["title"], s["desc"], path, f"{SITE}/assets/og.jpg", ld) + body + footer())


ABOUT_FAQ = [
    ("Who is Shams Ullah Baig?",
     "Shams Ullah Baig is a Full-Stack Developer and AI Engineer based in Islamabad, Pakistan. He has 3+ years of experience building web applications with React, Node.js and NestJS, and AI agents, chatbots and RAG systems with LangChain, OpenAI and Claude."),
    ("Where does Shams Ullah Baig work?",
     "He works as a Web Developer at uExel Foundation in Islamabad, building the DTS, PROMIS, IMS and UXL POS platforms. Before that he was a Full-Stack Developer at ValourAI, working remotely for an international client, and a Front-End Developer at Execudea in Rawalpindi."),
    ("What does Shams Ullah Baig do?",
     "He builds complete web applications, from database and REST API to React front end and AWS deployment, and adds AI features on top: AI agents that answer customers and book appointments, chatbots trained on a company's documents, and AI data processing."),
    ("Where did Shams Ullah Baig study?",
     "He holds a B.S. in Computer Science from SZABIST University, Islamabad (2021 to 2025)."),
    ("Is Shams Ullah Baig available for hire?",
     f"Yes. He is open to remote, freelance and full-time work. Contact him at <a href=\"mailto:{EMAIL}\">{EMAIL}</a> or on <a href=\"{WHATSAPP}\">WhatsApp</a>."),
]

EXPERIENCE = [
    ("Web Developer", "uExel Foundation", "Islamabad, Pakistan", "Jun 2025 to present",
     "React and NestJS features across four live platforms (DTS, PROMIS, IMS, UXL POS), payment-gateway integration and AWS deployment."),
    ("Full-Stack Developer", "ValourAI", "Remote, international client", "Mar 2022 to Jan 2025",
     "Automated trading platform from database design to deployed REST API, NestJS/Node.js API optimisation, and work on the Agentra AI agents product."),
    ("Front-End Developer", "Execudea", "Rawalpindi, Pakistan", "Sep 2021 to Feb 2022",
     "Responsive UI components with HTML, CSS and JavaScript, and cross-browser bug fixing."),
]


def about_page():
    path = "/about/"
    trail = [("Home", "/"), ("About", path)]
    ld = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "ProfilePage",
                "@id": f"{SITE}{path}#page",
                "url": f"{SITE}{path}",
                "name": "About Shams Ullah Baig",
                "dateModified": TODAY,
                "mainEntity": {"@id": PERSON_ID},
                "isPartOf": {"@id": f"{SITE}/#website"},
            },
            {
                "@type": "Person",
                "@id": PERSON_ID,
                "name": "Shams Ullah Baig",
                "url": f"{SITE}/",
                "image": f"{SITE}/assets/shams.jpg",
                "jobTitle": ["Full-Stack Developer", "AI Engineer"],
                "worksFor": {"@type": "Organization", "name": "uExel Foundation"},
                "alumniOf": {"@type": "CollegeOrUniversity", "name": "SZABIST University, Islamabad"},
                "address": {"@type": "PostalAddress", "addressLocality": "Islamabad", "addressCountry": "PK"},
                "knowsLanguage": ["English", "Urdu", "Shina"],
                "sameAs": [GITHUB, LINKEDIN, X_URL],
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
                    for q, a in ABOUT_FAQ
                ],
            },
            breadcrumb_ld(trail),
        ],
    }
    jobs = "".join(
        f'<div class="step offer"><strong>{escape(t)}, {escape(c)}</strong>'
        f'<span>{escape(when)} · {escape(where)}<br>{escape(d)}</span></div>'
        for t, c, where, when, d in EXPERIENCE)
    faqs = "".join(
        f'<details class="faq"{" open" if i == 0 else ""}><summary><h3>{escape(q)}</h3></summary><p>{a}</p></details>'
        for i, (q, a) in enumerate(ABOUT_FAQ))
    body = f"""{topbar("about")}
<main>
  {crumbs(trail)}
  <section class="hero">
    <span class="eyebrow">About</span>
    <h1 class="title-font metal">Who is Shams Ullah Baig?</h1>
    <p class="lead"><strong>Shams Ullah Baig is a Full-Stack Developer and AI Engineer in Islamabad, Pakistan.</strong> He has 3+ years of experience building web applications with React, Node.js and NestJS, and AI agents, chatbots and RAG systems with LangChain, OpenAI and Claude. He works at uExel Foundation and is available for remote, freelance and full-time work.</p>
    <div class="cta-row">
      <a class="btn primary" href="mailto:{EMAIL}">Email me</a>
      <a class="btn ghost" href="/assets/Shams_Ullah_Baig_CV.pdf" download>Download CV</a>
      <a class="btn ghost" href="/#projects">See projects</a>
    </div>
  </section>

  <div class="grid">
    <article class="content">
      <h2>What I do</h2>
      <p>I build complete web applications end to end: database design, REST APIs with authentication, responsive React and Next.js front ends, payment-gateway integration and deployment on AWS. On top of that I build the AI layer: AI agents that answer customers and book appointments, chatbots trained on a company's own documents, and AI data processing inside business systems.</p>
      <p>My work has gone into government, healthcare, fintech, retail and tourism products, including a Gilgit-Baltistan government tourism portal, a diagnostics platform, a multi-tenant point-of-sale system and the Agentra AI agents platform.</p>

      <h2>Experience</h2>
      <div class="steps">{jobs}</div>

      <h2>Skills</h2>
      <ul>
        <li><strong>Front end:</strong> React, Next.js, TypeScript, JavaScript, HTML, CSS</li>
        <li><strong>Back end:</strong> Node.js, NestJS, Express, REST APIs, JWT authentication, payment gateways</li>
        <li><strong>AI / LLM:</strong> OpenAI, Claude, LangChain, LlamaIndex, RAG, vector databases (Pinecone, FAISS, Chroma), AI agents, chatbots</li>
        <li><strong>Databases:</strong> MongoDB, PostgreSQL, MySQL</li>
        <li><strong>Cloud and tools:</strong> AWS (EC2, S3), Azure, Docker, Git, GitHub, CI/CD</li>
      </ul>

      <h2>Education</h2>
      <p>B.S. Computer Science, SZABIST University, Islamabad (2021 to 2025).</p>

      <h2>Selected projects</h2>
      <div class="cards">{"".join(card(p) for p in PROJECTS[:6])}</div>

      <h2>Questions about Shams Ullah Baig</h2>
      {faqs}
    </article>
    <aside class="side">
      <div class="box">
        <h2>Quick facts</h2>
        <dl class="facts">
          <div><dt>Name</dt><dd>Shams Ullah Baig</dd></div>
          <div><dt>Role</dt><dd>Full-Stack Developer &amp; AI Engineer</dd></div>
          <div><dt>Location</dt><dd>Islamabad, Pakistan</dd></div>
          <div><dt>Experience</dt><dd>3+ years</dd></div>
          <div><dt>Current job</dt><dd>uExel Foundation</dd></div>
          <div><dt>Education</dt><dd>B.S. CS, SZABIST</dd></div>
          <div><dt>Languages</dt><dd>English, Urdu, Shina</dd></div>
          <div><dt>Work type</dt><dd>Remote · Freelance · Full-time</dd></div>
        </dl>
      </div>
      <div class="box">
        <h2>Find me online</h2>
        <div class="chips">
          <a href="{GITHUB}" target="_blank" rel="noopener me"><span>GitHub</span></a>
          <a href="{LINKEDIN}" target="_blank" rel="noopener me"><span>LinkedIn</span></a>
          <a href="{X_URL}" target="_blank" rel="noopener me"><span>X</span></a>
        </div>
      </div>
      <div class="box">
        <h2>Services</h2>
        <p><a href="/hire-full-stack-developer/">Hire a full-stack developer</a><br><a href="/ai-agent-development/">AI agents &amp; chatbots</a></p>
      </div>
    </aside>
  </div>
</main>
"""
    title = "About Shams Ullah Baig | Full-Stack Developer & AI Engineer, Islamabad"
    desc = ("Who is Shams Ullah Baig? A Full-Stack Developer and AI Engineer in Islamabad, Pakistan with 3+ years "
            "building React, Node.js and NestJS apps and AI agents, chatbots and RAG systems.")
    return write(path, head(title, desc, path, f"{SITE}/assets/og.jpg", ld) + body + footer())


def homepage_faq():
    import re
    with open(os.path.join(ROOT, "index.html"), encoding="utf-8") as f:
        html = f.read()
    out = []
    for m in re.finditer(r'<details class="faq[^"]*".*?<h3[^>]*>(.*?)</h3>.*?</summary>(.*?)</details>', html, re.S):
        q = strip_tags(m.group(1)).strip()
        a = re.sub(r"\s+", " ", strip_tags(m.group(2))).strip()
        out.append((unescape(q), unescape(a)))
    return out


def llms_full():
    """Plain-text dump of the whole site for AI crawlers, kept in sync with the pages."""
    with open(os.path.join(ROOT, "llms.txt"), encoding="utf-8") as f:
        base = f.read().rstrip()
    t = lambda s: unescape(strip_tags(s))
    parts = [base, "", "---", "", "# Full content", ""]
    parts += ["## About Shams Ullah Baig", f"URL: {SITE}/about/", ""]
    for q, a in ABOUT_FAQ:
        parts += [f"### {q}", t(a), ""]
    parts += ["### Experience"]
    for ti, c, where, when, d in EXPERIENCE:
        parts.append(f"- {ti}, {c} ({where}), {when}: {d}")
    parts.append("")
    parts += ["## Frequently asked questions (homepage)", f"URL: {SITE}/#faq", ""]
    for q, a in homepage_faq():
        parts += [f"### {q}", a, ""]
    for s in SERVICES:
        parts += [f"## Service: {s['name']}", f"URL: {SITE}/{s['slug']}/", "", s["lead"], "",
                  f"### {s['offer_title']}"]
        parts += [f"- {a}: {b}" for a, b in s["offer"]]
        parts += ["", "### How we'll work"] + [f"- {a}: {b}" for a, b in s["process"]]
        parts += ["", f"Tech: {', '.join(s['stack'])}", "", "### FAQ"]
        for q, a in s["faq"]:
            parts += [f"Q: {q}", f"A: {t(a)}", ""]
    for p in PROJECTS:
        parts += [f"## Project: {p['name']}", f"Case study: {SITE}/projects/{p['slug']}/", f"Live site: {p['url']}",
                  f"Type: {p['kind']} · Client: {p['client']} · Role: {p['role']} · Industry: {p['industry']}",
                  f"Tech: {', '.join(p['stack'])}", "", p["lead"], ""]
        parts += p["overview"] + [""]
        parts += ["What he built:"] + [f"- {x}" for x in p["built"]]
        parts += ["Key features:"] + [f"- {x}" for x in p["features"]]
        parts += ["Results:"] + [f"- {x}" for x in p["results"]] + [""]
    parts.append(f"Last updated: {TODAY}")
    with open(os.path.join(ROOT, "llms-full.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(parts) + "\n")


def strip_tags(s):
    import re
    return re.sub(r"<[^>]+>", "", s)


def sitemap(paths):
    urls = "".join(f"  <url>\n    <loc>{SITE}{p}</loc>\n    <lastmod>{TODAY}</lastmod>\n  </url>\n" for p in ["/"] + paths)
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + urls + "</urlset>\n")


if __name__ == "__main__":
    written = [about_page()] + [project_page(p) for p in PROJECTS] + [service_page(s) for s in SERVICES]
    sitemap(written)
    llms_full()
    for w in written:
        print("wrote", w)
    print("sitemap.xml:", len(written) + 1, "URLs")
