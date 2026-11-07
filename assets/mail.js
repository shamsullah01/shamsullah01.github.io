/* Email chooser: mailto: links do nothing on PCs without a mail app, so offer Gmail / Outlook / app / copy. */
(function () {
  var css = '.mc-bg{position:fixed;inset:0;z-index:999;background:rgba(0,0,0,.6);backdrop-filter:blur(4px);display:grid;place-items:center;padding:16px}' +
    '.mc{width:100%;max-width:360px;background:#0b1626;border-radius:12px;padding:22px;box-shadow:0 0 0 1px rgba(42,140,255,.45),0 30px 80px rgba(0,0,0,.6);font-family:Montserrat,system-ui,sans-serif;color:#e8eef7}' +
    '.mc h2{font-family:Oswald,sans-serif;font-weight:500;font-size:14px;letter-spacing:.16em;text-transform:uppercase;color:#8a97a8;margin:0 0 4px}' +
    '.mc .addr{font-size:15px;font-weight:600;margin:0 0 16px;word-break:break-all}' +
    '.mc,.mc *{box-sizing:border-box}.mc a,.mc button{display:block;width:100%;text-align:left;margin:0 0 8px;padding:11px 14px;border-radius:8px;border:0;cursor:pointer;font:600 13px Montserrat,system-ui,sans-serif;letter-spacing:.04em;text-decoration:none;color:#e8eef7;background:rgba(255,255,255,.06);box-shadow:inset 0 0 0 1px rgba(255,255,255,.1)}' +
    '.mc a:hover,.mc button:hover{background:#bfe0ff;color:#06223f}' +
    '.mc .x{background:none;box-shadow:none;text-align:center;color:#8a97a8;margin:6px 0 0}';
  var st = document.createElement('style'); st.textContent = css; document.head.appendChild(st);

  function close() { var b = document.querySelector('.mc-bg'); if (b) b.remove(); }

  document.addEventListener('click', function (e) {
    var a = e.target.closest && e.target.closest('a[href^="mailto:"]');
    if (!a) return;
    e.preventDefault();
    var href = a.getAttribute('href');
    var to = decodeURIComponent(href.slice(7).split('?')[0]);
    var subj = 'Hiring enquiry from your portfolio';
    var enc = encodeURIComponent;
    var bg = document.createElement('div');
    bg.className = 'mc-bg';
    bg.innerHTML =
      '<div class="mc" role="dialog" aria-modal="true" aria-label="Send an email">' +
      '<h2>Email me</h2><p class="addr">' + to + '</p>' +
      '<a target="_blank" rel="noopener" href="https://mail.google.com/mail/?view=cm&fs=1&to=' + enc(to) + '&su=' + enc(subj) + '">Open in Gmail</a>' +
      '<a target="_blank" rel="noopener" href="https://outlook.live.com/mail/0/deeplink/compose?to=' + enc(to) + '&subject=' + enc(subj) + '">Open in Outlook</a>' +
      '<a class="app" href="mailto:' + to + '?subject=' + enc(subj) + '">Open mail app</a>' +
      '<button type="button" class="cp">Copy email address</button>' +
      '<button type="button" class="x">Close</button></div>';
    document.body.appendChild(bg);
    bg.addEventListener('click', function (ev) {
      if (ev.target === bg || ev.target.classList.contains('x')) return close();
      if (ev.target.classList.contains('cp')) {
        var done = function () { ev.target.textContent = 'Copied ✓'; };
        if (navigator.clipboard) navigator.clipboard.writeText(to).then(done, done); else done();
        return;
      }
      if (ev.target.tagName === 'A') {
        ev.stopPropagation();
        if (ev.target.classList.contains('app')) { location.href = ev.target.href; }
        else window.open(ev.target.href, '_blank', 'noopener');
        ev.preventDefault();
        setTimeout(close, 300);
      }
    });
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
})();
