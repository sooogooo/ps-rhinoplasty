# -*- coding: utf-8 -*-
"""鼻整形站 SVG 插图批量生成器（统一品牌视觉，文件名与正文引用对齐）"""
import os
D = os.path.dirname(os.path.abspath(__file__))

def svg(body, w=1200, h=520):
    head = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + str(w) + ' ' + str(h) + '" role="img" aria-label="鼻整形插图">'
    head += '<defs><linearGradient id="blue" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#0a6cb8"/><stop offset="100%" stop-color="#7ec3eb"/></linearGradient>'
    head += '<linearGradient id="gold" x1="0" y1="0" x2="1" y2="0"><stop offset="0%" stop-color="#d4a437"/><stop offset="100%" stop-color="#e8c068"/></linearGradient></defs>'
    head += '<rect width="' + str(w) + '" height="' + str(h) + '" fill="#f4f9fc"/>'
    return head + body + '</svg>'

def title(t, x=40, y=64):
    return ('<text x="%d" y="%d" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="32" font-weight="700" fill="#1c2b39">%s</text>'
            '<rect x="40" y="80" width="120" height="6" rx="3" fill="url(#blue)"/>' % (x,y,t))

def numbered_card(t, num, color="#0a6cb8"):
    return ('<g transform="translate(280,170)"><rect width="640" height="180" rx="18" fill="#fff" stroke="%s" stroke-width="2"/>'
            '<circle cx="60" cy="60" r="28" fill="%s"/><text x="60" y="71" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="30" font-weight="700" fill="#fff">%s</text>'
            '<text x="110" y="72" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="26" font-weight="700" fill="#1c2b39">%s</text>'
            '<rect x="40" y="120" width="120" height="5" rx="3" fill="url(#blue)"/></g>' % (color,color,str(num),t))

def a1_nasal_anatomy():
    b = title("鼻部：结构与功能")
    b += '<g transform="translate(60,150)"><rect width="1080" height="280" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<text x="60" y="46" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#0a6cb8">外鼻结构</text>'
    b += '<text x="60" y="100" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">鼻梁 · 鼻尖 · 鼻翼</text>'
    b += '<text x="60" y="140" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">鼻骨 · 鼻小柱</text>'
    b += '<text x="60" y="190" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">鼻中隔软骨 · 下外侧软骨</text>'
    b += '<line x1="560" y1="40" x2="560" y2="250" stroke="#d6e1ea" stroke-width="2"/>'
    b += '<text x="600" y="46" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#d4a437">功能</text>'
    b += '<text x="600" y="100" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">通气 · 加湿 · 嗅觉</text>'
    b += '<text x="600" y="140" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">鼻塞可能来自结构或黏膜</text>'
    b += '<text x="600" y="190" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" fill="#5a6c7c">形态与功能常需一起考虑</text>'
    b += '</g>'
    b += '<text x="600" y="492" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">鼻整形理解结构与功能，才能不只盯着外观</text>'
    return svg(b)

def fenzhen_overview():
    b = title("先别急着做：分诊红线")
    items=[("炎症/感染","#b3261e"),("鼻部占位","#b3261e"),("凝血异常","#b3261e"),("血糖未控","#b3261e"),("发育期","#d4a437")]
    x0=60; w=210; gap=26
    for i,(t,c) in enumerate(items):
        x=x0+i*(w+gap)
        b += '<g transform="translate(%d,190)"><rect width="%d" height="170" rx="16" fill="#fff" stroke="%s" stroke-width="2"/>' % (x,w,c)
        b += '<path d="M %d 55 L %d 45 L %d 55 L %d 45 L %d 55 L %d 45 L %d 55" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % (w/2, w/2-16, w/2-8, w/2+8, w/2+16, w/2, w/2, c)
        b += '<text x="%d" y="130" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" font-weight="700" fill="#1c2b39">%s</text>' % (w/2,t)
        b += '</g>'
    b += '<text x="600" y="430" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#b3261e">先排除危险信号，再谈鼻整形</text>'
    return svg(b)

