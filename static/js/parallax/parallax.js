window.addEventListener('DOMContentLoaded', () => {

    // Grab page header
    let pageHeader = [...document.getElementsByTagName('h2')][0].innerText;

    switch(pageHeader) {
        case "Welcome":
            setupParallaxForHomePage();
            break;
        case "Log in":
        case "Register":
            let scene = document.getElementById('scene');
            let parallaxInstance = new Parallax(scene);
            break;
      }
});

function setupParallaxForHomePage () {
    let images = [...document.getElementsByClassName('parallax-image')];

    for (let [index, image] of images.entries()) {
        if (index % 2 !== 0){
            applyParallaxToImage(image, 1.6, 'cubic-bezier(0,0,0,1)', 'right', 1.05);
        } else {
            applyParallaxToImage(image, 1.6, 'cubic-bezier(0,0,0,1)', 'left', 1.05);
        }
    }
}

function applyParallaxToImage(image, delay, transition, orientation, scale) {
    new simpleParallax(image, {
        delay: delay,
        transition: transition,
        orientation: orientation,
        scale, scale
    });
}

