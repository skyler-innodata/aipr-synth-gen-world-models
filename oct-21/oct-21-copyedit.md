# Copyedit of "AIPR 2026 Paper-updated" (21 October 2026)

Audience: Shrey, Skyler, Frank. This is a line-level pass over `oct-21/AIPR 2026 Paper-updated.pdf` (same text as the `.md` and `.docx`). Each item gives where it is, the text as it stands, what is wrong, and a fix you can paste. Locations use the LNCS section numbers of the updated PDF (Abstract, 1, 1.1, 2, 2.1, 2.2, 2.3, 3, 4, 5) and the LNCS figure numbers (Fig. 1 to 7). Where the source text uses a dollar sign, this file writes "USD" instead, because a dollar sign breaks Markdown rendering; the quoted wording is otherwise verbatim.

Nothing in the manuscript has been changed. Apply what you agree with in the Google Doc, then re-run `bash oct-21/updated/build.sh` after the markdown and `main.tex` are updated.

## 0. The ten that matter most

1. **The pipeline costs more per hour than real data, as written** (Sec. 4, item 4.6). The text says real egocentric video costs 3 to 25 USD per hour and the pipeline costs 96 USD per hour processed. Each 15-second clip takes 20 minutes of A100 time, so an hour of generated video costs about 96 USD whether you count per source hour or per output hour. On those numbers the pipeline is four to thirty times more expensive than collection, and the paper's economic argument inverts. Either the cost figure or the argument has to change. Draft 7 said 1.20 USD per hour; find out which number is right and what it is per.
2. **"the amount the amount"** (Sec. 1, para 4, item 1.14). The repeated words you spotted.
3. **EgoScale is still overstated** (Sec. 1, para 1 and 2, items 1.4 and 1.8). "upper limits of achieving a mean task acceptable score of 0.71" and "over 20k hours of video may be needed for a single task" are the two sentences the reviewing editor flagged; 0.71 is the value at the largest scale tested, not a ceiling, and the hours are shared pretraining, not per task.
4. **Three different source-data counts** (items 2.3, 3.3, 4.1). Method says "a 29 min video", Results says "Eight recordings ... 4 minutes to 8 minutes", Closing the Gap says "From 3, 10-minute video examples" and "One 10-minute video became 4 hours". The repo's confirmed numbers are eight recordings, about 80 minutes raw, 116 clips, 29 minutes retained. With 72 variants per clip, a 10-minute recording would become 12 hours, not 4; 4 hours is what 29 minutes divided by eight recordings gives.
5. **"producing 8,352 synthetic video variations"** (item 4.1). 64 variants were rendered. 8,352 is 116 clips times 72 admissible variations, a capacity, not an output.
6. **Wrong model names in Results** (item 3.5): "For Cosmos Reason" should be Cosmos 3 Nano, and "Predict2" appears with no introduction anywhere in the Method.
7. **Two captions still carry author notes** (items F6 and F7): "(find better example showing spaghetti)" and "... maybe we can find a better example?".
8. **"(see appendix for source code)"** (item 3.4) points to an appendix that does not exist.
9. **The Fig. 4 caption lists leakage as a feature** (item F4): "varying the skin color of the human" was not requested; the prompt asked for the countertop.
10. **"policies ... are bottlenecked"** (Abstract, item A.1). The subject is "Training", singular, so "is bottlenecked". First sentence of the paper.

## 1. Global consistency (fix once, apply everywhere)

| Issue | Where it varies | Pick one |
|---|---|---|
| Figure references | Text says "Figure 1", captions say "Fig. 1" | "Fig. N" everywhere (LNCS convention) |
| SAM 2 | "SAM2" in Abstract, Method, Sec. 2.3; reference 18 says "SAM 2" | "SAM 2" |
| TransNet V2 | "TransNetV2" in Method; reference 15 says "TransNet V2" | "TransNet V2" |
| Depth Anything V2 | "DepthAnything V2" in Sec. 2.3; reference 21 says "Depth Anything V2" | "Depth Anything V2" |
| Ontology | "Ontology" capitalised as a defined term in Abstract, 2, 2.1, 4; "ontology" lower case in Sec. 1 para 4 and Sec. 2 ("ontology of items"); "Ontological objects" in 2, 3, 4 | Lower-case "ontology" throughout, and "objects in the ontology" rather than "ontological objects" (ontological means something else) |
| Cosmos Transfer | "Cosmos Transfer 2.5" in Abstract; "Cosmos Transfer" in Sec. 2, 2.2, 2.3 | Say "Cosmos Transfer 2.5" at first use in Sec. 2, then "Transfer" |
| The reasoner | "Cosmos 3 Nano" in Abstract, 2, 2.1; "Cosmos Reason" in Sec. 3 | "Cosmos 3 Nano" (confirmed by Shrey on 19 October) |
| Currency | "USD 3 to USD 25 USD" (Sec. 1), "USD 3 - USD 25 USD" and "USD 96 USD" (Sec. 4), "0.12 USD" (Sec. 4), "0.1 cents" (Sec. 2.2) | One form: "3 to 25 USD", "96 USD", "0.12 USD", "0.001 USD" |
| Thousands | "20k hours" and "20,000+ hours" in the same paragraph | "20,000 hours" |
| The cloth | "towel" (Fig. 2 caption), "wash cloth" (Sec. 2.1), "rags" (Sec. 2.1), "paper towels" (Sec. 2.2), "rag" (Fig. 4 caption) | One word for the object in the clip |
| Oxford comma | Used in most lists ("objects, surfaces, and lighting"), missing in others ("text, an image or a video"; "depth, segmentation, edge and blurred-RGB maps") | Use it |
| Acronyms | "VLA" used in Sec. 1 without expansion; "WFMs" defined in 1.1 and never used; "LLM" used in Sec. 2.2 and Sec. 4 without expansion; "LLMs" in 2.2 | Expand each at first use, then use the acronym |
| Capitalised common nouns | "World Foundation Models", "Large Language Models", "Computer Vision", "Boundary detection", "Image Segmentation", "Canny Edge detection" (Abstract); "Egocentric video clip" (Sec. 2); "Frontier models", "prompt Engineering Principles" (2.2); "Notebooks" (3) | Lower case |
| References listed but not cited | 5 (FieldGen), 13 (ControlNet), 14 (Gen-1) | Springer requires list and text to match; restore the sentences or drop the entries and renumber |
| Reference 20 cited for the wrong thing | Sec. 2.3 item 1 cites [20] (Canny 1986) for "provided by OpenCV" | Cite [20] for Canny edge detection; OpenCV is uncited |

