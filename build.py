"""Genera index.html (ES) y en/index.html (EN). Ejecutar: python3 build.py"""
import json, os

SITE = "https://spacehub.barcelona"
IMG = "https://static.wixstatic.com/media/"
LOGO = IMG + "5e66d6_f48f99903a384c449490dd30f2d2d5b4~mv2.png"
HERO = IMG + "5e66d6_9e5f1ca8f7f94405ae538fa05c7bca74~mv2.jpg/v1/fill/w_1920,h_1238,al_c,q_80/coworking-spacehub-barcelona.jpg"
OG = IMG + "5e66d6_9e5f1ca8f7f94405ae538fa05c7bca74~mv2.jpg/v1/fill/w_1200,h_630,al_c,q_85/coworking-spacehub-barcelona-og.jpg"
CARDS = [
    "5e66d6_10d742c07e3d455593975238a9d6af29~mv2_d_3000_1968_s_2.jpg",
    "5e66d6_80dcfcafa7e34996b57dbda3830e3afb~mv2_d_2807_1790_s_2.jpg",
    "5e66d6_b526439ab24842328531c8693cdf7436~mv2_d_3000_1929_s_2.jpg",
]
TILES = [
    "nsplsh_6e70785857675133335a51~mv2_d_4076_2712_s_4_2.jpg",
    "5e66d6_186779c611b74ef4b12f871b95a239d5~mv2_d_2873_1860_s_2.jpg",
    "5e66d6_6db674d5a74041ac9592a3da9109857d~mv2_d_1672_1928_s_2.jpg",
]
JOIN = IMG + "5e66d6_d220c4bca1224ef88c8fc2ddc88f1aea~mv2_d_3000_2000_s_2.jpg/v1/fill/w_1300,h_700,al_c,q_80/comunidad-spacehub.jpg"
PHONE, PHONE_TXT = "+34932204140", "+34 932 204 140"
STREET, CP, CITY = "Carrer de Folgueroles, 17-25", "08022", "Barcelona"

def img(name, w, h, slug):
    return f"{IMG}{name}/v1/fill/w_{w},h_{h},al_c,q_80/{slug}.jpg"

