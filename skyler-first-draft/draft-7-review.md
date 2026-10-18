---
title: "Review of Draft 7: Analysis and Shore-Up List"
subtitle: "Synthetic Video Generation for Robot Learning Using World Foundation Models (AIPR 2026)"
author: "Prepared for S. Jha, S. Saucedo and F. Tanner, Innodata"
date: "18 October 2026"
abstract: |
  Draft 7 (12 pages, Google Docs export of 18 October 2026) is draft 5 with three of the draft 6 changes adopted: the data-scaling figure drawn from published numbers replaces the EgoScale screenshot, citations are numbered and a 27-entry reference list is attached, and a background paragraph on world foundation models fills the former placeholder. The remaining corrections from the draft 5 review were not carried over. Of the 31 factual items listed there, three are resolved and 27 stand, and the draft adds seven new problems, the most serious being the sentence "We set our weights to the standard default values," which contradicts the recorded control weights that the pipeline was tuned on. Seven of the 27 references are listed but never cited. The paper still lacks the count table, the leakage measurement, the statement that no policy was trained, and the cost arithmetic that supports its own closing claim. This document records every finding with its location, the evidence from the project record, and the replacement text, then gives a prioritised list of work for the four days before the 22 October submission.
---

# Scope and sources

This review compares the draft 7 PDF (`draft-7/AIPR 2026 Paper-draft-7.pdf`) against four things: the confirmed experimental record in `technical-details.md` and `review/assumptions.md`; the six reference papers in `references/`, read from the PDFs; draft 6 (the markdown file in `draft-6/`), which already contains corrected text for most of the issues below; and the project's writing rules in `CLAUDE.md`. Numbers quoted as "confirmed" are those Shrey stated and that are consistent across sources; "measured" means computed from files in the repository; "projection" means arithmetic on other numbers.

The review is organised as findings (Section 3), a prioritised shore-up list (Section 4), questions only the authors can answer (Section 5), and a submission schedule (Section 6). Appendix A gives replacement text ready to paste.

# What changed between drafts 5, 6 and 7

Draft 6 was built on draft 5's structure and corrected its content; draft 7 is draft 5 again, edited by hand, with a subset of the draft 6 material brought in. Table 1 shows which items crossed over.

Table: Draft 6 changes and their status in draft 7.

| Item | Draft 6 | Draft 7 |
|---|---|---|
| Figure 1 | Combined five-panel figure from `policy-vs-data-amount/` | Adopted; caption still says "three papers" |
| Numbered citations and reference list | 27 entries, LNCS style, all cited | Adopted; entries 15 to 20 and 22 are never cited |
| Background paragraph | 14 citations covering Cosmos, ControlNet, Gen-1, VLAs, domain randomization, ROSIE, GenAug | First half adopted (8 citations); second half dropped, which orphans references 15 to 20 |
| Author line | Yes | Added, as "Franklin Tanner"; README and deck say Frank Tanner |
| Abstract rewrite (one paragraph, scale number, measured boundary) | Yes | Not adopted; draft 5 abstract unchanged |
| Multiplier | 72-fold in duration, capacity, 64 rendered | "effectively 72x the amount of trainable data"; capacity and rendered count not stated |
| Method paragraphs (one reasoning step, Cosmos 3 Nano, VLM) | Yes | Not adopted; Cosmos Predict and Cosmos Reason "VLA" remain as two steps |
| Control weights and generation settings | edge 0.5, depth 0.2, vis 0.025, seg 0.175; guidance 4; 35 steps | Replaced by "standard default values" |
| Results setup (64 renders of 10 clips, no policy, no baseline) | Yes | "Eight recordings" adopted; the rest not |
| Leakage measurement | Yes | Not adopted |
| Fig. 6 to 9 captions and text | Rewritten | Not adopted |
| Fig. 5 | JSON listing in the schema | Dark screenshot and placeholder caption remain |
| Closing the Gap (counts, cost arithmetic, Table 1) | Rewritten | Not adopted; TODO for the table remains |
| Conclusion | Rewritten, no closing question | "task-grounded synthetic training variant clips" adopted; closing question remains |
| Keywords, affiliations | Yes | Not adopted |

# Findings

## Statements that contradict the confirmed record

Table 2 lists each sentence in draft 7 that disagrees with the experimental record, the record's value, and the fix. Locations are draft 7 section numbers and page numbers.

