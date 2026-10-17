# Draft 4: Abstract

Three variants. All use only confirmed numbers (technical-details.md): 8 recordings, 116 clips, 72 admissible variations per clip, about 2 min reasoning, 20 min per Transfer render, 64 renders, bucket-clip leakage of 75 (target) vs 35 (protected) mean CIE76 ΔE. None says "thousands of clips"; 8,352 is a projection and belongs in the Introduction as capacity.

---

## A. Talk order (problem, contrast, three stages, success then failure)

A robot policy trained on a few egocentric recordings learns those recordings: one counter, one bucket, one light. Vision-language-action models cover that variety with hundreds of thousands of demonstrations, mostly the same tasks under new appearances, and recording them by hand is slow. Domain randomization is cheap but blind to the scene, giving a cleaning bucket textures no bucket has. We describe a pipeline on NVIDIA Cosmos that produces appearance variants of real clips while keeping the recorded actions. Cosmos 3 Nano reads a clip and writes an ontology: the task, each object with its box and role, and variations grounded in that role. GPT-4o mini rejects implausible candidates and writes the prompt. SAM2 turns the boxes into tracked masks, a subtraction step isolates the surface to repaint, and edge, depth, color and segmentation maps guide Cosmos Transfer 2.5. On 116 clips from 8 recordings, reasoning yields 72 admissible variations per clip in about two minutes, and one render takes 20 minutes on an A100; we rendered 64. Single-surface recolors preserve hand pose, object shape and motion, but the edit does not stay where it was sent: in the counter-wiping example the target region moves by a mean CIE76 ΔE of 75 and the protected region by 35, and cluttered scenes recolor almost entirely. Action-level variation with Cosmos Predict2 produced no motion. Appearance variation is now cheap to propose and render; containing the edit and generating new actions stand between this output and a robot training set.

(248 words)

What it emphasizes: the pipeline as a system, with the slide 7 contrast against domain randomization as the reason for the reasoning stage. Closest to how the talk was given.

---

## B. Open-question first (the "Main Points" slide as an abstract)

Is synthetic appearance data enough to make a robot policy more general, or does action generation have to be solved first? We take the question seriously by building the appearance half and measuring where it breaks. Starting from 8 egocentric recordings of household chores, cut into 116 clips, a three-stage pipeline on NVIDIA Cosmos reasons about each clip, decides what may change, and renders the change with the recorded motion intact. Cosmos 3 Nano writes a task ontology with boxes, roles and candidate variations for each object; GPT-4o mini filters the candidates against six plausibility checks and writes the prompt; SAM2 and a subtraction mask mark the surface to repaint; Cosmos Transfer 2.5 renders under edge, depth, color and segmentation guidance. The reasoning stage admits 72 variations per clip in about two minutes, a render takes 20 minutes on one A100, and we produced 64. The renders answer the first half of the question in part. Recolors of a single surface keep hand pose, object geometry and motion, but containment fails: in the counter-wiping clip the protected region shifts by a mean CIE76 ΔE of 35 against 75 for the target, and scenes with many textures recolor wholesale. The second half of the question stays open, because Cosmos Predict2 asked to wind a cable or rotate a sheet of paper returned the scene unchanged. Appearance variation is cheap to propose and render; whether it helps a policy cannot be tested until the edit stays inside the mask.

(245 words)

What it emphasizes: the open question as the frame, so the paper reads as an honest probe rather than a system paper. Risk: a reviewer may ask why the policy experiment was not run, since the abstract promises the question.

---

## C. Plainest, shortest (the running example carries it)

One clip shows a person wiping a counter with a bucket and paper towels. A policy trained on that clip and others like it knows that counter, that bucket and that light, and recording every other counter is not practical. We built a pipeline on NVIDIA Cosmos that takes such a clip and returns the same actions with a different appearance. Cosmos 3 Nano describes the scene as an ontology of the task, its objects and the variations each object can plausibly take; GPT-4o mini filters those and writes a prompt; SAM2 masks the surface to repaint; Cosmos Transfer 2.5 renders it under four guidance maps. From 8 recordings and 116 clips the reasoning stage proposes 72 admissible variations per clip, and we rendered 64 of them at 20 minutes each on one A100. The counter turned blue and the hand, bucket and motion stayed put, but so did little else: the protected region changed by a mean CIE76 ΔE of 35 against 75 for the target, cluttered scenes recolored entirely, and two attempts at action-level change with Cosmos Predict2 produced no motion. The cheap part of synthetic appearance data is done. Keeping the edit where it belongs, and changing what happens rather than how it looks, are what is left.

