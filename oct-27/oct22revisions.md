# Frank's review of the 22 October manuscript

Source: `oct-27/AIPR 2026 Paper-oct22-edits.docx`, the 22 October Word export (`oct-22/AIPR 2026 Paper-oct22.docx`) returned by Frank Tanner with tracked changes and comments. All revisions are by one author ("Tanner, Franklin") and were made on 23 October 2026 between 09:51 and 12:14 (Eastern). None of the comments is marked resolved.

The base text of the file is the 22 October text word for word (the only differences are non-breaking spaces after "et al." and "vol." and an ellipsis glyph, both produced by the pandoc export). So the list below is the complete set of Frank's edits. Nothing was changed outside the tracked changes.

What Frank left: 9 text edits (insert/delete pairs), 1 formatting edit (italics on three model names), and 12 comments, one of which is a reply to his own comment. He did not touch the Abstract (he liked it), Sec. 2.3, the figure captions (he checked them in the PDF and signed off), the Fig. 4 and Fig. 5 paragraphs, Sec. 4's first paragraph, the Disclosure, or the References.

Line numbers below refer to `oct-22/paper/main.tex`, where the edits have to be applied. The Word file is a derived artifact; do not edit it directly.

## 1. Tracked text edits

| # | Section | Before | After | main.tex | Recommendation |
|---|---|---|---|---|---|
| 1 | 1 Introduction, last paragraph | "increase the amount of trainable data" | "increase the amount of ML training data" | 66 | Accept. |
| 2 | 1.1 Background | "NVIDIA Cosmos consists of three models:" | "Our pipeline employs three pieces of the NVIDIA Cosmos family of models:" | 70 | Accept the intent, reword. See comment C10 below; Frank's wording is not accurate for what the pipeline uses. |
| 3 | 1.1 Background | Predict, Transfer, Reason in roman | Predict, Transfer, Reason in italics | 70 | Accept. Use `\emph{}` in LaTeX. See C12. |
| 4 | 2.1, last sentence | "about 130 seconds per clip on one A100." | "about 130 seconds per clip on one A100 class GPU." | 106 | Accept, hyphenated: "one A100-class GPU". Sec. 3 says "an A100 80 GB", so the two can stay as they are. |
| 5 | 2.2, principle 2 | "despite prompting the color change of the counter" | "despite prompting only to change the color of the counter" | 116 | Accept. |
| 6 | 2.2, principle 3 | "We conjecture this is because the model was trained on" | "Our conjecture is that the model was trained on" | 117 | Accept. |
| 7 | 3 Results, first paragraph | "Every variant was inspected" | "Every variant was visually inspected" | 133 | Accept. |
| 8 | 4 Closing the Gap, cost paragraph | "What the pipeline buys is variation at scale" | "This pipeline provides variation at scale" | 173 | Accept. |
| 9 | 5 Conclusion | "who need more egocentric video" | "who need more video" | 177 | Accept. |

Edits 1, 4 to 9 are plain wording changes with no effect on claims or numbers. Edit 2 changes a factual statement and needs care (Sec. 2, C10).

## 2. Comments

Comment IDs are the Word comment numbers. Quoted text is Frank's, verbatim.

### C1. Author block: "Let's do away with titles. We're all just Innodata."

Anchored on the three affiliation lines (Physical AI Intern; Robotics and Physical AI Solutions Architect; VP Robotics and Computer Vision).

Action: drop the job titles. With one shared affiliation the LNCS class takes a single `\institute{Innodata}` and no `\inst{n}` superscripts on the names; the ORCID superscripts stay. In `main.tex` lines 41 to 48:

```latex
\author{Shrey Jha\orcidID{0009-0003-5044-4187} \and
Skyler Saucedo\orcidID{0009-0005-7005-7736} \and
Franklin~Tanner\orcidID{0009-0003-6814-2291}}
\authorrunning{S. Jha et al.}

\institute{Innodata}
```

Open point this reopens: Springer's instructions ask for city and country in the affiliation and for a corresponding-author email (`oct-21/oct-21-status-and-todo.md`, Sec. 4). The 22 October decision was to match the accepted AIPR 2025 papers and omit both. With the titles gone, "Innodata" alone is a thin affiliation line; "Innodata, Ridgefield Park, NJ, USA" would satisfy Springer without adding titles. [VERIFY: which office to list, and whether Frank wants an email.]

### C3. Abstract: "Awesome - great abstract!"

No action.

### C7. Introduction, last paragraph: "'a world foundation model' is a little ambiguous. Which model?"

Anchored on "a world foundation model then reads the first frame of each egocentric clip" (line 66).

Action: name it. The reasoner is Cosmos 3 Nano, which the Abstract already names. Replacement:

> Recordings are first cut into short clips with NVIDIA Cosmos Curate, and NVIDIA Cosmos 3 Nano then reads the first frame of each egocentric clip and provides a structured ontology of the scene.

