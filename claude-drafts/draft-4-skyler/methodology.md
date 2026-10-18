# Draft 4: Methodology

A single account of what the pipeline is, what each stage does, what settings it ran with, how the output was evaluated, and what was actually produced. Compiled 2026-10-17 from drafts 1 to 3 (`paper/`, `paper2/`, `paper3/`), the deck review, `technical-details.md`, `review/assumptions.md`, `review/leakage/README.md`, Shrey's answers and the prompt files. Every number carries the same status as in `technical-details.md`: **Confirmed** (author-stated and consistent), **Measured** (computed from files in the workspace), **Projection** (arithmetic), **Deck only** (on a slide, superseded or unverified), **Open** (no reliable value).

The purpose of this file is to fix the methodology in one place before the Method, Experiments and Discussion sections of draft 4 are written, so that the section variants can be judged against it rather than against each other.

---

## 1. The methodology in one paragraph

We take a real egocentric clip as the unit of data and multiply it by permuting the appearance of the scene around the recorded action. A reasoning model reads the clip and writes a structured ontology: the task, each task-relevant object with its box and its role in the task, and the variations each object could plausibly take while the task stays the same. A language model rejects implausible candidates and writes a generation prompt for one accepted variation. A segmenter turns the ontology's boxes into tracked masks, and a subtraction step isolates the one surface to repaint. Edge, depth, blurred-color and segmentation maps derived from the source clip guide a video-to-video world model, which renders the variant with the source motion intact. Action-level variations proposed by the ontology are routed to a separate video-prediction model. Output is judged by inspection of matched frames and by a masked color-difference measurement that separates the intended edit from leakage into the protected region. No policy was trained on the output, and no baseline was run.

---

## 2. Design premise

The premise that separates the pipeline from domain randomization is that the model should understand the scene before it varies it. Domain randomization swaps colors and textures with no notion of the task, so a cleaning bucket can receive a texture no bucket has. In our pipeline the reasoning stage records that the bucket in the counter-wiping clip is a waste container in a cleaning task, and the variations proposed for it are conditioned on that role (label designs, sizes, materials that bear scrubbing) rather than drawn at random. The deck calls this "ontology-driven variation" (slide 7); the drafts call it task-grounded variation.

Two consequences follow for the design. First, the same structured output drives both the text prompt (what should change) and the segmentation mask (where it should change), so one decision is made once and used twice. Second, the ontology separates appearance-level variations, which a video-to-video renderer can produce while keeping the recorded motion, from action-level variations such as "bucket tips over", which require a different kind of model. The pipeline has one branch for each.

The claim that this premise yields better training data than random variation is stated in all three drafts as a hypothesis, because no domain-randomization baseline was run (`review/assumptions.md`, D2). Draft 3's introduction says it "holds by construction and still awaits a baseline", which is the strength the evidence allows.

---

## 3. Data preparation

