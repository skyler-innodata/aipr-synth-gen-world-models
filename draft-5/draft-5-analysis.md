# Draft 5: analysis against the thesis, the references and drafts 1 to 4

Written 2026-10-18 from `draft-5/AIPR 2026 Paper-draft-5.pdf` (transcribed in `AIPR-2026-Paper-draft-5.md`), the deck review, `technical-details.md`, `review/assumptions.md`, `review/reference-abstracts.md`, the six PDFs in `references/`, drafts 1 to 3 (`paper/`, `paper2/`, `paper3/`) and the draft 4 ideation files in `draft-4-skyler/`. Numbers quoted from draft 5 are checked against the confirmed values in `technical-details.md`; numbers quoted from the references are checked against the PDFs.

---

## 1. The central thesis, as the repo records it

The deck (slide 2), draft 3's introduction and `draft-4-skyler/methodology.md` Section 11 agree on three claims and one open question.

1. A multi-model pipeline on NVIDIA Cosmos can turn a small real egocentric dataset into many synthetic training clips that keep the recorded action and change the appearance. Evidence: 116 clips reasoned over, 72 admissible variations per clip, 64 renders over 10 clips; the counter-wiping render keeps hand pose, bucket geometry and motion.
2. Appearance changes work for simple scenes and break down for cluttered scenes and for action-level changes. Evidence: the cloth-folding, desk and rug renders; the leakage measurement (protected region moves by a mean CIE76 ΔE of 35 against 75 for the target); two Predict2 runs that produced no motion.
3. Structured reasoning about the scene yields task-grounded rather than random variations. Status: holds by construction, no baseline run.

Open question: is appearance diversity enough to make a policy more general, or does action generation have to be solved first?

Everything in the repo that carries weight sits under claims 1 and 2: the count table (8 recordings to 116 clips to 8,352 capacity to 64 rendered), the control-weight table with its failure bounds, Eq. 1 for the subtraction mask, the leakage table, and the Predict2 outcome. The two things the repo says no draft may claim are that thousands of clips were generated and that the output is ready to train a robot.

## 2. What draft 5 says the thesis is

Draft 5 keeps claims 1 and 2 in the conclusion ("capable of changing appearance for simpler scenes, however more work must be done for complex scenes ... action-level changes remain unsolved") and keeps the open question. But the abstract and Section 5 re-centre the paper on a fourth claim that the repo flagged as unsupported: that the pipeline is "powerful and economical", "scalable", a "cohesive and practical solution" that makes data cheap. The table below puts each thesis-level sentence in draft 5 against what the evidence supports.

| Draft 5 sentence | Section | What the evidence supports | Status |
|---|---|---|---|
| "scaling a single video into hundreds of permutations" | Abstract | 72 admissible variations per 15 s clip (proposals, not renders); 64 renders across 10 clips, about 6 per clip | Overstated for renders, understated for capacity |
| "structured reasoning about a scene produces robust realistic permutions" | Abstract | Ontology is task-grounded by construction; no baseline; "robust" not measured | Unsupported as stated |
| "this powerful and economical approach is scalable" | Abstract | 80 A100-hours per synthetic hour; 6 to 30 times the collector rate per hour | Contradicted by the arithmetic in `results.md` Part 6 |
| "We propose a method that effectively x10 the amount of trainable data" | Intro | 72x in duration (capacity); 6.4x realized; no trained policy, so "trainable" is untested | Wrong multiplier |
| "Thousands of clips of first person videos of household chores we used" | Results | 116 source clips; 64 renders | False as written |
| "adding more entropy as desired" (wall and lighting changed) | Results | The prompt named wall, lighting, bucket and towels as preserved; the change is leakage, measured at ΔE 35 | Reframes the paper's main negative finding as a success |
| "producing 8,352 synthetic video variations, or about 35 hours of video" | Closing the gap | Projection: 116 x 72; 64 were rendered | Projection stated as output |
| "For every hour processed ... 1.20 USD in GPU ... 0.12 in token costs" | Closing the gap | 1.20 USD is about one A100-hour on Colab Pro+ (VERIFY); one synthetic hour needs 80 A100-hours; 0.12 USD was the LLM total for all 116 clips | Wrong by roughly two orders of magnitude |
| "turn a real, limited first-person dataset into thousands of synthetic training clips" | Conclusion | Capacity, not output | Projection stated as output |

