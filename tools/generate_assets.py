import math

PAPER="#EEF4F0"; PAPER2="#F6F9F7"; LINE="#C6D8CF"; PAT="#6F9C8E"
INK="#1C2B45"; PRINT="#2F3A5C"; MUTED="#6A7F77"; SEAL="#B8322C"
SANS="'Pretendard','Apple SD Gothic Neo','Malgun Gothic','Noto Sans KR','Noto Sans CJK KR',sans-serif"
MONO="'D2Coding','SFMono-Regular',Consolas,'Liberation Mono','Noto Sans Mono CJK KR',monospace"

def wave(x0,x1,cy,amp,ph,f1,f2,step=3):
    pts=[]
    x=x0
    while x<=x1:
        y=cy+amp*(0.62*math.sin(x/f1+ph)+0.38*math.sin(x/f2-2*ph))
        pts.append(f"{x:.1f},{y:.2f}")
        x+=step
    return "M"+" L".join(pts)

def guilloche(x0,x1,cy,amp,n,color,op,w=0.55,f1=38,f2=11):
    out=[]
    for i in range(n):
        ph=i*2*math.pi/n
        out.append(f'<path d="{wave(x0,x1,cy,amp,ph,f1,f2)}"/>')
    return f'<g fill="none" stroke="{color}" stroke-width="{w}" opacity="{op}">'+"".join(out)+'</g>'

# ---------------- header ----------------
def header():
    W,H=880,470
    rows=[
      ("1","세무사 시험 준비 2.5년","세법·회계 규정 해석"),
      ("2","금오공과대학교 컴퓨터공학","2026.08 졸업"),
      ("3","보살핌 Graph RAG","복약 위험 Recall 96.0%"),
      ("4","DarkAudit 룰 엔진","금융위 다크패턴 15유형 규칙화"),
      ("5","SSAFY 16기 데이터 트랙","교육 중"),
    ]
    micro=("금융과IT를잇는인터페이스 "*20)
    s=[]
    s.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="이정현, 금융과 IT를 잇는 인터페이스">')
    s.append(f'''<defs>
  <clipPath id="card"><rect x="1" y="1" width="{W-2}" height="{H-2}" rx="12"/></clipPath>
  <filter id="ink" x="-20%" y="-20%" width="140%" height="140%">
    <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="7" result="n"/>
    <feColorMatrix in="n" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -0.9 1.35" result="m"/>
    <feComposite in="SourceGraphic" in2="m" operator="in"/>
  </filter>
</defs>''')
    s.append(f'<g clip-path="url(#card)">')
    s.append(f'<rect width="{W}" height="{H}" fill="{PAPER}"/>')
    # security band
    s.append(f'<rect width="{W}" height="76" fill="#E1ECE6"/>')
    s.append(guilloche(-10,W+10,38,22,14,PAT,0.55))
    s.append(guilloche(-10,W+10,38,12,10,"#3F6F86",0.35,0.5,23,7))
    s.append(f'<line x1="0" y1="76" x2="{W}" y2="76" stroke="{LINE}"/>')
    s.append(f'<text x="0" y="86" font-family="{SANS}" font-size="5.2" fill="{PAT}" opacity="0.8" letter-spacing="0.4">{micro}</text>')
    # account tag on band
    s.append(f'<rect x="{W-252}" y="22" width="220" height="32" rx="4" fill="{PAPER}" stroke="{LINE}"/>')
    s.append(f'<text x="{W-240}" y="43" font-family="{MONO}" font-size="13" fill="{PRINT}" letter-spacing="0.5">계좌  github/Mystery2LEE</text>')
    # holder block
    s.append(f'<text x="44" y="118" font-family="{SANS}" font-size="12.5" fill="{MUTED}">예금주</text>')
    s.append(f'<text x="44" y="162" font-family="{SANS}" font-size="40" font-weight="800" fill="{INK}" letter-spacing="-0.5">이정현</text>')
    s.append(f'<text x="172" y="161" font-family="{SANS}" font-size="15" fill="{MUTED}">Lee Jeonghyun</text>')
    s.append(f'<text x="44" y="198" font-family="{SANS}" font-size="22" font-weight="700" fill="{INK}">금융과 IT를 잇는 인터페이스</text>')
    s.append(f'<text x="44" y="224" font-family="{SANS}" font-size="14" fill="{MUTED}">규정을 규칙으로, 데이터를 검증 가능한 판단으로. Data &amp; AI Engineer</text>')
    # seal
    cx,cy=770,158
    s.append(f'<g transform="rotate(-9 {cx} {cy})" filter="url(#ink)" opacity="0.95">'
             f'<circle cx="{cx}" cy="{cy}" r="44" fill="none" stroke="{SEAL}" stroke-width="4"/>'
             f'<circle cx="{cx}" cy="{cy}" r="37" fill="none" stroke="{SEAL}" stroke-width="1.4"/>'
             f'<text x="{cx}" y="{cy-11}" text-anchor="middle" font-family="{SANS}" font-size="21" font-weight="800" fill="{SEAL}">이정</text>'
             f'<text x="{cx}" y="{cy+17}" text-anchor="middle" font-family="{SANS}" font-size="21" font-weight="800" fill="{SEAL}">현인</text>'
             f'</g>')
    # ledger
    top=252; rh=27
    cols=[44,92,420]
    s.append(f'<line x1="32" y1="{top}" x2="{W-32}" y2="{top}" stroke="{INK}" stroke-width="1.2"/>')
    for x,t in zip(cols,["No","적요","기록"]):
        s.append(f'<text x="{x}" y="{top+18}" font-family="{SANS}" font-size="12" fill="{MUTED}">{t}</text>')
    s.append(f'<line x1="32" y1="{top+rh}" x2="{W-32}" y2="{top+rh}" stroke="{LINE}"/>')
    for i,(n,a,b) in enumerate(rows):
        y=top+rh*(i+1)
        s.append(f'<text x="{cols[0]+4}" y="{y+19}" font-family="{MONO}" font-size="13" fill="{PRINT}">{n}</text>')
        s.append(f'<text x="{cols[1]}" y="{y+19}" font-family="{MONO}" font-size="14" fill="{PRINT}">{a}</text>')
        s.append(f'<text x="{cols[2]}" y="{y+19}" font-family="{MONO}" font-size="14" fill="{PRINT}">{b}</text>')
        s.append(f'<line x1="32" y1="{y+rh}" x2="{W-32}" y2="{y+rh}" stroke="{LINE}"/>')
    y=top+rh*(len(rows)+1)
    s.append(f'<text x="{cols[0]+4}" y="{y+19}" font-family="{MONO}" font-size="13" fill="{PRINT}">6</text>')
    s.append(f'<text x="{cols[1]}" y="{y+19}" font-family="{MONO}" font-size="14" fill="{INK}" font-weight="700">다음 거래</text>')
    s.append(f'<text x="{cols[2]}" y="{y+19}" font-family="{MONO}" font-size="14" fill="{INK}" font-weight="700">금융권 IT·AI 개발</text>')
    s.append(f'<rect x="{cols[2]+146}" y="{y+6}" width="8" height="16" fill="{INK}"><animate attributeName="opacity" values="1;1;0;0" keyTimes="0;0.5;0.5;1" dur="1.1s" repeatCount="indefinite"/></rect>')
    s.append('</g>')
    s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="12" fill="none" stroke="#B7CCC2"/>')
    s.append('</svg>')
    return "\n".join(s)

