# Paper working folder

Springer LNCS format (`llncs`, `splncs04`), as required by AIPR 2026 whose proceedings appear in LNCS. AIPR 2026 sets no page limit (confirmed 2026-10-16). Working target about 20 pages so length is driven by content. Final paper deadline: October 22, 2026, via Springer Meteor, with PDF, source, figure source files and a signed Springer Licence to Publish.

## Layout

- `main.tex`: preamble, title block, section includes, bibliography, appendix.
- `sections/*.tex`: one file per section. Edit these, not `main.tex`.
- `figures/`: PNG frames copied from `review/images/` and `review/leakage/`, plus `leakage_per_frame.pdf`. The pipeline diagram is TikZ inside `method.tex`.
- `refs.bib`: 30 entries, each verified against the publisher, PMLR, arXiv, or the official model card by the session that built it. Do not add an entry without checking it exists.
- `scripts/leakage_metric.py`: produces the numbers in Table "leakage" and `figures/leakage_per_frame.pdf`. Run as `python leakage_metric.py <orig.mp4> <gen.mp4> <mask.mp4> <out_dir>`.

## Compiling

MiKTeX 25.12 is installed locally (user profile) with auto-install of missing packages enabled. Build from `paper/` with output in `build/`:

```
pdflatex -interaction=nonstopmode -output-directory=build main.tex
cd build && bibtex main && cd ..
pdflatex -interaction=nonstopmode -output-directory=build main.tex
pdflatex -interaction=nonstopmode -output-directory=build main.tex
```

Set `BIBINPUTS` to the `paper/` directory before the bibtex step so it finds `refs.bib`. The same sources compile on Overleaf (pdfLaTeX) from `paper-overleaf.zip`. The compiled PDF and log are copied to `draft-1/` after each review pass.

## Draft markers

`\verify{...}` renders in red. Each one is either a placeholder tagged `A1`..`A6`/`D1`..`D3` (resolved by updating `review/assumptions.md` and then editing the sentence) or a fact only the authors can check. Before submission, `grep -rn verify sections/` must return nothing, and the `\newcommand{\verify}` line in `main.tex` should be deleted so a stray marker fails the build.

## Open placeholders at a glance

- A1 clip counts (intro, experiments setup, cost section)
- A2 whether the mask was a hard constraint (method controls, leakage, discussion)
- A3 raw footage duration (intro, setup)
- A4 guidance scale, steps, seed (generation)
- A5 filter criteria, proposal counts, GPT-4o mini system prompt (reasoning, guidance, appendix)
- A6 Predict2 prompts (action results, appendix)
- Author emails in `main.tex`
- Cosmos 3 Nano parameter count
- Token counts behind the $0.12 figure
