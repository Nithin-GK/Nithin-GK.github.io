#!/usr/bin/env python3
"""
Create GIFs for SELECTED publications only.
These are the papers marked as selected={true} in papers.bib
"""

import os
from PIL import Image
from pathlib import Path

# Output directory for generated GIFs
OUTPUT_DIR = Path("generated_gifs")
OUTPUT_DIR.mkdir(exist_ok=True)

# Source images directory
DOWNLOADED_DIR = Path("downloaded_gifs")


def create_gif_from_frames(frames, output_name, duration=800):
    """Create GIF from list of PIL Image frames."""
    output_path = OUTPUT_DIR / output_name
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    print(f"  Created: {output_name} ({len(frames)} frames, {duration}ms each)")
    return output_path


def crop_and_create_gif(image_path, crop_regions, output_name, duration=800, resize=None):
    """Crop regions from image and create GIF."""
    img = Image.open(image_path)
    frames = []

    for region in crop_regions:
        cropped = img.crop(region)
        if cropped.mode in ('RGBA', 'P'):
            cropped = cropped.convert('RGB')
        if resize:
            cropped = cropped.resize(resize, Image.Resampling.LANCZOS)
        frames.append(cropped)

    return create_gif_from_frames(frames, output_name, duration)


def main():
    print("=" * 60)
    print("Creating GIFs for SELECTED Publications")
    print("=" * 60)

    # =========================================================================
    # 1. STEERED DIFFUSION (ICCV 2023) - selected=true
    # Show different conditional tasks: inpainting, colorization, SR, etc.
    # =========================================================================
    print("\n1. Steered Diffusion (ICCV 2023)")

    # Using the intro figure which shows multiple task results
    steered_intro = DOWNLOADED_DIR / "steered_introfig.png"
    if steered_intro.exists():
        img = Image.open(steered_intro)
        w, h = img.size
        print(f"   Source: {steered_intro} ({w}x{h})")

        # The intro figure shows results in columns - crop different result sections
        # Split into 4 horizontal sections
        num_sections = 4
        section_width = w // num_sections

        frames = []
        for i in range(num_sections):
            left = i * section_width
            right = (i + 1) * section_width
            cropped = img.crop((left, 0, right, h)).convert('RGB')
            # Resize to consistent size
            cropped = cropped.resize((300, int(300 * h / section_width)), Image.Resampling.LANCZOS)
            frames.append(cropped)

        create_gif_from_frames(frames, "steered_diffusion.gif", duration=1000)
    else:
        print(f"   WARNING: {steered_intro} not found")

    # =========================================================================
    # 2. UNITE AND CONQUER (CVPR 2023) - selected=true
    # Show face generation and natural image results
    # =========================================================================
    print("\n2. Unite and Conquer (CVPR 2023)")

    faces_img = DOWNLOADED_DIR / "unite_faces.png"
    natural_img = DOWNLOADED_DIR / "unite_natural.png"

    if faces_img.exists() and natural_img.exists():
        img1 = Image.open(faces_img).convert('RGB')
        img2 = Image.open(natural_img).convert('RGB')

        # Resize to same dimensions
        target_size = (400, 300)
        img1 = img1.resize(target_size, Image.Resampling.LANCZOS)
        img2 = img2.resize(target_size, Image.Resampling.LANCZOS)

        create_gif_from_frames([img1, img2], "unite_conquer.gif", duration=1500)
    else:
        print(f"   WARNING: Source images not found")

    # =========================================================================
    # 3. MAXFUSION (ECCV 2024) - selected=true
    # Toggle between contradictory and complementary results
    # =========================================================================
    print("\n3. MaxFusion (ECCV 2024)")

    contra_img = DOWNLOADED_DIR / "maxfusion_contradictory.png"
    comp_img = DOWNLOADED_DIR / "maxfusion_complementary.png"

    if contra_img.exists() and comp_img.exists():
        img1 = Image.open(contra_img).convert('RGB')
        img2 = Image.open(comp_img).convert('RGB')

        # Resize to same dimensions
        target_size = (500, 350)
        img1 = img1.resize(target_size, Image.Resampling.LANCZOS)
        img2 = img2.resize(target_size, Image.Resampling.LANCZOS)

        create_gif_from_frames([img1, img2], "maxfusion.gif", duration=1500)
    else:
        print(f"   WARNING: Source images not found")

    # =========================================================================
    # 4. GENDEG (CVPR 2025) - selected=true
    # Show degradation synthesis results
    # =========================================================================
    print("\n4. GenDeg (CVPR 2025)")

    gendeg_intro = DOWNLOADED_DIR / "gendeg_intro.png"
    gendeg_qual = DOWNLOADED_DIR / "gendeg_qual.png"

    if gendeg_intro.exists() and gendeg_qual.exists():
        img1 = Image.open(gendeg_intro).convert('RGB')
        img2 = Image.open(gendeg_qual).convert('RGB')

        # Resize to same dimensions
        target_size = (500, 350)
        img1 = img1.resize(target_size, Image.Resampling.LANCZOS)
        img2 = img2.resize(target_size, Image.Resampling.LANCZOS)

        create_gif_from_frames([img1, img2], "gendeg.gif", duration=1500)
    else:
        print(f"   WARNING: Source images not found")

    # =========================================================================
    # 5. SCALING TRANSFORMER NVS (ICCV 2025) - selected=true
    # Create from existing preview image by cropping different views
    # =========================================================================
    print("\n5. Scaling Transformer NVS (ICCV 2025)")

    scaling_img = Path("scalingtransformer.png")
    if scaling_img.exists():
        img = Image.open(scaling_img)
        w, h = img.size
        print(f"   Source: {scaling_img} ({w}x{h})")

        # Split image into sections (left: input views, right: novel views)
        left_region = img.crop((0, 0, w // 2, h)).convert('RGB')
        right_region = img.crop((w // 2, 0, w, h)).convert('RGB')

        # Resize to consistent size
        target_size = (350, int(350 * h / (w // 2)))
        left_region = left_region.resize(target_size, Image.Resampling.LANCZOS)
        right_region = right_region.resize(target_size, Image.Resampling.LANCZOS)

        create_gif_from_frames([left_region, right_region], "scaling_nvs.gif", duration=1200)
    else:
        print(f"   WARNING: {scaling_img} not found")

    # =========================================================================
    # 6. SCALE-WISE VAR (arXiv 2025) - selected=true
    # Create from existing SRDD.png
    # =========================================================================
    print("\n6. Scale-wise VAR / SRDD (arXiv 2025)")

    srdd_img = Path("SRDD.png")
    if srdd_img.exists():
        img = Image.open(srdd_img)
        w, h = img.size
        print(f"   Source: {srdd_img} ({w}x{h})")

        # This image likely shows scale-wise generation
        # Split into sections to show progression
        num_sections = 3
        section_width = w // num_sections

        frames = []
        for i in range(num_sections):
            left = i * section_width
            right = (i + 1) * section_width
            cropped = img.crop((left, 0, right, h)).convert('RGB')
            cropped = cropped.resize((300, int(300 * h / section_width)), Image.Resampling.LANCZOS)
            frames.append(cropped)

        create_gif_from_frames(frames, "srdd.gif", duration=1000)
    else:
        print(f"   WARNING: {srdd_img} not found")

    # =========================================================================
    # SUMMARY
    # =========================================================================
    print("\n" + "=" * 60)
    print("GIF Generation Complete!")
    print("=" * 60)

    print(f"\nOutput directory: {OUTPUT_DIR.absolute()}")
    print("\nGenerated GIFs:")
    for gif in sorted(OUTPUT_DIR.glob("*.gif")):
        size_kb = gif.stat().st_size / 1024
        print(f"  - {gif.name} ({size_kb:.1f} KB)")

    print("\nTo use these GIFs, update papers.bib preview fields:")
    print("  preview={steered_diffusion.gif}")
    print("  preview={unite_conquer.gif}")
    print("  preview={maxfusion.gif}")
    print("  preview={gendeg.gif}")
    print("  preview={scaling_nvs.gif}")
    print("  preview={srdd.gif}")


if __name__ == "__main__":
    main()
