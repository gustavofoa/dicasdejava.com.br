var share_post_params = {"effect":"1","opacity":"0","top_distance":"180","opacity_intensity":"0.7"};

window.onscroll = function scrollFunction() {
	console.log(screen.width);
    var scrollPos = document.body.scrollTop;

    var scroll_distance = 80;

    if (scrollPos > share_post_params.top_distance - scroll_distance) {
        document.getElementById("right-banner").style.position = "fixed";
        document.getElementById("right-banner").style.top = scroll_distance+"px";
    } else {
        document.getElementById("right-banner").style.position = "absolute";
        document.getElementById("right-banner").style.top = "0px";
    }
}
