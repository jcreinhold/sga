// Footnote -> margin sidenote relocator (SGA build).
//
// mdBook renders each footnote reference as `<sup class="footnote-reference">`
// with an inner `<a href="#footnote-NAME">N</a>`, and the definitions as an
// `<ol class="footnote-definition">` at the page foot (preceded by an `<hr>`).
// On wide screens footnotes.css shows margin sidenotes and hides that foot list;
// this pass builds the sidenotes by cloning each definition next to its marker.
// DOM-only and idempotent. No-JS readers keep the native foot list untouched.
(function () {
  "use strict";

  // Clone a definition's content into a sidenote, dropping the ↩ back-link.
  function buildSidenote(defEl, num) {
    var note = document.createElement("span");
    note.className = "gi-sidenote";

    var label = document.createElement("span");
    label.className = "gi-sn-num";
    label.textContent = num;
    note.appendChild(label);

    var src = defEl.querySelector("p") || defEl;
    var kids = src.childNodes;
    for (var i = 0; i < kids.length; i++) {
      var k = kids[i];
      if (
        k.nodeType === 1 &&
        k.tagName === "A" &&
        (k.getAttribute("href") || "").indexOf("#fr-") === 0
      ) {
        continue; // skip the back-reference arrow
      }
      note.appendChild(k.cloneNode(true));
    }
    return note;
  }

  function run() {
    var content = document.querySelector(".content");
    if (!content) return;

    var refs = content.querySelectorAll("sup.footnote-reference");
    for (var i = 0; i < refs.length; i++) {
      var sup = refs[i];
      if (sup.getAttribute("data-gi-sidenote")) continue;
      var a = sup.querySelector('a[href^="#footnote-"]');
      if (!a) continue;
      var def = document.getElementById(a.getAttribute("href").slice(1));
      if (!def) continue;

      var note = buildSidenote(def, (a.textContent || "").trim());
      sup.setAttribute("data-gi-sidenote", "1");
      // Insert right after the marker so the float lands beside the citing line.
      sup.parentNode.insertBefore(note, sup.nextSibling);
    }

    // Tag the rule before the foot list so it hides together with the list.
    var list = content.querySelector("ol.footnote-definition");
    if (list) {
      var prev = list.previousElementSibling;
      if (prev && prev.tagName === "HR") prev.classList.add("gi-footnotes-rule");
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