## 2. Section by section

### Abstract

**A.1** Now: "Training successful humanoid robotic manipulation policies within the space of Physical AI are bottlenecked by real-world data limitations in quantity and diversity of environment."
Issue: subject-verb agreement ("Training ... are"); "in quantity and diversity of environment" is missing articles.
Fix: "Training humanoid manipulation policies in Physical AI is bottlenecked by real-world data: there is too little of it, and it covers too few environments."

**A.2** Now: "In this paper, we describe a pipeline that leverages World Foundation Models from the NVIDIA Cosmos, along with Large Language Models like OpenAI's GPT-4o mini to generate variations of real egocentric video clips while keeping the recorded actions, scaling a single video into hundreds of permutations."
Issue: "from the NVIDIA Cosmos" is unfinished (Cosmos what?); "In this paper" is on the house list; "leverages" too; "hundreds of permutations" does not match Sec. 4 (72 per clip). Capitalisation.
Fix: "We describe a pipeline that uses NVIDIA Cosmos world foundation models together with a large language model (LLM), OpenAI's GPT-4o mini, to generate variations of real egocentric clips while keeping the recorded actions, turning one clip into dozens of permutations."

**A.3** Now: "Our method uses NVIDIA Cosmos 3 Nano to produce an Ontology of each clip, the task of each object's role, and plausible variations, along with GPT-4o mini to write a prompt to generate scene permutations."
Issue: "the task of each object's role" is garbled.
Fix: "Cosmos 3 Nano produces an ontology of each clip: the task, each object's role in it, and the variations that are plausible for that task. GPT-4o mini turns the ontology into a generation prompt."

**A.4** Now: "Our method employs traditional Computer Vision techniques like Boundary detection and Image Segmentation, using Canny Edge detection coupled with Segment Anything 2 (SAM2) to locate the objects we wish to permute, while Cosmos Transfer 2.5 renders the items maintaining realism within the video."
Issue: "Our method" starts two consecutive sentences; capitalisation; "renders the items maintaining realism" needs "while", but "while" is already used earlier in the sentence.
Fix: "Classical computer vision, Canny edge detection and Segment Anything 2 (SAM 2), locates the objects to permute, and Cosmos Transfer 2.5 renders the changed objects while preserving the realism of the video."

**A.5** Now: "This paper describes our process and findings, where structured reasoning about a scene produces robust realistic permutations."
Issue: second "this paper" sentence in one abstract; "robust realistic" needs a comma, and "robust" is on the strike list.
Fix: "Structured reasoning about the scene before anything is changed is what makes the permutations physically plausible."

**A.6** Now: "We outline limitations and provide best practices for leveraging these tools, demonstrating that this powerful and economical approach is scalable when solving problems in robot learning."
Issue: "leveraging"; "powerful and economical" is adjective stacking; "demonstrating ... scalable" claims more than the paper shows (no policy was trained, 64 variants rendered).
Fix: "We report the failure cases, give prompt and control-weight practices that worked, and estimate the cost per hour of generated video."

### 1 Introduction

**1.1** Para 1. Now: "Where humanoid robotic policy training and effectiveness are quantified, the consensus within the Physical AI community is that more training data is required, on the order of tens of thousands of hours, and that the diversity of objects within the space (defined in the Ontology) matter for policy robustness."
Issue: "diversity ... matter" should be "matters"; "Where ... are quantified" reads as a place; "(defined in the Ontology)" points forward to a term defined two pages later.
Fix: "Where policy performance has been measured against data volume, the finding is consistent: tens of thousands of hours are needed, and the diversity of objects in the training scenes matters as much as the hours."

**1.2** Para 1. Now: "As such, the mean acceptable score, defined as the robot's ability to successfully complete the task it was trained on, scales logarithmically with the hours of egocentric video [1]."
Issue: "As such" implies a consequence, but this is the evidence; "mean acceptable score" is not EgoScale's term and the definition describes binary success, whereas EgoScale's metric is a partial-credit completion score.
Fix: "In EgoScale, the average task completion score, a partial-credit measure of how far the robot gets through the task it was trained on, rises log-linearly with the hours of egocentric pretraining video [1]."

**1.3** Para 1. Now: "Zheng et al, authors of Egoscale, claim over 20,854 hours of egocentric video were used for pre-training their VLA, with upper limits of achieving a mean task acceptable score of 0.71."
Issue: "et al," needs a period; "Egoscale" is "EgoScale"; "claim" for a reported fact; "VLA" is not expanded; "upper limits of ... 0.71" is the factual error (0.71 is the score at 20k hours, the largest scale tested, and the authors report no saturation).
Fix: "Zheng et al. pretrain their vision-language-action (VLA) model on 20,854 hours of egocentric video and reach an average completion score of 0.71 at that scale, with no sign of saturation [1]."