(220 words)

What it emphasizes: the running example from slides 3 and 4, in the register of the speaker notes. Fewest method details; the reader learns the stages but not the mask construction or the guidance terminology.

---

## Notes for discussion

- A is the recommendation. B is worth considering if the paper's framing shifts toward the open question. C is the shortest and the most like the talk, but says the least about the method.
- All three keep "72 admissible variations per clip" rather than "about 70 from 100+", since the raw proposal count was never measured.
- All three report leakage from one clip only, and say so ("in the counter-wiping example"). The shelf and pillow masks on hand are nearly empty, so the measurement cannot be repeated on them (review/leakage/README.md).
- "Blind to the scene" (A) and "cheap but blind" could be read as dismissive of domain randomization. Neutral alternative: "Domain randomization is cheap but has no notion of the task, so its variations are not constrained by what the object is for."
- Keywords for LNCS: Synthetic data; World foundation models; NVIDIA Cosmos; Egocentric video; Robot learning.

---

## D. Skyler's draft (abstract.txt), revised

Keeps Skyler's order (bottleneck, pipeline, scale, boundary, what the paper offers) and replaces each unsupported claim with the measured one.

Robot manipulation policies are bottlenecked by real-world data: the demonstrations that make them generalize cost hours of human time per task, and most of that time goes to showing the same task under different objects, surfaces and lighting. We describe a pipeline on NVIDIA Cosmos that produces appearance variants of real egocentric clips while keeping the recorded actions, so a small dataset can be multiplied without new recording. Cosmos 3 Nano writes an ontology of each clip, the task and each object's role and plausible variations; GPT-4o mini filters the candidates and writes the prompt; SAM2 masks the surface to repaint; and Cosmos Transfer 2.5 renders under edge, depth, color and segmentation guidance. From 116 clips the reasoning stage admits 72 variations per clip, enough for about 8,000 synthetic clips at 20 GPU-minutes each; we rendered 64. Permuting attributes within the ontology gives task-grounded rather than random variation, and single-surface recolors keep hand pose, object shape and motion. The boundary is also clear: the edit leaks outside its mask (protected pixels shift by a mean CIE76 ΔE of 35 against 75 for the target), cluttered scenes recolor wholesale, and action-level changes with Cosmos Predict2 produce no motion. We report the process, the guidance weights and prompt rules that made it work, and the limits a policy trained on this data would inherit.

(214 words)

Changes from the .txt and why:
- "thousands of synthetic training clips" became "enough for about 8,000 ... we rendered 64". The deck's own slide 18 lists scaling past 100 clips as unfinished; 8,352 is arithmetic, not output.
- "provides the diversity needed for effective robot policy training" was cut. No policy was trained, so the sentence claims the one result we do not have. The closing sentence now says what a policy would inherit instead.
- "robust realistic permutations" became "task-grounded rather than random variation". "Robust" is on the strike list and nothing was measured for robustness; "task-grounded" is what the ontology actually does, and the contrast with random is the slide 7 argument.
- "a powerful and economical approach is scalable" was cut. The phrase is nearly verbatim from the MimicGen abstract ("a powerful and economical approach towards scaling up robot learning"), where it was earned by a cost comparison against human demonstrations. A reviewer who knows MimicGen will notice, and we have no cost comparison.
- "In this paper, we provide a primer" became "We report the process, the guidance weights and prompt rules". "In this paper" is on the project's do-not list; "primer" undersells a paper that has a measurement in it.
- "humanoid robotics" was dropped. Nothing in the deck or data is humanoid-specific; "robot manipulation policies" covers it.
- "task completion scores" was dropped because we report none.
- Spelling: maniuplation, availablity, realworld, smal, syntetic, permutions, aproach.
