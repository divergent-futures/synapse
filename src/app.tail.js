function network(){
 const nodes=Array.from(new Set([].concat.apply([],CV.map(c=>c.fl))));
 const cx=340,cy=232,R=168,N=nodes.length,pos={};
 nodes.forEach((f,i)=>{const a=i/N*2*Math.PI-Math.PI/2; pos[f]={x:cx+R*Math.cos(a),y:cy+R*Math.sin(a),a:a};});
 const anySel=state.sel.size>0;
 const cmax=Math.max.apply(null,nodes.map(f=>counts[f]||1));
 let edges='';
 CV.forEach(c=>{for(let i=0;i<c.fl.length;i++)for(let j=i+1;j<c.fl.length;j++){
   const A=pos[c.fl[i]],B=pos[c.fl[j]]; if(!A||!B)continue;
   const on=!anySel||c.fl.some(x=>state.sel.has(x));
   edges+='<path d="M'+A.x.toFixed(1)+' '+A.y.toFixed(1)+' Q '+cx+' '+cy+' '+B.x.toFixed(1)+' '+B.y.toFixed(1)+'" fill="none" stroke="#14b8a6" stroke-width="'+(on?2.2:1)+'" opacity="'+(on?0.85:0.12)+'"/>';
 }});
 let ns='';
 nodes.forEach(f=>{const p=pos[f],r=8+(counts[f]/cmax)*10;
   const self=state.sel.has(f);
   const on=!anySel||self||CV.some(c=>c.fl.some(x=>state.sel.has(x))&&c.fl.indexOf(f)>=0);
   const lx=cx+(R+18)*Math.cos(p.a),ly=cy+(R+18)*Math.sin(p.a);
   const anc=Math.cos(p.a)>0.15?'start':Math.cos(p.a)<-0.15?'end':'middle';
   ns+='<g class="nd" data-f="'+f+'" style="cursor:pointer" opacity="'+(on?1:0.3)+'"><circle cx="'+p.x.toFixed(1)+'" cy="'+p.y.toFixed(1)+'" r="'+r.toFixed(1)+'" fill="#1c2438" stroke="'+(self?'#14b8a6':'#6366f1')+'" stroke-width="'+(self?3:1.5)+'"/><text x="'+lx.toFixed(1)+'" y="'+(ly+3).toFixed(1)+'" fill="#95a1bd" font-size="10" text-anchor="'+anc+'">'+esc(f.split(' ')[0])+'</text></g>';
 });
 view.innerHTML='<p class="sub">Each node is a field, sized by how many makers are in it. Threads are convergences. Click nodes to select several and isolate their connections.</p><svg class="net" viewBox="0 0 680 480">'+edges+ns+'</svg>';
 view.querySelectorAll('.nd').forEach(e=>e.onclick=()=>{toggle(e.dataset.f);render();});}
function hubSVG(o){
 return '<svg class="hub" viewBox="0 0 680 220"><line x1="340" y1="110" x2="150" y2="55" stroke="#2a3350"/><line x1="340" y1="110" x2="150" y2="165" stroke="#2a3350"/><line x1="340" y1="110" x2="540" y2="110" stroke="#2a3350"/>'+
 '<circle cx="340" cy="110" r="52" fill="#1c2438" stroke="#6366f1"/><text x="340" y="106" fill="#e8ecf6" font-size="12" text-anchor="middle">'+esc(o.f.split(' ')[0])+'</text><text x="340" y="122" fill="#95a1bd" font-size="11" text-anchor="middle">'+counts[o.f]+' makers</text>'+
 '<rect x="40" y="34" width="200" height="42" rx="8" fill="#141a2b" stroke="#6366f1"/><text x="52" y="52" fill="#6366f1" font-size="11">Target companies</text><text x="52" y="68" fill="#95a1bd" font-size="10">join, partner, sell</text>'+
 '<rect x="40" y="144" width="200" height="42" rx="8" fill="#141a2b" stroke="#14b8a6"/><text x="52" y="162" fill="#14b8a6" font-size="11">In-room sponsors</text><text x="52" y="178" fill="#95a1bd" font-size="10">warmest first intro</text>'+
 '<rect x="440" y="89" width="200" height="42" rx="8" fill="#141a2b" stroke="#10b981"/><text x="452" y="107" fill="#10b981" font-size="11">Funding and grants</text><text x="452" y="123" fill="#95a1bd" font-size="10">non-dilutive plus accelerators</text></svg>';}
