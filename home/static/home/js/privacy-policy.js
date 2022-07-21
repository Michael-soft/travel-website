const noti = document.querySelector(".actions")

noti.addEventListener("click", function(){
    noti.classList.toggle("vieww")
})

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



