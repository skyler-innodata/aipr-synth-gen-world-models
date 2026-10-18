# AIPR 2026 paper: Synthetic Video Generation for Robot Learning Using World Foundation Models

Working repository for the AIPR 2026 manuscript (Springer LNCS proceedings, final paper due October 22, 2026). Authors: Shrey Jha, Skyler Saucedo, Frank Tanner (Innodata).

## Layout

| Path | What it is |
|---|---|
| `paper/` | Draft 1: full paper in LNCS format with corrected numbers (Introduction, Related Work, Method, Experiments, Discussion, Conclusion, appendices). Build instructions in `paper/README.md`. |
| `paper2/` | Draft 2: slide-sequence outline in LNCS format using the deck's own numbers. |
| `paper3/` | Draft 3: draft 1's structure, notation and bibliography with the talk's narrative and imagery, compressed toward a short-paper length. Build instructions in `paper3/README.md`. |
| `paper3v2/` | LaTeX copy of draft 3 reserved for typesetting draft 4 later. Build with `bash paper3v2/build.sh`. |
| `draft-4-skyler/` | Draft 4 (current): section ideations in Markdown, several variants per section, reviewed with Skyler one section at a time. |
| `draft-5/`, `draft-7/` | Skyler's Google Docs drafts exported to PDF, with word-for-word transcription, analysis and shore-up lists (draft 5) and a review in md, tex, pdf and docx (draft 7). `draft-7/main.pdf` is draft 7 typeset in LNCS. |
| `draft-6/` | Draft 6: draft 5's structure with the confirmed numbers, numbered LNCS citations with URLs, the combined data-scaling figure, and a schema-complete Fig. 5 JSON. |
| `paper7/` | LaTeX source of draft 7, word for word, in LNCS format. Build with `bash paper7/build.sh`. |
| `policy-vs-data-amount/` | Data-scaling claims compiled from the six reference papers, CSVs, and the script that draws the paper's Fig. 1. |
| `draft-1/main.pdf`, `draft-2/main-v2.pdf`, `draft-3/main.pdf` | Compiled PDFs of drafts 1 to 3. |
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
