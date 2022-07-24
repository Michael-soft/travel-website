let emailInput=document.querySelector("#inputEmail");
let emailIcon=document.querySelector(".email-icon");
let emailError=document.querySelector(".email-error");
let emailBox=document.querySelector(".emailBox");
let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


    emailInput.addEventListener("click",function( ){
    emailIcon.classList.remove("invisible")
    document.querySelector(".form-check2").classList.add("text-danger")
    document.querySelector(".sign-in").classList.remove("bg-dark")
    document.querySelector(".sign-in").classList.add("orange2")
   
  })

  let emailText=document.querySelector(".emailText");
    
  emailInput.addEventListener("input",function(){
       
      

      if (emailPattern.test(emailInput.value)){
      //   emailBox.classList.add("valid");
      //  emailBox.classList.remove("invalid");
      emailText.classList.add("invisible")
      emailError.classList.add("invisible")
      emailIcon.classList.remove("invisible")
          document.querySelector(".validEmail").classList.remove("invisible")

    }
      else{
      // emailBox.classList.add("invalid");
      // emailBox.classList.remove("valid");
      emailText.classList.remove("invisible")
      emailError.classList.remove("invisible")
      emailIcon.classList.add("invisible")
      emailText.innerHTML="Invalid Email address";
      emailInput.classList.add("border-danger")
      document.querySelector(".validEmail").classList.add("invisible")

      //  emailText.innerHTML="Invalid email address";

      }

    })
    

    
     

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