ES = dict(
    lang="es", path="/", alt_path="/en/", alt_lang="en",
    title="Coworking en Barcelona, Sant Gervasi | Spacehub",
    desc="Coworking en Sant Gervasi, Barcelona: mesas flexibles, salas de reuniones y sala de eventos. Acceso 24/7, internet de alta velocidad y café incluido.",
    og_title="Spacehub — Coworking en Sant Gervasi, Barcelona",
    nav=["Inicio", "Espacios", "Servicios", "Contacto"], contact_cta="Contacto", menu="Menú",
    eyebrow="Coworking en Sant Gervasi · Barcelona", h1="Bienvenido a Spacehub",
    hero_p="Un nuevo tipo de espacio para emprendedores, startups y freelancers: una comunidad basada en el networking, la innovación y la diversión.",
    hero_alt="Zona de trabajo del coworking Spacehub en Sant Gervasi, Barcelona",
    cta="Quiero mi espacio",
    safe_h="Seguro y flexible",
    safe_lead="Si buscas un espacio de trabajo flexible, dinámico y saludable, preparado para la nueva era del trabajo híbrido entre casa y oficina, Spacehub es tu solución.",
    safe_p="En Spacehub, la salud y la seguridad de nuestros miembros y empleados es nuestra prioridad: aquí encontrarás un espacio sano y seguro. Gracias a las dimensiones de nuestras instalaciones, mientras un coworking u oficina habitual tiene una ratio de 5 m² por persona, nosotros tenemos 15 m² por persona.",
    spaces_h="Nuestros espacios",
    cards=[
        ("Mesas de coworking", "Puestos de trabajo en el coworking Spacehub de Barcelona",
         "Nuestras opciones de espacio de trabajo se adaptan a todas tus necesidades profesionales. Una gran opción para freelancers y startups con horarios flexibles que buscan un espacio asequible. Las mesas de coworking incluyen internet de alta velocidad, servicio de impresión y mucho más."),
        ("Sala de eventos y comedor", "Sala de eventos y comedor de Spacehub Barcelona",
         "El verdadero corazón de Spacehub: nuestro auditorio y comedor. Sirve tanto para el evento más interesante de la ciudad como para tomar algo con tus compañeros. Cuenta con 2 proyectores SONY de gran formato, 2 baños, una micrococina con cerveza fresca y sistema de sonido multimedia Dolby Surround®."),
        ("Salas de reuniones", "Sala de reuniones en el coworking Spacehub, Sant Gervasi",
         "En Spacehub se respira emprendimiento, y nuestras salas de reuniones son el lugar perfecto para contagiarte. Como todos nuestros espacios, incluyen todas las ventajas y servicios de las instalaciones. Únete a una comunidad enérgica y encuentra un hogar para ti y tu negocio."),
    ],
    am_h="Servicios e instalaciones",
    am_p="En Spacehub sabemos lo que cuesta poner en marcha un negocio. Por eso hemos creado un coworking de primer nivel donde puedes centrarte en tu próximo gran proyecto. Del café gratis a internet de alta velocidad: hemos pensado en todo lo que puedas necesitar. Llámanos si tienes cualquier pregunta.",
    tiles=[
        ("Internet de máxima velocidad y servicios para empresas digitales", "Persona trabajando con portátil en Spacehub"),
        ("Acceso 24/7 con Akiles® y servicio de office manager", "Pasillo y zona común del coworking Spacehub"),
        ("Agua purificada, café recién molido y la mejor cerveza artesana con Beerbox®", "Barra con grifo de cerveza en Spacehub Barcelona"),
    ],
    join_h="¡ÚNETE AL HUB!", join_alt="Comunidad de emprendedores reunida en Spacehub",
    visit_h="Visítanos en Sant Gervasi",
    visit_p="Estamos en el barrio de Sarrià-Sant Gervasi, en la parte alta de Barcelona.",
    call="Llamar ahora", maps="Cómo llegar",
    faq_h="Preguntas frecuentes",
    faq=[
        ("¿Dónde está el coworking Spacehub?", f"En {STREET}, {CP} {CITY}, en el distrito de Sarrià-Sant Gervasi."),
        ("¿Qué incluye una mesa de coworking?", "Internet de alta velocidad, servicio de impresión, acceso a las zonas comunes, café, agua purificada y cerveza artesana."),
        ("¿Puedo acceder al coworking a cualquier hora?", "Sí. El edificio tiene acceso 24/7 mediante el sistema Akiles® y contamos con servicio de office manager."),
        ("¿Tenéis salas de reuniones y espacio para eventos?", "Sí. Tenemos salas de reuniones y una sala de eventos y comedor con 2 proyectores SONY de gran formato y sonido Dolby Surround®."),
        ("¿Cómo reservo mi espacio?", f"Llámanos al {PHONE_TXT} y te enseñamos el espacio y las opciones disponibles."),
    ],
    copy="Hecho en la preciosa ciudad de Barcelona.",
)