function detailBlock(o){return '<div class="grid2"><div class="card indigo"><div class="k">Adjacent industries</div><p>'+esc(o.ind)+'</p><div class="k">Target companies</div><p>'+esc(o.co)+'</p></div><div class="card green"><div class="k">Funding and competitions</div><p>'+esc(o.fund)+'</p><div class="k">In-room now (Open Sauce sponsors)</div><p style="color:var(--teal)">'+esc(o.spon)+'</p></div></div>';}
function opportunities(){
 if(state.sel.size===0){
  view.innerHTML='<p class="sub">Pick one or more fields (chips above, or the cards below) to see their industry maps.</p><div class="grid3">'+
   order.map(f=>{const o=FL.filter(x=>x.f===f)[0];return '<div class="card indigo fieldcard" data-f="'+f+'"><h3>'+f+'</h3><p style="color:var(--mut)">'+counts[f]+' makers</p><div class="k">In-room</div><p>'+(o?esc(o.spon):'')+'</p></div>';}).join('')+'</div>';
  view.querySelectorAll('.fieldcard').forEach(e=>e.onclick=()=>{toggle(e.dataset.f);render();});return;}
 const fs=order.filter(f=>state.sel.has(f));
 view.innerHTML=fs.map(f=>{const o=FL.filter(x=>x.f===f)[0];if(!o)return '<h3 style="margin:14px 0 4px">'+esc(f)+'</h3><p class="sub">No map yet.</p>';return '<h3 style="margin:16px 0 4px">'+esc(f)+'</h3>'+hubSVG(o)+detailBlock(o);}).join('')+'<p class="note">Plus the cross-cutting list - SBIR/Americas Seed Fund, HAX, Techstars, Crowd Supply, Kickstarter, SBDC/SCORE - applies across all of these.</p>';}
function convergences(){const cv=CV.filter(c=>state.sel.size===0||c.fl.some(x=>state.sel.has(x)));
 view.innerHTML=(cv.length?'<div class="grid2">'+cv.map(c=>'<div class="card indigo"><h3>'+esc(c.t)+'</h3><div class="who">'+esc(c.a)+' x '+esc(c.b)+'</div><p>'+esc(c.i)+'</p><div class="k">Pathway</div><p style="color:var(--mut)">'+esc(c.o)+'</p></div>').join('')+'</div>':'<p class="sub">No convergence touches the selected field(s) yet.</p>');}
