window.addEventListener('DOMContentLoaded', () => {

    // Grab page header
    let pageHeader = [...document.getElementsByTagName('h2')][0].innerText;

    switch(pageHeader) {
        case "Welcome":
            let images = document.querySelectorAll('img');
            new simpleParallax(images, {
                delay: .6,
	            transition: 'cubic-bezier(0,0,0,1)'
            });
            break;
        case "Log in":
        case "Register":
            let scene = document.getElementById('scene');
            let parallaxInstance = new Parallax(scene);
            break;
      }
});

