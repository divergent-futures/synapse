import csv, json, os, re
BASE=os.path.dirname(os.path.abspath(__file__))
ROOT=os.path.dirname(BASE)
TSV=os.path.join(ROOT,"os2026-exhibitors-raw.tsv")
OUT=os.path.join(ROOT,"Synapse-OS2026-App.html")

# --- v0.2 data model -------------------------------------------------------
# Each exhibitor is emitted with the compact base keys the app has always used
# (n=name, m=maker, c=category) plus an id, plus any OPTIONAL v0.2 fields that
# have been enriched for that maker. Empty optional fields are dropped so the
# ~225 base records stay tiny; the app renders only what is present.
#   v0.2 optional fields (see synapse-interchange-v0.2.json):
#   project, description, tags[], location{}, affiliations[], links[],
#   entrepreneurship_signals{}, history[], external_ids{}, is_public_figure
# Guardrail: links are PUBLIC profile/website URLs only. Instagram is stored as
# a profile URL and never scraped/embedded.

def slug(s):
    s=re.sub(r"[^a-z0-9]+","-",(s or "").lower()).strip("-")
    return "os2026-"+(s or "x")

from enrich import ENRICH  # curated per-maker v0.2 fields, keyed by exact name

OPT_KEYS=("project","description","tags","location","affiliations","links",
          "entrepreneurship_signals","history","external_ids")

def record(x):
    n=x["name"].strip(); m=x["maker"].strip(); c=x["auto_category"].strip()
    r={"n":n,"m":m,"c":c,"id":slug(n)}
    en=ENRICH.get(n)
    if en:
        for k in OPT_KEYS:
            v=en.get(k)
            if v: r[k]=v
        if en.get("is_public_figure"): r["is_public_figure"]=True
    return r

rows=[]
with open(TSV,encoding="utf-8") as f:
    for x in csv.DictReader(f,delimiter="\t"):
        rows.append(record(x))

