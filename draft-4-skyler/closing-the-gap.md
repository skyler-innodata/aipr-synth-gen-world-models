# Draft 4: Closing the Gap

Skyler's draft of the Discussion ("Closing the gap"), reviewed against the confirmed numbers, then rewritten. Numbers from `technical-details.md` and `results.md` Part 6. Written 2026-10-18.

## Corrections to the draft

- **Counts.** 6,260 is the projection for one raw hour, not what was produced. The chain is 8 recordings, 116 clips, 8,352 admissible variants (capacity), 64 rendered. 72 is the average number of admissible variations per 15 s clip, not per recording, and they are proposals, not renders.
- **"Without adding any hallucination"** is contradicted by Fig. 1 (new ceiling light, recolored towels and bucket, shifted wall) and by the leakage table (protected region ΔE 35 against 75 for the target).
- **Cost.** 1.20 USD is the price of one A100-hour. A synthetic hour needs 80 A100-hours, so about 96 USD per synthetic hour at that rate and about 2,500 USD to render everything from one raw hour. The 0.12 USD was the LLM cost for all 116 clips, not per hour. The pipeline costs 6 to 30 times the collector rate per hour of video; what it buys is diversity.
- **"Maintaining the overall physics"**: untested; no policy was trained and the leakage result argues the other way for appearance.
- **"Humanoids"**: nothing in the data or method is humanoid-specific. "Robot manipulation policies" covers it.
- **"Cohesive and practical solution"**: self-praise; cut.
- **"Sufficient hours"**: no result establishes sufficiency.

## Rewritten section

**5 Closing the Gap**

Eight recordings of about ten minutes each became 116 clips, and the reasoning stage admitted 72 variations per clip, so the set is capacity for 8,352 synthetic clips, about 35 hours of candidate video from 29 minutes of source. In duration that is a 72-fold multiplier: one 10-minute recording becomes about 4 hours without a new room, a new recording or a new collector. How many variants a clip admits depends on how many task-relevant objects the ontology finds and on which of their attributes a video-to-video model can change while holding the action fixed, which today means color, material and surface finish and not shape, layout or motion. We rendered 64 of the 8,352, and the 64 are the only synthetic video that exists.

The cost sits in the render. Reasoning takes two minutes per clip and the language model costs cents across the whole set, but a Transfer render takes 20 minutes per 15-second clip on an A100, so every hour of synthetic video costs 80 A100-hours, about 96 to 240 USD at current cloud rates [VERIFY: price], against 8 to 15 USD for an hour of collected egocentric video [CITATION NEEDED: rate]. At today's speed the pipeline is not a cheaper source of hours. What it is a cheaper source of is diversity: Lin et al. [lin2025scaling] found that a policy's generalization scales with the number of distinct environments and objects and that further demonstrations in a room it has already seen stop helping, and the pipeline produces 72 appearance variants of every action without the recruitment, travel and setup that a new room costs a collector. The distilled Transfer model, which NVIDIA reports at about one minute per clip on an H100, would bring the rate per synthetic hour into the collector's range; we have not run it, and the measurement is the first thing to do.

Three things stand between the rendered variants and a training set. The edit must stay inside its mask. On the one clip measured, the protected region moved by a mean CIE76 ΔE of 35 against 75 for the target, so a policy trained on today's variants would learn that counters, towels and buckets change color together. The mask entered the renderer only as a soft control; spatiotemporal control-weight maps or compositing the source back outside the mask are both available and both untested here, and a coverage check before rendering would have caught the two near-empty masks we retained. The premise needs a baseline. A prompt-level domain randomization that draws color and material at random for the same target under the same controls would test whether task-grounded variation is more plausible than random variation, at a cost of a few renders. And the variants need a policy. Training on them and measuring held-out success is the experiment that decides whether the pipeline is useful, and nothing above substitutes for it. Action-level variation is the longer gap: Predict2 held the scene still when asked to wrap a cable or turn a sheet of paper, and fine-tuning it on real manipulation video is the direct route. For a lab with a few hours of egocentric footage, one GPU and public checkpoints, the appearance half of this loop runs today; whether appearance diversity alone makes a policy more general, or action generation has to be solved first, is the question it leaves open.

(about 560 words)

## Notes

- Shorter version: drop the action-generation and baseline sentences from paragraph 3 and keep containment and policy training, which are the two a reviewer will ask about.
- The per-hour comparison should carry sourced prices or be restated in GPU-hours per synthetic hour against collector-hours per hour, which needs no price.
- "Lin et al. [lin2025scaling]" is a NEW bib entry listed in `introduction.md`; take it from the PDF in `references/` and check the ICLR 2025 version on DBLP.
- The opening sentence repeats Table 1 of Results on purpose, so the Discussion stands alone for a reader who skips to it; if the two sections sit on the same page, cut the first sentence here.
