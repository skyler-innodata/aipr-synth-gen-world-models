# Notes on answers-from-shrey.pdf (received 2026-10-16)

Structured transcription of the answers to the B6 open items in the slide review. Facts are recorded as given. Items marked OPEN still need an answer before they can go into the manuscript.

## Models and checkpoints

| Role | Model | Notes |
|---|---|---|
| Reasoning / detection / ontology | Cosmos 3 Nano | 16B total params, 8B reasoning tower, 8B generation tower. Reasoner "worked great". Generation tower tried and found to lack video-to-video transfer support. |
| Appearance transfer | Cosmos Transfer 2.5 | |
| Action generation (slide 15) | nvidia/Cosmos-Predict2-2B-Video2World | |
| Segmentation | SAM2 | Boxes from Cosmos 3 Nano (`bbox_2d`, normalized 0 to 1000), SAM2 converts to pixel masks, tracked across frames (video mode). Outputs `seg_mask.mp4` and `seg_overlay.mp4`. |
| Clipping | TransNetV2 (via Cosmos Curate) | |
| Prompt writing / filtering | GPT-4o mini (per deck) | System prompt not yet provided. OPEN. |

Consequence for the deck: slide 8's title ("What Cosmos Reason Produces") and slide 18's framing of Cosmos 3 as future work are both wrong. Cosmos 3 Nano was the reasoner in the actual pipeline.

## Data

- Source: 8 egocentric recordings, each about 10 minutes, person holding the camera while performing household tasks.
- Clipped with TransNetV2 to 129 clips. Downsampled to 15 s and 4 fps.
- Stated total duration: 31 min 44 s. 129 × 15 s = 32.25 min, so 31:44 is the post-clipping total, not the raw footage (8 × 10 min ≈ 80 min). OPEN: confirm, and state both numbers in the paper.
- Slide 24 says 116 clips. Answer says 129. OPEN: which is correct, or is 116 the count after some filter?

## Cosmos Transfer 2.5 control weights

```
edge  0.556
vis   0.028
depth 0.222
seg   0.194
```
Sum = 1.000. Rationale given: edge below ~0.56 caused shape collapse; depth above ~0.22 flattened the scene to a plane; vis above ~0.03 locked the source appearance; seg at ~0.19 kept generation spatially grounded. The effective tuning space was the vis/seg split within the ~0.22 left after edge and depth were fixed by failure modes.

OPEN: guidance scale, denoising steps, output resolution, frame count, seed policy. None were given.

OPEN (important): was the subtraction mask applied as a spatial constraint on generation (a region-weight or inpainting mask), or was it only fed as the seg control input at weight 0.194? If the latter, the pipeline never had a hard "paint only here" constraint, and the color leakage on slides 4, 13, 14, 16 is the expected behavior of a soft control, not a failure of masking. The paper's framing depends on this.

## Compute (Google Colab, A100 80 GB, Colab Pro+)

| Stage | Time per clip |
|---|---|
| Cosmos 3 Nano: boxes + ontology + prompt | 129.5 s |
| Cosmos Transfer 2.5 | ~20 min |
| Cosmos Predict2 2B | 3.5 min |

## Experiments actually run (Transfer prompts supplied)

1. Bucket cleaning → blue countertop. Full prompt provided. Described as "first and most-run prompt".
2. Shelf clip → blue desk and shelf. Full prompt provided.
3. Shelf clip → modern white desk with oak shelf. Full prompt provided.
4. Pillow casing → cobalt blue folded blanket on left of bed. Full prompt provided. Note: the prompt targets a blanket, but the output on slide 14 recolored nearly the whole frame.
5. Pillow casing → chunky cream knit blanket. Prompt text lost; same structure as 4.
6. Fixing bed → navy blue area rug. Full prompt provided.
7. Predict2: cord wrapping (slide 15). Prompt not provided. OPEN.

Mask figures provided for the shelf clip (furniture mask + overlay) and the bucket clip (surface / subtract / final strip).

OPEN (most important): how many synthetic clips were actually generated in total? Question 5 was answered "provided above" but no number appears. From the prompt list, the count looks like roughly 6 to 10 Transfer outputs and 1 Predict output, not hundreds. Slide 2's "thousands of clips" and slide 24's 8,120 are projections.

OPEN: mapping from each prompt to each output video on slides 13 to 16, and a one-line outcome for each.

## Baseline

No domain-randomization baseline exists. Author unsure how to run one.

## Clearance

Clearance to publish clips, frames, prompts and the ontology schema (confirmed with Frank Tanner).

## Cosmos 3 Nano prompt

Full system prompt `COSMOS3_BBOX_VARIATION_PROMPT` provided (pages 5 to 12 of the PDF). Key properties:
- Up to 10 task-relevant objects, each with `bbox_2d` normalized 0 to 1000.
- JSON schema: `location`, `task` (name, description, phase, action_primitive, difficulty, typical_duration_seconds), `key_objects[]` (rank, name, bbox_2d, is_primary, role_in_task, current_appearance{color_description, rgb, hex, material, texture, condition, size_estimate}, current_state{...}, variations{color_and_appearance, material_and_texture, size_and_shape, state_and_position, condition, interaction, brand_and_style}, robustness_gaps{what_robot_must_handle, common_failure_modes, edge_cases}), `scene_variations{...}`, `dataset_gaps{...}`.
- Instructs "enumerate EVERY variation dimension exhaustively", "Include 10+ solid colors".
- Output wrapped in `<think>...</think><answer>...</answer>`.

The "100+ raw proposals, ~70 after filtering" figure on slide 7 is therefore a direct consequence of this prompt's exhaustiveness instruction. OPEN: actual per-clip counts across the 129 clips, and the GPT-4o mini filter criteria and rejection rate.

## Observations on the answers themselves

Answers 3 and 4 are written in the second person ("Your Cosmos Transfer Colab", "the spec you just showed me") and read as pasted from an assistant's summary of Shrey's notebooks. The content is plausible (weights sum to exactly 1.0), but each fact should be checked against the notebook before it is typeset.