# ---------------- slips ----------------
def boxes(x,y,txt,strong):
    out=[]; bw=24; bh=34; gap=3
    for i,ch in enumerate(txt):
        bx=x+i*(bw+gap)
        out.append(f'<rect x="{bx}" y="{y}" width="{bw}" height="{bh}" rx="2" fill="{"#FFFFFF" if strong else "none"}" stroke="{INK if strong else LINE}" stroke-width="{1.2 if strong else 1}"/>')
        out.append(f'<text x="{bx+bw/2}" y="{y+24}" text-anchor="middle" font-family="{MONO}" font-size="19" font-weight="{700 if strong else 400}" fill="{INK if strong else MUTED}">{ch}</text>')
    return "".join(out), len(txt)*(bw+gap)-gap

def slip(no, stub, title, desc, metric, before, after, blabel, alabel, side_label, side_value, stack):
    W,H=880,196; SX=206
    s=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}: {desc}">']
    s.append(f'''<defs><mask id="punch"><rect width="{W}" height="{H}" fill="#fff"/>
<circle cx="{SX}" cy="0" r="9" fill="#000"/><circle cx="{SX}" cy="{H}" r="9" fill="#000"/></mask></defs>''')
    s.append(f'<g mask="url(#punch)">')
    s.append(f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="8" fill="{PAPER2}" stroke="#B7CCC2"/>')
    s.append(f'<path d="M8.5 0.5 H{SX} V{H-0.5} H8.5 a8 8 0 0 1 -8 -8 V8.5 a8 8 0 0 1 8 -8Z" fill="#E4EEE8"/>')
    s.append(f'<g clip-path="none">{guilloche(0,SX,H-26,9,8,PAT,0.35,0.5,21,7)}</g>')
    s.append(f'<line x1="{SX}" y1="12" x2="{SX}" y2="{H-12}" stroke="{PAT}" stroke-width="1.2" stroke-dasharray="2 5" stroke-linecap="round"/>')
    s.append('</g>')
    s.append(f'<text x="24" y="36" font-family="{MONO}" font-size="12" fill="{MUTED}">전표 No.{no}</text>')
    yy=66
    for k,v in stub:
        s.append(f'<text x="24" y="{yy}" font-family="{SANS}" font-size="11.5" fill="{MUTED}">{k}</text>')
        s.append(f'<text x="24" y="{yy+18}" font-family="{SANS}" font-size="14" font-weight="600" fill="{INK}">{v}</text>')
        yy+=44
    X=SX+30
    s.append(f'<text x="{X}" y="50" font-family="{SANS}" font-size="27" font-weight="800" fill="{INK}" letter-spacing="-0.3">{title}</text>')
    s.append(f'<text x="{X}" y="78" font-family="{SANS}" font-size="14.5" fill="#3E4C5E">{desc}</text>')
    s.append(f'<line x1="{X}" y1="98" x2="{W-30}" y2="98" stroke="{LINE}"/>')
    s.append(f'<text x="{X}" y="124" font-family="{SANS}" font-size="12.5" fill="{MUTED}">{metric}</text>')
    b,bw_=boxes(X,136,before,False)
    s.append(b)
    s.append(f'<text x="{X}" y="186" font-family="{SANS}" font-size="11.5" fill="{MUTED}">{blabel}</text>')
    ax=X+bw_+26
    s.append(f'<path d="M{ax} 153 h30 m-7 -6 l7 6 l-7 6" fill="none" stroke="{INK}" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>')
    X2=ax+50
    a,_=boxes(X2,136,after,True)
    s.append(a)
    s.append(f'<text x="{X2}" y="186" font-family="{SANS}" font-size="11.5" fill="{INK}" font-weight="600">{alabel}</text>')
    RX=650
    s.append(f'<line x1="{RX-24}" y1="116" x2="{RX-24}" y2="182" stroke="{LINE}"/>')
    s.append(f'<text x="{RX}" y="124" font-family="{SANS}" font-size="12.5" fill="{MUTED}">{side_label}</text>')
    s.append(f'<text x="{RX}" y="152" font-family="{MONO}" font-size="16" font-weight="700" fill="{INK}">{side_value}</text>')
    s.append(f'<text x="{RX}" y="178" font-family="{MONO}" font-size="11.5" fill="{MUTED}">{stack}</text>')
    s.append('</svg>')
    return "\n".join(s)

open("assets/header.svg","w").write(header())
open("assets/slip-darkaudit.svg","w").write(slip("01",
  [("구분","2026 금융 AI Challenge"),("역할","Data Engineer · 2인 팀")],
  "DarkAudit","금융상품 가입 화면의 다크패턴을 설계 단계에서 점검하는 UX 컴플라이언스 도구",
  "다크패턴 탐지 Precision","0.49","1.00","Rule Engine 단독","Rule + LLM 의미 검증","F1 score","0.66 → 0.77","FastAPI SQLAlchemy Docker"))
open("assets/slip-bosalpim.svg","w").write(slip("02",
  [("구분","캡스톤 디자인"),("역할","팀장 · Graph RAG 담당")],
  "보살핌","식약처 DUR 지식그래프로 간접 위험까지 찾는 고령자·1인 가구 복약 안전 서비스",
  "위험 조합 탐지 Recall (테스트 50건)","45.7%","96.0%","Vanilla RAG","Graph RAG","지식그래프 규모","성분 1,473 · 금기 1,313","Neo4j NestJS GPT-4o-mini"))
open("assets/slip-chatbot.svg","w").write(slip("03",
  [("구분","학부 프로젝트"),("역할","RAG 파이프라인 단독")],
  "학교 챗봇","크롤링부터 평가까지, 근거 있는 답변을 만드는 하이브리드 검색 RAG 파이프라인",
  "답변 근거 충실도 Faithfulness (Ragas)","76.1%","83.1%","개선 전","하이브리드 검색 + 리랭킹","Precision (Ragas)","62.5% → 70.4%","Qdrant bge-m3 Ragas"))
print("ok")