| Quantity | Value | Status |
|---|---|---|
| Raw recordings | 8, egocentric, handheld, one person doing household chores | Confirmed |
| Length per recording | about 10 min (about 80 min raw) | Confirmed |
| Tasks visible in the shown clips | counter wiping, cloth folding on a bed, bed making, cable wrapping at a desk | Confirmed; full task list across the 8 recordings not provided (Open) |
| Shot-boundary clipping | TransNetV2, as packaged in Cosmos Curate | Confirmed |
| Clips after clipping | 116 (129 was a miscount) | Confirmed |
| Clip length and rate | at most 15 s, downsampled to 4 fps, 60 frames | Confirmed, Measured |
| Resolution | 854 x 480 | Measured (Shrey's table said 848 x 480 "implied") |
| Total duration | about 30 min; the stated 31 min 44 s exceeds 116 x 15 s | Open |

What Cosmos Curate did: clipping only. The deck's speaker note that the clip was "produced using Cosmos Curate" means shot-boundary detection, not capture. The deck's "2 to 3 hours of data" (slide 1 notes) is inconsistent with every other figure and is not used.

---

## 4. Stage 1: Reasoning (clip to ontology)

**Model.** The reasoning tower of Cosmos 3 Nano (author-stated 16B total, 8B reasoning tower, 8B generation tower; one third-party source says 8B total, not verified against the Cosmos 3 report). The deck labels this stage "Cosmos Reason" on slides 5, 6 and 8 and lists Cosmos 3 as future work on slide 18; both are wrong, Cosmos 3 Nano was the reasoner in the pipeline that ran. The generation tower of Cosmos 3 Nano was tried and had no video-to-video support.

**Input.** The first frame of the clip, with a fixed instruction (`COSMOS3_BBOX_VARIATION_PROMPT`, pages 5 to 12 of `answers-from-shrey.pdf`; abridged in draft 1 Appendix A). Draft 1 justifies the first-frame choice: the boxes are needed only to seed the tracker, and the objects present in a 15-second household clip rarely change. This justification is inferred from the prompt's wording ("this egocentric image"), not author-stated.

**Instruction.** Identify up to 10 task-relevant objects; give each a 2D box `bbox_2d: [x1, y1, x2, y2]` normalized to 0 to 1000; enumerate "EVERY possible variation", including "10+ solid colors" per object. Answer as free-form reasoning inside `<think>` tags followed by JSON inside `<answer>` tags.

**Schema.** Five top-level blocks.

- `location`: room type, setting, time of day, lighting, room style.
- `task`: name, description, phase, action primitive, difficulty, typical duration.
- `key_objects[]`: rank, name, box, `is_primary`, `role_in_task`, `current_appearance` (color description, rgb, hex, material, texture, condition, size estimate), `current_state` (position on surface, height, orientation, interaction state, task phase), `variations` along seven dimensions (color_and_appearance, material_and_texture, size_and_shape, state_and_position, condition, interaction, brand_and_style), and `robustness_gaps` (what_robot_must_handle, common_failure_modes, edge_cases).
- `scene_variations`: seven dimensions (lighting, camera viewpoint, room style and culture, time of day, background clutter, person characteristics, task sequence variations).
- `dataset_gaps`: what the clip shows, what is missing, highest-priority variations.

Two fields matter downstream. `role_in_task` is what conditions the proposed variations on the task. `robustness_gaps.common_failure_modes` lists action-level changes (the bucket slipping, tipping over) that are routed away from the appearance renderer (Section 7).

**Output counts and time.**

| Quantity | Value | Status |
|---|---|---|
| Objects detected, running example | 5 (white wall, bucket, crumpled paper, hand, white surface) | Confirmed |
| Raw variation proposals per clip | "100+" | Deck only; exact count never supplied (Open) |
| Variations surviving the filter, per clip | 72 on average | Confirmed (deck said "about 70") |
| Reasoning time per clip (boxes, ontology, proposals) | 129.5 s | Confirmed, A100 80 GB |
| Clips reasoned over | all 116 | Confirmed |

**Known errors.** For the running example the ontology named the task "Disposing of crumpled paper into a bucket" when the clip shows wiping, and listed "Bucket cannot be opened" as a failure mode for an open bucket. The filter stage exists to catch such entries, but its precision has not been measured, so the 72-of-100-plus survival rate is a count, not an accuracy. Draft 1's Discussion phrases the ontology as "a strong proposal generator with an unmeasured error rate".

---

## 5. Stage 2: Guidance (ontology to prompt, mask and control maps)

### 5a. Plausibility filter and prompt writer

**Model.** GPT-4o mini, two instructions (draft 1 Appendices B and C; the second is `prompt-for-cosmos-transfer.txt`).

**Filter.** The full ontology JSON is passed with an instruction to reject any variation that fails one of six checks: material against the task's contact forces; object size against the scene; material against the environment type; physical possibility; lighting against time of day and room; and whether the object could plausibly be in such a scene. Rejected variations are dropped silently; each accepted one carries a one-line `plausibility_rationale`. The instruction also asks the model to prioritize variations that cover the ontology's robustness gaps. Output entries are structured per the Cosmos 3 caption schema, not plain text. Acceptance averages 72 per clip; the rejection rate cannot be stated without the raw count.

**Prompt writer.** For one accepted variation the second instruction writes the Cosmos Transfer prompt under seven rules: describe the changed object in detail (color, material, texture, finish); state explicitly that all other objects retain their original appearance; describe lighting and camera as in the original; repeat the target color or material two to three times in different contexts; stay under 300 words; never use "transform" or "change", describe the scene as if it already looks that way; be specific about materials ("smooth matte blue finish", not "blue").

Drafts 1 and 3 compress these into three rules found by trial on the bucket clip, each with its reason.

1. Repeat the target attribute and name the material, against a model that otherwise under-commits to the change.
2. Name every object that must stay unchanged, against a model that otherwise over-applies it. The leakage measurement (Section 8) tests how well this rule holds, and the answer is only partly.
3. Describe the result as a scene, not as an edit, because Transfer's text conditioning is a caption of the output video, not an instruction.

**Prompts recovered.** Six Transfer prompts (bucket to blue countertop; shelf to blue desk and shelf; shelf to white desk with oak shelf; pillow to cobalt blanket; pillow to chunky cream knit blanket; bed to navy rug) and two Predict2 prompts (cable wrapping; paper rotation), all reproduced in draft 1 Appendix D. The bucket prompt names the blue countertop four times and names the bucket, paper towels, walls, cabinets and lighting as preserved. GPT-4o mini for all 116 clips cost about 0.12 USD (Deck only; no token counts exist).

### 5b. Mask construction

**Problem.** The surface to recolor overlaps the objects that must not change: the bucket, the paper towels and the hand all sit on the countertop. A box or a single surface mask would include them.

**Segmenter.** SAM2 in video mode. It takes the boxes the reasoning stage already produced (converted from the 0 to 1000 range to pixels) and returns a mask per box, propagated across frames. Outputs were saved as `seg_mask.mp4` and `seg_overlay.mp4`. The deck's "no extra tools needed" (slide 11) is true of the detector, not of the segmenter.

**Subtraction.** With S(b, V) the tracked mask for box b over clip V, the final mask per frame t is

```
M_t = S(b_surf, V)_t  minus  union over k of S(b_k, V)_t
```

the surface mask (which includes whatever lies on the surface) minus the union of the object masks. Because the subtraction is computed on SAM2's propagated masks, M is temporally consistent without a separate tracker. The four-panel strip on slide 11 (original frame; surface mask; union of bucket, paper and hand masks; final mask) is the figure for this step in every draft.

**What the mask is and is not.** M enters Transfer only as the segmentation control video. It is a soft control: the model follows it to the degree set by the seg weight, and nothing in the pipeline forbids change outside M. There is no inpainting step, no region weight map and no compositing of source pixels back outside M. The deck's "painter's tape" and "exactly which pixels the model can change" (slide 10) overstate it, and the drafts say so. This fact decides how leakage is framed: as the expected behavior of a soft control, with a hard constraint named as the missing piece.

**Mask coverage.**

| Clip | Mean mask coverage (fraction of frame) | Status |
|---|---|---|
| Bucket (counter wiping) | 0.498 | Measured from `video-counter-blue-control-seg.mp4` |
| Shelf (exported `seg_mask_shelf_clip.mp4`) | 0.001 mean, 0.006 max | Measured; effectively empty |
| Pillow (exported `seg_mask_pillow.mp4`) | 0.025 mean, 0.039 max | Measured; effectively empty |

Whether the shelf and pillow exports are the masks Transfer received is Open (assumption A7). If they are, SAM2 propagation collapsed on those clips, the seg control carried no information, and the whole-frame recoloring on slides 14 and 16 is explained directly. Either way the drafts draw one methodological conclusion: a pipeline that depends on a tracked mask needs a coverage check before rendering, and ours did not have one.

### 5c. Control maps and weights

**Four control branches**, named in Cosmos Transfer's own terms (the deck says "Color" for vis and "Mask" for seg; slide 6 and slide 10 disagree on the count, and the paper uses four).

| Branch | Derived from | What it protects | Source of the map |
|---|---|---|---|
| edge | Canny edges of the source | object outlines, so the bucket stays a bucket | Transfer's packaged preprocessor |
| depth | monocular depth of the source | layout, what is in front and behind | Transfer's packaged preprocessor (specific depth model not named; drafts cite Depth Anything as the packaged default, Inferred) |
| vis | heavily blurred RGB of the source | global palette and lighting | Transfer's packaged preprocessor |
| seg | the subtraction mask M | where to paint | SAM2 plus subtraction (Section 5b) |

Control-map preprocessing takes about 2 min per clip.

**Weights.** The one set of hyperparameters tuned. Values as passed to the model (raw) sum to 0.9; Shrey's PDF reported them normalized to 1.

| Branch | Raw weight | Normalized | Failure when too low | Failure when too high |
|---|---|---|---|---|
| edge | 0.5 | 0.556 | objects lose coherent shape | nothing changes |
| depth | 0.2 | 0.222 | layout drifts | scene flattens to a plane |
| vis | 0.025 | 0.028 | none observed | recolor reverts to source appearance |
| seg | 0.175 | 0.194 | edits unlocalized | over-constrained |

**How they were tuned.** Not a grid search. Each weight was moved until a failure appeared and backed off, on the bucket clip, then checked on three other clips, all from one home. Edge and depth were pinned by failures on both sides; the only free choice was how to split the remaining budget between vis and seg. Vis stays near zero because the vis branch conditions on the source colors and directly opposes any recolor; this is the most useful practical finding in the deck (slide 11) and each draft explains it. The "too low" entries for depth and seg are the drafts' reading of the failure logic, not author-stated observations; only the edge lower bound, the depth upper bound and the vis upper bound are Confirmed.

**Guidance scale.** 4 throughout. At 2 and 3 the model often ignored the variation or applied it weakly; above 5 it followed the prompt and lost the room. No setting was found that recolored the target fully and left the protected region unchanged.

---

## 6. Stage 3: Generation (appearance variants)

**Model.** Cosmos Transfer 2.5, video-to-video, conditioned on the source clip, the prompt, the four control videos and their weights.

| Setting | Value | Status |
|---|---|---|
| Denoising steps | 35 | Confirmed |
| Time per step | 30.98 s | Confirmed |
| Sampling time | 18 min 4 s | Confirmed |
| Wall-clock per clip (with preprocessing) | about 20 min | Confirmed |
| Guidance scale | 4 | Confirmed |
| Seeds | not fixed; a repeated render is not bitwise reproducible | Confirmed |
| Output | 60 frames, 854 x 480, 4 fps, matching the input | Measured; Shrey cut outputs to 60 frames before saving |
| Hardware | one A100 80 GB, Google Colab Pro+ | Confirmed |
| NVIDIA reference timing | about 7.5 min on H100 NVL for 93 frames (base); about 1 min distilled edge | Background, not run by us |

Transfer preserves the source motion by construction: the output has the same hand pose, object geometry and camera path as the input, which is what makes the variant a training example for the same action.

---

## 7. Action-level branch (Cosmos Predict2)

Entries in `robustness_gaps` and `state_and_position` are changes of what happens, not of how it looks, and Transfer cannot produce them. For these we tried Cosmos Predict2 2B Video2World, which forecasts frames from a conditioning clip and a text description of what happens next.

| Setting | Value | Status |
|---|---|---|
| Denoising steps | 35 at 5.97 s per step | Confirmed |
| Wall-clock per clip | about 3.5 min | Confirmed |
| Output | 93 frames, 848 x 480, 16 fps (5.8 s) | Measured |
| Seed | abs(hash(prompt_id)) mod 2^32 | Confirmed |
| Runs | 2: cable wrapping; sheet of paper rotating 90 degrees with three objects staying on it | Confirmed |
| Outcome | no visible motion of the cable or the paper in either; the forecast reproduces the conditioning scene | Measured from first and last frames |

Both prompts are deliberately specific about what moves, what stays fixed and how the moving part stays attached; the cable prompt even points the model at the input frames as the reference motion. Predict2 was not fine-tuned. The drafts read the outcome as the model holding the scene stable, a form of success for a world model, without performing the action, the only thing asked of it.

---

## 8. Evaluation methodology

**What was evaluated and how.** Evaluation is by inspection of matched source and variant frames, and by one quantitative measurement. There is no policy training, no held-out task success, no rater study and no baseline. The deck's own notes say "everything is qualitative" (slide 18); the measurement below was added during the write-up.

**Inspection protocol.** For each shown render, list what the prompt asked to change, what it asked to preserve, and what changed. For the running example: intended, countertop to blue; preserved as intended, hand pose, bucket geometry, motion; changed although named as preserved, towels (white to blue cloth), bucket (white to grey-blue), wall (white to beige), hand skin tone lighter, a ceiling light fixture that was never in the source, the bucket label. Draft 1 Section 5.2 and draft 3 Section 4.1 do this for four clips, spanning the single-surface success, the multi-texture failure (cobalt blanket prompt recolored nearly every surface), color spreading onto adjacent objects (blue desk), and shape collapse (navy rug prompt: smeared surfaces, warped hand).

**Masked color-difference (leakage) metric.** Script: `paper/scripts/leakage_metric.py`. Inputs: the original clip, the generated clip and the tracked SAM2 mask video, all 854 x 480, 60 frames, 4 fps.

1. Convert each matched frame pair to CIELAB.
2. Compute per-pixel CIE76 ΔE between original and generated.
3. Split pixels by the tracked mask M: inside is the target the prompt asked to change; outside is the region it asked to preserve.
4. Report mean ΔE inside and outside over all pixels and frames, the standard deviation of per-frame means, the chroma-only distance (a and b channels, to separate color shift from exposure), and the fraction of protected pixels with ΔE above 10 and above 20. A ΔE of about 2 is just noticeable; 10 is an obvious change.
5. Save per-frame CSV, summary, a per-frame plot, and ΔE heatmaps with the mask contour at frames 0, 30 and 59.

**Result for the bucket clip** (the only render with a usable tracked mask).

| Quantity | Target (inside M) | Protected (outside M) |
|---|---|---|
| Mask coverage | 0.50 | 0.50 |
| Mean ΔE | 75.5 | 34.8 |
| Std of per-frame mean ΔE | 4.0 | 7.2 |
| Mean chroma-only ΔE | 68.2 | 24.2 |
| Protected pixels with ΔE above 10 | | 94.5 percent |
| Protected pixels with ΔE above 20 | | 65.3 percent |
| Ratio outside to inside | | 0.46 |

Reading: the recolor worked (target moved by 75), the protected region moved by almost half as much, nearly every protected pixel changed visibly, and the chroma-only figures show the change is color rather than exposure. The seg control and the prompt's preservation clause were the two soft containment mechanisms, and neither was sufficient. Caveats recorded in `review/leakage/README.md`: one clip; SAM2 border errors inflate the outside figure slightly relative to a 35-unit mean; CIE76 rather than CIEDE2000, which would compress large differences without changing the conclusion.

**Why one clip.** The shelf and pillow masks on hand are nearly empty (Section 5b), so the inside/outside split is meaningless for them; the pillow original and generated videos are not in the workspace either.

**Control-weight sensitivity.** Reported as the bounds table in Section 5c, from a manual sweep on one clip, not as a table of outputs per setting. The deck review suggested a small sweep figure (one output frame per setting); none exists.

---

## 9. What was actually run

| Quantity | Value | Status |
|---|---|---|
| Clips through reasoning | 116 | Confirmed |
| Transfer renders produced | 64, over 10 source clips (about 6.4 per clip) | Confirmed |
| Predict2 renders produced | 2 | Confirmed |
| Renders shown in the deck | 5 Transfer (bucket, pillow, shelf blue, bed rug, plus the slide 6 duplicate of bucket) and 2 Predict2 | Confirmed |
| Which of the 64 renders the figures are | by inference only | Open |
| GPU time for the 64 renders | about 21 A100-hours | Projection (64 x 20 min) |
| Reasoning time for 116 clips | about 4.2 h | Projection |
| Full projection | 116 x 72 = 8,352 variants, about 2,800 A100-hours | Projection; the deck's 8,120 used 70 |
| Policy trained on the output | none | Confirmed |
| Domain-randomization baseline | none | Confirmed |

The multiplier the numbers support is in diversity, not in cost per hour: one 15 s clip becomes 18 min of candidate video (72 x 15 s) and one 10 min recording about 4 h, with no new room, while a synthetic hour costs about 80 A100-hours at our settings (`draft-4-skyler/introduction.md`, notes). "Thousands of clips" (slides 2, 19) is a projection and no draft states it as output.

---

## 10. Notation used in the Method sections (drafts 1 and 3)

Introduced once, in one place, and reused in the equations and tables. Draft 4 should keep it.

| Symbol | Meaning |
|---|---|
| V = {I_t}, t = 1..T | a clip; T = 60 at 4 fps, 854 x 480 |
| R | reasoning model; O = R(I_1) is the ontology from the first frame |
| O | ontology: task record, objects {o_k} with boxes b_k in [0, 1000]^4, candidate variations U_k per object |
| u in U_k | one variation, a short phrase such as "solid blue matte" |
| L | prompt writer; p = L(O, u) is the prompt |
| S | segmenter; S(b, V) is a tracked binary mask over T x H x W |
| M | the subtraction mask, Eq. 1 (Section 5b) |
| c_edge, c_depth, c_vis, c_seg | the four control videos; c_seg = M |
| w | the control weights (Section 5c) |
| G | the renderer; V' = G(V, p, {c_j}, w) is the variant |

---

## 11. What the methodology supports, and what it does not

Supported at the strength of the evidence (from the deck review B3 and the drafts).

1. A chain of a scene-reasoning VLM, an LLM filter and prompt writer, and a multi-control video-to-video model produces appearance variations of egocentric manipulation clips while preserving hand pose, object geometry and motion (slides 4 and 13; the bucket render).
2. Masked multi-control conditioning as configured does not confine the edit to the target: color leaks into the protected region in every shown example, and in the one measured example the protected region moves by a mean ΔE of 35 against 75 for the target.
3. Vis weight must be near zero for any recolor; edge weight is bounded on both sides within a narrow band; guidance scale 4 is the usable value between under-application and loss of realism.
4. The ontology yields a large candidate set at negligible LLM cost: 72 admissible variations per clip, about 0.12 USD for all 116 clips.
5. Action-level variation through Predict2, without fine-tuning, produced no motion in both attempts.

Not supported, and no draft claims it.

- That reasoning beats random augmentation (no baseline).
- That the output is ready to train a robot, or improves policy generalization (no policy trained). Draft 1's Discussion reads the leakage result the other way: today's variants would teach a policy that counters, towels and buckets change color together.
- That thousands of clips were generated (64 were).
- That the pipeline is fully automatic (the control weights were tuned by hand; the only manual decision in the loop proper is which variation to render).

---

## 12. Named next steps that follow from the method

These are the fixes the drafts name, each tied to a specific cause.

- **Containment.** The mask is a soft control. Two remedies: spatiotemporal control-weight maps as supported in Transfer 1, or compositing source pixels back outside M after rendering. The bucket-clip leakage table is the baseline against which either is judged.
- **Mask coverage check** before rendering, given the near-empty shelf and pillow masks.
- **Domain-randomization baseline** at the prompt level: same target, same controls, color and material drawn at random, raters judge plausibility against the ontology-driven variant. Cheap relative to the renders already done.
- **Filter precision** measured on a sample of ontologies, so the 72 becomes an accuracy as well as a count.
- **Policy training** on the variants with held-out success as the metric. This is the experiment that decides whether the pipeline is useful.
- **Action generation**: fine-tune Predict2 on real manipulation video with low-rank adapters; longer term, Cosmos 3's generation tower once it supports video-to-video.
- **Distilled Transfer** timing (about 1 min per clip on H100 per NVIDIA docs), which would move the cost per synthetic hour into the range of human collection.

---

## 13. Open items that affect how the method is written

From `technical-details.md` Section 14 and `review/assumptions.md`.

1. Total footage duration (31:44 stated versus 29:00 by arithmetic). Drafts say "about 30 minutes".
2. Exact raw proposal count per clip before filtering, so a rejection rate can be stated.
3. Whether the exported shelf and pillow masks are the ones Transfer received (A7). Decides whether the multi-texture failure is a propagation failure or a containment failure.
4. Which depth estimator Transfer's preprocessor used. Drafts cite Depth Anything as the packaged default; this is inferred.
5. Cosmos 3 Nano parameter count against the Cosmos 3 technical report.
6. Which of the 64 renders correspond to the figures.
7. Full list of tasks across the 8 recordings.
8. Any code or data release.

---

## 14. How the methodology has been described across drafts

| | Draft 1 (`paper/`) | Draft 2 (`paper2/`) | Draft 3 (`paper3/`) |
|---|---|---|---|
| Method structure | Notation; Reasoning; Guidance (prompt and filter, mask, control maps); Generation; Routing action-level variations | Follows the slide order (slides 6 to 11) | Draft 1's stages in draft 2's order: pipeline figure first, then reasoning, prompts, guidance, generation |
| Pipeline figure | TikZ block diagram, three rows (reasoning; mask and prompt; controls and generation) | Slide 6 image | TikZ "what goes in, what comes out" redrawn from slide 6 with deck thumbnails |
| Equation | Eq. 1, the subtraction mask | none | Eq. 1 |
| Tables | weights with failure bounds; per-clip cost; leakage | none | weights with failure bounds; leakage |
| Numbers | corrected (Shrey's answers) | the deck's own | corrected |
| Appendices | ontology prompt, filter instruction, prompt-writer instruction, all eight prompts | none | none |

Skyler's verdict (2026-10-16): draft 1 had the structure but read "highfalutin"; draft 2 was faithful to the talk but "more like a guide"; draft 3 was the requested merge. For draft 4 the Method section should keep the plain register of the talk (running bucket example, three stages, four maps), the notation, Eq. 1, the weights table with its failure bounds, and the slide 10 and slide 11 figures, and cut prose before cutting any of those.

---

## Notes for discussion

- The methodology has three stages in every draft (reasoning, guidance, generation) plus a side branch for action-level variation and a measurement section. The deck's Part 1 / Part 2 split (slides 7 and 10) maps onto reasoning and guidance; generation has no slide of its own beyond slide 6. Draft 4 can keep three stages or fold generation into guidance; three is the talk's structure and reads cleanly.
- The mask story is the methodological spine of the paper: it is built from the ontology's boxes (one decision, used twice), it is a soft control (which explains the leakage), and the retained masks for two clips are nearly empty (which may explain the multi-texture failures). All three facts belong in the Method, not only in the Discussion.
- "Only manual decision is which variation to render" (slide 6) is true of the per-clip loop and false of the setup, since the weights were hand-tuned on one clip. Draft 3's wording ("the one set of hyperparameters we tuned") handles this; keep it.
- The two Predict2 prompts are the only place the pipeline was asked to change what happens rather than how it looks. Whether that branch belongs in the Method or only in the Results is a framing choice; drafts 1 and 3 give it one short Method subsection and report the outcome under Results, which keeps the "two kinds of variation" idea visible.
- The "72 admissible variations" figure is a count of filter output, not of renders and not of verified-plausible variations. Every sentence that uses it should say "admissible" or "proposed", never "generated".
- If the Method section for draft 4 is next, this file is the source; the section variants should differ in order and register, not in facts.

---

## 15. Skyler's pipeline paragraph, revised (2026-10-17)

Skyler's draft of the Fig. 1 paragraph, with the questions in it answered and the facts aligned to Sections 3 to 6 above.

### Answers and corrections

- **Why Cosmos Curate.** It split the 8 raw recordings into clips at shot boundaries with the TransNetV2 detector it packages. Clips were then trimmed to at most 15 s and downsampled to 4 fps at 854 x 480, the input format Cosmos Transfer consumes, giving 116 clips. Curate did not capture or caption anything.
- **"Cosmos Reason"** was the deck's label; the model that ran was the reasoning tower of Cosmos 3 Nano.
- **VLA** should be **VLM**. The reasoner outputs JSON, not robot actions.
- **Reasoning runs on the first frame**, not the whole clip.
- **GPT-4o mini does two jobs**: filter against six plausibility checks, then write the prompt for one accepted variation.
- **The four maps are edge, depth, vis and seg.** Vis is the blurred color map. There is no texture control. The mask is the fourth map, not a separate fifth input.
- **SAM2**, video mode, seeded by the ontology's boxes. The mask marks the surface to repaint; the objects on it are subtracted out. Object shape is preserved by edge and depth, not by the mask, and the mask is a soft control.
- **"Visual entropy"** is undefined in the paper. Use "appearance diversity".
- Spelling and register: "we're" becomes "we"; "Egocentric" lower case; "Fig. 1" for LNCS.

### Revised paragraph

Fig. 1 shows the pipeline. Its input is an egocentric clip V and its output is a variant V' in which the recorded task and hand motion are unchanged and the appearance of one or more scene elements is altered. The eight source recordings were first split into clips with Cosmos Curate, which applies TransNetV2 shot-boundary detection; each clip was trimmed to at most 15 s and downsampled to 4 fps at 854 x 480, the input format Cosmos Transfer expects, giving 116 clips. The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano, a vision-language model, which returns an ontology: a structured description of the task, the task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations each could plausibly take while the task stays the same. GPT-4o mini filters the proposed variations against six plausibility checks and, for one accepted variation, writes the text prompt for Cosmos Transfer. Four control videos derived from the source clip guide the renderer: Canny edges preserve object outlines, monocular depth preserves the spatial layout, a blurred copy of the source (the vis control) preserves global color and lighting, and a segmentation video marks the surface to repaint. The segmentation video comes from SAM2, which converts the ontology's boxes into masks tracked across the clip; subtracting the masks of the objects on the surface from the mask of the surface itself leaves only the region to change (Eq. 1). Cosmos Transfer 2.5 renders V' under these controls and the prompt. Because every control is derived from the source, the variant keeps the task, the actions and the inventory of objects, and differs only in the attributes the ontology permits, so one recording yields many appearance variants of the same demonstration.

(238 words)

Note: "differs only in the attributes the ontology permits" states the design. The leakage table in Results shows it does not hold in practice; the Method can state the intent and let Results qualify it, as drafts 1 and 3 do.

### Why clips, 15 s, 4 fps, 854 x 480, and TransNetV2 (Skyler's question, 2026-10-17)

Shrey gave no rationale; the following is inference consistent with the confirmed numbers, and is marked as such.

- **Clips.** Transfer and Predict2 generate a fixed frame window per pass (the NVIDIA reference timing is for 93 frames; Predict2 output measures 93 frames). A 10 min recording must be cut into pieces that fit one pass. The first-frame ontology and the once-seeded SAM2 mask also assume one continuous action with a stable object set per clip.
- **4 fps.** At 24 to 30 fps a 93-frame window is 3 to 4 s, shorter than a wiping or folding action. At 4 fps it covers 23 s, so a 15 s action (60 frames) fits in one pass. Shrey trimming outputs to 60 frames is consistent with the model producing more frames than the input. Chunked generation at full frame rate would multiply the 20 min render and compound drift. Inferred.
- **854 x 480.** Compute: 31 s per denoising step on an A100 80 GB at this size. Predict2's 848 x 480 is the same 480p rounded to a multiple of 16. Inferred.
- **TransNetV2.** The shot-boundary detector packaged in Cosmos Curate, NVIDIA's front end for preparing video for Cosmos (splitting, transcoding, filtering). It guarantees no cut inside a clip, which per-clip conditioning needs. Confirmed as the tool; the transcoding step's attribution to Curate is inferred.
- **4 fps for policy data.** RT-1 ran at 3 Hz and many Open X-Embodiment datasets are 3 to 10 Hz, so 4 fps is within the range policies train at. Name it in Limitations anyway: contact events are undersampled.

Questions for Shrey raised by the arithmetic (80 min raw, at most 29 min retained, about 41 s of footage per clip before trimming):

1. A continuous handheld recording has no editorial cuts. Were the recordings made in segments, or did TransNetV2 fire on fast head turns and occlusions?
2. About 50 of the 80 minutes were dropped. Was that the 15 s trim, a Curate filter, or manual selection?

Suggested Method sentence: "Each recording was split at shot boundaries with TransNetV2 as packaged in Cosmos Curate, and each clip was trimmed to at most 15 s and downsampled to 4 fps at 854 x 480, so that a complete manipulation action fits within the fixed frame window that Cosmos Transfer generates in a single pass [VERIFY: Shrey, frame window and reason for 4 fps]."

---

## 16. Reasoning subsection, fleshed out from slide 7 (2026-10-17)

Skyler's source was the slide 7 bullet list. Corrections before the prose:

- "Cosmos Reason" was the deck label; the reasoner that ran was the Cosmos 3 Nano reasoning tower.
- "70 plausible variants" is 72 (Shrey, confirmed). "100+ raw proposals" was never measured; mark it.
- "Proposes only physically grounded variations" contradicts a filter that rejects about a third. Say: proposes variations conditioned on the object's role; a second model filters.
- "The model must learn" should name the policy, or a reader takes it to mean the reasoner.
- Reasoning runs on the first frame, not the clip.

### A. Argument first, then mechanism (about 560 words)

**Reasoning with structured ontologies.** A policy trained on the counter-wiping clip must learn more than what a bucket looks like. It must learn what the bucket is for in this task, that it is held and positioned rather than resting on a shelf, and which of its properties the task depends on. Domain randomization [tobin2017] varies appearance without that information: it draws colors and textures at random for every surface, so a cleaning bucket may receive a texture no bucket has, and the policy spends capacity learning to ignore variation that never occurs. We instead ask a model to understand the scene before anything is varied, so that the variations proposed for an object are the ones it could plausibly take while the task stays the same.

The reasoning tower of Cosmos 3 Nano [cosmos3] receives the first frame of the clip and a fixed instruction, and returns a JSON record we call the ontology (Fig. X). The instruction asks for up to ten task-relevant objects, each with a 2D bounding box, and for every object the model fills a fixed schema: its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with the hand), candidate variations along seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style), and a robustness block listing what a robot would have to handle and how the object could cause a failure. A parallel block records scene-level variations (lighting, viewpoint, room style, time of day, clutter), and a final block states what training on this clip alone would miss.

