# Draft 4: Results

Four variants of the Results section, each a different way to organize the same evidence. Before them, a review of how the six reference papers in `references/` build their Results sections, and what that review implies for ours. All numbers come from `technical-details.md` and `draft-4-skyler/methodology.md`; nothing here is new measurement. Written 2026-10-17.

---

## Part 1. How the reference papers write Results

Read from the PDFs in `references/` (text extracted with pdftotext). One entry per paper: how the section is organized, what the unit of evidence is, what the tables and figures carry, and what to take from it.

### MimicGen (Mandlekar et al., CoRL 2023), Sec. 5 to 7

- **Organization.** A separate "Experiment Setup" section (tasks, variants D0/D1/D2, data generation protocol, policy learning protocol, reporting convention) precedes "Experiments". Experiments then opens with one sentence listing four things the section will show, and each subsection is a run of bold-faced claims, each followed by the evidence for it ("MimicGen data vastly improves agent performance on the source task. ... Square (11.3% to 90.7%)").
- **Unit of evidence.** Policy success rate, 3 seeds, max across evaluations, reported with standard deviation in one large table (Fig. 4 left) that covers every task and variant.
- **The honest part.** A whole subsection (6.3, "Analysis") asks questions the system does not answer cleanly: more source demos help only modestly; some source demos generate far more successes than others; returns diminish past 1000; generation success rate does not predict policy performance. The real-robot numbers (36 and 14 percent) are low and are reported with a hypothesis for why.
- **Take.** The bold-claim-then-evidence paragraph is the clearest form for a short paper. The "Analysis" subsection is the model for reporting what we found that we did not expect.

### Data Scaling Laws (Lin et al., ICLR 2025), Sec. 4 to 6

- **Organization.** Results are organized by the variable swept (objects, environments, both), each with its own figure, then a quantitative fit (power law, Pearson r in the legend), then a strategy derived from the fit, then a verification on two new tasks (Table 1, mean and std across 8 unseen environments).
- **Unit of evidence.** Normalized score averaged over 40 trials with 95 percent confidence intervals shaded in every curve.
- **What makes it persuasive.** Every figure has the same axes and the same six data-usage curves, so the reader learns one visual grammar and reuses it. The numbered observations after each figure ("(1) ... (2) ... (3) ...") state what to notice.
- **Take.** This is an empirical-study paper, and ours is closer to that shape than to a system paper. The enumerated observations after a figure are a form we can use for the leakage plot.

### pi0 (Black et al., 2024), Sec. VI

- **Organization.** Opens with four research questions in bold, then one subsection per question (base model, language following, new dexterous tasks, complex multi-stage tasks). Each subsection states the setup, the baselines and why they are the right baselines, the metric, and then the result in prose that points at a figure.
- **Unit of evidence.** Normalized score over 10 episodes per task and method, bar charts; data-scaling curves for fine-tuning.
- **The honest part.** Confounders are named in the text ("it is hard to make this last comparison fair: pi0-small uses fewer parameters"). Baselines that could not be trained to parity are flagged and a "compute parity" version of the own model is added.
- **Take.** Research questions as the organizing device is a good fit for a paper whose central question is open. The habit of naming the confounder in the same sentence as the result is one we should copy.

### FieldGen (Wang et al., 2025), Sec. IV

- **Organization.** Three stated questions (equal-time effectiveness, equal-data quality and generalization, ablations), then one subsection per question plus a diversity measurement, two ablations and an effort measurement. Tables I to IV are dense grids of success rates over tasks, policies, and budgets.
- **Unit of evidence.** Success rate over 12 randomized placements, two policy backbones, no variance reported.
- **What is useful to us.** FieldGen defines its own coverage metric (fraction of voxels traversed) and its own effort metric (Collection Time Ratio) and reports them in small tables. A paper is allowed to invent a measurement when the standard one does not exist, provided it defines it in one sentence and states the caveat.
- **Take.** The precedent for our leakage metric: define it, tabulate it, say what it does not capture.

### LingBot-VLA (Wu et al., 2026), Sec. 5

- **Organization.** Benchmark description first (platforms, data collection, protocol, metrics) at a level of detail most papers leave to an appendix; then real-world comparison, simulation comparison, throughput, ablations (scaling, data efficiency).
- **Unit of evidence.** Success rate and progress score over 15 trials per task-robot pair, 22,500 trials in total, one large table.
- **Take.** The protocol detail (same robot unit, randomized order, 3-minute limit, termination criteria) is what makes a large benchmark credible. Not our scale, but the lesson applies at ours: state the protocol fully even when the evaluation is inspection.

### EgoScale (Zheng et al., 2026), Sec. 3

