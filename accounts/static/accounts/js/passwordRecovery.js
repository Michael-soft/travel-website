let emailInput=document.querySelector("#inputEmail");
let emailIcon=document.querySelector(".email-icon2");
let emailError=document.querySelector(".email-error2");
let emailBox=document.querySelector(".emailBox");
let emailPattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;


    emailInput.addEventListener("click",function( ){
    emailIcon.classList.remove("invisible")
    // document.querySelector(".form-check2").classList.add("text-danger")
    document.querySelector(".pass").classList.remove("bg-dark")
    document.querySelector(".pass").classList.add("orange2")
   
  })

  let emailText=document.querySelector(".emailText");
    
  emailInput.addEventListener("input",function(){
       
      

      if (emailPattern.test(emailInput.value)){
      //   emailBox.classList.add("valid");
      //  emailBox.classList.remove("invalid");
      emailText.classList.add("invisible")
      emailError.classList.add("invisible")
      emailIcon.classList.remove("invisible")
          document.querySelector(".validEmail2").classList.remove("invisible")

    }
      else{
      // emailBox.classList.add("invalid");
      // emailBox.classList.remove("valid");
      emailText.classList.remove("invisible")
      emailError.classList.remove("invisible")
      emailIcon.classList.add("invisible")
      emailText.innerHTML="Invalid Email address";
      emailInput.classList.add("border-danger")
      document.querySelector(".validEmail2").classList.add("invisible")

      //  emailText.innerHTML="Invalid email address";

      }

    })
    

    
     