Three properties of this output carry the rest of the pipeline. The role field is what grounds the variations: a bucket recorded as a container for waste in a cleaning task is offered label designs, sizes and materials that bear scrubbing, not the contents a planter would have. The bounding boxes seed the segmenter (Sec. X), so the model that decides what may change also locates it, and no separate detector is run. The failure-mode list separates appearance variations, which a video-to-video renderer can produce while keeping the recorded motion, from action-level variations such as the bucket tipping over, which go to a video-prediction model (Sec. X). Because the output is a fixed schema rather than free text, each proposal can be inspected, counted and rejected on its own, which is what the filter stage requires.

We read the first frame rather than the clip because the boxes are needed only to initialize tracking, and the objects in a 15 s household clip rarely change. Reasoning takes about 130 s per clip on one A100. The exhaustiveness of the instruction, every dimension and at least ten solid colors per object, is deliberate: the model is asked to over-propose, and a second stage removes what fails a plausibility check. Across the 116 clips, 72 variations per clip on average survive that filter [VERIFY: raw proposal count; the deck says 100+]. The ontology is not free of errors. For the running example it named the task "disposing of crumpled paper into a bucket" when the clip shows wiping, and listed "bucket cannot be opened" as a failure mode for an open bucket (Fig. X). The filter exists to catch entries of this kind, but its precision has not been measured, so 72 is a count of admitted proposals, not a verified accuracy.

