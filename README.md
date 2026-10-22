# AIPR 2026 paper: Synthetic Video Generation for Robot Learning Using World Foundation Models

Working repository for the AIPR 2026 manuscript (Springer LNCS proceedings, final paper due 22 October 2026 via Springer Meteor). Authors: Shrey Jha, Skyler Saucedo, Frank Tanner (Innodata).

**Current manuscript: the 22 October version** (`oct-22/`), as `oct-22/AIPR 2026 Paper-oct22.pdf` (LNCS, 9 pages), `oct-22/AIPR 2026 Paper-oct22.docx` (for collaborative editing) and `oct-22/AIPR 2026 Paper-oct22.md`. It is the 21 October revision with the mechanical fixes applied, the author block in the style of the accepted AIPR 2025 papers, keywords, a Disclosure of Interests, the three uncited references removed and the list renumbered, the EgoScale and cost paragraphs corrected, and the figures rebuilt and placed in reading order. The full text is reproduced in Section 4 below; what changed and when is in Section 6; what the authors still owe is in `oct-21/oct-21-status-and-todo.md` and `oct-21/oct-21-copyedit.md`.

## 1. Directory structure

```
.
├── claude-drafts/                 drafts 1 to 6 and their LaTeX sources
│   ├── draft-1/                   compiled draft 1 (main.pdf) with its sections, figures, refs.bib
│   ├── draft-2/                   compiled draft 2 (main-v2.pdf)
│   ├── draft-3/                   compiled draft 3 (main.pdf)
│   ├── draft-4-skyler/            draft 4: section ideations in Markdown, several variants per section
│   ├── draft-5/                   draft 5 PDF, word-for-word transcription, analysis, shore-up list, figures/
│   ├── draft-6/                   draft 6 Markdown (draft 5 structure, confirmed numbers, LNCS citations), figures/
│   ├── paper/                     LaTeX source of draft 1 (LNCS); scripts/leakage_metric.py
│   ├── paper2/                    LaTeX source of draft 2 (slide-sequence outline)
│   ├── paper3/                    LaTeX source of draft 3; build.sh
│   └── paper3v2/                  LaTeX copy of draft 3 reserved for typesetting; build.sh
├── policy-vs-data-amount/         data-scaling claims compiled from the six reference papers
│   ├── data/                      one CSV per paper (EgoScale, LingBot-VLA, pi0, Lin et al., MimicGen, FieldGen)
│   ├── figures/                   policy_vs_data_amount.{pdf,png} (the paper's Fig. 1) and the two half figures
│   ├── make_plots.py              draws the figures from the CSVs; writes figures/fits.json
│   └── README.md                  claims table, figures, our fits, caveats
├── references/                    the six reference papers (arXiv PDFs)
├── review/                        analyses of the source material
│   ├── images/                    24 slide renders and 25 images extracted from the deck; _media-index.csv
│   ├── leakage/                   masked color-difference measurement on the bucket clip; mask coverage check
│   ├── answers-from-shrey-notes.md  transcription of Shrey's answers to the open items
│   ├── assumptions.md             working assumptions and their status
│   └── reference-abstracts.md     how the six reference abstracts are built
├── skyler-first-draft/            draft 7 (18 October)
│   ├── AIPR 2026 Paper-draft-7.pdf  the Google Docs export
│   ├── main.pdf                   draft 7 typeset in LNCS, word for word
│   ├── paper7/                    LaTeX source of main.pdf (main.tex, figures/, build.sh)
│   ├── draft-7-review.md          analysis and shore-up list for draft 7
│   ├── review/                    the review as .tex, .pdf and .docx
│   └── build-review.sh            builds the review into the three formats
├── oct-19/                        Skyler's 19 October export, transcribed; oct-19-revised.md (uncited refs removed,
│                                  citations renumbered, reasoner named consistently); oct-19-diff.md; figures/
├── oct-21/                        the 21 October revision
│   ├── Shrey et al AIPR 2026 - first draft-revisions.pdf  the Google Docs export
│   ├── Instructions+for+Authors+PDF.pdf  Springer's LNCS author instructions
│   ├── shrey-refs                 Shrey's reference audit (its numbering is not the manuscript's)
│   ├── AIPR 2026 Paper-updated.{md,docx,pdf}  the revision word for word in LNCS, verified non-arXiv references
│   ├── updated/                   LaTeX source (main.tex), build.sh, build/
│   ├── figures/                   the seven figures used by the LaTeX and the markdown
│   └── oct-21-status-and-todo.md  what was done on 20 and 21 October, reference verification table, to-do list
├── oct-22/                        the 22 October version (current)
│   ├── AIPR 2026 Paper-oct22.{md,docx,pdf}  the manuscript: markdown, Word for editing, LNCS PDF
│   ├── paper/                     LaTeX source (main.tex), build.sh (PDF via pdflatex, DOCX via pandoc)
│   ├── figures/                   the seven figures as used (fig6-reversal-oct22, fig7-variants-oct22 are composites)
│   ├── fig6.png                   Skyler's cord-winding variant frame (right panel of Fig. 6)
│   ├── alt-text.csv               alt text for every figure, for Springer's accessibility file
│   └── KlawaTanner_FinalManuscriptFormatted.pdf  Frank's accepted AIPR 2025 paper, the format exemplar
├── answers-from-shrey.pdf         Shrey's answers, including the Cosmos 3 Nano ontology instruction
├── prompt-for-cosmos-transfer.txt the GPT-4o mini prompt-writer instruction
├── technical-details.md           every number used in the drafts, with source and confidence
├── SynthethicVideoGenerationForWorldFoundationModels-Review.md  slide-by-slide review of the deck
├── CLAUDE.md                      writing rules for the manuscript
└── README.md                      this file
```

