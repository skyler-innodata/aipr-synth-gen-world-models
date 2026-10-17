# Reference abstracts (references/) and what they share

Read 2026-10-17 to calibrate the draft 4 abstract. One line on each, then the pattern.

| File | Paper | Problem sentence | System | Scale number | Downstream result |
|---|---|---|---|---|---|
| 2310.17596 | MimicGen (Mandlekar et al., CoRL 2023) | Human demos are costly to collect | Adapts a few demos to new contexts in simulation | 50K demos from 200 human demos, 18 tasks | Policies trained on it succeed at long-horizon tasks; "compares favorably to collecting additional human demonstrations" |
| 2410.18647 | Data Scaling Laws in Imitation Learning (Lin et al., ICLR 2025) | Do scaling laws exist in robot manipulation? | Empirical study, not a system | 40,000 demos, 15,000 rollouts | Power law in number of environments and objects; diversity matters more than demo count; 90% success in novel environments |
| 2410.24164 | pi0 (Physical Intelligence, 2024) | Data, generalization and robustness block general robot policies | VLA with flow-matching action expert on a VLM | Large cross-embodiment dataset (no number in abstract) | Laundry folding, table cleaning, box assembly |
| 2510.20774 | FieldGen (Wang et al., 2025) | Scale vs diversity vs quality trade-off in data collection | Pre-manipulation trajectories generated from an attraction field; humans do the fine phase | Not in abstract (fig: 6 min vs 2 min per collection) | Higher success and stability than teleoperation baselines |
| 2601.18692 | LingBot-VLA (Wu et al., 2026) | A VLA must generalize across tasks and platforms at acceptable cost | VLA pretrained on real dual-arm data | 20,000 hours, 9 robot configurations, 100 tasks x 4 platforms | "Clear superiority over competitors"; 261 samples/s training throughput |
| 2602.16710 | EgoScale (Zheng et al., NVIDIA, 2026) | Can large-scale egocentric human data support dexterous manipulation? | VLA pretrained on egocentric human video, then human-robot mid-training | 20,854 hours of egocentric video | Log-linear scaling law; +54% success over no-pretraining baseline on a 22-DoF hand |

## The pattern

Every abstract follows the same four beats: the data problem in one or two sentences; the system or study in two or three; one number that establishes scale; and a downstream result on a robot, with a number (success rate, improvement over baseline, or a scaling law). None of them spends more than a clause on limitations. The number that carries each abstract is the scale number paired with the policy result: 50K from 200 and then trained policies; 20,854 hours and then +54%.

## What this means for our abstract

- Our scale beat is real and should be stated with the same specificity: 116 clips, 72 admissible variations per clip, 64 rendered, 20 GPU-minutes per render. "Thousands" is an extrapolation (116 x 72 = 8,352) and must be labeled as capacity.
- Our fourth beat does not exist. No policy was trained on the output (deck slide 18 notes: "right now everything is qualitative"). The abstract therefore has to pivot on what we did measure: the leakage numbers and the action no-op. Phrased honestly this reads as a boundary-finding paper, which is a legitimate shape for a workshop paper, but it cannot borrow MimicGen's closing claim ("compares favorably to collecting additional human demonstrations") because that claim was earned by a training run.
- Two of the references argue for us. The data scaling laws paper finds that diversity of environments and objects matters more than the number of demonstrations, which is exactly the premise behind generating appearance variants. EgoScale establishes egocentric human video as a training source at scale, which is the kind of data we start from. Both belong in the Introduction's first two paragraphs.
- MimicGen is the closest structural analog: a small set of human demonstrations multiplied into a large synthetic set. The difference is that MimicGen multiplies trajectories in simulation and we multiply appearance in real video. That contrast is worth one sentence in Related Work.
- The register of these abstracts is plainer than it looks. They state numbers and let them argue. They do not use "primer", "best practices" or "powerful and economical" except MimicGen, whose closing phrase ("a powerful and economical approach towards scaling up robot learning") is backed by a cost comparison against human demos.
