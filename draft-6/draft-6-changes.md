# Draft 6: what changed from draft 5 and why

Written 2026-10-18. Draft 6 keeps draft 5's section order (Abstract, Introduction, Method with three subsections, Results, Closing the Gap, Conclusion, References) and its nine figure positions. Section numbers follow LNCS (the abstract is unnumbered), figures are cited as "Fig. N", citations are numbered in order of first appearance and formatted in Springer LNCS style. Items below are keyed to `draft-5/draft-5-analysis.md` (A = Sec. 4.1 accuracy, C = Sec. 5 consistency) and `draft-5/draft-5-shore-up.md` (A-numbers).

## Figure 1

Replaced the EgoScale screenshot with one figure of five panels (a) to (e) from `policy-vs-data-amount/figures/policy_vs_data_amount.{pdf,png}` (copied into `figures/`), one caption, and one explanatory paragraph that states the log-linear shape, our fitted increment per doubling (0.085), and Lin et al.'s diversity result. No reproduction permission is needed.

## Accuracy against the references (analysis Sec. 4.1)

- EgoScale: "20,000+ hours needed per task" and "upper limits of 0.71" replaced with the paper's statement: 20,854 hours of pretraining across tasks, score rising from 0.30 to 0.71 with no sign of saturation; the log-linear law attributed to the loss, not the score.
- FieldGen: "2.47x increase over a 2hr training example" replaced with the paper's Collection Time Ratio gain (2.47-fold) and what it saves (operator time, not environments).
- MimicGen: "200 into 50,000" made "fewer than 200 into over 50,000", matching the paper.
- Collection cost: one figure (8 to 15 USD), marked [VERIFY: source].

## Internal consistency (analysis Sec. 5)

- Source material: eight recordings of about 10 minutes, about 80 minutes raw, 116 clips of at most 15 s, 29 minutes retained, throughout (was "a 10 min video" in Method and "3, 10-minute video examples" in Sec. 5).
- Multiplier: 72-fold in duration as capacity, 64 rendered, everywhere (was "x10", "hundreds", "thousands").
- 72 admissible variations per clip (was 70 in Sec. 3.1 and 72 in Sec. 5).
- Prompt length: "a few hundred words" with [VERIFY] (was 150 in one place, 300 in the instruction).
- Reasoning stage: one step, the Cosmos 3 Nano reasoning tower, a vision-language model (was Cosmos Predict and then Cosmos Reason "a VLA" as two consecutive steps).
- Mask semantics: stated as a soft control in Sec. 2.3 and shown failing in Sec. 3 (was "exactly which pixels the model can change").
- Rule 2: the preservation clause "reduces but does not prevent" change, consistent with Fig. 6 (was "protects").
- Fig. 6: caption and text name the unintended changes as unintended, with the measured ΔE (75 target, 35 protected, 95 percent of protected pixels above 10); "varying the skin color of the human" and "entropy as desired" removed.
- Fig. 7: the cause is the near-empty retained mask (2 percent coverage), not Canny parameters; prompt described per the recovered prompt, with [VERIFY].
- Fig. 8: text matches the figure and the confirmed outcome (no motion); the reversal and spaghetti account is kept as a [VERIFY] note so Shrey can reinstate it with frames if the run exists; "VLA" replaced by Predict2.
- Fig. 9: caption states what was asked and what happened in each panel.
- Cost: 1.20 USD identified as a per-A100-hour price; 80 A100-hours per synthetic hour; 0.12 USD as the LLM total for all clips. The TODO table is now Table 1.

## Register (CLAUDE.md Sec. 3)

Strike-list words removed (leverage, robust, powerful, Additionally, Lastly, It should be noted, critical, exceptional, Surprisingly, cohesive and practical, meaningful solution). Rhetorical questions turned into statements. Title set in title case. Note-form expanded. Abstract made one paragraph with the scale number and the measured boundary. Model names corrected (GPT-4o mini; world foundation models rather than VLA; VLM for the reasoner). Spelling fixed.

## Added, because the fixes required it

- A background paragraph on world foundation models and related work, replacing the "Background?" placeholder (from draft 3's related-work paragraph, 14 citations).
- The control weights, guidance scale and denoising steps in Sec. 2.3, so the "tunable parameters" have values.
- The sentence "No policy was trained on the output, and no baseline was run" in Results.
- Keywords, author line, and a 27-entry reference list built from `paper3/refs.bib` plus the five references in `references/`. Every entry carries a URL: the arXiv abstract page for papers with a preprint (all 22 IDs checked against the arXiv API on 2026-10-18 and matched by title), the DOI for Canny 1986 (resolves to IEEE Xplore document 4767851), and the model-card or product page for the four NVIDIA and OpenAI entries, as recorded in `refs.bib`. For the conference papers the arXiv link stands in for the proceedings page; the LaTeX version should use the publisher DOI where `splncs04` prints one.

## Fig. 5 as a JSON listing (added 2026-10-18, on Skyler's request)

The dark screenshot is replaced by a typeset JSON listing in the exact schema of `COSMOS3_BBOX_VARIATION_PROMPT` (Shrey's answers, pages 6 to 10), abridged in the draft and complete in `figures/fig5_ontology_bucket.json`. What is the model's actual output, from deck slide 8: the task name, phase and action primitive; the bucket's name and role; the three `what_robot_must_handle` and three `common_failure_modes` entries. What is observed from the detection image: the five object names and ranks. Everything else (bounding-box coordinates estimated from the detection image, colors, materials, states, the variation lists, scene variations and dataset gaps) is a reconstruction written to be consistent with the frame and the schema, so the figure can be typeset now. Before submission, replace the file with the saved Cosmos 3 Nano output for this clip, or state in the caption that the listing is illustrative. If the saved output is not recoverable, the honest caption is: "an ontology in the schema returned by Cosmos 3 Nano; the task block and robustness gaps are the model's output, the remainder is illustrative."

## Still open ([VERIFY] markers in the draft)

Affiliations and ORCIDs; collection cost source; raw proposal count; typical prompt length; depth model; camera (handheld or head-mounted); recording length per task; code release; Fig. 7 prompt; whether the retained masks were the ones used; the Predict2 reversal run; the Colab A100-hour price; Fig. 4 image rebuild; whether to keep Fig. 5.
