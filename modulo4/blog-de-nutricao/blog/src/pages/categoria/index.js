import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import "../home/home.css";
import { Requisicao } from "../../services/requisicao";

export default function Categoria() {
  const { cat } = useParams();
    
  console.log({cat})
  const [post, setPost] = useState([]);

  useEffect(() => {
    Requisicao.loadPost().then((res) => setPost(res));
  }, []);
  console.log(post);

  
  return (
    <div className="conteiner">
      <h1>Blog de {`${cat}`}</h1>
      <br />
      <div className="corpo">
        {post.filter((f) => f.categoria === `${cat}`)
        .map((p) => {
          return (
            <article key={p.id}>
              <strong>{p.titulo}</strong>
              <Link to="/">
                <img src={p.capa} />
              </Link>
              <p>{p.subtitulo}</p>
            </article>
          );
        })}
      </div>
    </div>
  );
}
