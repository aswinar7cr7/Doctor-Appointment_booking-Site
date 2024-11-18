// home.js

function validateForm() {
    let isValid = true;
    const inputs = document.querySelectorAll("input[type='text']");
    inputs.forEach((input) => {
        if (input.value.trim() === "") {
            alert("All fields are required.");
            isValid = false;
            return false;
        }
    });
    return isValid;
}

document.querySelector("form").onsubmit = validateForm;