Not in the repo (ignored): the original `.pptx` deck, embedded `.mp4` clips, `.zip` archives for Overleaf, and LaTeX build directories.

## 2. Drafts at a glance

| Draft | Where | Form | What it is |
|---|---|---|---|
| 1 | `claude-drafts/paper/`, `claude-drafts/draft-1/main.pdf` | LNCS LaTeX, 19 pp | Full paper with corrected numbers, four appendices |
| 2 | `claude-drafts/paper2/`, `claude-drafts/draft-2/main-v2.pdf` | LNCS LaTeX, 12 pp | Slide-sequence outline using the deck's own numbers |
| 3 | `claude-drafts/paper3/`, `claude-drafts/draft-3/main.pdf` | LNCS LaTeX, 9 pp | Draft 1's structure and bibliography with the talk's narrative and imagery |
| 4 | `claude-drafts/draft-4-skyler/` | Markdown | Section ideations reviewed with Skyler one section at a time |
| 5 | `claude-drafts/draft-5/` | Google Docs PDF, 10 pp | Skyler's draft; transcribed word for word, analysed, shore-up list |
| 6 | `claude-drafts/draft-6/` | Markdown | Draft 5's structure with the confirmed numbers, numbered citations with URLs, the combined data-scaling figure, a schema-complete Fig. 5 JSON |
| 7 | `skyler-first-draft/` | Google Docs PDF, 12 pp; LNCS PDF, 11 pp | Draft 5 with Fig. 1, the reference list and part of the background paragraph adopted from draft 6 |
| 8 | `oct-19/` | Google Docs PDF, 12 pp; Markdown | Skyler's 19 October export. `oct-19-revised.md` removes the six never-cited references, renumbers citations by first appearance and names the reasoner as Cosmos 3 Nano throughout |
| 9 | `oct-21/` | Google Docs PDF, 10 pp; LNCS PDF, 10 pp; DOCX; Markdown | The 21 October revision word for word in LNCS; all 21 references on verified first sources (proceedings pages, DOIs, NVIDIA Research pages), no arXiv links |
| 10 | `oct-22/` | LNCS PDF, 9 pp; DOCX; Markdown | Current. The 21 October text with mechanical fixes, Frank-style author block, keywords, disclosure, 18 renumbered references, corrected EgoScale and cost paragraphs, Fig. 6 and Fig. 7 rebuilt, figures placed in reading order with no stretched gaps |

## 3. Building

MiKTeX is installed per user and is not on PATH; each `build.sh` sets PATH to the MiKTeX binaries plus the system directories (the MiKTeX format builder aborts otherwise).

```
bash oct-22/paper/build.sh                   # current manuscript: PDF (pdflatex) and DOCX (pandoc) into oct-22/
bash oct-21/updated/build.sh                 # 21 October version: PDF (pdflatex) and DOCX (pandoc) into oct-21/
bash skyler-first-draft/paper7/build.sh      # draft 7 in LNCS, writes skyler-first-draft/main.pdf
bash skyler-first-draft/build-review.sh      # the draft 7 review as .tex, .pdf and .docx (pandoc + pdflatex)
bash claude-drafts/paper3v2/build.sh         # the LaTeX copy reserved for typesetting the final paper
python policy-vs-data-amount/make_plots.py   # regenerates Fig. 1 from the CSVs
```

---

## 4. Current manuscript: the 22 October version, word for word

Reproduced from `oct-22/AIPR 2026 Paper-oct22.md`, which is the text of the LNCS PDF. Dollar amounts are written as USD. Figure images are those in `oct-22/figures/`. The author block, keywords and Disclosure of Interests are as submitted; the affiliation lines have no city or country and there is no corresponding email, matching the accepted AIPR 2025 papers.

## Synthetic Video Generation for Robot Learning Using World Foundation Models

Shrey Jha¹ (ORCID 0009-0003-5044-4187), Skyler Saucedo² (ORCID 0009-0005-7005-7736), and Franklin Tanner³ (ORCID 0009-0003-6814-2291)

¹ Innodata, Physical AI Intern
² Innodata, Robotics and Physical AI Solutions Architect
³ Innodata, VP Robotics and Computer Vision

### Abstract

