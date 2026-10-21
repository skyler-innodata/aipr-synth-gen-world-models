# AIPR 2026 paper: status as of 21 October 2026 and what remains

Audience: Shrey, Skyler, Frank. This file records what was done on 20 and 21 October, what the three output files in this folder are, how every reference was verified, and the list of things only the authors can settle before the paper goes to Springer. Final paper is due 22 October 2026 via Springer Meteor.

## 1. What was done

### 1.1 EgoScale wording (20 October)

The reviewing editor flagged that EgoScale does not claim 20,854 hours are needed per task. A full read of the EgoScale paper (references/2602.16710v1.pdf) confirmed this and found three further problems with how the draft used it. The findings are recorded here because the 21 October revision only partly addressed them (see Section 4.2).

- The 20,854 hours is the Stage I pretraining corpus for one VLA, spanning 6,015 tasks and 43,237 objects. Per-task robot data is 100 teleoperated demonstrations (20 for shirt rolling).
- The scaling plot (EgoScale Fig. 5 right) varies the pretraining corpus at 1k, 2k, 4k, 10k, 20k hours with the per-task demos held fixed. Average task completion goes 0.30, 0.45, 0.48, 0.57, 0.71. The authors state there is no saturation.
- 0.71 is not an upper limit. It is the value at the largest scale tested. The best EgoScale model (pretrain plus mid-train) averages 0.83 completion and 0.56 binary success.
- EgoScale fits a log-linear law to validation loss, not to completion score. The dashed line in our data-scaling figure is our own fit.
- "Task completion score" is a partial-credit rubric. The draft's "mean acceptable score, defined as the robot's ability to successfully complete the task" conflates it with binary success.

Suggested replacement text for the abstract sentence, the introduction paragraph, the cost paragraph, and the Fig. 1a caption was given in chat on 20 October and is reproduced in Section 4.2 below.

### 1.2 Frank's question on the "emergent property of VLAs" sentence (20 October)

Frank asked why reference [8] was cited for "We believe this is an emergent property of VLAs struggling to fully understand the physical world" and whether the claim holds. Findings:

- Reference [8] is the Cosmos-Predict2 model card. Its Limitations section does list "disappearing or morphing objects, unrealistic interactions, and implausible motions," but says nothing about emergence, and the model is a diffusion video model, not a VLA.
- The Cosmos platform paper [7] is the right source: Sec. 5.3.2 says "all the WFMs equally struggle with physics adherence" and names object impermanence, deformation, and implausible kinematics; Sec. 9 adds contact-rich dynamics and instruction following.
- "Emergent" is the wrong word. A failure to conserve mass is a documented limitation of the model class, not a capability that appeared with scale.
- The narrower mechanism: the model has only a denoising objective over captioned video, and in a Transfer run the edge, depth, and segmentation controls are computed from the source clip, so they encode the original winding direction and work against a prompt asking for the reverse.
- Larger problem: the repo's own records (claude-drafts/draft-5/draft-5-analysis.md, item 71) say the recovered Predict2 prompt asked for winding the cable with the block held fixed, not a reversal, and that both Predict2 runs produced no visible motion. Fig. 8 shows two near-identical frames, which matches "no motion" and not the "spaghetti" description.

The 21 October revision removed the sentence and the [8] citation. The paragraph describing the reversal experiment is still there, and the Fig. 8 caption now carries the author note "(find better example showing spaghetti)". Shrey needs to confirm whether a reversal run with the spaghetti frames exists (Section 4.3).

### 1.3 Repository sync