Table: Draft 7 statements against the confirmed record.

| # | Location | Draft 7 says | Record | Fix |
|---|---|---|---|---|
| R1 | Sec. 3.3, p. 7 | "We set our weights to the standard default values." | The four control weights were tuned by moving each until a failure appeared: edge 0.5, depth 0.2, vis 0.025, seg 0.175 as passed to the model; guidance scale 4; 35 denoising steps; seeds not fixed. The vis weight near zero is the deck's main practical finding (slide 11). | Replace with the weights sentence in Appendix A.3. NVIDIA's defaults were not used. |
| R2 | Sec. 3, p. 4 | "splitting a 10 min video of egocentric data into 116 individual 15-second clips" | Eight recordings of about 10 minutes, about 80 minutes raw, 116 clips of at most 15 s, about 29 minutes retained. | "splitting the eight recordings, about 80 minutes of footage, into 116 clips of at most 15 seconds" |
| R3 | Sec. 5, p. 10 | "From 3, 10-minute video examples" | Eight recordings. The sentence "One 10-minute video became 4 hours" is only consistent with eight (35 h over 8). | "From eight recordings of about ten minutes each" |
| R4 | Sec. 3, p. 4 | "reasoning stack of Cosmos Predict" then "Cosmos Reason, a Vision-Language-Action (VLA) model" as two consecutive steps | One reasoning step, on the first frame, with the reasoning tower of Cosmos 3 Nano, a vision-language model. Neither Cosmos Predict nor Cosmos Reason ran. | Merge the two paragraphs into the one in Appendix A.2. |
| R5 | Abstract, p. 1 | "Vision Action Language models like NVIDIA Cosmos" | Cosmos models are world foundation models; the reasoner is a VLM. | "NVIDIA Cosmos world foundation models" |
| R6 | Abstract, p. 1 | "OpenAI's mini-4o", "OpenAI's Mini-4o" | GPT-4o mini. | "GPT-4o mini" throughout |
| R7 | Abstract, p. 1 | "Canny Edge detection coupled with Segment Anything 2 (SAM2) to locate the objects" | The ontology's bounding boxes seed SAM2; Canny is a control map, not a locator. | "SAM2, seeded by the ontology's bounding boxes, to mask the surface we wish to repaint" |
| R8 | Sec. 3, p. 4 | "Four guidance maps ... edge, depth, color, and texture" | edge, depth, vis (blurred color) and seg (the mask). No texture control exists. | "edges, depth, overall color and the region to repaint" |
| R9 | Sec. 3.3, p. 7 | "We choose Canny over Sobel or Laplacian" | Canny is the preprocessor packaged with Transfer, on which the edge branch was trained. No comparison was made. | Drop the comparison; cite Canny [26] as the packaged preprocessor. |
| R10 | Sec. 3.3, p. 7 | "monocular depth video provided by DepthAnything V2 [27]" | The depth model behind Transfer's preprocessor was never confirmed; earlier drafts marked it inferred. | Keep [27] only if Shrey confirms; otherwise "the depth estimator packaged with Transfer [VERIFY]". |
| R11 | Sec. 3.3, p. 7 | The mask gives "clearly defined classification to which pixels the model can change ... without affecting the neighboring objects" | The mask enters only as the seg control at weight 0.175. It is a soft signal; Figs. 6 and 7 show change outside it. | Replace with the mask text in Appendix A.3. |
| R12 | Sec. 4, p. 7 | "captured egocentrically with a head-mounted camera" | Shrey's answer: handheld. | "handheld camera" [VERIFY] |
| R13 | Sec. 4, p. 7 | "Each task ranges from 4-8mins in total time" | Not in any source; recordings are about 10 minutes each. | Delete or verify. |
| R14 | Sec. 4, p. 8 | Fig. 6 caption: "Converting white countertop to blue, rag to blue, bucket to blue and varying the skin color of the human." | The prompt asked for the countertop only and named bucket, towels and lighting as preserved. The other changes are leakage. | Caption in Appendix A.4. |
| R15 | Sec. 4, p. 8 | "the background wall and lighting has changed, adding more entropy as desired" | Not desired; the prompt said to preserve them. Measured: target region mean CIE76 Delta E 75, protected region 35, 95 percent of protected pixels above 10. | Paragraph in Appendix A.4. |
| R16 | Sec. 4, p. 8 | Fig. 7: "stuff a throw pillow for a chair ... our only request was that the color of the pillow change to blue" | The recovered prompt targets "a cobalt blue folded blanket on the left of the bed" and names the pillow as preserved; the clip is cloth folding on a bed. | Describe per the recovered prompt [VERIFY]. |
| R17 | Sec. 4, p. 8 | "poor image segmentation results are the cause here, furthering the need to fine-tune Canny edge-gradient parameters" | Segmentation is SAM2, not Canny. The retained pillow mask covers about 2 percent of the frame. | Name the near-empty mask and the missing coverage check. |
| R18 | Sec. 4, p. 9 | Fig. 8: counterclockwise reversal; cord "looked like spaghetti", "gaining linear mass and length" | The recovered Predict2 prompt asks to wind the cable around its block with the block fixed; the confirmed outcome in both runs is no visible motion; Fig. 8 shows two identical frames. | Write what the figure shows, or supply the reversal frames [VERIFY]. |
| R19 | Sec. 4, p. 9 | "an emergent property of VLAs struggling to fully understand the physical world [8]" | Predict2 is a video world model, not a VLA; [8] is its model card and makes no such claim. | "Predict2 was not fine-tuned on manipulation video." Remove [8] from this sentence. |
| R20 | Sec. 5, p. 10 | "For every hour processed ... 1.20 USD in GPU cloud instance costs and 0.12 in token costs" | 1.20 USD is about one A100-hour on Colab Pro+ [VERIFY]. One synthetic hour needs 80 A100-hours (240 clips at 20 min), about 96 USD. The 0.12 USD was the LLM total for all 116 clips. | Paragraph in Appendix A.5. |
| R21 | Sec. 5, p. 10 | "while maintaining the overall physics of the scene" | Untested; geometry and motion are held by the edge and depth controls, and the leakage result argues the other way for appearance. | Delete. |
| R22 | Sec. 3.2, p. 6 | "the 150 word caption" | The prompt-writer instruction allows up to 300 words. | "a caption of a few hundred words" [VERIFY: count the bucket prompt] |
| R23 | Abstract, p. 1 | "scaling a single video into hundreds of permutations" | 72 admissible variations per clip (proposals); 64 renders across 10 clips. | "72 admissible variations per clip; we rendered 64" |
| R24 | Sec. 2, p. 3 | "effectively 72x the amount of trainable data" | 72x in duration is capacity (116 x 72 = 8,352 clips); 6.4x was realized; no policy was trained, so "trainable" is untested. | "multiplies the duration of candidate footage by up to 72 for appearance" |

