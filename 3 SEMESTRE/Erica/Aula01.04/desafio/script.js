
function exibirMensagemDeSucesso() {
    const form = document.getElementById("botãoDeEnviar");
    const rspMen = document.getElementById("rspMen");
    form.addEventListener('submit', function(event) {
        event.preventDefault();
        rspMen.style.display = 'block';
    });
}


