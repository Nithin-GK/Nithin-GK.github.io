(() => {
  "use strict";
  document.querySelectorAll("[data-slide-viewer]").forEach((viewer) => {
    const slides = JSON.parse(viewer.querySelector("[data-slide-data]").textContent);
    if (!slides.length) return;
    const image = viewer.querySelector("[data-slide-image]");
    const status = viewer.querySelector("[data-slide-status]");
    const prev = viewer.querySelector("[data-slide-prev]");
    const next = viewer.querySelector("[data-slide-next]");
    const fullscreen = viewer.querySelector("[data-slide-fullscreen]");
    let index = 0;
    const show = (position) => {
      index = Math.max(0, Math.min(slides.length - 1, position));
      image.src = slides[index].src;
      image.alt = slides[index].alt;
      status.textContent = `${index + 1} / ${slides.length} · ${slides[index].title}`;
      prev.disabled = index === 0;
      next.disabled = index === slides.length - 1;
      if (slides[index + 1]) {
        const preload = new Image();
        preload.src = slides[index + 1].src;
      }
    };
    viewer.querySelector("[data-slide-controls]").hidden = false;
    prev.addEventListener("click", () => show(index - 1));
    next.addEventListener("click", () => show(index + 1));
    viewer.addEventListener("keydown", (event) => {
      const destinations = { ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: slides.length - 1 };
      if (Object.prototype.hasOwnProperty.call(destinations, event.key)) {
        event.preventDefault();
        show(destinations[event.key]);
      }
    });
    let pointerStart;
    image.addEventListener("pointerdown", (event) => {
      pointerStart = { x: event.clientX, y: event.clientY };
    });
    image.addEventListener("pointerup", (event) => {
      if (!pointerStart) return;
      const dx = event.clientX - pointerStart.x,
        dy = event.clientY - pointerStart.y;
      if (Math.abs(dx) > 60 && Math.abs(dx) > Math.abs(dy) * 1.5) show(index + (dx < 0 ? 1 : -1));
      pointerStart = undefined;
    });
    image.addEventListener("pointercancel", () => {
      pointerStart = undefined;
    });
    image.addEventListener("dragstart", (event) => event.preventDefault());
    if (viewer.requestFullscreen) {
      fullscreen.hidden = false;
      fullscreen.addEventListener("click", async () => {
        try {
          if (document.fullscreenElement === viewer) await document.exitFullscreen();
          else await viewer.requestFullscreen();
        } catch (_) {
          fullscreen.hidden = true;
        }
      });
      document.addEventListener("fullscreenchange", () => {
        fullscreen.textContent = document.fullscreenElement === viewer ? "Exit full screen" : "Full screen";
      });
    }
    show(0);
  });
})();
