// register.js

function validateRegisterForm() {
    let isValid = true;
    const inputs = document.querySelectorAll("input[type='text'], input[type='password']");
    inputs.forEach((input) => {
        if (input.value.trim() === "") {
            alert("All fields are required.");
            isValid = false;
            return false;
        }
    });
    return isValid;
}

document.querySelector("form").onsubmit = validateRegisterForm;
