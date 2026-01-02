#!/usr/bin/env python3
"""
Create FINAL improved GIFs with Architecture + Multiple Result Images
"""

import os
from PIL import Image
from pathlib import Path

DOWNLOADED_DIR = Path("downloaded_gifs")
OUTPUT_DIR = Path("generated_gifs")
OUTPUT_DIR.mkdir(exist_ok=True)


def create_gif(frames, output_name, duration=1500):
    """Create GIF from list of PIL Image frames."""
    output_path = OUTPUT_DIR / output_name

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


def resize_to_width(img, target_width=600):
    """Resize image to target width maintaining aspect ratio."""
    w, h = img.size
    new_h = int(h * target_width / w)
    return img.resize((target_width, new_h), Image.Resampling.LANCZOS)


def pad_to_same_height(images, bg_color=(255, 255, 255)):
    """Pad all images to same height."""
    max_h = max(img.size[1] for img in images)
    padded = []
    for img in images:
        w, h = img.size
        if h < max_h:
            new_img = Image.new('RGB', (w, max_h), bg_color)
            offset = (max_h - h) // 2
            new_img.paste(img, (0, offset))
            padded.append(new_img)
        else:
            padded.append(img)
    return padded


def main():
    print("=" * 60)
    print("Creating FINAL GIFs with Architecture + Results")
    print("=" * 60)

    # =========================================================================
    # 1. SRDD (Scale-wise VAR) - arXiv 2025
    # Architecture + Intro results + Qualitative comparison
    # =========================================================================
    print("\n1. SRDD / Scale-wise VAR (arXiv 2025)")

    srdd_arch = DOWNLOADED_DIR / "srdd_arch.png"
    srdd_intro = DOWNLOADED_DIR / "srdd_intro_fig.png"
    srdd_qual = DOWNLOADED_DIR / "srdd_qualitative.png"

    if srdd_arch.exists() and srdd_intro.exists():
        images = []

        # Architecture diagram
        img_arch = Image.open(srdd_arch)
        images.append(img_arch)

        # Intro figure with results
        img_intro = Image.open(srdd_intro)
        images.append(img_intro)

        # Qualitative comparison (if exists)
        if srdd_qual.exists():
            img_qual = Image.open(srdd_qual)
            images.append(img_qual)

        # Resize all to same width
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)

        create_gif(frames, "srdd.gif", duration=2000)
    else:
        print("   WARNING: Source images not found")

    # =========================================================================
    # 2. UNITE AND CONQUER (CVPR 2023)
    # Method diagram + Face results + Natural results + Multimodal faces
    # =========================================================================
    print("\n2. Unite and Conquer (CVPR 2023)")

    unite_method = DOWNLOADED_DIR / "unite_method.png"
    unite_faces = DOWNLOADED_DIR / "unite_faces.png"
    unite_natural = DOWNLOADED_DIR / "unite_natural.png"
    unite_multimodal = DOWNLOADED_DIR / "unite_multimodal.png"

    images = []

    if unite_method.exists():
        images.append(Image.open(unite_method))
    if unite_faces.exists():
        images.append(Image.open(unite_faces))
    if unite_natural.exists():
        images.append(Image.open(unite_natural))
    if unite_multimodal.exists():
        images.append(Image.open(unite_multimodal))

    if len(images) >= 2:
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)
        create_gif(frames, "unite_conquer.gif", duration=1800)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 3. SCALING NVS (ICCV 2025) - Keep existing but improve
    # Architecture + Teaser with comparisons
    # =========================================================================
    print("\n3. Scaling Transformer NVS (ICCV 2025)")

    scaling_overview = DOWNLOADED_DIR / "scaling_overview.png"
    scaling_teaser = DOWNLOADED_DIR / "scaling_teaser.png"
    scaling_pca = DOWNLOADED_DIR / "scaling_pca.png"

    images = []
    if scaling_overview.exists():
        images.append(Image.open(scaling_overview))
    if scaling_teaser.exists():
        images.append(Image.open(scaling_teaser))
    if scaling_pca.exists():
        images.append(Image.open(scaling_pca))

    if len(images) >= 2:
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)
        create_gif(frames, "scaling_nvs.gif", duration=2000)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 4. GENDEG (CVPR 2025)
    # Method + Intro + Qualitative results
    # =========================================================================
    print("\n4. GenDeg (CVPR 2025)")

    gendeg_method = DOWNLOADED_DIR / "gendeg_method.png"
    gendeg_intro = DOWNLOADED_DIR / "gendeg_intro.png"
    gendeg_qual = DOWNLOADED_DIR / "gendeg_qual.png"

    images = []
    if gendeg_method.exists():
        images.append(Image.open(gendeg_method))
    if gendeg_intro.exists():
        images.append(Image.open(gendeg_intro))
    if gendeg_qual.exists():
        images.append(Image.open(gendeg_qual))

    if len(images) >= 2:
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)
        create_gif(frames, "gendeg.gif", duration=1800)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 5. MAXFUSION (ECCV 2024)
    # Method + Examples + Results
    # =========================================================================
    print("\n5. MaxFusion (ECCV 2024)")

    maxfusion_method = DOWNLOADED_DIR / "maxfusion_method.png"
    maxfusion_img1 = DOWNLOADED_DIR / "maxfusion_img1.png"
    maxfusion_contra = DOWNLOADED_DIR / "maxfusion_contradictory.png"
    maxfusion_comp = DOWNLOADED_DIR / "maxfusion_complementary.png"

    images = []
    if maxfusion_method.exists():
        images.append(Image.open(maxfusion_method))
    if maxfusion_img1.exists():
        images.append(Image.open(maxfusion_img1))
    if maxfusion_contra.exists():
        images.append(Image.open(maxfusion_contra))
    if maxfusion_comp.exists():
        images.append(Image.open(maxfusion_comp))

    if len(images) >= 2:
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)
        create_gif(frames, "maxfusion.gif", duration=1500)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 6. STEERED DIFFUSION (ICCV 2023)
    # Method + Results
    # =========================================================================
    print("\n6. Steered Diffusion (ICCV 2023)")

    steered_method = DOWNLOADED_DIR / "steered_method.png"
    steered_intro = DOWNLOADED_DIR / "steered_introfig.png"

    images = []
    if steered_method.exists():
        images.append(Image.open(steered_method))
    if steered_intro.exists():
        images.append(Image.open(steered_intro))

    if len(images) >= 2:
        frames = [resize_to_width(img, 550) for img in images]
        frames = pad_to_same_height(frames)
        create_gif(frames, "steered_diffusion.gif", duration=2000)
    else:
        print("   WARNING: Not enough source images")

    # =========================================================================
    # 7. CROWDIFF - Use official GIF
    # =========================================================================
    print("\n7. CrowDiff (CVPR 2024)")

    crowdiff_src = DOWNLOADED_DIR / "crowdiff_shha.gif"
    if crowdiff_src.exists():
        import shutil
        shutil.copy(crowdiff_src, OUTPUT_DIR / "crowdiff.gif")
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

    print("\n" + "=" * 60)
    print("GIF Contents Summary:")
    print("=" * 60)
    print("  srdd.gif: Architecture → Results → Qualitative (3 frames)")
    print("  unite_conquer.gif: Method → Faces → Natural → Multimodal (4 frames)")
    print("  scaling_nvs.gif: Architecture → Teaser → PCA (3 frames)")
    print("  gendeg.gif: Method → Intro → Qualitative (3 frames)")
    print("  maxfusion.gif: Method → Example → Contradictory → Complementary (4 frames)")
    print("  steered_diffusion.gif: Method → Results (2 frames)")
    print("  crowdiff.gif: Official animated density map")


if __name__ == "__main__":
    main()