Training successful humanoid robotic manipulation policies within the space of Physical AI is bottlenecked by real-world data limitations in the quantity and diversity of environments. Achieving acceptable completion scores for even the most straightforward tasks may require tens of thousands of hours of training data. The training data must include sufficient diversity for different objects, surfaces, and lighting to prevent model overfitting and promote generalization. In this paper, we describe a pipeline that leverages NVIDIA Cosmos world foundation models, along with large language models (LLMs) like OpenAI's GPT-4o mini, to generate variations of real egocentric video clips while keeping the recorded actions, scaling a single video into hundreds of permutations. Source recordings are first split into short clips with NVIDIA Cosmos Curate. Our method then uses NVIDIA Cosmos 3 Nano to produce an ontology of each clip: the task, each object's role in it, and plausible variations. GPT-4o mini then writes a prompt to generate scene permutations. Our method employs traditional computer vision techniques like boundary detection and image segmentation, using Canny edge detection coupled with Segment Anything 2 (SAM 2) to locate the objects we wish to permute, while Cosmos Transfer 2.5 renders the items, maintaining realism within the video. This paper describes our process and findings, where structured reasoning about a scene produces robust, realistic permutations. We outline limitations and provide best practices for leveraging these tools, demonstrating that this powerful and economical approach is scalable when solving problems in robot learning.

**Keywords:** Synthetic data generation, World foundation models, Egocentric video, Robot learning, Data augmentation

### 1 Introduction

Training humanoid robots to perform everyday household tasks requires large-scale egocentric data collection. Where humanoid robotic policy training and effectiveness are quantified, the consensus within the Physical AI community is that more training data is required, on the order of tens of thousands of hours, and that the diversity of objects within the space (defined below as the ontology) matters for policy robustness. As such, the mean acceptable score, defined as the robot's ability to successfully complete the task it was trained on, scales logarithmically with the hours of egocentric video [1]. Zheng et al. pretrain a vision-language-action (VLA) model on 20,854 hours of egocentric human video and report an average task completion score of 0.71 at that scale, the largest they tested, with performance still rising [1]. The π0 model pretrains on more than 10,000 hours of robot data to perform similar tasks [2]. LingBot-VLA pretrains on about 20,000 hours from nine dual-arm platforms, with success rates still rising at that scale [3].

Lin et al. collected 40,000 demonstrations and found that a single-task policy's generalization follows a power law in the number of training environments and objects [4]. While a corpus of 20,000 hours may be needed to reach that level of performance, an hour of egocentric video costs between 3 and 25 USD to collect, so a corpus of this magnitude can become cost-prohibitive for physical AI startups and academic labs.

While there are labs addressing this bottleneck, only a handful of solutions offer practical support. MimicGen can simulate 50,000 samples from 200 real human demonstrations by replaying trajectory segments in new object poses, but in simulation and for robot trajectories, not video [5].

We propose a method that can effectively increase the amount of trainable data. Recordings are first cut into short clips with NVIDIA Cosmos Curate, and a world foundation model then reads the first frame of each egocentric clip and provides a structured ontology of the scene. Leveraging classical computer vision techniques, we identify the items within the ontology and permute their attributes (color, texture, location), effectively creating video variants that describe the same task but provide the diversity a policy needs to learn tasks concerning dexterous hand motions within common environments, like living rooms, kitchens, and office spaces.

#### 1.1 Background

World foundation models are large-scale artificial intelligence systems trained to understand, simulate, and predict the physical world, including how objects move, interact, and follow the laws of physics [6]. NVIDIA Cosmos consists of three models: Predict forecasts future frames from text, an image, or a video [7]; Transfer adapts a video across environments under multi-control conditioning on depth, segmentation, edge, and blurred-RGB maps [8, 9]; Reason is a vision-language model for physical scene understanding [10]. Alongside the models, Cosmos Curate is the platform's video curation pipeline, which splits recordings at shot boundaries and prepares clips for the models [6]. Cosmos 3 folds the three models into one, with an autoregressive subnetwork that reasons about a scene and a diffusion-based subnetwork that generates video, audio, and actions conditioned on that reasoning [11].

### 2 Method

![Block diagram of the pipeline: an egocentric clip goes to the Cosmos 3 Nano reasoning tower, which produces an ontology; GPT-4o mini filters it and writes a prompt; SAM 2 produces tracked masks; Canny, depth, and blur produce control maps; Cosmos Transfer 2.5 renders the variant clip.](oct-22/figures/fig2-pipeline.png)

*Fig. 1. The Pipeline*

Fig. 1 shows the pipeline we are using to permute the objects in the ontology of an egocentric video.

First, the original egocentric video clip (V) is prepared with NVIDIA's Cosmos Curate. Curate applies TransNet V2 shot-boundary detection, splitting a 29 min video of egocentric data into 116 individual 15-second clips, downsampled to 4 fps at 854×480. Curate uses TransNet V2, a small convolutional neural network trained to detect scene transitions. TransNet V2 is fast and accurate on standard shot-detection benchmarks [12]. The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano [11, 13], a vision-language model that returns a structured description of the task, task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations that are plausible for the task. This structured understanding (scene, objects, attributes, actions) of the observed scene is what we define as the ontology. We feed the ontology (structured JSON) to GPT-4o mini [14] to write the text prompt that Cosmos Transfer 2.5 uses for variant video generation.

