#!/usr/bin/env python3
"""EVelec website generator.  Edit CONFIG / content below, then run:  python3 build.py"""
from pathlib import Path
from html import escape

CONFIG = {
    "phone": "01273 983951",
    "phone_link": "+441273983951",
    "email": "info@evelec.co.uk",
    "address": "Brighton, United Kingdom",
    "company_no": "11132874",
    "facebook": "https://www.facebook.com/EVelecUK/",
    "instagram": "https://www.instagram.com/evelecltd/",
    "google": "https://maps.app.goo.gl/jSq9Tzx1LCuBsJ2LA",
    "review_count": 224,
    "form_endpoint": "",   # e.g. https://formspree.io/f/xxxx — blank opens the visitor's email app
    "site_url": "https://www.evelec.co.uk",
}
C = CONFIG
OUT = Path(__file__).parent / "site"
AREAS = ["Brighton & Hove", "Sussex", "Surrey", "Hampshire", "Kent"]

# ------------------------------------------------------------------ icons --
P = {
 "bolt": '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "charger": '<path d="M5 21V5a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v16"/><path d="M3 21h14"/><path d="M15 9h2a2 2 0 0 1 2 2v5a1.5 1.5 0 0 0 3 0V8l-3-3"/><path d="m10 7-2 4h4l-2 4"/>',
 "home": '<path d="M3 10.5 12 3l9 7.5"/><path d="M5 9.5V21h14V9.5"/><path d="M10 21v-6h4v6"/>',
 "building": '<rect x="4" y="3" width="16" height="18" rx="1"/><path d="M9 7h1M14 7h1M9 11h1M14 11h1M9 15h1M14 15h1"/><path d="M10 21v-3h4v3"/>',
 "briefcase": '<rect x="3" y="7" width="18" height="13" rx="2"/><path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2"/><path d="M3 13h18"/>',
 "sun": '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/>',
 "battery": '<rect x="2" y="7" width="17" height="10" rx="2"/><path d="M22 11v2"/><path d="m11 9-2 3h4l-2 3"/>',
 "shield": '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 "pound": '<path d="M16 7a4 4 0 0 0-7 2.5V19"/><path d="M6 19h11"/><path d="M6 13h8"/>',
 "check": '<path d="m5 12 5 5 9-10"/>',
 "phone": '<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/>',
 "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 "pin": '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
 "arrow": '<path d="M5 12h14M13 6l6 6-6 6"/>',
 "arrow-ur": '<path d="M7 17 17 7M8 7h9v9"/>',
 "chev": '<path d="m6 9 6 6 6-6"/>',
 "x": '<path d="M6 6l12 12M18 6 6 18"/>',
 "menu": '<path d="M4 7h16M4 12h16M4 17h16"/>',
 "siren": '<path d="M7 18v-6a5 5 0 0 1 10 0v6"/><path d="M5 21h14v-3H5z"/><path d="M12 3v2M4 7l1.5 1M20 7l-1.5 1"/>',
 "clipboard": '<rect x="5" y="4" width="14" height="17" rx="2"/><path d="M9 4V3h6v1"/><path d="m9 13 2 2 4-4"/>',
 "search": '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 "cable": '<path d="M4 3v6a4 4 0 0 0 4 4h8a4 4 0 0 1 4 4v4"/><path d="M2 3h4M18 21h4"/>',
 "fuse": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M7 9v6M11 9v6M15 9v6"/>',
 "leaf": '<path d="M5 19c0-9 6-14 15-14 0 9-5 15-14 15"/><path d="M5 19c3-4 6-6 9-8"/>',
 "tree": '<path d="M12 22v-6"/><path d="M12 16c-4 0-6-3-6-6a6 6 0 0 1 12 0c0 3-2 6-6 6z"/>',
 "socket": '<rect x="4" y="4" width="16" height="16" rx="3"/><path d="M10 9v3M14 9v3M10 16h4"/>',
 "bulb": '<path d="M9 18h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2.1h5c0-.9.4-1.6 1-2.1A6 6 0 0 0 12 3z"/>',
 "dial": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="4.5"/><path d="M12 3v2"/>',
 "plug": '<path d="M9 2v5M15 2v5"/><path d="M6 7h12v4a6 6 0 0 1-12 0z"/><path d="M12 17v5"/>',
 "doc": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 13h6M9 17h6"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0"/><path d="M16 4.5a3.5 3.5 0 0 1 0 7M18 13.5a7 7 0 0 1 4 6.5"/>',
 "car": '<path d="M5 17h14v-5l-2-5H7l-2 5z"/><path d="M3 12h18"/><circle cx="7.5" cy="17" r="2"/><circle cx="16.5" cy="17" r="2"/>',
 "calendar": '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
 "layers": '<path d="m12 3 9 5-9 5-9-5z"/><path d="m3 13 9 5 9-5"/>',
 "drop": '<path d="M12 3s6 6.5 6 11a6 6 0 0 1-12 0c0-4.5 6-11 6-11z"/>',
 "fb": '<path d="M14 8h3V4h-3a4 4 0 0 0-4 4v3H7v4h3v7h4v-7h3l1-4h-4V8z"/>',
 "ig": '<rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><path d="M17.5 6.5h.01"/>',
 "play": '<path d="M7 4v16l13-8z"/>',
 "star": '<path d="m12 3 2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1-4.4-4.3 6.1-.9z"/>',
}
GOOGLE = '<svg viewBox="0 0 48 48" aria-hidden="true"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3.1 0 5.8 1.2 7.9 3.1l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2c-2 1.5-4.5 2.4-7.2 2.4-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>'

