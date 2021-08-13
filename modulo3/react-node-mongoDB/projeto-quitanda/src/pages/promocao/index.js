import React, {useState, useEffect} from "react";
import { Link } from 'react-router-dom';
import Vendedor from "../../vendedor"
import Header from "../../header"


const baseUrl = "http://localhost:5000";

export default function Promocao() {
      
  const [produto, setProduto] = useState([]);
  // const [nomeProduto, setNomeProduto] = useState("");
  // const [imagemProduto, setImagemProduto] = useState("");
  // const [ValorProduto, setValorProduto] = useState("");
  // const [tipoProduto, setTipoProduto] = useState("");
  // const [promocaoProduto, setPromocaoProduto] = useState("");
  // const [editando, setEditando] = useState(false);
  // const [idEditando, setIdEditando] = useState(null);

  const loadProduto = async () => {
    const res = await fetch(`${baseUrl}/produtos`);
    const dados = await res.json();
    setProduto(dados);
  };

  useEffect(() => {
    loadProduto();
  }, []);

  const deletar = async (id) => {
    await fetch(`${baseUrl}/produtos/${id}`, {
      method: "DELETE",
  });
  loadProduto();
};
  
    return (
      <div className="conteiner">
          <div className="header">
            <div className="bloco">
              <h1>Quitanda da blue</h1>
            </div>
            <div className="opcs">
              <Header/>
              <hr />
            </div>
          </div>
          <div className="dados">
            <Vendedor/>
            <div className="corpo">
              <span className="titulo">Produtos em promoção</span>
              <ul>
                {produto.filter(fil => fil.promocao === "sim" && "s" && "Sim")
                .map((p, index) => (
                  <li key={index}>
                    <h3>{p.nome}</h3>
                    <img src={p.imagemUrl} alt={p.nome} />
                    <p><b>R$:{p.valor}</b></p>
                    <br />
                    <div className="button">
                      <button className="botao" onClick={() => deletar(p._id)}>Comprar</button>
                      <Link to={`/criar/${p._id}`}>editar</Link>
                    </div>
                  </li>
                ))}
              </ul>
              <br/>
              <br/>
              <Link to="/" className="link">Pagina inicial</Link>
            </div>
          </div>
      </div>
    );
  }