### B. Mechanism first, compact (about 260 words)

**Reasoning with structured ontologies.** The reasoning tower of Cosmos 3 Nano [cosmos3] receives the first frame of each clip and a fixed instruction and returns the ontology, a JSON record of the scene (Fig. X): the task and its action primitive; up to ten task-relevant objects, each with a bounding box, a role in the task, its current appearance and state, and candidate variations along seven dimensions from color and material to size, condition and brand; scene-level variations such as lighting, viewpoint and clutter; and a list of ways each object could cause the task to fail. The role field is the reason for this stage. Domain randomization [tobin2017] draws colors and textures with no notion of the task, so a cleaning bucket may receive a texture no bucket has; here the bucket is recorded as a waste container in a cleaning task, and the variations offered for it are the ones a cleaning bucket could plausibly take. The boxes seed the segmenter (Sec. X), the failure modes mark action-level variations for a different renderer (Sec. X), and the fixed schema lets each proposal be counted and rejected on its own by the filter that follows. The instruction asks the model to over-propose, every dimension and at least ten colors per object, and reasoning on the first frame takes about 130 s per clip on one A100; 72 variations per clip on average survive the plausibility filter [VERIFY: raw count; deck says 100+]. The ontology has errors, for instance a wrong task name and an impossible failure mode for the running example (Fig. X), and the filter's precision is unmeasured, so 72 is a count, not an accuracy.