FIELDS=[
 ("Robotics and Automation","Industrial automation; warehouse & logistics; agtech; humanoid & service robots; defense","Boston Dynamics; Agility Robotics; Figure; iRobot; ABB; FANUC; Universal Robots; Amazon Robotics","MassRobotics residency; HAX (SOSV); SBIR/STTR (NSF, DoD)","Drover Labs; NestWorks; Pantheon Design; Vision Miner; Seeed; Raspberry Pi"),
 ("Combat Robotics","Sports & live entertainment; STEM education; R&D machining & materials","BattleBots; NHRL / NHRL Pro Tour; RoboGames; Bright Data","NHRL Pro Tour sponsorship; BattleBots casting; team sponsorship proposals","Ultimate Bots; PCBWay; OSH Cut; Chomp Shop"),
 ("Electronics and Hardware","Consumer electronics; IoT; contract manufacturing; EDA & test","SparkFun; Adafruit; Digi-Key; Espressif; Nordic; Analog Devices; TI","Crowd Supply (open hardware); SBIR/STTR; HAX","PCBWay; Seeed; Elegoo; Raspberry Pi; Framework; iFixit; OSH Cut"),
 ("Software AI and Computing","AI / ML; developer tools; robotics & embedded software; simulation","NVIDIA; Hugging Face; Scale AI; Roboflow; Unity; Unreal","Techstars AI; SBIR/STTR (NSF AI); YC; Boot.dev pipeline","Boot.dev; Drover Labs; Raven Resonance; NestWorks; YouTube"),
 ("Rocketry Space and Aero","Launch & satellites; drones & UAS; defense; ground systems","SpaceX; Rocket Lab; Firefly; Blue Origin; Relativity; Skydio; Anduril","Base 11; Spaceport America Cup; NASA SBIR/STTR; Techstars Space","Firefly Aerospace; Reflect Orbital; Zipline; Wing"),
 ("Fabrication and 3D Printing","Additive manufacturing; rapid prototyping services; tooling","Bambu Lab; Markforged; Xometry; Protolabs; Desktop Metal","Crowd Supply; SBIR (advanced mfg); state mfg grants","Prusa; Formlabs; Makera; xTool; Vision Miner; Elegoo; OSH Cut; ACCELaser"),
 ("Games and Interactive","Game studios & publishers; engines; location-based entertainment","Devolver; Annapurna; Raw Fury; Team17; Valve/Steam; Xbox","Epic MegaGrants ($5K-150K); WINGS (to $500K); ID@Xbox; Indie Fund; Kickstarter","YouTube; Crunch Labs; Kickstarter"),
 ("Music and Audio","Music technology; instruments; pro audio; audio DSP","Teenage Engineering; Ableton; Moog; Roland; Native Instruments; Focusrite","Crowd Supply; Kickstarter (strong music-tech track record); NAMM","Seeed; Raven Resonance"),
 ("Art Light and Sculpture","Experiential & themed entertainment; public art; festivals","Meow Wolf; teamLab; Two Bit Circus; museums; municipal art programs","NEA / state arts council; Burning Man Honoraria; Kickstarter","xTool; Formlabs; Makera"),
 ("Bio Medical and Wearable","Medtech; assistive & accessibility tech; consumer wearables","Medtronic; Open Bionics; Cala Health; Whoop; Dexcom; Ottobock","NIH SBIR/STTR; HAX health; accessibility grants (state + federal)","iFixit; (HAX health track)"),
 ("Education and STEM","Edtech; STEM kits & curriculum; schools & universities; museums","Sphero; Arduino Education; LEGO Education; Raspberry Pi Foundation","NSF DRK-12 & ITEST; DonorsChoose; state STEM grants","Crunch Labs; Boot.dev; Raspberry Pi; YouTube"),
 ("Cameras and Imaging","Imaging & optics; computational photography; cine & broadcast","Sony; Blackmagic; RED; Teledyne; Sigma; Insta360","Crowd Supply; Kickstarter; SBIR (sensors)","(route via Electronics)"),
 ("Cosplay Textiles Inflatables","Costuming & props; film & themed entertainment; maker retail","WETA Workshop; Punished Props; Etsy; convention circuit","Etsy sales; Patreon; Kickstarter; commissions","xTool; Formlabs"),
 ("Vehicles and Transport","EV & micromobility; automotive; personal mobility","Rivian (talent); Super73; Arcimoto; Onewheel","SBIR (DOE/DOT); state clean-transport grants; Kickstarter","(route via Electronics / Fabrication)"),
 ("Science and Physics","Research instruments; national labs; science outreach","Backyard Brains; Public Lab; national labs; Thorlabs","NSF; DOE; Moore / Sloan grants; SBIR","(route via Electronics / Education)"),
 ("Toys Kinetics and Puzzles","Toy & tabletop industry; collectibles; kinetic design","Hasbro; Spin Master; Goliath; tabletop publishers","Kickstarter / Gamefound (tabletop is huge); toy licensing","Kickstarter; Elegoo; Prusa"),
 ("Community and Makerspace","Makerspaces & hackerspaces; right-to-repair; civic tech","Nation of Makers; iFixit; EFF; Hacker Dojo; libraries","Nonprofit grants; Awesome Foundation; library partnerships","iFixit; Kickstarter"),
 ("Media and Creators","Creator economy; media & publishing; edutainment","YouTube; Nebula; Patreon; creator networks","YouTube programs; Patreon; brand sponsorships","YouTube; Crunch Labs"),
]
fields=[{"f":a,"ind":b,"co":c,"fund":d,"spon":e} for a,b,c,d,e in FIELDS]