**1.4** Para 1. Now: "0.71. π0 pretrains on more than 10,000 hours of robot data to perform similar tasks [2]."
Issue: a sentence beginning with a symbol; "similar tasks" to what is unclear.
Fix: "The π0 model pretrains on more than 10,000 hours of robot data for comparable manipulation tasks [2]."

**1.5** Para 2. Now: "Lin et al. collected 40,000 demonstrations and found that a single-task policy's generalization follows a power law in the number of training environments and objects [4]."
Issue: none in grammar. Note that this sentence is the strongest support for the paper's approach (diversity, not hours) and is now one line; draft 7's fuller version ("additional demonstrations in the same environment stop helping past a threshold, and 32 environments with one object each were enough for 90 percent success") carried the argument. Consider restoring it.

**1.6** Para 2. Now: "And while over 20k hours of video may be needed for a single task, an hour of egocentric video costs anywhere between USD 3 to USD 25 USD, so a 20,000+ hours for a single task becomes price prohibitive and economically infeasible for startups and academia labs."
Issue: sentence-initial "And"; "20k" then "20,000+"; "between 3 to 25" should be "between 3 and 25"; the dollar sign plus "USD" marks the currency twice; "a 20,000+ hours"; "price prohibitive" should be "cost-prohibitive", and "economically infeasible" repeats it; "academia labs" should be "academic labs"; and "for a single task" is the EgoScale error again.
Fix: "A corpus of that size is out of reach for most groups. At 3 to 25 USD per hour of egocentric video [CITATION NEEDED], 20,000 hours costs roughly 60,000 to 500,000 USD before curation, which is cost-prohibitive for startups and academic labs."

**1.7** Para 3. Now: "While there are labs addressing this bottleneck, only a handful of solutions offer practical support. MimicGen can simulate 50,000 samples from 200 real human demonstrations by replaying trajectory segments in new object poses, but in simulation and for robot trajectories, not video [6]."
Issue: "a handful of solutions" is followed by one example (the FieldGen sentence was cut, which also orphaned reference 5); "simulate ... in simulation" repeats; "but in simulation and for robot trajectories" is a fragment.
Fix: "Several groups have attacked this bottleneck. MimicGen generates 50,000 demonstrations from 200 human ones by replaying trajectory segments in new object poses, but it works in simulation on robot trajectories, not on video [6]. FieldGen generates manipulation data from teleoperated pre-manipulation trajectories and reports a 2.47 times gain over two hours of teleoperation [5]." (The second sentence restores the citation of reference 5; drop it and the entry if you prefer.)

**1.8** Para 4. Now: "We propose a method that can effectively increase the amount the amount of trainable data, where a world foundation model reads the first frame of an egocentric video clip and provides a structured ontology of the scene."
Issue: "the amount the amount" is doubled; "effectively" is vague where draft 7 gave a number.
Fix: "We propose a method that multiplies the amount of trainable data by up to 72, in which a world foundation model reads the first frame of an egocentric clip and returns a structured ontology of the scene."

**1.9** Para 4. Now: "Leveraging classical computer vision techniques, we identify the items within the ontology and permute their attributes (color, texture, location), effectively creating video variants that describe the same task but provide the diversity a policy needs to learn tasks concerning dexterous hand motions within common environments, like living rooms, kitchens, and office spaces."
Issue: "Leveraging"; second "effectively" in two sentences; "tasks concerning dexterous hand motions within common environments" is wordy; "location" is listed as a permuted attribute but no location change appears anywhere in Results.
Fix: "With classical computer vision we locate the objects in the ontology and permute their attributes (color, texture), producing video variants of the same task with the visual diversity a policy needs for dexterous manipulation in living rooms, kitchens, and offices."

### 1.1 Background

**1.10** Now: "World foundation models (WFMs) are large-scale artificial intelligence systems trained to understand, simulate, and predict the physical world, including how objects move, interact, and follow the laws of physics [7]."
Issue: "WFMs" is defined and never used again.
Fix: drop "(WFMs)", or use the acronym in Sec. 2 and 4 where "World Model suite" and "world foundation model" appear.

**1.11** Now: "NVIDIA Cosmos consists of three models: Predict forecasts future frames from text, an image or a video [8]; Transfer adapts a video across environments under multi-control conditioning on depth, segmentation, edge and blurred-RGB maps [9, 10]; Reason is a vision-language model for physical scene understanding [11]."
Issue: they are model families, not three models (Predict alone has 2B and 14B variants); two missing Oxford commas.
Fix: "NVIDIA Cosmos has three model families: Predict forecasts future frames from text, an image, or a video [8]; Transfer re-renders a video under multi-control conditioning on depth, segmentation, edge, and blurred-RGB maps [9, 10]; Reason is a vision-language model for physical scene understanding [11]."

**1.12** Now: "Cosmos 3 folds the three models into one, with an autoregressive subnetwork that reasons about a scene and a diffusion-based subnetwork that generates video, audio, and actions conditioned on that reasoning [12]."
Issue: none. If the ControlNet and Gen-1 sentence is restored here ("Transfer descends from ControlNet [13] and Gen-1 [14], which steer a frozen diffusion model with structure maps."), references 13 and 14 are cited again.

### 2 Method

**2.1** Now: "Figure 1 shows the pipeline we're using to permute the ontological objects within an egocentric video."
Issue: contraction; "ontological objects".
Fix: "Fig. 1 shows the pipeline we use to permute the objects in the ontology of an egocentric video."

**2.2** Now: "First, the original Egocentric video clip (V) is prepared with NVIDIA's Cosmos Curate."
Issue: capital E; "original" is redundant with "source" used later.
Fix: "First, the source egocentric clip V is prepared with NVIDIA Cosmos Curate."

