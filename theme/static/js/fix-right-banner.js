var adsense_position = 0;

window.onscroll = function scrollFunction() {

    var last_adsense_banner = document.getElementById("sidebar-banner");
    var footer = document.querySelector('footer')

    if (window.pageYOffset-80 > last_adsense_banner.offsetTop) {
        if(adsense_position == 0 
            && last_adsense_banner.offsetTop > 100)
            adsense_position = last_adsense_banner.offsetTop;
        last_adsense_banner.classList.add("fix-banner");
    }
    if (window.pageYOffset-80 < adsense_position || window.pageYOffset+600 > footer.offsetTop) {
        adsense_position = 0;
        last_adsense_banner.classList.remove("fix-banner");
    }
    if(window.pageYOffset+600 > footer.offsetTop)
        last_adsense_banner.classList.add("fix-banner-close-to-footer");
    else
        last_adsense_banner.classList.remove("fix-banner-close-to-footer");

}