CONV=[
 {"t":"Student ground-to-space telemetry","a":"Saddleback Rocketry","b":"DIY Satellite Antennas + ADSBee + Magnoplotter","i":"Amateur rocket & drone teams gain a shared long-range tracking and downlink stack from surplus parts.","p":"green","o":"Firefly Aerospace, Space Enterprise @ Berkeley, aero grants","fl":["Rocketry Space and Aero","Electronics and Hardware"]},
 {"t":"Open assistive-tech suite","a":"Hear us R.O.A.R.","b":"Range of Motion Device + Adaptive Tech Club + Haptic Gloves","i":"A modular open hardware kit for accessibility — comms, motion and haptic feedback any maker or clinic can build.","p":"green","o":"Accessibility grants (state+federal), medical-device partners, iFixit","fl":["Bio Medical and Wearable","Education and STEM","Robotics and Automation"]},
 {"t":"Distributed open manufacturing","a":"WorkCell autonomous printing","b":"Positron 3D + OpenCAL Layerless + DIY Micro 3D Printers","i":"A networked self-running print farm from open parts — factory-scale output without factory capital.","p":"green","o":"Formlabs / Makera / Prusa, small-business mfg grants","fl":["Fabrication and 3D Printing","Robotics and Automation"]},
 {"t":"AI-assisted hardware design","a":"tscircuit","b":"CaDoodle CAD + Vibeengineering","i":"Describe a board in plain language, auto-route it, get it fabbed — collapses the idea-to-PCB gap.","p":"green","o":"PCBWay / Seeed, dev-tool startups, Kickstarter","fl":["Software AI and Computing","Electronics and Hardware"]},
 {"t":"Combat-robotics league & curriculum","a":"Tombstone BattleBot","b":"Gigabyte + Malice + Team Exile + Experimental Division","i":"A standardized build-fight-teach circuit turns scattered teams into a franchise-able league with an education on-ramp.","p":"green","o":"Ultimate Bots, schools & universities, ticketed events","fl":["Combat Robotics","Education and STEM"]},
 {"t":"Wearable AI vision stack","a":"Visionary AI Glasses","b":"CSH Caption Glasses + Auto Turret body-tracking","i":"A shared low-cost eyewear platform: captions, object ID and tracking — accessibility and AR from one open base.","p":"purple","o":"Accessibility funds, AR startups, semiconductor sponsors","fl":["Software AI and Computing","Bio Medical and Wearable"]},
 {"t":"Open electromechanical instruments","a":"Musical Floppy Drives","b":"Mechanical Pianical + Staccato 3D Piano + Lupine Drum Machine","i":"A common standard for robotic acoustic instruments — makers compose for real mechanical hardware.","p":"purple","o":"Music-tech, education, maker-kit sales","fl":["Music and Audio","Robotics and Automation"]},
 {"t":"Ambient data-display platform","a":"The Stock Orb","b":"EnergyMe Home + go fetch","i":"One open ambient-display framework across finance, energy and play — glanceable data objects for the home.","p":"orange","o":"Smart-home brands, prosumer kits","fl":["Art Light and Sculpture","Electronics and Hardware"]},
 {"t":"Backyard aerospace propulsion","a":"Rocket Powered Laser","b":"Multistage coilgun + Solar drone","i":"High-energy DIY propulsion & energy projects share safety, materials and regulatory hurdles — needs guardrails.","p":"red","o":"Safety review, insurers, regulated-industry mentors","fl":["Rocketry Space and Aero","Science and Physics"]},
 {"t":"Open science instrumentation","a":"X-ray Vision (crystallography)","b":"Ionic Film Diodes + Miniature Natural History Museum","i":"Low-cost open lab instruments make real science reproducible in classrooms and garages.","p":"green","o":"STEM education grants, university outreach, NASA Ames","fl":["Science and Physics","Education and STEM"]},
]
DATA=json.dumps({"ex":rows,"fields":fields,"conv":CONV},ensure_ascii=False)
Z=lambda s:s.replace("\x00","")
css=Z(open(BASE+"/app.css",encoding="utf-8").read())
mark=Z(open(BASE+"/brand.svg",encoding="utf-8").read())
js=Z(open(BASE+"/app.head.js",encoding="utf-8").read())+"\n"+Z(open(BASE+"/app.tail.js",encoding="utf-8").read())
HTML=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
 '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Synapse - Open Sauce 2026</title>'
 '<style>'+css+'</style></head><body><div class="wrap">'
 '<div class="top">'+mark+'<div><h1>Synapse · Open Sauce 2026</h1><p class="sub">The room seen whole — exhibitors, the industries around them, and the connections no single booth can see.</p></div></div>'
 '<div class="tabs" id="tabs"></div><div class="chips" id="chips"></div><div id="view"></div>'
 '<footer>Synapse — Divergent Futures · proof of concept. Data: Open Sauce 2026 public exhibits page (snapshot, ~<span id="fn"></span> exhibitors, list still growing). Categories auto-derived then cleaned. Region &amp; year layers scaffolded, fill in with official data.</footer>'
 '</div><script id="prism" type="application/json">'+DATA+'</script>'+'<script>'+js+'</script></body></html>')
open(OUT,"w",encoding="utf-8").write(HTML)
print("saved",OUT,len(rows))

# --- self-verify: build + check in one step ---
_h=open(OUT,'rb').read(); _nul=_h.count(b'\x00')
_t=_h.decode('utf-8','replace'); _i=_t.rfind('<script>'); _j=_t.rfind('</script>'); _js=_t[_i+8:_j]
import subprocess,tempfile,shutil,os as _os
_ok=None
if shutil.which('node'):
    _tmp=_os.path.join(tempfile.gettempdir(),'synapse_check.js'); open(_tmp,'w',encoding='utf-8').write(_js)
    _ok=(subprocess.run(['node','--check',_tmp],capture_output=True,text=True).returncode==0)
for _fn in ['landscape','exhibitors','network','opportunities','convergences']:
    assert ('function '+_fn) in _js, 'MISSING TAB: '+_fn
_pass=(_nul==0) and (_ok is not False)
print('VERIFY nul=%d js_parses=%s 5tabs=ok -> %s'%(_nul,('yes' if _ok else ('no' if _ok is not None else 'skip')),'PASS' if _pass else 'FAIL'))
