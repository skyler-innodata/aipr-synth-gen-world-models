# Draft 5: what to shore up and add

Written 2026-10-18. Final paper is due 2026-10-22 via Springer Meteor (LNCS source, PDF, figure sources, signed Licence to Publish). Four days. Items are grouped by what blocks submission, then by what is missing, then by what to verify with Shrey, then by prose and packaging. Replacement text is given where it is cheap; longer replacements point at the draft 4 file that already has them.

Sources for every number: `technical-details.md`, `review/assumptions.md`, `review/leakage/README.md`, `draft-4-skyler/methodology.md`, `results-revised.md`, `closing-the-gap.md`.

---

## A. Factual errors to fix before anything else

| # | Where | What draft 5 says | Fix |
|---|---|---|---|
| A1 | Results, first sentence | "Thousands of clips of first person videos of household chores we used" | "Eight recordings of household chores, cut into 116 clips, were the source material." Thousands is the projection, not the input |
| A2 | Sec. 5 | "From 3, 10-minute video examples" | 8 recordings (confirmed). The "One 10-minute video became 4 hours" sentence is consistent with 8, not 3 (35 h / 8 = 4.4 h) |
| A3 | Method | "splitting a 10 min video ... into 116 individual 15-second clips" | "splitting the eight recordings into 116 clips of at most 15 s"; 116 x 15 s = 29 min cannot come from one 10-minute video |
| A4 | Sec. 5 | "For every hour processed with our pipeline, we spend 1.20 USD in GPU cloud instance costs and 0.12 in token costs" | 1.20 USD is about one A100-hour on Colab Pro+ [VERIFY price]. One synthetic hour is 240 clips x 20 min = 80 A100-hours, about 96 USD. The 0.12 USD was the LLM total for all 116 clips. Replacement paragraph in `closing-the-gap.md`, "Rewritten section", paragraph 2 |
| A5 | Abstract, Sec. 5 | "powerful and economical", "quickly scale a sparse dataset into one with sufficient hours" | At current settings a synthetic hour costs 6 to 30 times a collector's hour (`results.md` Part 6). The claim that holds is diversity per Lin et al.: 72 appearance variants of every action with no new room. Say that |
| A6 | Intro | "effectively x10 the amount of trainable data" | 72x in duration is capacity (116 x 72 = 8,352 clips, about 35 h from 29 min); 6.4x was realized (64 renders of 10 clips). "Trainable" is untested since no policy was trained |
| A7 | Abstract | "scaling a single video into hundreds of permutations" | "72 admissible variations per 15-second clip" (proposals), "we rendered 64" |
| A8 | Conclusion | "turn a real, limited first-person dataset into thousands of synthetic training clips" | "into task-grounded appearance variants at 72 per clip; we rendered 64" or keep "thousands" only with "capacity for" in front |
| A9 | Intro | EgoScale "20,000+ hours ... needed per task, with upper limits of ... 0.71" | EgoScale pretrains on 20,854 hours across tasks; score rises from 0.30 at 1k hours to 0.71 at 20k "with no signs of saturation". Write: "EgoScale pretrains on 20,854 hours of egocentric human video and finds task completion rising from 0.30 to 0.71 as hours grow from 1k to 20k, with no sign of saturation [egoscale]" |
| A10 | Intro | FieldGen "provides only a 2.47x increase over a 2hr training example" | 2.47x is the gain in Collection Time Ratio (66.73 percent against 27.07 percent), an operator-effort metric; throughput rose 2.11x. Write: "FieldGen automates the approach phase of a demonstration and raises the fraction of collection time spent acquiring data 2.47-fold; it saves operator time, not environments [fieldgen]" |
| A11 | Intro vs Sec. 5 | "3 to 15 USD" and "8 - 15 USD" per hour | One figure, with a source. If it is Innodata's own rate, say "in our own collection experience" and cite nothing |
| A12 | Method paras 3 and 4 | "reasoning stack of Cosmos Predict" and then "Cosmos Reason, a Vision-Language-Action (VLA) model" as two steps | One step: the reasoning tower of Cosmos 3 Nano, a vision-language model, reads the first frame. Delete the Cosmos Predict paragraph; rename Cosmos Reason to Cosmos 3 Nano; VLA to VLM. Replacement paragraph: `methodology.md` Section 15, "Revised paragraph" |
| A13 | Abstract | "Vision Action Language models like NVIDIA Cosmos" | Cosmos models are world foundation models; the reasoner is a VLM. Neither is a VLA |
| A14 | Abstract | "OpenAI's mini-4o", "Mini-4o" | GPT-4o mini, consistently |
| A15 | Abstract | "Canny Edge detection coupled with SAM2 to locate the objects we wish to permute" | Canny is a control map, not a locator. The ontology's bounding boxes seed SAM2, which returns tracked masks |
| A16 | Method para 5 | "Four guidance maps ... edge, depth, color, and texture" | edge, depth, vis (blurred color) and seg (the mask). There is no texture control |
| A17 | Sec. 3.3 item 1 | "We choose Canny over Sobel or Laplacian due to the models robustness" | Canny is the preprocessor packaged with Transfer; the edge branch was trained on Canny maps. Not our choice. Drop the comparison or phrase it as background (`methodology.md` Section 19) |
| A18 | Sec. 3.3 item 2 | "provided by DepthAnything V2" | The depth model behind Transfer's preprocessor was never confirmed; drafts cite Depth Anything as the packaged default, inferred. The only URL in the reference list points at Video Depth Anything, a different model. [VERIFY with Shrey] |
| A19 | Sec. 3.3 item 4 | The mask gives "clearly defined classification to which pixels the model can change ... without affecting the neighboring objects" | The mask enters only as the seg control at weight 0.175. It is a soft signal; nothing forbids change outside it. Fig. 6 and Fig. 7 show exactly that. Replacement: `methodology.md` Section 19 prose, "The segmentation control is the subtraction mask ..." |
| A20 | Fig. 6 caption | "Converting white countertop to blue, rag to blue, bucket to blue and varying the skin color of the human" | The prompt asked for the countertop only and named bucket, towels and lighting as preserved. Caption: "Counter-wiping clip, matched frames. The countertop recolor is the intended edit; hand pose, bucket geometry and motion are preserved. The grey-blue bucket, the blue rag, the beige wall, the lighter hand and the new ceiling light were not asked for." (`results-revised.md` Fig. 1 caption) |
| A21 | Results, Fig. 6 paragraph | "background wall and lighting has changed, adding more entropy as desired" | It was not desired; the prompt said to preserve them. This is the leakage result. Replace with the two sentences from `results-revised.md` 4.1, and put the leakage table after it |
| A22 | Fig. 7 paragraph | "stuff a throw pillow for a chair ... our only request was that the color of the pillow change to blue" | The recovered prompt targets "a cobalt blue folded blanket on the left of the bed" and names the pillow as preserved; the clip is cloth folding on a bed. [VERIFY which prompt produced Fig. 7] |
| A23 | Fig. 7 paragraph | "poor image segmentation results are the cause here, furthering the need to fine-tune Canny edge-gradient parameters" | Segmentation is SAM2, not Canny. The measured evidence is that the retained pillow mask covers about 2 percent of the frame (`review/leakage/README.md`); if that mask was fed to Transfer the seg control carried nothing. Say that, and name the fix: a mask-coverage check before rendering |
| A24 | Fig. 8 paragraph | Clockwise to counterclockwise "directional reversal"; cord "looked like spaghetti", "gaining linear mass and length" | The recovered Predict2 prompt asks to wind the cable around its block with the block held fixed; the confirmed outcome in both Predict2 runs is no visible motion, and Fig. 8's two frames are identical. Either show the spaghetti frames and the reversal prompt, or write what Fig. 8 shows: "In both forecasts the scene is reproduced and the cable does not move." [VERIFY with Shrey] |
| A25 | Fig. 8 paragraph | "an emergent property of VLAs struggling to fully understand the physical world" | Predict2 is a video world model, not a VLA. "Predict2 was not fine-tuned on manipulation video" is the honest cause |
| A26 | Results | "captured egocentrically with a head-mounted camera" | Shrey's answer: handheld, one person holding the camera. [VERIFY] |
| A27 | Results | "Each task ranges from 4-8mins in total time" | Not in any source; the confirmed figure is 8 recordings of about 10 min each. [VERIFY or delete] |
| A28 | Sec. 3.1 | "70 Plausible variants per 15 second clip, filtered from 100+ raw proposals" | 72 (confirmed); "100+" was never measured, mark [VERIFY] or write "the raw count exceeds the admitted count; the exact number was not recorded" |
| A29 | Sec. 3.2 | "150 word caption" | The prompt-writer limit is under 300 words. Count the bucket prompt and state its length |
| A30 | Sec. 5 | "while maintaining the overall physics of the scene" | Untested. Geometry and motion are held by the edge and depth controls; nothing was measured about physics |
| A31 | Sec. 5 | "One 10-minute video became 4 hours without a new scene or room generated" | Keep, with "about 4 hours of candidate video" and "capacity"; it is 72 x (10 min x 0.36 retained) |