## Statements that misread the cited references

Table 3 checks each sentence that characterises a reference against the reference's text. Two of the four errors found in draft 5 remain, and one has become more specific without becoming correct.

Table: Draft 7 against the cited references.

| # | Location | Draft 7 says | The reference says | Fix |
|---|---|---|---|---|
| C1 | Sec. 2, p. 1 | "Authors of Egoscale claim over 20,854 hours of egocentric video are needed per task, with upper limits of achieving a mean task acceptable score of 0.71" | 20,854 hours is the pretraining corpus across many tasks and environments. Average task completion rises from 0.30 at 1k hours to 0.71 at 20k hours "with no signs of saturation" (Sec. 3.3). No per-task requirement is stated. | "EgoScale pretrains on 20,854 hours of egocentric human video and finds task completion rising from 0.30 at 1k hours to 0.71 at 20k, with no sign of saturation [1]." |
| C2 | Sec. 2, p. 1 | "the mean acceptable score ... scales logarithmically with the hours" | The log-linear law (R squared 0.9983) is fitted to validation loss, not to the score. Our own fit to the five score points gives R squared 0.96 (Fig. 1a). | "its action-prediction loss falls log-linearly with hours; our fit to the reported scores has R squared 0.96 (Fig. 1a)" |
| C3 | Sec. 2, p. 3 | "FieldGen ... provides only a 2.47x increase over a 2hr training example [6]" | 2.47x is the gain in Collection Time Ratio (66.73 percent against 27.07 percent), an operator-effort metric; throughput rose 2.11x. No "2hr training example" appears. | "FieldGen automates the approach phase of a demonstration and raises the fraction of collection time spent acquiring data 2.47-fold; it saves operator time, not environments [6]." |
| C4 | Sec. 2, p. 3 | "MimicGen multiplies 200 human demonstrations into 50,000" | "over 50K demonstrations ... from less than 200 human demos"; one task on a physical arm. | "fewer than 200 ... into over 50,000" |
| C5 | Sec. 2, p. 2 and Sec. 5, p. 10 | "3 to 15 USD" and "8 - 15 USD" per hour | None of the six references gives a per-hour rate. | One figure, with a source, or "in our own collection experience". |
| C6 | Sec. 4, p. 9 | "[8]" attached to the claim that VLAs struggle with physics | [8] is the Cosmos Predict2 model card. | Remove. |
| C7 | Sec. 3.3, p. 7 | "Canny edge detection provided by OpenCV [26]" | [26] is Canny 1986; OpenCV is a library, not the reference. | "Canny edge detection [26], as packaged with Transfer" |

