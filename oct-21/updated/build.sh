#!/bin/bash
# Build "AIPR 2026 Paper-updated" in three formats from oct-21/updated/main.tex and
# oct-21/AIPR 2026 Paper-updated.md:
#   PDF  : pdflatex twice on main.tex (LNCS, thebibliography, no bibtex pass)
#   DOCX : pandoc from the markdown, with the dollar signs the manuscript uses
#          restored (the .md writes "USD" amounts without "$" so it renders cleanly)
# PATH is reduced to MiKTeX plus system dirs because MiKTeX's format builder aborts on
# PATH entries that are files rather than directories (see skyler-first-draft/paper7/build.sh).
cd "$(dirname "$0")"
OUT=".."
NAME="AIPR 2026 Paper-updated"
MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
PANDOC="/c/Users/endle/AppData/Local/Pandoc/pandoc.exe"
[ -x "$PANDOC" ] || PANDOC=pandoc

mkdir -p build figures
for f in fig2-pipeline fig3-source-clip fig4-reasoning-output fig6-countertop-blue fig7-pillow-stuffing fig8-directional-reversal fig9-variant-examples; do
  [ -f "figures/$f.png" ] || cp "../figures/$f.png" figures/
done

export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run1.txt 2>&1 || { echo "pass 1 failed"; grep -n "^!" -A3 build/main.log | head -20; exit 1; }
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run2.txt 2>&1
echo "errors:"; grep -n "^!" build/main.log | head
grep -o "Output written on [^(]*([0-9]* pages" build/main.log
echo "overfull: $(grep -c Overfull build/main.log)"; grep -i "undefined" build/main.log | head -3
cp build/main.pdf "$OUT/$NAME.pdf" && echo "wrote $OUT/$NAME.pdf"

# DOCX from the markdown, restoring the manuscript's dollar signs for the Word copy.
sed -e 's/between 3 to 25 USD/between $3 to $25 USD/' \
    -e 's/data is 3 - 25 USD per hour/data is $3 - $25 USD per hour/' \
    -e 's/we spend 96 USD for GPU/we spend $96 USD for GPU/' \
    "$OUT/$NAME.md" > build/docx-source.md
"$PANDOC" build/docx-source.md -s -o "$OUT/$NAME.docx" --resource-path="$OUT" \
  && echo "wrote $OUT/$NAME.docx" || { echo "pandoc docx failed"; exit 1; }
