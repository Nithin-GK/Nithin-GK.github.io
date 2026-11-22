(() => {
  "use strict";
  document.querySelectorAll("[data-slide-viewer]").forEach((viewer) => {
    const slides = Array.from(viewer.querySelectorAll("[data-slide]"));
    if (slides.length < 2) return;
    const stage = viewer.querySelector("[data-slide-stage]");
    const status = viewer.querySelector("[data-slide-status]");
    const count = viewer.querySelector("[data-slide-count]");
    const prev = viewer.querySelector("[data-slide-prev]");
    const next = viewer.querySelector("[data-slide-next]");
    const fullscreen = viewer.querySelector("[data-slide-fullscreen]");
    let index = 0;

    function show(position, announce = true) {
      index = Math.max(0, Math.min(slides.length - 1, position));
      slides.forEach((slide, i) => { slide.hidden = i !== index; });
      count.textContent = `${index + 1} / ${slides.length}`;
      if (announce) status.textContent = `Slide ${index + 1} of ${slides.length}. ${slides[index].querySelector("h3").textContent}`;
      if ((index === 0 && document.activeElement === prev) || (index === slides.length - 1 && document.activeElement === next)) {
        viewer.focus({ preventScroll: true });
      }
      prev.disabled = index === 0;
      next.disabled = index === slides.length - 1;
    }

    show(0, false);
    viewer.querySelector("[data-slide-controls]").hidden = false;
    prev.addEventListener("click", () => show(index - 1));
    next.addEventListener("click", () => show(index + 1));
    viewer.addEventListener("keydown", (event) => {
      if (event.altKey || event.ctrlKey || event.metaKey || event.shiftKey) return;
      // Let keyboard users scroll wide benchmark tables with the arrow keys.
      if (event.target.closest(".case-table-scroll")) return;
      const destinations = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: slides.length - 1 };
      if (Object.hasOwn(destinations, event.key)) {
        event.preventDefault();
        if (stage.contains(document.activeElement)) viewer.focus({ preventScroll: true });
        show(destinations[event.key]);
      }
    });

    let swipe;
    let suppressTap = false;
    stage.addEventListener("pointerdown", (event) => {
      suppressTap = false;
      if (event.isPrimary && event.pointerType === "touch" && event.target.closest(".research-slide-figure")) {
        swipe = { x: event.clientX, y: event.clientY };
      }
    });
    stage.addEventListener("pointerup", (event) => {
      if (!event.isPrimary || !swipe) return;
      const dx = event.clientX - swipe.x;
      const dy = event.clientY - swipe.y;
      swipe = undefined;
      if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) {
        suppressTap = true;
        show(index + (dx < 0 ? 1 : -1));
      }
    });
    stage.addEventListener("pointercancel", () => { swipe = undefined; });
    stage.addEventListener("click", (event) => {
      if (suppressTap && event.detail > 0) event.preventDefault();
      suppressTap = false;
    });

    if (document.fullscreenEnabled && viewer.requestFullscreen) {
      fullscreen.hidden = false;
      fullscreen.addEventListener("click", async () => {
        try {
          if (document.fullscreenElement === viewer) await document.exitFullscreen();
          else await viewer.requestFullscreen();
        } catch {
          fullscreen.hidden = true;
        }
      });
      document.addEventListener("fullscreenchange", () => {
        fullscreen.textContent = document.fullscreenElement === viewer ? "Exit full screen" : "Full screen";
      });
    }
  });
})();
