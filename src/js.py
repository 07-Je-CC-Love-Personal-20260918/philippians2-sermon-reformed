# -*- coding: utf-8 -*-
JS = r"""
(function(){
  'use strict';
  var d=document, root=d.documentElement;

  /* ---------- 主题：明 / 暗 / 跟随系统 ---------- */
  var KEY='php2-theme', modes=['auto','light','dark'], label={auto:'◑ 跟随',light:'☀ 明亮',dark:'☾ 暗色'};
  function apply(m){
    if(m==='auto'){ root.removeAttribute('data-theme'); }
    else { root.setAttribute('data-theme',m); }
    var b=d.getElementById('theme'); if(b) b.textContent=label[m];
  }
  var cur=(function(){ try{ return localStorage.getItem(KEY)||'auto'; }catch(e){ return 'auto'; } })();
  if(modes.indexOf(cur)<0) cur='auto';
  apply(cur);
  var mq=window.matchMedia('(prefers-color-scheme: dark)');
  function sysSync(){ if(cur==='auto'){ root.removeAttribute('data-theme'); } }
  if(mq.addEventListener) mq.addEventListener('change',sysSync);

  /* ---------- 目录高亮：rAF + getBoundingClientRect ---------- */
  var links=[].slice.call(d.querySelectorAll('nav#toc a[href^="#"]'));
  var targets=links.map(function(a){
    var el=d.getElementById(a.getAttribute('href').slice(1));
    return el?{a:a,el:el}:null;
  }).filter(Boolean);
  var lastOn=null, ticking=false, tocEl=d.getElementById('toc');

  function highlight(){
    ticking=false;
    var best=null, bestTop=-1e9, line=90;
    for(var i=0;i<targets.length;i++){
      var top=targets[i].el.getBoundingClientRect().top;
      if(top<=line && top>bestTop){ bestTop=top; best=targets[i]; }
    }
    if(!best && targets.length) best=targets[0];
    if(best && best.a!==lastOn){
      if(lastOn) lastOn.classList.remove('on');
      best.a.classList.add('on'); lastOn=best.a;
      if(tocEl && window.innerWidth>980){
        var r=best.a.getBoundingClientRect(), t=tocEl.getBoundingClientRect();
        if(r.top<t.top+20||r.bottom>t.bottom-20){
          tocEl.scrollTop += (r.top-t.top) - t.height/2 + r.height/2;
        }
      }
    }
    var h=d.body.scrollHeight-window.innerHeight;
    var p=d.getElementById('prog');
    if(p) p.style.width=(h>0?Math.min(100,Math.max(0,window.scrollY/h*100)):0)+'%';
  }
  function onScroll(){ if(!ticking){ ticking=true; requestAnimationFrame(highlight); } }
  window.addEventListener('scroll',onScroll,{passive:true});
  window.addEventListener('resize',onScroll,{passive:true});

  /* ---------- 移动端抽屉 ---------- */
  var scrim=d.getElementById('scrim');
  function drawer(open){
    if(!tocEl) return;
    tocEl.classList.toggle('open',open);
    if(scrim) scrim.style.display=open?'block':'none';
    d.body.style.overflow=open?'hidden':'';
  }
  d.addEventListener('click',function(e){
    var t=e.target.closest?e.target.closest('[data-act]'):null;
    if(t){
      var act=t.getAttribute('data-act');
      if(act==='menu'){ drawer(!tocEl.classList.contains('open')); }
      else if(act==='theme'){
        cur=modes[(modes.indexOf(cur)+1)%modes.length];
        try{ localStorage.setItem(KEY,cur); }catch(err){}
        apply(cur);
      }
      else if(act==='print'){ window.print(); }
      else if(act==='expand'){
        var qs=[].slice.call(d.querySelectorAll('details.qa'));
        var anyClosed=qs.some(function(x){ return !x.open; });
        qs.forEach(function(x){ x.open=anyClosed; });
        t.textContent=anyClosed?'▲ 收起全部问答':'▼ 展开全部问答';
      }
      else if(act==='top'){ window.scrollTo({top:0,behavior:'smooth'}); }
      return;
    }
    if(e.target.id==='scrim'){ drawer(false); }
    var a=e.target.closest?e.target.closest('nav#toc a'):null;
    if(a && window.innerWidth<=980){ drawer(false); }
  });
  d.addEventListener('keydown',function(e){ if(e.key==='Escape') drawer(false); });

  /* ---------- 打印前展开全部问答 ---------- */
  window.addEventListener('beforeprint',function(){
    [].slice.call(d.querySelectorAll('details')).forEach(function(x){
      if(!x.open){ x.setAttribute('data-wasclosed','1'); x.open=true; }
    });
  });
  window.addEventListener('afterprint',function(){
    [].slice.call(d.querySelectorAll('details[data-wasclosed]')).forEach(function(x){
      x.open=false; x.removeAttribute('data-wasclosed');
    });
  });

  highlight();
})();
"""
