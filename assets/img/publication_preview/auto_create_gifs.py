#!/usr/bin/env python3
"""
Auto GIF Creator - Creates GIFs by cropping regions from existing preview images
"""

import os
from PIL import Image
from pathlib import Path

OUTPUT_DIR = Path("generated_gifs")
OUTPUT_DIR.mkdir(exist_ok=True)

def create_gif_from_crops(image_path, crop_regions, output_name, duration=800):
    """
    Create a GIF by cropping multiple regions from a single image.

    Args:
        image_path: Path to source image
        crop_regions: List of (left, upper, right, lower) tuples
        output_name: Output GIF filename
        duration: Duration per frame in ms
    """
    img = Image.open(image_path)
    frames = []

    for region in crop_regions:
        cropped = img.crop(region)
        if cropped.mode in ('RGBA', 'P'):
            cropped = cropped.convert('RGB')
        frames.append(cropped)

    # Save GIF
    output_path = OUTPUT_DIR / output_name
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    print(f"Created: {output_path}")
    return output_path


def create_toggle_gif(img1_path, img2_path, output_name, duration=800, resize=None):
    """Create a toggle GIF from two separate images."""
    img1 = Image.open(img1_path).convert('RGB')
    img2 = Image.open(img2_path).convert('RGB')

    if resize:
        img1 = img1.resize(resize, Image.Resampling.LANCZOS)
        img2 = img2.resize(resize, Image.Resampling.LANCZOS)

    # Ensure same size
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.Resampling.LANCZOS)

    output_path = OUTPUT_DIR / output_name
    img1.save(
        output_path,
        save_all=True,
        append_images=[img2],
        duration=duration,
        loop=0
    )
    print(f"Created: {output_path}")
    return output_path