## Internal contradictions

Table: Pairs of statements in draft 7 that cannot both be true.

| # | A | B | Resolution |
|---|---|---|---|
| I1 | "a 10 min video ... into 116 individual 15-second clips" (Sec. 3) | "From 3, 10-minute video examples ... 116 clips ... 29 minutes of source data" (Sec. 5) and "Eight recordings" (Sec. 4) | Eight recordings everywhere. |
| I2 | "3 to 15 USD" (Sec. 2) | "8 - 15 USD" (Sec. 5) | One figure. |
| I3 | "hundreds of permutations" (Abstract) | "72x", "8,352 synthetic video variations" (Secs. 2, 5) | 72 per clip, 8,352 capacity, 64 rendered. |
| I4 | "We set our weights to the standard default values" (Sec. 3.3) | "each control modality comes with tunable parameters to decide how strong the variant is rendered" (Sec. 3.3) and the deck's tuning account | State the tuned values. |
| I5 | Rule 2: the preservation clause "protects non-target objects" (Sec. 3.2) | Fig. 6: bucket, rag, wall and lighting changed under a prompt containing the clause | "reduces but does not prevent" |
| I6 | Mask defines "which pixels the model can change" (Sec. 3.3) | Figs. 6 and 7: neighbouring objects change | Soft control. |
| I7 | Fig. 6 caption lists the skin-tone change with the intended recolor | Rule 2 and the bucket prompt asked for the countertop only | Caption in Appendix A.4. |
| I8 | Fig. 8 text: spaghetti cord | Fig. 8 image: two identical frames | Match text to figure, or change the figure. |
| I9 | "Cosmos Predict" reasoning stack, then "Cosmos Reason" (Sec. 3) | Fig. 2 and the Abstract: Cosmos 3 Nano | One step, Cosmos 3 Nano. |
| I10 | Fig. 1 caption: "in three papers" | Five panels from five papers | "five papers" |

## Citations and bibliography

The reference list is correct in content and format, and every URL resolves (checked 18 October). The problems are in how the list is used.

- References 15 (RT-2), 16 (OpenVLA), 17 (Open X-Embodiment), 18 (domain randomization), 19 (ROSIE), 20 (GenAug) and 22 (Cosmos3-Nano model card) are listed but never cited. In LNCS a numbered list must match the citations in the text. Either restore the second half of the background paragraph from draft 6, which cites all seven, or delete the seven entries and renumber. Restoring is better: domain randomization, ROSIE and GenAug are the three works a reviewer will expect to see positioned against this method, and the Conclusion's closing question about random augmentation has no citation without [18].
- "[1]" in the Fig. 1 caption and "[21]" in Sec. 3 follow a full stop. LNCS places the citation before the punctuation.
- "[26]" credits OpenCV to Canny (C7). "[8]" supports a claim the model card does not make (C6).
- "Egoscale" should be "EgoScale" (Sec. 2). "pi0" is set once as a superscript zero in the Fig. 1 caption and as "pi0" elsewhere; LaTeX will fix this if the subscript is written as math.
- The author line reads "Franklin Tanner"; the deck, the README and the clearance note say Frank Tanner. Confirm the form the author wants in print.
- No affiliations, emails, ORCIDs or keywords. LNCS requires affiliations and keywords.

## Figures and captions

