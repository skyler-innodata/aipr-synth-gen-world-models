# Masked color-difference (leakage) measurement

Computed 2026-10-16 from the videos embedded in the deck. Script: `leakage_metric.py` (kept in the session scratchpad; copy into `paper/scripts/` before submission).

## What was measured

For the bucket clip (original `video-original-bucket-cleaning.mp4`, generated `video-generated-counter-blue-clean.mp4`, tracked SAM2 mask `video-counter-blue-control-seg.mp4`; all 854×480, 60 frames, 4 fps):

- Per pixel and frame, CIE76 ΔE between original and generated frame in CIELAB.
- Mean ΔE inside the mask (countertop, the region the prompt targeted) and outside it (bucket, paper towels, hand, wall: the region the prompt said to preserve).
- Chroma-only distance (a, b channels) to separate color shift from lightness shift.
- Fraction of protected pixels whose ΔE exceeds 10 and 20. A ΔE of about 2 is a just-noticeable difference; 10 is an obvious color change.

## Results (bucket clip)

| Quantity | Value |
|---|---|
| Frames | 60 |
| Mask coverage (mean fraction of frame) | 0.498 |
| Mean ΔE inside mask (target) | 75.5 (std over frames 4.0) |
| Mean ΔE outside mask (protected) | 34.8 (std over frames 7.2) |
| Mean chroma-only ΔE inside / outside | 68.2 / 24.2 |
| Ratio outside / inside | 0.46 |
| Protected pixels with ΔE > 10 | 94.5% |
| Protected pixels with ΔE > 20 | 65.3% |

Files: `bucket/leakage_per_frame.csv`, `bucket/leakage_summary.txt`, `bucket/leakage_per_frame.{pdf,png}`, heatmaps and matched frames at t = 0, 30, 59.

## Reading

The target region moved by a large margin, so the recolor succeeded. The protected region moved by almost half as much, and nearly every protected pixel changed by a visible amount. The chroma-only figure shows that the protected-region change is mostly color, not just exposure. This is a direct measurement of what the slide notes described qualitatively: blue bled into the towels and bucket, and the wall tone shifted.

## Shelf and pillow masks received 2026-10-16 (`segmentation/`)

Both files have the right geometry (shelf 270×480, pillow 854×480, 60 frames at 4 fps) but are almost entirely black:

| File | Mean white fraction per frame | Max in any frame |
|---|---|---|
| `seg_mask_shelf_clip.mp4` | 0.001 | 0.006 |
| `seg_mask_pillow.mp4` | 0.025 | 0.039 |

Frame 30 of each is saved in `mask-check/`. Neither resembles the furniture mask (about half the frame) shown in Shrey's PDF answer. Two readings are possible and they lead to different papers:

1. **Wrong export.** The intended `seg_mask.mp4` exists elsewhere and these are a different artifact. Then the leakage rows for shelf and pillow simply wait for the right files.
2. **These are the masks that were actually fed to Transfer.** Then the seg control carried almost no information for those two runs, and the whole-frame recoloring on slides 14 and 16 is explained directly: there was no mask to leak out of. That would be a real finding (SAM2 propagation collapsed on these clips) and would change the paper's account of why multi-texture scenes failed.

The leakage metric was not run on these masks; with 0.1% coverage the inside/outside split is meaningless. Shrey needs to say which reading is correct.

## Caveats

- One clip. The shelf and pillow clips have no mask video in the deck, so the same measurement cannot be run on them from the extracted assets. If Shrey can export `seg_mask.mp4` for those runs, the script runs unchanged.
- The mask is SAM2's tracked output, which has its own errors. Pixels misassigned by SAM2 near object borders will inflate "outside" ΔE slightly. The effect is small relative to a 35-unit mean.
- CIE76 is used for simplicity. CIEDE2000 would compress large differences but would not change the conclusion.
