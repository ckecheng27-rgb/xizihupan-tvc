# -*- coding: utf-8 -*-
import os

LOGO_URL = 'https://raw.githubusercontent.com/ckecheng27-rgb/xizihupan-tvc/main/images/logo.png'

page = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>我在西子湖畔 · TVC创意与AI实践</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:-apple-system,"PingFang SC",sans-serif;background:#0d0d0d;color:#f0ede8;overflow-x:hidden}
.scroll-container{height:100vh;overflow-y:scroll;scroll-snap-type:y mandatory;scrollbar-width:none}
.scroll-container::-webkit-scrollbar{display:none}
.section{min-height:100vh;scroll-snap-align:start;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:60px 24px;position:relative}
.nav-dots{position:fixed;right:20px;top:50%;transform:translateY(-50%);z-index:100;display:flex;flex-direction:column;gap:12px}
.nav-dots a{display:block;width:8px;height:8px;border-radius:50%;background:rgba(240,237,232,.2);transition:all .4s;text-decoration:none}
.nav-dots a:hover,.nav-dots a.active{background:#c9a84c;box-shadow:0 0 12px rgba(201,168,76,.4);transform:scale(1.3)}
#hero{background:linear-gradient(135deg,#0d0d0d,#1a1510,#0d0d0d);text-align:center}
#about{background:#111;text-align:center}
#concept{background:#0d0d0d;text-align:center}
#highlights{background:#111;text-align:center}
#cases{background:#0d0d0d}
#tech{background:#111;text-align:center}
#data{background:#0d0d0d;text-align:center}
#footer{background:linear-gradient(135deg,#0d0d0d,#1a1510,#0d0d0d);text-align:center}
.hero-logo{max-height:80px;max-width:80%;margin-bottom:18px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.hero-tag{font-size:11px;letter-spacing:4px;color:#c9a84c;margin-bottom:16px}
.hero-sub{font-size:clamp(14px,2vw,20px);font-weight:200;letter-spacing:4px;color:rgba(240,237,232,.8);margin-bottom:8px}
.hero-year{font-size:11px;letter-spacing:3px;color:rgba(240,237,232,.4)}
.scroll-hint{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);color:rgba(240,237,232,.3);font-size:10px;letter-spacing:3px;animation:f 2s ease-in-out infinite}
@keyframes f{0%,100%{transform:translateX(-50%) translateY(0)}50%{transform:translateX(-50%) translateY(-8px)}}
.st{font-size:clamp(20px,3vw,36px);font-weight:200;letter-spacing:6px;margin-bottom:12px;text-align:center}
.st em{font-style:normal;color:#c9a84c;font-weight:300}
.sd{width:40px;height:1px;background:rgba(201,168,76,.3);margin:0 auto 30px}
.ss{font-size:clamp(13px,1.5vw,16px);font-weight:200;letter-spacing:2px;color:rgba(240,237,232,.65);max-width:600px;margin:0 auto 36px;text-align:center;line-height:1.8}
.at{max-width:680px;font-size:clamp(14px,1.5vw,17px);font-weight:200;line-height:2;letter-spacing:1px;color:rgba(240,237,232,.82);text-align:center}
.g4{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;max-width:960px;width:100%}
.gc{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);padding:28px 20px;border-radius:8px;transition:all .3s}
.gc:hover{border-color:rgba(201,168,76,.2);background:rgba(255,255,255,.05)}
.gn{font-size:clamp(24px,3vw,36px);font-weight:100;color:rgba(201,168,76,.35);margin-bottom:10px;letter-spacing:2px}
.gc h4{font-size:15px;font-weight:300;letter-spacing:2px;margin-bottom:8px}
.gc p{font-size:12px;font-weight:200;letter-spacing:.5px;color:rgba(240,237,232,.6);line-height:1.7}
.cg{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:18px;max-width:1100px;width:100%}
.cc{background:rgba(255,255,255,.03);border:1px solid rgba(255,255,255,.06);border-radius:10px;overflow:hidden;cursor:pointer;transition:all .3s}
.cc:hover{border-color:rgba(201,168,76,.25);transform:translateY(-3px);background:rgba(255,255,255,.06)}
.cv{position:relative;width:100%;padding-top:56.25%;background:#000}
.cv video{position:absolute;top:0;left:0;width:100%;height:100%;object-fit:cover}
.ci{padding:16px 18px 18px}
.cl{font-size:10px;letter-spacing:2px;color:#c9a84c;margin-bottom:4px}
.ci h3{font-size:15px;font-weight:300;letter-spacing:1px;margin-bottom:6px;line-height:1.4}
.cd{font-size:12px;font-weight:200;color:rgba(240,237,232,.55);line-height:1.6}
.ch{font-size:10px;letter-spacing:1px;color:rgba(201,168,76,.4);margin-top:10px;text-align:right}
.mo{position:fixed;top:0;left:0;width:100%;height:100%;z-index:1000;background:rgba(5,5,5,.93);display:none;justify-content:center;overflow-y:auto;padding:40px 20px}
.mo.s{display:flex}
.mc{position:fixed;top:20px;right:28px;z-index:1001;background:none;border:none;color:rgba(240,237,232,.3);font-size:24px;cursor:pointer}
.mc:hover{color:#c9a84c}
.mi{max-width:680px;width:100%;margin:40px auto}
.mn{font-size:11px;letter-spacing:3px;color:#c9a84c;margin-bottom:6px}
.mi h2{font-size:clamp(22px,3vw,32px);font-weight:200;letter-spacing:3px;margin-bottom:16px}
.mst{font-size:12px;letter-spacing:4px;color:rgba(201,168,76,.6);margin:30px 0 14px;padding-bottom:8px;border-bottom:1px solid rgba(201,168,76,.1)}
.si{display:grid;grid-template-columns:70px 1fr;gap:12px;padding:12px 16px;margin-bottom:8px;border:1px solid rgba(255,255,255,.05);background:rgba(255,255,255,.015);border-radius:6px}
.stm{font-size:12px;color:#c9a84c;font-weight:300;letter-spacing:1px}
.sdd{font-size:13px;font-weight:200;line-height:1.6;color:rgba(240,237,232,.75)}
.aii{padding:14px 16px;margin-bottom:8px;border:1px solid rgba(201,168,76,.08);background:rgba(255,255,255,.01);border-radius:6px}
.aii .al{font-size:11px;letter-spacing:2px;color:#c9a84c;margin-bottom:4px}
.aii p{font-size:12px;font-weight:200;color:rgba(240,237,232,.6);line-height:1.6}
.dg{display:flex;justify-content:center;gap:40px;flex-wrap:wrap}
.di{text-align:center}
.dn{font-size:clamp(32px,5vw,56px);font-weight:100;color:#c9a84c;letter-spacing:2px}
.dl{font-size:12px;font-weight:200;letter-spacing:2px;color:rgba(240,237,232,.45);margin-top:6px}
.fl{max-height:50px;max-width:60%;margin-bottom:12px}
.ft{font-size:13px;font-weight:200;letter-spacing:3px;color:rgba(240,237,232,.4);margin-bottom:30px}
.fc{font-size:10px;letter-spacing:2px;color:rgba(240,237,232,.2)}
.al{position:fixed;bottom:20px;right:20px;z-index:99}
.al a{color:rgba(240,237,232,.12);text-decoration:none;font-size:10px;letter-spacing:1px;transition:color .3s}
.al a:hover{color:rgba(240,237,232,.35)}
.fi{opacity:0;transform:translateY(30px);transition:all .8s cubic-bezier(.23,1,.32,1)}
.fi.v{opacity:1;transform:translateY(0)}
@media(max-width:600px){.section{padding:40px 16px}.g4{grid-template-columns:1fr}.cg{grid-template-columns:1fr}.dg{gap:24px}}
</style>
</head>
<body>
<nav class="nav-dots" id="nd">''' + '\n'.join(['<a href="#'+s+'"></a>' for s in ['hero','about','concept','highlights','cases','tech','data','footer']]) + r'''
</nav>
<div class="mo" id="mo"><button class="mc" id="mc">✕</button><div class="mi" id="mi"></div></div>
<div class="scroll-container">

<section class="section" id="hero"><div class="fi">
<img class="hero-logo" src="''' + LOGO_URL + r'''" alt="我在西子湖畔">
<div class="hero-tag">AI · CREATIVE · STRATEGY</div>
<div class="hero-sub">直播间TVC创意与AI实践方案</div>
<div class="hero-year">2026 · 十惠鸭品牌</div>
</div><div class="scroll-hint">向下探索</div></section>

<section class="section" id="about"><div class="st fi">关于<em>方案</em></div><div class="sd"></div>
<div class="at fi"><p>本方案以"十惠鸭"IP为核心，融合江南水墨意境与AI技术，打造4支风格各异的TVC短片。从白蛇传说、端午民俗到江湖武侠、反差幽默，用AI重新定义品牌叙事。</p></div></section>

<section class="section" id="concept"><div class="st fi">核心<em>创意</em></div><div class="sd"></div>
<div class="ss fi">AIDA法则驱动的品牌叙事模型</div>
<div class="g4">''' + ''.join(['<div class="gc fi"><div class="gn">'+i[0]+'</div><h4>'+i[1]+'</h4><p>'+i[2]+'</p></div>' for i in [('A','引起注意','强烈的视觉冲击或悬念，在第一秒留住观众'),('I','激发兴趣','结合观众痛点，让故事产生代入感'),('D','唤起欲望','展示美好愿景，让观众渴望拥有'),('A','促成行动','明确的行动指令，完成互动闭环')]]) + r'''
</div></section>

<section class="section" id="highlights"><div class="st fi">方案<em>亮点</em></div><div class="sd"></div>
<div class="g4">''' + ''.join(['<div class="gc fi"><div class="gn">'+str(i[0]).zfill(2)+'</div><h4>'+i[1]+'</h4><p>'+i[2]+'</p></div>' for i in [(1,'AI全流程创作','从剧本到成片，Midjourney + Runway实现"所想即所得"'),(2,'AI分镜提示词公式','【镜头类型】+【运镜方式】+【主体】+【环境】+【氛围】'),(3,'统一IP视觉体系','"十惠鸭"贯穿四个案例，打造品牌记忆锚点'),(4,'低成本高效率','成本仅为传统TVC的5%-10%，迭代速度快')]]) + r'''
</div></section>

<section class="section" id="cases"><div class="st fi">案例<em>实践</em></div><div class="sd"></div>
<div class="ss fi">点击卡片查看详细分镜与创意解析</div>
<div class="cg" id="cg"></div></section>

<section class="section" id="tech"><div class="st fi">技术<em>实现</em></div><div class="sd"></div>
<div class="g4">''' + ''.join(['<div class="gc fi"><h4>'+i[0]+'</h4><p>'+i[1]+'</p></div>' for i in [('ChatGPT','脚本与文案生成'),('Midjourney','视觉设计与分镜'),('Runway','AI视频生成'),('剪映','剪辑与合成')]]) + r'''
</div></section>

<section class="section" id="data"><div class="st fi">数据<em>效果</em></div><div class="sd"></div>
<div class="dg">''' + ''.join(['<div class="di fi"><div class="dn">'+i[0]+'</div><div class="dl">'+i[1]+'</div></div>' for i in [('4','支TVC成片'),('90%','成本降低'),('3-5','天制作周期')]]) + r'''
</div></section>

<section class="section" id="footer">
<img class="fl" src="''' + LOGO_URL + r'''" alt="我在西子湖畔">
<div class="ft">十惠鸭品牌 · 直播电商 AI 赋能</div>
<div class="fc">© 2026 十惠鸭品牌 · 直播间TVC创意方案</div></section>

</div>
<div class="al"><a href="admin.html" target="_blank">⚙ 管理</a></div>

<script>
// Case data
var CASE_DATA=[{"n":"CASE 01","t":"西子湖畔 · 福利召唤","d":"新中式意境融合，白蛇传说与直播间福利的创意碰撞","v":"videos/case-1.mp4","sh":[["0-4s","开篇水墨长卷展开，白蛇剪影浮现"],["4-8s","十惠鸭IP出场"],["8-12s","福利场景蒙太奇"],["12-15s","品牌LOGO定帧"]],"ai":[["A","水墨山巅+十惠鸭剪影"],["I","白蛇传说与福利结合"],["D","福利场景刺激期待"],["A","引导领取福利"]]},{"n":"CASE 02","t":"十惠鸭 · 荷间寻惠","d":"水墨江南意境，十惠鸭泛舟西湖寻找福利的故事","v":"videos/case-2.mp4","sh":[["0-6s","烟雨西湖远景"],["6-10s","荷叶转动浮现福利"],["10-14s","抢红包动画"],["14-18s","品牌口号引导"]],"ai":[["A","烟雨西湖水墨开篇"],["I","十惠鸭寻惠之旅"],["D","福利涌现获得感"],["A","引导关注直播间"]]},{"n":"CASE 03","t":"湖畔端午 · 破五毒","d":"武侠风格创意，十惠鸭端午破五毒的趣味叙事","v":"videos/case-3.mp4","sh":[["KF 1","画卷入画粽叶飘香"],["KF 2","十惠鸭破五毒"],["KF 3","五毒化福利掉落"],["KF 4","端午祝福引导"]],"ai":[["A","国风武侠视觉冲击"],["I","端午民俗破五毒"],["D","福利掉落激发参与"],["A","进入直播间领取"]]},{"n":"CASE 04","t":"福利一出 · 十拿九稳","d":"反差幽默，钓鱼梗与红包福利的惊喜结合","v":"videos/case-4.mp4","sh":[["0-3s","西湖晨起钓鱼"],["3-7s","浮标拖出大红包"],["7-11s","福利飞出"],["11-15s","品牌口号引导"]],"ai":[["A","清晨钓鱼反差悬念"],["I","红包拖出期待感"],["D","惊喜福利不断"],["A","十惠鸭等你来"]]}];

// Render cases
var cg=document.getElementById('cg');
CASE_DATA.forEach(function(c,i){
  var card=document.createElement('div');
  card.className='cc fi';
  card.style.transitionDelay=(i*0.1)+'s';
  card.innerHTML='<div class="cv"><video muted loop playsinline><source src="'+c.v+'" type="video/mp4"></video></div><div class="ci"><div class="cl">'+c.n+'</div><h3>'+c.t+'</h3><div class="cd">'+c.d+'</div><div class="ch">点击查看详情 ➞</div></div>';
  card.addEventListener('click',function(){
    var sh='';c.sh.forEach(function(s){sh+='<div class="si"><div class="stm">'+s[0]+'</div><div class="sdd">'+s[1]+'</div></div>'});
    var ah='';c.ai.forEach(function(a){ah+='<div class="aii"><div class="al">'+a[0]+'</div><p>'+a[1]+'</p></div>'});
    document.getElementById('mi').innerHTML='<div class="mn">'+c.n+'</div><h2>'+c.t+'</h2><div class="mst">━ 分镜脚本</div>'+sh+'<div class="mst">━ AIDA 叙事拆解</div>'+ah;
    document.getElementById('mo').style.display='flex';
  });
  cg.appendChild(card);
});

// Modal close
document.getElementById('mc').addEventListener('click',function(){document.getElementById('mo').style.display='none'});
document.getElementById('mo').addEventListener('click',function(e){if(e.target===this)this.style.display='none'});

// Nav dots
var observer=new IntersectionObserver(function(entries){
  entries.forEach(function(e){
    if(e.isIntersecting){
      document.querySelectorAll('.nav-dots a').forEach(function(a){a.classList.remove('active')});
      var dot=document.querySelector('.nav-dots a[href="#'+e.target.id+'"]');
      if(dot)dot.classList.add('active');
    }
  });
},{threshold:0.5});
document.querySelectorAll('.section').forEach(function(s){observer.observe(s)});

// Fade in
var fo=new IntersectionObserver(function(entries){
  entries.forEach(function(e){if(e.isIntersecting)e.target.classList.add('v')});
},{threshold:0.1});
document.querySelectorAll('.fi').forEach(function(el){fo.observe(el)});

// Video hover play
document.querySelectorAll('.cc').forEach(function(c){
  c.addEventListener('mouseenter',function(){var v=this.querySelector('video');if(v)v.play()});
  c.addEventListener('mouseleave',function(){var v=this.querySelector('video');if(v){v.pause();v.currentTime=0}});
});

// Load config from localStorage
try{
  var ls=localStorage.getItem('xizitvc_config');
  if(ls){
    var cfg=JSON.parse(ls);
    if(cfg.hero_subtitle){var e=document.querySelector('.hero-sub');if(e)e.textContent=cfg.hero_subtitle}
    if(cfg.hero_year){var e=document.querySelector('.hero-year');if(e)e.innerHTML=cfg.hero_year}
    if(cfg.hero_tag){var e=document.querySelector('.hero-tag');if(e)e.textContent=cfg.hero_tag}
    if(cfg.about_text){var e=document.querySelector('.at p');if(e)e.innerHTML=cfg.about_text}
    if(cfg.footer_text){var e=document.querySelector('.ft');if(e)e.textContent=cfg.footer_text}
    if(cfg.footer_cr){var e=document.querySelector('.fc');if(e)e.innerHTML=cfg.footer_cr}
  }
}catch(e){}
</script>
</body>
</html>'''

path = r'C:\Users\Designer\Desktop\西子湖畔交互展示\index.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(page)
print(f'Written: {len(page)} bytes')
