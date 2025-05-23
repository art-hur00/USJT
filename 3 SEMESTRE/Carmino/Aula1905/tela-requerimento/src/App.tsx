import React, { useEffect, useState } from 'react';
import './App.css';

interface Convidado {
  _id?: string;
  nome: string;
  endereco: string;
  cidade: string;
}

const endpointBase = 'https://crudcrud.com/api/44ed57aab4ae415a92e3553444f98d6d/convidados'; // Substitua com seu novo endpoint válido do crudcrud

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

    if (acao === 'novo') {
      setFormData({ nome: '', endereco: '', cidade: '' });
    } else if ((acao === 'editar' || acao === 'excluir') && id) {
      const convidado = convidados.find(c => c._id === id);
      if (convidado) setFormData(convidado);
    }

    setModalVisible(true);
  };

  const fecharModal = () => {
    setModalVisible(false);
    setAcaoAtual(null);
    setFormData({ nome: '', endereco: '', cidade: '' });
    setIdAtual('');
  };

  const salvar = async () => {
    try {
      if (acaoAtual === 'novo') {
        await fetch(endpointBase, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(formData)
        });
      } else if (acaoAtual === 'editar' && idAtual) {
        const { _id, ...dadosSemId } = formData;
        await fetch(`${endpointBase}/${idAtual}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(dadosSemId)
        });
      } else if (acaoAtual === 'excluir' && idAtual) {
        await fetch(`${endpointBase}/${idAtual}`, {
          method: 'DELETE'
        });
      }

      await carregarLista();
      fecharModal();
    } catch (error) {
      console.error('Erro na operação:', error);
    }
  };

  return (
    <div className="App">
      <div className="cont-esq">
        <div className="campo">
          <div className="label-box">ID</div>
          <input type="text" value={formData._id || ''} readOnly />
        </div>

        <div className="campo">
          <div className="label-box">Nome</div>
          <input
            type="text"
            value={formData.nome}
            onChange={(e) => setFormData({ ...formData, nome: e.target.value })}
          />
        </div>

        <div className="campo">
          <div className="label-box">Endereço</div>
          <input
            type="text"
            value={formData.endereco}
            onChange={(e) => setFormData({ ...formData, endereco: e.target.value })}
          />
        </div>

        <div className="campo">
          <div className="label-box">Cidade</div>
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
            <h3>Confirmar {acaoAtual?.toUpperCase()}?</h3>
            <button onClick={salvar}>Salvar</button>
            <button onClick={fecharModal}>Cancelar</button>
          </div>
        </div>
      )}
    </div>
  );
};

export default App;





