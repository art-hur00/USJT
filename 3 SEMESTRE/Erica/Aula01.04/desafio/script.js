
function exibirMensagemDeSucesso() {
   
    const form = document.getElementById("botãoDeEnviar");
    const rspMen = document.getElementById("rspMen");
  
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        rspMen.style.display = 'block';
        exibirCarregamento();
    });
}

function exibirCarregamento() {
        const progressBar = document.getElementById('carregamento');
        let progresso = 0;
    
    const interval = setInterval(() => {
        if (progresso >= 100) {
            clearInterval(interval);
        } else {
            progresso += 10;
            progressBar.style.width = progresso + '%';
        }
    }, 500);
}