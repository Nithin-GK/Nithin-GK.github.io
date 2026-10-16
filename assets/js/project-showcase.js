(() => {
  "use strict";
  document.querySelectorAll("[data-image-comparison]").forEach((comparison) => {
    const range = comparison.querySelector('input[type="range"]');
    range?.addEventListener("input", () => {
      comparison.style.setProperty("--compare-position", range.value + "%");
      range.setAttribute("aria-valuetext", range.value + "% original, " + (100 - Number(range.value)) + "% edited");
    });
  });
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
  document.querySelectorAll("[data-expand-figure]").forEach((button) => {
    button.addEventListener("click", () => {
      const figure = button.closest(".case-demo-panel") || button.closest("[data-case-figure]");
      const image = figure?.querySelector("[data-case-image]");
      if (!dialog || !dialogImage || !image) return;
      dialogImage.src = image.dataset.fullSrc || image.currentSrc || image.src;
      dialogImage.alt = image.alt;
      dialogCaption.textContent = figure.querySelector("figcaption")?.textContent || image.alt;
      lastExpandButton = button;
      dialog.showModal();
    });
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