EN = dict(
    lang="en", path="/en/", alt_path="/", alt_lang="es",
    title="Coworking Space in Barcelona, Sant Gervasi | Spacehub",
    desc="Coworking in Sarrià-Sant Gervasi, Barcelona: flexible desks, meeting rooms and an events room. 24/7 access, high-speed internet, coffee and craft beer. Call us.",
    og_title="Spacehub — Coworking in Sant Gervasi, Barcelona",
    nav=["Home", "Workspaces", "Amenities", "Contact"], contact_cta="Get In Touch", menu="Menu",
    eyebrow="Coworking in Sant Gervasi · Barcelona", h1="Welcome to Spacehub",
    hero_p="A new kind of space for entrepreneurs, startups, and freelancers to form a community based on networking, innovation and fun.",
    hero_alt="Workspace at Spacehub coworking in Sant Gervasi, Barcelona",
    cta="Get my space now",
    safe_h="Safe & Flexible",
    safe_lead="If you're looking for a flexible, dynamic and healthy workspace prepared for the new era of mixed home-office/face-to-face work, then Spacehub is your solution.",
    safe_p="At Spacehub, the health and safety of our members and employees is our top priority: here you'll find a healthy and secure space. Thanks to the size of our facilities, where a coworking or common office has a ratio of 5 sqm per person, we have 15 sqm per person.",
    spaces_h="Our Spaces",
    cards=[
        ("Working Desks", "Coworking desks at Spacehub Barcelona",
         "At Spacehub, our custom workspace options can be adapted to all your professional needs. This is a great option for freelancers and startups with flexible schedules that are looking for an affordable space to work in. Not to mention our Coworking Desks come with high-speed internet, printing services and more."),
        ("Dining & Events Room", "Dining and events room at Spacehub Barcelona",
         "The real core of the Spacehub: our auditorium & dining room. Whether it's for the coolest event in town or for a drink with your hubmates, it fits them all. It incorporates 2 large format SONY projectors, 2 toilets, a microkitchen with fresh beer and our Dolby Surround® multimedia sound system."),
        ("Meeting Rooms", "Meeting room at Spacehub coworking, Sant Gervasi",
         "Entrepreneurship is in the air at Spacehub, and our Meeting Rooms make the perfect places for this vibe to rub off on you. As with all of our workspaces, this option comes with our full range of benefits and facility amenities. Join our energetic and vibrant community and find a home for you and your business."),
    ],
    am_h="Amenities & Facilities",
    am_p="At Spacehub, we know what it takes to get a business off the ground. That’s why we built a state-of-the-art Coworking Space, where you can focus on your next big project. From free coffee to high-speed internet - we’ve thought about everything you might need. Give us a call if you have any questions.",
    tiles=[
        ("Highest speed internet in town and services for digital companies", "Person working on a laptop at Spacehub"),
        ("24/7 building access with Akiles® and office manager service", "Corridor and common area at Spacehub coworking"),
        ("Purified water, fresh blended coffee & best craft beer with Beerbox®", "Beer tap bar at Spacehub Barcelona"),
    ],
    join_h="JOIN THE HUB!", join_alt="Entrepreneurs community meeting at Spacehub",
    visit_h="Visit us in Sant Gervasi",
    visit_p="We are in the Sarrià-Sant Gervasi district, in uptown Barcelona.",
    call="Call now", maps="Get directions",
    faq_h="FAQ",
    faq=[
        ("Where is Spacehub coworking?", f"At {STREET}, {CP} {CITY}, in the Sarrià-Sant Gervasi district."),
        ("What does a coworking desk include?", "High-speed internet, printing services, access to common areas, coffee, purified water and craft beer."),
        ("Can I access the coworking at any time?", "Yes. The building has 24/7 access with the Akiles® system and an office manager service."),
        ("Do you have meeting rooms and an events space?", "Yes. We have meeting rooms and a dining & events room with 2 large format SONY projectors and Dolby Surround® sound."),
        ("How do I book my space?", f"Call us at {PHONE_TXT} and we'll show you the space and the available options."),
    ],
    copy="Made in the lovely city of Barcelona.",
)

