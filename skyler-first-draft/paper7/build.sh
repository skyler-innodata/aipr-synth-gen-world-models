#!/bin/bash
# Build draft 7 (paper7/main.tex) with pdflatex twice; output in build/, copy to ../main.pdf
# (skyler-first-draft/main.pdf).
# The bibliography is a thebibliography environment, so no bibtex pass is needed.
# PATH is reduced to MiKTeX plus system dirs because MiKTeX's format builder aborts on
# PATH entries that are files rather than directories (this machine has one).
cd "$(dirname "$0")"
MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"
mkdir -p build
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run1.txt 2>&1 || { echo "pass 1 failed"; grep -n "^!" -A3 build/main.log | head -20; exit 1; }
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run2.txt 2>&1
echo "errors:"; grep -n "^!" build/main.log | head
grep -o "Output written on [^(]*([0-9]* pages" build/main.log
echo "overfull: $(grep -c Overfull build/main.log)"; grep -i "undefined" build/main.log | head -3
cp build/main.pdf ../main.pdf && echo "copied to skyler-first-draft/main.pdf"