### Notes

- A makes the domain-randomization contrast as an argument, which is all the evidence allows; if the subsection runs long, cut the first paragraph to two sentences and leave the contrast to Related Work.
- The "what a robot would have to handle" block is the one schema field no draft uses downstream; it can be dropped from the list.
- "Fig. X" is the slide 8 detection image plus the JSON excerpt (draft 3 Fig. 2); "Sec. X" are the mask and Predict2 subsections.

---

## 17. Why GPT-4o mini (Skyler's question, 2026-10-17)

No author-stated rationale exists; the deck names the model and the cost only.

**Role.** Two text-to-text jobs downstream of the ontology: filter the proposals against the six plausibility checks, then write the Transfer prompt for one accepted variation. Inputs are JSON from Cosmos 3 Nano; no vision is needed.

**Why a second model at all.** The reasoner is instructed to over-propose, so something must prune. A separate model with a separate instruction checks the first model's output rather than continuing it. The prompt writer also carries Transfer's prompting conventions (caption, not instruction; repetition; naming what stays fixed), which fit a short system instruction better than the reasoner's schema prompt. This is methodological and can be stated in the paper.

**Why this LLM.** Inferred: cost (about 0.12 USD for 116 clips, Deck only), speed and keeping the A100 free for rendering, reliable JSON-schema output. No comparison appears to have been run.

