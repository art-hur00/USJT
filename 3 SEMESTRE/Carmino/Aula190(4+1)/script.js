const endpointBase = 'https://crudcrud.com/api/118e57538b334c8b8b60d32c305daac6/convidados';

let acaoAtual = ''; // novo, editar ou excluir
let idAtual = '';

const modal = document.getElementById('modal');
const modalTitulo = document.getElementById('modal-titulo');

function abrirModal(acao, id = '') {
  acaoAtual = acao;
  idAtual = id;
  modalTitulo.textContent = `Deseja confirmar a ação: ${acao.toUpperCase()}?`;
  modal.style.display = 'flex';
}

document.getElementById('bt-nv').addEventListener('click', () => {
  abrirModal('novo');
});

document.getElementById('bt-edt').addEventListener('click', () => {
  const id = document.getElementById('id').value;
  if (!id) return alert('Preencha o ID para editar.');
  abrirModal('editar', id);
});

document.getElementById('bt-exc').addEventListener('click', () => {
  const id = document.getElementById('id').value;
  if (!id) return alert('Preencha o ID para excluir.');
  abrirModal('excluir', id);
});

document.getElementById('modal-cancelar').addEventListener('click', () => {
  modal.style.display = 'none';
});

document.getElementById('modal-salvar').addEventListener('click', async () => {
  const nome = document.getElementById('nome').value;
  const endereco = document.getElementById('endereco').value;
  const cidade = document.getElementById('cidade').value;

  try {
    if (acaoAtual === 'novo') {
      await fetch(endpointBase, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, endereco, cidade })
      });
    }

    if (acaoAtual === 'editar') {
      await fetch(`${endpointBase}/${idAtual}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ nome, endereco, cidade })
      });
    }

    if (acaoAtual === 'excluir') {
      await fetch(`${endpointBase}/${idAtual}`, {
        method: 'DELETE'
      });
    }
  } catch (e) {
    console.error('Erro na operação:', e);
  }

  modal.style.display = 'none';
  carregarLista();
});

async function carregarLista() {
  const lista = document.getElementById('lista-clientes');
  const res = await fetch(endpointBase);
  const dados = await res.json();

document.getElementById('id').value = '';
document.getElementById('nome').value = '';
document.getElementById('endereco').value = '';
document.getElementById('cidade').value = '';


  lista.innerHTML = '<h3>Lista de clientes</h3>';
  dados.forEach(pessoa => {
    const item = document.createElement('li');
    item.textContent = `${pessoa.nome} (${pessoa.cidade})`;
    item.addEventListener('click', () => {
      document.getElementById('id').value = pessoa._id;
      document.getElementById('nome').value = pessoa.nome;
      document.getElementById('endereco').value = pessoa.endereco;
      document.getElementById('cidade').value = pessoa.cidade;
    });
    lista.appendChild(item);
  });
}

carregarLista();

