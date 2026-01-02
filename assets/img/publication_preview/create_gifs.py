#!/usr/bin/env python3
"""
GIF Creator for Publication Thumbnails
=======================================
This script creates animated GIFs from image frames for paper thumbnails.

Usage:
    python create_gifs.py

Requirements:
    pip install Pillow imageio

The script provides two modes:
1. Create GIF from multiple frames (for multi-step animations)
2. Create toggle GIF from 2 images (before/after style)
"""

import os
from PIL import Image
import imageio
from pathlib import Path


def create_gif_from_frames(
    frame_paths: list,
    output_path: str,
    duration: float = 0.5,
    loop: int = 0,
    resize: tuple = None
):
    """
    Create a GIF from multiple image frames.

    Args:
        frame_paths: List of paths to image frames (in order)
        output_path: Output path for the GIF
        duration: Duration of each frame in seconds (default 0.5s)
        loop: Number of loops (0 = infinite)
        resize: Optional tuple (width, height) to resize all frames
    """
    frames = []

    for path in frame_paths:
        img = Image.open(path)

        # Convert to RGB if necessary (GIFs don't support alpha well)
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # Resize if specified
        if resize:
            img = img.resize(resize, Image.Resampling.LANCZOS)

        frames.append(img)

    # Save as GIF
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=int(duration * 1000),  # Convert to milliseconds
        loop=loop
    )

    print(f"✓ Created GIF: {output_path}")
    print(f"  Frames: {len(frames)}, Duration: {duration}s per frame")


def create_toggle_gif(
    image1_path: str,
    image2_path: str,
    output_path: str,
    duration: float = 0.8,
    resize: tuple = None
):
    """
    Create a simple 2-frame toggle GIF (before/after style).

    Args:
        image1_path: Path to first image
        image2_path: Path to second image
        output_path: Output path for the GIF
        duration: Duration of each frame in seconds
        resize: Optional tuple (width, height) to resize
    """
    create_gif_from_frames(
        [image1_path, image2_path],
        output_path,
        duration=duration,
        resize=resize
    )


def create_fade_gif(
    image1_path: str,
    image2_path: str,
    output_path: str,
    num_frames: int = 10,
    duration: float = 0.1,
    resize: tuple = None
):
    """
    Create a GIF that fades between two images.

    Args:
        image1_path: Path to first image
        image2_path: Path to second image
        output_path: Output path for the GIF
        num_frames: Number of transition frames
        duration: Duration of each frame in seconds
        resize: Optional tuple (width, height) to resize
    """
    img1 = Image.open(image1_path).convert('RGB')
    img2 = Image.open(image2_path).convert('RGB')

    if resize:
        img1 = img1.resize(resize, Image.Resampling.LANCZOS)
        img2 = img2.resize(resize, Image.Resampling.LANCZOS)

    # Ensure same size
    if img1.size != img2.size:
        img2 = img2.resize(img1.size, Image.Resampling.LANCZOS)

    frames = []

    # Fade from img1 to img2
    for i in range(num_frames):
        alpha = i / (num_frames - 1)
        blended = Image.blend(img1, img2, alpha)
        frames.append(blended)

    # Hold on img2
    for _ in range(5):
        frames.append(img2)

    # Fade from img2 to img1
    for i in range(num_frames):
        alpha = i / (num_frames - 1)
        blended = Image.blend(img2, img1, alpha)
        frames.append(blended)

    # Hold on img1
    for _ in range(5):
        frames.append(img1)

    # Save
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=int(duration * 1000),
        loop=0
    )

    print(f"✓ Created fade GIF: {output_path}")


def batch_create_toggle_gifs(config: dict, output_dir: str = "."):
    """
    Batch create toggle GIFs from a configuration dictionary.

    Args:
        config: Dictionary with format:
            {
                "paper_name": {
                    "before": "path/to/before.png",
                    "after": "path/to/after.png",
                    "duration": 0.8  # optional
                }
            }
        output_dir: Directory to save GIFs
    """
    for paper_name, settings in config.items():
        output_path = os.path.join(output_dir, f"{paper_name}.gif")
        duration = settings.get("duration", 0.8)

        create_toggle_gif(
            settings["before"],
            settings["after"],
            output_path,
            duration=duration
        )


