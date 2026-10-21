# Changes from oct-19-manuscript.md to oct-19-revised.md

Three kinds of change were made: the six never-cited references were removed, citation numbers were made consistent with order of first appearance, and the Method now names the reasoning model consistently as Cosmos 3 Nano (confirmed by Shrey on 19 October) with the Cosmos3-Nano model card cited where the model is used. Nothing else in the prose was touched. The raw unified diff is at the end of this file.

## 1. Itemised changes

| # | Location | Before | After | Why |
|---|---|---|---|---|
| 1 | Fig. 1 caption, panel (e) | "for teleoperation and for FieldGen [6]" | "for teleoperation and for FieldGen [5]" | FieldGen is first cited here, before MimicGen is cited in the body, so FieldGen takes number 5 and MimicGen number 6. |
| 2 | Introduction, paragraph beginning "While there are labs addressing this bottleneck" | "not video [5]. FieldGen ... over a 2hr training example [6]." | "not video [6]. FieldGen ... over a 2hr training example [5]." | Same swap as item 1. |
| 3 | Sec. 3, Cosmos Curate paragraph | "standard shot-detection benchmarks. [21]" | "standard shot-detection benchmarks. [15]" | Renumbering. TransNetV2 is the first new citation after the Background, so it becomes 15. |
| 4 | Sec. 3, reasoning paragraph | "The first frame of each clip is passed to the reasoning stack of Cosmos Predict, a Vision Language Model that returns ..." | "The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano [12, 16], a vision-language model that returns ..." | Cosmos Predict is the video generation family, not a vision-language model, and the sentence had no citation. The reasoner was Cosmos 3 Nano, as the Abstract already says. Cites the Cosmos 3 report [12] and the Cosmos3-Nano model card [16], which was previously listed but never cited. |
| 5 | Sec. 3, paragraph beginning "Next, the clip is fed to Cosmos Reason" | "Next, the clip is fed to Cosmos Reason, a Vision-Language-Action (VLA) model that provides a structured understanding (scene, objects, attributes, actions) of the observed scene which we define as the Ontology. We feed the Ontology (structured JSON) to GPT-4o mini [23], ..." | "This structured understanding (scene, objects, attributes, actions) of the observed scene is what we define as the Ontology. We feed the Ontology (structured JSON) to GPT-4o mini [17], ..." | The paragraph described the same reasoning step a second time under a third model name (Cosmos Reason), which was not the model used, and labelled it a VLA. The duplicate lead-in was removed. GPT-4o mini renumbered 23 to 17. |
| 6 | Sec. 3, guidance maps paragraph | "SAM2 [24]" and "Cosmos Transfer [10,25]" | "SAM2 [18]" and "Cosmos Transfer [10, 19]" | Renumbering. |
| 7 | Sec. 3.1, paragraph after Fig. 4 | "Cosmos reasoning receives the first frame of the clip" | "Cosmos 3 Nano receives the first frame of the clip" | Name the model consistently with the Abstract and Sec. 3. |
| 8 | Sec. 3.2, first sentence | "GPT-4o mini [23]" | "GPT-4o mini [17]" | Renumbering. |
| 9 | Sec. 3.3, item 1 | "OpenCV [26]" | "OpenCV [20]" | Renumbering. |
| 10 | Sec. 3.3, item 2 | "DepthAnything V2 [27]" | "DepthAnything V2 [21]" | Renumbering. |
| 11 | References | 27 entries | 21 entries; original entries 15 to 20 deleted, original 22 (Cosmos3-Nano) kept and now cited, remaining entries renumbered (map below) | Entries 15 (RT-2), 16 (OpenVLA), 17 (Open X-Embodiment), 18 (Tobin et al. domain randomization), 19 (ROSIE) and 20 (GenAug) were never cited in the text. |
| 12 | Header note under the author line | Transcription note | Revision note | Describes the file. Not part of the manuscript. |

The Abstract is unchanged: it already named Cosmos 3 Nano.

## 2. Reference renumbering map

