import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import "../home/home.css";
import { Requisicao } from "../../services/requisicao";

export default function PostPorId() {
  const { cat } = useParams();
    
  console.log({cat})
  const [post, setPost] = useState([]);

  useEffect(() => {
    Requisicao.loadPost().then((res) => setPost(res));
  }, []);
  console.log(post);

  
  return (
    <div className="conteiner">
      <h1>Pagina em construcão</h1>
      <Link to="/">Voltar</Link>
      {/* <h1>Blog de {`${cat}`}</h1>
      <br />
      <div className="corpo">
        {post.filter((f) => f.id === `${cat}`)
        .map((p) => {
          return (
            <article key={p.id}>
              <strong>{p.titulo}</strong>
              <img src={p.capa} />
              <p>{p.subtitulo}</p>
            </article>
          );
        })}
      </div> */}
    </div>
  );
}