- **Organization.** Five research questions up front, then an "Experiment Setup" subsection (tasks, demonstrations per task, metric, seeds, trials, initialization procedure), then one subsection per question with a declarative title that states the finding ("Policy Performance Scales with Pretraining Data Size").
- **Unit of evidence.** Task completion score and success rate, 2 seeds, 10 trials, bar charts; a scaling curve with a fitted equation and R-squared.
- **Take.** Declarative subsection titles that state the finding are the strongest form for a reader who skims. Our findings can be titled the same way, including the negative ones ("The Edit Does Not Stay Inside the Mask").

### What the six have in common, and where we differ

1. Every one of them reports a downstream policy result with a number. We have none. Our Results section therefore cannot end on the beat theirs end on, and must not imply one.
2. Every one states the evaluation protocol fully (trials, seeds, metric, initialization) before the first result. Ours is inspection plus one measurement on one clip; the protocol is short but must still be stated, including why only one clip.
3. Four of six organize by research question or by bold claim. Two (Lin, FieldGen) organize by the variable swept. Both forms are available to us.
4. All six report variance or confidence intervals somewhere. We can report the per-frame standard deviation of the leakage metric and should.
5. MimicGen and pi0 report low or negative numbers and give a hypothesis in the same paragraph. That is the model for our Predict2 outcome and the whole-frame recolors.
6. None of them lets a projection stand as a result. Our 8,352 is capacity, and belongs in a "cost of scaling" paragraph that says so.

---

## Part 2. The evidence available (one list, used by all four variants)

| Item | What it is | Status |
|---|---|---|
| Setup | 8 recordings, 116 clips, 4 fps, 854 x 480, one A100 80 GB; reasoning 130 s, Transfer 20 min, Predict2 3.5 min per clip; GPT-4o mini about 0.12 USD total | Confirmed |
| What was run | reasoning on 116 clips; 64 Transfer renders over 10 clips; 2 Predict2 renders; no policy; no baseline | Confirmed |
| Running example | counter wiping, blue countertop: counter blue, hand pose, bucket geometry and motion preserved; towels, bucket, wall, hand tone, ceiling fixture, bucket label changed although named as preserved | Confirmed by inspection |
| Multi-texture case | cloth folding, cobalt blanket prompt: nearly every surface turned blue; pillow pattern survives as relief; hands preserved | Confirmed by inspection |
| Adjacent-object case | cable wrapping, blue desk prompt: blue spreads onto shelf objects and cable | Confirmed by inspection |
| Shape-collapse case | bed making, navy rug prompt: bedspread correct, surfaces smear, hand warps | Confirmed by inspection |
| Leakage metric | bucket clip, 60 frames: target mean ΔE 75.5 (std 4.0), protected 34.8 (std 7.2); chroma-only 68.2 vs 24.2; 94.5 percent of protected pixels above 10, 65.3 percent above 20; ratio 0.46 | Measured |
| Why one clip | shelf and pillow exported masks cover 0.001 and 0.025 of the frame | Measured; whether these were the masks used is Open |
| Weight sensitivity | edge bounded both sides; depth upper bound; vis near zero; guidance 2 to 3 under-applies, above 5 loses realism | Confirmed, qualitative |
| Predict2 | cable wrapping and paper rotation: no motion of the target object in either; scene reproduced | Measured from first and last frames |
| Cost of scaling | 64 renders about 21 A100-hours; 116 x 72 = 8,352 at about 2,800 A100-hours | Projection |

Figures available: the running example pair (slides 3, 4); the cloth-folding pair (slide 14); desk, rug and Predict2 stills (slides 15, 16); the leakage per-frame plot and the frame-30 heatmap with mask contour (`review/leakage/bucket/`); the mask strip (slide 11).

---

## Part 3. Four Results sections

Citation keys as in refs.bib. "Fig. X" and "Table X" to be numbered at typesetting. Each variant is complete on its own.

### Variant A. By research question (pi0 and EgoScale form)

Three questions, stated at the top, one subsection each, with a declarative title that gives the answer.

---

**Results.** The experiments answer three questions. Does the pipeline produce appearance variants that keep the recorded action? Does the edit stay where the mask and prompt send it? Can the same models produce a change of action rather than of appearance?

**Setup.** One person recorded 8 egocentric videos of household chores, about 10 minutes each, with a handheld camera. TransNetV2 [transnetv2] split them into 116 clips of at most 15 s at 4 fps and 854 x 480, about 30 minutes in total. All runs used one A100 80 GB through Google Colab Pro+. Per clip, reasoning took 130 s, a Transfer render 20 min and a Predict2 render 3.5 min; GPT-4o mini across all 116 clips cost about 0.12 USD. We ran the reasoning stage on every clip and rendered 64 Transfer variants of 10 source clips, about six per clip, plus two Predict2 clips. Evaluation is by inspection of matched source and variant frames and by the masked color-difference measurement defined below. No policy was trained on the output and no baseline was run; Sec. X returns to both.

