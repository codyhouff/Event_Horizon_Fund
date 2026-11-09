"""Portable Markdown-to-PDF packaging with embedded fonts and wrapped tables.

Uses reportlab, markdown and beautifulsoup4. Does not alter source prose.
Set EHF_REPORT_DEPS to a dependency directory if packages are not installed.
"""
import html
import os
import re
import sys
from pathlib import Path

deps=os.environ.get('EHF_REPORT_DEPS',str(Path(os.environ.get('TEMP','C:/Temp'))/'ehf_report_deps_20261108'))
if Path(deps).exists(): sys.path.insert(0,deps)
import markdown
from bs4 import BeautifulSoup, NavigableString, Comment
from reportlab import rl_config
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, LongTable, TableStyle, PageBreak, NextPageTemplate

ROOT=Path(__file__).resolve().parents[2]
FONT=Path('C:/Windows/Fonts')
for name,file in [('EHF','arial.ttf'),('EHF-Bold','arialbd.ttf'),('EHF-Italic','ariali.ttf'),('EHF-BoldItalic','arialbi.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(FONT/file)))
pdfmetrics.registerFontFamily('EHF',normal='EHF',bold='EHF-Bold',italic='EHF-Italic',boldItalic='EHF-BoldItalic')
rl_config.warnOnMissingFontGlyphs=1
INK=colors.HexColor('#192b3c'); BLUE=colors.HexColor('#175b87')
styles={
 'body':ParagraphStyle('body',fontName='EHF',fontSize=10,leading=14.4,spaceAfter=7,textColor=INK,splitLongWords=True),
 'small':ParagraphStyle('small',fontName='EHF',fontSize=8,leading=10.5,spaceAfter=5,textColor=INK),
 'cell':ParagraphStyle('cell',fontName='EHF',fontSize=8,leading=10.8,textColor=INK,splitLongWords=True),
 'headcell':ParagraphStyle('headcell',fontName='EHF-Bold',fontSize=8,leading=10.5,textColor=colors.white),
 'h1':ParagraphStyle('h1',fontName='EHF-Bold',fontSize=22,leading=27,spaceBefore=6,spaceAfter=18,textColor=INK,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='EHF-Bold',fontSize=16,leading=20,spaceBefore=15,spaceAfter=11,textColor=BLUE,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='EHF-Bold',fontSize=12,leading=16,spaceBefore=12,spaceAfter=8,textColor=BLUE,keepWithNext=True),
 'h4':ParagraphStyle('h4',fontName='EHF-Bold',fontSize=10.5,leading=14,spaceBefore=10,spaceAfter=6,textColor=INK,keepWithNext=True),
}

def inline(node):
    if isinstance(node,Comment): return ''
    if isinstance(node,NavigableString): return html.escape(str(node))
    text=''.join(inline(c) for c in node.children)
    if node.name in ['strong','b']: return '<b>'+text+'</b>'
    if node.name in ['em','i']: return '<i>'+text+'</i>'
    if node.name=='code': return '<font color="#4b5360">'+text+'</font>'
    if node.name=='br': return '<br/>'
    if node.name=='a':
        href=node.get('href','')
        if href.startswith(('https://','http://')):
            return '<a href="'+html.escape(href,quote=True)+'" color="#175b87">'+text+'</a>'
    return text

class ReportDoc(BaseDocTemplate):
    def afterFlowable(self,flowable):
        if isinstance(flowable,Paragraph) and flowable.style.name in ['h1','h2','h3']:
            plain=flowable.getPlainText()
            level={'h1':0,'h2':1,'h3':2}[flowable.style.name]
            key='heading-'+str(self.seq.nextf('heading'))
            self.canv.bookmarkPage(key)
            self.canv.addOutlineEntry(plain,key,level=level,closed=level>0)

def footer(canvas,doc):
    width,height=canvas._pagesize
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor('#cdd7df'))
    canvas.line(38,31,width-38,31)
    canvas.setFont('EHF',7.5); canvas.setFillColor(colors.HexColor('#5a6771'))
    canvas.drawString(38,20,'EVENT HORIZON | Independent analysis | 2026-11-08')
    canvas.drawRightString(width-38,20,str(doc.page))
    canvas.restoreState()

def column_widths(rows,total):
    n=len(rows[0]); head=[c.get_text(' ',strip=True) for c in rows[0]]
    if n==9: weights=[5,11,10,13,10,10,9,6,26]
    elif n==8 and 'Action' in head: weights=[6,7,8,6,8,7,27,31]
    elif n==7 and any('2030 revenue' in x for x in head): weights=[16,15,14,17,12,13,18]
    else:
        weights=[]
        for i in range(n):
            lengths=sorted(len(row[i].get_text(' ',strip=True)) for row in rows[1:] if len(row)>i)
            typical=lengths[int(.75*(len(lengths)-1))] if lengths else 10
            weights.append(max(8,min(46,(max(typical,len(head[i]))**.65)*2)))
        if head[0]=='Ticker' and n>=5: weights[0]=8
    return [total*w/sum(weights) for w in weights]

def render(mdpath):
    source=mdpath.read_text(encoding='utf-8')
    soup=BeautifulSoup(markdown.markdown(source,extensions=['tables','fenced_code','sane_lists']), 'html.parser')
    pdfpath=mdpath.with_suffix('.pdf')
    doc=ReportDoc(str(pdfpath),pagesize=A4,leftMargin=42,rightMargin=42,topMargin=42,bottomMargin=43,
                  title=mdpath.stem,author='Independent Event Horizon research',pageCompression=1)
    templates=[]
    for name,size in [('portrait',A4),('wide',landscape(A4))]:
        width,height=size
        frame=Frame(42,43,width-84,height-85,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,id=name)
        templates.append(PageTemplate(id=name,frames=[frame],pagesize=size,onPage=footer))
    doc.addPageTemplates(templates)
    story=[]; orientation='portrait'
    nodes=[n for n in soup.children if getattr(n,'name',None)]
    for idx,node in enumerate(nodes):
        name=node.name
        if name=='table':
            rows=[tr.find_all(['th','td'],recursive=False) for tr in node.find_all('tr')]
            if not rows: continue
            target='wide' if len(rows[0])>=5 else 'portrait'
            if target!=orientation:
                story.extend([NextPageTemplate(target),PageBreak()]); orientation=target
            width=(landscape(A4) if target=='wide' else A4)[0]-84
            cells=[[Paragraph(inline(c),styles['headcell' if j==0 else 'cell']) for c in row] for j,row in enumerate(rows)]
            table=LongTable(cells,colWidths=column_widths(rows,width),repeatRows=1,hAlign='LEFT',splitByRow=1)
            table.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),INK),('VALIGN',(0,0),(-1,-1),'TOP'),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,colors.HexColor('#f0f4f7')]),
                ('LINEBELOW',(0,0),(-1,0),.5,INK),('LINEBELOW',(0,1),(-1,-1),.25,colors.HexColor('#dce3e8')),
                ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
                ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
            story.extend([table,Spacer(1,10)])
            continue
        switched=False
        if orientation!='portrait':
            story.extend([NextPageTemplate('portrait'),PageBreak()]); orientation='portrait'
            switched=True
        if name in ['h1','h2','h3','h4']:
            if name=='h2' and story and not switched: story.append(PageBreak())
            story.append(Paragraph(inline(node),styles[name]))
        elif name in ['p','blockquote']:
            story.append(Paragraph(inline(node),styles['body']))
        elif name in ['ol','ul']:
            for j,li in enumerate(node.find_all('li',recursive=False),1):
                lead=f'{j}. ' if name=='ol' else '• '
                story.append(Paragraph(html.escape(lead)+inline(li),styles['body']))
        elif name=='pre':
            for line in node.get_text().splitlines(): story.append(Paragraph(html.escape(line),styles['small']))
        elif name=='hr': story.append(Spacer(1,10))
    doc.build(story)
    print(str(pdfpath),pdfpath.stat().st_size)

if __name__=='__main__':
    if len(sys.argv)>1:
        for name in sys.argv[1:]: render(Path(name))
    else:
        render(ROOT/'inputs'/'Codex Deep Dive 2026-11-08.md')
        render(ROOT/'Deployment Strategy'/'Deployment Strategy 2026-11-08.md')
