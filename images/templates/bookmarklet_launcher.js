(function () {
  let site_url = "https://b8258d8903aa.ngrok.io/";
  if (window.bookmarklet !== undefined) {
    bookmarklet.bookmarklet();
  } else {
    document.body.appendChild(document.createElement("script")).src =
      site_url +
      "static/js/bookmarklet.js?r=" +
      Math.floor(Math.random() * 999999999);
  }
})();