**The action survives; the appearance changes beyond the target.** Fig. X shows the running example under the blue-countertop prompt. The counter is blue, the hand pose and bucket geometry are preserved frame for frame, and the motion is the source motion, so the variant is a demonstration of the same wiping action under a new surface. The prompt named the bucket, the towels and the lighting as preserved, and each of them changed: the towels became blue cloth, the bucket grey-blue, the wall beige, the hand tone lighter, and a ceiling fixture appeared that the source does not contain. Fig. X shows three further renders that span what we saw across the 64. In the cloth-folding clip the prompt asked for a cobalt blanket on one side of the bed and the render turned nearly every surface blue, the pillow pattern surviving only as relief. In the desk clip the blue of the desk spread onto the shelf objects and the cable. In the bed-making clip the navy-rug prompt returned the correct bedspread with smeared surfaces and a warped hand, the shape-collapse failure that bounds the edge weight from below (Table X). In every render the geometry and the hand motion of the source are retained; in every render color is applied beyond the target.

**The edit does not stay inside the mask.** To put a number on the unintended change we compare source and variant frame by frame in CIELAB and split the per-pixel CIE76 distance ΔE by the tracked mask M: pixels inside M are the target the prompt asked to change, pixels outside are the ones it asked to preserve. A ΔE of about 2 is just noticeable and 10 is an unmistakable change. Table X gives the result for the counter-wiping clip, the one render for which a usable tracked mask was retained. Three observations follow. (1) The recolor worked: the target moved by a mean ΔE of 75. (2) The protected region moved by 35, almost half as much, and 95 percent of its pixels moved by more than 10. (3) The chroma-only distance (a and b channels) is 24 in the protected region against 68 in the target, so the change is color, not exposure. Fig. X shows where: the towels and bucket, adjacent to the target, change nearly as much as the target does, and the wall changes less but visibly; the gap between the two curves is stable across the clip and the protected curve never approaches zero. The segmentation control at weight 0.175 and the prompt's preservation clause were the two mechanisms for containment, both soft, and neither was sufficient. The measurement covers one clip because the tracked masks retained for the desk and cloth-folding renders cover under 1 percent and about 2 percent of the frame, against roughly half for the regions they were meant to mark; with such masks the inside-outside split is meaningless. If those were the masks Transfer received, the segmentation control carried no information for those renders, which would account for the whole-frame recolor of Fig. X directly. We have not confirmed whether they were, and report the observation rather than the conclusion.

**Control weights trade shape against change.** Table X records the sweep on the counter-wiping clip. We did not grid-search; each weight was moved until a failure appeared and backed off, and the result was checked on three further clips. Edge is the dominant term and is bounded on both sides within a narrow band: lower and objects lose shape, higher and nothing changes. Depth has an upper bound at which the scene flattens. Vis must be near zero for any recolor, because it conditions on the source colors and opposes the prompt. Guidance scale trades prompt adherence against realism: at 2 and 3 the model often ignored the variation or applied it weakly, above 5 it followed the prompt and no longer rendered the same room, and all reported renders use 4. No setting recolored the target fully and left the protected region unchanged.

**Action-level prompts produce no action.** Two action variations from the ontology were run through Cosmos Predict2 [cosmospredict2] (35 steps, 848 x 480, 93 frames at 16 fps): winding a charger cable around its block with the block held fixed, and a sheet of paper on the desk rotating 90 degrees while three objects on it stay in place. Both prompts state what moves, what stays fixed and how the moving part stays attached; the cable prompt points the model at the input frames as the reference motion. In both renders the forecast reproduces the conditioning scene and neither the cable nor the paper moves (Fig. X). The model held the scene stable, which is a form of success for a world model, and did not perform the action, which was the only thing asked of it. We did not fine-tune Predict2.

**Cost of scaling.** At the per-clip figures above and 72 admissible variations per clip, rendering every variation of every clip would produce 116 x 72 = 8,352 variants at about 2,800 A100-hours. The 64 we rendered took about 21 GPU-hours; reasoning and filtering for all 116 clips took a few hours and under a dollar. The render is the entire cost, and it is the stage whose output is not yet contained.

(about 1,050 words)

What it emphasizes: the open question as the frame. Each subsection title is an answer, including two negative ones. Closest to EgoScale and pi0. Longest of the four.

---

### Variant B. By claim, bold-faced (MimicGen form)