- Fig. 1 is the combined five-panel figure and reads well at page width. The caption should say that the dashed line in (a) is our fit, give its R squared (0.96), say that the values in (b) and (c) were read off the source figures, and count five papers rather than three. Draft 6's caption has all of this.
- Fig. 2 keeps the caption "The Pipeline". A caption should state what to notice: every input to the renderer is produced by an earlier stage.
- Fig. 4 is now a clean rebuild without the cropped page header. Its caption should note the two errors in the ontology (the task name is wrong for a wiping clip; "bucket cannot be opened" is implausible), since the filter stage is justified by them.
- Fig. 5 is still the dark screenshot with the placeholder caption "May be overkill and not needed, real JSON pref". Draft 6 has a typeset JSON listing in the exact schema of the Cosmos 3 Nano instruction, with the complete record in `draft-6/figures/fig5_ontology_bucket.json`; the task block and robustness gaps are the model's output, the rest is a reconstruction marked as such. Use it or drop the figure.
- Fig. 6 and Fig. 7 keep the "Old / New" slide chrome. Use the raw frames as subfigures (a) and (b).
- Fig. 8 shows two identical frames under the caption "Directional Reversal Experiment". If the text is corrected (R18), the caption becomes "conditioning frame beside a forecast frame; nothing moved", which is the finding.
- Fig. 9's caption is still "Some examples of variants ... maybe we can find a better example?". The three frames are the blue-desk render (colour spread onto shelf objects and cable), the navy-rug render (smeared surfaces, warped arm, no rug), and the Predict2 paper-rotation forecast (nothing moves). They are the failure cases and need a caption that says what was asked and what happened.

## Missing content

The following exist in draft 6 and are absent from draft 7.

1. A setup paragraph stating what was run: reasoning on all 116 clips, 64 Transfer renders over 10 source clips, 2 Predict2 renders, evaluation by inspection plus one measurement, no policy trained, no baseline run.
2. Table 1, the count and cost chain from 8 recordings to 116 clips to 8,352 admissible variants (capacity) to 64 rendered, with time per stage. This is the table the Sec. 5 TODO asks for.
3. The control weights, guidance scale and denoising steps (R1).
4. How the mask is built: SAM2 surface mask minus the union of the object masks, per frame on SAM2's propagated masks.
5. The leakage measurement: masked CIE76 Delta E on the counter-wiping clip (target 75.5, protected 34.8, chroma-only 68.2 against 24.2, 94.5 percent of protected pixels above 10) and the one-clip caveat. This is the paper's only quantitative result.
6. The Predict2 result stated plainly: two runs, 35 steps, 93 frames at 16 fps, no motion in either, not fine-tuned.
7. The second half of the background paragraph (VLAs, domain randomization, ROSIE, GenAug), which also resolves the uncited references.
8. A limitations statement: one person, one home; weights tuned on one clip and checked on three; leakage measured on one clip; ontology error rate unmeasured; seeds not fixed; one closed LLM in the loop; 4 fps undersamples contact.
9. Keywords and affiliations.
10. An abstract with the scale number and the measured boundary in place of "powerful and economical".

## Register and mechanics

Measured against `CLAUDE.md` Section 3. Strike-list words present: leverages, leveraging, leverage (four uses), robust and robustness (three), powerful, Additionally (two), Lastly (two), It should be noted, critical, exceptional, Surprisingly, cohesive and practical, meaningful solution. Rhetorical questions in body text: three, plus "Why?" inside rule 3. The abstract is two paragraphs and closes on a phrase borrowed from the MimicGen abstract ("a powerful and economical approach"). The title is in capitals. Note-form fragments remain ("4-8mins", "etc...", "@TODO"). Spelling: PhysicalAI, permutions (twice), Onotology is gone but "objects,states" and "clutter _" remain, lightning, contests, dextrous, sows, "Chat GPT 4o mini", "we're", "it's". "Humanoid" appears eight times although nothing in the data or method is humanoid-specific.

# Shore-up list, prioritised

P0 items are errors of fact a reviewer can check against the record or the references; the paper should not be submitted with any of them. P1 items are missing evidence for the paper's own claims. P2 items are register and packaging.

Table: Shore-up list.

