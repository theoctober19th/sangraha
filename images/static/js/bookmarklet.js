(function () {
  let jquery_version = "3.5.1";
  let site_url = "https://9b99c9156ba4.ngrok.io/";
  let static_url = site_url + "static/";
  let min_height = 100;
  let min_width = 100;

  function bookmarklet() {
    //load css
    var link = jQuery("<link>");
    link.attr({
      rel: "stylesheet",
      type: "text/css",
      href:
        static_url +
        "css/bookmarklet.css?r=" +
        Math.floor(Math.random() * 99999999),
    });
    jQuery("head").append(link);

    //load html
    box_html = `
        <div id="bookmarklet">
            <a href="#" id="close">&times;</a>
            <h1>Select an image to bookmark.</h1>
            <div class="images"></div>
        </div>
    `;
    jQuery("body").append(box_html);

    jQuery("#bookmarklet #close").click(function () {
      jQuery("#bookmarklet").remove();
    });

    jQuery.each(jQuery('img[src$="jpg"]'), function (index, image) {
      if (
        jQuery(image).width() >= min_width &&
        jQuery(image).height() >= min_height
      ) {
        var image_url = jQuery(image).attr("src");
        console.log(image_url);
        new_entry = `
                <a href="#">
                    <img src="${image_url}" />
                </a>`;
        jQuery("#bookmarklet .images").append(new_entry);
      }
    });

    jQuery("#bookmarklet .images a").click(function (e) {
      selected_image = jQuery(this).children("img").attr("src");
      jQuery("#bookmarklet").hide();

      var url =
        site_url +
        "images/create/?url=" +
        encodeURIComponent(selected_image) +
        "&title=" +
        encodeURIComponent(jQuery("title").text());
      window.open(url, "_blank");
    });
  }

  if (window.jQuery) {
    bookmarklet();
  } else {
    var script = document.createElement("script");
    script.src =
      "//ajax.googleapis.com/ajax/libs/jquery/" +
      jquery_version +
      "/jquery.min.js";
    document.head.appendChild(script);
    script.onload = bookmarklet;
    script.onerror = function () {
      alert("Could not load jquery");
    };
  }
})();