A short setup, then a run of claims in bold with the evidence after each, and a closing "Analysis" subsection for what we found that we did not expect.

---

**Results.**

**Setup.** 8 egocentric recordings of household chores, 116 clips of at most 15 s at 4 fps and 854 x 480 after TransNetV2 [transnetv2] splitting; one A100 80 GB; reasoning 130 s, Transfer 20 min and Predict2 3.5 min per clip; GPT-4o mini about 0.12 USD for all clips. Reasoning ran on all 116 clips; 64 Transfer variants of 10 clips and two Predict2 clips were rendered. Evaluation is inspection of matched frames and the masked ΔE measurement of Sec. X. No policy was trained; no baseline was run.

**Single-surface recolors keep the recorded action.** Under the blue-countertop prompt the counter is blue while hand pose, bucket geometry and motion match the source frame for frame (Fig. X). Across all 64 renders the hand motion and object geometry of the source were retained; the edge and depth controls did their job.

**Every render changes more than the prompt allowed.** In the running example the towels became blue cloth, the bucket grey-blue, the wall beige, the hand lighter, and a ceiling fixture appeared, each of them named as preserved in the prompt. In the cloth-folding clip a prompt for one cobalt blanket recolored nearly every surface (Fig. X). In the desk clip blue spread from the desk onto the shelf objects and the cable. In the bed-making clip the navy-rug prompt smeared the surfaces and warped the hand.

**Leakage is about half the size of the intended edit.** On the counter-wiping clip the mean CIE76 ΔE between source and variant is 75 inside the tracked mask and 35 outside it (Table X); 95 percent of protected pixels moved by more than 10, and the chroma-only distance (24 outside against 68 inside) shows the change is color rather than exposure. The per-frame curves (Fig. X) keep a stable gap and the protected curve never approaches zero. The seg control at weight 0.175 and the preservation clause in the prompt were both soft, and together they held back about half of the edit.

**Vis must be nearly off and edge sits in a narrow band.** The weight sweep on the counter-wiping clip (Table X) found edge bounded on both sides, depth bounded above, and vis required near zero because it conditions on the source colors and fights any recolor. Guidance scale 4 was the one value that applied the variation without losing the room; 2 and 3 under-applied it and above 5 the scene stopped reading as the same place.

**Action prompts return the scene unchanged.** Predict2 [cosmospredict2] was asked to wind a cable around its block and to rotate a sheet of paper 90 degrees, with prompts that fix what moves and what stays. In both forecasts (93 frames, 16 fps) nothing moves (Fig. X). The scene is held stable; the action is not performed. Predict2 was not fine-tuned.

**Rendering is the whole cost.** Reasoning and filtering for 116 clips took a few hours and under a dollar; the 64 renders took about 21 A100-hours. Rendering all 72 admissible variations of all 116 clips, 8,352 variants, would take about 2,800 A100-hours.

**Analysis.** Three things we did not expect. The tracked masks retained for the desk and cloth-folding renders are almost empty, under 1 percent and about 2 percent of the frame; if those are the masks Transfer received, SAM2's propagation collapsed and the seg control carried nothing for those renders, which would explain the whole-frame recolors without appeal to leakage at all. We have not confirmed which it is. The ontology's errors are visible in the running example (a wrong task name, an impossible failure mode for an open bucket), and the filter's precision is unmeasured, so 72 admissible variations per clip is a count and not an accuracy. And the leakage measurement is on one clip; the same script runs unchanged on any clip for which a usable mask exists.

(about 640 words)

What it emphasizes: scannable claims, each with its number. The negative claims get the same bold treatment as the positive one, which is the honest shape. The "Analysis" subsection is where the mask-collapse question lives. Shortest of the four.

---

### Variant C. Success, then failure, then measurement (the talk's order)

The order of slides 12 to 16: one success, then the failures, then the number that explains them, then the action attempt. Closest to draft 3.

---

**Results.**

**Setup.** As in Variant A, one paragraph.

**Appearance variation.** Fig. X is the running example under the blue-countertop prompt. The counter is blue, hand pose and bucket geometry are preserved frame for frame, and the motion is the source motion. Every unintended change is also easy to see: the rags became blue cloth, the bucket grey-blue, the wall beige, and a ceiling fixture appeared, although the prompt named the bucket, towels and lighting as preserved. Fig. X shows the cloth-folding clip, where the prompt asked for a cobalt blanket on the left of the bed and the render turned nearly every surface blue. Where the counter clip leaks at the edges of the target, a frame with many textures fails almost completely. Fig. X also shows a blue-desk prompt whose color spreads onto the shelf objects and the cable, and a navy-rug prompt that returned the right bedspread with smeared surfaces and a warped hand, the shape-collapse failure of Table X. In every case the geometry and the hand motion of the source are retained, and in every case color is applied beyond the target.