Four guidance maps are generated to preserve item edges, depth, color, and segmentation. Segmentation masks of all items are generated using SAM 2 [15] to maintain item integrity while preserving the task at hand. Finally, Cosmos Transfer 2.5 [9, 16] renders a synthetic variant (V') of the video with the same task, action, and ontology of items, but with directed permutations of item attributes to increase visual diversity.

#### 2.1 Reasoning with Structured Ontologies

![First-person frame of a hand holding a white plastic bucket on a white countertop, with a crumpled cloth beside it.](oct-22/figures/fig3-source-clip.png)

*Fig. 2. Sample egocentric video, a person wipes a countertop with a towel and a bucket.*

As shown in Fig. 2, our example video consists of a white bucket on a white countertop, and the task is defined as follows: a human must use a washcloth from the bucket to clean the countertop. If we wish to train a robot policy on this cleaning task, we will need to augment portions of the video to increase the amount of training data to improve our average task completion score. If we decide to change the color of the bucket, countertop, or rags, does that permutation affect the outcome of the robot training policy? Whichever model is used, it must learn to associate objects with the broader actions and physical context they participate in: not just what they look like, but how they behave in the task. This requirement is why reasoning with structured ontologies is critical: we ask a model to understand the scene, objects, states, materials, lighting, and actions before anything else is varied, so that the permutations proposed for an object are physically plausible for the given task.

![Left: the bucket frame with five labelled bounding boxes (white plastic bucket, human hand, crumpled paper, white surface). Right: an excerpt of the JSON ontology listing the task, the bucket's role, robustness gaps, and common failure modes.](oct-22/figures/fig4-reasoning-output.png)

*Fig. 3. Reasoning output for the scene with object detection bounding boxes, along with the JSON ontology.*

Cosmos 3 Nano receives the first frame of the clip together with a fixed instruction, and returns a structured JSON record that defines the observed ontology (Fig. 3). Our pipeline asks for up to ten task-relevant objects, each with a bounding box, and for each object: its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with hands), and candidate variations along seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style). A parallel block records scene-level variations (lighting, viewpoint, room style, time of day, clutter) and a final block states what training on this clip could miss. Reasoning takes about 130 seconds per clip on one A100.

#### 2.2 From Ontology to Generation-Ready Prompts

In this step, we use OpenAI's GPT-4o mini [14] to prepare the prompt for Cosmos Transfer. We chose GPT-4o mini for its speed and low cost, averaging about 0.001 USD per 15-second clip. Additionally, GPT-4o mini provides reliable structured JSON output and adheres to the Cosmos caption schema. Lastly, GPT-4o mini is one of the most widely available LLMs in the market currently. It should be noted that we did not run a comprehensive comparison against other frontier models at the time.

From our work with this process, three prompt-engineering principles were discovered:

1. Repeat target attributes: "solid blue countertop", "vivid blue color". More repetition of the changed attribute helps reinforce the change. A single mention of "blue" is one token competing with everything else in the 150-word caption; repeating the attribute in different contexts puts more of the prompt's attention mass on the property to be modified.
2. Explicitly preserve unchanged elements: "Bucket and paper towels retain their original appearance". This preservation clause reinforces continuity and protects non-target objects. Prior to enforcing this clause, we observed evidence of leakage (the bucket turning blue despite prompting the color change of the counter).
3. Describe the result, not the change: to change the countertop color, the prompt should say "a person cleaning a solid blue countertop", not "change the white countertop to blue...". We conjecture this is because the model was trained on descriptive video captions rather than edit instructions, placing imperative prompts outside its training distribution.

#### 2.3 Guiding the Rendering

Before any object attributes are applied, we send Cosmos Transfer four control modalities from the source clip. Each control modality comes with tunable parameters to decide how strongly the variant is rendered.

1. Edge detection: We use Canny edge detection [17], as implemented in OpenCV.
2. Depth: The depth control is monocular depth video from Depth Anything V2 [18], which provides an emergent layer of pseudo-3-dimensional object spatial positioning.
3. Color for lighting: maintaining the overall color palette and continuity as we adjust light parameters. We use a bilateral blur of the input RGB frames.
4. Segmentation mask: All objects in the ontology are identified pixel by pixel. The mask provides a clearly defined classification of which pixels the model can change. If two or more objects spatially relate or overlap, or if there is occlusion, we can render the object in question without affecting the neighboring objects in the scene.

### 3 Results

Eight recordings of first-person videos of household chores were used to generate realistic permutation variants. Tasks were captured egocentrically with a head-mounted camera and include counter wiping, cloth folding, bed making, and cable wrapping. Each task ranges from 4 minutes to 8 minutes in duration. Our studies ran on Google Colab Pro+ notebooks (see appendix for source code) on an A100 80 GB. For Cosmos 3 Nano, the average reasoning time was 130 seconds per clip. Transfer renders averaged about 20 minutes, and Predict2 renderings took about 3.5 minutes. LLM inference by GPT-4o mini took only a few seconds per clip. Every variant was inspected to see how it compared to the matched source.

