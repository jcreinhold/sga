// AMS theorem-environment tagger (SGA build).
//
// Math is rendered to static HTML at build time (mdbook-katex), so the DOM is
// final at DOMContentLoaded — no async-render race to wait out. This pass scans
// reading-surface paragraphs for a leading <strong> label like "Proposition."
// or "Theorem 2.2 (…)." and tags the paragraph so theorems.css can apply the
// right AMS style. It changes no markdown, only adds classes, and is idempotent.
//
// SGA authors most statements in a SPLIT form: a label-only paragraph
// (`**Proposition.**`), then an HTML `<!-- label: I.2.1 -->` comment, then the
// statement as a separate paragraph. So when the label paragraph carries no body
// of its own, the tagger also styles the FOLLOWING statement paragraph (skipping
// the comment/whitespace nodes between). The gentle-iut inline form — label and
// body in one paragraph — is still handled directly.
(function () {
  "use strict";

  // Label keyword -> AMS style bucket (see theorems.css).
  var KIND = {
    Theorem: "plain",
    Lemma: "plain",
    Proposition: "plain",
    Corollary: "plain",
    Scholium: "plain",
    Conjecture: "plain",
    Definition: "defn",
    Example: "defn",
    Construction: "defn",
    Notation: "defn",
    Convention: "defn",
    Remark: "remark",
    Caution: "remark",
    Proof: "proof",
  };

  // Anchored at paragraph start; \b keeps "Theorem" from matching "Theorems"
  // but still matches "Proposition 0.5." (keyword followed by space/number).
  var LABEL_RE = new RegExp("^(" + Object.keys(KIND).join("|") + ")\\b");

  // The label is the first element child of the paragraph; skip any leading
  // whitespace-only text node before it.
  function leadingStrong(p) {
    var n = p.firstChild;
    while (n && n.nodeType === 3 && !n.textContent.trim()) {
      n = n.nextSibling;
    }
    return n && n.nodeType === 1 && n.tagName === "STRONG" ? n : null;
  }

  // True when the paragraph is JUST the label (SGA's split form): its trimmed
  // text equals the label's. Then the statement lives in a later paragraph.
  function isLabelOnly(p, strong) {
    return p.textContent.trim() === strong.textContent.trim();
  }

  // The statement paragraph in the split form: the next sibling ELEMENT, past
  // the `<!-- label: … -->` comment and whitespace text nodes.
  function nextStatement(p) {
    var n = p.nextSibling;
    while (n) {
      if (n.nodeType === 1) return n; // element
      n = n.nextSibling; // skip comments (8) and whitespace text (3)
    }
    return null;
  }

  function isLabeled(p) {
    var s = leadingStrong(p);
    return !!(s && LABEL_RE.test(s.textContent.trim()));
  }

  function tag(p) {
    if (!p || p.hasAttribute("data-gi-thm")) return;
    var strong = leadingStrong(p);
    if (!strong) return;
    var m = LABEL_RE.exec(strong.textContent.trim());
    if (!m) return;
    var kind = KIND[m[1]];

    p.setAttribute("data-gi-thm", kind);
    strong.classList.add("gi-thm-label");

    if (isLabelOnly(p, strong)) {
      // Label-only paragraph: give it the block margin + label hook, then carry
      // the AMS body style to the following statement paragraph.
      p.classList.add("gi-thm");
      var stmt = nextStatement(p);
      if (
        stmt &&
        stmt.tagName === "P" &&
        !stmt.hasAttribute("data-gi-thm") &&
        !isLabeled(stmt) // don't swallow a back-to-back labelled statement
      ) {
        stmt.setAttribute("data-gi-thm", kind);
        stmt.classList.add("gi-thm", "gi-thm--" + kind);
      }
    } else {
      // Inline form: label and body share one paragraph.
      p.classList.add("gi-thm", "gi-thm--" + kind);
    }
  }

  function run() {
    var content = document.querySelector(".content");
    if (!content) return;
    // All content paragraphs: top-level statements and the label paragraph
    // inside caution blockquotes are both <p>; the keyword anchor guards
    // against bolded defined-terms mid-sentence (those never lead a paragraph
    // with a matching keyword).
    var ps = content.querySelectorAll("main p");
    for (var i = 0; i < ps.length; i++) tag(ps[i]);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", run);
  } else {
    run();
  }
})();