**Measuring leakage.** To put a number on the unintended change we compare source and variant frame by frame in CIELAB and split the per-pixel CIE76 distance ΔE by the tracked mask M; a ΔE of 10 is unmistakable to a viewer. Table X gives the result for the counter clip, the one render with a usable tracked mask. The target moved by a mean ΔE of 75, so the recolor worked. The protected region moved by 35, 95 percent of its pixels by more than 10, and the chroma-only distance shows the change is color rather than exposure. Fig. X shows the spatial pattern at frame 30: the towels and bucket beside the target change almost as much as the target, the wall less but visibly. The seg control and the prompt's preservation clause were the two soft mechanisms for containment, and neither was sufficient. The tracked masks retained for the desk and cloth-folding renders cover under 1 and about 2 percent of the frame, so the measurement cannot be repeated on them; whether those are the masks Transfer received, in which case the seg control carried no information for those renders, is not yet confirmed.

**Control-weight sensitivity.** Table X summarizes the sweep on the counter-wiping clip, done by moving each weight until a failure appeared and backing off rather than by grid search. Edge is the dominant term and bounded on both sides. Vis must be near zero because it conditions on the source colors. Guidance scale 4 was the usable value between under-application at 2 and 3 and loss of realism above 5. No setting recolored the target fully and left the protected region unchanged.

**Action-level variation.** Two action variations were run through Cosmos Predict2 [cosmospredict2] (35 steps, 848 x 480, 93 frames at 16 fps): winding a charger cable around its block, and a sheet of paper rotating 90 degrees with three objects staying on it. In both renders the forecast reproduces the conditioning scene and the cable and paper do not move (Fig. X). The model held the scene stable, a kind of success for a world model, and did not perform the action, the only thing we asked of it.

**Cost of scaling.** As in Variant A, one paragraph.

(about 620 words plus the two shared paragraphs, about 800 in total)

What it emphasizes: the narrative of the talk. A reader who saw the deck recognizes the order. Least structured of the four and the one Skyler's draft 3 feedback already approved in shape.

---

### Variant D. Organized by the variable examined (Lin et al. form)

Each subsection isolates one thing: the target of the edit, the region of the edit, the control weights, the kind of variation. Each ends with enumerated observations.

---

**Results.**

**Protocol.** Source material, models, hardware and per-clip times as in Variant A. Every render is compared with its source on matched frames. For the counter-wiping clip, where a tracked mask of the target surface was retained, we also compute the per-pixel CIE76 ΔE in CIELAB between source and variant and report it separately inside and outside the mask, per frame and over the clip, together with the chroma-only distance and the fraction of protected pixels above ΔE thresholds of 10 and 20. We rendered 64 Transfer variants of 10 clips and 2 Predict2 clips, reasoned over all 116 clips, trained no policy and ran no baseline.

**Effect of the target.** We compare the four source clips of Fig. X, which differ in how much of the frame the target occupies and how many distinct textures surround it. (1) When the target is one large uniform surface (the countertop, about half the frame), the recolor is complete and the geometry and motion of the source are retained. (2) When the target is one object among several textures (a blanket on a made bed), the render recolors the scene wholesale; the pillow pattern survives only as relief. (3) When the target is a surface with objects resting on it (a desk and shelf), the color spreads to the objects. (4) When the target is a floor surface partly occluded by the bed and the person (the rug), the render returns smeared surfaces and a warped hand. Observation (4) is the edge-weight lower-bound failure of Table X appearing at a fixed weight, which suggests the usable edge band is clip-dependent.

**Effect of the region.** Table X and Fig. X give the masked ΔE for the counter-wiping clip. (1) Inside the mask the mean ΔE is 75 with a per-frame standard deviation of 4; the edit is applied uniformly across the clip. (2) Outside the mask the mean ΔE is 35 with a standard deviation of 7, and 95 percent of pixels exceed 10. (3) The chroma-only distance is 68 inside and 24 outside; the protected-region change is a color change. (4) The spatial pattern (Fig. X) is graded by adjacency: towels and bucket, which touch the target, change almost as much as the target; the wall changes less. The ratio of outside to inside change is 0.46. Both containment mechanisms, the seg control at weight 0.175 and the preservation clause in the prompt, are soft, and this ratio is what they achieved together. The measurement is on one clip; the tracked masks retained for two others cover under 1 and about 2 percent of the frame and cannot support the split, and whether those are the masks the renderer received is unconfirmed.

