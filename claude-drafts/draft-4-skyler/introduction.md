# Draft 4: Introduction

Two variants, both built on Skyler's points: scale per EgoScale; diversity per the data scaling laws paper; collection cost; the multiplier from permuting the ontology; and why this matters to robotics companies (closing the real-to-sim-to-real loop quickly). Citation keys in brackets. Existing keys are from refs.bib; five new ones are marked NEW and listed at the end.

Before reading, see the cost arithmetic in the notes. The confirmed numbers support a 72-fold multiplier in hours of video, not a 10-fold cost reduction, and "hundreds of hours" from one video is about 4 hours. Both variants state what the numbers support.

---

## A. Points in order (scale, diversity, cost, multiplier, loop)

Policies that generalize are trained on volumes of data no single lab records by hand. pi0 pretrains on more than 10,000 hours of robot data [pi0]; LingBot-VLA on about 20,000 hours from nine dual-arm platforms, with success rates still rising at that scale [NEW lingbotvla]; EgoScale on 20,854 hours of egocentric human video, where action-prediction loss falls log-linearly with hours and that loss tracks success on a real robot [NEW egoscale]. The last result is the one that matters here, because it makes egocentric human video rather than teleoperation the scalable source: a person wearing a camera while doing chores is training data. What the hours contain matters as much as how many there are. Lin et al. collected 40,000 demonstrations and found that a single-task policy's generalization follows a power law in the number of training environments and objects, that additional demonstrations in the same environment stop helping past a threshold, and that 32 environments with one object each were enough for 90 percent success in rooms and on objects never seen [NEW lin2025scaling]. The useful unit of data is a new combination of surface, object, lighting and clutter around the same action. We call that combination the ontology of a scene, and diversity of ontology, not hours, is what a policy needs.

Recording that diversity is where the cost sits. An hour of egocentric video costs 8 to 15 USD in collector pay [CITATION NEEDED: hourly rate], so 20,000 hours for a single task is 160,000 to 300,000 USD before anyone has found that many different kitchens, and the kitchens are the hard part: the scaling result says the next hour in the same room is close to worthless. The existing shortcuts each give up something. MimicGen multiplies 200 human demonstrations into 50,000 by replaying trajectory segments in new object poses, but in simulation and for robot trajectories, not video [NEW mimicgen]. FieldGen automates the reaching phase of a demonstration and keeps the human for contact [NEW fieldgen]; it saves operator time, not environments. Domain randomization perturbs colors and textures with no notion of the task, so a cleaning bucket gets a texture no bucket has [tobin2017]. Generative augmentation with image diffusion models produces plausible single frames but does not hold hands and objects steady across a clip [rosie, genaug]. Structure-conditioned video models can restyle a whole clip [gen1, controlnet], and NVIDIA's Cosmos family packages this for physical AI [cosmos2025], but none of them decides what in a clip should change and what must stay fixed.

We take the clip as the unit and permute the ontology around the recorded action. A reasoning model reads the clip and writes the scene as a structured ontology: the task, each object with its role in that task, and the variations each object could plausibly take while the task stays the same. A language model filters the candidates and writes a prompt, a segmenter builds a mask of the one surface to change, and a guided video-to-video model renders the variant with the hand motion intact (Fig. 1). On 116 clips from 8 recordings the reasoning stage admits 72 variations per clip, so a 15-second clip becomes 18 minutes of candidate video and a 10-minute recording about 4 hours, a 72-fold multiplier with no new recording and no new kitchen. The same arithmetic sets the limit: a render costs 20 minutes on one A100, or 80 GPU-hours per synthetic hour, so at today's speed the pipeline buys diversity rather than cheaper hours. For a robotics company the value is in the loop this closes. Real recordings from a deployment become synthetic variants the same day, the variants retrain the policy, the retrained policy goes back on the robot, and its new recordings seed the next round; the pipeline turns the real-to-sim-to-real cycle from a collection campaign into a batch job. The paper reports what the pipeline produces and where it stops. Single-surface recolors keep hand pose, object shape and motion, but the edit does not stay inside its mask: in the counter-wiping clip the protected region shifts by a mean CIE76 ΔE of 35 against 75 for the target. Scenes with many textures recolor wholesale, and two attempts at action-level change with Cosmos Predict2 returned the scene unchanged. Whether appearance diversity alone makes a policy more general, or whether action generation has to be solved first, is the question these results leave open.