**Reviewer risk.** The one closed component sits at the step that decides plausibility. Mitigate by pinning the version [VERIFY: snapshot used], publishing both instructions (draft 1 App. B and C), and saying in Limitations that any instruction-following LLM could replace it and that its filter precision is unmeasured.

**Suggested sentence.** "GPT-4o mini [gpt4omini] performs the two text-only steps, filtering the proposed variations and writing the Transfer prompt; we chose it for cost (about 0.12 USD across all 116 clips) and for reliable schema-conformant output, and did not compare alternatives [VERIFY: Shrey, model version and reason for choice]."

**Ask Shrey.** Was any other LLM tried, and which 4o mini snapshot ran?

---

## 18. The three prompt-writing rules, with reasons (Skyler's question, 2026-10-17)

Heuristics found by trial on the bucket clip, not ablated. Present them as practice with a reason attached, not as results.

**1. Repeat the target attribute.** Text conditioning enters through cross-attention over prompt tokens; one mention of "blue" competes with a 150-word caption. Repetition in different contexts puts more attention mass on the one property that must change. The pull it works against is the vis control, which conditions on source colors even at weight 0.025. Repetition made the recolor commit without raising guidance above 4. The bucket prompt names blue four times; the instruction says two to three; the deck says "3x". Write "two to three times".