**Effect of the control weights.** Table X. The sweep on the counter-wiping clip, by moving one weight at a time until a failure appeared, found: (1) edge bounded below by shape loss and above by no change, within a narrow band; (2) depth bounded above by flattening; (3) vis required near zero, since it conditions on the source colors and opposes the prompt; (4) seg taking the remaining budget. Guidance scale: 2 and 3 under-applied the variation, above 5 lost the scene, 4 used throughout. No combination recolored the target fully and left the protected region unchanged.

**Effect of the kind of variation.** Appearance variations go to Transfer, which preserves motion by construction. Action variations went to Predict2 [cosmospredict2]: winding a cable around its block, and rotating a sheet of paper with objects on it. (1) In both forecasts (93 frames, 16 fps) the scene is reproduced and the target object does not move. (2) The prompts were specific about what moves and what stays and, for the cable, pointed at the input motion as reference; specificity did not help. (3) Predict2 was not fine-tuned.

**Cost.** Reasoning and filtering for all 116 clips: a few hours and under a dollar. 64 renders: about 21 A100-hours. All 8,352 admissible variants: about 2,800 A100-hours, a projection.

(about 760 words)

What it emphasizes: the paper as an empirical probe. Each subsection isolates one factor, which is what the project rules ask of ablations. The "effect of the target" subsection is the new content: it reads the four renders as a sweep over scene complexity rather than as a success and three failures. Risk: with one clip per condition and no repeated seeds, calling it a sweep may draw a reviewer's objection; the enumerated form makes the n of 1 visible, which is the right side of that risk.

---

## Part 4. Shared tables and figures

**Table X (leakage).** Masked color difference for the counter-wiping variant, 60 frames. The protected region changes by almost half as much as the target, and nearly all of it changes visibly.

| | Target (inside M) | Protected (outside M) |
|---|---|---|
| Mask coverage (fraction of frame) | 0.50 | 0.50 |
| Mean ΔE | 75.5 | 34.8 |
| Std of per-frame mean ΔE | 4.0 | 7.2 |
| Mean chroma-only ΔE | 68.2 | 24.2 |
| Pixels with ΔE above 10 (percent) | | 94.5 |
| Pixels with ΔE above 20 (percent) | | 65.3 |

**Table X (weights).** As in `methodology.md` Section 19.

**Table X (cost).** Per-clip cost on one A100 80 GB: reasoning 2.2 min; GPT-4o mini about 0.12 USD for all clips; Transfer 20 min (35 steps at 31 s plus about 2 min of maps); Predict2 3.5 min (35 steps at 6 s).

**Figures.** Running example pair; cloth-folding pair; desk, rug and Predict2 stills in one strip; leakage per-frame plot; frame-30 heatmap with mask contour.

---

## Notes for discussion

- **Which to pick.** A if the paper is framed on the open question (abstract variant B); C if it is framed on the talk (abstract variant A); B if the section must be short. D is the most defensible to a methods reviewer and the least like the talk.
- **The fourth beat.** All six references close Results on a policy number. Ours closes on cost. Every variant says "no policy was trained" in the setup paragraph so that the reader is not waiting for it. Do not move that sentence to Limitations.
- **The mask question (A7) decides the wording of the multi-texture failure** in every variant. If Shrey confirms the near-empty masks were the ones used, the cloth-folding and desk results move from "leakage" to "no mask", and the paper gains a finding (a coverage check is required) and loses a comparison (the leakage metric cannot be run on them either way).
- **Variance.** Only the per-frame standard deviation exists. Seeds were not fixed for Transfer, so a repeat render would differ; say so once, in the setup.
- **Enumerated observations** (Lin et al. form) are used in A for the leakage subsection and throughout D. They are a clean way to make an n of 1 look like what it is.
- **Strike-list check.** None of the variants uses "robust", "significantly", "novel", "leverage" or "state-of-the-art". "Remarkably" and "notably", which the references use freely, are absent.
- **Numbers that appear in prose** (75, 35, 95 percent, 0.46) all also appear in Table X, so the prose can be thinned at typesetting without losing them.

---

## Part 5. Skyler's pick: draft 3 structure, practical register (2026-10-17)

Skyler chose draft 3's Results (Setup; Appearance Variation; Measuring Leakage; Action-Level Variation) and asked for two changes: make the count from 8 recordings to synthetic clips visible, and write the Setup so that a reader could repeat the process.

### The multiplier, honestly

| From | To | Factor | Status |
|---|---|---|---|
| 8 recordings, about 80 min raw | 116 clips, about 29 min retained | 14.5 clips per recording; 0.36 of the footage kept | Confirmed |
| 116 clips, 29 min | 8,352 admissible variants, about 35 h of candidate video | 72x in duration | Projection (capacity) |
| One 10-min recording | about 4.4 h of candidate video | 72x | Projection |
| 10 source clips, 2.5 min | 64 rendered variants, 16 min | 6.4x realized | Confirmed |
| 8 recordings | 8,352 variants | "1,044 clips per recording" | Misleading: 15 s clips against 10 min videos; do not use |

