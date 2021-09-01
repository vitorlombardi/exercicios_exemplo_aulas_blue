import { useState, useEffect } from "react";
import { Link, useParams } from "react-router-dom";
import "../../style.css";
import { Requisicao } from "../../services/requisicao";

export default function Categoria() {
  const { cat } = useParams();

  console.log({ cat });
  const [post, setPost] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Requisicao.loadPost().then((res) => {
      setPost(res);
      setLoading(false);
    });
  }, []);
  console.log(post);

  if (loading) {
    return (
      <div className="post-carregando">
        <h1>Carregando...</h1>
        <img
          src="https://fellipe.com/slides/performance-javascript/i/loading.gif"
          alt="gif"
        />
      </div>
    );
  }

  return (
    <div className="conteiner">
      <h1>Blog de {`${cat}`}</h1>
      <br />
      <div className="corpo">
        {post
          .filter((f) => f.categoria === `${cat}`)
          .map((p) => {
            return (
              <article key={p.id}>
                <hr />
                <div className="corpo-post">
                  <Link to={`/post/${p.id}`}>
                    <img src={p.capa} alt={p.categoria} />
                  </Link>
                  <div className="titulos">
                    <strong>{p.titulo}</strong>
                    <p>{p.subtitulo}</p>
                  </div>
                </div>
              </article>
            );
          })}
      </div>
    </div>
  );
}
