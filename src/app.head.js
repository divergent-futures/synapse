const D=JSON.parse(document.getElementById('prism').textContent);
const EX=D.ex, FL=D.fields, CV=D.conv;
EX.forEach((e,i)=>e._i=i);
const counts={}; EX.forEach(e=>counts[e.c]=(counts[e.c]||0)+1);
const order=FL.map(f=>f.f).filter(f=>counts[f]);
document.getElementById('fn').textContent=EX.length;
// --- personalization (Phase 3): prefs live in localStorage, fully optional ---
const PREF_KEY='synapse_prefs_v1', SEEN_KEY='synapse_ob_seen_v1';
const PERSONAS=[
 ['visitor','Visitor','Here for the day — who to meet, what to see.'],
 ['exhibitor','Exhibitor','I have a booth — collaborators and adjacent makers.'],
 ['sponsor','Industry / Sponsor','Scouting talent, partners and funding.'],
 ['explore','Just exploring','No agenda — surprise me with the good stuff.']];
function loadPrefs(){try{const p=JSON.parse(localStorage.getItem(PREF_KEY)||'null');if(p&&p.persona)return p;}catch(_){}return null;}
function savePrefs(p){try{localStorage.setItem(PREF_KEY,JSON.stringify(p));localStorage.setItem(SEEN_KEY,'1');}catch(_){}}
function onboardSeen(){try{return !!localStorage.getItem(SEEN_KEY);}catch(_){return false;}}
function markSeen(){try{localStorage.setItem(SEEN_KEY,'1');}catch(_){}}
const PREFS=loadPrefs();
let state={tab:(PREFS?'For You':'Landscape'),sel:new Set(PREFS?PREFS.interests:[]),ex:null,
 persona:(PREFS?PREFS.persona:null),interests:new Set(PREFS?PREFS.interests:[])};
const TABS=['For You','Landscape','Exhibitors','Network','Opportunities','Convergences'];
const tabsEl=document.getElementById('tabs'), chipsEl=document.getElementById('chips'), view=document.getElementById('view');
function esc(s){return (''+s).replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]));}
function inSel(c){return state.sel.size===0||state.sel.has(c);}
function toggle(f){if(f==='All'){state.sel.clear();}else{if(state.sel.has(f))state.sel.delete(f);else state.sel.add(f);}state.ex=null;}
function drawTabs(){tabsEl.innerHTML=TABS.map(t=>'<div class="tab '+(t===state.tab?'on':'')+'" data-t="'+t+'">'+t+'</div>').join('');
 tabsEl.querySelectorAll('.tab').forEach(e=>e.onclick=()=>{state.tab=e.dataset.t;state.ex=null;render();});}
function drawChips(){const chips=['All'].concat(order);
 chipsEl.innerHTML=chips.map(f=>{const on=f==='All'?state.sel.size===0:state.sel.has(f);return '<div class="chip '+(f==='All'?'all ':'')+(on?'on':'')+'" data-f="'+f+'">'+f+(f!=='All'?' - '+counts[f]:'')+'</div>';}).join('');
 chipsEl.querySelectorAll('.chip').forEach(e=>e.onclick=()=>{toggle(e.dataset.f);render();});}
function landscape(){const max=Math.max.apply(null,order.map(f=>counts[f]));
 let h='<div class="intro"><p><b>What this is.</b> Synapse maps everyone at a maker event and surfaces the connections no single booth can see - collaborators, industry and funding. Click a category bar below to drill into it, or use the tabs above.</p><p class="ithemes"><b>The lens.</b> Divergent Futures sees humanity move through a prism of decisions into four futures: great decisions bend toward <span class="tA">Abundance</span>, good toward <span class="tP">Progress</span>, ok toward <span class="tS">Stagnation</span>, poor toward <span class="tC">Collapse</span>. Synapse helps make the great ones - by connecting the room.</p></div><div class="stats"><div class="stat"><b>'+EX.length+'</b><span>exhibitors</span></div><div class="stat"><b>'+order.length+'</b><span>domains</span></div><div class="stat"><b>'+CV.length+'</b><span>convergences</span></div></div>';
 h+='<div class="bars">'+order.map(f=>'<div class="bar '+(state.sel.has(f)?'on':'')+'" data-f="'+f+'"><div class="lbl">'+f+'</div><div class="track"><div class="fill" style="width:'+Math.round(counts[f]/max*100)+'%"></div></div><div class="num">'+counts[f]+'</div></div>').join('')+'</div>';
 view.innerHTML=h;
 view.querySelectorAll('.bar').forEach(e=>e.onclick=()=>{state.sel=new Set([e.dataset.f]);state.ex=null;state.tab='Exhibitors';render();});}
