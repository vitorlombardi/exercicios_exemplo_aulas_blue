import React from "react";
import { Link } from "react-router-dom";
import Vendedor from "../../vendedor";
import Header from "../../header";

export default class Legumes extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      legumes: [],
      nome_legme: "",
      imagem_legume: "",
      valor_legume: "",
      tipo_produto: "",
      promocao_produto: "",
      editando: false,
      index_editando: null,
    };
  }

  async buscarProduto() {
    this.setState({ loading: true });

    const res = await fetch("http://localhost:5000/produtos");
    const json = await res.json();

    this.setState({ legumes: json, loading: false });
  }

  componentDidMount() {
    this.buscarProduto();
  }

  onSubmit = async (e) => {
    e.preventDefault();

    const {
      legumes,
      editando,
      index_editando,
      nome_legme,
      imagem_legume,
      valor_legume,
      tipo_produto,
      promocao_produto,
      idEditando,
    } = this.state;

    if (editando) {
      await fetch(`http://localhost:5000/produtos/${idEditando}`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          nome: nome_legme,
          imagemUrl: imagem_legume,
          valor: valor_legume,
          tipo: tipo_produto,
          promocao: promocao_produto,
        }),
      });
      this.buscarProduto();
      this.setState({
        index_editando: null,
        editando: false,
      });
    } else {
      await fetch("http://localhost:5000/produtos", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          nome: nome_legme,
          imagemUrl: imagem_legume,
          valor: valor_legume,
          tipo: tipo_produto,
          promocao: promocao_produto,
        }),
      });
      this.buscarProduto();
    };

    this.setState({
      nome_legme: "",
      imagem_legume: "",
      valor_legume: "",
      tipo_produto: "",
      promocao_produto: "",
    });
  };

  deletar = async (idDeletar) => {
    await fetch(`http://localhost:5000/produtos/${idDeletar}`, {
      method: "DELETE",
    });
    this.buscarProduto();
  };

  render() {
    const {
      legumes,
      nome_legme,
      imagem_legume,
      editando,
      index_editando,
      valor_legume,
      tipo_produto,
      promocao_produto,
    } = this.state;
    return (
      <div className="conteiner">
        <main className="main">
          <div className="header">
            <div className="bloco">
              <h1>Quitanda da blue</h1>
            </div>
            <div className="opcs">
              <Header />
              <hr />
            </div>
            <div className="bloco">
              <h2>
                {editando
                  ? `Editando:${legumes[index_editando].nome}`
                  : "cadastre um novo legume"}
              </h2>
              <form onSubmit={this.onSubmit} className="form">
                <input
                  placeholder="Nome"
                  value={nome_legme}
                  onChange={(e) => {
                    this.setState({
                      nome_legme: e.target.value,
                    });
                  }}
                />
                <input
                  placeholder="Url da Imagem"
                  value={imagem_legume}
                  onChange={(e) => {
                    this.setState({
                      imagem_legume: e.target.value,
                    });
                  }}
                />
                <input
                  placeholder="tipo do produto"
                  value={tipo_produto}
                  onChange={(e) => {
                    this.setState({
                      tipo_produto: e.target.value,
                    });
                  }}
                />
                <input
                  placeholder="promoção"
                  value={promocao_produto}
                  onChange={(e) => {
                    this.setState({
                      promocao_produto: e.target.value,
                    });
                  }}
                />
                <input
                  type="number"
                  placeholder="Valor"
                  value={valor_legume}
                  onChange={(e) => {
                    this.setState({
                      valor_legume: e.target.value,
                    });
                  }}
                />
                <br />
                <button 
                className="botao" 
                type="submit">
                  Salvar
                </button>
              </form>
            </div>
            <hr />
          </div>
          <div className="dados">
            <Vendedor />
            <div className="corpo">
              <span className="titulo">Legumes</span>
              <ul>
                {legumes.filter(fil => fil.tipo === "legume" && "legumes" && "l")
                .map((l, index) => (
                  <li key={l._id}>
                    <h3>{l.nome}</h3>
                    <img src={l.imagemUrl} alt={l.nome} />
                    <p>
                      <b>valor: {l.valor}</b>
                    </p>
                    <br />
                    <div className="button">
                      <button
                        className="botao"
                        onClick={() => this.deletar(l._id)}
                      >
                        Comprar
                      </button>
                      <br />
                      <button
                        className="botao"
                        onClick={() => {
                          this.setState({
                            idEditando: l._id,
                            editando: true,
                            index_editando: index,
                            nome_legme: l.nome,
                            imagem_legume: l.imagemUrl,
                            valor_legume: l.valor,
                            tipo_produto: l.tipo,
                            promocao_produto: l.promocao,
                          });
                        }}
                      >
                        Mudar anuncio
                      </button>
                    </div>
                  </li>
                ))}
              </ul>
              <br />
              <Link to="/" className="link">
                Pagina inicial
              </Link>
            </div>
          </div>
        </main>
      </div>
    );
  }
}