![Two frames labelled Old and New. Old: a hand holds a white bucket on a white countertop with a cloth beside it. New: the same pose with the countertop, bucket, and cloth rendered blue, a darker wall, and a ceiling light visible.](oct-22/figures/fig6-countertop-blue.png)

*Fig. 4. Converting the white countertop to blue, the rag to blue, the bucket to blue, and varying the skin color of the human.*

Fig. 4 shows that the resulting variant permutes the color of the objects in the ontology, while maintaining the hand pose and the bucket and countertop geometry. We observed that the cleaning motion observed in the before video is maintained by the variant, frame by frame. We also observed that the background wall and lighting have changed, increasing scene diversity.

![Two frames labelled Old and New. Old: hands stuff a white pillow on a wooden chair with patterned cushions. New: the pillow, the cushions, and the chairs are all rendered blue.](oct-22/figures/fig7-pillow-stuffing.png)

*Fig. 5. Adding stuffing to a chair pillow*

We see that adding complexity to objects can sometimes add unintended consequences to the variant scene. As observed in Fig. 5, we task the data collector to stuff a throw pillow for a chair. When we employed the pipeline to produce variants, our only request was that the color of the pillow change to blue. The variant not only changed the pillow blue but also changed the background chairs blue. We found that poor image segmentation results are the cause here, suggesting the need to fine-tune Canny edge-gradient parameters.

![Two frames. Left: the source clip, hands holding a white charger cable in front of a desk and bookshelf. Right: the variant prompted to wind the cord the other way, in which the cable has become a tangled, smeared loop across the desk.](oct-22/figures/fig6-reversal-oct22.png)

*Fig. 6. Directional Reversal Experiment*

We did observe some limitations in this process, particularly when requesting permutations in the physics of the scene. In Fig. 6, the data collector is taking a phone charger and winding the USB cord around the wall plug in a clockwise direction (with respect to the wall plug). Next, we ask the pipeline to wind the cord in the opposite direction, counterclockwise. Surprisingly, the resulting variant was unable to maintain this ask: the spooling wire looked like spaghetti, with the cord gaining linear mass and length at times. The hands do in fact maintain the same orientation as the original video, but the variant fails to maintain the physics, violating conservation of mass and continuity. Fig. 7 places the source desk clip and its appearance variant side by side.

![Two frames. Left: the source desk clip, hands holding a charger cable in front of a bookshelf. Right: the same scene with the desk and shelf objects rendered blue.](oct-22/figures/fig7-variants-oct22.png)

*Fig. 7. Desk clip: source (left) and appearance variant with desk and shelf recolored blue (right).*

### 4 Closing the Gap

From three 10-minute video examples, we used our workflow to create 116 clips to generate 72 variations per clip, producing 8,352 synthetic video variations, or about 35 hours of video from 29 minutes of source data. The number of permuted variants depends on the number of objects in the ontology available to change, along with what physical attributes are within the current limit of the NVIDIA World Model suite. One 10-minute video became 4 hours without a new scene or room generated. At the time of publication, the authors have not quantified how much of this synthetic data is useful.

Rendering costs about 0.25 USD per 15-second variant on a Colab Pro+ A100 (20 minutes of GPU time at roughly 0.75 USD per A100-hour as of 2026), plus about 0.03 USD per clip for reasoning and 0.001 USD in LLM tokens. What the pipeline buys is variation at scale: new colors, materials, and lighting on motion that has already been recorded, which Lin et al. identify as the quantity that moves generalization [4].

### 5 Conclusion

We describe a multi-model pipeline on NVIDIA Cosmos that turns a real, limited first-person dataset into task-grounded synthetic training variant clips for humanoid robotic policy training. This workflow provides a scalable solution for academics and practitioners who need more egocentric video to increase the average task completion score. We demonstrate how the workflow is capable of changing appearance for simpler scenes. However, more work must be done for complex scenes. Additionally, action-level changes (multiple tasks executed within the video) remain unsolved. Lastly, more questions need to be explored, such as does structured reasoning about a scene produce better variations than random augmentation? Overall, we have explored NVIDIA Cosmos models and their current capacity for synthetic video generation for egocentric household data.

**Disclosure of Interests.** The authors have no competing interests to declare that are relevant to the content of this article.

### References