// --- v0.2 people-centric helpers -----------------------------------------
const LINK_GLYPH={website:'◉',youtube:'▶',instagram_profile:'◎',github:'</>',tiktok:'♪',x:'✕',patreon:'♥',kickstarter:'⚡',store:'▲',linkedin:'in',other:'→'};
function linkList(e){return (e.links||[]).filter(l=>l&&l.url);}
function linksHTML(e){
 const ls=linkList(e); if(!ls.length)return '';
 return '<div class="links">'+ls.map(l=>{const g=LINK_GLYPH[l.kind]||LINK_GLYPH.other;
  return '<a class="lk lk-'+(l.kind||'other')+'" href="'+esc(l.url)+'" target="_blank" rel="noopener"><span class="lkg">'+g+'</span>'+esc(l.label||l.kind||'Link')+'</a>';}).join('')+'</div>';}
function tagsHTML(tags,extra){if(!tags||!tags.length)return '';return '<div class="tags">'+tags.map(t=>'<span class="tag'+(extra?' '+extra:'')+'">'+esc(t)+'</span>').join('')+'</div>';}
function isRich(e){return !!(e.description||e.project||linkList(e).length||(e.tags&&e.tags.length)||(e.affiliations&&e.affiliations.length)||(e.history&&e.history.length));}
function locHTML(l){if(!l)return '';const parts=[l.city,l.state,l.region,l.country].filter(Boolean);if(!parts.length)return '';return '<div class="k">Location</div><p>'+esc(parts.join(', '))+'</p>';}
function affHTML(a){if(!a||!a.length)return '';return '<div class="k">Affiliations</div><p>'+a.map(f=>{const nm=esc(f.name||'')+(f.type?' <span class="mut">· '+esc(f.type)+'</span>':'');return f.url?'<a class="lk lk-other" href="'+esc(f.url)+'" target="_blank" rel="noopener">'+esc(f.name||'')+'</a>':'<span class="tag">'+nm+'</span>';}).join(' ')+'</p>';}
function entHTML(s){if(!s)return '';const on=[];if(s.has_business)on.push('Business');if(s.for_sale)on.push('Product for sale');if(s.crowdfunding)on.push('Crowdfunding'+(typeof s.crowdfunding==='string'?' · '+s.crowdfunding:''));if(s.hiring)on.push('Hiring');if(s.patents_or_ip)on.push('Patents / IP');if(!on.length)return '';return '<div class="k">Entrepreneurship</div>'+tagsHTML(on,'ent');}
function histHTML(h){if(!h||!h.length)return '';return '<div class="k">History</div>'+h.map(y=>'<p class="hist"><b>'+esc(''+(y.year||''))+(y.event?' · '+esc(y.event):'')+'</b>'+(y.showed?' — '+esc(y.showed):'')+(y.booth?' <span class="mut">(booth '+esc(y.booth)+')</span>':'')+'</p>').join('');}
// fields that converge with a given field (from the convergence graph)
function bridgingFields(cat){const s=new Set();CV.forEach(c=>{if(c.fl.indexOf(cat)>=0)c.fl.forEach(f=>{if(f!==cat)s.add(f);});});return s;}
function meetRank(x,e){let s=0;if(isRich(x))s+=3;if(x.tags&&e.tags){const t=new Set(e.tags);x.tags.forEach(g=>{if(t.has(g))s+=2;});}if(linkList(x).length)s+=1;return s;}
function whoToMeet(e){
 const adj=bridgingFields(e.c),seen={},out=[];
 function push(x,why){if(x._i===e._i||seen[x._i])return;seen[x._i]=1;out.push({x:x,why:why});}
 const adjM=EX.filter(x=>x._i!==e._i&&adj.has(x.c)).sort((a,b)=>meetRank(b,e)-meetRank(a,e));
 adjM.forEach(x=>{if(out.length<4)push(x,'Bridges '+e.c.split(' ')[0]+' × '+x.c.split(' ')[0]);});
 if(out.length<3){EX.filter(x=>x._i!==e._i&&x.c===e.c).sort((a,b)=>meetRank(b,e)-meetRank(a,e)).forEach(x=>{if(out.length<4)push(x,'Also in '+x.c);});}
 return out.slice(0,4);}