## B. Content that is missing and should be added

Each item exists in draft 4 and can be moved with light editing.

1. **A setup paragraph that states what was run.** 8 recordings, 116 clips, reasoning on all 116, 64 Transfer renders over 10 clips, 2 Predict2 renders, no policy trained, no baseline run, evaluation by inspection plus one measurement. Source: `results-revised.md` "Setup", two paragraphs. This is also where the "see appendix for source code" sentence should point at a real appendix or be cut.
2. **Table 1, the count chain.** 8 recordings (about 80 min) to 116 clips (29 min) to 8,352 admissible variants (35 h, capacity) to 64 rendered (16 min). Source: `results-revised.md` Table 1. This is the table the Sec. 5 TODO asks for ("Add a table that sows cost in time, money"), with a cost column added: reasoning 2.2 min per clip, Transfer 20 min, Predict2 3.5 min, LLM 0.12 USD total.
3. **The control weights and generation settings.** edge 0.5, depth 0.2, vis 0.025, seg 0.175 (sum 0.9), with the failure that bounds each; guidance scale 4 (2 and 3 under-apply, above 5 loses the room); 35 denoising steps; seeds not fixed; 60 frames at 854 x 480 and 4 fps. Source: `methodology.md` Section 19 Table X and Section 6. Without these the Method is not reproducible and Sec. 3.3's "tunable parameters" has no values.
4. **The subtraction mask.** One sentence or Eq. 1: the mask is SAM2's surface mask minus the union of the object masks, per frame on SAM2's propagated masks. Source: `methodology.md` Section 5b. The four-panel strip from slide 11 (`paper3/figures/s11_mask_strip.png`) is the figure. Draft 5 never says how the mask is built.
5. **The leakage measurement.** Two sentences defining masked CIE76 ΔE, the table (target 75.5, protected 34.8, chroma-only 68.2 against 24.2, 94.5 percent of protected pixels above 10), and the one-clip caveat. Source: `results-revised.md` 4.2 and Table 2; files in `review/leakage/bucket/`. This is the paper's only quantitative result and the evidence for claim 2 of the thesis.
6. **The Predict2 result, stated plainly.** Two runs, 35 steps, 93 frames at 16 fps, no motion in either, not fine-tuned. Source: `results-revised.md` 4.3. Draft 5 has only the unverified spaghetti account.
7. **A Related Work paragraph.** Draft 5 has the placeholder "Background? - Description of World Language Models?". Draft 3's `related.tex` is one paragraph with 17 citations covering Cosmos (Predict, Transfer, Reason, Cosmos 3), ControlNet and Gen-1, VLAs and Open X-Embodiment, Ego4D, domain randomization, ROSIE and GenAug, SAM2, TransNetV2, Canny and Depth Anything. Add one sentence each for MimicGen and FieldGen (simulation trajectories and operator time, against appearance in real video) and one for the scaling papers.
8. **A reference list.** Draft 5 has two URLs. `paper3/refs.bib` has 30 verified entries; `introduction.md` lists the five new ones to add (egoscale, lin2025scaling, mimicgen, fieldgen, lingbotvla) with the arXiv numbers from `references/`. Check DBLP for the ICLR 2025 and CoRL 2023 versions of Lin et al. and MimicGen. Every "[cite ...]", "[NEW ...]" and "[site reference]" in draft 5 then resolves.
9. **Figure 9 captions.** The three frames are the blue-desk render (color spread onto shelf objects and cable), the navy-rug render (smeared surfaces, warped arm, no rug) and the Predict2 paper-rotation forecast (nothing moves). Each needs what was asked and what happened. Source: `results-revised.md` Fig. 3 caption. They are the failure cases, not "examples of variants", and they belong next to Fig. 7.
10. **Closing the gap, rewritten.** `closing-the-gap.md` "Rewritten section" (about 560 words) replaces draft 5's Sec. 5 in full: the count chain, the cost in GPU-hours with the diversity argument from Lin et al., and the three things between the renders and a training set (containment, a baseline, a trained policy), plus action generation.
11. **Limitations stated in one place.** One person, one home; weights tuned on one clip and checked on three; leakage measured on one clip; ontology error rate unmeasured; seeds not fixed; one closed LLM in the loop; 4 fps undersamples contact; no policy, no baseline. Draft 5 scatters some of these and omits most.
12. **Keywords, author block, affiliations, ORCIDs.** Required by LNCS. Keywords from draft 4: Synthetic data; World foundation models; NVIDIA Cosmos; Egocentric video; Robot learning.
13. **The abstract's scale number and boundary.** Replace the last two sentences with draft 4 abstract D's: "From 116 clips the reasoning stage admits 72 variations per clip, enough for about 8,000 synthetic clips at 20 GPU-minutes each; we rendered 64. ... the edit leaks outside its mask (protected pixels shift by a mean CIE76 ΔE of 35 against 75 for the target), cluttered scenes recolor wholesale, and action-level changes with Cosmos Predict2 produce no motion."

