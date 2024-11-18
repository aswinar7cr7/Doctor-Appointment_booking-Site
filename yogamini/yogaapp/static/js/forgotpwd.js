// forgotpwd.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const username = document.querySelector('input[name="uname"]');
        const password = document.querySelector('input[name="password"]');

        // Simple validation
        if (username.value.trim() === '' || password.value.trim() === '') {
            alert("Please fill in both fields.");
            event.preventDefault();
        }
    });
});
