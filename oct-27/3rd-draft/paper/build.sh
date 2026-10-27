#!/bin/bash
# Build "AIPR 2026 Paper-3rd-draft": the Fig. 1 diagram from fig1-pipeline.tex (pdflatex, then
# rendered and trimmed to ../figures/fig2-pipeline.png), the PDF from main.tex (pdflatex twice,
# LNCS, inline bibliography), and the DOCX from the markdown via pandoc with implicit figures
# off, so Word shows the captions only and not the image alt text (Frank's comment C17).
# PATH is reduced to MiKTeX plus system dirs because MiKTeX's format builder aborts on
# PATH entries that are files rather than directories.
cd "$(dirname "$0")"
OUT=".."
NAME="AIPR 2026 Paper-3rd-draft"
MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
PANDOC="/c/Users/endle/AppData/Local/Pandoc/pandoc.exe"
[ -x "$PANDOC" ] || PANDOC=pandoc
mkdir -p build figures

# Fig. 1 diagram: compiled and rendered with the full PATH, since PIL needs conda's DLL dirs.
PATH="$MIK:$PATH" pdflatex -interaction=nonstopmode -output-directory=build fig1-pipeline.tex > build/fig1.txt 2>&1 || { echo "fig1 failed"; grep -n "^!" -A3 build/fig1-pipeline.log | head; exit 1; }
python -X utf8 - <<'PY'
import pypdfium2 as pdfium
from PIL import Image, ImageChops
page = pdfium.PdfDocument('build/fig1-pipeline.pdf')[0]
im = page.render(scale=4).to_pil().convert('RGB')
bg = Image.new('RGB', im.size, 'white')
bbox = ImageChops.difference(im, bg).getbbox()
im = im.crop((bbox[0]-20, bbox[1]-20, bbox[2]+20, bbox[3]+20))
im.save('../figures/fig2-pipeline.png', optimize=True)
print('fig2-pipeline.png', im.size)
PY

for f in fig2-pipeline fig3-source-clip fig4-reasoning-output fig6-countertop-blue fig7-pillow-stuffing fig6-reversal-oct22 fig7-variants-oct22; do
  cp "../figures/$f.png" figures/
done

# Main build with the reduced PATH (MiKTeX's format builder aborts on PATH entries that are files).
export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"

pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run1.txt 2>&1 || { echo "pass 1 failed"; grep -n "^!" -A3 build/main.log | head -20; exit 1; }
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run2.txt 2>&1
echo "errors:"; grep -n "^!" build/main.log | head
grep -o "Output written on [^(]*([0-9]* pages" build/main.log
echo "overfull: $(grep -c Overfull build/main.log)"; grep -i "undefined" build/main.log | head -3
cp build/main.pdf "$OUT/$NAME.pdf" && echo "wrote $OUT/$NAME.pdf"

"$PANDOC" "$OUT/$NAME.md" -f markdown-implicit_figures -s -o "$OUT/$NAME.docx" --resource-path="$OUT" \
  && echo "wrote $OUT/$NAME.docx" || { echo "pandoc docx failed"; exit 1; }
