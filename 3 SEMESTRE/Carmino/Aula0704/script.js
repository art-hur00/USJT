var telaExcluir = document.getElementById("tela-excluir"); // Recebe ID da div tela-excluir
var telaEditar = document.getElementById("tela-editar"); // Recebe ID da div tela-editar
var telaLancamento = document.getElementById("tela-lancamento"); // Recebe ID da div tela-lancamento

// Função para abrir Tela de Lançamento
function abrirTelaLancamento() {
    telaLancamento.style.display = "block";
}
// Abre a Tela de Lançamento ao clicar no botão -> Novo Lançamento, abaixo da Tabela
document.querySelectorAll(".novo-lancamento").forEach(button => {
    button.addEventListener('click', function() {
        abrirTelaLancamento();
    });
});
// Função para fechar Tela de Lançamento
function fecharTelaLancamento() {
    telaLancamento.style.display = "none";
}
// Fechar a Tela de Lançamento ao clicar no botão -> Cancelar
document.getElementById('cancelar-lancamento').addEventListener('click', fecharTelaLancamento);



// Função para abrir Tela de Editar
function abrirTelaEditar() {
    telaEditar.style.display = "block";
}
// Abre a Tela de Editar ao clicar no botão -> Editar, na Tabela
document.querySelectorAll('.acao-edit').forEach(button => {
    button.addEventListener('click', function() {
        abrirTelaEditar();
    });
});
// Função para fechar Tela de Editar
function fecharTelaEditar() {
    telaEditar.style.display = "none";
}
// Fecha a Tela de Editar ao clicar no botão -> Cancelar
document.getElementById('cancelar-editar').addEventListener('click', fecharTelaEditar);



// Função para abrir Tela de Excluir
function openModal() {
    telaExcluir.style.display = "block";
}
// Abre a Tela de Excluir ao clicar no botão -> Deletar, na Tabela
document.querySelectorAll('.acao-delete').forEach(button => {
    button.addEventListener('click', function() {
        openModal();
    });
});
// Função para fechar Tela de Excluir
function fecharTelaExcluir() {
    telaExcluir.style.display = "none";
}
// Fecha a Tela de Excluir ao clicar no botão -> Cancelar
document.getElementById('cancelar-excluir').addEventListener('click', fecharTelaExcluir);