The sentence that holds: every 15 s clip admits 72 variations, so one 10-minute recording becomes about 4 hours of candidate video without a new room or a new recording. What was realized is 64 renders over 10 clips. Say "capacity" for the first and "rendered" for the second, every time.

### Section text

**4 Results**

**Setup.** One person recorded 8 egocentric videos of household chores (counter wiping, cloth folding, bed making, cable wrapping) with a handheld camera, about 10 minutes each. TransNetV2 [transnetv2], as packaged in Cosmos Curate, split them at shot boundaries into 116 clips; each clip was trimmed to at most 15 s and downsampled to 4 fps at 854 x 480, so that one manipulation action fits in the frame window Transfer renders in a single pass. Everything downstream ran on one A100 80 GB through Google Colab Pro+ with the public checkpoints of Cosmos 3 Nano, Cosmos Transfer 2.5, Cosmos Predict2 2B and SAM2, and an API key for GPT-4o mini. Table X gives what each stage costs per clip. Reasoning on the first frame takes about two minutes and produces the ontology, the boxes and the candidate variations; filtering and prompt writing for all 116 clips cost about 0.12 USD; a Transfer render takes 20 minutes, of which about two are control-map preprocessing; a Predict2 render takes 3.5 minutes. The control weights (edge 0.5, depth 0.2, vis 0.025, seg 0.175), guidance scale 4 and 35 denoising steps were fixed for every render after the sweep of Sec. X.

Table X traces the count from the recordings to the renders. The reasoning stage admits 72 variations per clip on average, so the 116 clips are capacity for 8,352 synthetic clips, about 35 hours of candidate video from 29 minutes of source: a 72-fold multiplier in duration, and one 10-minute recording becomes about 4 hours, with no new room and no new recording. We rendered 64 of them, about six variants of each of 10 source clips, which is 16 minutes of synthetic video at about 21 GPU-hours, plus two Predict2 clips. At these rates the full 8,352 would take about 2,800 A100-hours; a reader with N clips should budget N x 72 x 20 minutes for a complete render and N x 2 minutes for reasoning. Evaluation is by inspection of matched source and variant frames and by the masked color-difference measurement of Sec. 4.2, which needs only the source video, the rendered video and the tracked mask video. No policy was trained on the output.

**Table X.** From 8 recordings to synthetic clips.

| Stage | Count | Duration | Factor | Status |
|---|---|---|---|---|
| Recordings | 8 | about 80 min | | recorded |
| Clips after TransNetV2, trim, downsample | 116 | about 29 min | 14.5 per recording | measured |
| Admissible variations (72 per clip) | 8,352 | about 35 h | 72x in duration | capacity |
| Transfer renders | 64 (10 source clips) | 16 min | 6.4 per clip | rendered |
| Predict2 renders | 2 | 12 s | | rendered |

**4.1 Appearance Variation.** Fig. X is the running example under the blue-countertop prompt. The counter is blue, hand pose and bucket geometry are preserved frame for frame, and the motion is the source motion, so the variant is a demonstration of the same wiping action on a different surface. Every unintended change is also easy to see: the rags became blue cloth, the bucket grey-blue, the wall beige, and a ceiling fixture appeared, although the prompt named the bucket, towels and lighting as preserved. Fig. X shows the cloth-folding clip, where the prompt asked for a cobalt blanket on the left of the bed and the render turned nearly every surface blue. Where the counter clip leaks at the edges of the target, a frame with many textures fails almost completely. Fig. X also shows a blue-desk prompt whose color spreads onto the shelf objects and the cable, and a navy-rug prompt that returned the right bedspread with smeared surfaces and a warped hand, the shape-collapse failure of Table X. In every case the geometry and the hand motion of the source are retained, and in every case color is applied beyond the target. A reader trying this should expect the first behavior on a single large uniform surface and the second as soon as the target shares the frame with several textures.

**4.2 Measuring Leakage.** To put a number on the unintended change we compare source and variant frame by frame in CIELAB and split the per-pixel CIE76 distance ΔE by the tracked mask M; a ΔE of 10 is unmistakable to a viewer. The script takes three videos (source, variant, mask) and returns the mean inside and outside the mask per frame, the chroma-only distance, and the fraction of protected pixels above a threshold, so it can be run on any render for which the mask was kept. Table X gives the result for the counter clip, the one render with a usable tracked mask. The target moved by a mean ΔE of 75, so the recolor worked. The protected region moved by 35, 95 percent of its pixels by more than 10, and the chroma-only distance shows the change is color rather than exposure. Fig. X shows where: the towels and bucket beside the target change almost as much as the target, the wall less but visibly, and the gap between the two per-frame curves is stable across the clip. The seg control and the prompt's preservation clause were the two soft mechanisms for containment, and neither was sufficient. The masks retained for the desk and cloth-folding renders cover under 1 and about 2 percent of the frame, so the measurement cannot be repeated on them; if those are the masks Transfer received, the seg control carried no information for those renders. The practical lesson is to check mask coverage before rendering, which our pipeline did not do.

