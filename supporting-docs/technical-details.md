# Technical details: every number behind draft 1 and draft 2

Compiled 2026-10-16. Each quantity is listed with its value, where it came from, how confident we can be in it, and where it is used. "Deck" means the AIPR presentation (`SynthethicVideoGenerationForWorldFoundationModels.pptx`, slide numbers given). "PDF" means `answers-from-shrey.pdf`. "Chat" means Shrey's two later messages (2026-10-16). "Measured" means I computed it from the media files in the workspace.

Status key: **Confirmed** (author-stated and consistent), **Measured** (derived from files here), **Projection** (arithmetic on other numbers, not an observation), **Deck only** (stated on a slide, superseded or unverified), **Open** (no reliable value).

---

## 1. Source data

| Quantity | Value | Source | Status | Notes |
|---|---|---|---|---|
| Raw recordings | 8 | PDF Q2 | Confirmed | Egocentric, handheld, one person performing household chores |
| Length per recording | about 10 min | PDF Q2 | Confirmed | So about 80 min of raw footage |
| Clipping tool | TransNetV2 (Cosmos Curate) | PDF Q2 | Confirmed | Shot-boundary detection |
| Clips after clipping | **116** | Chat (re-verified) | Confirmed | PDF said 129; Shrey called that a miscount |
| Clips on deck slide 24 | 116 | Deck | Deck only | Matches corrected value |
| Clip length | up to 15 s | PDF Q2 | Confirmed | Downsampled target |
| Frame rate after downsampling | 4 fps | PDF Q2, Measured | Confirmed | All Transfer inputs and outputs in the deck are 4 fps |
| Frames per clip | 60 | Measured, Chat Q8 | Confirmed | 15 s × 4 fps; Shrey cut outputs to 60 before saving |
| Resolution | 854 × 480 | Measured | Confirmed | Shrey's table said 848 × 480 "implied"; files measure 854 |
| Total duration stated | 31 min 44 s | PDF Q6 | Open | 116 × 15 s = 29 min 0 s, so the total cannot be right for 116 clips of at most 15 s. Drafts say "about 30 minutes" |
| "2 to 3 hours of data" | slide 1 speaker notes | Deck | Deck only | Inconsistent with every other figure; used only in draft 2 for fidelity to the talk |
| Tasks recorded | counter wiping, cloth folding on bed, bed making, cable wrapping at desk | Deck slides 3, 14, 15, 16; prompts | Confirmed | Four tasks visible in the shown clips; full task list of the 8 recordings not provided |

## 2. Models and checkpoints

| Component | Value | Source | Status |
|---|---|---|---|
| Reasoner | Cosmos 3 Nano, reasoning tower | PDF Q1 | Confirmed |
| Cosmos 3 Nano size | 16B total; 8B reasoning tower, 8B generation tower | PDF Q1 | Author-stated; one third-party source says 8B total. Not verified against the Cosmos 3 report |
| Generation tower of Cosmos 3 Nano | tried; no video-to-video support | PDF Q1 | Confirmed |
| Appearance renderer | Cosmos Transfer 2.5 | PDF Q1 | Confirmed |
| Action renderer | nvidia/Cosmos-Predict2-2B-Video2World | PDF Q1 | Confirmed |
| Segmenter | SAM2, video mode (tracked masks) | PDF Q3 | Confirmed |
| Prompt writer and filter | GPT-4o mini | Deck slide 9; Chat | Confirmed |
| Edge, depth, blur preprocessors | Cosmos Transfer packaged tools (Canny, monocular depth, blur) | Deck slide 10; inferred | Inferred; specific depth model not named |
| Deck's label for reasoner | "Cosmos Reason" (slides 5, 6, 8) | Deck | Deck only; actual model was Cosmos 3 Nano |
| Cosmos Predict sizes | 2B and 14B | Deck slide 5 | Background fact |
| Cosmos 3 Nano on A100 | "fits on the same A100 hardware" | Deck slide 18 | Deck only |

## 3. Reasoning stage (ontology and variations)