**2.3** Now: "Curate applies TransNetV2 shot-boundary detection, splitting a 29 min video of egocentric data into 116 individual 15-second clips, downsampled to 4 fps at 854x480."
Issue: "a 29 min video" conflicts with Results (eight recordings) and Sec. 4 (three 10-minute examples); the clips are at most 15 seconds, not all 15 seconds (the repo's confirmed count: 116 clips, 29 minutes retained); "854x480" should use a multiplication sign.
Fix: "Curate applies TransNet V2 shot-boundary detection, splitting about 80 minutes of recordings into 116 clips of at most 15 seconds (29 minutes retained), downsampled to 4 fps at 854×480."

**2.4** Now: "Curate uses TransNetV2, a small convolutional neural network trained to detect scene transitions. Curate is fast and accurate on standard shot-detection benchmarks [15]."
Issue: the benchmark result in [15] belongs to TransNet V2, not to Curate; "scene transitions" should be "shot transitions" to match the term in the previous sentence.
Fix: "TransNet V2 is a small convolutional network trained to detect shot transitions; it is fast and accurate on the standard shot-detection benchmarks [15]."

**2.5** Now: "The first frame of each clip is passed to the reasoning tower of Cosmos 3 Nano [12, 16], a vision-language model that returns a structured description of the task, task-relevant objects with bounding boxes and their roles in the task, their current appearance and state, and the variations that are plausible for the task."
Issue: "task" four times.
Fix: "The first frame of each clip goes to the reasoning tower of Cosmos 3 Nano [12, 16], a vision-language model that returns a structured description: the task, the relevant objects with bounding boxes and roles, their current appearance and state, and the variations plausible for that task."

**2.6** Now: "This structured understanding (scene, objects, attributes, actions) of the observed scene is what we define as the Ontology."
Issue: "scene ... of the observed scene".
Fix: "This structured description (scene, objects, attributes, actions) is what we call the ontology."

**2.7** Now: "We feed the Ontology (structured JSON) to GPT-4o mini [17] to write a text prompt for Cosmos Transfer for variant video generation."
Issue: "for ... for".
Fix: "We feed the ontology, as JSON, to GPT-4o mini [17], which writes the text prompt that Cosmos Transfer 2.5 uses to generate the variant."

**2.8** Now: "Four guidance maps are generated to preserve item edge, depth, color, and texture."
Issue: the four controls listed in Sec. 2.3 are edge, depth, blurred RGB, and segmentation; "texture" is not one of them, and "item edge" needs a plural.
Fix: "Four control maps are computed from the source clip: edges, depth, blurred RGB (color and lighting), and segmentation."

**2.9** Now: "Segmentation masks of all items are generated using SAM2 [18] to maintain item integrity while preserving the task at hand."
Issue: "generated" in two consecutive sentences; "maintain item integrity while preserving the task at hand" says little.
Fix: "SAM 2 [18] provides the segmentation masks, so that the renderer knows which pixels belong to each object."

**2.10** Now: "Finally, Cosmos Transfer [10, 19] renders a synthetic variant (V') of the video with the same task, action, and ontology of items, but with directed permutations to item attributes to increase visual diversity."
Issue: "permutations to" should be "permutations of".
Fix: "Finally, Cosmos Transfer 2.5 [10, 19] renders the variant V' with the same task, action, and objects, but with directed changes to object attributes that add visual diversity."

### 2.1 Reasoning with Structured Ontologies

**2.11** Now: "As shown in Figure 2, our example video consists of a white bucket on a white countertop, and the task is defined as follows: A human must use a wash cloth from the bucket to clean a countertop."
Issue: "wash cloth" is one word; capital A after a colon; "a countertop" should be "the countertop".
Fix: "In the example clip (Fig. 2), a white bucket sits on a white countertop, and the task is: a person uses a washcloth from the bucket to wipe the countertop."

**2.12** Now: "If we wish to train a robot policy on this cleaning task, we will need to augment portions of the video to increase the amount of training data to improve our average task completion score."
Issue: "to increase ... to improve" chain.
Fix: "To train a robot policy on this task we need more training data than one clip, so we augment the video to raise the average task completion score."

**2.13** Now: "If we decide to change the color of the bucket, countertop, or rags, does that permutation affect the outcome of the robot training policy?"
Issue: rhetorical question in the body; "robot training policy" should be "trained policy".
Fix: "Changing the color of the bucket, countertop, or cloth should not change what the policy has to learn about the task, but the model generating the variant has no way to know that unless it is told."

**2.14** Now: "Whichever model is used, it must learn to associate objects with the broader actions and physical context they participate in. Not just what they look like, but how they behave in the task."
Issue: the second sentence is a fragment.
Fix: "Whichever model is used, it must associate objects with the actions and physical context they take part in: not just what they look like, but how they behave in the task."

**2.15** Now: "This is why reasoning with structured ontologies is critical: we ask a model to understand the scene, objects, states, materials, lighting, and actions before anything else is varied, so that the permutations proposed for an object are ones that are physically plausible for the given task."
Issue: "This is why" with no noun; "are ones that are".
Fix: "That requirement is why we reason first: a model describes the scene, objects, states, materials, lighting, and actions before anything is varied, so that the permutations proposed for an object are physically plausible for the task."

**2.16** Now: "Cosmos 3 Nano receives the first frame of the clip and a fixed instruction and returns a structured JSON record that defines the observed Ontology."
Issue: "and ... and".
Fix: "Cosmos 3 Nano receives the first frame of the clip together with a fixed instruction, and returns a JSON record that defines the ontology."

**2.17** Now: "Our pipeline asks for up to ten task-relevant objects, each with bounding boxes, and each object has the following: its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with hands) and candidate variations among seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style)."
Issue: "each with bounding boxes" (one box per object); "each object has the following:" is clumsy; missing comma before "and candidate variations"; "among seven dimensions" should be "along".
Fix: "The instruction asks for up to ten task-relevant objects, each with a bounding box, its role in the task, its current appearance (color, material, texture, condition, size), its current state (position, orientation, interaction with hands), and candidate variations along seven dimensions (color and appearance, material and texture, size and shape, state and position, condition, interaction, brand and style)."

**2.18** Now: "A parallel block records scene-level variations (lighting, viewpoint, room style, time of day, clutter) and a final block states what training on this clip could potentially miss."
Issue: "could potentially" is doubled hedging.
Fix: "... and a final block states what a policy trained on this clip alone would miss."

**2.19** Now: "Reasoning takes about 130 seconds per clip on one A100."
Issue: the same number is stated again in Sec. 3 ("For Cosmos Reason, the average reasoning time was 130 seconds per clip"). Keep it in one place; Results is the natural home.

### 2.2 From Ontology to Generation-Ready Prompts

**2.20** Now: "In this step, we use OpenAI's GPT-4o mini [17] to prepare the prompt for Cosmos Transfer. We leverage GPT-4o mini for its exceptional speed and cost, averaging about 0.1 cents per 15-second clip."
Issue: "leverage"; "exceptional speed and cost" (cost is not exceptional, it is low); "0.1 cents" in a paper that otherwise uses USD.
Fix: "GPT-4o mini [17] writes the prompt for Cosmos Transfer. We chose it for speed and price: about 0.001 USD per 15-second clip."

**2.21** Now: "Additionally, GPT-4o mini provides a reliable structured JSON output and adheres to the Cosmos caption schema. Lastly, GPT-4o mini is one of the most available LLMs in the market currently."
Issue: "Additionally"; "a reliable structured JSON output" (no article); "most available ... currently" is both vague and dated the day it is printed.
Fix: "It returns structured JSON reliably and follows the Cosmos caption schema, and it is widely available."

**2.22** Now: "It should be noted that we did not run a comprehensive comparison against other Frontier models at the time."
Issue: "It should be noted that"; "comprehensive"; capital F.
Fix: "We did not compare it against other frontier models."

**2.23** Now: "From our work with this process, three prompt Engineering Principles were discovered:"
Issue: stray capitals; passive "were discovered".
Fix: "Three prompt-writing rules came out of this work:"

**2.24** Item 1. Now: "... A single mention of "blue" is one token competing with everything else in the 150 word caption; repeating the attribute in different context puts more of the prompt's attention mass on the property to be modified."
Issue: "150 word" needs a hyphen, and the repo's record of the prompt length is "a few hundred words" (marked VERIFY in draft 6); "in different context" should be plural; "attention mass" is speculative jargon.
Fix: "A single mention of "blue" is one token competing with everything else in a 150-word caption [VERIFY length]; repeating the attribute in different phrases gives the property more weight in the prompt."

**2.25** Item 2. Now: "... Prior to enforcing this clause, we observed evidence of data leakage (bucket turning blue despite prompting the color change of the counter.)"
Issue: the period belongs outside the parenthesis; "data leakage" is a machine-learning evaluation term and means something else here; "Prior to" for "Before".
Fix: "Before we added this clause, the change bled into other objects: the bucket turned blue when only the counter was prompted."

**2.26** Item 3. Now: "Describe the result, not the change: to change the countertop color, the prompt should say, "a person cleaning a solid blue countertop", not "change white countertop to blue..." We conjecture this is because the model was trained on descriptive video captions rather than edit instructions, placing imperative prompts outside its training distribution."
Issue: missing article in the quoted bad prompt; "this is because" with no noun.
Fix: "... not "change the white countertop to blue". We attribute this to the model having been trained on descriptive video captions rather than edit instructions, so imperative prompts fall outside its training distribution."

### 2.3 Guiding the Rendering

**2.27** Now: "Before any object attributes are applied, we send Cosmos Transfer four control modalities from the source clip. Each control modality comes with tunable parameters to decide how strong the variant is rendered."
Issue: "attributes are applied" should be "are changed"; "how strong the variant is rendered" does not say what the parameter does (it is a weight on how tightly each control constrains the render).
Fix: "Before any attribute is changed, we send Cosmos Transfer four control signals computed from the source clip. Each carries a weight that sets how tightly it constrains the render."

**2.28** Item 1. Now: "Edge detection: We use Canny edge detection provided by OpenCV [20]."
Issue: reference 20 is Canny's 1986 paper, not OpenCV. Draft 7's justification (why Canny rather than Sobel or Laplacian) was cut; without it the item is one line.
Fix: "Edge: Canny edge detection [20], as implemented in OpenCV."

**2.29** Item 2. Now: "Depth: The depth control is monocular depth video provided by DepthAnything V2 [21], and it provides an emergent layer of pseudo-3-dimensional object spatial positioning."
Issue: "provided ... provides"; "emergent layer of pseudo-3-dimensional object spatial positioning" is five nouns deep; model name spelling.
Fix: "Depth: a monocular depth video from Depth Anything V2 [21], which gives the renderer an approximate 3D layout of the scene so that object ordering is kept."

**2.30** Item 3. Now: "Color for lighting: maintaining overall color alette and continuity as we adjust light parameters. We use a bilateral bluir input RGB frames."
Issue: "alette" is "palette"; "bluir" is "blur"; the second sentence is missing "of the"; the item name does not match "blurred-RGB maps" in Sec. 1.1.
Fix: "Blurred RGB (color and lighting): a bilateral blur of the source RGB frames, which keeps the overall palette and lighting continuous while attributes change."

**2.31** Item 4. Now: "Segmentation Mask: All ontological objects are identified pixel-by-pixel. This provides clearly defined classification to which pixels the model can change. If two or more objects spatially relate or overlap, or if there is occlusion, we can render the object in question without affecting the neighboring objects in the scene."
Issue: "This provides" with no noun; "clearly defined classification to which pixels"; "spatially relate or overlap"; and the last clause claims what Fig. 5 (chairs turned blue with the pillow) and Fig. 4 (hand, wall, and lighting changed) show did not happen. The mask is a soft control at the weights used.
Fix: "Segmentation: a pixel-level mask of every object in the ontology from SAM 2, which tells the renderer which pixels belong to the target. Where objects touch, overlap, or occlude one another, the mask is what keeps the change on the intended object, to the extent the control weight enforces it (Sec. 3 shows two cases where it did not)."

### 3 Results

**3.1** Now: "Eight recordings of first-person videos of household chores were used to generate realistic permutation variants."
Issue: "recordings of ... videos" doubles up.
Fix: "Eight first-person recordings of household chores were the source material."

**3.2** Now: "Tasks were captured egocentrically with a head-mounted camera and include counter wiping, cloth folding, bed making, and cable wrapping."
Issue: "egocentrically with a head-mounted camera" says the same thing twice; Shrey's answers record a handheld camera, not head-mounted.
Fix: "They were recorded with a [VERIFY: handheld or head-mounted] camera and cover counter wiping, cloth folding, bed making, and cable wrapping."

**3.3** Now: "Each task ranges from 4 minutes to 8 minutes in duration."
Issue: it is the recording, not the task, that has a duration; conflicts with "a 29 min video" (Sec. 2) and "3, 10-minute video examples" (Sec. 4). Eight recordings of 4 to 8 minutes is 32 to 64 minutes, not 80.
Fix: "Each recording runs [VERIFY] minutes; about 80 minutes in all, of which 29 minutes survived shot detection as 116 clips."

**3.4** Now: "Our studies ran on Google Collab Pro+ Notebooks (see appendix for source code) on an A100 80 GB."
Issue: "Colab"; lower-case "notebooks"; "on ... on"; there is no appendix.
Fix: "All runs used Google Colab Pro+ notebooks with one A100 80 GB GPU." (Add an appendix with the code, or a repository link, if "see appendix" is to stay.)

**3.5** Now: "For Cosmos Reason, the average reasoning time was 130 seconds per clip. Transfer renders averaged about 20 minutes. And Predict2 renderings took about 3.5 minutes."
Issue: "Cosmos Reason" is the wrong model (Cosmos 3 Nano); sentence-initial "And"; "renders" then "renderings"; Predict2 has not been introduced anywhere, so the reader does not know what it was used for (the two action-variation runs).
Fix: "Per clip, Cosmos 3 Nano reasoning took about 130 seconds, a Transfer render about 20 minutes, and a Predict2 render about 3.5 minutes (Predict2 was used for the two action-level runs in Fig. 6)."

**3.6** Now: "LLM inference by Chat GPT-4o mini only took a few seconds per clip."
Issue: "Chat GPT-4o mini" mixes the product (ChatGPT) with the model (GPT-4o mini); "only took" should be "took only".
Fix: "GPT-4o mini took only a few seconds per clip."

**3.7** Now: "Every variant was inspected to see how it compared to the matched source."
Fix: "Every variant was inspected against its source clip."

**3.8** Now: "Figure 4 shows that the resultant variant permutes the color of the Ontological objects, while maintaining the hand pose, bucket and table geometry."
Issue: "resultant" should be "resulting"; "Ontological objects"; "table" is "countertop" everywhere else; missing comma.
Fix: "Fig. 4 shows that the variant recolors the objects in the ontology while keeping the hand pose and the geometry of the bucket and countertop."

**3.9** Now: "We observed that the cleaning motion observed in the before video is maintained by the variant, frame by frame."
Issue: "observed ... observed"; "before video".
Fix: "The wiping motion of the source clip is preserved frame by frame."

**3.10** Now: "We also observed that the background wall and lighting has changed, adding more entropy as desired."
Issue: "wall and lighting has" should be "have"; "as desired" is wrong, since the prompt asked for the countertop only (your own rule 2 in Sec. 2.2 says non-target objects should be preserved); "entropy" for "diversity".
Fix: "The background wall and the lighting also changed. That adds diversity, but it was not requested, and the skin tone of the hand shifted as well; both are the leakage that rule 2 in Sec. 2.2 is meant to prevent."

**3.11** Now: "We see that adding complexity to objects can sometimes add unintended consequences to the variant scene."
Issue: "adding ... add"; "adding complexity to objects" does not describe what happened (several similar objects in one scene).
Fix: "Scenes with several similar objects produce unintended changes."

**3.12** Now: "As observed in Figure 5, we task the data collector to stuff a throw pillow for a chair."
Issue: present tense for a past action; "As observed in".
Fix: "In Fig. 5 the data collector stuffs a throw pillow for a chair."

**3.13** Now: "Employing the pipeline to produce variants, our only request was that the color of the pillow change to blue."
Issue: dangling modifier (the request did not employ the pipeline); the repo's recovered prompt for this clip asked for "a cobalt blue folded blanket" and named the pillow as preserved, so check which clip and prompt Fig. 5 shows.
Fix: "The only requested change was the pillow's color, to blue [VERIFY against the prompt file]."

**3.14** Now: "The variant not only changed the pillow blue but also changed the background chairs blue as well."
Issue: "not only ... but also ... as well" is one connector too many.
Fix: "The variant turned the pillow blue, and the background chairs with it."

**3.15** Now: "We found that poor image segmentation results are the cause here, suggesting the need to fine-tune Canny edge-gradient parameters."
Issue: "We found" claims a diagnosis that was not measured; and the sentence blames segmentation (SAM 2) but proposes tuning Canny (edges), which are different controls. The repo's mask-coverage check found the retained masks for this clip nearly empty, which is a segmentation failure.
Fix: "We attribute this to a near-empty segmentation mask for the clip, which left the segmentation control with nothing to protect; a check on mask coverage before rendering, and tuning of the segmentation and edge weights, are the remedies."

**3.16** Now: "We did observe some limitations in this process, particularly when requesting permutations in the physics of the scene."
Issue: "We did observe" (emphatic "did"); "permutations in the physics".
Fix: "The pipeline fails when the requested change is to the motion rather than the appearance."

**3.17** Now: "In Figure 6, the data collector is taking a phone charger and winding the USB cord around the wall plug in a clockwise direction (with respect to the wall plug)."
Issue: "is taking ... and winding"; "in a clockwise direction (with respect to the wall plug)" is long.
Fix: "In Fig. 6 the data collector winds the USB cord of a phone charger clockwise around its wall plug, as seen from the plug."

**3.18** Now: "Next, we ask the pipeline to wind the cord in the opposite direction, counterclockwise."
Issue: present tense; the repo's recovered Predict2 prompt asked for winding with the block fixed, not a reversal (Shrey to confirm, see `oct-21-status-and-todo.md`, Sec. 4.3).
Fix: "We then asked the pipeline to render the cord winding counterclockwise [VERIFY prompt]."

**3.19** Now: "Surprisingly, the resultant variant was unable to maintain this ask, the spooling wire looked like spaghetti, with the cord gaining linear mass and length at times."
Issue: comma splice after "ask"; "this ask" is colloquial; "resultant"; "gaining linear mass" (a cord gaining mass is what you mean, "linear" adds nothing); "Surprisingly" editorialises.
Fix: "The variant did not follow the instruction: the wound cord looked like spaghetti, and at times it gained length and thickness."

**3.20** Now: "The hands do in fact maintain the same orientation as the original video, but the variant fails to maintain the physics, violating conservation of mass and continuity."
Issue: "do in fact" is filler; "maintain ... maintain"; "as the original video" should be "as in the source clip"; "fails to maintain the physics" is loose.
Fix: "The hands keep the same orientation as in the source clip, but the cord does not keep its length or continuity, so the render violates the physical constraints of the scene."

### Figure captions

**F1** "The Pipeline": fine, but LNCS captions that are not sentences take no period and are centred; this one is. Consider "Pipeline: source clip V to variant V' through Curate, Cosmos 3 Nano, GPT-4o mini, SAM 2, and Cosmos Transfer 2.5" so the caption stands alone.

**F2** Now: "Sample egocentric video, a person wipes a countertop with towel and a bucket."
Issue: comma splice; missing "a" before "towel".
Fix: "Source clip: a person wipes a countertop with a cloth from a bucket."

**F3** "Reasoning output for the scene with object detection bounding boxes, along with JSON Ontology."
Fix: "Cosmos 3 Nano output for the first frame: detected objects with bounding boxes (left) and an excerpt of the JSON ontology (right)."

**F4** Now: "Converting white countertop to blue, rag to blue, bucket to blue and varying the skin color of the human."
Issue: the skin-tone change was leakage, not a requested variation; three "to blue"; missing articles.
Fix: "Source clip (left) and variant with the countertop, cloth, and bucket recolored blue (right). The wall, the lighting, and the skin tone of the hand also changed, none of which was requested."

**F5** Now: "Adding stuffing to a chair pillow"
Fix: "Pillow-stuffing clip: source (left) and variant prompted to turn the pillow blue (right); the chairs turned blue as well."

**F6** Now: "Directional Reversal Experiment (find better example showing spaghetti)"
Issue: author note left in; title case.
Fix: "Cord-winding clip: source (left) and the variant prompted to wind in the opposite direction (right)." Replace the right-hand frame with one that shows the failure described in the text, or describe what the frames actually show.

**F7** Now: "Some examples of variants ... maybe we can find a better example?"
Issue: author note left in; the three panels are not identified.
Fix: "Further variants: the desk clip recolored blue (left), the bed-making clip rendered with a beige bedspread, showing the smearing described in the text (center), and the desk source clip (right) [VERIFY panel order]."

### 4 Closing the Gap

**4.1** Now: "From 3, 10-minute video examples, we used our workflow to create 116 clips to generate 72 variations per clip, producing 8,352 synthetic video variations, or about 35 hours of video from 29 minutes of source data."
Issue: "3, 10-minute" should be "three 10-minute", and it conflicts with eight recordings in Sec. 3; "producing 8,352" claims renders that were not made (64 were rendered; 8,352 is 116 times 72, the capacity); "create 116 clips to generate 72 variations" runs two steps together.
Fix: "From eight recordings, 29 minutes of which survived shot detection as 116 clips, the reasoning stage proposed 72 admissible variations per clip. That is a capacity of 8,352 synthetic clips, about 35 hours of video from 29 minutes of source; we rendered 64 of them."

**4.2** Now: "The number of permuted variants depends upon the number of Ontological objects available to change, along with what physical attributes are within the current limit of the NVIDIA World Model suite."
Issue: "depends upon"; "Ontological objects"; "within the current limit of the NVIDIA World Model suite".
Fix: "The number of variants depends on how many objects the ontology offers to change and on which attributes the current Cosmos models can render."

**4.3** Now: "One 10-minute video became 4 hours without a new scene or room generated."
Issue: the arithmetic does not hold: 10 minutes times 72 is 12 hours. Four hours is 35 hours divided by eight recordings, each of which retained about 3.6 minutes.
Fix: "Each recording, about 3.6 minutes of retained footage, expands to about 4.4 hours of variants without any new scene or room."

**4.4** Now: "It should be noted that at the time of publication, the authors have not quantified how much of this synthetic data is useful."
Issue: "It should be noted that"; "the authors" for "we"; the stronger fact is that no policy was trained.
Fix: "We have not measured how much of this synthetic data helps a policy; no policy was trained on it, and no baseline against random augmentation was run."

**4.5** Now: "Considering the current market rate for raw egocentric data is USD 3 - USD 25 USD per hour, we find that this process can quickly scale a sparse dataset into one with sufficient hours and,diversity, while maintaining the overall physics of the scene."
Issue: "and,diversity" (stray comma, missing space); the currency marked twice; no source for the rate; "we find" for an estimate; "quickly" and "sufficient" are unsupported; "while maintaining the overall physics of the scene" is contradicted by Fig. 6 two paragraphs earlier.
Fix: "Raw egocentric video costs 3 to 25 USD per hour to collect [CITATION NEEDED]. For appearance changes, the pipeline turns a small dataset into a larger and more varied one while keeping the recorded motion."

**4.6** Now: "For every hour processed with our pipeline, we spend USD 96 USD for GPU cloud instance costs (80 A100-hours at 20 minutes per clip) and 0.12 USD in token costs for LLM."
Issue: currency marked twice; "token costs for LLM" (no article, acronym unexpanded). The number itself is the problem: 80 A100-hours per source hour is one Transfer render per clip. Each render is a 15-second clip for 20 minutes of GPU, so an hour of output costs 240 renders times 20 minutes, which is the same 80 A100-hours, or 96 USD at 1.20 USD per A100-hour. That is four to thirty times the quoted cost of collecting an hour of real video, so as written the pipeline is not economical. Draft 7 gave 1.20 USD per hour. One of the two is wrong, or the unit is.
Fix: state the cost per hour of generated video and compare it honestly, or make the argument about diversity rather than price: "Rendering costs about 96 USD per hour of generated video (80 A100-hours at 1.20 USD each, 20 minutes per 15-second clip) plus 0.12 USD in LLM tokens [VERIFY both figures]. That is more than the collection cost of an hour of real video; what the pipeline buys is diversity of appearance on the same recorded motion, which Lin et al. show is the quantity that moves generalization [4]."

**4.7** Now: "For practitioners and academics who have a limited budget for training robot policies, this workflow provides a cohesive and practical solution."
Issue: "cohesive" is the wrong word; "solution" overclaims after 4.4.
Fix: "For groups with a limited budget, the workflow is a practical way to add visual diversity to a small egocentric dataset."

### 5 Conclusion

**5.1** Now: "We describe a multi-model pipeline on NVIDIA Cosmos that turns a real, limited first-person dataset into task-grounded synthetic training variant clips for humanoid robotic policy training."
Issue: "training variant clips ... policy training".
Fix: "We describe a multi-model pipeline on NVIDIA Cosmos that turns a small real first-person dataset into task-grounded synthetic variants for training humanoid manipulation policies."

**5.2** Now: "This workflow provides a scalable solution for academics and practitioners who need more egocentric video to increase an average task completion score."
Issue: "an average" should be "the average"; "scalable solution" is a claim the paper does not test.
Fix: "It is aimed at academics and practitioners who need more, and more varied, egocentric video."

**5.3** Now: "We demonstrate how the workflow is capable of changing appearance for simpler scenes. However, more work must be done for complex scenes."
Issue: "demonstrate how ... is capable of" for "show that ... changes".
Fix: "The workflow changes object appearance in simple scenes; cluttered scenes with several similar objects still bleed color across them."

**5.4** Now: "Additionally, action-level changes (multiple tasks executed within the video) remain unsolved."
Issue: "Additionally"; the parenthesis defines action-level change as "multiple tasks", but the experiment in Sec. 3 was a change to the motion of one task.
Fix: "Action-level changes, where the motion itself is altered as in the cord-winding reversal, remain unsolved."

**5.5** Now: "Lastly, more questions need to be explored, such as does structured reasoning about a scene produce better variations than random augmentation?"
Issue: rhetorical question; "Lastly".
Fix: "Whether structured reasoning produces better variations than random augmentation is untested, since no baseline was run; that experiment is cheap relative to the renders already made and is the next step."

**5.6** Now: "Overall, we have explored NVIDIA Cosmos's models and their current capacity for synthetic video generation for ego centric household data."
Issue: "Overall" plus a closing summary (house rule); "Cosmos's"; "ego centric" is one word; "for ... for".
Fix: delete the sentence. The conclusion already says what was done.

## 3. Things that are not wrong but will draw a reviewer's eye

- The abstract promises "hundreds of permutations" per video; Sec. 4 gives 72 per clip and 64 rendered in total.
- "Reason is a vision-language model" (Sec. 1.1) and Cosmos 3 Nano's "reasoning tower" (Sec. 2) are both described, but the paper never says which was used for what; Sec. 3 then says "Cosmos Reason". One name throughout.
- "location" is listed as a permuted attribute (Sec. 1 para 4) and "state and position" as a variation dimension (Sec. 2.1), but no result changes an object's position.
- The Method says four controls preserve "edge, depth, color, and texture"; Sec. 2.3 lists edge, depth, blurred RGB, and segmentation. Sec. 2.3 is right.
- Sec. 2.3 item 4 promises the mask prevents changes to neighbors; Fig. 4 and Fig. 5 show neighbors changing. Say what the mask does at the weights used, not what it should do.
- The data-scaling figure that carried the introduction's argument in draft 7 is gone; the introduction now cites four papers' numbers with nothing to look at. See README Appendix A for the corrected figure if it is to come back.
- No keywords, no corresponding author email, no Disclosure of Interests (all required by Springer; see `oct-21-status-and-todo.md`, Sec. 4.1).
