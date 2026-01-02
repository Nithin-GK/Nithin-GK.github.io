#!/usr/bin/env python3
"""
Create IMPROVED GIFs for selected publications.
Each GIF combines: Architecture diagram + Result images
"""

import os
from PIL import Image
from pathlib import Path

# Directories
DOWNLOADED_DIR = Path("downloaded_gifs")
OUTPUT_DIR = Path("generated_gifs")
OUTPUT_DIR.mkdir(exist_ok=True)


def create_gif(frames, output_name, duration=1200):
    """Create GIF from list of PIL Image frames."""
    output_path = OUTPUT_DIR / output_name

    # Convert all frames to RGB
    rgb_frames = []
    for f in frames:
        if f.mode in ('RGBA', 'P'):
            f = f.convert('RGB')
        rgb_frames.append(f)

    rgb_frames[0].save(
        output_path,
        save_all=True,
        append_images=rgb_frames[1:],
        duration=duration,
        loop=0
    )
    print(f"  Created: {output_name} ({len(rgb_frames)} frames, {duration}ms each)")
    return output_path


def resize_to_match(images, target_width=600):
    """Resize all images to same width, maintaining aspect ratio."""
    resized = []
    for img in images:
        w, h = img.size
        new_h = int(h * target_width / w)
        resized.append(img.resize((target_width, new_h), Image.Resampling.LANCZOS))
    return resized


def pad_to_same_height(images, bg_color=(255, 255, 255)):
    """Pad all images to the same height (max height among them)."""
    max_h = max(img.size[1] for img in images)
    padded = []
    for img in images:
        w, h = img.size
        if h < max_h:
            # Create new image with padding
            new_img = Image.new('RGB', (w, max_h), bg_color)
            # Center vertically
            offset = (max_h - h) // 2
            new_img.paste(img, (0, offset))
            padded.append(new_img)
        else:
            padded.append(img)
    return padded


def main():
    print("=" * 60)
    print("Creating IMPROVED GIFs (Architecture + Results)")
    print("=" * 60)

    # =========================================================================
    # 1. SCALING TRANSFORMER NVS (ICCV 2025) - selected=true
    # Architecture overview + Teaser results
    # =========================================================================
    print("\n1. Scaling Transformer NVS (ICCV 2025)")

    overview = DOWNLOADED_DIR / "scaling_overview.png"
    teaser = DOWNLOADED_DIR / "scaling_teaser.png"

    if overview.exists() and teaser.exists():
        img_arch = Image.open(overview)
        img_results = Image.open(teaser)

        # Resize to same width
        frames = resize_to_match([img_arch, img_results], target_width=600)
        frames = pad_to_same_height(frames)

        create_gif(frames, "scaling_nvs.gif", duration=2000)
    else:
        print("   WARNING: Source images not found")

    # =========================================================================
    # 2. GENDEG (CVPR 2025) - selected=true
    # Method diagram + Qualitative results
    # =========================================================================
    print("\n2. GenDeg (CVPR 2025)")

    method = DOWNLOADED_DIR / "gendeg_method.png"
    qual = DOWNLOADED_DIR / "gendeg_qual.png"
    intro = DOWNLOADED_DIR / "gendeg_intro.png"

    if method.exists() and qual.exists():
        img_method = Image.open(method)
        img_qual = Image.open(qual)
        img_intro = Image.open(intro) if intro.exists() else None

        images = [img_method, img_qual]
        if img_intro:
            images.append(img_intro)

        frames = resize_to_match(images, target_width=600)
        frames = pad_to_same_height(frames)

        create_gif(frames, "gendeg.gif", duration=1800)
    else:
        print("   WARNING: Source images not found")

    # =========================================================================
    # 3. MAXFUSION (ECCV 2024) - selected=true
    # Method + Contradictory results + Complementary results
    # =========================================================================
    print("\n3. MaxFusion (ECCV 2024)")

    method = DOWNLOADED_DIR / "maxfusion_method.png"
    img1 = DOWNLOADED_DIR / "maxfusion_img1.png"
    img2 = DOWNLOADED_DIR / "maxfusion_img2.png"
    contra = DOWNLOADED_DIR / "maxfusion_contradictory.png"
    comp = DOWNLOADED_DIR / "maxfusion_complementary.png"

    images_to_use = []
    if method.exists():
        images_to_use.append(Image.open(method))
    if img1.exists():
        images_to_use.append(Image.open(img1))
    if contra.exists():
        images_to_use.append(Image.open(contra))
    if comp.exists():
        images_to_use.append(Image.open(comp))

    if len(images_to_use) >= 2:
        frames = resize_to_match(images_to_use, target_width=550)
        frames = pad_to_same_height(frames)
        create_gif(frames, "maxfusion.gif", duration=1500)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 4. STEERED DIFFUSION (ICCV 2023) - selected=true
    # Method diagram + Results
    # =========================================================================
    print("\n4. Steered Diffusion (ICCV 2023)")

    method = DOWNLOADED_DIR / "steered_method.png"
    intro = DOWNLOADED_DIR / "steered_introfig.png"

    if method.exists() and intro.exists():
        img_method = Image.open(method)
        img_intro = Image.open(intro)

        frames = resize_to_match([img_method, img_intro], target_width=600)
        frames = pad_to_same_height(frames)

        create_gif(frames, "steered_diffusion.gif", duration=2000)
    else:
        print("   WARNING: Source images not found")

    # =========================================================================
    # 5. UNITE AND CONQUER (CVPR 2023) - selected=true
    # Face results + Natural scene results
    # =========================================================================
    print("\n5. Unite and Conquer (CVPR 2023)")

    faces = DOWNLOADED_DIR / "unite_faces.png"
    natural = DOWNLOADED_DIR / "unite_natural.png"

    if faces.exists() and natural.exists():
        img_faces = Image.open(faces)
        img_natural = Image.open(natural)

        frames = resize_to_match([img_faces, img_natural], target_width=550)
        frames = pad_to_same_height(frames)

        create_gif(frames, "unite_conquer.gif", duration=2000)
    else:
        print("   WARNING: Source images not found")

    # =========================================================================
    # 6. SCALE-WISE VAR / SRDD (arXiv 2025) - selected=true
    # Use existing preview image - it's already good
    # =========================================================================
    print("\n6. Scale-wise VAR / SRDD (arXiv 2025)")

    srdd = Path("SRDD.png")
    if srdd.exists():
        img = Image.open(srdd)
        # This image is already a good representation
        # Just copy it as a single-frame "GIF" for consistency
        img_rgb = img.convert('RGB')
        img_rgb.save(OUTPUT_DIR / "srdd.gif")
        print(f"  Created: srdd.gif (1 frame - already good preview)")
    else:
        print("   WARNING: SRDD.png not found")

    # =========================================================================
    # BONUS: CrowDiff - already has great GIFs from the repo
    # Just copy one of them
    # =========================================================================
    print("\n7. CrowDiff (CVPR 2024) - Using official GIF")

    crowdiff_gif = DOWNLOADED_DIR / "crowdiff_shha.gif"
    if crowdiff_gif.exists():
        import shutil
        shutil.copy(crowdiff_gif, OUTPUT_DIR / "crowdiff.gif")
        print(f"  Copied: crowdiff.gif (official animated density map)")

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


if __name__ == "__main__":
    main()