| Quantity | Value | Source | Status | Notes |
|---|---|---|---|---|
| Objects detected per frame (example) | 5 | Deck slide 8 image | Confirmed | White wall, bucket, crumpled paper, hand, white surface |
| Max objects requested | 10 | Reasoning prompt (PDF) | Confirmed | "up to 10" |
| Bounding-box coordinate range | 0 to 1000, normalized | Reasoning prompt | Confirmed | `bbox_2d: [x1, y1, x2, y2]` |
| Raw variation proposals per clip | "100+" | Deck slide 7 | Deck only | Exact count never supplied; prompt asks for "10+ solid colors" per object and exhaustive enumeration |
| Accepted variations per clip | **72** (average) | Chat Q1 | Confirmed | Deck said "~70" |
| Variation dimensions in schema | 7 per object | Reasoning prompt | Confirmed | color_and_appearance, material_and_texture, size_and_shape, state_and_position, condition, interaction, brand_and_style |
| Scene-level variation dimensions | 7 | Reasoning prompt | Confirmed | lighting, camera_viewpoint, room_style_and_culture, time_of_day, background_clutter, person_characteristics, task_sequence_variations |
| Plausibility filter checks | 6 | Chat Q2 | Confirmed | material vs task forces; object size vs scene; material vs environment; physics; lighting vs time of day; implausible object |
| Reasoning time per clip | 129.5 s (about 2.2 min) | PDF Q9 | Confirmed | Boxes + ontology + proposals, Cosmos 3 Nano on A100 |
| Reasoning input | first frame of clip | Inferred from prompt ("this egocentric image") | Inferred |
| Ontology task label for bucket clip | "Disposing of crumpled paper into a bucket" | Deck slide 8 | Confirmed | Conflicts with narrative "wiping down a table"; reported as an ontology error in draft 1 |
| Known implausible ontology entry | "Bucket cannot be opened" (open bucket) | Deck slide 8 | Confirmed | Evidence of hallucinated entries |

## 4. Prompt writing

| Quantity | Value | Source | Status |
|---|---|---|---|
| Prompt length limit | under 300 words | Prompt-writer instruction | Confirmed |
| Target attribute repetitions | 2 to 3 (deck says "3x") | Instruction; Deck slide 9 | Confirmed |
| Prompt-writer rules | 7 | Instruction (`prompt-for-cosmos-transfer.txt`) | Confirmed |
| Prompts recovered | 6 Transfer + 2 Predict2 | PDF Q7; Chat | Confirmed |
| GPT-4o mini cost, all clips | about $0.12 | Deck slide 24 | Deck only; no token counts exist (Chat Q7) |

The six Transfer prompts: bucket → blue countertop; shelf → blue desk and shelf; shelf → white desk with oak shelf; pillow → cobalt blanket; pillow → chunky cream knit blanket; bed → navy rug. The two Predict2 prompts: cable wrapping; paper rotating 90 degrees.

## 5. Guidance (control maps and mask)

| Quantity | Value | Source | Status | Notes |
|---|---|---|---|---|
| Control branches used | 4: edge, depth, vis, seg | PDF Q4; Chat | Confirmed | Deck slide 10 calls vis "Color" and seg "Mask"; slide 6 lists "Edges, Depth, Color, Seg" plus a separate subtraction mask |
| Edge weight (raw) | **0.5** | Chat Q4 (TransferWeights dataclass) | Confirmed | |
| Depth weight (raw) | **0.2** | Chat Q4 | Confirmed | |
| Vis weight (raw) | **0.025** | Chat Q4 | Confirmed | |
| Seg weight (raw) | **0.175** | Chat Q4 | Confirmed | |
| Sum of raw weights | 0.9 | Arithmetic | Measured | |
| Normalized weights | 0.556 / 0.222 / 0.028 / 0.194 | PDF Q4 | Confirmed | Equal to raw ÷ 0.9; PDF reported these |
| Edge lower-bound failure | shape collapse | PDF Q4 | Confirmed | "Pushing edge any lower caused objects to lose coherent shape" |
| Depth upper-bound failure | scene flattens to a plane | PDF Q4 | Confirmed | |
| Vis upper-bound failure | recolor reverts to source appearance | PDF Q4; Deck slide 11 | Confirmed | |
| Mask semantics | soft control via seg weight, not a hard constraint | Chat Q2 | Confirmed | Deck slide 10 says "exactly which pixels the model can change", which overstates it |
| Mask construction | surface mask minus union of object masks | Deck slide 11; PDF Q3 | Confirmed | |
| Mask tracking | SAM2 propagation across frames | PDF Q3 | Confirmed | |
| Bucket-clip mask coverage | 0.498 of frame (mean over 60 frames) | Measured | Measured | From `video-counter-blue-control-seg.mp4` |
| Shelf-clip exported mask coverage | 0.001 mean, 0.006 max | Measured | Measured | `segmentation/seg_mask_shelf_clip.mp4`; effectively empty |
| Pillow-clip exported mask coverage | 0.025 mean, 0.039 max | Measured | Measured | `segmentation/seg_mask_pillow.mp4`; effectively empty |
| Whether those were the masks fed to Transfer | unknown | — | Open | Decides whether the whole-frame recoloring on slides 14 and 16 is explained by mask collapse |

