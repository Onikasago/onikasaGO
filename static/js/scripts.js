/*!
* Start Bootstrap - Grayscale v7.0.5 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2022 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            offset: 74,
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });

});

function viewChange(){
    if(document.getElementById('sample')){
        id = document.getElementById('sample').value;
        if(id == 'select1'){
            document.getElementById('Box1').style.display = "";
            document.getElementById('Box2').style.display = "none";
        }else if(id == 'select2'){
            document.getElementById('Box1').style.display = "none";
            document.getElementById('Box2').style.display = "";
        }
    }
    window.onload = viewChange;
}
function viewChange2(){
    if(document.getElementById('sample2')){
        id = document.getElementById('sample2').value;
        if(id == 'select3'){
            document.getElementById('Box3').style.display = "";
            document.getElementById('Box4').style.display = "none";
            document.getElementById('Box5').style.display = "none";
        }
        else if(id == 'select4'){
            document.getElementById('Box3').style.display = "none";
            document.getElementById('Box4').style.display = "";
            document.getElementById('Box5').style.display = "none";
        }
        else if(id == 'select5'){
            document.getElementById('Box3').style.display = "none";
            document.getElementById('Box4').style.display = "none";
            document.getElementById('Box5').style.display = "";
        }
    }
window.onload = viewChange2;
}