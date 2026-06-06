(function(){
  var id='moonn-teen-camp-home-banner';
  var targetUrl='/podrostkovyy-lager-psihologiya';
  var videoUrl='https://cdn.jsdelivr.net/gh/rublevalexandermsu-design/moonn-psy-pages@312fd045c882d59ebc32474320f4e3c784d49ad7/assets/teen-psychology-camp-2026/teen-intensive-hall-preview-2026-06-06.mp4';
  function addStyle(){
    if(document.getElementById(id+'-style')) return;
    var style=document.createElement('style');
    style.id=id+'-style';
    style.textContent='.moonn-teen-camp-home-banner{font-family:Inter,Arial,sans-serif;position:relative;z-index:3;max-width:1120px;margin:28px auto;padding:28px;border-radius:28px;background:linear-gradient(135deg,rgba(248,250,255,.97),rgba(242,247,255,.96));box-shadow:0 18px 48px rgba(37,47,91,.13);border:1px solid rgba(49,73,201,.14);display:grid;grid-template-columns:minmax(0,1.08fr) minmax(300px,.92fr);gap:24px;align-items:center;overflow:hidden}.moonn-teen-camp-home-kicker{display:inline-flex;width:max-content;max-width:100%;padding:8px 12px;border-radius:999px;background:rgba(255,255,255,.78);color:#3149c9;font-size:13px;font-weight:800;line-height:1.2;margin-bottom:12px;box-shadow:inset 0 0 0 1px rgba(49,73,201,.16)}.moonn-teen-camp-home-title{font-size:clamp(28px,3.8vw,48px);line-height:1.05;margin:0 0 12px;color:#18205c;font-weight:900;letter-spacing:0}.moonn-teen-camp-home-text{font-size:18px;line-height:1.5;color:#4f5688;margin:0 0 20px;max-width:690px}.moonn-teen-camp-home-actions{display:flex;flex-wrap:wrap;gap:12px;align-items:center}.moonn-teen-camp-home-button{display:inline-flex;align-items:center;justify-content:center;min-height:48px;padding:0 22px;border-radius:999px;background:linear-gradient(135deg,#3149c9,#21a4d8);color:#fff!important;text-decoration:none!important;font-weight:800;box-shadow:0 14px 26px rgba(49,73,201,.24);transition:transform .2s ease,box-shadow .2s ease}.moonn-teen-camp-home-button:hover{transform:translateY(-2px);box-shadow:0 18px 34px rgba(49,73,201,.32)}.moonn-teen-camp-home-note{font-size:14px;color:#5f6794}.moonn-teen-camp-home-media{position:relative;display:block;border-radius:22px;overflow:hidden;box-shadow:0 18px 42px rgba(18,31,84,.18);background:#11163d;aspect-ratio:4/3}.moonn-teen-camp-home-media video{display:block;width:100%;height:100%;object-fit:cover}.moonn-teen-camp-home-media:after{content:"";position:absolute;inset:0;background:linear-gradient(180deg,rgba(6,10,32,0) 45%,rgba(6,10,32,.44) 100%);pointer-events:none}.moonn-teen-camp-home-badge{position:absolute;left:14px;bottom:14px;z-index:1;padding:9px 12px;border-radius:14px;background:rgba(255,255,255,.92);color:#18205c;font-size:13px;font-weight:800;box-shadow:0 8px 24px rgba(18,31,84,.12)}@media(max-width:860px){.moonn-teen-camp-home-banner{grid-template-columns:1fr;margin:22px 16px;padding:22px;border-radius:22px}.moonn-teen-camp-home-text{font-size:16px}.moonn-teen-camp-home-media{order:-1}.moonn-teen-camp-home-button{width:100%}}';
    document.head.appendChild(style);
  }
  function mount(){
    if(document.getElementById(id)) return;
    var root=document.querySelector('#allrecords')||document.body;
    if(!root) return;
    addStyle();
    var records=Array.prototype.slice.call(root.querySelectorAll('.r'));
    var anchor=records.find(function(el){return el.offsetHeight>180;}) || records[0] || root.firstElementChild;
    var banner=document.createElement('section');
    banner.id=id;
    banner.className='moonn-teen-camp-home-banner';
    banner.setAttribute('aria-label','Подростковый интенсив по психологии');
    banner.innerHTML='<div><div class="moonn-teen-camp-home-kicker">6-10 июля · Москва · 8-12 подростков</div><h2 class="moonn-teen-camp-home-title">Подростковый интенсив по психологии</h2><p class="moonn-teen-camp-home-text">Пять дней практики с Татьяной Мунн: уверенность в себе, общение, ораторство, эмоции и искусственный интеллект в обучении — без школьной скуки и давления.</p><div class="moonn-teen-camp-home-actions"><a class="moonn-teen-camp-home-button" href="'+targetUrl+'">Узнать программу</a><span class="moonn-teen-camp-home-note">40 000 ₽ ранняя оплата · Сущёвский Вал, 56 · 10:00-18:00</span></div></div><a class="moonn-teen-camp-home-media" href="'+targetUrl+'" aria-label="Открыть страницу подросткового интенсива"><video autoplay muted loop playsinline preload="metadata" aria-label="Подростковый интенсив по психологии в зале"><source src="'+videoUrl+'" type="video/mp4"></video><span class="moonn-teen-camp-home-badge">Интенсив по психологии 2026</span></a>';
    if(anchor && anchor.parentNode){anchor.parentNode.insertBefore(banner, anchor.nextSibling);} else {root.insertBefore(banner, root.firstChild);}
    var video=banner.querySelector('video');
    if(video){
      video.muted=true;
      video.playbackRate=.6;
      video.addEventListener('loadedmetadata', function(){ video.playbackRate=.6; });
      var play=video.play();
      if(play && typeof play.catch==='function') play.catch(function(){});
    }
  }
  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded', mount); else mount();
})();