| Priority | Item | Where | Source of the fix |
|---|---|---|---|
| P0 | Restore the tuned control weights and generation settings (R1, I4) | Sec. 3.3 | Appendix A.3; draft 6 Sec. 2.3 |
| P0 | Eight recordings, about 80 min raw, 116 clips, 29 min retained, everywhere (R2, R3, I1) | Secs. 3, 5 | Appendix A.2, A.5 |
| P0 | One reasoning step on Cosmos 3 Nano, a VLM (R4, R5, I9) | Abstract, Sec. 3 | Appendix A.2 |
| P0 | EgoScale and FieldGen sentences (C1, C2, C3) | Sec. 2 | Table 3 |
| P0 | Cost paragraph with the right arithmetic (R20, R21) | Sec. 5 | Appendix A.5 |
| P0 | Fig. 6 caption and paragraph: leakage named as leakage, with the measurement (R14, R15, I5, I7) | Sec. 4 | Appendix A.4 |
| P0 | Fig. 8 text matched to the figure and the confirmed outcome; remove [8] (R18, R19, C6, I8) | Sec. 4 | Draft 6 Sec. 3 |
| P0 | Mask described as a soft control (R11, I6) | Sec. 3.3 | Appendix A.3 |
| P0 | Cite or delete references 15 to 20 and 22 | Background, References | Draft 6 background paragraph |
| P0 | One collection-cost figure with a source (C5, I2) | Secs. 2, 5 | Ask the authors |
| P1 | Setup paragraph with what was run, no policy, no baseline | Sec. 4 | Draft 6 Sec. 3, first paragraph |
| P1 | Table 1, counts and cost per stage | Sec. 5 | Draft 6 Table 1 |
| P1 | Leakage sentences and the one-clip caveat | Sec. 4 | Draft 6 Sec. 3 |
| P1 | Fig. 7 cause: near-empty mask, coverage check (R16, R17) | Sec. 4 | Draft 6 Sec. 3 |
| P1 | Fig. 9 caption with prompt and outcome per panel | Sec. 4 | Draft 6 Fig. 9 |
| P1 | Fig. 5: JSON listing or drop | Sec. 3.1 | Draft 6 Fig. 5 |
| P1 | Mask construction sentence (surface minus objects) | Sec. 3 | Draft 6 Sec. 2 |
| P1 | Abstract: one paragraph, scale number, measured boundary (R23) | Abstract | Appendix A.1 |
| P1 | Multiplier stated as capacity, 64 rendered (R24, I3) | Secs. 2, 5, Conclusion | Draft 6 |
| P1 | Limitations statement | Sec. 5 or Conclusion | Draft 6 Sec. 4; draft 5 shore-up list, item B11 |
| P1 | Camera and recording length verified (R12, R13) | Sec. 4 | Ask the authors |
| P2 | Strike-list words, rhetorical questions, title case, fragments, spelling | Throughout | Section 3.7 |
| P2 | Citation placement before punctuation; OpenCV attribution (C7) | Throughout | |
| P2 | Fig. 1, 2, 4 captions | Secs. 2, 3 | Draft 6 captions |
| P2 | Keywords, affiliations, author name form | Front matter | Ask the authors |
| P2 | LNCS LaTeX typesetting (`llncs`, `splncs04`), figures as vector where available | Packaging | `paper3v2/`; the PDF figures in `policy-vs-data-amount/figures/` |

# Questions for the authors

1. Were the control weights the tuned values (edge 0.5, depth 0.2, vis 0.025, seg 0.175) or NVIDIA's defaults? The deck, Shrey's answers and the chat all say tuned; draft 7 says default.
2. Eight recordings or three? Handheld or head-mounted? Where does "4 to 8 minutes per task" come from?
3. Does a counterclockwise cable-reversal run exist, with frames showing the "spaghetti" cord? The recovered prompt and the stills show no motion.
4. Fig. 7: was the prompt "pillow to blue" or the recovered cobalt-blanket prompt?
5. Are the exported shelf and pillow masks (0.1 and 2.5 percent coverage) the masks Transfer received?
6. Which depth model does the Transfer preprocessor run?
7. What is the source of the per-hour collection rate, and is it 3 to 15 or 8 to 15 USD?
8. Is 1.20 USD the Colab Pro+ price per A100-hour?
9. Typical prompt length: 150 or up to 300 words?
10. Will the notebooks be released? If not, cut "see appendix for source code".
11. Author name: Frank or Franklin Tanner? Affiliations and ORCIDs for all three.

# Submission checklist and schedule

The final paper is due 22 October 2026 via Springer Meteor: LNCS source, PDF, figure source files and a signed Licence to Publish. Four days remain.