MAPS = "https://www.google.com/maps/search/?api=1&query=Carrer+de+Folgueroles+17,+08022+Barcelona"


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def schema(t):
    url = SITE + t["path"]
    biz = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "additionalType": "https://en.wikipedia.org/wiki/Coworking",
        "@id": SITE + "/#business",
        "name": "Spacehub Barcelona",
        "alternateName": "Spacehub Coworking",
        "description": t["desc"],
        "url": url,
        "telephone": PHONE,
        "image": [OG, HERO],
        "logo": LOGO,
        "address": {"@type": "PostalAddress", "streetAddress": STREET, "postalCode": CP,
                    "addressLocality": CITY, "addressRegion": "Catalunya", "addressCountry": "ES"},
        "areaServed": ["Sarrià-Sant Gervasi", "Barcelona"],
        "openingHoursSpecification": {"@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
            "opens": "00:00", "closes": "23:59"},
        "amenityFeature": [{"@type": "LocationFeatureSpecification", "name": n, "value": True}
                           for n, _ in t["tiles"]],
        "hasMap": MAPS,
        "parentOrganization": {"@type": "Organization", "name": "Spacelab SL"},
    }
    faq = {"@context": "https://schema.org", "@type": "FAQPage",
           "mainEntity": [{"@type": "Question", "name": q,
                           "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faq"]]}
    site = {"@context": "https://schema.org", "@type": "WebSite", "name": "Spacehub Barcelona",
            "url": SITE + "/", "inLanguage": t["lang"]}
    return "\n".join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>'
                     for x in (biz, faq, site))


