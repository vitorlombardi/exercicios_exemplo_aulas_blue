import { useState, useEffect } from "react";
import {Link} from "react-router-dom"
import "./home.css"
import {Requisicao} from "../../services/requisicao"

export default function Home(){
  const[post , setPost] = useState([])


  useEffect(() => {
    Requisicao.loadPost()
    .then((res)=> setPost(res))
  }, [])

  return(
    <div className="conteiner">
      <h1>Blog de Nutrição</h1>
      <br/>
      <div className="corpo">
          {post.map((p) => {
            return(
                <article key={p.id}>
                    <strong>{p.titulo}</strong>
                    <Link to={`/post/${p.id}`}>
                        <img src={p.capa}/>
                    </Link>
                    <p>{p.subtitulo}</p>
                </article>
            );
        })}   
                
      </div>
    </div>
  );

};