## C. Questions for Shrey (answers change the text)

1. Three recordings or eight? Draft 5 says 3; the PDF answer says 8 of about 10 min each.
2. Handheld or head-mounted camera?
3. Where does "each task ranges from 4-8 mins" come from?
4. The Predict2 cable experiment: was a counterclockwise reversal prompt run? Do frames exist showing the "spaghetti" cord? The recovered prompt and the stills show no motion.
5. Fig. 7: was the prompt "pillow to blue" or the recovered "cobalt blue folded blanket on the left of the bed"? Is the clip pillow stuffing or cloth folding?
6. Are the exported shelf and pillow masks (0.1 percent and 2.5 percent coverage) the masks Transfer received? (Assumption A7; decides whether Fig. 7 is leakage or rendering without a mask.)
7. Which depth model does the Transfer preprocessor run? Depth Anything V2, Video Depth Anything, or something else?
8. The 1.20 USD figure: is it per A100-hour on Colab Pro+? What is the compute-unit rate it came from?
9. Typical prompt length: 150 words or under 300? Count the bucket prompt.
10. Raw proposal count per clip before the filter (the "100+").
11. Which GPT-4o mini snapshot ran?
12. Will the Colab notebooks be released? If yes, the "see appendix for source code" sentence becomes a URL; if no, cut it.
13. The source of the per-hour collection rate (3 to 15 or 8 to 15 USD).

