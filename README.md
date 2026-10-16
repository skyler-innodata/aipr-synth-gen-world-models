# AIPR 2026 paper: Synthetic Video Generation for Robot Learning Using World Foundation Models

Working repository for the AIPR 2026 manuscript (Springer LNCS proceedings, final paper due October 22, 2026). Authors: Shrey Jha, Skyler Saucedo, Frank Tanner (Innodata).

## Layout

| Path | What it is |
|---|---|
| `paper/` | Draft 1: full paper in LNCS format with corrected numbers (Introduction, Related Work, Method, Experiments, Discussion, Conclusion, appendices). Build instructions in `paper/README.md`. |
| `paper2/` | Draft 2: slide-sequence outline in LNCS format using the deck's own numbers. |
| `draft-1/main.pdf`, `draft-2/main-v2.pdf` | Compiled PDFs of the two drafts. |
| `review/` | Analyses of the source material: slide-by-slide breakdown, Shrey's answers, working assumptions and their status, leakage measurement. |
| `review/images/` | Images extracted from the deck (videos are excluded from the repo by `.gitignore`). |
| `technical-details.md` | Every number used in the drafts, with source and confidence. |
| `SynthethicVideoGenerationForWorldFoundationModels-Review.md` | Full review of the presentation deck. |
| `CLAUDE.md` | Writing rules for the manuscript. |

Not in the repo (ignored): the original `.pptx` deck, embedded `.mp4` clips, `.zip` archives for Overleaf, and LaTeX build directories.

## Building

MiKTeX or TeX Live with `llncs`. From `paper/` or `paper2/`:

```
pdflatex -interaction=nonstopmode -output-directory=build main.tex
cd build && bibtex main && cd ..
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex
```
