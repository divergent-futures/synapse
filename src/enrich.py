# -*- coding: utf-8 -*-
# Curated v0.2 enrichment for Open Sauce 2026 makers, keyed by EXACT exhibitor
# name (must match os2026-exhibitors-raw.tsv). Every field is optional; the app
# renders only what is present, so the long tail can stay empty.
#
# Guardrails (see BUILD-GUARDRAILS.md):
#   - Public profile/website links ONLY. Instagram is stored as a profile URL
#     under kind "instagram_profile" and is NEVER scraped or photo-embedded.
#   - The four Divergent Futures themes are the channel lens only — never a
#     per-maker rating, so they never appear here.
#   - Descriptions/affiliations/locations below are derived from the public
#     Open Sauce exhibits page and the exhibitor's own public profiles.
#   - Every external URL here was checked to resolve (HTTP 200) at build-authoring
#     time. Links kept intentionally to public front doors, not deep content.
#
# link kinds: website youtube instagram_profile github tiktok x patreon
#             kickstarter store linkedin other
#
# Shape per entry (all keys optional) — see synapse-interchange-v0.2.json.

def _os2026(showed, booth=None):
    return [{"year": 2026, "event": "Open Sauce", "showed": showed, "booth": booth}]

ENRICH = {
 # ---- makers with verified public links -----------------------------------
 "Linus Tech Tips": {
   "project": "The internet's biggest tech channel, live on the Open Sauce floor.",
   "description": "Linus Media Group brings its tech-review and maker-experiment operation to the show — hardware demos, meet-and-greets, and the crew behind one of the largest technology channels online.",
   "tags": ["creator", "tech media", "hardware", "reviews"],
   "is_public_figure": True,
   "location": {"country": "CA", "region": "British Columbia"},
   "links": [
     {"label": "YouTube", "url": "https://www.youtube.com/@LinusTechTips", "kind": "youtube"},
     {"label": "Linus Media Group", "url": "https://linusmediagroup.com/", "kind": "website"},
     {"label": "X", "url": "https://x.com/linustech", "kind": "x"},
   ],
   "entrepreneurship_signals": {"has_business": True, "for_sale": True, "hiring": True},
   "history": _os2026("Tech demos and creator meet-up"),
 },
 "The World's Most Advanced Pokedex": {
   "project": "A functional, AI-powered Pokedex build by maker-YouTuber BigRig Creates.",
   "description": "BigRig Creates turns the Pokedex from prop into working device — computer vision, custom electronics and a lot of overengineering, documented on his channel.",
   "tags": ["AI", "computer vision", "props", "creator"],
   "is_public_figure": True,
   "links": [
     {"label": "YouTube", "url": "https://www.youtube.com/@BigRigCreates", "kind": "youtube"},
     {"label": "X", "url": "https://x.com/BigRigCreates", "kind": "x"},
   ],
   "history": _os2026("The World's Most Advanced Pokedex"),
 },
 "Electronic Frontier Foundation (EFF)": {
   "project": "Digital rights on the maker floor — privacy, right-to-repair and free expression.",
   "description": "The EFF is the leading nonprofit defending civil liberties in the digital world. At a maker event they connect the room to right-to-repair, open hardware and privacy work.",
   "tags": ["digital rights", "right to repair", "privacy", "nonprofit"],
   "location": {"city": "San Francisco", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "company", "name": "Electronic Frontier Foundation", "url": "https://www.eff.org/"}],
   "links": [
     {"label": "Website", "url": "https://www.eff.org/", "kind": "website"},
     {"label": "X", "url": "https://x.com/EFF", "kind": "x"},
   ],
   "history": _os2026("Digital-rights outreach and right-to-repair advocacy"),
 },
 "NASA": {
   "project": "NASA's Ames Research Center — aeronautics, space science and exploration tech.",
   "description": "Ames, in Silicon Valley, is one of NASA's most research-heavy centers: aeronautics, astrobiology, small spacecraft and supercomputing. A direct line from the maker floor to the agency.",
   "tags": ["space", "aeronautics", "research", "government"],
   "location": {"city": "Mountain View", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "lab", "name": "NASA Ames Research Center", "url": "https://www.nasa.gov/ames/"}],
   "links": [
     {"label": "NASA Ames", "url": "https://www.nasa.gov/ames/", "kind": "website"},
   ],
   "history": _os2026("Ames Research Center outreach"),
 },
 "Hacker Dojo": {
   "project": "Silicon Valley's community hackerspace and makerspace.",
   "description": "A nonprofit community space in Mountain View where makers, founders and hackers build, learn and host events. A model for the local makerspace ecosystem.",
   "tags": ["makerspace", "community", "nonprofit", "hackerspace"],
   "location": {"city": "Mountain View", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "club", "name": "Hacker Dojo", "url": "https://hackerdojo.org/"}],
   "links": [
     {"label": "Website", "url": "https://hackerdojo.org/", "kind": "website"},
   ],
   "entrepreneurship_signals": {"has_business": True},
   "history": _os2026("Community makerspace showcase"),
 },
 "Bottango: DIY Animatronics": {
   "project": "Software that makes animatronics accessible — drive servos and motors with a visual timeline.",
   "description": "Bottango is a free-to-start toolkit for controlling animatronics and robotics: a visual keyframe editor that drives real hardware, so cosplayers and makers can bring builds to life without deep firmware work.",
   "tags": ["animatronics", "software", "robotics", "servos"],
   "links": [
     {"label": "Website", "url": "https://www.bottango.com/", "kind": "website"},
   ],
   "entrepreneurship_signals": {"has_business": True, "for_sale": True},
   "history": _os2026("DIY animatronics control software"),
 },
 "tscircuit - Design Electronics with React": {
   "project": "Design electronics as code — describe circuits in React/TypeScript and get real PCBs.",
   "description": "tscircuit is an open-source stack for electronics-as-code: express a board with React components, auto-layout and route it, and export for fabrication. It collapses the gap between software developers and hardware.",
   "tags": ["EDA", "open source", "PCB", "developer tools", "react"],
   "links": [
     {"label": "Website", "url": "https://tscircuit.com/", "kind": "website"},
     {"label": "GitHub", "url": "https://github.com/tscircuit", "kind": "github"},
   ],
   "external_ids": {"github": "tscircuit"},
   "entrepreneurship_signals": {"has_business": True},
   "history": _os2026("Electronics-as-code demo"),
 },
 "Positron 3D x LDO": {
   "project": "Upside-down, high-speed resin-quality FDM printing — with LDO Motors.",
   "description": "Positron builds an unusual inverted 3D printer aimed at portability and print quality, shown alongside LDO Motion, a maker-favorite supplier of stepper motors and printer components.",
   "tags": ["3D printing", "open hardware", "FDM", "for sale"],
   "links": [
     {"label": "Positron 3D", "url": "https://positron3d.com/", "kind": "website"},
     {"label": "LDO Motion", "url": "https://ldomotion.com/", "kind": "website"},
   ],
   "entrepreneurship_signals": {"has_business": True, "for_sale": True},
   "history": _os2026("Positron inverted 3D printer with LDO"),
 },
 "DIY Satellite Antennas": {
   "project": "Pulling images and signals from space with salvaged and homemade antennas.",
   "description": "Saveitforparts documents receiving weather-satellite images, tracking spacecraft and building ground stations from surplus and DIY hardware — accessible space signal reception for anyone.",
   "tags": ["space", "RF", "antennas", "salvage", "creator"],
   "is_public_figure": True,
   "links": [
     {"label": "YouTube", "url": "https://www.youtube.com/@saveitforparts", "kind": "youtube"},
   ],
   "history": _os2026("DIY satellite ground-station antennas"),
 },
 "Attoparsec: Technical art for curious people": {
   "project": "Kinetic and technical art — mechanisms, instruments and beautifully odd machines.",
   "description": "Matthew 'Fish' Dockrey builds technical art: mechanical curiosities, custom instruments and kinetic sculpture, explained with an engineer's clarity on the Attoparsec channel.",
   "tags": ["kinetic art", "mechanisms", "creator", "instruments"],
   "is_public_figure": True,
   "location": {"state": "WA", "country": "US"},
   "links": [
     {"label": "Website", "url": "https://www.attoparsec.com/", "kind": "website"},
     {"label": "YouTube", "url": "https://www.youtube.com/channel/UCUtVZ70RhZBnH1NS9oyZvpA", "kind": "youtube"},
   ],
   "history": _os2026("Technical art and kinetic mechanisms"),
 },
 "CuriousMarc Vintage Electronics Restorations": {
   "project": "Restoring Apollo-era and vintage computing hardware to working order.",
   "description": "CuriousMarc and collaborators restore historic electronics — Apollo Guidance Computers, vintage calculators and lab gear — reverse-engineering and reviving hardware most museums only display.",
   "tags": ["restoration", "vintage computing", "electronics", "creator"],
   "is_public_figure": True,
   "location": {"state": "CA", "country": "US", "region": "Bay Area"},
   "links": [
     {"label": "YouTube", "url": "https://www.youtube.com/@CuriousMarc", "kind": "youtube"},
     {"label": "Website", "url": "https://www.curiousmarc.com/", "kind": "website"},
     {"label": "Patreon", "url": "https://www.patreon.com/curiousmarc", "kind": "patreon"},
   ],
   "history": _os2026("Vintage electronics restoration"),
 },
 "Prospecting the Stars - Space Enterprise at Berkeley": {
   "project": "UC Berkeley students building liquid-fuel rockets aiming for space.",
   "description": "Space Enterprise at Berkeley is a student group designing and flying increasingly capable liquid-bipropellant rockets, with the long-term goal of reaching the Karman line — a serious collegiate aerospace pipeline.",
   "tags": ["rocketry", "aerospace", "student team", "liquid propulsion"],
   "location": {"city": "Berkeley", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "university", "name": "UC Berkeley — Space Enterprise at Berkeley", "url": "https://www.berkeleyse.org/"}],
   "links": [
     {"label": "Website", "url": "https://www.berkeleyse.org/", "kind": "website"},
   ],
   "history": _os2026("Student liquid-fuel rocketry program"),
 },
 "Mosi Audio - MIDI Guitars and more": {
   "project": "MIDI guitars and instrument tech for players who want to trigger anything.",
   "description": "Mosi Audio builds MIDI-guitar hardware and related music-tech products, turning a guitar into a controller for synths, samplers and software.",
   "tags": ["music tech", "MIDI", "instruments", "for sale"],
   "links": [
     {"label": "Website", "url": "https://mosiaudio.com/", "kind": "website"},
     {"label": "YouTube", "url": "https://www.youtube.com/c/MosiAudio", "kind": "youtube"},
     {"label": "TikTok", "url": "https://www.tiktok.com/@mosiaudio", "kind": "tiktok"},
   ],
   "entrepreneurship_signals": {"has_business": True, "for_sale": True},
   "history": _os2026("MIDI guitars and music-tech products"),
 },
 "Bringing Robots to Life - Semio Community": {
   "project": "Tools and community for building social and interactive robots.",
   "description": "Semio focuses on the software and community around social robotics — giving makers a path to build robots that interact with people, not just move.",
   "tags": ["robotics", "social robots", "community", "software"],
   "links": [
     {"label": "Semio Community", "url": "https://semio.community/", "kind": "website"},
   ],
   "history": _os2026("Social robotics tools and community"),
 },
 "Vinylessence: World's First Smart LED Vinyl Slipmat": {
   "project": "A smart LED slipmat that reacts on the turntable.",
   "description": "Vinylessence is a lit, reactive slipmat for record players — a small piece of consumer hardware that brought its idea to crowdfunding and a public launch.",
   "tags": ["consumer hardware", "LED", "music", "crowdfunding"],
   "links": [
     {"label": "Website", "url": "https://www.vinyl-essence.com/", "kind": "website"},
     {"label": "Kickstarter", "url": "https://www.kickstarter.com/projects/vinylessence/vinylessence-smart-led-vinyl-slipmat-for-turntables", "kind": "kickstarter"},
     {"label": "YouTube", "url": "https://www.youtube.com/@OfficialVinylessence", "kind": "youtube"},
   ],
   "entrepreneurship_signals": {"has_business": True, "for_sale": True, "crowdfunding": "Kickstarter"},
   "history": _os2026("Smart LED vinyl slipmat"),
 },
 "Iron Panthers Robotics": {
   "project": "FIRST Robotics Competition team 5026, competing and mentoring in the Bay Area.",
   "description": "The Iron Panthers are a well-established FRC team (5026) out of the Peninsula, known for strong engineering and outreach — a template for how student robotics teams grow talent.",
   "tags": ["FRC", "student team", "robotics", "STEM"],
   "location": {"city": "Burlingame", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "team", "name": "FRC Team 5026 — Iron Panthers", "url": "https://ironpanthers.com/"}],
   "links": [
     {"label": "Website", "url": "https://ironpanthers.com/", "kind": "website"},
     {"label": "GitHub", "url": "https://github.com/iron-panthers", "kind": "github"},
   ],
   "history": _os2026("FRC robot demonstration"),
 },

 # ---- data-derived enrichment (affiliation/location/tags from public data) --
 "Saddleback Rocketry - Argo Barracuda": {
   "project": "Argo Barracuda — a student-built high-power competition rocket.",
   "description": "A collegiate rocketry team flying Argo Barracuda, a student-designed high-power rocket built for intercollegiate competition and hands-on aerospace training.",
   "tags": ["rocketry", "student team", "aerospace", "high-power"],
   "location": {"state": "CA", "country": "US"},
   "affiliations": [{"type": "university", "name": "Saddleback College Rocketry", "url": None}],
   "history": _os2026("Argo Barracuda high-power rocket"),
 },
 "Exo Bronco Two Stage Rocket - Cal Poly Pomona": {
   "project": "Exo Bronco — a two-stage rocket from Cal Poly Pomona.",
   "description": "A student team from Cal Poly Pomona showing Exo Bronco, a two-stage rocket — staging, recovery and avionics built as a learn-by-launching aerospace project.",
   "tags": ["rocketry", "two-stage", "student team", "aerospace"],
   "location": {"city": "Pomona", "state": "CA", "country": "US"},
   "affiliations": [{"type": "university", "name": "Cal Poly Pomona", "url": None}],
   "history": _os2026("Exo Bronco two-stage rocket"),
 },
 "Menlo-Atherton High School FRC Team 766 M-A Bears": {
   "project": "FRC Team 766, the M-A Bears — high-school competitive robotics.",
   "description": "A veteran high-school FIRST Robotics team building competition robots and pulling younger students into serious engineering.",
   "tags": ["FRC", "high school", "robotics", "STEM"],
   "location": {"city": "Atherton", "state": "CA", "country": "US", "region": "Bay Area"},
   "affiliations": [{"type": "school", "name": "Menlo-Atherton High School — FRC 766", "url": None}],
   "history": _os2026("FRC Team 766 robot"),
 },
 "Sacramento State Competitive Robotics": {
   "project": "University competitive-robotics team from Sacramento State.",
   "description": "A Sacramento State student club building competition robots — a regional pipeline for combat and competitive robotics talent.",
   "tags": ["robotics", "student team", "combat robotics", "STEM"],
   "location": {"city": "Sacramento", "state": "CA", "country": "US"},
   "affiliations": [{"type": "university", "name": "California State University, Sacramento", "url": None}],
   "history": _os2026("Competitive robotics demos"),
 },
 "Getting Started in Combat Robotics - Backslash Robotics Chico State AIME": {
   "project": "An on-ramp to combat robotics, from Chico State's AIME / Backslash Robotics.",
   "description": "A student club demystifying how to start in combat robotics — safety, weapons, drivetrains and getting your first bot into the arena.",
   "tags": ["combat robotics", "student team", "education", "STEM"],
   "location": {"city": "Chico", "state": "CA", "country": "US"},
   "affiliations": [{"type": "university", "name": "Chico State — AIME / Backslash Robotics", "url": None}],
   "history": _os2026("Intro to combat robotics"),
 },
 "Sierra College Robotics Club Demos": {
   "project": "Community-college robotics club demonstrations.",
   "description": "Sierra College's robotics club showing student builds — proof that serious robotics work happens at community colleges, not just universities.",
   "tags": ["robotics", "student team", "community college", "STEM"],
   "location": {"city": "Rocklin", "state": "CA", "country": "US"},
   "affiliations": [{"type": "university", "name": "Sierra College Robotics Club", "url": None}],
   "history": _os2026("Robotics club demonstrations"),
 },
 "MOSMAGE: Modular Open-Source Automated Genome Engineering": {
   "project": "Open-source automated genome engineering, from the uLethbridge iGEM team.",
   "description": "A student synthetic-biology team building modular, open-source automation for genome engineering — lowering the cost of real molecular biology work.",
   "tags": ["synthetic biology", "open source", "automation", "student team"],
   "location": {"city": "Lethbridge", "state": "AB", "country": "CA"},
   "affiliations": [{"type": "university", "name": "University of Lethbridge iGEM", "url": None}],
   "history": _os2026("Modular open-source genome engineering"),
 },
 "CSH Devcade: Custom Arcade Cabinet": {
   "project": "A student-built arcade cabinet with a homebrew game library.",
   "description": "From Computer Science House at RIT: a custom arcade cabinet running student-made games — a community hardware + software project.",
   "tags": ["arcade", "student team", "hardware", "games"],
   "location": {"city": "Rochester", "state": "NY", "country": "US"},
   "affiliations": [{"type": "club", "name": "Computer Science House @ RIT", "url": None}],
   "history": _os2026("Devcade custom arcade cabinet"),
 },
 "CSH Caption Glasses": {
   "project": "Live-captioning smart glasses for accessibility.",
   "description": "A Computer Science House project putting real-time captions in the wearer's view — an accessibility-focused take on smart eyewear.",
   "tags": ["accessibility", "wearable", "AR", "student team"],
   "location": {"city": "Rochester", "state": "NY", "country": "US"},
   "affiliations": [{"type": "club", "name": "Computer Science House @ RIT", "url": None}],
   "history": _os2026("Live-captioning glasses"),
 },
 "CSH Bits 'n Bytes: AI Vision Smart Vending": {
   "project": "A smart vending machine using AI vision.",
   "description": "Computer Science House's AI-vision vending build — computer vision applied to a real, always-on piece of hardware.",
   "tags": ["AI", "computer vision", "vending", "student team"],
   "location": {"city": "Rochester", "state": "NY", "country": "US"},
   "affiliations": [{"type": "club", "name": "Computer Science House @ RIT", "url": None}],
   "history": _os2026("AI-vision smart vending"),
 },
 "CSH KILOBYTE: Motorized Shopping Cart": {
   "project": "A motorized, rideable shopping cart.",
   "description": "A playful Computer Science House vehicle build — a motorized shopping cart that is exactly as fun and as questionable as it sounds.",
   "tags": ["vehicle", "student team", "hardware", "for fun"],
   "location": {"city": "Rochester", "state": "NY", "country": "US"},
   "affiliations": [{"type": "club", "name": "Computer Science House @ RIT", "url": None}],
   "history": _os2026("Motorized shopping cart"),
 },
 "Oak Park Mechatronics Class": {
   "project": "A high-school mechatronics class showing student projects.",
   "description": "Student mechatronics work from a high-school program — the earliest end of the maker pipeline, where robotics and electronics first click.",
   "tags": ["mechatronics", "high school", "education", "STEM"],
   "location": {"state": "CA", "country": "US"},
   "affiliations": [{"type": "school", "name": "Oak Park High School — Mechatronics", "url": None}],
   "history": _os2026("Student mechatronics projects"),
 },
 "SF-HAB: High Altitude Ballooning in the Bay Area": {
   "project": "Near-space high-altitude balloon flights out of the Bay Area.",
   "description": "SF-HAB flies high-altitude balloons to the edge of space, handling tracking, recovery and payloads — accessible near-space access for makers.",
   "tags": ["high-altitude balloon", "near space", "tracking", "community"],
   "location": {"state": "CA", "country": "US", "region": "Bay Area"},
   "history": _os2026("High-altitude balloon flights"),
 },
 "Tombstone BattleBot": {
   "project": "Tombstone — the legendary heavyweight BattleBot from Ray Billings.",
   "description": "One of the most feared heavyweight bots in BattleBots history, Tombstone is a horizontal-spinner built by Ray Billings (Hardcore Robotics) — a benchmark for combat-robot design.",
   "tags": ["combat robotics", "BattleBots", "heavyweight", "spinner"],
   "is_public_figure": True,
   "history": _os2026("Tombstone heavyweight combat robot"),
 },
 "Gigabyte The Battlebot": {
   "project": "Gigabyte — a full-body-spinner combat robot.",
   "description": "A shell-spinner combat robot bringing serious kinetic energy to the arena — the kind of build that draws crowds at any robot-fight event.",
   "tags": ["combat robotics", "BattleBots", "spinner"],
   "history": _os2026("Gigabyte full-body-spinner bot"),
 },
 "Open-source Layerless 3D Printing, OpenCAL": {
   "project": "OpenCAL — open-source layerless (computed axial lithography) 3D printing.",
   "description": "From a nanomanufacturing research lab: an open-source take on layerless resin printing, where a whole object cures at once from projected light instead of building up layer by layer.",
   "tags": ["3D printing", "open source", "research", "CAL"],
   "affiliations": [{"type": "lab", "name": "Design for Nanomanufacturing Lab", "url": None}],
   "history": _os2026("OpenCAL layerless 3D printing"),
 },
}