| Old | New | Work |
|---|---|---|
| 1 | 1 | EgoScale |
| 2 | 2 | pi-zero |
| 3 | 3 | LingBot-VLA |
| 4 | 4 | Lin et al., Data Scaling Laws |
| 5 | 6 | MimicGen |
| 6 | 5 | FieldGen |
| 7 | 7 | Cosmos World Foundation Model Platform |
| 8 | 8 | Cosmos-Predict2 model card |
| 9 | 9 | Cosmos-Transfer1 |
| 10 | 10 | World Simulation with Video Foundation Models (Predict 2.5 / Transfer 2.5) |
| 11 | 11 | Cosmos-Reason1 |
| 12 | 12 | Cosmos 3 |
| 13 | 13 | ControlNet |
| 14 | 14 | Gen-1 |
| 15 | deleted | RT-2 (never cited) |
| 16 | deleted | OpenVLA (never cited) |
| 17 | deleted | Open X-Embodiment (never cited) |
| 18 | deleted | Domain randomization, Tobin et al. (never cited) |
| 19 | deleted | ROSIE (never cited) |
| 20 | deleted | GenAug (never cited) |
| 21 | 15 | TransNet V2 |
| 22 | 16 | Cosmos3-Nano model card (now cited in Sec. 3) |
| 23 | 17 | GPT-4o mini |
| 24 | 18 | SAM 2 |
| 25 | 19 | Cosmos-Transfer2.5 model card |
| 26 | 20 | Canny 1986 |
| 27 | 21 | Depth Anything V2 |

Order of first appearance in the revised text, checked by script: 1 through 21 in sequence. Every number in the body has an entry and every entry is cited.

## 3. Decisions you may want to reverse

- **MimicGen and FieldGen swapped numbers** because the Fig. 1 caption cites FieldGen before the body cites MimicGen. If the figure moves below that paragraph in the final layout, swap them back.
- **Cosmos-Reason1 [11] is still cited once**, in the Background sentence describing the Reason family. It is a correct description of the family, so it stays, but the pipeline itself no longer mentions Cosmos Reason.
- **Reference style is still LNCS.** AIPR uses IEEE format. Not changed here because it is a template question, not a content one.

## 4. Left as they were (flagged in the 19 October review, not part of this request)

- Fig. 8 discussion cites the Cosmos-Predict2 model card [8] for the claim that "VLAs" struggle with physics. The model is not a VLA and the model card makes no such claim.
- The EgoScale sentence in the Introduction ("20,854 hours ... needed per task", "upper limits ... 0.71") does not match the paper, which trained on 20,854 hours total and reports 0.71 with no saturation. The missing space after "0.71." is also still there.
- The FieldGen "2.47x increase over a 2hr training example" describes a collection time ratio, not a data multiplier.
- Egocentric data cost appears as 3 to 15 USD per hour in the Introduction and 8 to 15 USD in Sec. 5, with no citation for either.
- GPT-4o mini is also called "mini-4o", "Mini-4o", "GPT-4o" and "Chat GPT 4o mini".
- The author notes in the Fig. 5 and Fig. 9 captions and the "@TODO" line in Sec. 5 are still in the text.

## 5. Raw unified diff

