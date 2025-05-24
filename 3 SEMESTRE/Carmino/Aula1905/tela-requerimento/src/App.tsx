import React, { useEffect, useState } from 'react';
import './App.css';

interface Convidado {
  _id?: string;
  nome: string;
  endereco: string;
  cidade: string;
}

const endpointBase = 'https://crudcrud.com/api/7b9e2d02bd1b4fcea2cd427d479ee37c/convidados';

const App: React.FC = () => {
  const [convidados, setConvidados] = useState<Convidado[]>([]);
  const [formData, setFormData] = useState<Convidado>({ nome: '', endereco: '', cidade: '' });
  const [modalVisible, setModalVisible] = useState(false);
  const [acaoAtual, setAcaoAtual] = useState<'novo' | 'editar' | 'excluir' | null>(null);
  const [idAtual, setIdAtual] = useState<string>('');

  useEffect(() => {
    carregarLista();
  }, []);

  const carregarLista = async () => {
    try {
      const res = await fetch(endpointBase);
      const dados = await res.json();
      setConvidados(dados);
    } catch (error) {
      console.error('Erro ao carregar lista:', error);
    }
  };

  const abrirModal = (acao: 'novo' | 'editar' | 'excluir', id: string = '') => {
    setAcaoAtual(acao);
    setIdAtual(id);

    if (acao === 'excluir' && id) {
      const convidado = convidados.find(c => c._id === id);
      if (convidado) setFormData(convidado);
    }

    setModalVisible(true);
  };

  const fecharModal = () => {
    setModalVisible(false);
    setAcaoAtual(null);
    setIdAtual('');
  };

  const salvar = async () => {
    try {
      const { nome, endereco, cidade } = formData;
      if (!nome || !endereco || !cidade) {
        alert('Preencha todos os campos antes de salvar.');
        return;
      }

      if (acaoAtual === 'novo') {
        const { _id, ...semId } = formData;
        await fetch(endpointBase, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(semId),
        });
      } else if (acaoAtual === 'editar' && idAtual) {
        const { _id, ...dadosSemId } = formData;
        await fetch(`${endpointBase}/${idAtual}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(dadosSemId),
        });
      } else if (acaoAtual === 'excluir' && idAtual) {
        await fetch(`${endpointBase}/${idAtual}`, {
          method: 'DELETE',
        });
      }

      await carregarLista();
      setFormData({ nome: '', endereco: '', cidade: '' }); // Limpa só depois de salvar
      fecharModal();
    } catch (error) {
      console.error('Erro na operação:', error);
    }
  };

  return (
    <div className="App">
      <div className="cont-esq">
        <div className="form-field">
          <label>ID</label>
          <input type="text" value={formData._id || ''} readOnly />
        </div>

        <div className="form-field">
          <label>Nome</label>
          <input
            type="text"
            value={formData.nome}
            onChange={(e) => setFormData({ ...formData, nome: e.target.value })}
          />
        </div>

        <div className="form-field">
          <label>Endereço</label>
          <input
            type="text"
            value={formData.endereco}
            onChange={(e) => setFormData({ ...formData, endereco: e.target.value })}
          />
        </div>

        <div className="form-field">
          <label>Cidade</label>
          <input
            type="text"
            value={formData.cidade}
            onChange={(e) => setFormData({ ...formData, cidade: e.target.value })}
          />
        </div>

        <div className="Botoes">
          <button onClick={() => abrirModal('novo')}>Novo</button>
          <button onClick={() => abrirModal('editar', formData._id || '')}>Editar</button>
          <button onClick={() => abrirModal('excluir', formData._id || '')}>Excluir</button>
        </div>
      </div>

      <div className="cont-dir">
        <h3>Lista de clientes</h3>
        <ul>
          {convidados.map((c) => (
            <li key={c._id} onClick={() => setFormData(c)}>
              {c.nome} ({c.cidade})
            </li>
          ))}
        </ul>
      </div>

      {modalVisible && (
        <div className="modal">
          <div className="modal-content">
            <h3>Deseja confirmar a ação: {acaoAtual?.toUpperCase()}?</h3>
            <p>Nome: {formData.nome}</p>
            <p>Endereço: {formData.endereco}</p>
            <p>Cidade: {formData.cidade}</p>
            <button onClick={salvar}>Confirmar</button>
            <button onClick={fecharModal}>Cancelar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;