1. Day 1 (18 October). Send Section 5 to the authors. Apply every P0 item; each has replacement text in Appendix A or draft 6. Decide where the paper is typeset; `paper3v2/` holds an LNCS LaTeX copy with the tables, equation and bibliography already in place, and `paper3v2/build.sh` builds it.
2. Day 2. Apply the P1 items: setup paragraph, Table 1, leakage sentences, Fig. 5, Fig. 7 and Fig. 9 text, mask construction, abstract, limitations.
3. Day 3. P2 pass against `CLAUDE.md` Section 3; captions; keywords and affiliations; replace remaining `[VERIFY]` markers with the authors' answers or delete the dependent sentence.
4. Day 4. Build the PDF, check page count and overfull boxes, read once end to end, sign the licence, submit.

# Appendix A: Replacement text

Each block is taken from draft 6 and can be pasted over the corresponding draft 7 passage. Citation numbers follow the draft 7 reference list.

## A.1 Abstract

Robot manipulation policies are bottlenecked by real-world data. Acceptable completion scores on even simple household tasks have been reached only with tens of thousands of hours of egocentric video, and the policies need that footage to vary in objects, surfaces and lighting rather than repeat one room. We describe a pipeline that uses NVIDIA Cosmos world foundation models and the GPT-4o mini language model to generate appearance variations of real egocentric clips while keeping the recorded actions. Cosmos 3 Nano reads each clip and writes an ontology: the task, each object's role in it, and the variations that are plausible for that role. GPT-4o mini filters the candidates and writes the generation prompt. Segment Anything 2 (SAM2) turns the ontology's bounding boxes into tracked masks of the surface to repaint, and Cosmos Transfer 2.5 renders the variant under edge, depth, color and segmentation guidance. From 116 clips the reasoning stage admits 72 variations per clip, capacity for about 8,000 synthetic clips at 20 GPU-minutes each; we rendered 64. Single-surface recolors keep hand pose, object shape and motion, but the edit leaks outside its mask: on the counter-wiping clip the protected region shifts by a mean CIE76 Delta E of 35 against 75 for the target, cluttered scenes recolor wholesale, and action-level changes with Cosmos Predict2 produce no motion. We report the process, the guidance weights and prompt rules that made it work, and the limits a policy trained on this data would inherit.

## A.2 Method, first three paragraphs

Fig. 2 shows the pipeline we use to permute the ontological objects within an egocentric video.

First, the source recordings (V) are prepared with NVIDIA's Cosmos Curate. Curate applies TransNetV2 shot-boundary detection [21], splitting the eight recordings, about 80 minutes of egocentric footage, into 116 clips of at most 15 seconds, downsampled to 4 fps at 854x480. TransNetV2 is a small convolutional network trained to detect scene transitions; it is fast and accurate on standard shot-detection benchmarks [21].

The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano [12, 22], a vision-language model that returns a structured description of the task, the task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations that are plausible for the task. We call this structured JSON record the ontology. We feed the ontology to GPT-4o mini [23], a language model that filters the proposed variations and writes a text prompt for Cosmos Transfer.

Four guidance videos derived from the source clip preserve edges, depth, overall color and the region to repaint. SAM2 [24] converts the ontology's bounding boxes into masks tracked across the clip; subtracting the masks of the objects resting on the target surface from the mask of the surface itself leaves only the region to change. Finally, Cosmos Transfer 2.5 [10, 25] renders a synthetic variant (V') of the video with the same task, actions and inventory of objects, but with permuted item attributes that add appearance diversity.

## A.3 Guiding the rendering, items 1 to 4 and the weights

1. Edges: a Canny edge video [26], computed by the preprocessor packaged with Transfer, carries the outline of every object in every frame. If the edges are not clearly defined, object geometry warps during rendering; if the edge weight is too high, nothing changes.
2. Depth: a monocular depth video from the estimator packaged with Transfer [27] [VERIFY: which model] carries the layout, what is in front of what. As we permute object attributes, this control keeps the ordering of objects consistent in the variant.
3. Color for lighting: a heavily blurred copy of the source (the vis control) keeps the overall palette and the direction of the light. It also opposes any recolor, because it conditions on the source colors, so its weight is held near zero.
4. Segmentation mask: the subtraction mask built from SAM2 marks, pixel by pixel, the surface the prompt applies to. It is a control signal rather than a hard constraint: the model follows it to the degree set by its weight, and nothing in the pipeline forbids change outside it. When objects overlap or occlude one another, subtracting their masks from the surface mask keeps them out of the target region, but as Sec. 4 shows, it does not keep the render from changing them.

