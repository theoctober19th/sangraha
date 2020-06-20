(function () {
  let site_url = "https://9b99c9156ba4.ngrok.io/";
  if (window.bookmarklet !== undefined) {
    bookmarklet.bookmarklet();
  } else {
    document.body.appendChild(document.createElement("script")).src =
      site_url +
      "static/js/bookmarklet.js?r=" +
      Math.floor(Math.random() * 999999999);
  }
})();