**2. Name what must stay unchanged.** Without the clause the caption says nothing about the bucket or towels, so the model may restyle them to match. With it, the caption asserts they are the source objects. It is a request, not a constraint: on the bucket clip the protected region still moved by a mean ΔE of 35 against 75 for the target, with 95 percent of protected pixels changing visibly. "Protects non-target objects" overstates; "reduces but does not prevent change" is what was measured.

**3. Describe the result, not the change (the [why?]).** Transfer was trained on video paired with captions of what the video shows, not on edit instructions with before-and-after pairs (the InstructPix2Pix formulation). "Change the white countertop to blue" is out of distribution twice: the verb has no counterpart in a caption, and the prompt names two colors where one should appear. "A person cleaning a solid blue countertop" is caption-shaped and names only the target. The source clip supplies the "before"; the prompt describes only the "after". Rule 6 of the prompt-writer instruction encodes this.

### Prose for the Method

Three prompt-writing rules were found by trial on the counter-wiping clip and are encoded in the GPT-4o mini instruction. First, the target attribute is stated two to three times in different phrasings and tied to a material ("a smooth matte blue finish"), because a single mention competes with the rest of the caption for the model's attention and the vis control, even at its small weight, biases the render toward the source colors. Second, every object that must stay unchanged is named with the clause "retain their original appearance", and the lighting and camera are described as in the source; without this the caption says nothing about the bucket or the towels and the model is free to restyle them. Third, the prompt describes the scene as it should appear, not the edit that produces it. Transfer's text conditioning was trained on captions of videos, not on edit instructions, so "change the white countertop to blue" is out of distribution and names two colors where only one should appear, whereas "a person cleaning a solid blue countertop" is a caption the model has seen the like of and mentions only the target color. The source clip supplies the "before"; the prompt should describe only the "after". These rules are heuristics, not ablated results. Sec. X measures how far the second one holds and finds the answer is only partly.

