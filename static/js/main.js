// Toggle for Password Field
const togglePassword = document.querySelector('#togglePassword');
const password = document.querySelector('#password');
const toggleIconPassword = document.querySelector('#toggleIconPassword');

togglePassword.addEventListener('click', function () {
    // Toggle the type attribute
    const type = password.getAttribute('type') === 'password' ? 'text' : 'password';
    password.setAttribute('type', type);

    // Toggle the icon
    toggleIconPassword.classList.toggle('fa-eye');
    toggleIconPassword.classList.toggle('fa-eye-slash');
});

// Toggle for Confirm Password Field
const toggleConfirmPassword = document.querySelector('#toggleConfirmPassword');
const confirmPassword = document.querySelector('#confirmPassword');
const toggleIconConfirmPassword = document.querySelector('#toggleIconConfirmPassword');

toggleConfirmPassword.addEventListener('click', function () {
    // Toggle the type attribute
    const type = confirmPassword.getAttribute('type') === 'password' ? 'text' : 'password';
    confirmPassword.setAttribute('type', type);

    // Toggle the icon
    toggleIconConfirmPassword.classList.toggle('fa-eye');
    toggleIconConfirmPassword.classList.toggle('fa-eye-slash');
});