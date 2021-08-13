// pagina para editar e criar produto : em construção

import React, {useState, useEffect} from 'react';
import { Link, useParams } from 'react-router-dom';
import Header from "../../header"

const baseUrl = "http://localhost:5000";


export default function Criar () {
  const {id} = useParams();
  console.log(id)

    const [nomeProduto, setNomeProduto] = useState("");
    const [imagemProduto, setImagemProduto] = useState("");
    const [valorProduto, setValorProduto] = useState("");
    const [tipoProduto, setTipoProduto] = useState("");
    const [promocaoProduto, setPromocaoProduto] = useState("");
    //const [editando, setEditando] = useState(false);
    //const [idEditando, setIdEditando] = useState(null);

    

    const onSubmit = async (e) => {
        e.preventDefault();

        
        //setIdEditando(id);
        //console.log(idEditando)

        if (id){
          await fetch(`${baseUrl}/produtos/${id}`, {
            method: "PUT",
            header: {"Content-Type": "application/json"},
            body: JSON.stringify({
              nome: nomeProduto,
              imagemUrl: imagemProduto,
              valor: valorProduto,
              tipo: tipoProduto,
              promocao: promocaoProduto,
            }),
          });
        }else{
          await fetch(`${baseUrl}/produtos`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({
              nome: nomeProduto,
              imagemUrl: imagemProduto,
              valor: valorProduto,
              tipo: tipoProduto,
              promocao: promocaoProduto,
            }),
          });
          setNomeProduto("");
          setImagemProduto("");
          setTipoProduto("")
          setValorProduto("");
          setPromocaoProduto("");
        }
        
    }

    return (
        <div>
            <div className="bloco">
              <h1>Quitanda da blue</h1>
            </div>
            <div className="opcs">
              <Header/>
              <hr />
            </div>
            <h2>Criar produto</h2>
            <form onSubmit={onSubmit} className="form">
                <input
                  placeholder="Nome"
                  value={nomeProduto}
                  onChange={(e) => {
                    setNomeProduto(e.target.value)
                  }}
                />
                <input
                  placeholder="Url da Imagem"
                  value={imagemProduto}
                  onChange={(e) => {
                   setImagemProduto(e.target.value)
                  }}
                />
                <input
                  placeholder="tipo do produto"
                  value={tipoProduto}
                  onChange={(e) => {
                   setTipoProduto(e.target.value)
                  }}
                />
                <input
                  placeholder="promoção"
                  value={promocaoProduto}
                  onChange={(e) => {
                    setPromocaoProduto(e.target.value)
                  }}
                />
                <input
                  type="text"
                  placeholder="valor"
                  value={valorProduto}
                  onChange={(e) => {
                   setValorProduto(e.target.value)
                    }}
                />
                <br />
                <button className="botao" type="submit">Salvar</button>
            </form>
        </div>
    )
}