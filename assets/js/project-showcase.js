(() => {
  "use strict";
  const filters = [...document.querySelectorAll("[data-project-filter]")];
  const cards = [...document.querySelectorAll("#papers [data-project-card]")];
  const status = document.querySelector("[data-filter-status]");
  filters.forEach((button) =>
    button.addEventListener("click", () => {
      const theme = button.dataset.projectFilter;
      let count = 0;
      filters.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
      cards.forEach((card) => {
        card.hidden = theme !== "all" && card.dataset.theme !== theme;
        if (!card.hidden) count++;
      });
      if (status) status.textContent = count + " research project" + (count === 1 ? "" : "s");
    })
  );
  const dialog = document.querySelector("[data-figure-dialog]");
  const dialogImage = document.querySelector("[data-dialog-image]");
  const dialogCaption = document.querySelector("[data-dialog-caption]");
  let lastExpandButton;
  document.querySelector("[data-close-figure]")?.addEventListener("click", () => dialog.close());
  dialog?.addEventListener("close", () => lastExpandButton?.focus());
  dialog?.addEventListener("click", (event) => {
    if (event.target === dialog) {
      const rect = dialog.getBoundingClientRect();
      if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
    }
  });
  document.querySelectorAll("[data-case-gallery]").forEach((gallery) => {
    let figures;
    try {
      figures = JSON.parse(gallery.querySelector("[data-case-media]").textContent);
    } catch {
      return;
    }
    const image = gallery.querySelector("[data-case-image]");
    const caption = gallery.querySelector("[data-case-caption]");
    const buttons = [...gallery.querySelectorAll("[data-figure-index]")];
    let request = 0;
    buttons.forEach((button) =>
      button.addEventListener("click", () => {
        const figure = figures[Number(button.dataset.figureIndex)];
        if (!figure) return;
        const token = ++request;
        const preload = new Image();
        image.classList.add("is-loading");
        buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
        preload.onload = () => {
          if (token !== request) return;
          image.src = figure.preview || figure.src;
          image.dataset.fullSrc = figure.src;
          image.alt = figure.alt;
          caption.textContent = figure.caption;
          image.classList.remove("is-loading");
        };
        preload.onerror = () => {
          if (token !== request) return;
          image.classList.remove("is-loading");
          caption.textContent = "This figure could not load. Please try the figure again.";
        };
        preload.src = figure.preview || figure.src;
      })
    );
    gallery.querySelector("[data-expand-figure]")?.addEventListener("click", (event) => {
      if (!dialog || !dialogImage) return;
      dialogImage.src = image.dataset.fullSrc || image.currentSrc || image.src;
      dialogImage.alt = image.alt;
      dialogCaption.textContent = caption.textContent;
      lastExpandButton = event.currentTarget;
      dialog.showModal();
    });
  });
  document.querySelectorAll("[data-comparison]").forEach((comparison) => {
    const range = comparison.querySelector("[data-comparison-range]");
    const update = () => {
      const value = Math.min(100, Math.max(0, Number(range.value)));
      comparison.style.setProperty("--reveal", value + "%");
      range.setAttribute("aria-valuetext", 100 - value + "% edited image");
    };
    range.addEventListener("input", update);
    update();
  });
  const crowd = document.querySelector("[data-crowd-explorer]");
  if (crowd) {
    const data = { 1: ["74.59", "210 ms"], 2: ["71.94", "430 ms"], 4: ["68.95", "770 ms"], 8: ["66.97", "1,360 ms"] };
    const buttons = [...crowd.querySelectorAll("[data-hypotheses]")];
    buttons.forEach((button) =>
      button.addEventListener("click", () => {
        const values = data[button.dataset.hypotheses];
        if (!values) return;
        buttons.forEach((item) => item.setAttribute("aria-pressed", String(item === button)));
        crowd.querySelector("[data-crowd-mae]").textContent = values[0];
        crowd.querySelector("[data-crowd-time]").textContent = values[1];
      })
    );
  }
})();
