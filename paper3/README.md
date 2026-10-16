# Draft 3 working folder

Springer LNCS format (`llncs`, `splncs04`) for AIPR 2026. Draft 3 keeps the academic structure and bibliography of draft 1 (`paper/`) and tells the story in the order and register of the talk (`paper2/`): running example first, then the three-stage pipeline, ontology-driven variation, the four guidance maps and the subtraction mask, results from success to failure, and the open question. The Method section keeps draft 1's notation and the mask equation. Figures are the deck's own frames; the pipeline diagram is a TikZ redraw of slide 6 because the slide screenshot is not legible at page width.

## Layout

- `main.tex`: preamble, title block, section includes, bibliography.
- `sections/*.tex`: one file per section. Edit these, not `main.tex`.
- `figures/`: PNG frames copied from `paper2/figures/` (deck exports). `pipeline_slide.png` is a crop of slide 6 kept for reference; the paper uses the TikZ figure in `method.tex` instead.
- `refs.bib`: the draft 1 bibliography with `url`, `doi` and `note` fields removed to save space. Entries are otherwise identical to `paper/refs.bib`; restore the DOIs from there if Springer asks for them.
- `build.sh`: full pdflatex, bibtex, pdflatex, pdflatex cycle into `build/`, with the page count and overfull-box count printed at the end.

## Compiling

MiKTeX 25.12 is installed in the user profile at `C:\Users\endle\AppData\Local\Programs\MiKTeX\miktex\bin\x64` (not on PATH). `cm-super` is installed so T1 text is Type 1 rather than bitmap. Run `bash build.sh` from this folder in Git Bash. The script shortens PATH to MiKTeX plus the system directories because MiKTeX's format builder aborts when a PATH entry is a file rather than a directory, which is the case on this machine.

The compiled PDF and log are copied to `draft-3/` after each pass.

## Length

Draft 3 compiles to 9 LNCS pages: about 7.7 pages of content and 1.3 pages of references (21 entries). Six pages was the target. A full LNCS text page holds about 480 words; the five figures and two tables take about two pages and the references 1.3, so six pages would leave roughly 1,200 words of body text against the 2,300 here. Reaching six would mean some combination of: dropping two figures (the ontology excerpt and the failure strip are the candidates), cutting the bibliography to about 12 entries, and halving the Method and Results prose. Six LNCS pages corresponds to about three pages in the two-column IEEE format AIPR used in earlier years.
