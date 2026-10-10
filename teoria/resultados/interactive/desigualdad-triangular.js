/* MA-APP-0001. Derived from the canonical Obsidian design. No dependencies or network calls. */
'use strict';
(() => {
  const $ = id => document.getElementById(id);
  const ns = 'http://www.w3.org/2000/svg';
  const P = {
    triangle: { A:[0,0], B:[3,0], C:[3,4], exact:false, text:'Desigualdad estricta: el recorrido mide 7 y la distancia directa, 5.' },
    inside: { A:[0,0], B:[2,0], C:[5,0], exact:true, text:'Igualdad certificada: B pertenece al segmento cerrado AC.' },
    outside: { A:[0,0], B:[7,0], C:[5,0], exact:false, text:'Desigualdad estricta: los tres puntos están alineados, pero B no está entre A y C. Hay retroceso.' },
    endpoint: { A:[0,0], B:[0,0], C:[5,0], exact:true, text:'Igualdad certificada: B=A, así que uno de los tramos mide cero.' },
    'same-ends': { A:[0,0], B:[1,0], C:[0,0], exact:false, text:'Desigualdad estricta: A=C no implica igualdad si B es distinto.' },
    'same-all': { A:[0,0], B:[0,0], C:[0,0], exact:true, text:'Igualdad certificada: A=B=C y las tres longitudes son cero.' }
  };
  const realP = { same:[2,3], cancel:[5,-3], zero:[0,-4], negative:[-2,-3], opposite:[1,-1] };
  const state = { mode:'plane', plane:'triangle', A:[0,0], B:[3,0], C:[3,4], showDirect:true, showRoute:true, x:2, y:3, real:'same', prediction:null, step:0 };
  const svgNode = (name, attrs = {}, text) => { const n=document.createElementNS(ns,name); for(const [k,v] of Object.entries(attrs)) n.setAttribute(k,String(v)); if(text!==undefined)n.textContent=text; return n; };
  const fmt = n => new Intl.NumberFormat('es-CL',{maximumFractionDigits:3}).format(Math.abs(n)<1e-12?0:n);
  const sqdist = (a,b) => Math.hypot(a[0]-b[0],a[1]-b[1]);
  const ps = p => [110+48*p[0],220-42*p[1]];
  const clamp=(v,min,max)=>Math.min(max,Math.max(min,v));
  function switchMode(mode,focus=false){
    state.mode=mode;
    for(const name of ['plane','real','proof']){
      const selected=name===mode;
      $('tab-'+name).setAttribute('aria-selected',String(selected));
      $('tab-'+name).tabIndex=selected?0:-1;
      $('panel-'+name).hidden=!selected;
    }
    if(focus)$('tab-'+mode).focus();
  }
  for(const mode of ['plane','real','proof']) $('tab-'+mode).addEventListener('click',()=>switchMode(mode));
  const modes=['plane','real','proof'];
  document.querySelector('.modes').addEventListener('keydown',e=>{
    const i=modes.indexOf(state.mode);let j;
    if(e.key==='ArrowRight')j=(i+1)%3;
    else if(e.key==='ArrowLeft')j=(i+2)%3;
    else if(e.key==='Home')j=0;
    else if(e.key==='End')j=2;
    else return;
    e.preventDefault();switchMode(modes[j],true);
  });
  for(const b of document.querySelectorAll('.to-proof'))b.addEventListener('click',()=>switchMode('proof',true));
  function setPlanePreset(name){
    const p=P[name];if(!p)return;
    state.plane=name;state.A=[...p.A];state.B=[...p.B];state.C=[...p.C];
    state.showDirect=true;state.showRoute=true;
    $('plane-preset').value=name;
    $('show-direct').checked=true;$('show-route').checked=true;
    $('plane-input-error').hidden=true;
    $('bx').setAttribute('aria-invalid','false');$('by').setAttribute('aria-invalid','false');
    renderPlane();
  }
  function addPoint(g,xy,name,draggable){
    const [x,y]=ps(xy);
    const circle=svgNode('circle',{cx:x,cy:y,r:draggable?17:8,class:draggable?'point-b':'point-halo'});
    if(draggable){circle.dataset.drag='B';circle.setAttribute('aria-hidden','true');}
    g.appendChild(circle);
    g.appendChild(svgNode('text',{x:x+(name==='A'?-12:16),y:y+(name==='C'?23:-13),class:'point-label'},name));
  }
  function renderPlane(){
    const {A,B,C}=state;
    const D=sqdist(A,C),R=sqdist(A,B)+sqdist(B,C),gap=R-D;
    $('plane-d').textContent=fmt(D);$('plane-r').textContent=fmt(R);$('plane-gap').textContent=fmt(Math.max(0,gap));
    $('bx').value=String(B[0]);$('by').value=String(B[1]);
    $('plane-preset').value=state.plane;
    $('plane-direct').style.display=state.showDirect?'':'none';
    $('plane-route').style.display=state.showRoute?'':'none';
    const a=ps(A),b=ps(B),c=ps(C);
    $('plane-direct').setAttribute('d',`M${a[0]} ${a[1]} L${c[0]} ${c[1]}`);
    $('plane-route').setAttribute('d',`M${a[0]} ${a[1]} L${b[0]} ${b[1]} L${c[0]} ${c[1]}`);
    const g=$('plane-points');g.replaceChildren();
    // Draw A and C before the draggable B, so B remains accessible even when points coincide.
    addPoint(g,A,'A',false);addPoint(g,C,'C',false);addPoint(g,B,'B',true);
    const approx=1e-9*Math.max(1,D,R);
    if(state.plane!=='custom')$('plane-message').textContent=P[state.plane].text;
    else if(gap>approx)$('plane-message').textContent='En esta configuración se observa desigualdad estricta: el recorrido es mayor que la distancia directa.';
    else $('plane-message').textContent='Igualdad numérica aproximada. Para afirmar igualdad exacta, verifica que B pertenezca al segmento AC; utiliza «Mostrar igualdad» para un caso certificado.';
    $('plane-desc').textContent=`A=(${A.join(',')}), B=(${B.join(',')}), C=(${C.join(',')}). Distancia directa ${fmt(D)}; recorrido ${fmt(R)}; exceso ${fmt(Math.max(0,gap))}.`;
  }
  function grid(){const g=$('plane-grid');g.replaceChildren();for(let x=-2;x<=9;x++)g.appendChild(svgNode('line',{x1:ps([x,0])[0],y1:10,x2:ps([x,0])[0],y2:430,class:x===0?'axis':'gridline'}));for(let y=-5;y<=5;y++)g.appendChild(svgNode('line',{x1:10,y1:ps([0,y])[1],x2:590,y2:ps([0,y])[1],class:y===0?'axis':'gridline'}));}
  function manualB(i,value){
    const input=$(i?'by':'bx'), lo=i?-4.5:-2,hi=i?4.5:9;
    if(input.value.trim()===''||!Number.isFinite(value)||value<lo||value>hi){
      input.setAttribute('aria-invalid','true');$('plane-input-error').hidden=false;
      $('plane-input-error').textContent=`Introduce una coordenada ${i?'vertical':'horizontal'} finita entre ${lo} y ${hi}. No se ha modificado la figura.`;
      return;
    }
    input.setAttribute('aria-invalid','false');$('plane-input-error').hidden=true;
    state.B[i]=value;state.plane='custom';renderPlane();
  }
  for(const [name,i] of [['bx',0],['by',1]]){
    $(name).addEventListener('change',()=>manualB(i,Number($(name).value)));
    $(name).addEventListener('blur',()=>{if($(name).getAttribute('aria-invalid')==='true')$(name).value=String(state.B[i]);});
  }
  $('plane-preset').addEventListener('change',e=>setPlanePreset(e.target.value));
  $('plane-reset').addEventListener('click',()=>{state.prediction=null;document.querySelectorAll('[name=prediction]').forEach(r=>r.checked=false);$('prediction-message').textContent='Elige una respuesta y contrástala con los casos de igualdad y retroceso.';setPlanePreset('triangle');});
  $('plane-equal').addEventListener('click',()=>setPlanePreset('inside'));
  $('plane-outside').addEventListener('click',()=>setPlanePreset('outside'));
  for(const [input,key] of [['show-direct','showDirect'],['show-route','showRoute']])$(input).addEventListener('change',e=>{state[key]=e.target.checked;renderPlane();});
  document.querySelectorAll('[name=prediction]').forEach(r=>r.addEventListener('change',e=>{
    state.prediction=e.target.value;
    $('prediction-message').textContent=state.prediction==='no'?'Conjetura formulada: comprueba el caso de igualdad y el caso de retroceso; después examina la prueba general.':state.prediction==='yes'?'Busca una configuración que lo haga posible. Si no la encuentras, ¿qué argumento universal podría descartarla?':'Explora los dos casos sugeridos y vuelve a formular una conjetura. La prueba se encuentra en la tercera vista.';
  }));
  const planeSvg=$('plane-svg');let dragging=false;
  function pointerToB(e){
    const ctm=planeSvg.getScreenCTM();if(!ctm)return;
    const p=new DOMPoint(e.clientX,e.clientY).matrixTransform(ctm.inverse());
    const bx=clamp(Math.round(((p.x-110)/48)*20)/20,-2,9);
    const by=clamp(Math.round(((220-p.y)/42)*20)/20,-4.5,4.5);
    if(!Number.isFinite(bx)||!Number.isFinite(by))return;
    state.B=[bx,by];state.plane='custom';renderPlane();
  }
  planeSvg.addEventListener('pointerdown',e=>{if(e.target.dataset.drag!=='B')return;dragging=true;planeSvg.setPointerCapture(e.pointerId);pointerToB(e);});
  planeSvg.addEventListener('pointermove',e=>{if(dragging)pointerToB(e);});
  const stopDrag=e=>{if(!dragging)return;dragging=false;if(planeSvg.hasPointerCapture(e.pointerId))planeSvg.releasePointerCapture(e.pointerId);};
  planeSvg.addEventListener('pointerup',stopDrag);planeSvg.addEventListener('pointercancel',stopDrag);
  function realLine(){
    const g=$('real-figure');g.replaceChildren();const sx=n=>300+n*12.5;
    g.appendChild(svgNode('line',{x1:34,y1:112,x2:566,y2:112,class:'axis'}));
    for(let n=-20;n<=20;n+=5){const x=sx(n);g.appendChild(svgNode('line',{x1:x,y1:106,x2:x,y2:118,class:'axis'}));g.appendChild(svgNode('text',{x,y:139,'text-anchor':'middle',class:'tiny-label'},String(n)));}
    const x=state.x,y=state.y,xy=x+y;
    g.appendChild(svgNode('path',{d:`M${sx(0)} 77 L${sx(x)} 77 L${sx(xy)} 77`,class:'route-arrow'}));
    g.appendChild(svgNode('path',{d:`M${sx(0)} 164 L${sx(xy)} 164`,class:'direct-arrow'}));
    for(const [n,label,offset] of [[0,'0',-16],[x,'x',-16],[xy,'x+y',35]]){
      g.appendChild(svgNode('circle',{cx:sx(n),cy:112,r:4,fill:'#183c5d'}));
      g.appendChild(svgNode('text',{x:sx(n),y:112+offset,'text-anchor':'middle',class:'tiny-label'},label));
    }
    g.appendChild(svgNode('text',{x:300,y:28,'text-anchor':'middle',class:'tiny-label'},'Tramos: 0 → x → x+y'));
    g.appendChild(svgNode('text',{x:300,y:205,'text-anchor':'middle',class:'tiny-label'},'Desplazamiento directo: 0 → x+y'));
    $('real-desc').textContent=`Primer desplazamiento ${x}, segundo ${y}, total con signo ${xy}; magnitud directa ${fmt(Math.abs(xy))}, recorrido ${fmt(Math.abs(x)+Math.abs(y))}.`;
  }
  function renderReal(){
    const {x,y}=state,D=Math.abs(x+y),R=Math.abs(x)+Math.abs(y);
    $('real-x').value=String(x);$('real-y').value=String(y);
    $('real-x-out').textContent=fmt(x);$('real-y-out').textContent=fmt(y);
    $('real-d').textContent=fmt(D);$('real-r').textContent=fmt(R);$('real-gap').textContent=fmt(Math.max(0,R-D));
    $('real-preset').value=state.real;
    $('real-message').textContent=x*y>=0?'Igualdad: los sumandos tienen el mismo signo o alguno es cero; no hay cancelación.':'Desigualdad estricta: los sumandos no nulos tienen signos opuestos y parte de la longitud recorrida se cancela.';
    realLine();
  }
  function setReal(name){if(!realP[name])return;state.real=name;[state.x,state.y]=realP[name];renderReal();}
  $('real-preset').addEventListener('change',e=>setReal(e.target.value));
  for(const [id,key] of [['real-x','x'],['real-y','y']])$(id).addEventListener('input',e=>{const n=Number(e.target.value);if(Number.isFinite(n)){state[key]=n;state.real='custom';renderReal();}});
  $('real-equal').addEventListener('click',()=>setReal('same'));
  $('real-cancel').addEventListener('click',()=>setReal('cancel'));
  $('real-reset').addEventListener('click',()=>setReal('same'));
  const proof=[
    ['Preparación','Consideramos A, B y C arbitrarios en ℝ². No utilizaremos ninguna medición de la figura.','La conclusión deberá valer para todos los puntos del plano.'],
    ['Definir desplazamientos','u = B − A y v = C − B. Al sumar: u + v = C − A.','Los términos B y −B se cancelan algebraicamente.'],
    ['Reconocer distancias','d₂(A,B) = ‖u‖₂; d₂(B,C) = ‖v‖₂; d₂(A,C) = ‖u+v‖₂.','Por definición, la distancia euclidiana entre dos puntos es la norma de su diferencia.'],
    ['Desarrollar el cuadrado','‖u+v‖₂² = ‖u‖₂² + 2⟨u,v⟩ + ‖v‖₂².','Se desarrolla el producto escalar ⟨u+v,u+v⟩.'],
    ['Acotar el término cruzado','⟨u,v⟩ ≤ ‖u‖₂‖v‖₂.','Cauchy–Schwarz controla el producto escalar; su demostración está en §7.1 del artículo.'],
    ['Completar un cuadrado','‖u+v‖₂² ≤ ‖u‖₂² + 2‖u‖₂‖v‖₂ + ‖v‖₂² = (‖u‖₂+‖v‖₂)².','Sustituimos el término cruzado por una cota superior y reconocemos una identidad algebraica.'],
    ['Pasar a las longitudes','‖u+v‖₂ ≤ ‖u‖₂ + ‖v‖₂.','Ambos miembros son no negativos. Sólo por eso podemos comparar las cantidades al comparar sus cuadrados.'],
    ['Traducir y concluir','d₂(A,C) ≤ d₂(A,B) + d₂(B,C), para cualesquiera A, B y C de ℝ².','Se sustituyen las normas por sus distancias. La prueba depende de Cauchy–Schwarz, no de la comprobación gráfica.']
  ];
  const completion='Prueba reconstruida: la validez general procede de las identidades algebraicas y de Cauchy–Schwarz. Mover puntos sólo permitió explorar ejemplos.';
  function renderProof(){
    const step=state.step,[title,content,reason]=proof[step];
    $('proof-count').textContent=`Paso ${step} de 7`;
    $('proof-heading').textContent=title;$('proof-content').textContent=content;$('proof-reason').textContent=reason;
    $('proof-prev').disabled=step===0;
    $('proof-next').textContent=step===7?'He reconstruido la prueba':'Siguiente';
  }
  $('proof-prev').addEventListener('click',()=>{state.step=Math.max(0,state.step-1);renderProof();});
  $('proof-next').addEventListener('click',()=>{if(state.step<7){state.step++;renderProof();}else $('proof-reason').textContent=completion;});
  $('proof-reset').addEventListener('click',()=>{state.step=0;renderProof();});
  $('proof-content').setAttribute('aria-live','polite');
  grid();setPlanePreset('triangle');setReal('same');renderProof();switchMode('plane');
})();
