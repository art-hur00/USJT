function updateProgressBar(percentage) {
    const progressBar = document.getElementById('Barra');
    progressBar.style.width = percentage + '%';
}

let progress = 0;
const interval = setInterval(() => {
    if (progress >= 100) {
        clearInterval(interval);
    } else {
        progress += 10;
        updateProgressBar(progress);
    }
}, 1000);
        
const form = document.getElementById('myForm');
const successMessage = document.getElementById('successMessage');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    successMessage.style.display = 'block';
});