// --- Phase 3: onboarding modal + "For You" recommendations ---------------
function closeOnboard(){const o=document.getElementById('ob');if(o)o.remove();}
function openOnboard(){
 closeOnboard();
 const ov=document.createElement('div');ov.className='overlay';ov.id='ob';
 let sel=state.persona, ints=new Set(state.interests);
 function draw(){
  ov.innerHTML='<div class="modal"><div class="mh">Welcome to Synapse</div>'+
   '<p class="msub">Two quick taps and we tailor the room to you. Skip anytime — every tab stays fully open.</p>'+
   '<div class="mlbl">I\'m here as…</div><div class="persona">'+PERSONAS.map(p=>'<div class="pbtn'+(sel===p[0]?' on':'')+'" data-p="'+p[0]+'"><b>'+esc(p[1])+'</b><span>'+esc(p[2])+'</span></div>').join('')+'</div>'+
   '<div class="mlbl">Interested in… <span class="mut">(optional — pick a few)</span></div><div class="ichips">'+order.map(f=>'<div class="ichip'+(ints.has(f)?' on':'')+'" data-f="'+esc(f)+'">'+esc(f)+'</div>').join('')+'</div>'+
   '<div class="mact"><button class="btn ghost" id="skip">Skip for now</button><button class="btn go" id="done"'+(sel?'':' disabled')+'>Show my recommendations</button></div></div>';
  ov.querySelectorAll('.pbtn').forEach(el=>el.onclick=()=>{sel=el.dataset.p;draw();});
  ov.querySelectorAll('.ichip').forEach(el=>el.onclick=()=>{const f=el.dataset.f;if(ints.has(f))ints.delete(f);else ints.add(f);draw();});
  ov.querySelector('#skip').onclick=()=>{markSeen();closeOnboard();};
  ov.querySelector('#done').onclick=()=>{if(!sel)return;const arr=order.filter(f=>ints.has(f));savePrefs({persona:sel,interests:arr});state.persona=sel;state.interests=new Set(arr);state.sel=new Set(arr);state.tab='For You';state.ex=null;closeOnboard();render();};
 }
 draw();ov.onclick=(ev)=>{if(ev.target===ov){markSeen();closeOnboard();}};document.body.appendChild(ov);
}
function foryou(){
 if(!state.persona){
  view.innerHTML='<div class="intro"><p><b>Make it yours.</b> Tell Synapse who you are and what you are into, and this tab becomes a shortlist — makers to meet, convergences to watch, and your fields pre-selected across every other tab. Nothing else moves.</p></div><button class="btn go" id="startp">Personalize Synapse</button>';
  document.getElementById('startp').onclick=openOnboard;return;}
 const ints=state.interests,hasInt=ints.size>0;
 const makers=EX.filter(e=>hasInt?ints.has(e.c):isRich(e)).slice().sort((a,b)=>meetRank(b,{})-meetRank(a,{})).slice(0,6);
 const convs=CV.filter(c=>!hasInt||c.fl.some(f=>ints.has(f))).slice(0,4);
 const greet={visitor:'Here for the day',exhibitor:'Fellow exhibitor',sponsor:'Scouting the room',explore:'Just exploring'}[state.persona]||'Welcome';
 let h='<div class="foryou-hd"><div><h3 style="margin:0;font-size:17px">Recommended for you</h3><p class="sub">'+esc(greet)+(hasInt?' · '+Array.from(ints).map(esc).join(', '):'')+'</p></div><button class="btn ghost" id="editp">Edit</button></div>';
 h+='<div class="k">Makers to meet</div><div class="lst">'+(makers.length?makers.map(cardHTML).join(''):'<p class="sub">Add a few interests to get maker picks — tap Edit.</p>')+'</div>';
 if(convs.length)h+='<div class="k" style="margin-top:16px">Convergences to watch</div><div class="grid2">'+convs.map(c=>'<div class="card indigo"><h3>'+esc(c.t)+'</h3><div class="who">'+esc(c.a)+' × '+esc(c.b)+'</div><p>'+esc(c.i)+'</p></div>').join('')+'</div>';
 h+='<p class="note">Your interests are pre-selected as chips too — open <b>Exhibitors</b>, <b>Network</b> or <b>Opportunities</b> to go deeper, or tap <b>All</b> to clear them and see everything.</p>';
 view.innerHTML=h;
 document.getElementById('editp').onclick=openOnboard;
 view.querySelectorAll('.excard').forEach(el=>el.onclick=()=>goExhibit(parseInt(el.dataset.i)));}
function render(){drawTabs();drawChips();({'For You':foryou,Landscape:landscape,Exhibitors:exhibitors,Network:network,Opportunities:opportunities,Convergences:convergences}[state.tab])();}
render();
if(!PREFS&&!onboardSeen())openOnboard();