(about 700 words)

What it emphasizes: the argument chain exactly as laid out, with each reference doing one job. Longest of the two; the second paragraph carries six citations of prior work and part of it could move to Related Work.

---

## B. Running example first, then the points

One clip shows a person wiping a counter with a bucket and paper towels (Fig. 1a). A policy trained on it and a few hundred like it learns that counter, that bucket and that light, and nothing in the data says the task survives a blue laminate or a different bucket. The field's answer to this is scale. EgoScale pretrains on 20,854 hours of egocentric human video and finds that action-prediction loss falls log-linearly with hours, with no sign of flattening, and that the loss predicts real-robot success [NEW egoscale]; LingBot-VLA sees the same trend on 20,000 hours of robot data [NEW lingbotvla]. But Lin et al. show that the hours are not interchangeable: across 40,000 demonstrations, a policy's generalization grows as a power law in the number of distinct environments and objects, and extra demonstrations in a room it has already seen stop helping [NEW lin2025scaling]. What the policy needs from the counter clip is the same wiping motion over many counters, buckets and lights. That set of variations, tied to the action, is what we call the ontology of the scene.

Collecting it is the expense. At 8 to 15 USD per hour of egocentric video [CITATION NEEDED: hourly rate], a 20,000-hour set for one task costs 160,000 to 300,000 USD, and the money is the smaller problem: each hour has to come from a different room with different objects to count. MimicGen showed in simulation that 200 demonstrations can become 50,000 by replaying them in new object poses [NEW mimicgen], and FieldGen cut operator time by automating the approach phase [NEW fieldgen], but neither produces new appearances of a real scene. Domain randomization does, blindly [tobin2017]; image diffusion augmentation does, one frame at a time [rosie, genaug]; conditioned video models restyle a clip but have no way to decide what should change [gen1, controlnet, cosmos2025].

We chain existing models so that a reasoning step makes that decision and a guided renderer carries it out. Cosmos 3 Nano reads the clip and writes the ontology, GPT-4o mini filters it and writes the prompt, SAM2 masks the surface to repaint, and Cosmos Transfer 2.5 renders the variant with the source motion (Fig. 1b). On 116 clips the reasoning stage admits 72 variations per clip, so one 10-minute recording becomes about 4 hours of candidate video, a 72-fold gain in hours without a new room. A render costs 20 minutes on an A100, so the gain is in diversity rather than in cost per hour, and we say so. What that buys a robotics company is a short loop: footage from today's deployment becomes tomorrow's training variants, the retrained policy goes back on the robot, and the real-to-sim-to-real cycle runs in days instead of a collection season. The renders show where the method stands: the counter turns blue with hand, bucket and motion intact, but the protected region still shifts by a mean CIE76 ΔE of 35 against 75 for the target, cluttered scenes recolor entirely, and Cosmos Predict2 asked to wind a cable or rotate a sheet of paper did neither. The open question is whether appearance diversity alone makes a policy more general, or whether action generation has to be solved first.

(about 580 words)

What it emphasizes: the talk's running example as the hook, with the points folded into three paragraphs. Shorter, and closer to the register of the talk.

---

## Notes for discussion

### The cost claim, with the confirmed numbers

| Quantity | Value | Source |
|---|---|---|
| Admissible variations per 15 s clip | 72 | Shrey, confirmed |
| Synthetic video per clip | 18 min (72 x 15 s) | arithmetic |
| Synthetic video per 10-min recording | about 4.4 h (14.5 clips x 18 min) | arithmetic |
| Synthetic video from all 116 clips | about 35 h | arithmetic |
| Multiplier in hours | 72x | arithmetic |
| Transfer render time | 20 min per 15 s clip on one A100 80 GB | Shrey, confirmed |
| GPU time per synthetic hour | 80 A100-hours (240 clips x 20 min) | arithmetic |
| GPU cost per synthetic hour | about 96 USD at 1.2 USD per A100-hour (Colab Pro+ rate, VERIFY); about 240 USD at 3 USD per hour (cloud list, VERIFY) | arithmetic |
| Human collection cost per hour | 8 to 15 USD | Skyler; CITATION NEEDED |
| Distilled Transfer (NVIDIA docs, about 1 min per clip on H100) | about 4 GPU-hours per synthetic hour, 5 to 12 USD | NVIDIA reference timing, not run by us |

