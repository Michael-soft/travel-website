window.addEventListener('scroll', show);

function show(){
    let shows = document.querySelectorAll('.showw');

    for(let i = 0; i < shows.length; i++){

        let windowheight = window.innerHeight;
        let showtop = shows[i].getBoundingClientRect().top;
        let showpoint = 150;

        if(showtop < windowheight - showpoint){
            shows[i].classList.add('active');
        }else{
            shows[i].classList.remove('active');
        }
    }
}

// var swiper = new Swiper(".mySwiper", {
//     pagination: {
//         el: ".swiper-pagination",
//         clickable: true,
//     },
//     loop: true,
//     breakpoints: {
//         640: {
//             slidesPerView: 1,
//             spaceBetween: 10,
//         },
//         768: {
//             slidesPerView: 2,
//             spaceBetween: 10,
//         },
//         1024: {
//             slidesPerView: 3,
//             spaceBetween: 10,
//         },
//     },
//     centeredSlides: true,
//     autoplay: {
//         delay: 2000,
//         disableOnInteraction: true,
//     },
// });

// Notification dropdown

const noti = document.querySelector(".actions")

noti.addEventListener("click", function(){
    noti.classList.toggle("vieww")
})