## 6. Generation settings

### Cosmos Transfer 2.5

| Quantity | Value | Source | Status |
|---|---|---|---|
| Denoising steps | 35 | Chat Q4 (progress bar) | Confirmed |
| Time per step | 30.98 s | Chat Q4 | Confirmed |
| Sampling time | 18 min 4 s | Chat Q4 | Confirmed |
| Control-map preprocessing | about 2 min | Chat Q4 | Confirmed |
| Wall-clock per clip | about 20 min | Chat Q4; PDF Q9 | Confirmed |
| Guidance scale | 4 | Chat Q4 | Confirmed |
| Guidance values tried | 2, 3 (under-applied or skipped the variation); above 5 (scene lost realism) | Chat Q5 | Confirmed |
| Output frames | 60 | Chat Q8; Measured | Confirmed (Shrey's table said 93 "implied"; he confirmed 60) |
| Output resolution | 854 × 480 | Measured | Confirmed (table said 848 × 480 "implied") |
| Output fps | 4 | Measured | Confirmed |
| Seeds | not fixed | Chat Q4 | Confirmed |
| GPU | A100 80 GB, Google Colab Pro+ | PDF Q9; Chat | Confirmed |
| NVIDIA reference timing | about 7.5 min on H100 NVL for 93 frames (base); about 1 min distilled edge | Chat Q4 (NVIDIA docs) | Background |

### Cosmos Predict2 2B Video2World

| Quantity | Value | Source | Status |
|---|---|---|---|
| Denoising steps | 35 | Chat | Confirmed |
| Time per step | 5.97 s | Chat | Confirmed |
| Wall-clock per clip | about 3.5 min | Chat; PDF Q9 | Confirmed |
| Output resolution | 848 × 480 | Chat; Measured | Confirmed |
| Output fps | 16 | Chat; Measured | Confirmed |
| Output frames | 93 (5.8 s) | Measured | Confirmed |
| Seed | abs(hash(prompt_id)) mod 2^32 | Chat | Confirmed |
| Runs | 2 (cable wrapping; paper rotation) | Deck slides 15, 16; Chat | Confirmed |
| Outcome | no visible motion of the target object in either | Visual inspection of first/last frames | Measured |

## 7. What was generated

| Quantity | Value | Source | Status |
|---|---|---|---|
| Transfer renders produced | **64** | Chat Q1 | Confirmed |
| Source clips covered by those renders | **10** | Chat Q1 | Confirmed |
| Renders per source clip | about 6.4 | Arithmetic | Projection |
| Predict2 renders | 2 | Deck; Chat | Confirmed |
| Renders shown in the deck | 5 Transfer (bucket, pillow, shelf blue, bed rug, and the slide-6 duplicate of bucket) + 2 Predict2 | Deck slides 4, 6, 13, 14, 15, 16 | Confirmed |
| GPU time for the 64 renders | about 21 A100-hours | 64 × 20 min | Projection |
| Policy trained on the output | none | Deck slide 18 notes | Confirmed ("everything is qualitative") |

## 8. Scale projection

| Quantity | Value | Source | Status |
|---|---|---|---|
| Deck projection | 8,120 = 116 × 70 | Deck slide 24 | Deck only |
| Corrected projection | 8,352 = 116 × 72 | Chat Q1 | Projection |
| GPU time for full projection | about 2,784 A100-hours (8,352 × 20 min) | Arithmetic | Projection |
| Reasoning time for all 116 clips | about 4.2 h (116 × 129.5 s) | Arithmetic | Projection |
| "Thousands of clips" (slides 2, 19) | projection, not produced | Chat Q1 | Deck only |
| "Scale to greater than 100 clips" (slide 18 to-do) | consistent with 64 produced | Deck | Confirmed |

## 9. Leakage measurement (bucket clip, computed here)

Script: `paper/scripts/leakage_metric.py`. Inputs: `review/images/video-original-bucket-cleaning.mp4`, `video-generated-counter-blue-clean.mp4`, `video-counter-blue-control-seg.mp4`. Outputs in `review/leakage/bucket/`.

| Quantity | Value | Status |
|---|---|---|
| Frames compared | 60 | Measured |
| Color space and metric | CIELAB, CIE76 ΔE per pixel | Method choice |
| Mask coverage (mean) | 0.498 | Measured |
| Mean ΔE inside mask (target) | 75.5 | Measured |
| Std of per-frame mean ΔE, inside | 4.0 | Measured |
| Mean ΔE outside mask (protected) | 34.8 | Measured |
| Std of per-frame mean ΔE, outside | 7.2 | Measured |
| Mean chroma-only ΔE (a, b), inside | 68.2 | Measured |
| Mean chroma-only ΔE (a, b), outside | 24.2 | Measured |
| Ratio outside / inside | 0.46 | Measured |
| Protected pixels with ΔE > 10 | 94.5% | Measured |
| Protected pixels with ΔE > 20 | 65.3% | Measured |
| Reference thresholds | ΔE ≈ 2 just noticeable; ΔE 10 obvious | Standard CIE76 interpretation |
| Same measurement on shelf and pillow clips | not possible | Exported masks nearly empty; pillow videos not in workspace |

Qualitative leakage observed on the bucket render (slide 4 notes and inspection): towels white → blue cloth; bucket white → grey-blue; wall white → beige; hand skin tone lighter; ceiling light fixture appears; bucket label changed. Preserved: hand pose, bucket geometry, motion.

## 10. Media inventory from the deck

| Item | Count | Notes |
|---|---|---|
| Slides | 24 | 1 to 20 main talk; 21 Innodata boilerplate; 22 to 24 backup |
| Embedded images | 25 PNG/JPEG + 1 JPEG-XR | Renamed in `review/images/`, index in `_media-index.csv` |
| Embedded videos | 8 MP4 | 6 Transfer-related (60 frames, 4 fps), 2 Predict2 (93 frames, 16 fps) |
| Deck file size | 39.0 MB | |
| Mislabeled pair found | slide 14 pillow old/new | Image files were stored in reverse order; corrected in both drafts |

## 11. Venue and format

| Quantity | Value | Source | Status |
|---|---|---|---|
| Venue | AIPR 2026, Washington, DC, Oct 12 to 13, 2026 | aipr-workshop.org | Confirmed |
| Proceedings | Springer LNCS | aipr-workshop.org | Confirmed |
| Template | llncs, splncs04 | Springer | Confirmed |
| Page limit | none | User (confirmed via organizers) | Confirmed |
| 2025 volume for reference | LNCS 16446, 41 papers, 622 pages, about 15 pages/paper | Springer, bookseller listing | Reference |
| Final paper deadline | Oct 22, 2026 | aipr-workshop.org | Confirmed |
| Required submission items | LNCS source, PDF, figure source files, signed Licence to Publish, via Springer Meteor | aipr-workshop.org | Confirmed |
| Abstract deadline (past) | Aug 11, 2026 | aipr-workshop.org | Confirmed |

## 12. Drafts produced

| Quantity | Draft 1 (`paper/`, `draft-1/main.pdf`) | Draft 2 (`paper2/`, `draft-2/main-v2.pdf`) |
|---|---|---|
| Pages | 19 | 12 |
| Structure | Full paper: Introduction, Related Work, Method, Experiments, Discussion and Limitations, Conclusion, 4 appendices | Slide-sequence outline, 9 sections, no appendices |
| Figures | 9 | 9 |
| Tables | 3 | 0 |
| References cited | 25 of 30 in `refs.bib` | 12 |
| Numbers used | corrected (Shrey's answers) | deck's own values |
| Verify markers remaining | 0 | 0 |
| Overfull boxes | 0 | 0 |

## 13. Bibliography

| Quantity | Value |
|---|---|
| Entries in `refs.bib` | 30, each verified against publisher, PMLR, arXiv or the official model card |
| Entries with author lists truncated to 3 + et al. | those with more than 10 authors (Cosmos reports, Ego4D, RT-2, OpenVLA, π0, Open X-Embodiment, SAM2, Depth Anything and similar) |
| Items with no citable paper | Cosmos Predict2 (model card only); Cosmos Transfer 2 (does not exist; lineage is Transfer1 → 2.5); TransNetV2 (arXiv only) |

## 14. Open numbers (no reliable value as of this document)

1. Total footage duration (31:44 vs 29:00 arithmetic).
2. Exact raw proposal count per clip before filtering.
3. Whether the exported shelf and pillow masks are the ones Transfer received.
4. GPT-4o mini token counts behind the $0.12.
5. Cosmos 3 Nano parameter count against the Cosmos 3 technical report.
6. Which of the 64 renders correspond to the figures (by inference only).
7. Full list of tasks across the 8 recordings.
8. Any code or data release URL.
