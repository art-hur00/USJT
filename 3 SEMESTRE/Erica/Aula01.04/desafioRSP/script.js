const form = document.getElementById('myForm');
const progressBar = document.getElementById('Barra');
const successMessage = document.getElementById('successMessage');

form.addEventListener('submit', function(event) {
    event.preventDefault();

    // Iniciar a barra de progresso
    let progress = 0;
    const interval = setInterval(() => {
        if (progress >= 100) {
            clearInterval(interval);
            successMessage.style.display = 'block'; // Exibir a mensagem de sucesso
        } else {
            progress += 10;
            progressBar.style.width = progress + '%'; // Atualizar a largura da barra
        }
    }, 500);
});