```diff
--- oct-19-manuscript.md	2026-10-19 09:15:48.390244300 -0500
+++ oct-19-revised.md	2026-10-19 09:37:26.374654400 -0500
@@ -2,7 +2,7 @@
 
 Shrey Jha, Skyler Saucedo, and Franklin Tanner
 
-Verbatim transcription of `AIPR 2026 Paper-oct19.pdf` (12 pages, header "S. Jha et al." / "2026 AIPR Paper"). Text is reproduced word for word, including the authors' inline notes. Line breaks within paragraphs have been removed. Figures are embedded from `figures/` (extracted from the PDF).
+Revision of `oct-19-manuscript.md` (19 October 2026). Changes: the six never-cited references are removed, the Cosmos3-Nano model card is now cited where the model is used, citations are renumbered in order of first appearance, and the Method names the reasoning model consistently as Cosmos 3 Nano. All other text is unchanged. See `oct-19-diff.md` for the itemised changes.
 
 ## 1. Abstract
 
@@ -16,13 +16,13 @@
 
 ![Figure 1](figures/fig1-data-scaling.png)
 
-*Figure 1 - Policy performance against hours of data in three papers. (a) EgoScale: average task completion score on five dexterous tasks after pretraining on 1k to 20k hours of egocentric human video; dashed line is a log-linear fit.[1] (b) LingBot-VLA: average success and progress rate over 25 tasks on three dual-arm robots after pretraining on 3k to 20k hours of robot data [3] (c) π0: average task progress over six tasks against hours of fine-tuning data, for the pretrained model [2] (d) Lin et al. 2025, Mouse Arrangement: normalized score on unseen environments and objects against the number of training environments, objects, or environment-object pairs, drawn from the power-law fits [4] (e) FieldGen: success rate, mean of four pick tasks, against wall-clock collection time for teleoperation and for FieldGen [6].*
+*Figure 1 - Policy performance against hours of data in three papers. (a) EgoScale: average task completion score on five dexterous tasks after pretraining on 1k to 20k hours of egocentric human video; dashed line is a log-linear fit.[1] (b) LingBot-VLA: average success and progress rate over 25 tasks on three dual-arm robots after pretraining on 3k to 20k hours of robot data [3] (c) π0: average task progress over six tasks against hours of fine-tuning data, for the pretrained model [2] (d) Lin et al. 2025, Mouse Arrangement: normalized score on unseen environments and objects against the number of training environments, objects, or environment-object pairs, drawn from the power-law fits [4] (e) FieldGen: success rate, mean of four pick tasks, against wall-clock collection time for teleoperation and for FieldGen [5].*
 
 Lin et al. collected 40,000 demonstrations and found that a single-task policy's generalization follows a power law in the number of training environments and objects, that additional demonstrations in the same environment stop helping past a threshold, and that 32 environments with one object each were enough for 90 percent success in rooms and on objects never seen [4].
 
 And while over 20k hours of video are needed for a single task, an hour of egocentric video costs anywhere between 3 to 15 USD, so a 20,000+ hours for a single task becomes price prohibitive and economically infeasible for startups and academia labs.
 
-While there are labs addressing this bottleneck, only a handful of solutions offer practical support. MimicGen multiplies 200 human demonstrations into 50,000 by replaying trajectory segments in new object poses, but in simulation and for robot trajectories, not video [5]. FieldGen, a field-guided data generation framework that enables scalable collection, provides a meaningful solution, but provides only a 2.47x increase over a 2hr training example [6].
+While there are labs addressing this bottleneck, only a handful of solutions offer practical support. MimicGen multiplies 200 human demonstrations into 50,000 by replaying trajectory segments in new object poses, but in simulation and for robot trajectories, not video [6]. FieldGen, a field-guided data generation framework that enables scalable collection, provides a meaningful solution, but provides only a 2.47x increase over a 2hr training example [5].
 
 We propose a method that can effectively 72x the amount of trainable data, where a world foundation model reads the first frame of an egocentric video clip and provides a structured ontology of the scene. Leveraging classical Computer Vision techniques, we identify the items within the ontology and permute their attributes (color, texture, location), effectively creating video variants that describe the same task but provide the diversity a policy needs to perform tasks concerning dextrous hand motions within common environments, like living rooms, kitchens, and office spaces.
 
@@ -38,13 +38,13 @@
 
 Figure 2 shows the pipeline we're using to permute the ontological objects within an egocentric video.
 
-First, the original Egocentric video clip (V) is prepared with NVIDIA's Cosmos Curate. Curate applies TransNetV2 shot-boundary detection, splitting a 29 min video of egocentric data into 116 individual 15-second clips, downsampled to 4 fps at 854x480. Curate uses TransNetV2, a small convolutional neural network trained to detect scene transitions; it's fast and accurate on standard shot-detection benchmarks. [21]
+First, the original Egocentric video clip (V) is prepared with NVIDIA's Cosmos Curate. Curate applies TransNetV2 shot-boundary detection, splitting a 29 min video of egocentric data into 116 individual 15-second clips, downsampled to 4 fps at 854x480. Curate uses TransNetV2, a small convolutional neural network trained to detect scene transitions; it's fast and accurate on standard shot-detection benchmarks. [15]
 
-The first frame of each clip is passed to the reasoning stack of Cosmos Predict, a Vision Language Model that returns a structured description of the task, task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations that are plausible for the task.
+The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano [12, 16], a vision-language model that returns a structured description of the task, task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations that are plausible for the task.
 
-Next, the clip is fed to Cosmos Reason, a Vision-Language-Action (VLA) model that provides a structured understanding (scene, objects, attributes, actions) of the observed scene which we define as the Ontology. We feed the Ontology (structured JSON) to GPT-4o mini [23], an LLM that writes a text prompt for Cosmos Transfer for variant video generation.
+This structured understanding (scene, objects, attributes, actions) of the observed scene is what we define as the Ontology. We feed the Ontology (structured JSON) to GPT-4o mini [17], an LLM that writes a text prompt for Cosmos Transfer for variant video generation.
 
-Four guidance maps are generated to preserve item edge, depth, color, and texture. Segmentation masks of all items are provided using SAM2 [24] to maintain item integrity while preserving the task at hand. Finally, Cosmos Transfer [10,25] renders a synthetic variant (V') of the video, same task, action, and ontology of items, but with permutations to item attributes to increase visual entropy and diversity.
+Four guidance maps are generated to preserve item edge, depth, color, and texture. Segmentation masks of all items are provided using SAM2 [18] to maintain item integrity while preserving the task at hand. Finally, Cosmos Transfer [10, 19] renders a synthetic variant (V') of the video, same task, action, and ontology of items, but with permutations to item attributes to increase visual entropy and diversity.
 
 ### 3.1 - Reasoning with Structured Ontologies
 
@@ -58,7 +58,7 @@
 
 *Figure 4 - Reasoning output for the scene with object detection bounding boxes, along with JSON Ontology.*
 
-Cosmos reasoning receives the first frame of the clip and a fixed instruction and returns a structured JSON record that defines the observed Ontology. Our pipeline asks for up to ten task-relevant objects, each with bounding boxes, and each object has the following: its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with hands) and candidate variations among seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style). A parallel block records scene-level variations (lighting, viewpoint, room style, time of day, clutter) and a final block states what training on this clip could potentially miss. Reasoning takes about 130 seconds per clip on one A100.
+Cosmos 3 Nano receives the first frame of the clip and a fixed instruction and returns a structured JSON record that defines the observed Ontology. Our pipeline asks for up to ten task-relevant objects, each with bounding boxes, and each object has the following: its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with hands) and candidate variations among seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style). A parallel block records scene-level variations (lighting, viewpoint, room style, time of day, clutter) and a final block states what training on this clip could potentially miss. Reasoning takes about 130 seconds per clip on one A100.
 
 ![Figure 5](figures/fig5-json-ontology.png)
 
@@ -66,7 +66,7 @@
 
 ### 3.2 - From Ontology to Generation-Ready Prompts
 
-In this step, we use OpenAI's GPT-4o mini [23] to prepare the prompt for Cosmos Transfer. We leverage GPT-4o mini for its exceptional speed and cost, averaging about 0.1 cents per 15-second clip. Additionally, GPT-4o provides a reliable structured JSON output and adheres to the Cosmos caption schema. Lastly, GPT-4o is one of the most available LLMs in the market currently. It should be noted that we did not run a comprehensive comparison against other Frontier models at the time.
+In this step, we use OpenAI's GPT-4o mini [17] to prepare the prompt for Cosmos Transfer. We leverage GPT-4o mini for its exceptional speed and cost, averaging about 0.1 cents per 15-second clip. Additionally, GPT-4o provides a reliable structured JSON output and adheres to the Cosmos caption schema. Lastly, GPT-4o is one of the most available LLMs in the market currently. It should be noted that we did not run a comprehensive comparison against other Frontier models at the time.
 
 From our work with this process, three prompt Engineering Principles were discovered:
 
@@ -80,9 +80,9 @@
 
 Before any object attributes are applied, we send Cosmos Transfer four control modalities from the source clip, each control modality comes with tunable parameters to decide how strong the variant is rendered.
 
-1. Edge detection: We use Canny edge detection provided by OpenCV [26]. We choose Canny over Sobel or Laplacian due to the models robustness and ability to clearly distinguish edges in poor lighting conditions. Successful edge detection is important since if the edges are not clearly defined, object geometry could warp during clip permutation.
+1. Edge detection: We use Canny edge detection provided by OpenCV [20]. We choose Canny over Sobel or Laplacian due to the models robustness and ability to clearly distinguish edges in poor lighting conditions. Successful edge detection is important since if the edges are not clearly defined, object geometry could warp during clip permutation.
 
-2. Depth: The depth control is monocular depth video provided by DepthAnything V2 [27], and it provides an emergent layer of pseudo-3-dimensional object spatial positioning. As we permute object attributes, it's important to maintain persistent object ordering within the variant output.
+2. Depth: The depth control is monocular depth video provided by DepthAnything V2 [21], and it provides an emergent layer of pseudo-3-dimensional object spatial positioning. As we permute object attributes, it's important to maintain persistent object ordering within the variant output.
 
 3. Color for lightning: maintaining overall color palette and continuity as we adjust light parameters.
 
@@ -138,9 +138,9 @@
 
 4. Lin, F., Hu, Y., Sheng, P., Wen, C., You, J., Gao, Y.: Data Scaling Laws in Imitation Learning for Robotic Manipulation. In: International Conference on Learning Representations (ICLR) (2025). https://arxiv.org/abs/2410.18647
 
-5. Mandlekar, A., Nasiriany, S., Wen, B., Akinola, I., Narang, Y., Fan, L., Zhu, Y., Fox, D.: MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations. In: Proceedings of the 7th Conference on Robot Learning (CoRL) (2023). https://arxiv.org/abs/2310.17596
+5. Wang, W., Ye, K., Zhou, X., Chen, T., Min, C., Zhu, Q., Yang, X., Luo, P., Shen, Y., Yang, Y., Yao, M., Mu, Y.: FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation. arXiv preprint arXiv:2510.20774 (2025). https://arxiv.org/abs/2510.20774
 
-6. Wang, W., Ye, K., Zhou, X., Chen, T., Min, C., Zhu, Q., Yang, X., Luo, P., Shen, Y., Yang, Y., Yao, M., Mu, Y.: FieldGen: From Teleoperated Pre-Manipulation Trajectories to Field-Guided Data Generation. arXiv preprint arXiv:2510.20774 (2025). https://arxiv.org/abs/2510.20774
+6. Mandlekar, A., Nasiriany, S., Wen, B., Akinola, I., Narang, Y., Fan, L., Zhu, Y., Fox, D.: MimicGen: A Data Generation System for Scalable Robot Learning using Human Demonstrations. In: Proceedings of the 7th Conference on Robot Learning (CoRL) (2023). https://arxiv.org/abs/2310.17596
 
 7. NVIDIA, Agarwal, N., Ali, A., et al.: Cosmos World Foundation Model Platform for Physical AI. arXiv preprint arXiv:2501.03575 (2025). https://arxiv.org/abs/2501.03575
 
@@ -158,28 +158,16 @@
 
 14. Esser, P., Chiu, J., Atighehchian, P., Granskog, J., Germanidis, A.: Structure and Content-Guided Video Synthesis with Diffusion Models. In: Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV), pp. 7346-7356 (2023). https://arxiv.org/abs/2302.03011
 
-15. Zitkovich, B., Yu, T., Xu, S., et al.: RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. In: Proceedings of the 7th Conference on Robot Learning (CoRL), PMLR 229, pp. 2165-2183 (2023). https://arxiv.org/abs/2307.15818
+15. Souček, T., Lokoč, J.: TransNet V2: An Effective Deep Network Architecture for Fast Shot Transition Detection. arXiv preprint arXiv:2008.04838 (2020). https://arxiv.org/abs/2008.04838
 
-16. Kim, M.J., Pertsch, K., Karamcheti, S., et al.: OpenVLA: An Open-Source Vision-Language-Action Model. In: Proceedings of the 8th Conference on Robot Learning (CoRL), PMLR 270, pp. 2679-2713 (2025). https://arxiv.org/abs/2406.09246
+16. NVIDIA: Cosmos3-Nano. Hugging Face model card (2026). https://huggingface.co/nvidia/Cosmos3-Nano
 
-17. Open X-Embodiment Collaboration, O'Neill, A., et al.: Open X-Embodiment: Robotic Learning Datasets and RT-X Models. In: Proceedings of the IEEE International Conference on Robotics and Automation (ICRA), pp. 6892-6903 (2024). https://arxiv.org/abs/2310.08864
+17. OpenAI: GPT-4o mini: Advancing Cost-Efficient Intelligence (2024). https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
 
-18. Tobin, J., Fong, R., Ray, A., Schneider, J., Zaremba, W., Abbeel, P.: Domain Randomization for Transferring Deep Neural Networks from Simulation to the Real World. In: Proceedings of the IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 23-30 (2017). https://arxiv.org/abs/1703.06907
+18. Ravi, N., Gabeur, V., Hu, Y.T., et al.: SAM 2: Segment Anything in Images and Videos. In: International Conference on Learning Representations (ICLR) (2025). https://arxiv.org/abs/2408.00714
 
-19. Yu, T., Xiao, T., Tompson, J., et al.: Scaling Robot Learning with Semantically Imagined Experience. In: Proceedings of Robotics: Science and Systems (RSS) (2023). https://arxiv.org/abs/2302.11550
+19. NVIDIA: Cosmos-Transfer2.5: A Suite of Diffusion-based World-to-World Models. Hugging Face model card (2025). https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B
 
-20. Chen, Q., Kiami, S.C., Gupta, A., Kumar, V.: GenAug: Retargeting Behaviors to Unseen Situations via Generative Augmentation. In: Proceedings of Robotics: Science and Systems (RSS) (2023). https://arxiv.org/abs/2302.06671
+20. Canny, J.: A Computational Approach to Edge Detection. IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-8(6), 679-698 (1986). https://doi.org/10.1109/TPAMI.1986.4767851
 
-21. Souček, T., Lokoč, J.: TransNet V2: An Effective Deep Network Architecture for Fast Shot Transition Detection. arXiv preprint arXiv:2008.04838 (2020). https://arxiv.org/abs/2008.04838
-
-22. NVIDIA: Cosmos3-Nano. Hugging Face model card (2026). https://huggingface.co/nvidia/Cosmos3-Nano
-
-23. OpenAI: GPT-4o mini: Advancing Cost-Efficient Intelligence (2024). https://openai.com/index/gpt-4o-mini-advancing-cost-efficient-intelligence/
-
-24. Ravi, N., Gabeur, V., Hu, Y.T., et al.: SAM 2: Segment Anything in Images and Videos. In: International Conference on Learning Representations (ICLR) (2025). https://arxiv.org/abs/2408.00714
-
-25. NVIDIA: Cosmos-Transfer2.5: A Suite of Diffusion-based World-to-World Models. Hugging Face model card (2025). https://huggingface.co/nvidia/Cosmos-Transfer2.5-2B
-
-26. Canny, J.: A Computational Approach to Edge Detection. IEEE Transactions on Pattern Analysis and Machine Intelligence PAMI-8(6), 679-698 (1986). https://doi.org/10.1109/TPAMI.1986.4767851
-
-27. Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng, J., Zhao, H.: Depth Anything V2. In: Advances in Neural Information Processing Systems (NeurIPS) (2024). https://arxiv.org/abs/2406.09414
+21. Yang, L., Kang, B., Huang, Z., Zhao, Z., Xu, X., Feng, J., Zhao, H.: Depth Anything V2. In: Advances in Neural Information Processing Systems (NeurIPS) (2024). https://arxiv.org/abs/2406.09414
```