1. Zheng, R., Niu, D., Xie, Y., Wang, J., Xu, M., Jiang, Y., Castañeda, F., Hu, F., Tan, Y.L., Fu, L., Darrell, T., Huang, F., Zhu, Y., Xu, D., Fan, L.: EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data. Technical report, NVIDIA (2026). https://research.nvidia.com/labs/gear/egoscale/
2. Black, K., Brown, N., Driess, D., et al.: π0: A Vision-Language-Action Flow Model for General Robot Control. In: Proceedings of Robotics: Science and Systems (RSS) XXI (2025). doi: 10.15607/RSS.2025.XXI.010. https://roboticsproceedings.org/rss21/p010.html
3. Wu, W., Lu, F., Wang, Y., Yang, S., Liu, S., Wang, F., et al.: A Pragmatic VLA Foundation Model. Technical report, Robbyant (2026). https://technology.robbyant.com/lingbot-vla
4. Lin, F., Hu, Y., Sheng, P., Wen, C., You, J., Gao, Y.: Data Scaling Laws in Imitation Learning for Robotic Manipulation. In: International Conference on Learning Representations (ICLR) (2025). https://proceedings.iclr.cc/paper_files/paper/2025/hash/88b7b2c896506daabc8d3fd587055167-Abstract-Conference.html
5. Mandlekar, A., Nasiriany, S., Wen, B., Akinola, I., Narang, Y., Fan, L., Zhu, Y., Fox, D.: MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations. In: Proceedings of the 7th Conference on Robot Learning (CoRL). Proceedings of Machine Learning Research, vol. 229, pp. 1820-1864. PMLR (2023). https://proceedings.mlr.press/v229/mandlekar23a.html
6. NVIDIA, Agarwal, N., Ali, A., et al.: Cosmos World Foundation Model Platform for Physical AI. Technical report, NVIDIA (2025). https://research.nvidia.com/publication/2025-01_cosmos-world-foundation-model-platform-physical-ai
7. NVIDIA: Cosmos-Predict2: A Suite of Diffusion-based World Foundation Models Available in 2B and 14B. Hugging Face model card (2025). https://huggingface.co/nvidia/Cosmos-Predict2-2B-Video2World
8. NVIDIA, Abu Alhaija, H., Alvarez, J., et al.: Cosmos-Transfer1: Conditional World Generation with Adaptive Multimodal Control. Technical report, NVIDIA (2025). https://research.nvidia.com/labs/cosmos-lab/cosmos-transfer1/
9. NVIDIA, Ali, A., Bai, J., et al.: World Simulation with Video Foundation Models for Physical AI. Technical report, NVIDIA (2025). https://research.nvidia.com/publication/2025-09_world-simulation-video-foundation-models-physical-ai
10. NVIDIA, Azzolini, A., Bai, J., et al.: Cosmos-Reason1: From Physical Common Sense to Embodied Reasoning. Technical report, NVIDIA (2025). https://research.nvidia.com/labs/cosmos-lab/cosmos-reason1/
11. NVIDIA: Cosmos 3: Omnimodal World Models for Physical AI. Technical report, NVIDIA (2026). https://research.nvidia.com/labs/cosmos-lab/cosmos3/
12. Souček, T., Lokoč, J.: TransNet V2: An Effective Deep Network Architecture for Fast Shot Transition Detection. In: Proceedings of the 32nd ACM International Conference on Multimedia (MM), pp. 11218-11221. ACM (2024). doi: 10.1145/3664647.3685517
13. NVIDIA: Cosmos3-Nano. Hugging Face model card (2026). https://huggingface.co/nvidia/Cosmos3-Nano
14. OpenAI: GPT-4o mini: Advancing Cost-Efficient Intelligence (2024). https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
15. Ravi, N., Gabeur, V., Hu, Y.T., et al.: SAM 2: Segment Anything in Images and Videos. In: International Conference on Learning Representations (ICLR) (2025). https://proceedings.iclr.cc/paper_files/paper/2025/hash/45c1f6a8cbf2da59ebf2c802b4f742cd-Abstract-Conference.html
16. NVIDIA: Cosmos-Transfer2.5: A Suite of Diffusion-based World-to-World Models. Hugging Face model card (2025). https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B
17. Canny, J.: A Computational Approach to Edge Detection. IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-8(6), 679-698 (1986). doi: 10.1109/TPAMI.1986.4767851
18. Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng, J., Zhao, H.: Depth Anything V2. In: Advances in Neural Information Processing Systems (NeurIPS) 37 (2024). https://proceedings.neurips.cc/paper_files/paper/2024/hash/26cfdcd8fe6fd75cc53e92963a656c58-Abstract-Conference.html

---

## 5. Supporting tables

The numbers behind every draft, with source and confidence, are in `technical-details.md`. The measured leakage result for the counter-wiping clip is in `review/leakage/README.md`. The data-scaling claims compiled for the data-scaling figure (removed from the manuscript on 21 October; see Appendix A), with our fits, are in `policy-vs-data-amount/README.md`. The list of what to fix in draft 7 before submission, with replacement text, is `skyler-first-draft/draft-7-review.md`. The reference verification table, the Springer requirements that apply to us, and the list of what the authors still owe before submission are in `oct-21/oct-21-status-and-todo.md`. The line-level copyedit of the 21 October text, with what was and was not applied on 22 October, is `oct-21/oct-21-copyedit.md`.

## 6. What changed on 20 and 21 October