function meetHTML(e){const m=whoToMeet(e);if(!m.length)return '';
 return '<div class="k" style="margin-top:14px">Who you should meet</div><p class="mut" style="margin:0 0 8px">Complementary makers in adjacent and convergent fields.</p><div class="meet">'+
  m.map(o=>'<div class="meetcard" data-i="'+o.x._i+'"><div class="mn">'+esc(o.x.n)+'</div><div class="mmk">'+esc(o.x.m)+'</div><div class="mw">'+esc(o.why)+'</div></div>').join('')+'</div>';}
function goExhibit(i){state.tab='Exhibitors';state.ex=i;window.scrollTo(0,0);render();}
function exhibitorDetail(){const e=EX[state.ex];
 const pubfig=e.is_public_figure?'<span class="pubfig">public figure</span>':'';
 const proj=e.project?'<div class="k">Project</div><p class="proj">'+esc(e.project)+'</p>':'';
 const about=e.description?'<div class="k">About</div><p>'+esc(e.description)+'</p>':'';
 const links=linkList(e).length?'<div class="k">Public links</div>'+linksHTML(e):'';
 const find='<div class="k">Find them</div><p><a class="lk lk-other" href="https://www.google.com/search?q='+encodeURIComponent(e.n+' '+e.m)+'" target="_blank" rel="noopener"><span class="lkg">→</span>Search the web</a></p>';
 const pend=isRich(e)?'':'<p class="pend">Bio, links, affiliations and history appear here once this exhibitor is enriched. Use the search below in the meantime.</p>';
 view.innerHTML='<div class="tab" id="back" style="display:inline-block;margin-bottom:12px">&larr; Back to exhibitors</div>'+
  '<div class="card indigo detail"><h3 class="dt">'+esc(e.n)+pubfig+'</h3><div class="who">'+esc(e.m)+' · '+e.c+'</div>'+
  proj+about+tagsHTML(e.tags)+links+locHTML(e.location)+affHTML(e.affiliations)+entHTML(e.entrepreneurship_signals)+histHTML(e.history)+pend+find+meetHTML(e)+'</div>';
 document.getElementById('back').onclick=()=>{state.ex=null;render();};
 view.querySelectorAll('.meetcard').forEach(el=>el.onclick=()=>{state.ex=parseInt(el.dataset.i);window.scrollTo(0,0);render();});}
function cardHTML(e){
 const n=linkList(e).length;
 const lk=n?'<span class="lkn">'+n+' link'+(n>1?'s':'')+'</span>':'';
 const snipTxt=e.description||e.project||'';
 const snip=snipTxt?'<div class="snip">'+esc(snipTxt.length>124?snipTxt.slice(0,122)+'…':snipTxt)+'</div>':'';
 const tg=(e.tags&&e.tags.length)?'<div class="extags">'+esc(e.tags.slice(0,3).join(' · '))+'</div>':'';
 return '<div class="excard'+(isRich(e)?' rich':'')+'" data-i="'+e._i+'"><div class="exhd"><div class="exn">'+esc(e.n)+'</div>'+lk+'</div><div class="exm">'+esc(e.m)+' · '+e.c+'</div>'+snip+tg+'</div>';}
function exhibitors(){
 if(state.ex!==null)return exhibitorDetail();
 const list=EX.filter(e=>inSel(e.c));
 view.innerHTML='<input id="q" placeholder="Search '+list.length+' exhibitors by name, maker or tag..."><div id="lst" class="lst"></div>';
 const lst=document.getElementById('lst');
 function draw(){const q=(document.getElementById('q').value||'').toLowerCase();
  const r=list.filter(e=>!q||e.n.toLowerCase().indexOf(q)>=0||e.m.toLowerCase().indexOf(q)>=0||(e.tags&&e.tags.join(' ').toLowerCase().indexOf(q)>=0)).slice(0,400);
  lst.innerHTML=r.map(cardHTML).join('')||'<div class="row"><div class="m">No matches.</div></div>';
  lst.querySelectorAll('.excard').forEach(el=>el.onclick=()=>{state.ex=parseInt(el.dataset.i);window.scrollTo(0,0);render();});}
 document.getElementById('q').oninput=draw; draw();}
