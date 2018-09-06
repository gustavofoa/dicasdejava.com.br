var adsense_position = 0;

window.onscroll = function scrollFunction() {

    //last adsense banner
    var last_adsense_banner = document.getElementById("sidebar-banner");

    // console.log(window.pageYOffset, last_adsense_banner.offsetTop, adsense_position)

    if (window.pageYOffset-100 > last_adsense_banner.offsetTop) {
        if(adsense_position == 0)
            adsense_position = last_adsense_banner.offsetTop;
        last_adsense_banner.classList.add("fix-bannner");
    }
    if (window.pageYOffset-100 < adsense_position) {
        adsense_position = 0;
        last_adsense_banner.classList.remove("fix-bannner");
    }

}