We set the weights by moving each until a failure appeared and backing off, on the counter-wiping clip, then checked them on three further clips: edge 0.5, depth 0.2, vis 0.025 and seg 0.175 as passed to the model, with guidance scale 4 and 35 denoising steps. At guidance 2 and 3 the model often ignored the variation; above 5 it followed the prompt and lost the room. Seeds were not fixed.

## A.4 Fig. 6 caption and paragraph

Fig. 6. Counter-wiping clip, matched frames. Left: the source, a white bucket held over a white counter with a grey rag. Right: the variant rendered for the blue-countertop prompt. The countertop recolor is the intended edit, and hand pose, bucket geometry and motion are preserved. The grey-blue bucket, the blue rag, the beige wall, the lighter hand and the new ceiling light were not asked for; the prompt named each of them as preserved.

Fig. 6 shows that the variant recolors the countertop while maintaining the hand pose and the bucket and table geometry. The cleaning motion of the source is maintained in the variant, frame by frame. The render also changed what the prompt said to preserve: the rag became blue cloth, the bucket grey-blue, the wall beige, and the lighting changed. Measured in CIELAB over the 60 frames, the target region moved by a mean CIE76 Delta E of 75 and the protected region by 35, and 95 percent of protected pixels changed by more than 10, a difference any viewer sees. The segmentation control and the prompt's preservation clause were the two mechanisms for containment, both of them soft, and together they held back about half of the edit.

## A.5 Closing the gap

From eight recordings of about ten minutes each, our workflow produced 116 clips, and the reasoning stage admitted 72 variations per clip, so the set is capacity for 8,352 synthetic variations, about 35 hours of video from 29 minutes of source. The number of variants a clip admits depends on how many ontological objects are available to change and on which of their attributes the NVIDIA world model suite can change while holding the action fixed, which today means color, material and surface finish rather than shape, layout or motion. One 10-minute video became about 4 hours of candidate video without a new scene or room. We rendered 64 of the 8,352, and those 64 are the only synthetic video that exists (Table 1).

Table: From eight recordings to synthetic clips, with the time of each stage on one A100 80 GB. Rows marked capacity are projections from the per-clip figures, not output.

| Stage | Count | Video duration | Time per unit | Total GPU time | Status |
|---|---|---|---|---|---|
| Recordings | 8 | about 80 min | | | recorded |
| Clips after TransNetV2, trim, downsample | 116 | about 29 min | seconds | | measured |
| Reasoning (Cosmos 3 Nano) | 116 clips | | 130 s | about 4.2 h | run |
| Filter and prompt (GPT-4o mini) | 116 clips | | seconds | 0.12 USD total | run |
| Admissible variations (72 per clip) | 8,352 | about 35 h | | | capacity |
| Transfer renders | 64 (10 source clips) | 16 min | 20 min | about 21 h | rendered |
| Predict2 renders | 2 | 12 s | 3.5 min | 7 min | rendered |
| Transfer renders of every admissible variation | 8,352 | about 35 h | 20 min | about 2,800 h | capacity |

The cost sits in the render. Reasoning takes two minutes per clip and the language model costs 0.12 USD across the whole set, but a Transfer render takes 20 minutes per 15-second clip, so every hour of synthetic video costs 80 A100-hours, about 96 USD at the Colab Pro+ rate of about 1.20 USD per A100-hour [VERIFY: price], against 8 to 15 USD for an hour of collected egocentric video [VERIFY: rate]. At today's speed the pipeline is not a cheaper source of hours. What it is a cheaper source of is diversity. Lin et al. [4] found that generalization scales with the number of distinct environments and objects and that further demonstrations in a room the policy has already seen stop helping, and the pipeline produces 72 appearance variants of every action without the recruitment, travel and setup a new room costs a collector. Whether a rendered variant counts as a new environment in their sense is untested, since layout, geometry and motion are unchanged and no policy was trained. The distilled Transfer model, which NVIDIA reports at about one minute per clip on an H100 [25], would bring the rate per synthetic hour into the collector's range; we have not run it. For practitioners and academics with a limited budget, the appearance half of this loop runs today on one GPU with public checkpoints.
