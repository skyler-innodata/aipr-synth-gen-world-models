#!/bin/bash
# Build draft-7-review.md into LaTeX, PDF and DOCX (output in draft-7/review/).
# PATH is reduced for pdflatex because MiKTeX's format builder aborts on PATH entries
# that are files rather than directories (see paper3/build.sh).
cd "$(dirname "$0")"
mkdir -p review
PANDOC="/c/Users/endle/AppData/Local/Pandoc/pandoc.exe"
[ -x "$PANDOC" ] || PANDOC=pandoc

"$PANDOC" draft-7-review.md -s -o review/draft-7-review.tex \
  -V documentclass=article -V fontsize=11pt -V geometry:margin=1in \
  -V colorlinks=true -V linkcolor=blue -V urlcolor=blue \
  --number-sections --toc --toc-depth=2 || { echo "pandoc tex failed"; exit 1; }

"$PANDOC" draft-7-review.md -s -o review/draft-7-review.docx --number-sections --toc --toc-depth=2 \
  || { echo "pandoc docx failed"; exit 1; }

MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"
cd review
pdflatex -interaction=nonstopmode draft-7-review.tex > run1.txt 2>&1 || { echo "pass 1 failed"; grep -n "^!" -A3 draft-7-review.log | head -20; exit 1; }
pdflatex -interaction=nonstopmode draft-7-review.tex > run2.txt 2>&1
echo "errors:"; grep -n "^!" draft-7-review.log | head
grep -o "Output written on [^(]*([0-9]* pages" draft-7-review.log
echo "overfull: $(grep -c Overfull draft-7-review.log)"
