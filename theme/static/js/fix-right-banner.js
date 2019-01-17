var adsense_position = 0;

window.onscroll = function scrollFunction() {

    var last_adsense_banner = document.getElementById("sidebar-banner");
    var footer = document.querySelector('footer')

    if (window.pageYOffset-100 > last_adsense_banner.offsetTop) {
        if(adsense_position == 0)
            adsense_position = last_adsense_banner.offsetTop;
        last_adsense_banner.classList.add("fix-bannner");
    }
    if (window.pageYOffset-100 < adsense_position || window.pageYOffset+600 > footer.offsetTop) {
        adsense_position = 0;
        last_adsense_banner.classList.remove("fix-bannner");
    }

}