/* Lyons Contracting — site interactions
   No dependencies. Safe to load with `defer` on every page. */
(function () {
  "use strict";

  var PHONE_DISPLAY = "703-299-8888";

  /* ---------- Mobile nav ---------- */
  var header = document.querySelector(".site-header");
  var toggle = document.querySelector(".nav-toggle");
  if (toggle && header) {
    toggle.addEventListener("click", function () {
      var open = header.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    header.querySelectorAll(".nav-links a").forEach(function (a) {
      a.addEventListener("click", function () {
        header.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- FAQ accordion ---------- */
  document.querySelectorAll(".faq-q").forEach(function (q) {
    q.addEventListener("click", function () {
      var item = q.closest(".faq-item");
      var isOpen = item.classList.contains("open");
      var group = item.parentElement;
      if (group) {
        group.querySelectorAll(".faq-item.open").forEach(function (i) {
          if (i !== item) {
            i.classList.remove("open");
            var sib = i.querySelector(".faq-q");
            if (sib) sib.setAttribute("aria-expanded", "false");
          }
        });
      }
      item.classList.toggle("open", !isOpen);
      q.setAttribute("aria-expanded", !isOpen ? "true" : "false");
    });
  });

  /* ---------- Scroll reveal ---------- */
  var reveals = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  if (!reduce && "IntersectionObserver" in window && reveals.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add("in"); });
  }

  /* ---------- Instant estimate calculator ----------
     Ranges are deliberately wide and clearly labelled as ballpark figures.
     NOTE TO OWNER: replace the per-square-foot numbers below with Lyons' own
     current pricing before launch — these are placeholders for the demo. */
  var PRICE = {                 // $ per sq ft of roof area, installed
    shingle:  { lo: 5.5,  hi: 9.0  },
    metal:    { lo: 13.0, hi: 22.0 },
    flat:     { lo: 8.0,  hi: 14.0 },
    slate:    { lo: 25.0, hi: 45.0 },
    tile:     { lo: 16.0, hi: 28.0 }
  };
  var STORY_MULT   = { "1": 1.0, "2": 1.08, "3": 1.18 };
  var COMPLEX_MULT = { simple: 0.94, average: 1.0, complex: 1.14 };
  var TEAR_OFF     = { none: 0, one: 0.9, two: 1.7 };   // $ per sq ft added

  var calc = document.getElementById("calc");
  if (calc) {
    var out   = document.getElementById("calc-range");
    var outMo = document.getElementById("calc-mo");

    // Round to the nearest $100 so the range reads as an estimate, not a quote.
    var money = function (n) {
      return "$" + (Math.round(n / 100) * 100).toLocaleString("en-US");
    };

    var update = function () {
      var area    = parseFloat(calc.querySelector("#calc-area").value) || 0;
      var mat     = calc.querySelector("#calc-material").value;
      var stories = calc.querySelector("#calc-stories").value;
      var cplx    = calc.querySelector("#calc-complexity").value;
      var tear    = calc.querySelector("#calc-tearoff").value;

      if (!area || !PRICE[mat]) {
        out.textContent = "—";
        outMo.textContent = "";
        return;
      }
      // Roof area runs larger than footprint because of pitch; ~1.25 is a fair average.
      var roofArea = area * 1.25;
      var m = (STORY_MULT[stories] || 1) * (COMPLEX_MULT[cplx] || 1);
      var extra = TEAR_OFF[tear] || 0;

      var lo = roofArea * (PRICE[mat].lo + extra) * m;
      var hi = roofArea * (PRICE[mat].hi + extra) * m;

      out.textContent = money(lo) + " – " + money(hi);
      // Illustrative financing figure: 120 months at ~9.99% APR on the midpoint.
      var mid = (lo + hi) / 2, r = 0.0999 / 12, n = 120;
      var pmt = mid * r / (1 - Math.pow(1 + r, -n));
      outMo.textContent = "Roughly $" + Math.round(pmt / 5) * 5 + "/mo with financing";
    };

    calc.querySelectorAll("input, select").forEach(function (el) {
      el.addEventListener("input", update);
      el.addEventListener("change", update);
    });
    update();
  }

  /* ---------- Lead forms ----------
     NOTE TO OWNER: see README section 2a. Put a real endpoint in the form's
     `action` (Web3Forms / Formspree / Netlify) and this submits by AJAX with an
     inline thank-you. Until then it falls back to the visitor's mail client so
     no lead is ever silently lost.

     Deliberately NOT here: a CAPTCHA. The hidden honeypot field below stops the
     bots without making a homeowner prove they are human. */
  document.querySelectorAll("form[data-lead-form]").forEach(function (form) {
    form.addEventListener("submit", function (e) {
      // Honeypot — only a bot fills this in.
      var hp = form.querySelector('input[name="company_website"]');
      if (hp && hp.value) { e.preventDefault(); return; }

      var endpoint = form.getAttribute("action");
      var success = form.querySelector(".form-success");
      var fields = form.querySelector(".form-fields");
      var btn = form.querySelector("button[type=submit]");
      var label = btn ? btn.textContent : "";

      var showSuccess = function () {
        form.reset();
        if (success) success.style.display = "block";
        if (fields) fields.style.display = "none";
        if (success && success.scrollIntoView) success.scrollIntoView({ block: "center" });
      };

      if (endpoint && endpoint.indexOf("FORM_ENDPOINT") === -1 && endpoint.charAt(0) !== "#") {
        e.preventDefault();
        if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
        fetch(endpoint, { method: "POST", body: new FormData(form), headers: { Accept: "application/json" } })
          .then(function (r) {
            if (r.ok) { showSuccess(); }
            else { alert("Sorry — something went wrong. Please call us at " + PHONE_DISPLAY + "."); }
          })
          .catch(function () { alert("Sorry — something went wrong. Please call us at " + PHONE_DISPLAY + "."); })
          .finally(function () { if (btn) { btn.disabled = false; btn.textContent = label; } });
        return;
      }

      // Fallback: hand the lead to the visitor's mail client.
      e.preventDefault();
      var data = new FormData(form);
      var lines = [];
      data.forEach(function (v, k) { if (v && k !== "company_website") lines.push(k + ": " + v); });
      var subject = encodeURIComponent("Free Estimate Request — " + (data.get("name") || "New Lead"));
      var body = encodeURIComponent(lines.join("\n"));
      // NOTE TO OWNER: replace with the address that should receive leads.
      window.location.href = "mailto:INFO@LYONSCONTRACTING.COM?subject=" + subject + "&body=" + body;
      showSuccess();
    });
  });

  /* ---------- Footer year ---------- */
  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
