# CLAUDE.md — Technical paper writing for peer-reviewed venues

This workspace exists to produce a technical paper for an academic venue (target venues in this family: IEEE conferences and transactions, CVPR/ICCV/ECCV, NeurIPS/ICML/ICLR, and applied venues such as AIPR). Everything written here must read as if a careful human researcher wrote it. Reviewers and area chairs now recognize machine-written prose on sight, and papers that trigger that recognition get read less charitably. The rules below exist to prevent that.

## 1. The deliverable

- The paper is the product. Slides, notes, and extracted assets are inputs.
- Default format: LaTeX using the venue's official template (IEEEtran, cvpr.sty, neurips_2026.sty). Do not invent a template. If no template is in the repo, ask which venue before producing the final LaTeX; drafting in Markdown first is fine.
- Keep a `paper/` folder with `main.tex`, `sections/*.tex`, `figures/`, `refs.bib`. Keep source material (`slides/`, `notes/`, `review/`) separate from the manuscript.
- Every claim that is not ours must carry a citation. Every number must trace to an experiment, a table, or a cited source. If the source is not known, write `[CITATION NEEDED]` or `[VERIFY: ...]` inline rather than inventing a reference or a figure. Never fabricate a BibTeX entry.

## 2. Voice and register

Write like a researcher explaining work to peers, not like an assistant summarizing a document.

- Use first person plural ("we") for what the authors did. Use plain declaratives for facts.
- Prefer concrete nouns and specific verbs. "We render 12,000 clips" beats "A substantial volume of clips is generated."
- Sentences vary in length. Some are short. Others carry a qualification, a reason, and a consequence in one breath, because that is how argument actually moves in a methods section.
- Hedge only where the evidence requires it, and hedge once. "Our results suggest" is fine; "may potentially suggest" is not.
- It is acceptable, and often better, to state a limitation bluntly: "This does not hold for scenes with more than two moving agents."
- Technical terms are defined once, at first use, then used consistently. Do not rotate synonyms for variety.
- Past tense for what was done, present tense for what is true or what the paper shows.

## 3. Things that make prose smell machine-written (do not do these)

These are patterns reviewers associate with LLM output. Avoid them in the manuscript, the abstract, the rebuttal, and the cover letter.

**Structural tells**
- Opening a section with a throat-clearing sentence that restates the heading ("In this section, we describe our methodology.").
- Three-item lists everywhere. Real papers list two things, or five, or write a paragraph.
- Every paragraph the same length. Every paragraph ending in a summarizing sentence.
- Bullet points in the Introduction, Related Work, or Discussion. Those sections are prose.
- A "contributions" list where every bullet begins with "We propose" / "We introduce" / "We demonstrate" in lockstep.
- Headers used as a substitute for transitions. If a subsection can be deleted and the argument still flows, delete it.
- Closing a section with "In summary," "Overall," or "Taken together."

**Lexical tells**
- Words and phrases to strike on sight: delve, leverage (as a verb), utilize, robust (unless statistically meant), seamless, holistic, paradigm, landscape, tapestry, crucial, pivotal, groundbreaking, novel (as self-praise), cutting-edge, state-of-the-art (unless comparing to a specific SOTA number), it is worth noting, it is important to note, notably, importantly, furthermore, moreover, additionally, in conclusion, overall, comprehensive, multifaceted, nuanced, underscore, highlight (as a verb), showcase, facilitate, foster, harness, unlock, empower, realm, embark, journey, testament, ever-evolving, rapidly evolving, in today's world, plays a crucial role, a wide range of, a variety of, not only ... but also, serves as, aims to, stands as.
- Em-dashes. Use a comma, a colon, a period, or parentheses. Never an em-dash.
- Rhetorical questions in the body text.
- Adjective stacking ("a powerful, flexible, and scalable framework").
- "This" with no noun after it ("This enables ..."). Write "This constraint enables ...".
- Exclamation marks. Anywhere.
- Sentences that begin with "By doing X, we Y." more than once per page.
- Vague intensifiers: significantly (unless a statistical test was run), substantially, greatly, dramatically, remarkably.