# ============================================================================
# EXAMPLE CONFIGURATIONS FOR YOUR PAPERS
# ============================================================================
#
# After extracting figures from your papers, update these paths and run the script.
# The script expects you to have extracted the relevant figures as PNG/JPG files.

PAPER_CONFIGS = {
    # Example: T2V-DDPM (Thermal to Visible) - simple toggle
    # "t2v_ddpm": {
    #     "before": "frames/t2v_thermal.png",      # Thermal input
    #     "after": "frames/t2v_visible.png",       # Generated visible
    #     "duration": 1.0
    # },

    # Example: AT-DDPM (Turbulence Mitigation) - multi-frame
    # To use: uncomment and provide frame paths
    # "at_ddpm_frames": [
    #     "frames/at_ddpm_degraded.png",
    #     "frames/at_ddpm_step1.png",
    #     "frames/at_ddpm_step2.png",
    #     "frames/at_ddpm_restored.png",
    # ],

    # Example: GenDeg - cycle through degradations
    # "gendeg_frames": [
    #     "frames/gendeg_clean.png",
    #     "frames/gendeg_haze.png",
    #     "frames/gendeg_rain.png",
    #     "frames/gendeg_snow.png",
    #     "frames/gendeg_blur.png",
    #     "frames/gendeg_lowlight.png",
    #     "frames/gendeg_raindrop.png",
    # ],

    # Example: DDPM-CD (Change Detection) - 3 frame
    # "ddpm_cd_frames": [
    #     "frames/ddpmcd_time1.png",
    #     "frames/ddpmcd_time2.png",
    #     "frames/ddpmcd_change_mask.png",
    # ],
}


def main():
    """Main function with interactive menu."""
    print("=" * 60)
    print("Publication Thumbnail GIF Creator")
    print("=" * 60)
    print()
    print("Options:")
    print("1. Create toggle GIF (2 images: before/after)")
    print("2. Create multi-frame GIF")
    print("3. Create fade GIF (smooth transition between 2 images)")
    print("4. Run batch from config (edit PAPER_CONFIGS in script)")
    print("5. Exit")
    print()

    choice = input("Select option (1-5): ").strip()

    if choice == "1":
        print("\n--- Create Toggle GIF ---")
        img1 = input("Path to first image (before): ").strip()
        img2 = input("Path to second image (after): ").strip()
        output = input("Output filename (e.g., paper_name.gif): ").strip()
        duration = input("Duration per frame in seconds [0.8]: ").strip()
        duration = float(duration) if duration else 0.8

        create_toggle_gif(img1, img2, output, duration=duration)

    elif choice == "2":
        print("\n--- Create Multi-Frame GIF ---")
        print("Enter frame paths one per line. Enter empty line when done.")
        frames = []
        while True:
            path = input(f"Frame {len(frames) + 1}: ").strip()
            if not path:
                break
            frames.append(path)

        if len(frames) < 2:
            print("Need at least 2 frames!")
            return

        output = input("Output filename (e.g., paper_name.gif): ").strip()
        duration = input("Duration per frame in seconds [0.5]: ").strip()
        duration = float(duration) if duration else 0.5

        create_gif_from_frames(frames, output, duration=duration)

    elif choice == "3":
        print("\n--- Create Fade GIF ---")
        img1 = input("Path to first image: ").strip()
        img2 = input("Path to second image: ").strip()
        output = input("Output filename (e.g., paper_name.gif): ").strip()

        create_fade_gif(img1, img2, output)

    elif choice == "4":
        print("\n--- Running Batch Config ---")
        if not PAPER_CONFIGS:
            print("No configs defined! Edit PAPER_CONFIGS in the script.")
            return

        for name, config in PAPER_CONFIGS.items():
            if isinstance(config, dict):
                # Toggle GIF config
                create_toggle_gif(
                    config["before"],
                    config["after"],
                    f"{name}.gif",
                    duration=config.get("duration", 0.8)
                )
            elif isinstance(config, list):
                # Multi-frame config
                create_gif_from_frames(config, f"{name}.gif")

    elif choice == "5":
        print("Goodbye!")
        return
    else:
        print("Invalid option!")


if __name__ == "__main__":
    main()