Per hour of video, the pipeline at our settings costs 6 to 30 times more than paying a collector, not 10 times less. The claim that holds is the multiplier in diversity: one recording yields 72 appearance variants of every action without a new room, and the room is what the scaling law says is scarce. Both variants are written on that claim. If the distilled Transfer model is run and timed, cost per hour becomes comparable to human collection and the sentence can be revised. "Hundreds of hours" from one video is not supported; about 4 hours per 10-minute recording is.

Also: the 72 are proposals that passed a plausibility filter, not rendered clips. We rendered 64 across 10 clips. The multiplier is capacity.

### The real-to-sim-to-real loop

Both variants now carry one or two sentences on it, placed after the multiplier so the reader has the numbers first. Two cautions. The loop is a value proposition, not a result: nobody in this work retrained a policy and redeployed it, so the sentence has to stay in the conditional register ("turns the cycle into a batch job") and not claim a measured cycle time. And "sim" is loose here, since the variants are edited real video rather than a simulator; "real-to-synthetic-to-real" is more exact if a reviewer is likely to object. The Discussion is the place to expand the loop into a paragraph, with the policy-training experiment named as the step that would close it.

### The 8 to 15 USD per hour figure

None of the six references states a per-hour collection cost. MimicGen says "costly and time-consuming", FieldGen "prohibitively expensive", neither with a number. If the figure comes from Innodata's own collection rates, say so in the text ("in our own collection experience") and it needs no citation. If it is meant as a field-wide number it needs a source; the Ego4D or EPIC-KITCHENS papers may report participant compensation, and crowd-work rate surveys are another option. Marked CITATION NEEDED in both variants.

### How the reference introductions are built

All six open on the field's data problem, not on their own system, and all but pi0 reach a specific number inside the first two paragraphs (200 demos for 73 percent, 1.5 years for RT-1, 20,854 hours, 40,000 demonstrations). All six end with a contributions list; MimicGen and EgoScale phrase theirs as findings with numbers, which is the form the project rules ask for. Variant A's last paragraph does this in prose; a three-bullet version is easy to add if the page reads better with one. pi0 is the outlier, opening with a Heinlein epigraph and a page of philosophy, and is not a model for a workshop paper.

### Mapping references to the points

1. Lots of egocentric data needed: EgoScale (20,854 h, log-linear scaling); LingBot-VLA (20,000 h, no saturation); pi0 (10,000 h) as the VLA baseline.
2. Diversity for generalization: Lin et al. 2025 (power law in environments and objects; diversity beats demo count; 32 environments x 1 object x 50 demos for 90 percent). This is the strongest single citation in the paper's favor and should carry the "ontology diversity" claim.
3. Cost: no reference gives a rate. MimicGen's RT-1 anecdote (1.5 years, several kitchens) is the best qualitative support.
4. Multiplier: MimicGen (200 to 50K) is the precedent for "small set, large synthetic set" and the natural comparison; the difference is simulation trajectories vs real-video appearance.
5. Loop: no reference frames it this way. FieldGen is the closest (semi-automated collection as an ongoing process).

### New bib entries needed (do not fabricate; take from the PDFs in references/)

- egoscale: Zheng et al., "EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data", arXiv 2602.16710, 2026.
- lin2025scaling: Lin et al., "Data Scaling Laws in Imitation Learning for Robotic Manipulation", ICLR 2025 (arXiv 2410.18647).
- mimicgen: Mandlekar et al., "MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations", CoRL 2023 (arXiv 2310.17596).
- fieldgen: Wang et al., "FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation", arXiv 2510.20774, 2025.
- lingbotvla: Wu et al., "A Pragmatic VLA Foundation Model" (LingBot-VLA), arXiv 2601.18692, 2026.

pi0 is already in refs.bib. Published versions should be checked on DBLP before the entries are added (CoRL for MimicGen, ICLR for Lin et al.).
