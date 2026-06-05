# -*- coding: utf-8 -*-
admin = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>后台管理 · 西子湖畔TVC</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,"PingFang SC",sans-serif;background:#0d0d0d;color:#f0ede8}
/* Login */
.login-wrap{min-height:100vh;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:40px 20px}
.login-box{max-width:360px;width:100%}
.login-box h1{font-size:24px;font-weight:200;letter-spacing:4px;text-align:center;margin-bottom:6px}
.login-box h1 strong{font-weight:300;color:#c9a84c}
.login-sub{font-size:11px;color:rgba(240,237,232,.25);letter-spacing:2px;text-align:center;margin-bottom:40px}
.login-box .field{margin-bottom:16px}
.login-box .field label{display:block;font-size:11px;color:rgba(240,237,232,.3);letter-spacing:2px;margin-bottom:6px}
.login-box .field input{width:100%;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);color:#f0ede8;padding:10px 14px;font-size:14px;border-radius:6px;outline:none;transition:border .3s}
.login-box .field input:focus{border-color:#c9a84c}
.login-btn{width:100%;padding:12px;background:transparent;border:1px solid #c9a84c;color:#c9a84c;font-size:13px;letter-spacing:3px;cursor:pointer;transition:all .3s;border-radius:6px;margin-top:8px}
.login-btn:hover{background:#c9a84c;color:#0d0d0d}
.login-error{color:#e06060;font-size:12px;text-align:center;margin-top:12px;display:none}
/* Admin Panel */
.panel-wrap{display:none;padding:40px 20px;max-width:800px;margin:0 auto}
.panel-wrap.s{display:block}
.panel-wrap h1{font-size:24px;font-weight:200;letter-spacing:4px;margin-bottom:4px}
.panel-wrap h1 strong{font-weight:300;color:#c9a84c}
.panel-sub{font-size:11px;color:rgba(240,237,232,.25);letter-spacing:2px;margin-bottom:30px}
.sc{border:1px solid rgba(255,255,255,.06);background:rgba(255,255,255,.015);margin-bottom:16px;padding:20px 24px;border-radius:8px}
.sc h2{font-size:13px;font-weight:300;letter-spacing:2px;color:#c9a84c;margin-bottom:14px;padding-bottom:8px;border-bottom:1px solid rgba(201,168,76,.1)}
.field{margin-bottom:12px}
.field label{display:block;font-size:10px;color:rgba(240,237,232,.3);letter-spacing:1px;margin-bottom:4px}
.field input,.field textarea{width:100%;background:rgba(255,255,255,.04);border:1px solid rgba(255,255,255,.08);color:#f0ede8;padding:8px 12px;font-size:13px;border-radius:4px;outline:none;transition:border .3s;font-family:inherit}
.field input:focus,.field textarea:focus{border-color:#c9a84c}
.field textarea{resize:vertical;min-height:50px;line-height:1.6}
.row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.btn-group{display:flex;gap:12px;margin:24px 0;flex-wrap:wrap}
.btn{padding:10px 24px;border:1px solid #c9a84c;background:transparent;color:#c9a84c;font-size:12px;letter-spacing:2px;cursor:pointer;transition:all .3s;border-radius:4px}
.btn:hover{background:#c9a84c;color:#0d0d0d}
.btn-p{border-color:#c9a84c;background:#c9a84c;color:#0d0d0d}
.btn-d{border-color:rgba(255,80,80,.3);color:rgba(255,80,80,.5)}
.btn-d:hover{background:rgba(255,80,80,.1);color:#e06060}
.toast{position:fixed;top:20px;right:20px;padding:12px 24px;background:#c9a84c;color:#0d0d0d;font-size:13px;letter-spacing:1px;border-radius:4px;opacity:0;transform:translateY(-20px);transition:all .4s;z-index:999}
.toast.s{opacity:1;transform:translateY(0)}
@media(max-width:600px){.row{grid-template-columns:1fr}}
</style>
</head>
<body>

<!-- Login -->
<div class="login-wrap" id="loginWrap">
<div class="login-box">
<h1>内容<strong>管理</strong></h1>
<div class="login-sub">请登录以进入后台</div>
<div class="field"><label>账号</label><input type="text" id="loginUser" placeholder="请输入账号" value="2021687574"></div>
<div class="field"><label>密码</label><input type="password" id="loginPass" placeholder="请输入密码"></div>
<button class="login-btn" onclick="doLogin()">登 录</button>
<div class="login-error" id="loginError">账号或密码错误，请重试</div>
</div>
</div>

<!-- Admin Panel -->
<div class="panel-wrap" id="panelWrap">
<h1>内容<strong>管理</strong></h1>
<div class="panel-sub">在线修改文字内容，保存后刷新主页面即可生效</div>

<div class="sc">
<h2>🏠 首页 (Hero)</h2>
<div class="field"><label>副标题</label><input type="text" id="hero_subtitle" value="直播间TVC创意与AI实践方案"></div>
<div class="field"><label>顶部标签</label><input type="text" id="hero_tag" value="AI · CREATIVE · STRATEGY"></div>
<div class="field"><label>年份/品牌</label><input type="text" id="hero_year" value="2026 · 十惠鸭品牌"></div>
</div>

<div class="sc">
<h2>📖 关于方案</h2>
<div class="field"><label>正文</label><textarea id="about_text" rows="3">本方案以"十惠鸭"IP为核心，融合江南水墨意境与AI技术，打造4支风格各异的TVC短片。从白蛇传说、端午民俗到江湖武侠、反差幽默，用AI重新定义品牌叙事。</textarea></div>
</div>

<div class="sc">
<h2>⭐ 方案亮点 (4项)</h2>
<div class="row">
<div class="field"><label>亮点1 标题</label><input type="text" id="h1_title" value="AI全流程创作"></div>
<div class="field"><label>亮点1 描述</label><input type="text" id="h1_desc" value='从剧本到成片，Midjourney + Runway实现"所想即所得"'></div>
</div>
<div class="row">
<div class="field"><label>亮点2 标题</label><input type="text" id="h2_title" value="AI分镜提示词公式"></div>
<div class="field"><label>亮点2 描述</label><input type="text" id="h2_desc" value="【镜头类型】+【运镜方式】+【主体】+【环境】+【氛围】"></div>
</div>
<div class="row">
<div class="field"><label>亮点3 标题</label><input type="text" id="h3_title" value='统一IP视觉体系'></div>
<div class="field"><label>亮点3 描述</label><input type="text" id="h3_desc" value='"十惠鸭"贯穿四个案例，打造品牌记忆锚点'></div>
</div>
<div class="row">
<div class="field"><label>亮点4 标题</label><input type="text" id="h4_title" value="低成本高效率"></div>
<div class="field"><label>亮点4 描述</label><input type="text" id="h4_desc" value="成本仅为传统TVC的5%-10%，迭代速度快"></div>
</div>
</div>

<div class="sc">
<h2>📱 案例 (4个)</h2>
<div class="field"><label>CASE 01 描述</label><input type="text" id="c1_desc" value="新中式意境融合，白蛇传说与直播间福利的创意碰撞"></div>
<div class="field"><label>CASE 02 描述</label><input type="text" id="c2_desc" value="水墨江南意境，十惠鸭泛舟西湖寻找福利的故事"></div>
<div class="field"><label>CASE 03 描述</label><input type="text" id="c3_desc" value="武侠风格创意，十惠鸭端午破五毒的趣味叙事"></div>
<div class="field"><label>CASE 04 描述</label><input type="text" id="c4_desc" value="反差幽默，钓鱼梗与红包福利的惊喜结合"></div>
</div>

<div class="sc">
<h2>🔧 技术实现</h2>
<div class="row">
<div class="field"><label>工具1</label><input type="text" id="t1" value="ChatGPT · 脚本生成"></div>
<div class="field"><label>工具2</label><input type="text" id="t2" value="Midjourney · 视觉设计"></div>
</div>
<div class="row">
<div class="field"><label>工具3</label><input type="text" id="t3" value="Runway · 视频生成"></div>
<div class="field"><label>工具4</label><input type="text" id="t4" value="剪映 · 剪辑合成"></div>
</div>
</div>

<div class="sc">
<h2>📊 数据</h2>
<div class="row">
<div class="field"><label>数据1 数值</label><input type="text" id="d1_num" value="4"></div>
<div class="field"><label>数据1 单位</label><input type="text" id="d1_label" value="支TVC成片"></div>
</div>
<div class="row">
<div class="field"><label>数据2 数值</label><input type="text" id="d2_num" value="90%"></div>
<div class="field"><label>数据2 单位</label><input type="text" id="d2_label" value="成本降低"></div>
</div>
<div class="row">
<div class="field"><label>数据3 数值</label><input type="text" id="d3_num" value="3-5"></div>
<div class="field"><label>数据3 单位</label><input type="text" id="d3_label" value="天制作周期"></div>
</div>
</div>

<div class="sc">
<h2>🏁 页脚</h2>
<div class="field"><label>文字</label><input type="text" id="footer_text" value="十惠鸭品牌 · 直播电商 AI 赋能"></div>
<div class="field"><label>版权</label><input type="text" id="footer_cr" value="© 2026 十惠鸭品牌 · 直播间TVC创意方案"></div>
</div>

<div class="btn-group">
<button class="btn btn-p" onclick="saveConfig()">💾 保存配置</button>
<button class="btn btn-d" onclick="resetConfig()">↺ 恢复默认</button>
<button class="btn" onclick="window.open('./','_blank')">👁 预览页面</button>
<button class="btn" onclick="logout()">🚪 退出登录</button>
</div>
</div>

<div class="toast" id="toast"></div>

<script>
var ACCOUNT='2021687574',PASS='Zxc10231417';
var DEFAULTS={hero_subtitle:'直播间TVC创意与AI实践方案',hero_tag:'AI · CREATIVE · STRATEGY',hero_year:'2026 · 十惠鸭品牌',about_text:'本方案以"十惠鸭"IP为核心，融合江南水墨意境与AI技术，打造4支风格各异的TVC短片。从白蛇传说、端午民俗到江湖武侠、反差幽默，用AI重新定义品牌叙事。',h1_title:'AI全流程创作',h1_desc:'从剧本到成片，Midjourney + Runway实现"所想即所得"',h2_title:'AI分镜提示词公式',h2_desc:'【镜头类型】+【运镜方式】+【主体】+【环境】+【氛围】',h3_title:'统一IP视觉体系',h3_desc:'"十惠鸭"贯穿四个案例，打造品牌记忆锚点',h4_title:'低成本高效率',h4_desc:'成本仅为传统TVC的5%-10%，迭代速度快',c1_desc:'新中式意境融合，白蛇传说与直播间福利的创意碰撞',c2_desc:'水墨江南意境，十惠鸭泛舟西湖寻找福利的故事',c3_desc:'武侠风格创意，十惠鸭端午破五毒的趣味叙事',c4_desc:'反差幽默，钓鱼梗与红包福利的惊喜结合',t1:'ChatGPT · 脚本生成',t2:'Midjourney · 视觉设计',t3:'Runway · 视频生成',t4:'剪映 · 剪辑合成',d1_num:'4',d1_label:'支TVC成片',d2_num:'90%',d2_label:'成本降低',d3_num:'3-5',d3_label:'天制作周期',footer_text:'十惠鸭品牌 · 直播电商 AI 赋能',footer_cr:'© 2026 十惠鸭品牌 · 直播间TVC创意方案'};

function showToast(msg,ok){
  var t=document.getElementById('toast');
  t.textContent=msg;t.style.color=ok?'#c9a84c':'#e06060';
  t.classList.add('s');setTimeout(function(){t.classList.remove('s')},2500);
}
function doLogin(){
  var u=document.getElementById('loginUser').value.trim();
  var p=document.getElementById('loginPass').value;
  if(u===ACCOUNT&&p===PASS){
    document.getElementById('loginWrap').style.display='none';
    document.getElementById('panelWrap').classList.add('s');
    loadConfig();
  }else{
    document.getElementById('loginError').style.display='block';
  }
}
function logout(){
  document.getElementById('panelWrap').classList.remove('s');
  document.getElementById('loginWrap').style.display='flex';
  document.getElementById('loginPass').value='';
  document.getElementById('loginError').style.display='none';
}
function loadConfig(){
  try{
    var d=JSON.parse(localStorage.getItem('xizitvc_config')||'{}');
    Object.keys(DEFAULTS).forEach(function(k){
      var el=document.getElementById(k);
      if(el&&d[k]!==undefined)el.value=d[k];
    });
  }catch(e){}
}
function saveConfig(){
  var cfg={};
  Object.keys(DEFAULTS).forEach(function(k){
    var el=document.getElementById(k);
    if(el)cfg[k]=el.value;
  });
  localStorage.setItem('xizitvc_config',JSON.stringify(cfg));
  showToast('✅ 配置已保存！刷新主页面即可生效',true);
}
function resetConfig(){
  if(!confirm('恢复默认？当前修改会丢失。'))return;
  Object.keys(DEFAULTS).forEach(function(k){
    var el=document.getElementById(k);
    if(el)el.value=DEFAULTS[k];
  });
  localStorage.removeItem('xizitvc_config');
  showToast('↺ 已恢复默认',true);
}
// Enter key login
document.getElementById('loginPass').addEventListener('keydown',function(e){if(e.key==='Enter')doLogin()});
document.getElementById('loginUser').addEventListener('keydown',function(e){if(e.key==='Enter')document.getElementById('loginPass').focus()});
</script>
</body>
</html>'''

path = r'C:\Users\Designer\Desktop\西子湖畔交互展示\admin.html'
with open(path, 'w', encoding='utf-8') as f:
    f.write(admin)
print(f'Written: {len(admin)} bytes')