## D. Prose and register pass

Run after the content is in place, against CLAUDE.md Section 3.

- Strike-list words to remove: leverages / leveraging / leverage (4 uses), robust / robustness (3), powerful, Additionally (2), Lastly (2), It should be noted, critical, exceptional, Surprisingly, cohesive and practical, meaningful solution.
- Rhetorical questions to turn into statements: Sec. 3.1 ("how does this affect the outcome..."), Results opening ("Can we generate..."), the Conclusion's last sentence, and "Why?" in rule 3.
- Heading restatements to cut: "In this step, we use ...", "This paper describes our process and findings".
- Note-form to expand: "x10", "4-8mins", "etc…", "Result -> 70", the bullet fragments at the top of page 5 ("Proposes only physically grounded variations per object").
- The abstract's closing sentence is MimicGen's ("a powerful and economical approach towards scaling up robot learning"); a reviewer who knows that paper will see it. Draft 4 abstract D has the replacement.
- "Humanoid" appears nine times. Nothing in the data or method is humanoid-specific; "robot manipulation policies" covers it and avoids a reviewer asking which humanoid.
- "Ontology" is defined in the Intro as "the diversity of objects within the space" and in the Method as the structured JSON record. Use the second, once, at first use.
- "Visual entropy" (Method) is undefined; "appearance diversity".
- Tense: past for what was done ("we rendered"), present for what the paper shows.
- Spelling: PhysicalAI (Physical AI), permutions, acceptables, Onotology, objects,states, "clutter _", lightning, contests, dextrous, sows, Egoscale, "Chat GPT 4o mini", "a A100", "we're", "it's".
- Title: LNCS will set it in title case; drop the capitals. The README's title, "Synthetic Video Generation for Robot Learning Using World Foundation Models", is fine unchanged.