def tongqi_cause():
    b = title("鼻塞的两类原因")
    b += '<g transform="translate(60,150)"><rect width="500" height="280" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<text x="250" y="46" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#0a6cb8">结构性</text>'
    b += '<text x="250" y="110" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="17" fill="#5a6c7c">鼻中隔偏曲</text>'
    b += '<text x="250" y="170" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">通道被挤窄</text>'
    b += '<text x="250" y="230" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">可考虑矫正</text></g>'
    b += '<g transform="translate(640,150)"><rect width="500" height="280" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<text x="250" y="46" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#d4a437">炎症性</text>'
    b += '<text x="250" y="110" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="17" fill="#5a6c7c">鼻甲肥大 · 黏膜</text>'
    b += '<text x="250" y="170" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">黏膜肥厚</text>'
    b += '<text x="250" y="230" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">先用药物控制</text></g>'
    b += '<text x="600" y="492" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">先到耳鼻喉科明确病因，再谈整形</text>'
    return svg(b)

def a9_revision_timeline():
    b = title("二次修复时机")
    b += '<g transform="translate(60,160)"><rect width="1080" height="260" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<line x1="60" y1="150" x2="1100" y2="150" stroke="#d6e1ea" stroke-width="3"/>'
    marks=[("术后早期","肿胀未退",80,"#d4a437"),("6月","逐步稳定",340,"#4a9fd4"),("1年","基本稳定",600,"#0a6cb8"),("更久","多次修复·瘢痕多",860,"#b3261e")]
    for label,desc,x,c in marks:
        b += '<circle cx="%d" cy="150" r="11" fill="%s"/><text x="%d" y="120" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" font-weight="700" fill="#1c2b39">%s</text><text x="%d" y="190" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="14" fill="#5a6c7c">%s</text>' % (x,c,x,label,x,desc)
    b += '</g>'
    b += '<text x="600" y="470" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">需等恢复稳定再评估，二次手术本身又形成新瘢痕</text>'
    return svg(b)

def a10_prep_checklist():
    b = title("鼻整形前要准备什么")
    items=[("术前检查","#0a6cb8"),("停抗凝药","#0a6cb8"),("戒烟戒酒","#4a9fd4"),("清洁鼻腔","#4a9fd4"),("沟通与影像","#d4a437")]
    x0=60; w=210; gap=26
    for i,(t,c) in enumerate(items):
        x=x0+i*(w+gap)
        b += '<g transform="translate(%d,190)"><rect width="%d" height="190" rx="16" fill="#fff" stroke="%s" stroke-width="2"/>' % (x,w,c)
        b += '<circle cx="%d" cy="45" r="22" fill="%s"/><text x="%d" y="54" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="24" font-weight="700" fill="#fff">%d</text>' % (w/2,c,w/2,i+1)
        b += '<text x="%d" y="130" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="18" font-weight="700" fill="#1c2b39">%s</text>' % (w/2,t)
        b += '</g>'
    b += '<text x="600" y="450" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="22" font-weight="700" fill="#0a6cb8">遵医嘱 · 如实告知病史与用药</text>'
    return svg(b)

def a11_nose_timeline():
    b = title("鼻子要恢复多久")
    b += '<g transform="translate(60,150)"><rect width="500" height="330" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<line x1="90" y1="40" x2="90" y2="300" stroke="#0a6cb8" stroke-width="4" stroke-linecap="round"/>'
    stages=[("第1周","肿胀·淤青·鼻夹板",50),("2-4周","部分消退",130),("1-3月","逐步自然",205),("6月以上","逐渐稳定",280)]
    for t,d,y in stages:
        b += '<circle cx="90" cy="%d" r="12" fill="#0a6cb8"/><text x="115" y="%d" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="19" font-weight="700" fill="#1c2b39">%s</text><text x="115" y="%d" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="15" fill="#5a6c7c">%s</text>' % (y,y-2,t,y+18,d)
    b += '</g>'
    b += '<g transform="translate(640,150)"><rect width="500" height="330" rx="16" fill="#fff" stroke="#d6e1ea"/>'
    b += '<text x="26" y="46" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="20" font-weight="700" fill="#d4a437">恢复快慢因人而异</text>'
    b += '<text x="26" y="100" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="17" fill="#5a6c7c">基础条件、范围、是否合并功能手术</text>'
    b += '<text x="26" y="136" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="17" fill="#5a6c7c">会影响恢复与最终形态</text>'
    b += '<rect x="26" y="180" width="440" height="70" rx="12" fill="#fff7ea" stroke="#f0c05a"/><text x="46" y="228" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#8a6d1c">恢复与鼻型稳定需时间，不能几天就定型</text>'
    b += '</g>'
    b += '<text x="600" y="500" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="16" fill="#7a8a98">把恢复期分成阶段看，管理预期</text>'
    return svg(b)