The shift matters because the six reference papers all earn their closing claim with a trained policy and a number. Draft 5 borrows the MimicGen closing phrase ("a powerful and economical approach") without the policy result that justified it there, and adds a cost comparison whose numbers go the other way.

## 3. Draft 5 against drafts 1 to 4

### 3.1 Structure and content

| | Draft 1 (`paper/`) | Draft 2 (`paper2/`) | Draft 3 (`paper3/`) | Draft 4 (`draft-4-skyler/`) | Draft 5 |
|---|---|---|---|---|---|
| Form | LNCS LaTeX, 19 pp | LNCS LaTeX, 12 pp | LNCS LaTeX, 9 pp | Markdown ideations, section by section | Google Doc, 10 pp |
| Sections | Intro, Related, Method, Experiments, Discussion, Conclusion, 4 appendices | Slide order, 9 sections | Intro, Background and Related, Method (4 subsections), Results (3), Closing the Gap, Conclusion | Abstract, Intro, Methodology, Results, Results (revised), Closing the Gap | Abstract, Intro, Method (3 subsections), Results, Closing the gap, Conclusion, References |
| Related work | Yes | Partial | One paragraph, 17 citations | Folded into Intro variants | Placeholder: "Background? - Description of World Language Models?" |
| Numbers policy | Confirmed values | Deck's values | Confirmed values | Confirmed values with status tags | Mixed: 116 and 72 confirmed; "thousands", "x10", "3 videos", "4-8 mins", "head-mounted", "1.20 USD per hour" unconfirmed or wrong |
| Pipeline figure | TikZ, 3 rows | Slide 6 image | TikZ, in/out | Draft 3's | Draft 1's TikZ, pasted as a bitmap |
| Equation (subtraction mask) | Eq. 1 | none | Eq. 1 | Eq. 1 | none |
| Control-weight table | yes | no | yes | yes, with failure bounds | none; weights not stated |
| Generation settings (35 steps, guidance 4, seeds) | yes | no | yes | yes | none |
| Leakage table | yes | no | yes | yes | none; leakage described as "entropy as desired" |
| Count table (8 to 116 to 8,352 to 64) | partial | no | in prose | Table 1 | in prose, with "3" recordings and no "64 rendered" |
| Predict2 outcome | no motion | no motion | no motion | no motion | "spaghetti", cord "gaining linear mass" (new, unverified, and Fig. 8 shows two identical frames) |
| "No policy was trained" | yes | no | yes | yes, in Setup | absent |
| "No baseline was run" | yes | no | yes | yes | absent; posed as a closing question instead |
| References | 25 cited of 30 | 12 | 17 | keys plus 5 NEW entries listed | two bare URLs |
| Register (Skyler's verdict) | "highfalutin" | "like a guide" | the requested merge | per-section review | Skyler's own voice, plain and practical |

### 3.2 What draft 5 took from draft 4, and what it reverted

Draft 5 lifts several passages from draft 4 nearly verbatim: the Lin et al. sentence, the pi0 and LingBot sentences, the MimicGen sentence (all from `introduction.md` variant A), the three prompt-writing rules with their reasons (`methodology.md` Section 18) and the four-map description (Section 19, partially). It also uses draft 1's pipeline figure and draft 3's ontology figure.

It does not adopt the corrections that `closing-the-gap.md` (written the same day, 2026-10-18) made to the same section: the count chain, the cost arithmetic, "maintaining the overall physics", "cohesive and practical solution", "humanoids" and "sufficient hours" were all flagged there with reasons, and all of them survive in draft 5's Section 5. The Section 3.3 text likewise keeps three claims that `methodology.md` Section 19 corrected: that Canny was chosen over Sobel by us (it is the preprocessor Transfer ships), that the mask defines "exactly which pixels the model can change" (it is a soft control), and "Color for lightning".

### 3.3 What draft 5 adds that no earlier draft had

- The EgoScale scaling figure as Figure 1 (reproduced from the reference; permission needed, see the shore-up file).
- A per-hour cost comparison against collector pay. The intent is right for this venue; the numbers are not (Section 5 of this file).
- Task durations of "4-8mins" and a "head-mounted camera". Neither is in Shrey's answers; Shrey's answer says handheld.
- Depth Anything V2 as the named depth model. Earlier drafts marked the depth model as inferred; the only reference URL in draft 5 points at Video Depth Anything, a different model.
- A "directional reversal" account of the Predict2 experiment (clockwise to counterclockwise winding, "spaghetti" cord). The recovered Predict2 prompt asked for winding the cable around its block with the block held fixed, and the confirmed outcome is no visible motion in either run. Fig. 8 in draft 5 shows two frames that look identical, which matches the confirmed outcome and not the text.
- The pillow clip described as "stuffing a throw pillow for a chair" with a prompt to "change the pillow to blue". The recovered prompt for that clip targets "a cobalt blue folded blanket on the left of the bed" and names the pillow as preserved.

### 3.4 Where draft 5 is better than draft 3

The voice is Skyler's and it reads like a practitioner, which is what the AIPR audience is. Three things are worth keeping as they are:

- The three prompt rules each carry a one-sentence reason, and rule 3's reason (captions, not edit instructions) is the best explanatory sentence in any draft.
- Section 3.1 opens on the running example and asks what a policy must learn before it says what the reasoner does; that order is right.
- The cost framing in Section 5 is the right question for the venue, once the numbers are fixed.

## 4. Draft 5 against the six references

### 4.1 Accuracy of what draft 5 says about each reference

| Reference | Draft 5 says | The PDF says | Verdict |
|---|---|---|---|
| EgoScale (2602.16710) | "over 20,000+ hours of egocentric video are needed per task, with upper limits of achieving a mean task acceptables score of 0.71" | Pretrains on 20,854 hours total across many tasks and environments; average task completion score rises from 0.30 at 1k hours to 0.71 at 20k hours "with no signs of saturation" | Wrong on two points: the hours are not per task, and 0.71 is not an upper limit |
| EgoScale | "scales logarithmically with the hours" | Validation loss follows a log-linear law (R² 0.998); policy score rises monotonically with hours | Acceptable if phrased as "loss falls log-linearly and task completion rises with it" |
| Lin et al. (2410.18647) | 40,000 demos; power law in environments and objects; 32 environments x 1 object gives 90 percent in novel rooms | Matches the abstract and Sec. 4 | Correct (sentence taken from draft 4) |
| pi0 (2410.24164) | "pretrains on more than 10,000 hours of robot data" | "pre-training on over 10,000 hours of robot data" | Correct |
| LingBot-VLA (2601.18692) | "about 20,000 hours from nine dual-arm platforms, with success rates still rising" | "around 20,000 hours ... from 9 popular dual-arm robot configurations"; "no signs of saturation even at the 20,000-hour mark" | Correct |
| MimicGen (2310.17596) | "multiplies 200 human demonstrations into 50,000 by replaying trajectory segments in new object poses, but in simulation" | "over 50K demonstrations across 18 tasks ... from less than 200 human demos", 2 simulators and one physical arm | Correct; "in simulation" is slightly too strong since one real-arm task exists |
| FieldGen (2510.20774) | "provides only a 2.47x increase over a 2hr training example" | 2.47x is the increase in Collection Time Ratio (66.73 percent against 27.07 percent for teleoperation), an operator-effort metric; throughput rose 2.11x (1203 against 569 frames per minute); no "2hr training example" appears | Wrong: the number is misattributed |
| "an hour of egocentric video costs anywhere between 3 to 15 USD" / "8 - 15 USD per hour" | Intro and Section 5 | None of the six references gives a per-hour rate | Uncited, and the two figures disagree with each other |

### 4.2 Abstract, against the four-beat pattern

`review/reference-abstracts.md` found that all six abstracts follow problem, system, one scale number, one downstream robot result with a number. Draft 5's abstract has the problem (two sentences) and the system (three sentences). Its scale beat is "hundreds of permutations", with no number, and its result beat is "robust realistic permutions" and "powerful and economical ... scalable", with no number and no robot. Draft 4's abstract D, which Skyler's own `abstract.txt` was revised into, has the scale beat (116 clips, 72 per clip, 64 rendered, 20 GPU-minutes) and replaces the missing fourth beat with the measured boundary (ΔE 35 against 75, no motion from Predict2). Draft 5 goes back to the `abstract.txt` wording that D corrected.

### 4.3 Results section, against how the references write theirs

`results.md` Part 1 lists what the six Results sections share: the protocol is stated in full before the first result; variance is reported somewhere; negative numbers get a hypothesis in the same paragraph; no projection stands as a result. Draft 5's Results opens with a false count ("thousands of clips"), states the hardware and per-clip times (good), omits what was run (64 renders of 10 clips, 2 Predict2), omits the evaluation protocol beyond "every variant was inspected", reports no number for any render, and gives a hypothesis for the pillow failure ("poor image segmentation ... Canny edge-gradient parameters") that names the wrong component: segmentation is SAM2, and the retained pillow mask covers about 2 percent of the frame, which is the measured evidence.

## 5. Internal consistency of draft 5

Pairs of statements inside draft 5 that cannot both be true.

| A | B | Note |
|---|---|---|
| "splitting a 10 min video ... into 116 individual 15-second clips" (Method) | "From 3, 10-minute video examples, we used our workflow to create 116 clips" (Sec. 5) and "29 minutes of source data" | 116 x 15 s = 29 min, so neither one 10-minute video nor three can be the source if clips are at most 15 s and footage is dropped. Confirmed: 8 recordings, about 80 min raw. The "One 10-minute video became 4 hours" sentence only works with 8 recordings (35 h / 8 = 4.4 h), so "3" is most likely a typo for 8 |
| "3 to 15 USD" per hour (Intro) | "8 - 15 USD per hour" (Sec. 5) | Pick one and cite it, or attribute it to Innodata's own collection experience |
| "effectively x10 the amount of trainable data" (Intro) | "8,352 synthetic video variations ... from 29 minutes" (Sec. 5), i.e. 72x | Same paper, two multipliers |
| "hundreds of permutations" (Abstract) | "thousands of synthetic training clips" (Conclusion) | Pick the confirmed numbers: 72 admissible per clip, 64 rendered, 8,352 capacity |
| "70 Plausible variants per 15 second clip" (Sec. 3.1) | "72 variations per clip" (Sec. 5) | 72 is confirmed |
| "150 word caption" (Sec. 3.2) | Prompt-writer instruction limits prompts to under 300 words (`prompt-for-cosmos-transfer.txt`) | VERIFY the typical prompt length; the bucket prompt is the one to count |
| Rule 2: the preservation clause "protects non-target objects"; before it "bucket turning blue" was observed (Sec. 3.2) | Fig. 6 and its caption: bucket to blue, rag to blue, wall and lighting changed, under the prompt that contains the clause | The clause did not protect them; the leakage table says by how much |
| Sec. 3.3 item 4: the mask gives "clearly defined classification to which pixels the model can change" and lets us render "without affecting the neighboring objects" | Fig. 6 and Fig. 7, where neighbouring objects change | The mask is a soft control at seg weight 0.175; the deck's "painter's tape" overstatement, already corrected in drafts 1, 3 and 4, has come back |
| Fig. 6 caption: "varying the skin color of the human" listed alongside the intended recolor | Sec. 3.2 rule 2 and the bucket prompt, which asked for the countertop only | The skin-tone shift was leakage, not a variation, and listing it as one is both wrong and a sentence a reviewer will stop on |
| "Cosmos Predict" reasoning stack (Method para 3) and "Cosmos Reason, a Vision-Language-Action (VLA) model" (para 4) described as two consecutive steps | Fig. 2 and the abstract: Cosmos 3 Nano | One reasoning step ran, on the first frame, with the reasoning tower of Cosmos 3 Nano, a vision-language model. Neither Cosmos Predict nor Cosmos Reason was the reasoner, and VLA is the wrong class |
| Fig. 8 text: cord "looked like spaghetti", "gaining linear mass and length" | Fig. 8 image: two visually identical frames; confirmed outcome "no visible motion" | Either the spaghetti frames exist and should be shown, or the text should say what the figure shows |

## 6. Register, against the project rules (CLAUDE.md Section 3)

Strike-list words present: "leverages" (Abstract), "leveraging" (Abstract, Intro), "leverage" (3.2), "robust" (Abstract), "robustness" (Intro, 3.3), "powerful" (Abstract), "Additionally" (3.2, Conclusion), "Lastly" (3.2, Conclusion), "It should be noted" (3.2), "critical" (3.1), "exceptional" (3.2), "Surprisingly" (Results), "cohesive and practical solution" (Sec. 5), "meaningful solution" (Intro).

Rhetorical questions in body text: three ("how does this affect the outcome of the robot training policy?", "Can we generate realistic permutation variants ...?", and the closing sentence of the Conclusion). "Why?" inside rule 3 is a fourth.

Other patterns: the title is in capitals and the headings carry numbers and colons, which the LNCS template will replace; "In this step, we use" and "This paper describes" are heading restatements; "etc…" and "x10" and "4-8mins" are note-form; the abstract's last sentence is self-praise in the exact shape the rules warn against ("powerful and economical", "scalable"). Three-item lists are natural here (three prompt rules) and not a tell. Paragraph lengths vary, which is good.

Spelling and typing to fix: PhysicalAI (twice), mini-4o / Mini-4o, permutions (twice), acceptables, Onotology, objects,states, "clutter _", lightning, contests, dextrous, sows, "Chat GPT 4o mini", "a A100", "we're", "it's" (twice), "[cite EgoScale].Authors", "Egoscale".

## 7. Verdict

Draft 5 has the right order (problem with the scaling papers, the running example, three stages, success then failure, cost, open question) and a voice that fits the venue. It is missing the evidence that drafts 1, 3 and 4 built and that the thesis rests on: the count table, the weights, the generation settings, the mask equation, the leakage table and the plain statements that 64 clips were rendered, no policy was trained and no baseline was run. In their place it has a cost claim that the arithmetic contradicts and a reading of Fig. 6 that calls the main negative result a feature.

A reviewer who knows MimicGen will recognise the closing phrase of the abstract. A reviewer who knows EgoScale or FieldGen will find the numbers misread. A reviewer who reads Section 3.3 and then looks at Fig. 7 will find the mask claim contradicted by the paper's own figure. None of these needs new experiments to fix; the material exists in `draft-4-skyler/results-revised.md`, `closing-the-gap.md` and `methodology.md`, and the shore-up file lists what to move and what to change.

Recommendation: keep draft 5's skeleton and voice, restore the evidence from draft 4 (Table 1 count, the weights table, the leakage table, Eq. 1 or its prose equivalent), replace Section 5 with the `closing-the-gap.md` rewrite, and fix the citations. That yields a paper whose thesis is the one the repo supports: appearance variation is now cheap to propose and render, task-grounded by construction, and not yet contained; action generation is unsolved; whether the variants help a policy is the open experiment.
