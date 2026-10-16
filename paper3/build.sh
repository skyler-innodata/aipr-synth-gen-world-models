#!/bin/bash
# Build draft 3 from paper3/: pdflatex -> bibtex -> pdflatex x2, output in build/.
# PATH is reduced to MiKTeX plus system dirs because MiKTeX's format builder aborts on
# PATH entries that are files rather than directories (this machine has one).
cd "$(dirname "$0")"
MIK="/c/Users/endle/AppData/Local/Programs/MiKTeX/miktex/bin/x64"
export PATH="$MIK:/c/Windows/system32:/c/Windows:/usr/bin:/bin"
export BIBINPUTS="$(pwd -W);" BSTINPUTS="$(pwd -W);"
mkdir -p build
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run1.txt 2>&1 || { echo "pass 1 failed"; tail -8 build/run1.txt; exit 1; }
(cd build && bibtex main | grep -i "warning\|error" | grep -v "MiKTeX updates")
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run2.txt 2>&1
pdflatex -interaction=nonstopmode -output-directory=build main.tex > build/run3.txt 2>&1
echo "errors:"; grep -n "^!" build/main.log | head
grep -A1 "Output written" build/main.log | tr -d '\n' | grep -o "([0-9]* pages"; echo
echo "overfull: $(grep -c Overfull build/main.log)"; grep -i "undefined" build/main.log | head -3
