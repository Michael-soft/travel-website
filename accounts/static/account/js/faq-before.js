const questions = document.querySelectorAll(".question-answer");

questions.forEach(function(question){
    const btn = question.querySelector(".control");
    btn.addEventListener("click", function(){
        questions.forEach(function(item){
            if(item !== question){
                item.classList.remove("show-text")
            }
        })
        question.classList.toggle("show-text")
    })

})

window.addEventListener('scroll', show);

function show(){
    let shows = document.querySelectorAll('.showw');

    for(let i = 0; i < shows.length; i++){

        let windowheight = window.innerHeight;
        let showtop = shows[i].getBoundingClientRect().top;
        let showpoint = 150;

        if(showtop < windowheight - showpoint){
            shows[i].classList.add('operational');
        }else{
            shows[i].classList.remove('operational');
        }
    }
}

