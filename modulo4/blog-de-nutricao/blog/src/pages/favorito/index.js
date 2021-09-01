import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./favorito.css";
import { toast } from "react-toastify"

export default function Favoritos() {
  const [post, setPost] = useState([]);

  useEffect(() => {
    const minhaListaPost = localStorage.getItem("posts");
    setPost(JSON.parse(minhaListaPost) || []);
  }, []);

  function deletarPost(id) {
    let filtroPostId = post.filter((f) => f.id !== id);
    setPost(filtroPostId);
    localStorage.setItem("posts", JSON.stringify(filtroPostId));
    toast.error("filme excluido com sucesso ✖");
  }

  return (
    <div className="post-favorito">
      <ul>
        {post.map((p) => {
          return (
            <div className="lista-post">
              <li key={p.id}>
                <div className="itens">
                  <img src={p.capa} alt={p.categoria} />
                  <span>{p.titulo}</span>
                  <Link to={`/post/${p.id}`}>ver post</Link>
                  <button onClick={() => deletarPost(p.id)}>excluir</button>
                </div>
              </li>
            </div>
          );
        })}
      </ul>
    </div>
  );
}
