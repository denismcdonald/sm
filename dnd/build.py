"""Rebuild index.html with Python 3; no third-party packages required."""
from pathlib import Path
import base64, html, re
ROOT = Path(__file__).resolve().parent
source = (ROOT / 'DnD World.md').read_text(encoding='utf-8')
parts = re.split(r'^# (.+)\s*$', source, flags=re.M)
entries = [(parts[i].strip(), parts[i+1].strip()) for i in range(1,len(parts),2)]
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')
def render(text):
    # Paragraphs, line breaks and subheadings cover the supplied Obsidian note.
    blocks=[]
    for p in re.split(r'\n\s*\n', text):
        m=re.match(r'^(#{2,5}) (.+)$',p)
        if m: blocks.append(f'<h{len(m[1])+1}>{html.escape(m[2])}</h{len(m[1])+1}>')
        else: blocks.append('<p>'+html.escape(p).replace('\n','<br>')+'</p>')
    return '\n'.join(blocks)
original = 'data:image/jpeg;base64,' + base64.b64encode((ROOT/'DnD Map.jpeg').read_bytes()).decode()
image = 'data:image/png;base64,' + base64.b64encode((ROOT/'map-corrected.png').read_bytes()).decode()
toc=''.join(f'<a href="#{slug(t)}"><span>{i:02}</span>{html.escape(t)}</a>' for i,(t,_) in enumerate(entries))
sections=[]
for i,(title,body) in enumerate(entries):
    if title=='Map':
        content=f'''<figure><button class="map-open" aria-label="Open Dale’s map at full size" onclick="showMap()"><img src="{image}" width="1600" height="1200" alt="Dale’s hand-drawn map of Sharal, showing settlements, roads, mountains, forests and neighbouring territories."></button><figcaption><span>Dale's map</span><span class="map-actions"><button class="text-button map-toggle" onclick="toggleMap()" aria-pressed="false">Original photo</button><button class="text-button" onclick="showMap()">View full size</button></span></figcaption></figure>'''
    else: content='<div class="prose">'+render(body)+'</div>'
    sections.append(f'<section id="{slug(title)}" aria-labelledby="heading-{slug(title)}"><div class="section-heading"><span class="number">{i:02}</span><h2 id="heading-{slug(title)}">{html.escape(title)}</h2><a class="back" href="#contents" aria-label="Back to contents from {html.escape(title)}">Contents ↑</a></div>{content}</section>')
page=(ROOT/'template.html').read_text(encoding='utf-8').replace('{{CONTENTS}}',toc).replace('{{SECTIONS}}','\n'.join(sections)).replace('{{MAP}}',image).replace('{{ORIGINAL}}',original)
(ROOT/'index.html').write_text(page,encoding='utf-8')
print('Built index.html:',len(entries),'sections')