- **EgoScale wording.** The reviewing editor flagged that EgoScale does not claim 20,854 hours per task. A full read confirmed it: the hours are a shared pretraining corpus over 6,015 tasks, per-task robot data is 100 demonstrations, and 0.71 is the completion score at the largest scale tested, not a ceiling. The 21 October revision fixed "needed per task" but still says "upper limits of ... 0.71" and "over 20k hours of video may be needed for a single task". Replacement text is in `oct-21/oct-21-status-and-todo.md`, Section 4.2.
- **Frank's question on "an emergent property of VLAs".** Reference [8] (the Predict2 model card) does list physics failures but says nothing about emergence, and Cosmos Transfer is a diffusion video model, not a VLA. The right source is the Cosmos platform paper, Sec. 5.3.2 and Sec. 9. The sentence was removed in the 21 October revision. The repo's records say the recovered Predict2 cable prompt asked for winding with the block fixed, not a reversal, and that both runs produced no visible motion; Shrey needs to confirm whether the "spaghetti" run exists.
- **Springer LNCS requirements** read from `oct-21/Instructions+for+Authors+PDF.pdf`: corresponding author with mandatory email, keywords, reference list matching the text exactly, DOIs encouraged, Disclosure of Interests statement, alt text for figures, signed license-to-publish, 6 to 11 pages for a short paper.
- **References.** All 21 entries moved off arXiv. Corrections to Shrey's audit: TransNet V2 is in ACM Multimedia 2024 with a DOI; pi0 is in the RSS 2025 proceedings with a DOI; the "OpenReview" hash for Lin et al. was the ICLR proceedings file id. Seven works (EgoScale, LingBot-VLA, FieldGen, the four Cosmos reports) have no peer-reviewed venue and are cited as technical reports or project pages. Every URL was fetched on 21 October; the OpenAI page blocks automated requests but is the canonical URL.
- **Open items for the authors** (full list in `oct-21/oct-21-status-and-todo.md`, Section 4): corresponding author email and marking; keywords; references 5, 13 and 14 are listed but no longer cited; Disclosure of Interests; whether the data-scaling figure (Appendix A) and the JSON ontology figure return; alt text; the EgoScale sentences; the cost-per-hour source and units; "3, 10-minute video examples" versus eight recordings; the Fig. 6 skin-colour caption; the missing appendix the Results section points to; the typos preserved word for word ("alette", "bluir", "Collab", "and,diversity", "the amount the amount").

## 7. What changed on 22 October

The 22 October version (`oct-22/`) starts from the 21 October text and applies, in this order:

- **Mechanical pass** from `oct-21/oct-21-copyedit.md`: the doubled "the amount", "alette", "bluir", "Collab", "and,diversity", "ego centric", "academia labs", "Egoscale", "et al,", subject-verb agreement, articles, a fragment and a comma splice, a dangling modifier; "Fig. N" throughout; SAM 2, TransNet V2, Depth Anything V2, lower-case "ontology", Cosmos Transfer 2.5 at first use, Cosmos 3 Nano in Results, currency as "N USD", acronyms expanded at first use, Canny cited for Canny rather than OpenCV, the Method's list of control maps matched to Sec. 2.3. Alt text for all seven figures in `oct-22/alt-text.csv`.
- **Header** in the style of Frank's accepted AIPR 2025 paper: superscript 1, 2, 3 on the names, ORCIDs as 7 pt superscripts, one affiliation line per author (Innodata, Physical AI Intern; Innodata, Robotics and Physical AI Solutions Architect; Innodata, VP Robotics and Computer Vision). No corresponding email, by decision.
- **Keywords**: Synthetic data generation, World foundation models, Egocentric video, Robot learning, Data augmentation. **Disclosure of Interests** added with Springer's standard sentence.
- **References**: FieldGen, ControlNet and Gen-1 removed as uncited; the remaining 18 renumbered in order of first citation. All on verified non-arXiv first sources with clickable URLs and DOIs.
- **EgoScale**: the Introduction now says Zheng et al. "report an average task completion score of 0.71 at that scale, the largest they tested, with performance still rising", replacing "upper limits of ... 0.71", and the cost sentence no longer reads the corpus as per task. See Appendix A for the plot behind this.
- **Cost paragraph** (Sec. 4) rebuilt from measured figures: about 0.25 USD per 15-second variant on a Colab Pro+ A100 (20 minutes at roughly 0.75 USD per A100-hour, the measured 7.52 compute units per hour at 0.10 USD per unit, as of 2026), plus about 0.03 USD per clip for reasoning and 0.001 USD in LLM tokens. The earlier 96 USD per hour used a 2024-era 1.20 USD per A100-hour, and the 0.12 USD LLM figure was the project total. The paragraph now states what the spend buys rather than claiming the pipeline is cheaper per hour than collection.
- **Wording**: "NVIDIA Cosmos world foundation models" and "three models" instead of "family"; Cosmos Curate introduced in the abstract, the introduction and the background before the Method uses it; "increasing scene diversity" instead of "adding more entropy as desired".
- **Figures**: Fig. 6 is the source panel of the original reversal figure beside Skyler's `fig6.png` frame, scaled uniformly (aspect 1.769 kept). Fig. 7 is the source desk clip beside its blue variant, two panels. Every figure is cited in the text (the reasoning-output figure was not). Figures 3, 5, 6 and 7 are placed exactly where they stand in the text, pages are ragged-bottom, and the reading order on pages 6 to 8 is Fig. 4, Results, Fig. 5, pillow paragraph, Fig. 6, reversal paragraph, Fig. 7, Closing the Gap. The stretched gaps that bottom-anchored floats had caused are gone.
- **Still open** (content the authors must settle; see `oct-21/oct-21-status-and-todo.md` Sec. 4 and `oct-21/oct-21-copyedit.md`): the three conflicting source-data counts and "one 10-minute video became 4 hours"; "producing 8,352 synthetic video variations" where 64 were rendered; whether the Fig. 6 render was prompted as a reversal and what the Fig. 5 prompt asked for; head-mounted versus handheld camera; the Fig. 4 caption treating skin-tone, wall and lighting changes as requested; Sec. 2.3's claim that the mask protects neighbors; Predict2 unintroduced in the Method; "(see appendix for source code)" with no appendix; the two rhetorical questions and the strike-list words; whether the Disclosure of Interests should name Innodata's data-collection business as the source of the 3 to 25 USD figure.

