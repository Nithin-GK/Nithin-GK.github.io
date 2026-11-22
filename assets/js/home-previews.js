document.querySelectorAll("[data-paper-preview]").forEach((preview) => {
  const link = preview.querySelector("[data-preview-control]");
  if (!link) return;

  const button = document.createElement("button");
  button.type = "button";
  button.className = link.className;
  button.append(...link.childNodes);
  link.replaceWith(button);

  const playLabel = link.getAttribute("aria-label");
  const video = document.createElement("video");
  video.muted = true;
  video.playsInline = true;
  video.hidden = true;
  video.setAttribute("aria-hidden", "true");
  preview.insertBefore(video, button);

  function showState(playing) {
    button.setAttribute("aria-pressed", String(playing));
    button.setAttribute("aria-label", playing ? playLabel.replace(/^Play/, "Pause") : playLabel);
    button.title = playing ? "Pause preview" : "Play preview";
  }

  showState(false);
  button.addEventListener("click", () => {
    if (!video.paused) {
      video.pause();
      return;
    }

    document.querySelectorAll("[data-paper-preview] video").forEach((other) => {
      if (other !== video) other.pause();
    });
    if (!video.src) video.src = link.href;
    video.play().catch((error) => {
      if (error.name !== "AbortError") {
        // Keep the original media link available if inline playback is unsupported.
        link.append(...button.childNodes);
        button.replaceWith(link);
        video.remove();
      }
    });
  });
  video.addEventListener("play", () => {
    video.hidden = false;
    showState(true);
  });
  video.addEventListener("pause", () => showState(false));
  video.addEventListener("ended", () => {
    video.hidden = true;
    showState(false);
  });
});
