"""Render only this critique, with column widths tuned to its required tables."""
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent))
import render_reports as renderer

default_widths=renderer.column_widths

def widths(rows,total):
    head=[c.get_text(' ',strip=True) for c in rows[0]]
    if len(head)==10 and head[0]=='Row / ticker':
        weights=[7,4,4,10,10,10,10,15,13,22]
    elif len(head)==9 and 'bottleneck' in head[0]:
        weights=[16,7,7,9,9,9,13,13,24]
    elif len(head)==5 and 'operating bridge' in head[1]:
        weights=[7,29,15,29,15]
    elif len(head)==7 and head[0]=='#':
        weights=[4,13,13,13,26,23,12]
    else:
        return default_widths(rows,total)
    return [total*w/sum(weights) for w in weights]

renderer.column_widths=widths
# An after-table spacer can spill onto a fresh page immediately before the
# renderer's orientation change, producing a footer-only page. No spacing is
# needed there because the next content changes page templates anyway.
original_spacer=renderer.Spacer
renderer.Spacer=lambda width,height: original_spacer(width,0 if height==10 else height)
if __name__=='__main__':
    renderer.render(ROOT.parent.parent/'Codex Critique of Claude 2026-11-08.md')