def page(t):
    url = SITE + t["path"]
    alt_url = SITE + t["alt_path"]
    es_url, en_url = (url, alt_url) if t["lang"] == "es" else (alt_url, url)
    css = "../styles.css" if t["lang"] == "en" else "styles.css"
    n = t["nav"]
    cards = "\n".join(f'''      <article class="card">
        <img src="{img(CARDS[i], 800, 600, 'spacehub-' + str(i+1))}" width="800" height="600" loading="lazy" decoding="async" alt="{esc(alt)}">
        <h3>{esc(h)}</h3>
        <p>{esc(p)}</p>
      </article>''' for i, (h, alt, p) in enumerate(t["cards"]))
    tiles = "\n".join(f'''      <div class="tile">
        <img src="{img(TILES[i], 800, 1000, 'spacehub-servicio-' + str(i+1))}" width="800" height="1000" loading="lazy" decoding="async" alt="{esc(alt)}">
        <h3>{esc(h)}</h3>
      </div>''' for i, (h, alt) in enumerate(t["tiles"]))
    faq = "\n".join(f'''    <details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>''' for q, a in t["faq"])
    lang_es = 'class="on" aria-current="true"' if t["lang"] == "es" else ''
    lang_en = 'class="on" aria-current="true"' if t["lang"] == "en" else ''
    return f'''<!DOCTYPE html>
<html lang="{t['lang']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t['title'])}</title>
<meta name="description" content="{esc(t['desc'])}">
<meta name="robots" content="index, follow, max-image-preview:large">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="es" href="{es_url}">
<link rel="alternate" hreflang="en" href="{en_url}">
<link rel="alternate" hreflang="x-default" href="{es_url}">
<meta name="theme-color" content="#000000">
<meta name="geo.region" content="ES-CT">
<meta name="geo.placename" content="Barcelona">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Spacehub Barcelona">
<meta property="og:locale" content="{'es_ES' if t['lang']=='es' else 'en_GB'}">
<meta property="og:title" content="{esc(t['og_title'])}">
<meta property="og:description" content="{esc(t['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{OG}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(t['og_title'])}">
<meta name="twitter:description" content="{esc(t['desc'])}">
<meta name="twitter:image" content="{OG}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{LOGO}">
<link rel="preconnect" href="https://static.wixstatic.com">
<link rel="preload" as="image" href="{HERO}" fetchpriority="high">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Libre+Franklin:wght@300;700&family=Raleway:wght@300;400;600&family=Playfair+Display&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
{schema(t)}
</head>
<body>
<a class="skip" href="#main">{'Saltar al contenido' if t['lang']=='es' else 'Skip to content'}</a>
<header id="top">
  <div class="wrap">
    <a href="{t['path']}" class="logo"><img src="{LOGO}" width="143" height="38" alt="Spacehub Barcelona — coworking"></a>
    <nav aria-label="{t['menu']}">
      <span class="lang"><a href="/" hreflang="es" lang="es" {lang_es}>ES</a> · <a href="/en/" hreflang="en" lang="en" {lang_en}>EN</a></span>
      <a href="#top">{n[0]}</a>
      <a href="#espacios">{n[1]}</a>
      <a href="#servicios">{n[2]}</a>
      <a href="#contacto">{n[3]}</a>
    </nav>
    <div class="contact-top">
      <a href="tel:{PHONE}">{PHONE_TXT}</a>
      <a href="#contacto" style="display:flex;align-items:center;gap:8px">
        <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2C8.1 2 5 5.1 5 9c0 5.2 7 13 7 13s7-7.8 7-13c0-3.9-3.1-7-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"/></svg>
        {t['contact_cta']}</a>
    </div>
    <button class="menu-btn" aria-label="{t['menu']}" onclick="this.closest('header').classList.toggle('open')">☰</button>
  </div>
</header>

<main id="main">
<section class="hero">
  <img class="hero-img" src="{HERO}" width="1920" height="1238" fetchpriority="high" alt="{esc(t['hero_alt'])}">
  <div class="wrap">
    <h1><span class="eyebrow">{esc(t['eyebrow'])}</span>{esc(t['h1'])}</h1>
    <p>{esc(t['hero_p'])}</p>
    <a href="#contacto" class="btn">{esc(t['cta'])}</a>
  </div>
</section>

<section class="safe">
  <div class="wrap">
    <h2>{esc(t['safe_h'])}</h2>
    <p class="lead">{esc(t['safe_lead'])}</p>
    <p>{esc(t['safe_p'])}</p>
  </div>
</section>

<section class="spaces" id="espacios">
  <div class="wrap">
    <h2 class="title">{esc(t['spaces_h'])}</h2>
    <div class="grid3">
{cards}
    </div>
    <div class="center"><a href="#contacto" class="btn">{esc(t['cta'])}</a></div>
  </div>
</section>

<section class="amenities" id="servicios">
  <div class="wrap">
    <h2>{esc(t['am_h'])}</h2>
    <p class="intro">{esc(t['am_p'])}</p>
    <div class="tiles">
{tiles}
    </div>
    <div class="center"><a href="#contacto" class="btn">{esc(t['cta'])}</a></div>
  </div>
</section>

<section class="faq" id="faq">
  <div class="wrap">
    <h2>{esc(t['faq_h'])}</h2>
{faq}
  </div>
</section>

<section class="join" id="contacto">
  <div class="wrap">
    <div class="join-box">
      <div class="txt"><h2>{esc(t['join_h'])}</h2></div>
      <img src="{JOIN}" width="1300" height="700" loading="lazy" decoding="async" alt="{esc(t['join_alt'])}">
    </div>
    <div class="visit">
      <h2>{esc(t['visit_h'])}</h2>
      <address class="nap"><strong>Spacehub Barcelona</strong><br>{STREET}, {CP} {CITY}<br><a href="tel:{PHONE}">{PHONE_TXT}</a></address>
      <p class="nap">{esc(t['visit_p'])}</p>
      <div class="ctas"><a class="btn" href="tel:{PHONE}">{esc(t['call'])}</a><a class="btn ghost" href="{MAPS}" target="_blank" rel="noopener">{esc(t['maps'])}</a></div>
    </div>
    <iframe class="map" loading="lazy" title="Spacehub — {STREET}, {CITY}"
      src="https://maps.google.com/maps?q=Carrer%20de%20Folgueroles%2017%2C%2008022%20Barcelona&z=16&output=embed"></iframe>
  </div>
</section>
</main>

<footer>
  <div class="wrap">
    <img src="{LOGO}" width="200" height="53" loading="lazy" alt="Spacehub Barcelona">
    <p>{STREET}, {CP} {CITY} · <a href="tel:{PHONE}">{PHONE_TXT}</a></p>
    <p class="copy">© Spacelab SL · {esc(t['copy'])}</p>
  </div>
</footer>
</body>
</html>
'''


os.makedirs("en", exist_ok=True)
open("index.html", "w").write(page(ES))
open("en/index.html", "w").write(page(EN))
print("ok")
