var adsense_position = 0;

window.onscroll = function scrollFunction() {

    var last_adsense_banner = document.getElementById("sidebar-banner");
    var footer = document.querySelector('footer')

    if (window.pageYOffset-680 > last_adsense_banner.offsetTop) {
        if(adsense_position == 0 
            && last_adsense_banner.offsetTop > 100)
            adsense_position = last_adsense_banner.offsetTop;
        last_adsense_banner.classList.add("fix-banner");
    }
    if (window.pageYOffset-680 < adsense_position) {
        adsense_position = 0;
        last_adsense_banner.classList.remove("fix-banner");
    }
    if(window.pageYOffset+600 > footer.offsetTop)
        last_adsense_banner.classList.add("fix-banner-close-to-footer");
    else
        last_adsense_banner.classList.remove("fix-banner-close-to-footer");

    if(window.pageYOffset+600 > footer.offsetTop)
        last_adsense_banner.classList.remove("fix-banner");

}