- Commit e7d997d (20 October) added the oct-19 folder (Skyler's 19 October export, transcription, revised markdown with renumbered references, itemised diff) and the README rewrite.
- Commit dfe59f2 (Skyler, 21 October) added oct-21/ with the Springer instructions PDF, the revisions PDF, and shrey-refs.
- Local main was fast-forwarded to dfe59f2. Two root-level PDFs remain untracked because they are byte-identical to copies already in the repo (the draft-7 export and the oct19 export).

### 1.4 Springer LNCS requirements that matter for us

From oct-21/Instructions+for+Authors+PDF.pdf (the link.springer.com page redirects to a cookie wall and could not be fetched; the PDF is the same document):

- LaTeX or Word template from Springer. Submit all source files, the PDF, and the bib or bbl file. Avoid long file names.
- Author names final at submission; no changes after. ORCIDs in superscript next to names. One corresponding author, marked in the header, with a mandatory email.
- Headings in title case, left aligned, only two levels numbered, no "0" numbering.
- Short papers 6 to 11 pages, full papers 12 to 15 or more.
- Figures: caption below, tables caption above, lettering no smaller than 6 pt, vector graphics where possible, legible in black and white, cross-referenced in text.
- Citations by number in square brackets, list in order of citation or alphabetical, list and text must match exactly, DOIs strongly encouraged, CrossRef-conformant entries.
- Alt text for all figures (EU Accessibility Act); either the PC chairs ask authors or the typesetters do it.
- Acknowledgments and a Disclosure of Interests statement as third-level headings at the end, before the references. The disclosure is now required ("The authors have no competing interests to declare that are relevant to the content of this article." or specific statements).
- Signed license-to-publish from the corresponding author, by hand, no digital signatures.

### 1.5 The three output files

| File | What it is |
|---|---|
| oct-21/AIPR 2026 Paper-updated.pdf | The revisions draft typeset word for word in LNCS. 10 pages, no LaTeX errors, no overfull lines. Built from oct-21/updated/main.tex. |
| oct-21/AIPR 2026 Paper-updated.docx | Same text, built by pandoc from the markdown, seven figures embedded. |
| oct-21/AIPR 2026 Paper-updated.md | Same text in Markdown. Dollar amounts are written "3 to 25 USD" because a dollar sign breaks Markdown rendering; the PDF and DOCX keep the draft's dollar signs. |

Rebuild all three with:

```
bash oct-21/updated/build.sh
```

The script runs pdflatex twice (MiKTeX path is set inside the script), copies the PDF up one level, restores the dollar signs into a scratch copy of the markdown, and runs pandoc for the DOCX. Figures are in oct-21/figures/ and were checked pixel-size for pixel-size against the images embedded in the revisions PDF.

### 1.6 Word-for-word check

The body text of the new PDF was diffed word by word against the revisions PDF. The only differences are:

- Section numbers (the draft numbers the abstract as 1 and the introduction as 2; LNCS leaves the abstract unnumbered and starts at 1).
- Figure numbers (see Section 4.1).
- Heading capitalisation ("Closing the gap" is set as "Closing the Gap", per Springer).
- Three spacing fixes that are extraction artefacts, not wording: "0.71.π0" set as "0.71. π0", "[4] .And" set as "[4]. And", and "Cosmos ," set as "Cosmos,".

Every typo in the draft is preserved (Section 4.4).

## 2. Reference verification

The rule from the editor is no arXiv references. Shrey's audit (oct-21/shrey-refs) was the starting point; every entry was then checked by fetching the URL on 21 October, and DOIs were resolved through the Crossref API. Entry numbers are the manuscript's, which differ from the numbering in shrey-refs.

| # | Work | Old link | New link | Status |
|---|---|---|---|---|
| 1 | EgoScale (Zheng et al.) | arXiv 2602.16710 | research.nvidia.com/labs/gear/egoscale/ | Project page, 200. Still a technical report, no venue. |
| 2 | pi0 (Black et al.) | arXiv 2410.24164 | roboticsproceedings.org/rss21/p010.html, DOI 10.15607/RSS.2025.XXI.010 | RSS 2025 proceedings, 200. Shrey's note said RSS 2025 but gave the arXiv link. |
| 3 | LingBot-VLA (Wu et al.) | arXiv 2601.18692 | technology.robbyant.com/lingbot-vla | Project page, 200. Technical report, no venue. |
| 4 | Lin et al., data scaling laws | arXiv 2410.18647 | proceedings.iclr.cc .../88b7b2c896506daabc8d3fd587055167-Abstract-Conference.html | ICLR 2025 oral, 200. Shrey's "openreview" URL was actually this proceedings hash. The real OpenReview id is pISLZG7ktL. |
| 5 | FieldGen (Wang et al.) | arXiv 2510.20774 | fieldgen.github.io | Project page, 200. Under review, no venue. Not cited in the revised text. |
| 6 | MimicGen (Mandlekar et al.) | arXiv 2310.17596 | proceedings.mlr.press/v229/mandlekar23a.html | CoRL 2023, PMLR 229:1820-1864, 200. |
| 7 | Cosmos platform (NVIDIA) | arXiv 2501.03575 | research.nvidia.com/publication/2025-01_cosmos-world-foundation-model-platform-physical-ai | NVIDIA Research page, 200. Technical report. |
| 8 | Cosmos-Predict2 card | unchanged | huggingface.co/nvidia/Cosmos-Predict2-2B-Video2World | 200. |
| 9 | Cosmos-Transfer1 | arXiv 2503.14492 | research.nvidia.com/labs/cosmos-lab/cosmos-transfer1/ | Cosmos Lab page, 200. Technical report. |
| 10 | Cosmos 2.5 (World Simulation...) | arXiv 2511.00062 | research.nvidia.com/publication/2025-09_world-simulation-video-foundation-models-physical-ai | NVIDIA Research page, 200. Technical report. |
| 11 | Cosmos-Reason1 | arXiv 2503.15558 | research.nvidia.com/labs/cosmos-lab/cosmos-reason1/ | Cosmos Lab page, 200. The NVIDIA publication page uses a different title, so the lab page was chosen. |
| 12 | Cosmos 3 | arXiv 2606.02800 | research.nvidia.com/labs/cosmos-lab/cosmos3/ | Cosmos Lab page, 200. Technical report PDF is linked from it. |
| 13 | ControlNet (Zhang et al.) | arXiv 2302.05543 | DOI 10.1109/ICCV51070.2023.00355 | ICCV 2023, Crossref confirms. Pages changed to IEEE pagination 3813-3824 (draft had CVF pagination 3836-3847). Not cited in the revised text. |
| 14 | Gen-1 (Esser et al.) | arXiv 2302.03011 | DOI 10.1109/ICCV51070.2023.00675 | ICCV 2023, Crossref confirms. Pages 7312-7322 (draft had 7346-7356). Not cited in the revised text. |
| 15 | TransNet V2 (Soucek, Lokoc) | arXiv 2008.04838 | DOI 10.1145/3664647.3685517 | ACM Multimedia 2024, pp. 11218-11221, Crossref confirms. Shrey's note said arXiv-only; that is wrong. |
| 16 | Cosmos3-Nano card | unchanged | huggingface.co/nvidia/Cosmos3-Nano | 200. |
| 17 | GPT-4o mini (OpenAI) | unchanged | openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/ | Returns 403 to automated requests; canonical URL confirmed by search. Opens in a browser. |
| 18 | SAM 2 (Ravi et al.) | arXiv 2408.00714 | proceedings.iclr.cc .../45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html | ICLR 2025 oral, 200. OpenReview id Ha6RTeWMd0 confirmed via the OpenReview search API. |
| 19 | Cosmos-Transfer2.5 card | unchanged | huggingface.co/nvidia/Cosmos-Transfer2.5-2B | 200. |
| 20 | Canny 1986 | unchanged | DOI 10.1109/TPAMI.1986.4767851 | Crossref confirms. |
| 21 | Depth Anything V2 (Yang et al.) | arXiv 2406.09414 | proceedings.neurips.cc .../26cfdcd8fe6fd75cc53e92963a656c58-Abstract-Conference.html | NeurIPS 2024 proceedings, 200. |

Seven entries (1, 3, 5, 7, 9, 10, 11, 12) remain technical reports or project pages with no peer-reviewed venue. That is the honest state of the literature; they are cited as such rather than as arXiv preprints.

## 3. Author identity

All three ORCIDs were resolved against the public ORCID registry on 21 October and return the right names: Shrey Jha 0009-0003-5044-4187, Skyler Saucedo 0009-0005-7005-7736, Franklin Tanner 0009-0003-6814-2291. The revisions draft had a stray "D" at the end of Skyler's; it is dropped in the outputs. Affiliation is set to Innodata, as in draft 7.

## 4. What we need to do

### 4.1 Springer blockers (must be fixed or the paper will bounce)

1. **Corresponding author.** Pick one, mark them in the header, and supply the email. The PDF currently shows a visible placeholder "[VERIFY: corresponding author email]" under the affiliation. Springer says the corresponding author also signs the license-to-publish by hand.
2. **Keywords.** The LNCS template expects a keywords line after the abstract. The draft has none. Suggest three to five, for example: synthetic data, world foundation models, egocentric video, robot learning, data augmentation.
3. **Reference list must match the text.** References 5 (FieldGen), 13 (ControlNet), and 14 (Gen-1) are listed but no longer cited anywhere, because the FieldGen sentence and the "Transfer descends from ControlNet and Gen-1" sentence were cut in this revision. Either restore those sentences or delete the three entries and renumber 6 to 21. The renumbering touches every citation from [6] onward.
4. **Disclosure of Interests.** Required. Add a third-level heading before the references, for example "The authors have no competing interests to declare that are relevant to the content of this article." Add Acknowledgments if any.
5. **Figure numbering.** The draft's figures are numbered 2, 3, 4, 6, 7, 8, 9. Figures 1 (the data-scaling plot) and 5 (the JSON ontology listing) are gone. LNCS renumbers to 1 through 7 and the in-text references follow automatically. Decide whether Figure 1 comes back (it is the one visual that supports the introduction's scaling argument; the file is skyler-first-draft/paper7/figures/fig1_policy_vs_data_amount.pdf and the CSVs are in policy-vs-data-amount/). If it does, its caption needs the EgoScale fix in Section 4.2.
6. **Alt text.** Springer will ask for it for every figure, as an Excel file with the submission. Seven short descriptions.
7. **Affiliation and author names.** Confirm "Innodata" and the exact spelling of all three names. Nothing can change after submission.
8. **Submission package.** main.tex, the figures folder, the PDF, and because we use a thebibliography environment there is no separate bib file; say so if asked. File names should be short (Springer's request), so submit the contents of oct-21/updated/ rather than the long-named PDF.

### 4.2 Content accuracy (should be fixed; a reviewer who knows the papers will catch these)

1. **EgoScale is still overstated.** The revision fixed "needed per task" to "were used for pre-training their VLA" but kept "with upper limits of achieving a mean task acceptable score of 0.71" and, in the next paragraph, "while over 20k hours of video may be needed for a single task." Both are the errors the editor flagged. Suggested replacements, drawn from the 20 October review:

   Introduction, replacing the two sentences from "As such" through "0.71.":

   > Zheng et al. pretrain a vision-language-action model on 20,854 hours of egocentric human video spanning 6,015 tasks and 43,237 objects, then post-train on 100 robot demonstrations per task [1]. Holding the per-task demonstrations fixed and varying only the pretraining corpus, average task completion over five dexterous tasks rises from 0.30 at 1k hours to 0.71 at 20k hours with no sign of saturation [1]. The hours are not spent per task; they buy a shared prior that every downstream task draws on, and the prior is still improving at the largest scale tested.

   Cost paragraph:

   > A corpus of that size is out of reach for most groups. At 3 to 25 USD per hour of egocentric video [CITATION NEEDED], 20,000 hours costs roughly 60,000 to 500,000 USD before curation, and the same recipe at 1,000 hours reaches a completion score of only 0.30 [1]. Lin et al. point to the cheaper lever: generalization scales with the number of distinct environments and objects, not with repeated demonstrations in the same scene [4].

   Also replace "mean acceptable score" with "average task completion score" throughout and say once that it is a partial-credit rubric.

2. **Cost per hour needs a source and a units check.** "3 to 25 USD per hour" appears twice with no citation (draft 7 said 3 to 15, then 8 to 15). Separately, "For every hour processed with our pipeline, we spend 96 USD for GPU cloud instance costs (80 A100-hours at 20 minutes per clip)" counts one Transfer render per clip (240 clips per source hour times 20 minutes). Producing the 72 variants per clip claimed in the same section would cost 72 times that. Either state the cost per rendered variant hour or make the multiplier explicit.
3. **"From 3, 10-minute video examples" versus "Eight recordings".** Results says eight recordings of 4 to 8 minutes; Closing the Gap says three 10-minute examples. The repo's confirmed numbers (review/assumptions.md) are eight recordings, about 80 minutes raw, 116 clips of at most 15 s, 29 minutes retained.
4. **8,352 variations were not rendered.** The repo records 64 renders over 10 clips; 8,352 is capacity (116 clips times 72 admissible variations). The sentence "It should be noted that at the time of publication, the authors have not quantified how much of this synthetic data is useful" helps, but the paragraph still reads as if 35 hours exist. Say "could produce" or give the rendered count.
5. **Fig. 6 caption lists "varying the skin color of the human" as an intended variation.** The prompt asked for the countertop only; the skin-tone shift was leakage. Reword or drop it.
6. **Fig. 7 (pillow) description.** The recovered prompt for that clip targeted "a cobalt blue folded blanket on the left of the bed" and named the pillow as preserved; the text says the only request was that the pillow change to blue. Check against the prompt file.
7. **"(see appendix for source code)"** in Results. There is no appendix. Either add one (Springer puts appendices before the references) or remove the parenthetical.
8. **Head-mounted versus handheld camera.** Shrey's answers say handheld; the text says head-mounted.

### 4.3 Experiment facts Shrey must confirm

1. Does a Predict2 or Transfer run exist in which the cable was prompted to wind counterclockwise and the output showed the "spaghetti" cord? The recovered prompt and the recorded outcome say no (block held fixed, no visible motion), and Fig. 8 shows two near-identical frames. If the run exists, its frames go in Fig. 8 and the caption note comes out. If not, the paragraph should describe the no-motion result.
2. Were the segmentation masks for the pillow and desk clips the ones actually sent to Transfer? The retained masks cover under 3 percent of the frame, which would explain the whole-frame recoloring in Figs. 5 and 7 (new numbering).

### 4.4 Typos and author notes left in the text (kept word for word, fix in the next pass)

- "color alette" (palette), "bilateral bluir input RGB frames" (blur on), "Google Collab Pro+" (Colab), "hours and,diversity", "increase the amount the amount of trainable data", "ego centric" (egocentric), "Zheng et al," (missing period).
- Caption notes: Fig. 6 "(find better example showing spaghetti)" and Fig. 7 "... maybe we can find a better example?" (new numbering).
- "In this paper, we describe" in the abstract and "This paper describes" later in the abstract; the house rule is no "In this paper" in an abstract.
- "Figure N" in text; LNCS convention is "Fig. N". The template sets captions as "Fig." already, so the text is inconsistent with its own captions.

### 4.5 Nice to have

- Restore the data-scaling figure as Figure 1 with the corrected caption ("values read from Fig. 5 of [1]; dashed line is our log-linear fit").
- Restore the one-sentence mention of ControlNet and Gen-1 in Background so references 13 and 14 earn their place.
- A cost table (the "@TODO" from draft 7 was removed in this revision rather than filled).

## 5. File map for this folder

| Path | Purpose |
|---|---|
| Instructions+for+Authors+PDF.pdf | Springer's instructions, the source for Section 1.4 |
| Shrey et al AIPR 2026 - first draft-revisions.pdf | The 21 October Google Docs export, the source text for the outputs |
| shrey-refs | Shrey's reference audit (its numbering is not the manuscript's) |
| AIPR 2026 Paper-updated.{md,docx,pdf} | The deliverables |
| updated/main.tex, updated/build.sh, updated/build/ | LNCS source, build script, build artefacts |
| figures/ | The seven figures used by both the LaTeX and the markdown |
| oct-21-status-and-todo.md | This file |