## E. Figures and packaging

- **Fig. 1 (EgoScale plots)** is a screenshot of a figure from another paper. Springer requires written permission to reproduce it, and there is no time to get it. Options: cite the result in prose with the five numbers (0.30 to 0.71), or redraw a single bar chart from those numbers with "data from Zheng et al. [egoscale]" in the caption. Redrawing from published numbers does not need permission.
- **Fig. 2 (pipeline)** is draft 1's TikZ diagram pasted as a bitmap. Use the TikZ source from `paper/main.tex` (or draft 3's version in `paper3/sections/method.tex`) so it is vector and legible at print size. The caption "you will need to define this better" needs replacing with draft 3's: every input to the renderer is produced by an earlier stage.
- **Fig. 4** carries a cropped page header ("4 S. Jha et al.") from the draft 3 PDF. Rebuild from `paper3/figures/s08_detection.png` plus the listing in `paper3/sections/method.tex`.
- **Fig. 5** is a dark screenshot of JSON and duplicates Fig. 4's listing; draft 5's own caption says it may be overkill. Drop it, or typeset as a listing in an appendix.
- **Figs. 6 and 7** keep the "Old / New" chrome from the slides. Use the raw frames (`review/images/result-bucket-old.png`, `result-bucket-new-blue.png`, `result-pillows-old.png`, `result-pillows-new-blue.png`) as subfigures (a) and (b). Note the deck stored the pillow pair in reverse order; the corrected names are in `results-revised.md` Notes.
- **Fig. 8** shows two identical frames. If it stays, the caption must say that is the point (conditioning frame beside a forecast frame, nothing moved).
- **Figures to add:** the mask-construction strip (slide 11), the four control maps for one frame (slide 10), and the leakage per-frame plot or the frame-30 ΔE heatmap (`review/leakage/bucket/`). All exist in `paper3/figures/` and `review/leakage/bucket/`.
- **Template.** The submission must be LNCS LaTeX (`llncs`, `splncs04`). `paper3v2/` is the LaTeX copy reserved for this; `paper3v2/build.sh` builds it (see the memory note on the MiKTeX PATH quirk). Tables in booktabs, "Fig. 3" and "Table 2" in text, every figure with a standalone caption that states what to notice.
- **Licence to Publish** signed, author order (Shrey Jha, Skyler Saucedo, Frank Tanner), emails and ORCIDs filled in (`review/assumptions.md` D3 still lists placeholders).
- **Clearance** to publish clips, frames, prompts and the ontology schema is confirmed with Frank Tanner (`answers-from-shrey-notes.md`); say so in an acknowledgement or data statement if the venue asks.

## F. Suggested order of work for the four days

1. Today: send Section C to Shrey. Fix A1 to A11 (numbers and citations) in the Google Doc or directly in `paper3v2/`. Decide where the paper is typeset; the LaTeX copy already has the tables, equation and bibliography.
2. Day 2: move B1 to B6 and B10 into place (setup, Table 1, weights, mask, leakage, Predict2, Closing the gap). Fix A12 to A25 (model names, mask semantics, figure captions).
3. Day 3: Related Work and references (B7, B8); figure rebuilds (Section E); limitations paragraph (B11); abstract (B13).
4. Day 4: the prose pass (Section D), a full read for every remaining [VERIFY] and [CITATION NEEDED], build the PDF, check page count and overfull boxes, sign and submit.