---

## Appendix A. The data-scaling figure removed on 21 October

Draft 7 and the 19 October revision opened with this figure as Fig. 1, cited in the introduction's argument that policy performance rises with hours of data and with the diversity of environments and objects. The 21 October revision dropped it (its figures run 2, 3, 4, 6, 7, 8, 9 in the source document, with 1 and 5 missing). It is kept here because it is the one visual that supports the introduction's scaling argument, and because the numbers in it were compiled and plotted by us from the five papers, so the figure is ours to reuse. Source CSVs, the plotting script and the caveats are in `policy-vs-data-amount/`; regenerate with `python policy-vs-data-amount/make_plots.py`.

![Policy performance against hours of data and against diversity, compiled from five papers](oct-19/figures/fig1-data-scaling.png)

*Policy performance against hours of data in five papers. (a) EgoScale: average task completion score on five dexterous tasks after pretraining on 1k to 20k hours of egocentric human video, with 100 robot demonstrations per task held fixed; values read from Fig. 5 of EgoScale; the dashed line is our log-linear fit, not one reported by EgoScale. (b) LingBot-VLA: average success and progress rate over 25 tasks on three dual-arm robots after pretraining on 3k to 20k hours of robot data, read off its Fig. 5. (c) pi0: average task progress over six tasks against hours of fine-tuning data, for the pretrained model, from scratch, and Diffusion Policy, read off its Fig. 11. (d) Lin et al. 2025, Mouse Arrangement: normalized score on unseen environments and objects against the number of training environments, objects, or environment-object pairs, drawn from the published power-law fits. (e) FieldGen: success rate, mean of four pick tasks, against wall-clock collection time for teleoperation and for FieldGen.*

The data points and fits behind the figure (from `policy-vs-data-amount/data/` and `policy-vs-data-amount/figures/fits.json`):

| Panel | Source | Data | Our fit or reading |
|---|---|---|---|
| (a) EgoScale | Zheng et al. 2026, Fig. 5 right | 0.30, 0.45, 0.48, 0.57, 0.71 at 1k, 2k, 4k, 10k, 20k hours | score = -0.53 + 0.123 ln(hours), R² = 0.96. EgoScale itself fits a log-linear law to validation loss (R² = 0.998), not to the score |
| (b) LingBot-VLA | Wu et al. 2026, Fig. 5 | success and progress rates at 3k, 6k, 13k, 20k hours, read off the plot | success = -0.60 + 0.095 ln(hours), R² = 0.82 |
| (c) pi0 | Black et al. 2025, Fig. 11 | task progress at 1, 5, 10 hours of fine-tuning data, read off the plot | no fit; pretrained pi0 reaches 0.87 at 10 hours |
| (d) Lin et al. | Lin et al. 2025, published power laws | objects: 1 - 0.826 x^-0.697; environments: 1 - 0.827 x^-0.466; env-object pairs: 1 - 1.263 x^-0.683 | at 32: objects 0.93, pairs 0.88, environments 0.84 |
| (e) FieldGen | Wang et al. 2025 | success at 4 to 20 minutes of collection, Diffusion Policy and RDT-small | at 20 min: FieldGen 0.98 / 0.94, teleoperation 0.65 / 0.56 |

What the figure supports, and what it does not: the hours-versus-score panels show a log-linear trend with no saturation in the tested range, which is the premise of the paper's cost argument. They do not show that 20k hours are needed per task; in EgoScale the hours are shared pretraining and the per-task data is fixed. Panel (d) is the strongest support for the pipeline, because it shows that diversity of environments and objects, not repeated demonstrations, is what moves generalization, and diversity is what the pipeline produces. If the figure returns to the manuscript, the caption above is the corrected one; the draft 7 caption said "three papers" for five panels and did not say the fit was ours.
