import React, {useState, useEffect} from "react";
import { Link } from 'react-router-dom';
import Vendedor from "../../vendedor"
import Header from "../../header"

const baseUrl = "http://localhost:5000";


export default function Frutas() {
  const [frutas, setFrutas] = useState([]);
  const [nome_fruta, setNomeFrutas] = useState("");
  const [imagem_fruta, setImagemFrutas] = useState("");
  const [valor_fruta, setValorFrutas] = useState("");
  const [tipo_fruta, setTipoFrutas] = useState("");
  const [promocao_fruta, setPromocaoFrutas] = useState("");
  const [editando, setEditando] = useState(false);
  const [idEditando, setIdEditando] = useState(null);

  const loadProduto = async () => {
    const res = await fetch(`${baseUrl}/produtos`);
    const dados = await res.json();
    setFrutas(dados);
  };

  useEffect(() => {
    loadProduto();
  }, []);

  useEffect(() => {
    if (idEditando !== null && editando){
      const fruta = frutas.find((f) => f._id === idEditando);
      setNomeFrutas(fruta.nome);
      setImagemFrutas(fruta.imagemUrl);
      setValorFrutas(fruta.valor);
      setTipoFrutas(fruta.tipo);
      setPromocaoFrutas(fruta.promocao);
    }
  }, [idEditando]);

  const onSubmit = async (e) => {
    e.preventDefault();

    if (editando) {
      await fetch(`${baseUrl}/produtos/${idEditando}`, {
        method: "PUT",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          nome: nome_fruta,
          imagemUrl: imagem_fruta,
          valor: valor_fruta,
          tipo: tipo_fruta,
          promocao: promocao_fruta,
        }),
      });
      setEditando(false);
      setIdEditando(null);
    } else {
      await fetch(`${baseUrl}/produtos`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
          nome: nome_fruta,
          imagemUrl: imagem_fruta,
          valor: valor_fruta,
          tipo: tipo_fruta,
          promocao: promocao_fruta,
        }),
      });
    }
    loadProduto();
    setNomeFrutas("");
    setImagemFrutas("");
    setTipoFrutas("")
    setValorFrutas("");
    setPromocaoFrutas("");
  };


  const deletar = async (id) => {
    await fetch(`${baseUrl}/produtos/${id}`, {
      method: "DELETE",
  });
  loadProduto();
};

    return (
      <div className="conteiner">
        <main className="main">
          <div className="header">
            <div className="bloco">
              <h1>Quitanda da blue</h1>
            </div>
            <div className="opcs">
              <Header/>
              <hr />
            </div>
            <div className="bloco">
              <h2>
                {editando
                  ? `Editando:${frutas.find((f) => f._id === idEditando)?.nome}`
                  : "cadastre uma nova fruta"}
              </h2>
              <form onSubmit={onSubmit} className="form">
                <input
                  placeholder="Nome"
                  value={nome_fruta}
                  onChange={(e) => {
                    setNomeFrutas(e.target.value)
                  }}
                />
                <input
                  placeholder="Url da Imagem"
                  value={imagem_fruta}
                  onChange={(e) => {
                   setImagemFrutas(e.target.value)
                  }}
                />
                <input
                  placeholder="tipo do produto"
                  value={tipo_fruta}
                  onChange={(e) => {
                   setTipoFrutas(e.target.value)
                  }}
                />
                <input
                  placeholder="promoção"
                  value={promocao_fruta}
                  onChange={(e) => {
                    setPromocaoFrutas(e.target.value)
                  }}
                />
                <input
                  type="text"
                  placeholder="valor"
                  value={valor_fruta}
                  onChange={(e) => {
                   setValorFrutas(e.target.value)
                    }}
                />
                <br />
                <button className="botao" type="submit">Salvar</button>
              </form>
            </div>
            <hr />
          </div>
          <div className="dados">
            <Vendedor/>
            <div className="corpo">
              <span className="titulo">Frutas</span>
              <ul>
                {frutas.filter(fil => fil.tipo === "fruta" && "frutas" && "f")
                .map((f, index) => (
                  <li key={index}>
                    <h3>{f.nome}</h3>
                    <img src={f.imagemUrl} alt={f.nome} />
                    <p><b>{f.valor}</b></p>
                    <br />
                    <div className="button">
                      <button className="botao" onClick={() => deletar(f._id)}>comprar</button>
                      <br/>
                      <button className="botao"
                        onClick={() => {
                            setEditando(true);
                            setIdEditando(f._id);
                        }}
                      >
                        Mudar anuncio
                      </button>
                    </div>
                  </li>
                ))}
              </ul>
              <br/>
              <Link to="/" className="link">Pagina inicial</Link>
            </div>
          </div>
        </main>
      </div>
    );
  }