### Notes

- All three rules live in the prompt-writer instruction (draft 1 App. C), so they apply to every prompt automatically; the bucket prompt (App. D) is the worked example a reader can check against them.
- The caption-versus-instruction argument for rule 3 is reasoning about how Transfer was trained, not something Shrey tested. If a reviewer wants evidence, the natural check is one render with the instruction-phrased prompt; it has not been run.

---

## 19. Section 3.3, Guiding the renderer, rewritten (Skyler's draft, 2026-10-17)

Corrections to the draft bullets:

- "Default weights": NVIDIA's defaults were not used. The four weights are the one tuned hyperparameter set; report them as ours with the failure bounds.
- Canny was not chosen over Sobel by us. It is the preprocessor Transfer ships and the edge branch was trained on Canny maps; another detector would be out of distribution. Background if asked: Sobel gives thick, graded gradient magnitude at every pixel; Canny applies non-maximum suppression and hysteresis thresholds to give thin, connected contours and suppress texture, which is what an outline control wants.
- "Mask describes exactly which pixels the model can change" and "without affecting the neighboring objects" claim what the leakage table disproves. The mask is a soft control.
- "Color for lightning" is lighting; "Depth is" needs completing.

### Prose

**Guiding the renderer.** Transfer receives four control videos derived from the source clip, each with a scalar weight, and the weights decide how strongly the render is held to each property of the source (Fig. X). The text prompt says what should change; the controls say what must not.

The edge control is a Canny edge video [canny1986], computed by the preprocessor packaged with Transfer, and carries the outline of every object in every frame. It is the control that keeps a bucket a bucket: when its weight falls, surfaces smear and the hand warps (Fig. X, navy-rug render), and when it rises the render reproduces the source and nothing changes. The depth control is a monocular depth video [depthanything] and carries the layout, what is in front of what and where the surface lies under the hand; too much of it flattens the scene toward a plane, too little lets the layout drift. The vis control is a heavily blurred copy of the source RGB and carries the global palette and the direction of the light, so the variant still reads as the same room under the same lamps. It is also the control that opposes the edit, because it conditions on the source colors: at any appreciable weight the countertop reverts toward white, so vis is held close to zero. The segmentation control is the subtraction mask M of Sec. X, one channel marking the surface to repaint, and tells the model where the prompt applies. It is a control signal, not a constraint; the model follows it to the degree set by its weight, and nothing in the pipeline forbids change outside it.

Table X gives the weights, which we set by moving each until a failure appeared and backing off, on the counter-wiping clip, then checked on three further clips from the same home. Edge is the dominant term and is pinned on both sides within a narrow band; depth has an upper bound; vis must be near zero; seg takes what remains. Guidance scale was 4: at 2 and 3 the model often applied the variation weakly or not at all, and above 5 it followed the prompt and lost the room.

Together the controls divide the source into what is preserved and what is free. Edges and depth fix the geometry, so the hand motion, the object shapes and the camera path survive unchanged, which is what makes the variant a demonstration of the same action. Vis, nearly off, lets the color change while keeping the light. The mask directs the change to one surface. The text prompt then fills the free part, and the quality of the variant depends on how cleanly these two sets separate; Sec. X measures where they did not.

(about 430 words)

### Table X

Control weights as passed to Transfer (raw, sum 0.9) with the normalized values Shrey reported, and the failure that bounds each.

| Control | Derived from | Protects | Raw | Normalized | Too low | Too high |
|---|---|---|---|---|---|---|
| edge | Canny edges | object outlines | 0.5 | 0.556 | objects lose shape | nothing changes |
| depth | monocular depth | layout, occlusion order | 0.2 | 0.222 | layout drifts | scene flattens |
| vis | blurred source RGB | palette and lighting | 0.025 | 0.028 | none observed | recolor reverts |
| seg | subtraction mask M | where to paint | 0.175 | 0.194 | edits unlocalized | over-constrained |

Only the edge lower bound, the depth upper bound and the vis upper bound are Shrey's observations; the other failure entries are the drafts' reading of the failure logic and could be marked VERIFY or dropped. The depth model behind the preprocessor is not named by Shrey; Depth Anything is the packaged default and is cited on that basis [VERIFY].

### Why this section matters (Skyler's question)

It is the only place in the pipeline that decides what must not change, and a variant is training data for the same action only if the hand path, the contact, the object shapes and the camera motion survive. The controls pin those to the source; the prompt fills what is left. Four reasons a reviewer reads it closely: it holds the only tuned parameters; it contains the one non-obvious finding (vis near zero because it conditions on source colors); it explains both the bucket success (edge and depth held geometry) and the failures (rug warp at the edge lower bound, leakage from a soft mask); and the seg control built from the ontology's boxes is where the reasoning stage reaches into the renderer, which is the title claim.

Candidate lead sentences for the subsection:

- "The prompt says what should change; this section is about everything that must not, which for training data is the larger half."
- "A variant is a demonstration of the same action only if the hand path, the contact and the object shapes survive the render; the four controls are how the source is held fixed so that the prompt can change nothing else."