def a12_postop_signals():
    b = title("术后护理与并发症信号")
    items=[("肿胀持续加重","#b3261e"),("持续出血","#b3261e"),("感染发热","#b3261e"),("皮肤发白发紫","#b3261e"),("剧烈疼痛","#d4a437")]
    x0=60; w=210; gap=26
    for i,(t,c) in enumerate(items):
        x=x0+i*(w+gap)
        b += '<g transform="translate(%d,190)"><rect width="%d" height="200" rx="16" fill="#fff" stroke="%s" stroke-width="2"/>' % (x,w,c)
        b += '<path d="M %d 62 L %d 52 L %d 62 L %d 52 L %d 62 L %d 52 L %d 62" fill="none" stroke="%s" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>' % (w/2, w/2-16, w/2-8, w/2+8, w/2+16, w/2, w/2, c)
        b += '<text x="%d" y="155" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="17" font-weight="700" fill="#1c2b39">%s</text>' % (w/2,t)
        b += '</g>'
    b += '<text x="600" y="458" text-anchor="middle" font-family="PingFang SC,Microsoft YaHei,sans-serif" font-size="24" font-weight="700" fill="#b3261e">一出现，第一时间联系医生</text>'
    return svg(b)

def series_card(name, titles, color):
    out={}
    for i,t in enumerate(titles):
        out[name+str(i+1)+".svg"] = svg(numbered_card(t, i+1, color))
    return out

FENZHEN = ["分诊红线总览","活动性炎症","鼻部占位","凝血功能","血糖未控","免疫力低下","发育期","修复史与妊娠","心理评估"]
TONGQI = ["鼻子不通气先别急","鼻塞的两类原因","鼻中隔偏曲","鼻甲肥大","两个方向","功能与形态兼顾","先控制炎症","先做专科检查","先到耳鼻喉科"]
CAILIAO = ["隆鼻材料怎么选","三类材料总览","硅胶的优点","硅胶的局限","膨体的优点","膨体的局限","自体软骨三种来源","医生选材料依据","先分诊再方案"]
BUZHOU = ["鼻综合整体搭配","鼻综合整体部位","鼻梁塑形","鼻小柱支撑","鼻尖支架成形","鼻翼调整","鼻骨内推","面诊评估","整体协调设计"]

files = {
  "a1-nasal-anatomy.svg": a1_nasal_anatomy(),
  "fenzhen.svg": fenzhen_overview(),
  "tongqi1.svg": tongqi_cause(),
  "a9-revision-timeline.svg": a9_revision_timeline(),
  "a10-prep-checklist.svg": a10_prep_checklist(),
  "a11-nose-timeline.svg": a11_nose_timeline(),
  "a12-postop-signals.svg": a12_postop_signals(),
}
series = [
  ("fenzhen", FENZHEN, "#b3261e"),
  ("tongqi", TONGQI, "#0a6cb8"),
  ("cailiao", CAILIAO, "#d4a437"),
  ("buzhou", BUZHOU, "#0a6cb8"),
]
for prefix, titles, color in series:
    files.update(series_card(prefix, titles, color))

for name, content in files.items():
    with open(os.path.join(D,name),"w",encoding="utf-8") as f:
        f.write(content)
print("生成", len(files), "个 SVG")