def main():
    print("=" * 60)
    print("Creating GIFs from existing preview images...")
    print("=" * 60)

    # =========================================================================
    # 1. STEERED DIFFUSION - Cycle through different tasks
    # The image shows: Inpainting, Colorization, Super-resolution,
    # Semantic Generation, Identity Replication, Text-based editing
    # =========================================================================
    print("\n1. Steered Diffusion - Multi-task GIF")
    img = Image.open("steered.png")
    w, h = img.size
    # Image has 6 columns (tasks), 2 rows (Input, Generated)
    # We'll crop each task's "Generated Samples" column
    col_width = w // 6
    row_height = h // 2

    # Crop the "Generated Samples" from each task (bottom half of each column)
    steered_crops = []
    for i in range(6):
        left = i * col_width + col_width // 3  # Skip "Input" part
        upper = row_height // 2  # Get generated samples row
        right = (i + 1) * col_width - 10
        lower = h - 20
        steered_crops.append((left, upper, right, lower))

    create_gif_from_crops("steered.png", steered_crops, "steered_tasks.gif", duration=700)

    # =========================================================================
    # 2. MAXFUSION - Toggle between conditions and composite
    # =========================================================================
    print("\n2. MaxFusion - Condition to composite GIF")
    img = Image.open("maxfusion.png")
    w, h = img.size
    # Left side: conditions, Right side: composite results
    # Create a simple left-right toggle
    left_region = (0, 0, w // 2, h)
    right_region = (w // 2, 0, w, h)
    create_gif_from_crops("maxfusion.png", [left_region, right_region], "maxfusion_toggle.gif", duration=1000)

    # =========================================================================
    # 3. BINOISING - Diffusion process comparison
    # Top row: standard diffusion, Bottom row: bi-noising
    # =========================================================================
    print("\n3. Bi-Noising - Diffusion comparison GIF")
    img = Image.open("binoising.png")
    w, h = img.size
    # Get the face sequence from top and bottom
    # The image shows diffusion steps - crop individual faces
    # Top row y: ~0 to h/2, Bottom row y: ~h/2 to h
    # There are multiple face images in sequence

    # Just do top vs bottom toggle showing the improvement
    top_region = (0, 0, w, h // 2 - 20)
    bottom_region = (0, h // 2 + 20, w, h)
    create_gif_from_crops("binoising.png", [top_region, bottom_region], "binoising_compare.gif", duration=1200)

    # =========================================================================
    # 4. MAITREYA WACV (Diffuse and Restore) - Training vs Inference
    # =========================================================================
    print("\n4. Diffuse and Restore - Process GIF")
    img = Image.open("maitreya_wacv.png")
    w, h = img.size
    # Left: Training Stage, Right: Inference Stage
    left_region = (0, 0, w // 2, h)
    right_region = (w // 2, 0, w, h)
    create_gif_from_crops("maitreya_wacv.png", [left_region, right_region], "diffuse_restore.gif", duration=1500)

    # =========================================================================
    # 5. UNITE AND CONQUER (multi.png) - GLIDE vs OURS comparison
    # =========================================================================
    print("\n5. Unite and Conquer - Method comparison GIF")
    img = Image.open("multi.png")
    w, h = img.size
    # Image shows GLIDE [21] on left, OURS on right for top section
    # Bottom shows semantic label to face and sketch to face

    # Top section: GLIDE vs OURS (approximately top 60% of image)
    top_h = int(h * 0.55)
    glide_region = (0, 0, w // 2, top_h)
    ours_region = (w // 2, 0, w, top_h)
    create_gif_from_crops("multi.png", [glide_region, ours_region], "unite_conquer_compare.gif", duration=1200)

    # =========================================================================
    # 6. AT-DDPM (wacv_img.png) - Training vs Inference pipeline
    # =========================================================================
    print("\n6. AT-DDPM - Pipeline GIF")
    img = Image.open("wacv_img.png")
    w, h = img.size
    # Left: Training, Right: Inference
    left_region = (0, 0, w // 2, h)
    right_region = (w // 2, 0, w, h)
    create_gif_from_crops("wacv_img.png", [left_region, right_region], "at_ddpm_pipeline.gif", duration=1500)

    # =========================================================================
    # 7. GENDEG - Degradation synthesis (architecture + examples)
    # =========================================================================
    print("\n7. GenDeg - Architecture vs Results GIF")
    img = Image.open("gendeg.png")
    w, h = img.size
    # The image has (a) architecture, (b) degradation generator, (c) examples
    # Approximately: (a) takes left ~45%, (b) and (c) take right side
    left_region = (0, 0, int(w * 0.45), h)
    right_region = (int(w * 0.45), 0, w, h)
    create_gif_from_crops("gendeg.png", [left_region, right_region], "gendeg_toggle.gif", duration=1500)

    # =========================================================================
    # 8. T2V-DDPM (th_vis.png) - Show diffusion process
    # =========================================================================
    print("\n8. T2V-DDPM - Diffusion process GIF")
    img = Image.open("th_vis.png")
    w, h = img.size
    # The image shows the diffusion chain - we can crop the face images
    # showing progression from thermal to visible
    # Faces appear at: top-left (thermal pair), middle (intermediate), right (visible)

    # Simplified: left vs right showing thermal input vs visible output
    left_region = (0, 0, w // 3, h)
    right_region = (2 * w // 3, 0, w, h)
    create_gif_from_crops("th_vis.png", [left_region, right_region], "t2v_ddpm.gif", duration=1000)

    # =========================================================================
    # 9. DDPM-CD - Show the change detection pipeline
    # =========================================================================
    print("\n9. DDPM-CD - Change detection GIF")
    img = Image.open("ddpmcd.png")
    w, h = img.size
    # Image shows: Input images (left), Pipeline (middle), Change mask (right)
    # Crop the satellite images and change mask

    # Get the input pair (top-left and bottom-left satellite images)
    input_region = (0, 0, int(w * 0.15), h)
    # Get the change mask (far right)
    output_region = (int(w * 0.85), 0, w, h)
    create_gif_from_crops("ddpmcd.png", [input_region, output_region], "ddpmcd_change.gif", duration=1200)

    # =========================================================================
    # 10. CROWDIFF - Crowd counting results
    # =========================================================================
    print("\n10. CrowDiff")
    img = Image.open("crowdiff.png")
    w, h = img.size
    # Just create a simple zoom effect or split if there's before/after
    # For now, let's skip if it's just a single result image
    print("    Skipping - single result image (consider adding comparison frames)")

    print("\n" + "=" * 60)
    print(f"GIFs created in: {OUTPUT_DIR.absolute()}")
    print("=" * 60)

    # List all created GIFs
    print("\nCreated GIFs:")
    for gif in OUTPUT_DIR.glob("*.gif"):
        size = gif.stat().st_size / 1024
        print(f"  - {gif.name} ({size:.1f} KB)")


if __name__ == "__main__":
    main()
