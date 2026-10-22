#!/bin/bash
# Build "AIPR 2026 Paper-oct22" from oct-22/paper/main.tex (PDF, pdflatex twice) and from
# oct-22/AIPR 2026 Paper-oct22.md (DOCX via pandoc). Figures are read from oct-22/figures
# through \graphicspath; the loop below also copies them next to main.tex so the paper/
# folder can be zipped for Springer as-is (that copy is git-ignored).
# PATH is reduced to MiKTeX plus system dirs because MiKTeX's format builder aborts on
# PATH entries that are files rather than directories.
cd "$(dirname "$0")"
OUT=".."
NAME="AIPR 2026 Paper-oct22"
MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
PANDOC="/c/Users/endle/AppData/Local/Pandoc/pandoc.exe"
[ -x "$PANDOC" ] || PANDOC=pandoc

mkdir -p build figures
for f in fig2-pipeline fig3-source-clip fig4-reasoning-output fig6-countertop-blue fig7-pillow-stuffing fig8-directional-reversal fig7-variants-oct22; do
  [ -f "figures/$f.png" ] || cp "../figures/$f.png" figures/
done

export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run1.txt 2>&1 || { echo "pass 1 failed"; grep -n "^!" -A3 build/main.log | head -20; exit 1; }
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run2.txt 2>&1
echo "errors:"; grep -n "^!" build/main.log | head
grep -o "Output written on [^(]*([0-9]* pages" build/main.log
echo "overfull: $(grep -c Overfull build/main.log)"; grep -i "undefined" build/main.log | head -3
cp build/main.pdf "$OUT/$NAME.pdf" && echo "wrote $OUT/$NAME.pdf"

"$PANDOC" "$OUT/$NAME.md" -s -o "$OUT/$NAME.docx" --resource-path="$OUT" \
  && echo "wrote $OUT/$NAME.docx" || { echo "pandoc docx failed"; exit 1; }
