import React from "react";
import { useState, useEffect } from "react";
import api from "../../services/api";
import {Link} from "react-router-dom"
import "./home.css"

export default function Home(){
  const[filmes, setFilmes] = useState([]);

  useEffect(() =>{
    async function loadFilme(){
      const res = await api.get("r-api/?api=filmes")
      //console.log(res.data)
      setFilmes(res.data);
    }
    loadFilme();
  },[])


  return(
    <div className="conteiner">
      <div className="listaFilmes">
        {filmes.map((f) =>{
          return(
            <article key={f.id}>
              <strong>{f.nome}</strong>
              <img src={f.foto} alt={f.nome}/>
              <Link to={`/filme/${f.id}`}>Acessar</Link>
            </article>
          );
        })}
      </div>
    </div>
  );

};