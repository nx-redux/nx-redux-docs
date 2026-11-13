// The theme fetches GitHub facts for one repository only. This fills in the
// mobile repository's stars and forks the same way, cached for the session.
(function () {
  var links = document.querySelectorAll(".nx-source-mobile");
  if (!links.length) return;
  var KEY = "nx-source-mobile";
  function round(n) { return n > 999 ? (n / 1000).toFixed(n > 99999 ? 0 : 1) + "k" : String(n); }
  function show(facts) {
    links.forEach(function (link) {
      var list = link.querySelector(".md-source__facts");
      if (!list || list.querySelector(".md-source__fact--stars")) return;
      [["stars", facts.stars], ["forks", facts.forks]].forEach(function (f) {
        var li = document.createElement("li");
        li.className = "md-source__fact md-source__fact--" + f[0];
        li.textContent = round(f[1]);
        list.appendChild(li);
      });
    });
  }
  var cached = null;
  try { cached = JSON.parse(sessionStorage.getItem(KEY)); } catch (e) {}
  if (cached) { show(cached); return; }
  var repo = links[0].href.replace(/^https:\/\/github\.com\//, "").replace(/\/$/, "");
  fetch("https://api.github.com/repos/" + repo)
    .then(function (r) { return r.ok ? r.json() : Promise.reject(); })
    .then(function (d) {
      var facts = { stars: d.stargazers_count, forks: d.forks_count };
      try { sessionStorage.setItem(KEY, JSON.stringify(facts)); } catch (e) {}
      show(facts);
    })
    .catch(function () {});
})();