**Content tells**
- Claims of novelty without a specific contrast ("unlike prior work" with no citation).
- Related work written as a list of one-sentence summaries. Group work by idea, say how each group falls short for our setting, and say it in prose.
- A limitations section that only lists limitations that are actually strengths.
- Future work that is just the method applied to more data.
- Symmetric praise and criticism in equal measure. Have an opinion.

## 4. Section-by-section expectations

**Title.** Specific, under 12 words, no colon-subtitle unless the subtitle does real work. No "Towards," no "A Novel."

**Abstract.** 150–250 words, one paragraph. Problem, why existing approaches fall short, what we do, the main quantitative result with the number, and what it means. No citations in the abstract. No "In this paper."

**Introduction.** Opens on the problem, not on the field. By the end of the first paragraph the reader knows what is hard and why. Second paragraph: what others have done and the specific gap. Third: what we do and the key idea in one sentence. Contributions can be a short list, but phrase each as a finding or an artifact, not as an action verb. End with a sentence that tells the reader what the results show, with a number.

**Related Work.** Organized by theme, two to four paragraphs. Each paragraph ends by positioning our work relative to that theme. Cite generously; the point is to show the reviewers we know their papers.

**Method.** Notation introduced once, in a single place. Figures referenced before they are explained. Equations numbered only if referenced. Every design decision gets one sentence of justification, and where the justification is empirical, point to the ablation table.

**Experiments.** State the setup fully: data, splits, metrics, hardware, training budget, seeds. Report variance where feasible. Tables have bold for the best result and a caption that states the takeaway. Ablations isolate one factor each. If a result is negative, report it.

**Discussion / Limitations.** Honest. Specific. Short.

**Conclusion.** Three to five sentences. What was shown, what it changes, what remains open. No new claims.

## 5. Figures and tables

- Every figure has a caption that can be read standalone and states what to notice.
- Figure text is legible at print size (no smaller than 8pt after scaling).
- Vector formats (PDF/SVG) for plots; PNG for renders and screenshots.
- Tables use `booktabs` (`\toprule`, `\midrule`, `\bottomrule`), no vertical rules.
- Units in column headers, not in cells. Consistent decimal places within a column.
- Refer to figures and tables in text as "Fig. 3" and "Table 2" (IEEE) or "Figure 3" (NeurIPS), matching the template.

## 6. Citations and references

- BibTeX only. Use the venue-published entry (DBLP or the proceedings page), not an arXiv entry when a published version exists.
- Cite the original source for a method, not a survey that mentions it.
- `\citep` / `\citet` (natbib) or `\cite` (IEEEtran) consistently. Never cite as a sentence subject in IEEE style ("[12] showed"); write "Smith et al. [12] showed".
- Before submitting, run a pass for every `[CITATION NEEDED]` and `[VERIFY]` marker. None may remain.

## 7. Working process in this repo

- When asked to draft a section, draft the whole section, not an outline of it, unless asked for an outline.
- When editing, make the edit in place. Do not re-emit the whole file in chat.
- After drafting, run a self-check against Section 3 and remove every flagged pattern. Do this silently; the user does not need a changelog of the words you removed.
- When extracting material from slides or notes, preserve the author's actual phrasing and numbers. Mark gaps instead of filling them.
- Keep a `review/` folder for analyses of source material (slide breakdowns, literature notes). Those documents can be looser in tone than the manuscript, but still follow Section 3.
- Ask when a result, a dataset name, or a baseline is ambiguous. Do not guess at experimental numbers.

## 8. Quick self-review checklist (run before handing back any prose)

1. Did I open any paragraph by restating its heading? Cut it.
2. Any em-dash? Replace it.
3. Any word from the strike list? Replace or delete.
4. Three-item lists where the content did not naturally come in threes? Rewrite.
5. Any number without a source? Mark it.
6. Any paragraph that ends in a summary of itself? Cut the last sentence.
7. Could a reviewer paste the abstract into a detector and get a hit? Rewrite until no.
8. Does each section say something a smart reader could not have predicted from the heading?
