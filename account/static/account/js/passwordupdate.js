// password
let passwordInput=document.querySelector("#inputPassword");
let passwordIcon=document.querySelector( ".password-icon");
let passwordError=document.querySelector( ".password-error");
let passwordPattern=/^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,15}$/;

 passwordInput.addEventListener("click",function(){
     passwordIcon.classList.remove("invisible")
     document.querySelector(".show").classList.remove("invisible")
     document.querySelector(".sign-in").classList.remove("bg-dark")
     document.querySelector(".sign-in").classList.add("orange2")

 })

 passwordInput.addEventListener("input",function(){



 if(passwordPattern.test(passwordInput.value)){
 
  document.querySelector(".passtext").classList.add("invisible")
  passwordError.classList.add("invisible")
}


else{
 passwordError.classList.remove("invisible")
 passwordIcon.classList.add("invisible")
 document.querySelector(".passtext").classList.remove("invisible")

}
 })
  
function showPassword(){
     passwordInput.setAttribute("type","text")
     document.querySelector(".show").classList.add("invisible")
     document.querySelector(".hide").classList.remove("invisible")
    
  }
 function hidePassword(){
     passwordInput.setAttribute("type","password")
     document.querySelector(".show").classList.remove("invisible")
     document.querySelector(".hide").classList.add("invisible")

 }