**4.3 Action-Level Variation.** Two action variations from the ontology were run through Predict2 (35 steps, 848 x 480, 93 frames at 16 fps): winding a charger cable around its block with the block held fixed, and a sheet of paper rotating 90 degrees while the objects on it stay put. Both prompts state what moves, what stays and how the moving part stays attached. In both renders the forecast reproduces the conditioning scene and the cable and paper do not move (Fig. X). The model held the scene stable, a kind of success for a world model, and did not perform the action, the only thing we asked of it. We did not fine-tune Predict2; a reader who needs action-level variants should expect to.

(about 1,000 words with the table)

### Notes

- Three sentences address the reader directly ("should expect", "should budget"). That is about the limit before an LNCS reviewer reads the section as a tutorial; the rest of the practical content is carried by the numbers in the Setup and the table.
- "72-fold" is tied to "candidate" or "capacity" at every mention. The 64 renders are the only synthetic video that exists.
- The leakage table, the weights table and the cost table are shared with Part 4.

---

## Part 6. Cost of scaling: one hour of egocentric video (Skyler's question, 2026-10-18)

### From one raw hour

| Quantity | Value | Basis |
|---|---|---|
| Clips | about 87 | 116 clips from about 80 min |
| Footage retained | about 22 min | 0.36 of raw after the 15 s trim |
| Admissible variations | about 6,260 | 72 per clip |
| Candidate synthetic video | about 26 h | 6,260 x 15 s |
| Multiplier | 26x on the raw hour, 72x on retained footage | |
| Reasoning time | about 3 GPU-hours | 130 s per clip |
| Filter and prompts | under 0.10 USD | 0.12 USD per 116 clips |
| Render time, all variants | about 2,090 A100-hours | 20 min per render |
| Render time per synthetic hour | 80 A100-hours | fixed by 20 min per 15 s clip, however many are rendered |

### Cost per hour of video

| Source | Cost per hour | Basis |
|---|---|---|
| Human collector | 8 to 15 USD | Skyler's figure, CITATION NEEDED |
| Pipeline, Transfer 2.5 on A100 | about 96 to 240 USD | 80 A100-hours at 1.2 to 3 USD per hour (Colab Pro+ and cloud list, VERIFY) |
| Pipeline, distilled Transfer on H100 | about 8 to 16 USD | NVIDIA's about 1 min per clip, 4 H100-hours per synthetic hour at 2 to 4 USD per hour, not run by us |

At current settings a synthetic hour costs 6 to 30 times a collector's hour. The cost claim holds only with the distilled model, which was not run. The claim that holds now is diversity: 72 appearance variants of every action with no new room, where Lin et al. say the room is what is scarce and the next hour in the same room is close to worthless. Whether a rendered variant counts as a new environment in their sense is untested, since layout, geometry and motion are unchanged and no policy was trained.

### Pros

- 72 appearance variants per clip without a new room or recording; proposal stage costs minutes and cents.
- Action held fixed by construction, so trajectories and action labels carry over to every variant unchanged.
- Variations conditioned on the object's role; schema makes every proposal inspectable and countable.
- One A100, public checkpoints, one API key.
- Deployment footage becomes training variants in the same loop.

### Cons

- 80 A100-hours per synthetic hour, 6 to 30 times the collector rate, until the distilled model is timed.
- Leakage: protected region moved by about half as much as the target on the one clip measured; variants would teach co-varying colors.
- Appearance only; layout, geometry, contact and motion do not vary; action-level attempts produced no motion.
- Multi-texture scenes recolor wholesale; retained masks for two of them nearly empty; mask collapse undetected by the pipeline.
- 4 fps undersamples contact; ontology error rate unmeasured; seeds not fixed; one closed LLM in the loop; one person, one home.
- No policy trained, no baseline run; the premise remains a premise.

### Where this goes in the paper

The per-hour table belongs in the "Cost of scaling" paragraph of Results with the two VERIFY prices resolved or the dollar figures dropped in favor of GPU-hours. The pros and cons are the Discussion, in prose. The sentence to keep is: at today's speed the pipeline buys diversity rather than cheaper hours.