def ic(n, cls="icon"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{P[n]}</svg>'

def checks(items, dark=False):
    return '<ul class="checks">' + "".join(f'<li><span class="ck">{ic("check")}</span><span>{i}</span></li>' for i in items) + "</ul>"

def vid(name, poster=None, cls="", inview=True):
    poster = poster or name
    return (f'<video class="{cls}" muted loop playsinline preload="none" poster="assets/img/{poster}.jpg" '
            f'data-src="assets/video/{name}.mp4" data-inview aria-hidden="true"></video>')

# ---------------------------------------------------------------- reviews --
REVIEWS = [
 ("Craig H.", "Ohme ePod", "Tom did a great job of installing our new Ohme ePod EV charger. He arrived promptly at the arranged appointment time and talked us through the installation and how he intended to run the cabling from our house to our carport, some 30 metres away. He was very polite and professional and made everything look very neat and tidy."),
 ("Roger B.", "Solar & battery", "Chris, Mark and team have just completed my solar and battery install. As always they are professional, polite and very tidy. This is my 4th project with them since 2023, and I am very happy to recommend them."),
 ("Michael F.", "Hypervolt 3 Pro", "Just had a Hypervolt 3 Pro installed and the service was fantastic, they arrived when they said they would, got the job done to a very high standard, no mess, managed to come up with a solution to reduce the cable required and adjusted the bill, can't rate them highly enough."),
 ("Mark", "zappi", "From the initial discussions and clear advice through to the competitive quote and the thoroughly professional installation of my Zappi car charger, I've been extremely impressed with EVelec. The whole process was smooth, efficient, and carried out to a very high standard. Highly recommended."),
 ("Alison F.", "EV charger", "Great service, great price. Had 3 different quotes to fit a EV Charger and this company gave me the best deal and fitted it quicker than the others could fit one. Will definitely use again for any electrical needs, and I would highly recommend."),
 ("M R.", "EV charger", "This is a brilliant company, they were punctual, tidy and went to extra lengths to fit my Dad's electric charge point. The chap who installed was extremely kind and polite to my elderly parents and would highly recommend to anyone looking to install through them."),
 ("Richard B.", "Hypervolt", "Contacted Evelec Ltd via their contact form and Chris contacted me same day to book in an assessment. Meeting went well and together we agreed on my best solution. Date booked for Alex to install and this went very well. Both Chris and Alex were very professional, pleasant and I now have a lovely Hypervolt EV Charger installed."),
 ("Edward G.", "Hypervolt", "A huge thankyou to the team at EVelec for installing our Hypervolt charger. From start to finish the whole process has been brilliant Chris and Alex were spot on. We are enjoying charging our ev and would definitely recommend EVelec to anyone."),
 ("Darren Y.", "Second charger · Worthing", "This is the second EV charger EVelec have installed for me. On time, informative, tidy and honest. Accommodated all my requests. Thank you!"),
 ("Luke W.", "EV charger", "Really impressed with these guys, after shopping around they stood out for product range I wanted, prompt service, and price. Chris (site survey) and Alex (Fitter) were really easy to work with and overall did a great job. Would recommend."),
 ("Andrew", "EV charger", "Totally professional and efficient service from first phone call to final fitting of EV charger and setting up the app. Mark did a very neat job and managed to position the charger and other components exactly where we wanted them. He was quick and tidy too. Helpful, competent and friendly."),
 ("Leigh N.", "Hypervolt", "Great service. From the initial quote through to the works, friendly, informative and on time. We had a Hypervolt car charger fitted, would definitely recommend and will be back for a quote on solar panels and battery in the future."),
 ("Drew F.", "EV charger", "An excellent job of installation done by Mark. Am very pleased. And, he gave me some good advice about which apps to use to get the most out of my new electric car. Would highly recommend."),
 ("Timo C.", "EV charger", "Brilliant service from EVelec. Professional consultation, fair pricing, and an exceptional final result with a finish that exceeded our expectations. Quality workmanship and genuine professionalism at every stage. Fully recommend."),
 ("Heather S.", "EV + outdoor sockets", "Pleased with the work by Chris and Mark to install EV charging point and external electrical power points. Mark visited to get a proper understanding of the site (not entirely straightforward) and prepared the quote accordingly. Everything works well and they were most professional."),
 ("Ian H.", "26-bay residential car park", "We wanted EV charge points installing across 26 bays in our residential development underground car park. After sourcing quotes from numerous National suppliers, which seemed quite expensive, we were recommended to EVelec. …"),
 ("Chris F.", "Office & residential", "We have had EVelec install two EV chargers at our office and at a residential property. Both installations were flawless with minimal mess created and incredibly neat cabling at both locations. …"),
 ("Martin S.", "Solar & battery", "I'm really pleased with my solar and battery installation. Chris and team were brilliant throughout - from advising on the spec and different options, assessing all the practicalities and a neat and professional result. …"),
 ("Jackie H.", "Solar & electrical", "I'm extremely pleased I chose this local company. The team were punctual, reliable, respectful of my home, and flexible around my schedule and visitors. …"),
 ("David F.", "EV, rewire & battery", "What a delight it was to have Mark and Chris here working on our EV charging. Great work so then we got them back to do our house rewiring, new build electrics, power diverter and then battery storage! That must say it all! …"),
]
def rcard(r):
    name, svc, text = r
    return f'''<article class="rcard"><div class="top"><span class="stars" aria-label="5 out of 5 stars">★★★★★</span><span class="svc-tag">{escape(svc)}</span></div>
<p>“{escape(text)}”</p><div class="who"><span class="av">{escape(name[0])}</span><div><b>{escape(name)}</b><small>Google review</small></div></div></article>'''

def reviews_marquee(title="Don't just take our word for it"):
    row1 = REVIEWS[:10]; row2 = REVIEWS[10:]
    t1 = "".join(rcard(r) for r in row1); t2 = "".join(rcard(r) for r in row2)
    return f'''<section class="section reviews" id="reviews"><div class="wrap">
<div class="head-row"><div class="head rv"><div class="pill-label">Customer reviews</div><h2>{title}</h2>
<p class="lead">Real words from real customers across Brighton, Sussex and the South East.</p></div>
<a class="rev-summary rv d1" href="{C["google"]}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit"><span class="g">{GOOGLE}</span><span class="big">5.0</span><span><span class="stars">★★★★★</span><small><b>{C["review_count"]}</b> five-star reviews on Google</small></span></a></div></div>
<div class="rev-rows">
<div class="marquee"><div class="track" style="--dur:90s">{t1}{t1}</div></div>
<div class="marquee"><div class="track rev" style="--dur:100s">{t2}{t2}</div></div>
</div>
<div class="wrap" style="text-align:center;margin-top:40px"><a class="btn btn-dark" href="{C["google"]}" target="_blank" rel="noopener">Read all {C["review_count"]} reviews on Google <span class="arr">{ic("arrow-ur")}</span></a></div>
</section>'''

# --------------------------------------------------------------- chrome ----
def mi(href, icon, title, sub, tag=""):
    return f'<a class="mi" href="{href}"><span class="ib">{ic(icon)}</span><span><b>{title}{tag}</b><small>{sub}</small></span></a>'

def tagh(t, red=False):
    return f'<span class="tag{" red" if red else ""}">{t}</span>'

NAV = [("ozev-grant.html", "Grants"), ("our-work.html", "Our Work"), ("reviews.html", "Reviews"), ("about.html", "About"), ("contact.html", "Contact")]

def header(active):
    links = "".join(f'<li><a href="{h}"{" class=active" if h == active else ""}>{l}</a></li>' for h, l in NAV)
    mega = f'''<div class="mega" role="region" aria-label="Services menu">
  <div class="mega-side">
    <div class="mega-label">Tailored solutions for</div>
    <a class="tailored" href="ev-charging.html#home"><span>Homeowners<small>Chargers, solar &amp; batteries</small></span><span class="go">{ic("arrow")}</span></a>
    <a class="tailored" href="ev-charging.html#workplace"><span>Businesses &amp; landlords<small>Workplace &amp; residential blocks</small></span><span class="go">{ic("arrow")}</span></a>
    <div class="mega-label" style="margin-top:8px">Watch</div>
    <a class="tour" href="index.html#top"><div class="thumb" style="background-image:url(assets/img/hero-2-aerial.jpg)"><span class="play">{ic("play")}</span><span class="cap">The EVelec film</span></div>
      <div class="meta"><span>Charge. Generate. Store.<small>See what we do in 20 seconds</small></span></div></a>
  </div>
  <div class="mega-main">
    <div class="mega-col"><div class="mega-label">{ic("charger")} EV Charging</div>
      {mi("ev-charging.html#home","home","Home Charging","Smart chargers fitted at home")}
      {mi("ev-charging.html#workplace","briefcase","Workplace Charging","Up to £14,000 OZEV funding")}
      {mi("ev-charging.html#residential","building","Residential Blocks","Managed, billable charging")}
      {mi("ozev-grant.html","pound","OZEV Grants","We handle the paperwork",tagh("Save £350"))}
    </div>
    <div class="mega-col"><div class="mega-label">{ic("sun")} Renewables</div>
      {mi("solar-pv.html","sun","Solar PV","0% VAT · cut your bills")}
      {mi("battery-storage.html","battery","Battery Storage","Store cheap-rate &amp; solar energy")}
      {mi("solar-pv.html#together","layers","Solar + Battery + EV","One connected system")}
      {mi("solar-pv.html#together","drop","Hot Water Diverters","myenergi eddi &amp; Solar Boost")}
    </div>
    <div class="mega-col"><div class="mega-label">{ic("bolt")} Electrical</div>
      {mi("electrical-services.html#emergency","siren","Emergency Call-outs","A local engineer, fast",tagh("Urgent",True))}
      {mi("electrical-services.html","clipboard","EICR Reports","Safety reports to BS 7671")}
      {mi("electrical-services.html","fuse","Rewires &amp; Fuse Boards","18th Edition consumer units")}
      {mi("electrical-services.html","plug","PAT, Lighting &amp; Nest","Plus sockets &amp; garden lighting")}
    </div>
    <div class="mega-foot"><span class="stars-row" style="display:flex;align-items:center;gap:8px;color:var(--muted);font-weight:600"><span class="stars">★★★★★</span>{C["review_count"]} five-star reviews on Google</span>
      <a href="index.html#services">See all services <span class="dot">{ic("arrow")}</span></a></div>
  </div>
</div>'''
    sheet = f'''<div class="sheet" aria-label="Menu">
  <div class="sheet-top"><img src="assets/img/evelec-logo-white.png" alt="EVelec"><button data-sheet aria-label="Close menu">{ic("x")}</button></div>
  <a class="sl" href="index.html">Home</a>
  <details open><summary>Services {ic("chev","icon chev")}</summary><div class="sub">
    <a href="ev-charging.html#home">{ic("home")} Home Charging</a><a href="ev-charging.html#workplace">{ic("briefcase")} Workplace Charging</a>
    <a href="ev-charging.html#residential">{ic("building")} Residential Blocks</a><a href="solar-pv.html">{ic("sun")} Solar PV</a>
    <a href="battery-storage.html">{ic("battery")} Battery Storage</a><a href="electrical-services.html">{ic("bolt")} Electrical Services</a>
  </div></details>
  {"".join(f'<a class="sl" href="{h}">{l}</a>' for h, l in NAV)}
  <div class="btn-row"><a class="btn btn-outline" href="tel:{C["phone_link"]}">{ic("phone")} Call</a><a class="btn btn-green" href="contact.html">Free quote</a></div>
</div>'''
    return f'''<div class="topwrap">
<div class="announce"><div class="wrap">
  <span class="new">NEW</span>
  <span>{ic("bolt","icon")}</span>
  <span><b>OZEV grants available.</b> <span class="msg-long">Up to £350 off a home charger, or £14,000 for your workplace.</span></span>
  <a class="go" href="ozev-grant.html">Check eligibility {ic("arrow")}</a>
  <button class="x" aria-label="Dismiss">{ic("x")}</button>
</div></div>
<div class="navbar"><div class="nav-inner">
  <a class="brand" href="index.html" aria-label="EVelec home"><img src="assets/img/evelec-logo-white.png" alt="EVelec" width="123" height="34"></a>
  <ul class="nav-links">
    <li><button data-mega aria-expanded="false" aria-haspopup="true">Services {ic("chev","icon chev")}</button></li>
    {links}
  </ul>
  <div class="nav-right">
    <a class="phone" href="tel:{C["phone_link"]}">{ic("phone")} {C["phone"]}</a>
    <a class="btn btn-outline" href="contact.html?service=Site%20survey">Book a survey</a>
    <a class="btn btn-light" href="contact.html">Get free quote {ic("arrow")}</a>
  </div>
  <button class="burger" data-sheet aria-label="Open menu">{ic("menu")}</button>
</div>{mega}</div>
</div>{sheet}'''

def footer():
    return f'''<footer class="site"><div class="wrap">
  <div class="foot-cta"><h2>Ready to charge smarter and power your home with the <span class="green">sun</span>?</h2>
    <div class="btn-row"><a class="btn btn-green" href="contact.html">Get a free quote <span class="arr">{ic("arrow")}</span></a><a class="btn btn-outline" href="tel:{C["phone_link"]}">{ic("phone")} {C["phone"]}</a></div></div>
  <div class="foot-cols">
    <div><img src="assets/img/evelec-logo-white.png" alt="EVelec" width="145" height="40">
      <p>The leading installer of EV charge points, Solar PV and battery storage for homes, apartment blocks and businesses across Brighton and the South East.</p>
      <div class="accred"><span>OZEV Approved Installer</span><span>NICEIC Approved Contractor</span><span>City &amp; Guilds</span><span>Nest Pro</span></div>
      <div class="socials"><a href="{C["facebook"]}" target="_blank" rel="noopener" aria-label="Facebook">{ic("fb")}</a><a href="{C["instagram"]}" target="_blank" rel="noopener" aria-label="Instagram">{ic("ig")}</a><a href="{C["google"]}" target="_blank" rel="noopener" aria-label="Google reviews">{ic("star")}</a></div>
    </div>
    <div><h4>EV Charging</h4><ul><li><a href="ev-charging.html#home">Home Charging</a></li><li><a href="ev-charging.html#workplace">Workplace Charging</a></li><li><a href="ev-charging.html#residential">Residential Blocks</a></li><li><a href="ozev-grant.html">OZEV Grants</a></li></ul></div>
    <div><h4>Company</h4><ul><li><a href="solar-pv.html">Solar PV</a></li><li><a href="battery-storage.html">Battery Storage</a></li><li><a href="electrical-services.html">Electrical Services</a></li><li><a href="our-work.html">Our Work</a></li><li><a href="reviews.html">Reviews</a></li><li><a href="about.html">About</a></li></ul></div>
    <div><h4>Get in touch</h4><ul><li><a href="tel:{C["phone_link"]}">{C["phone"]}</a></li><li><a href="mailto:{C["email"]}">{C["email"]}</a></li><li>{C["address"]}</li><li>Covering Sussex, Surrey, Hampshire &amp; Kent</li><li><a href="{C["google"]}" target="_blank" rel="noopener">★★★★★ {C["review_count"]} Google reviews</a></li></ul></div>
  </div>
  <div class="foot-bottom"><span>© <span id="year">2026</span> EVelec Ltd · Registered in England &amp; Wales · Company no. {C["company_no"]}</span><span>Brighton · Sussex · Surrey · Hampshire · Kent</span></div>
</div></footer>
<div class="mbar"><a class="call" href="tel:{C["phone_link"]}">{ic("phone")} Call us</a><a class="q" href="contact.html">{ic("bolt")} Free quote</a></div>'''

def page(fn, title, desc, body, og="hero-2-aerial"):
    html = f'''<!doctype html>
<html lang="en-GB">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{C["site_url"]}/{"" if fn == "index.html" else fn}">
<meta property="og:type" content="website"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:image" content="{C["site_url"]}/assets/img/{og}.jpg">
<meta name="theme-color" content="#111416">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Sora:wght@600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"Electrician","name":"EVelec Ltd","url":"{C["site_url"]}","telephone":"{C["phone_link"]}","email":"{C["email"]}","image":"{C["site_url"]}/assets/img/evelec-logo.png","address":{{"@type":"PostalAddress","addressLocality":"Brighton","addressCountry":"GB"}},"areaServed":["Brighton","Sussex","Surrey","Hampshire","Kent"],"sameAs":["{C["facebook"]}","{C["instagram"]}"],"aggregateRating":{{"@type":"AggregateRating","ratingValue":"5","reviewCount":"{C["review_count"]}"}}}}</script>
</head>
<body>
{header(fn)}
<main id="top">
{body}
</main>
{footer()}
<script src="assets/main.js"></script>
</body>
</html>'''
    (OUT / fn).write_text(html, encoding="utf-8")

def phero(crumb, label, h1, lead, video, service=""):
    q = f"contact.html?service={service}" if service else "contact.html"
    return f'''<section class="phero">{vid(video)}<div class="wrap">
<div class="crumbs"><a href="index.html">Home</a> / {crumb}</div>
<div class="pill-label" style="background:rgba(126,206,74,.14);border-color:rgba(126,206,74,.35);color:var(--green)">{label}</div>
<h1>{h1}</h1><p class="lead">{lead}</p>
<div class="btn-row" style="margin-top:28px"><a class="btn btn-green" href="{q}">Get a free quote <span class="arr">{ic("arrow")}</span></a><a class="btn btn-outline" href="tel:{C["phone_link"]}">{ic("phone")} {C["phone"]}</a></div>
</div></section>'''

def grant_band():
    return f'''<section class="section tight"><div class="wrap"><div class="grant rv">
<div><div class="pill-label" style="background:rgba(255,255,255,.5);border-color:transparent">OZEV approved installers</div><h2>Save with government EV grants</h2>
<p>We supply and install the charge point of your choice and handle all of the grant paperwork for you.</p>
<a class="btn btn-dark" href="ozev-grant.html">Check your eligibility <span class="arr" style="background:rgba(255,255,255,.15)">{ic("arrow")}</span></a></div>
<div class="g"><div class="n">£350</div><p>off a home charge point for flat owners and renters with designated parking</p></div>
<div class="g"><div class="n">£14,000</div><p>for businesses: £350 per socket, up to 40 sockets</p></div>
</div></div></section>'''

def quote_section(title="Get your free, no-obligation quote"):
    areas = "".join(f"<span>{ic('pin')}{a}</span>" for a in AREAS)
    opts = ["Home EV Charging", "Workplace EV Charging", "Residential Block EV Charging", "Solar PV", "Battery Storage", "Solar + Battery + EV", "Electrical Services", "Emergency Call-out", "Site survey", "OZEV Grant Enquiry", "Other"]
    options = "".join(f"<option>{o}</option>" for o in opts)
    return f'''<section class="section dark" id="quote"><div class="wrap split">
<div class="rv"><div class="pill-label">Get in touch</div><h2>{title}</h2>
<p class="lead">Tell us about your property and what you're looking for. We'll arrange a site visit and come back with a clear quote.</p>
<div class="areas">{areas}</div>
<div class="contact-lines">
 <a href="tel:{C["phone_link"]}"><span class="ic">{ic("phone")}</span><span><small>Call us</small>{C["phone"]}</span></a>
 <a href="mailto:{C["email"]}"><span class="ic">{ic("mail")}</span><span><small>Email</small>{C["email"]}</span></a>
 <div><span class="ic">{ic("pin")}</span><span><small>Based in</small>{C["address"]}</span></div>
</div></div>
<form class="quote rv d1" data-endpoint="{C["form_endpoint"]}" data-email="{C["email"]}">
 <h3>Request a quote</h3><p class="sub">Free site survey · No obligation</p>
 <div class="form-row"><div class="field"><label for="q-name">Full name *</label><input id="q-name" name="name" required autocomplete="name"></div>
 <div class="field"><label for="q-phone">Phone *</label><input id="q-phone" name="phone" type="tel" required autocomplete="tel"></div></div>
 <div class="form-row"><div class="field"><label for="q-email">Email *</label><input id="q-email" name="email" type="email" required autocomplete="email"></div>
 <div class="field"><label for="q-post">Postcode *</label><input id="q-post" name="postcode" required autocomplete="postal-code"></div></div>
 <div class="field"><label for="q-svc">What do you need? *</label><select id="q-svc" name="service" required>{options}</select></div>
 <div class="field"><label>Property type</label><div class="chips">
  <label><input type="radio" name="property" value="House" checked><span>House</span></label>
  <label><input type="radio" name="property" value="Flat / apartment"><span>Flat / apartment</span></label>
  <label><input type="radio" name="property" value="Residential block"><span>Residential block</span></label>
  <label><input type="radio" name="property" value="Business"><span>Business</span></label></div></div>
 <div class="field"><label for="q-msg">Anything else?</label><textarea id="q-msg" name="message" placeholder="e.g. your car, preferred charger, where you'd like it fitted…"></textarea></div>
 <button class="btn btn-green" type="submit" style="width:100%">Send my enquiry <span class="arr">{ic("arrow")}</span></button>
 <p class="form-note">We only use your details to respond to your enquiry.</p>
 <div class="form-success">Thanks! Your enquiry has been sent. We'll be in touch shortly.</div>
</form></div></section>'''

def trustbar():
    items = [("shield", "OZEV Approved Installer"), ("check", "NICEIC Approved Contractor"), ("clipboard", "City &amp; Guilds qualified"), ("dial", "Nest Pro Installers")]
    t = "".join(f'<span class="trust-item"><span class="ic">{ic(i)}</span>{l}</span>' for i, l in items)
    wms = ('<span class="wm andersen">ANDERSEN</span><span class="wm hypervolt">HYPER<i>V</i>OLT</span><span class="wm zappi">zappi</span>'
           '<span class="wm easee">easee</span><span class="wm eo">EO</span><span class="wm sp">Simpson &amp; Partners</span>')
    one = t + wms
    return f'<div class="trustbar"><div class="marquee"><div class="track">{one}{one}</div></div></div>'

# ---------------------------------------------------------------- pages ----
def build_home():
    services = [
        ("s-7 tall", "svc-home", "01", "Home Charging", "From £350 grant", "Smart, safe chargers from Andersen, Hypervolt, zappi and more, neatly fitted with hidden cable runs.", "ev-charging.html#home"),
        ("s-5 tall", "svc-solar", "02", "Solar PV", "0% VAT", "Generate your own clean electricity, slash your bills and sell surplus back to the grid.", "solar-pv.html"),
        ("s-4", "svc-battery", "03", "Battery Storage", "Store & save", "Charge on cheap-rate tariffs or from your solar, and use it when you need it.", "battery-storage.html"),
        ("s-4", "svc-workplace", "04", "Workplace Charging", "Up to £14,000", "Charge points for staff, fleet and visitors with OZEV Workplace Charging Scheme funding.", "ev-charging.html#workplace"),
        ("s-4", "svc-residential", "05", "Residential Blocks", "Landlords & agents", "Scalable, billable charging for apartment car parks, from 2 bays to 26 and beyond.", "ev-charging.html#residential"),
    ]
    cards = "".join(f'''<a class="svc {c} rv{" d"+str(i%3) if i else ""}" href="{h}">{vid(v)}<span class="num">{n}</span><span class="tagline">{tg}</span>
<div class="body"><h3>{t}</h3><p>{d}</p></div><span class="go">{ic("arrow")}</span></a>''' for i, (c, v, n, t, tg, d, h) in enumerate(services))
    cards += f'''<a class="svc s-12 wide rv" href="electrical-services.html">{vid("svc-electrical")}<span class="num">06</span><span class="tagline">Domestic &amp; commercial</span>
<div class="body"><h3>Electrical Services</h3><p>EICRs, fault finding, rewires, new fuse boards, lighting, Nest and PAT testing, all certified within 28 days.</p>
<span class="emerg">{ic("siren")} Emergency call-outs available</span></div><span class="go">{ic("arrow")}</span></a>'''
    gallery = [("home-charging-porsche-andersen", "Andersen charger · Porsche Macan"), ("battery-libbi-solis-inverter", "Twin myenergi libbi + Solis inverter"),
               ("home-charging-hypervolt", "Hypervolt Home 3 Pro"), ("solar-pv-flat-roof", "Flat-roof solar array"),
               ("home-charging-ohme", "Ohme with immaculate cable runs"), ("van-with-charger", "Another install complete"),
               ("battery-storage-sigenergy", "Sigenergy battery system"), ("home-charging-bmw-x1", "BMW X1 home charging, Brighton")]
    gal = "".join(f'<figure class="rv"><img src="assets/img/{f}.jpg" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c in gallery)
    body = f'''
<section class="hero" aria-label="EVelec film">
  <div class="hero-media">
    <img class="on" src="assets/img/hero-1-plug.jpg" alt="" fetchpriority="high">
    <video muted playsinline preload="auto" poster="assets/img/hero-1-plug.jpg" aria-hidden="true"><source src="assets/video/hero-1-m.mp4" type="video/mp4" media="(max-width: 760px)"><source src="assets/video/hero-1.mp4" type="video/mp4"></video>
    <video muted playsinline preload="auto" poster="assets/img/hero-2-aerial.jpg" aria-hidden="true"><source src="assets/video/hero-2-m.mp4" type="video/mp4" media="(max-width: 760px)"><source src="assets/video/hero-2.mp4" type="video/mp4"></video>
    <video muted playsinline preload="auto" poster="assets/img/hero-3-logo.jpg" aria-hidden="true"><source src="assets/video/hero-3-m.mp4" type="video/mp4" media="(max-width: 760px)"><source src="assets/video/hero-3.mp4" type="video/mp4"></video>
  </div>
  <div class="hero-content"><div class="wrap"><div class="hero-copy">
    <div class="pill-label" style="background:rgba(126,206,74,.14);border-color:rgba(126,206,74,.35);color:var(--green)">OZEV approved · NICEIC approved contractor</div>
    <h1>Charge at home.<br>Run on <span class="green">sunshine.</span></h1>
    <p class="lead">Brighton's EV charging, solar and battery specialists. Expert installations for homes, apartment blocks and businesses across the South East.</p>
    <div class="hero-ctas">
      <a class="btn btn-green" href="contact.html">Get a free quote <span class="arr">{ic("arrow")}</span></a>
      <a class="g-chip" href="{C["google"]}" target="_blank" rel="noopener"><span class="g">{GOOGLE}</span><span><b><span class="stars">★★★★★</span></b>{C["review_count"]} five-star Google reviews</span></a>
    </div>
  </div></div></div>
  <div class="hero-bar"><div class="wrap">
    <div class="chapters"><button class="chapter active"><i></i>Charge</button><button class="chapter"><i></i>Generate</button><button class="chapter"><i></i>EVelec</button></div>
    <a class="scroll-cue" href="#services"><span></span>Scroll</a>
  </div></div>
</section>
{trustbar()}

<section class="section" id="services"><div class="wrap">
  <div class="head-row"><div class="head rv"><div class="pill-label">What we do</div><h2>Everything you need to go electric</h2>
  <p class="lead">From a single home charger to a full solar, battery and EV system, one qualified local team handles it all.</p></div>
  <a class="btn btn-dark rv d1" href="contact.html">Talk to an expert <span class="arr" style="background:rgba(255,255,255,.15)">{ic("arrow")}</span></a></div>
  <div class="bento">{cards}</div>
</div></section>

<section class="section dark tight"><div class="wrap">
  <div class="stats">
    <div class="stat rv"><div class="n"><span data-count="{C["review_count"]}">{C["review_count"]}</span></div><p>five-star reviews on Google</p></div>
    <div class="stat rv d1"><div class="n"><span class="green">£</span><span data-count="14000">14,000</span></div><p>OZEV workplace funding available</p></div>
    <div class="stat rv d2"><div class="n"><span data-count="28">28</span><span class="green"> days</span></div><p>certification issued on every job</p></div>
    <div class="stat rv d3"><div class="n"><span data-count="5">5</span><span class="green"> areas</span></div><p>Brighton, Sussex, Surrey, Hampshire &amp; Kent</p></div>
  </div>
</div></section>

<section class="section white"><div class="wrap eco">
  <div class="eco-img rv"><img src="assets/img/hero-2-aerial.jpg" alt="Home with solar roof and an electric car charging on the driveway" loading="lazy">
    <span class="hotspot" style="left:58%;top:24%"><i></i><span>Solar PV</span></span>
    <span class="hotspot" style="left:76%;top:52%"><i></i><span>Battery storage</span></span>
    <span class="hotspot" style="left:52%;top:70%"><i></i><span>EV charger</span></span>
  </div>
  <div class="rv d1"><div class="pill-label">Better together</div><h2>Generate. Store. Drive.</h2>
    <p class="lead">Solar, batteries and EV charging work best as one system, and we design and install all three.</p>
    <div class="steps-v">
      <div class="step-v"><span class="ic">{ic("sun")}</span><div><h4>Generate</h4><p>Solar panels turn daylight into free electricity for your home or business.</p></div></div>
      <div class="step-v"><span class="ic">{ic("battery")}</span><div><h4>Store</h4><p>A battery holds surplus solar or cheap overnight energy until you need it.</p></div></div>
      <div class="step-v"><span class="ic">{ic("car")}</span><div><h4>Drive</h4><p>Solar-aware chargers like zappi top your car up with your own clean power.</p></div></div>
    </div></div>
</div></section>

<section class="section"><div class="wrap">
  <div class="head center rv"><div class="pill-label">How it works</div><h2>From enquiry to charging in four simple steps</h2>
  <p class="lead">No guesswork and no hidden extras. Our customers say the process is the best part.</p></div>
  <div class="process">
    <div class="pstep rv"><span class="ic">{ic("phone")}</span><h3>Get in touch</h3><p>Call, email or send the form. We reply fast, often within minutes.</p></div>
    <div class="pstep rv d1"><span class="ic">{ic("home")}</span><h3>Free site survey</h3><p>We visit in person to plan the best location and cable route. No guessing from photos.</p></div>
    <div class="pstep rv d2"><span class="ic">{ic("doc")}</span><h3>Clear quote &amp; grants</h3><p>A clear, competitive quote, with OZEV grant paperwork handled for you.</p></div>
    <div class="pstep rv d3"><span class="ic">{ic("bolt")}</span><h3>Install &amp; certify</h3><p>A neat, tidy installation, app setup and full certification within 28 days.</p></div>
  </div>
</div></section>

{reviews_marquee()}

<section class="section white"><div class="wrap">
  <div class="head-row"><div class="head rv"><div class="pill-label">Recent installations</div><h2>Work we're proud of</h2>
  <p class="lead">Real installs by our team across Brighton, Sussex and the South East.</p></div>
  <a class="btn btn-dark rv d1" href="our-work.html">View all our work <span class="arr" style="background:rgba(255,255,255,.15)">{ic("arrow")}</span></a></div>
  <div class="gallery">{gal}</div>
</div></section>

{grant_band()}
{quote_section()}'''
    page("index.html", "EVelec | EV Charger, Solar PV & Battery Installers in Brighton & Sussex",
         "OZEV approved EV charge point, Solar PV and battery storage installers in Brighton, Sussex, Surrey, Hampshire and Kent. 224 five-star Google reviews. Free site survey.", body)

def build_ev():
    revs = lambda idx: '<div class="rgrid" style="margin-top:40px">' + "".join(rcard(REVIEWS[i]) for i in idx) + "</div>"
    body = f'''{phero("EV Charging", "EV charge point installation", "EV charging for homes, workplaces &amp; apartments",
        "OZEV approved installers of electric vehicle charge points across Brighton, Sussex, Surrey, Hampshire and Kent. We supply and install the charger of your choice and handle the grant paperwork for you.", "svc-home", "Home%20EV%20Charging")}
<nav class="subnav" aria-label="EV charging sections"><div><a href="#home">Home</a><a href="#workplace">Workplace</a><a href="#residential">Residential blocks</a><a href="ozev-grant.html">OZEV grants</a></div></nav>

<section class="section" id="home"><div class="wrap split">
  <div class="rv"><div class="pill-label">Charging for home</div><h2>Charge your car efficiently at home</h2>
    <p class="lead">If you've ordered an electric vehicle, or you're researching the switch, how you'll charge it efficiently at home is going to be top of your list.</p>
    <p>We'll recommend the right smart charger for your car, your property and your energy tariff, then install it safely and neatly, with cables hidden wherever possible.</p>
    {checks(["Andersen, Hypervolt, zappi, easee, EO and more", "Compatible with every plug-in vehicle brand", "Solar-ready chargers that run on your own power", "App setup and a full walkthrough on the day", "Certified installation by qualified engineers"])}
    <div class="note" style="background:var(--mint);border-color:#CBE8B6;color:var(--ink)"><b>Save up to £350:</b> residents of rental properties, and flat or apartment owners with designated parking, may be eligible for the OZEV EV Charge Point Grant. <a href="ozev-grant.html">Check eligibility →</a></div>
  </div>
  <div class="duo rv d1"><img src="assets/img/home-charging-porsche-andersen.jpg" alt="Andersen charger installed beside a Porsche Macan" loading="lazy"><img src="assets/img/home-charging-andersen-closeup.jpg" alt="Andersen A3 charger close-up" loading="lazy"></div>
</div><div class="wrap">{revs([0, 2, 6])}</div></section>

<section class="section dark" id="workplace"><div class="wrap split">
  <div class="vid-frame rv">{vid("svc-workplace")}</div>
  <div class="rv d1"><div class="pill-label">Charging for the workplace</div><h2>A must-do for every business</h2>
    <p class="lead">With all new cars and vans set to be zero emission by 2030, offering EV charging is no longer a "nice to have" but a "must-do" for businesses.</p>
    <p>Charging for staff is a great way to stay competitive, and with the OZEV Workplace Charging Scheme there's really no excuse.</p>
    <div class="panel" style="background:var(--ink-2);margin:24px 0;padding:28px"><div class="big-n">£14,000</div><p style="margin:8px 0 0">UK businesses can claim up to £14,000: £350 per socket, for up to 40 sockets.</p></div>
    {checks(["Staff, fleet, customer and visitor charging", "Commercial premises of every size", "Grant applications handled for you"])}
    <a class="btn btn-green" href="contact.html?service=Workplace%20EV%20Charging">Talk to us about your workplace <span class="arr">{ic("arrow")}</span></a>
  </div>
</div></section>

<section class="section" id="residential"><div class="wrap split">
  <div class="rv"><div class="pill-label">Residential blocks &amp; apartments</div><h2>EV charging for residential buildings</h2>
    <p class="lead">Owners and property managers want their buildings to offer the very best facilities and to be energy efficient.</p>
    <p>Grants are available for charge points in the car parks of residential buildings and apartment blocks, covering both the charge points and the infrastructure that enables wider roll-out across larger buildings.</p>
    <div class="grid g2" style="margin:26px 0">
      <div class="card"><div class="ic">{ic("pound")}</div><h3>Charge point &amp; infrastructure grants</h3><p>Funding for the chargers and the electrical backbone.</p></div>
      <div class="card"><div class="ic">{ic("users")}</div><h3>Built for landlords &amp; agents</h3><p>Back-office systems for easy resident billing and costing.</p></div>
    </div>
    <a class="btn btn-dark" href="contact.html?service=Residential%20Block%20EV%20Charging">Discuss your building <span class="arr" style="background:rgba(255,255,255,.15)">{ic("arrow")}</span></a>
  </div>
  <div class="vid-frame rv d1">{vid("svc-residential")}</div>
</div><div class="wrap">{revs([15, 16, 4])}</div></section>
{grant_band()}
{quote_section("Let's get you charging")}'''
    page("ev-charging.html", "EV Charger Installation Brighton & Sussex | Home, Workplace & Apartments | EVelec",
         "OZEV approved EV charge point installers for homes, workplaces and residential blocks across Brighton, Sussex, Surrey, Hampshire and Kent.", body, "svc-home")

def build_ozev():
    body = f'''{phero("OZEV Grants", "Government funding", "EV charger grants, handled for you",
        "As approved OZEV installers, we supply and install the charge point of your choice, and we take care of all the grant paperwork.", "hero-1", "OZEV%20Grant%20Enquiry")}
<section class="section"><div class="wrap">
  <div class="grid g2">
    <div class="card rv" style="padding:40px"><div class="ic">{ic("home")}</div><div class="pill-label">At home</div><div class="big-n" style="color:var(--ink)">£350</div>
      <h3 style="margin-top:12px">OZEV EV Charge Point Grant</h3>
      <p>Residents of rental properties, and owners of flats or apartments with designated parking, are eligible for up to £350 off the cost of an EV charge point (subject to meeting all eligibility criteria).</p>
      <div style="margin-top:20px">{checks(["Flat & apartment owners with designated parking", "Tenants in rental properties", "Deducted straight from your installation cost"])}</div></div>
    <div class="card rv d1" style="padding:40px;background:var(--ink);color:#fff;border-color:var(--ink)"><div class="ic" style="background:var(--green);color:var(--ink)">{ic("briefcase")}</div><div class="pill-label" style="background:rgba(126,206,74,.12);border-color:rgba(126,206,74,.3);color:var(--green)">At work</div><div class="big-n">£14,000</div>
      <h3 style="margin-top:12px">Workplace Charging Scheme (WCS)</h3>
      <p style="color:var(--muted-dk)">£350 per socket, up to 40 sockets, for commercial premises serving staff, customers and visitors, or both.</p>
      <div style="margin-top:20px" class="dark">{checks(["£350 per socket", "Up to 40 sockets", "For staff, customers & visitors"])}</div></div>
  </div>
  <div class="split" style="margin-top:80px">
    <div class="rv"><div class="pill-label">How it works</div><h2>We handle the paperwork</h2>
      {checks(["Tell us about your property and parking", "We confirm eligibility and recommend a charger", "We apply for the grant on your behalf", "Our engineers install and certify your charge point"])}</div>
    <div class="note rv d1"><b>Please note:</b> all grants are subject to eligibility criteria set by the Office for Zero Emission Vehicles (OZEV), and schemes and amounts can change. Get in touch and we'll confirm exactly what you're entitled to.</div>
  </div>
</div></section>
{quote_section("Find out what you're entitled to")}'''
    page("ozev-grant.html", "OZEV EV Charger Grants | Home & Workplace Charging Scheme | EVelec",
         "Approved OZEV installers: up to £350 off a home charge point and up to £14,000 through the Workplace Charging Scheme. We handle the paperwork.", body, "hero-1-plug")

def build_solar():
    revs = '<div class="rgrid" style="margin-top:48px">' + "".join(rcard(REVIEWS[i]) for i in (1, 17, 18)) + "</div>"
    body = f'''{phero("Solar PV", "Solar PV installers", "Solar panels for homes &amp; businesses",
        "We specialise in solar panel installation for domestic and commercial buildings, from small domestic systems to larger commercial premises.", "svc-solar", "Solar%20PV")}
<section class="section"><div class="wrap split top">
  <div class="rv"><div class="pill-label">Why go solar?</div><h2>The advantages of solar PV</h2>
    <p class="lead">As well as the 0% VAT that currently applies to Solar PV installations, solar panels bring significant advantages:</p>
    {checks(["Reduce your energy bills and reliance on the National Grid", "Sell surplus energy back to the National Grid", "Charge your electric vehicle", 'Integrate with <a href="battery-storage.html">battery storage</a> for even more savings', "Heat hot water or underfloor heating with myenergi eddi or Solar Boost", "0% VAT rated by the UK Government", "Push your property towards Net Zero"])}
  </div>
  <div class="rv d1"><img class="ph" src="assets/img/solar-pv-flat-roof.jpg" alt="Solar panels installed on a flat roof in the Sussex countryside" loading="lazy">
    <div class="panel" style="margin-top:18px"><div class="big-n">0% VAT</div><h3 style="margin-top:10px">How solar reduces your bills</h3>
    <p style="margin:0">Generate your own electricity and take control of your energy use. Your monthly bills will come tumbling down.</p></div></div>
</div><div class="wrap">{revs}</div></section>
<section class="section dark" id="together"><div class="wrap">
  <div class="head center rv"><div class="pill-label">Make the most of your panels</div><h2>Pair solar with storage and EV charging</h2></div>
  <div class="bento">
    <a class="svc s-4 rv" href="battery-storage.html">{vid("svc-battery")}<div class="body"><h3>Battery Storage</h3><p>Use your daytime solar in the evening.</p></div><span class="go">{ic("arrow")}</span></a>
    <a class="svc s-4 rv d1" href="ev-charging.html">{vid("svc-home")}<div class="body"><h3>EV Charging</h3><p>Charge your car with your own clean power.</p></div><span class="go">{ic("arrow")}</span></a>
    <div class="svc s-4 rv d2"><img src="assets/img/garage-zappi-libbi-battery.jpg" alt="zappi charger and myenergi libbi battery in a garage" loading="lazy"><div class="body"><h3>Hot water diverters</h3><p>Send surplus solar to your hot water with myenergi eddi or Solar Boost.</p></div></div>
  </div>
</div></section>
{quote_section("Start generating your own power")}'''
    page("solar-pv.html", "Solar Panel Installers Brighton & Sussex | Solar PV | EVelec",
         "Domestic and commercial Solar PV installation across Brighton, Sussex and the South East. 0% VAT, lower bills and EV charging integration.", body, "svc-solar")

def build_battery():
    body = f'''{phero("Battery Storage", "Battery storage installers", "Store your energy. Use it when it suits you.",
        "Battery storage installations for domestic and commercial buildings, charged from your solar panels or cheap overnight tariffs.", "svc-battery", "Battery%20Storage")}
<section class="section"><div class="wrap split top">
  <div class="duo rv"><img src="assets/img/battery-myenergi-libbi.jpg" alt="myenergi libbi battery installed in a garage" loading="lazy"><img src="assets/img/battery-libbi-solis-inverter.jpg" alt="Two libbi batteries with Solis inverter" loading="lazy"></div>
  <div class="rv d1"><div class="pill-label">Why add a battery?</div><h2>The advantages of battery storage</h2>
    <p class="lead">As well as the 0% VAT that currently applies, a battery storage system brings significant advantages:</p>
    {checks(["Reduce your energy bills and reliance on the National Grid", "Charge your battery on cheap-rate tariffs", "Store surplus energy to use when you want", "Sell surplus energy back to the National Grid", "Charge your electric vehicle", 'Integrate with <a href="solar-pv.html">Solar PV</a>', "Heat hot water or underfloor heating with myenergi eddi or Solar Boost", "0% VAT rated by the UK Government", "Push your property towards Net Zero"])}
    <a class="btn btn-green" href="contact.html?service=Battery%20Storage">Get a battery quote <span class="arr">{ic("arrow")}</span></a>
  </div>
</div></section>
<section class="section white"><div class="wrap"><div class="strip">
  <img class="rv" src="assets/img/battery-storage-sigenergy.jpg" alt="Sigenergy battery system" loading="lazy">
  <img class="rv d1" src="assets/img/garage-zappi-libbi-battery.jpg" alt="zappi and libbi installation" loading="lazy">
  <img class="rv d2" src="assets/img/battery-myenergi-libbi.jpg" alt="myenergi libbi" loading="lazy">
  <img class="rv d3" src="assets/img/battery-libbi-solis-inverter.jpg" alt="Battery and inverter install" loading="lazy">
</div></div></section>
{quote_section("Store more, spend less")}'''
    page("battery-storage.html", "Battery Storage Installers Brighton & Sussex | EVelec",
         "Home and commercial battery storage installation across Brighton, Sussex and the South East. Store cheap-rate and solar energy. 0% VAT.", body, "svc-battery")

def build_electrical():
    items = [
        ("clipboard", "EICR Reports", "A full condition report highlighting all safety risks, as set out by BS 7671."),
        ("search", "Fault Finding", "We fix and repair what isn't working, quickly and cost-effectively."),
        ("cable", "Full &amp; Partial Rewires", "Full property or partial rewires for kitchens and loft extensions, working smoothly alongside other trades."),
        ("fuse", "New Fuse Boards", "New RCD-protected, metal-clad consumer units to the latest 18th Edition standards."),
        ("leaf", "Energy Saving Solutions", "From LED lighting to energy-efficient heating products, cut your energy use and save money."),
        ("tree", "Garden Lighting &amp; Sockets", "Turn the garden into an extra room with atmospheric lighting or weatherproof sockets."),
        ("socket", "Extra Sockets", "Add sockets to an existing installation and cut fire risk by removing extension leads."),
        ("bulb", "New Lighting", "From a new dining room fitting to full LED kitchen downlights, we'll advise and install."),
        ("dial", "Nest Technology", "We're Nest Pro Installers, trained to install Nest products in homes and businesses."),
        ("plug", "PAT Testing", "Keep employees safe and insurers happy with documented appliance testing."),
    ]
    cards = "".join(f'<div class="card rv{" d"+str(i%3) if i%3 else ""}"><div class="ic">{ic(a)}</div><h3>{t}</h3><p>{d}</p></div>' for i, (a, t, d) in enumerate(items))
    body = f'''{phero("Electrical Services", "Electricians in Brighton", "Domestic &amp; commercial electrical services",
        "As well as EV charging, our Brighton electricians look after residential and commercial customers across Sussex and beyond.", "svc-electrical", "Electrical%20Services")}
<section class="section" id="emergency"><div class="wrap">
  <div class="emergency rv"><div><h3>{ic("siren")} Emergency call-outs</h3><p>Need an engineer urgently to diagnose or fix an electrical issue? Our local team can be with you swiftly, and our call-out rates are some of the most competitive around.</p></div>
  <a class="btn btn-light" href="tel:{C["phone_link"]}">{ic("phone")} Call {C["phone"]}</a></div>
  <div class="head-row" style="margin-top:80px"><div class="head rv"><div class="pill-label">Our services</div><h2>Every job signed off and certified</h2></div>
  <p class="lead rv d1" style="max-width:420px">All work is signed off on completion, with the correct certification issued within 28 days.</p></div>
  <div class="svc-list">{cards}</div>
  <div class="rgrid" style="margin-top:56px">{rcard(REVIEWS[14])}{rcard(REVIEWS[19])}{rcard(REVIEWS[4])}</div>
</div></section>
{quote_section("Need an electrician?")}'''
    page("electrical-services.html", "Electricians in Brighton & Sussex | EICR, Rewires, Fuse Boards | EVelec",
         "Domestic and commercial electricians in Brighton and Sussex: emergency call-outs, EICRs, fault finding, rewires, fuse boards, lighting, Nest and PAT testing.", body, "svc-electrical")

def build_work():
    photos = [("home-charging-porsche-andersen", "Andersen charger · Porsche Macan"), ("battery-libbi-solis-inverter", "Twin myenergi libbi + Solis inverter"),
              ("home-charging-hypervolt", "Hypervolt Home 3 Pro"), ("vans-on-site", "The EVelec team on site"),
              ("solar-pv-flat-roof", "Flat-roof solar array"), ("home-charging-ohme", "Ohme with immaculate cable runs"),
              ("garage-zappi-libbi-battery", "zappi + libbi battery garage install"), ("van-with-charger", "Another install complete"),
              ("home-charging-andersen-closeup", "Andersen A3 in wood finish"), ("battery-storage-sigenergy", "Sigenergy battery system"),
              ("home-charging-bmw-x1", "BMW X1 home charging, Brighton"), ("battery-myenergi-libbi", "myenergi libbi battery"),
              ("home-charging-hypervolt-2", "Hypervolt, hidden cable entry"), ("vans-fleet", "Our all-electric vans")]
    gal = "".join(f'<figure class="rv"><img src="assets/img/{f}.jpg" alt="{c}" loading="lazy"><figcaption>{c}</figcaption></figure>' for f, c in photos)
    body = f'''{phero("Our Work", "Recent installations", "Neat. Tidy. Built to last.",
        "A selection of recent EV charger, solar and battery installations by our team across Brighton and the South East.", "hero-2")}
<section class="section"><div class="wrap"><div class="gallery">{gal}</div></div></section>
{reviews_marquee("Our customers say it best")}
{quote_section()}'''
    page("our-work.html", "Our Work | EV Charger, Solar & Battery Installations | EVelec",
         "Recent EV charger, solar PV and battery storage installations by EVelec across Brighton, Sussex and the South East.", body, "home-charging-porsche-andersen")

def build_reviews():
    grid = "".join(rcard(r) for r in REVIEWS)
    body = f'''{phero("Reviews", "Rated 5.0 on Google", f"{C['review_count']} five-star reviews",
        "We're proud of every single one. Here's a selection of what our customers say about working with us.", "hero-3")}
<section class="section"><div class="wrap">
  <div class="head-row"><div class="head rv"><h2>What our customers say</h2></div>
  <a class="rev-summary rv d1" href="{C["google"]}" target="_blank" rel="noopener" style="text-decoration:none;color:inherit"><span class="g">{GOOGLE}</span><span class="big">5.0</span><span><span class="stars">★★★★★</span><small><b>{C["review_count"]}</b> reviews on Google</small></span></a></div>
  <div class="rgrid">{grid}</div>
  <div style="text-align:center;margin-top:44px"><a class="btn btn-dark" href="{C["google"]}" target="_blank" rel="noopener">Read all reviews on Google <span class="arr" style="background:rgba(255,255,255,.15)">{ic("arrow-ur")}</span></a></div>
</div></section>
{quote_section("Join our happy customers")}'''
    page("reviews.html", "Reviews | 224 Five-Star Google Reviews | EVelec",
         "Read what customers say about EVelec's EV charger, solar and battery installations: 224 five-star reviews on Google.", body)

def build_about():
    team = [("C", "Chris", "Surveys &amp; quotes"), ("M", "Mark", "Installation engineer"), ("A", "Alex", "Installation engineer"),
            ("T", "Tom", "Installation engineer"), ("S", "Sonny", "Installation engineer")]
    tm = "".join(f'<div class="rv"><span class="av">{a}</span><b>{n}</b><small>{r}</small></div>' for a, n, r in team)
    body = f'''{phero("About", "About EVelec", "Passionate about EV technology",
        "EVelec is the leading installer of EV charge points for homes, residential and apartment blocks, and businesses in Brighton, covering the whole of Sussex, Surrey, Hampshire and Kent.", "hero-2")}
<section class="section"><div class="wrap split">
  <div class="rv"><div class="pill-label">Who we are</div><h2>Installations we'd be proud to have at home</h2>
    <p class="lead">Our engineers have extensive experience in domestic and commercial electrical work and hold the latest qualifications and accreditations for EV installations.</p>
    <p>Our customers in Brighton, Sussex and across the South East know we know our stuff. We're passionate about EV technology and committed to the highest quality installations, ones we'd be proud to have in our own homes and workplaces.</p>
    <p>EVelec Ltd is fully qualified and insured to install Solar PV and battery storage, from small domestic systems to larger commercial premises. We help customers take the worry out of high energy bills and harness the power and convenience of renewable energy.</p></div>
  <div class="duo rv d1"><img src="assets/img/vans-fleet.jpg" alt="EVelec's all-electric vans" loading="lazy"><img src="assets/img/vans-on-site.jpg" alt="EVelec vans on a customer's driveway" loading="lazy"></div>
</div></section>
<section class="section white"><div class="wrap">
  <div class="head center rv"><div class="pill-label">Accredited &amp; insured</div><h2>Qualified to the highest standards</h2></div>
  <div class="grid g4">
    <div class="card rv"><div class="ic">{ic("shield")}</div><h3>OZEV Approved Installer</h3><p>Approved to install grant-funded home and workplace charge points.</p></div>
    <div class="card rv d1"><div class="ic">{ic("check")}</div><h3>NICEIC Approved Contractor</h3><p>Work regularly assessed to NICEIC standards for safety and quality.</p></div>
    <div class="card rv d2"><div class="ic">{ic("clipboard")}</div><h3>City &amp; Guilds</h3><p>Engineers trained and qualified to City &amp; Guilds standards.</p></div>
    <div class="card rv d3"><div class="ic">{ic("dial")}</div><h3>Nest Pro Installers</h3><p>Trained to install Nest products in homes and businesses.</p></div>
  </div>
</div></section>
<section class="section"><div class="wrap">
  <div class="head center rv"><div class="pill-label">The team</div><h2>The people you'll meet</h2><p class="lead">Names our customers mention again and again in their reviews.</p></div>
  <div class="team">{tm}</div>
</div></section>
{reviews_marquee("Why customers choose EVelec")}
{quote_section()}'''
    page("about.html", "About EVelec | EV, Solar & Battery Installers in Brighton",
         "EVelec is the leading installer of EV charge points, Solar PV and battery storage in Brighton, covering Sussex, Surrey, Hampshire and Kent.", body, "vans-fleet")

def build_contact():
    body = f'''{phero("Contact", "Get in touch", "Let's talk about your project",
        "Call, email or send us a few details below. We'll arrange a free site survey and a clear, no-obligation quote.", "hero-3")}
{quote_section("Request your free quote")}'''
    page("contact.html", "Contact EVelec | Free EV Charger, Solar & Battery Quotes | 01273 983951",
         "Contact EVelec for a free quote on EV charge points, Solar PV, battery storage and electrical services across Brighton, Sussex and the South East.", body)

if __name__ == "__main__":
    for fn in [build_home, build_ev, build_ozev, build_solar, build_battery, build_electrical, build_work, build_reviews, build_about, build_contact]:
        fn()
    print("Built:", ", ".join(sorted(p.name for p in OUT.glob("*.html"))))
