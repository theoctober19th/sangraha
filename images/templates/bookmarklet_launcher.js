(function () {
  let site_url = "https://cf57332129fb.ngrok.io/";
  if (window.bookmarklet !== undefined) {
    bookmarklet.bookmarklet();
  } else {
    document.body.appendChild(document.createElement("script")).src =
      site_url +
      "static/js/bookmarklet.js?r=" +
      Math.floor(Math.random() * 999999999);
  }
})();
