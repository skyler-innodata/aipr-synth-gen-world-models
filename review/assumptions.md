# Working assumptions and their resolution

Each row is an open question from `answers-from-shrey-notes.md`. The manuscript marks every dependent sentence with `[VERIFY: A<n>]`. When a row is CONFIRMED, grep the paper for its tag and remove the marker after fixing the sentence.

Status key: ASSUMED = placeholder. CONFIRMED = Shrey's answer (chat, 2026-10-16 10:11). PARTLY = some sub-items still open.

| Tag | Question | Current answer | Status |
|---|---|---|---|
| A1 | How many synthetic clips were actually generated? | **64 Transfer renders over 10 source clips** (about 6 per clip). "Thousands" on the slides = 72 variations accepted by GPT-4o mini per clip × 116 clips = 8,352, a projection. | CONFIRMED |
| A2 | Was the subtraction mask a hard spatial constraint? | **No.** The mask enters only as the seg control; the diffusion model follows it to the degree set by the seg weight. No inpainting or hard region mask. The paper frames leakage as expected soft-control behavior and names a hard constraint as the missing piece. | CONFIRMED |
| A3 | 116 or 129 source clips? | **116 clips**; 129 was a miscount, not a pre-filter number. Total stated duration 31 min 44 s still exceeds 116 × 15 s = 29 min, so the total itself needs re-checking. | PARTLY (total duration) |
| A4 | Generation settings | Transfer frame count confirmed: Shrey cut outputs to 60 frames before saving; report 60. Guidance: 2 and 3 under-applied or skipped the variation; above 5 the scene stopped looking real; 4 used throughout. **Transfer 2.5:** 35 denoising steps at 30.98 s/step (18 min 4 s sampling), about 2 min control-map overhead, about 20 min wall-clock per clip; guidance scale 4; raw control weights edge 0.5, depth 0.2, vis 0.025, seg 0.175 (sum 0.9; the earlier 0.556/0.222/0.028/0.194 are these normalized to 1); seeds not fixed. Shrey's table says 93 frames at 848×480 but marks both as "implied" from the NVIDIA benchmark, whereas the actual output videos in the deck measure 854×480, 60 frames, 4 fps. The paper reports the measured values. **Predict2 2B Video2World:** 35 steps at 5.97 s/step, 3.5 min per clip, 848×480, 16 fps, 93 frames (measured), seed = abs(hash(prompt_id)) mod 2^32. | CONFIRMED (frame count discrepancy noted) |
| A5 | GPT-4o mini prompts, filter criteria, counts | **Both instructions received.** Filter: six plausibility checks (material vs task forces, object size vs scene, material vs environment, physics, lighting vs time of day, implausible object), silent rejection, one-line rationale per accepted item; output structured per the Cosmos 3 caption schema. Prompt writer: `prompt-for-cosmos-transfer.txt`. Acceptance 72 per clip on average. Still open: exact raw proposal count behind "100+". | PARTLY (raw count) |
| A6 | Prompt-to-output mapping; Predict2 prompts | All prompts recovered, including the Predict2 cable-wrapping prompt. Which of the 64 renders correspond to the slide figures is still by inference. | CONFIRMED (prompts) |
| A7 | Seg masks for shelf and pillow | Files received in `segmentation/` but nearly empty (0.1% and 2.4% white). Either a wrong export or evidence that SAM2 propagation collapsed on those clips, in which case the seg control was effectively absent for those renders. See `review/leakage/README.md`. Pillow original and generated videos also still needed (deck has stills only). | BLOCKED |
| A8 | GPT-4o mini token counts | Not available. The $0.12 figure stands without a token breakdown. | CLOSED (no data) |

## Decisions

| Tag | Decision | Current | Status |
|---|---|---|---|
| D1 | Venue template and length | Springer LNCS (`llncs`), AIPR 2026 proceedings. **No page limit** (confirmed by user, 2026-10-16). Working target stays at about 20 pages so the paper is sized by content, not by the absence of a cap. Final paper due Oct 22, 2026 via Springer Meteor with PDF, source, figure sources, signed Licence to Publish. | CONFIRMED |
| D2 | Domain-randomization baseline | Not run; stated as a hypothesis in the Discussion. | ASSUMED |
| D3 | Author order and contact | Shrey Jha, Skyler Saucedo, Frank Tanner. Emails and ORCIDs are placeholders. | PLACEHOLDER |