The Background paragraph that follows introduces what Cosmos is, so the name can stand alone here.

### C10. Background: "I reworded because I believe that cosmos 3.0 has refactored this into a single united model. If you don't like this wording, please feel free to revert"

Anchored on edit 2. Frank's reason is right: the paragraph's last sentence already says Cosmos 3 folds the three models into one, so "NVIDIA Cosmos consists of three models" in the present tense contradicts it. His replacement, "Our pipeline employs three pieces of the NVIDIA Cosmos family of models: Predict ...; Transfer ...; Reason ...", has its own problem: the pipeline does not use Reason (it uses Cosmos 3 Nano for reasoning) and uses Predict only in the reversal experiment, not in the main pipeline. A reader who then meets Cosmos 3 Nano and Transfer 2.5 in the Method would be confused about which three pieces were meant.

Recommended wording, which keeps Frank's point and the chronology straight:

> World foundation models are large-scale artificial intelligence systems trained to understand, simulate, and predict the physical world, including how objects move, interact, and follow the laws of physics [6]. NVIDIA released Cosmos as three models: *Predict* forecasts future frames from text, an image, or a video [7]; *Transfer* adapts a video across environments under multi-control conditioning on depth, segmentation, edge, and blurred-RGB maps [8, 9]; *Reason* is a vision-language model for physical scene understanding [10]. Alongside the models, Cosmos Curate is the platform's video curation pipeline, which splits recordings at shot boundaries and prepares clips for the models [6]. Cosmos 3 folds the three models into one, with an autoregressive subnetwork that reasons about a scene and a diffusion-based subnetwork that generates video, audio, and actions conditioned on that reasoning [11]. Our pipeline uses Curate, the Cosmos 3 Nano reasoner, and Transfer 2.5.

The last sentence is new and answers Frank's "which pieces" question directly. Note the 22 October change log records that "family" was replaced by "three models" deliberately; Frank's edit reverses that, and the wording above avoids both.

### C12. Background: "I added italics here since these are common verbs and we want the reader to know that these are the model names."

Action: accept. Apply `\emph{Predict}`, `\emph{Transfer}`, `\emph{Reason}` at first mention only (line 70). Do not italicize "Cosmos Transfer 2.5" or "Cosmos 3 Nano" elsewhere; with the Cosmos prefix they are not ambiguous.

### C17 and C18. Fig. 1 caption: "This is weird formatting for the caption. Make sure this is cleaned-up in the camera ready version." Reply: "I looked at the PDF version. It looks clean"

Anchored on the Fig. 1 block. The oddity is that the Word export shows the alt text ("Block diagram of the pipeline: an egocentric clip goes to ...") as a paragraph above "Fig. 1. The Pipeline". That is how pandoc renders the markdown image alt text; the PDF has only the caption. Frank withdrew the concern after checking the PDF.

Action: none for the manuscript. If another Word round is needed, strip the alt text from the image lines before running pandoc so the .docx matches the PDF, or Frank will see the same thing again on every figure.

### C19. Method: "I still don't know what a 'reasoning tower' is. If you think this is a term of art that the reader would know, please discard this comment. Otherwise, maybe rephrase to 'reasoning process'? I'm just getting stuck on the 'tower' concept."

Anchored on "the reasoning tower of Cosmos 3 Nano" (line 83). "Tower" is not a term the Cosmos 3 report uses for the public; our own Background sentence calls it "an autoregressive subnetwork that reasons about a scene". Frank raised the same question on an earlier draft ("still"), so it should be settled now.

Action: replace with the paper's own term so the Method matches the Background:

> The first frame of each clip is passed to the reasoning subnetwork of Cosmos 3 Nano [11, 13], a vision-language model that returns ...

"Tower" also appears in the Fig. 1 alt text (`oct-22/alt-text.csv`, row for Fig. 1, and the markdown image line) and may be printed inside the Fig. 1 diagram itself. [VERIFY: open `oct-22/figures/fig2-pipeline.png` and check the block label; if it says "reasoning tower", relabel it.]

### C21. Sec. 2.1: "Stylistically, I don't like having a question in the middle of a paragraph. I'd rather have an assertion such as 'We are attempting to answer the question: "does adding variations of the color of bucket, countertop, and/or rags affect the outcome of the robot training policy?"'"

Anchored on "If we decide to change the color of the bucket, countertop, or rags, does that permutation affect the outcome of the robot training policy?" (line 96). The repo's writing rules also ban rhetorical questions in body text, so this was already an open item.

Action: replace the question with a declarative. Frank's suggestion still contains a question mark inside the quotation; a cleaner version:

> We want to know whether varying the color of the bucket, countertop, or rags changes the outcome of the robot training policy.

The same objection applies to the Conclusion, which Frank did not mark: "Lastly, more questions need to be explored, such as does structured reasoning about a scene produce better variations than random augmentation?" (line 177). Suggested replacement:

> Lastly, whether structured reasoning about a scene produces better variations than random augmentation remains untested.

### C22. Fig. 3 caption: "I saw in the pdf version that all of the captions look correct so I'm not reviewing these."

No action. Frank did not review captions in the Word file; the PDF captions stand.

### C35. Results: "Predict2? Not sure where the 2 came from?"

Anchored on "Predict2 renderings took about 3.5 minutes" (line 133). The model is NVIDIA Cosmos Predict2 2B Video2World, reference [7] in the list, which was used for the two action-level renders (the cable-winding clip in Fig. 6 and the paper-rotation clip not shown). Its name is correct, but the Method never introduces it, so the Results is the first place the reader meets it with no cite. This was already flagged as open in the 22 October change log.

Action, two parts:

1. In Sec. 2, after the Transfer 2.5 sentence at the end of the Method's second paragraph (line 85), add one sentence:

   > For action-level changes, such as the cord reversal in Fig. 6, we instead use Cosmos Predict2 [7], which generates the clip from the first frame and the text prompt alone rather than from control maps.

2. In Results (line 133), write "Cosmos Predict2 [7] renderings took about 3.5 minutes" so the cite is adjacent.

Related open item, not raised by Frank but relevant to the same sentence: the prompt records in `supporting-docs/technical-details.md` say the two recovered Predict2 cable prompts asked for winding with the block fixed, not for a reversal, and Shrey has not yet confirmed that the "spaghetti" render in Fig. 6 was prompted as a reversal. This should be settled before the Fig. 6 paragraph is finalized.

### C37. Fig. 6/7: "I find it odd that you go back to appearance perturbation in the section about directional reversal. I'd recommend moving the appearance figure above the reversal experiment discussion. Maybe with the caption 'another example of color perturbation on a cable winding video'. You'll need to fix some of the transition in order to do that."

Anchored on "Fig. 7 places the source desk clip and its appearance variant side by side." (line 160). This sentence was added on 22 October only to give Fig. 7 a citation in the text; Frank is right that it is a non sequitur at the end of the physics-failure paragraph.

Action: reorder so the Results run appearance, appearance, appearance, then the one failed action change, and the section ends on the limitation. Concretely in `main.tex`:

1. Move the `fig:variants` figure block (lines 162 to 167) to just after the pillow paragraph (after line 151). It becomes Fig. 6; the reversal figure becomes Fig. 7. LaTeX renumbers automatically.
2. New caption for the desk figure:

   > Another example of color permutation, on the cable-winding clip: source (left) and variant with the desk and shelf recolored blue (right).

3. New short paragraph after the desk figure, in place of the orphaned sentence:

   > Fig. 6 shows the same kind of appearance change on the cable-winding clip: the desk and shelf are recolored and the hands and cable are preserved. We used this clip to test a change of a different kind.

4. The reversal paragraph (line 160) then opens unchanged ("We did observe some limitations ...") and drops its last sentence ("Fig. 7 places ..."). Change "In Fig. 6" to "In Fig. 7" in it, or rely on `\ref`.
5. Update the figure order in `oct-22/alt-text.csv`, the markdown manuscript, and the README figure list (Sec. 7, "Figures" bullet), which currently describe the order Fig. 6 reversal, Fig. 7 variants.

The desk figure is set at 0.36 of the line width; once it sits between two full-width figures it will look small. Consider 0.5 or match the reversal figure's 0.8.

## 3. Work list

Accept directly (no judgment needed):

- Edits 1, 4, 5, 6, 7, 8, 9 (Sec. 1 table).
- Italics on Predict, Transfer, Reason (C12).
- Remove job titles from the author block (C1).

Apply with the rewording proposed above:

- Background sentence on the Cosmos models, with the added "our pipeline uses" sentence (edit 2, C10).
- "a world foundation model" to "NVIDIA Cosmos 3 Nano" (C7).
- "reasoning tower" to "reasoning subnetwork" in the Method and the Fig. 1 alt text (C19).
- Rhetorical question in Sec. 2.1 to a declarative, and the same for the Conclusion (C21).
- Introduce Cosmos Predict2 in the Method and cite it in Results (C35).
- Move the desk-clip figure above the reversal paragraph, recaption, rewrite the transition, renumber (C37).

Needs an author decision:

- Affiliation line: "Innodata" alone, or with city and country, and whether to add a corresponding email (C1).
- Whether the Fig. 1 diagram image itself needs relabeling (C19).
- Whether the Fig. 6 render was in fact a reversal prompt (C35, carried over from the 22 October open items).

After the edits: rebuild with `bash oct-22/paper/build.sh` (or in a new `oct-27/paper/` copy), regenerate the markdown and Word export, and reply to Frank's comments in the Word file or by message so he knows which of his suggestions were taken as written and which were reworded (C10 and C21 in particular, since he offered alternatives).
