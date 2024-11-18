function validateForm() {
    const username = document.querySelector("input[name='username']");
    const password = document.querySelector("input[name='password']");
    if (!username.value || !password.value) {
        alert("Both username and password are required!");
        return false;
    }
    return true;
}
