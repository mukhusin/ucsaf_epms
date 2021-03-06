const usernameField = document.querySelector('#usernameField');
const passwordField = document.querySelector('#passwordField');
// const emailField = document.querySelector('#emailField')
const feedBackArea = document.querySelector('.invalid_feedback');
const emailFeedBackArea = document.querySelector('.email_feedback');
const passwordFeedBackArea = document.querySelector('.password_feedback');
const usernameSuccess = document.querySelector(".usernameSuccess");
const showPasswordToggle = document.querySelector(".showPasswordToggle");
const submitBtn = document.querySelector(".submit-btn");

const handleToggleInput = (e)=>{
  
    if (showPasswordToggle.textContent == "show") {
        showPasswordToggle.textContent = "hide";
        passwordField.setAttribute("type","text")
    }else{
        showPasswordToggle.textContent = "show";
        passwordField.setAttribute("type","password")
    }

}

showPasswordToggle.addEventListener('click', handleToggleInput)


emailField.addEventListener("keyup",(e)=> {
    console.log('333',33333)
    const emailVal = e.target.value;

    emailField.classList.remove("is-invalid");
    emailFeedBackArea.style.display = "none";

    if (emailVal.length > 0) {
        fetch('/authentication/validate-email',{
            body: JSON.stringify({email: emailVal}),
            method: "POST",
        }).then(res=>res.json()).then((data) => {
            console.log('data', data);
            if (data.email_error) {
                submitBtn.disabled = true
                emailField.classList.add("is-invalid");
                emailFeedBackArea.style.display = "block";
                emailFeedBackArea.innerHTML=`<h6>${data.email_error}</h6>`;
            }else{
                submitBtn.removeAttribute("disabled");
            }
        });
    }

});


usernameField.addEventListener("keyup",(e)=> {
    const usernameVal = e.target.value;
    usernameSuccess.style.display = 'block';

    usernameSuccess.textContent=`Checking ${usernameVal}`;

    usernameField.classList.remove("is-invalid");
    feedBackArea.style.display = "none";

    if (usernameVal.length > 0) {
        fetch('/authentication/validate-username',{
            body: JSON.stringify({username: usernameVal}),
            method: "POST",
        }).then(res=>res.json()).then((data) => {
            console.log('data', data);
            usernameSuccess.style.display = 'none';
            if (data.username_error) {
                usernameField.classList.add("is-invalid");
                feedBackArea.style.display = "block";
                feedBackArea.innerHTML=`<h6>${data.username_error}</h6>`;
                submitBtn.disabled = true;
            }else{
                submitBtn.removeAttribute("disabled");
            }
        });
    }

});