window.addEventListener('scroll', show);

function show(){
    let shows = document.querySelectorAll('.appear');

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


