// Add loading state when form is submitted
document.getElementById('interfaceForm').addEventListener('submit', function() {
    const form = this;
    const button = form.querySelector('button');
    const buttonText = document.getElementById('buttonText');

    form.classList.add('loading');
    buttonText.textContent = 'Processing...';

    // Prevent double submission
    button.disabled = true;
});

// Add smooth focus transitions
const inputs = document.querySelectorAll('input[type="text"]');
inputs.forEach(input => {
    input.addEventListener('focus', function() {
        this.parentElement.style.transform = 'scale(1.02)';
        this.parentElement.style.transition = 'transform 0.2s ease';
    });

    input.addEventListener('blur', function() {
        this.parentElement.style.transform = 'scale(1)';
    });
});