import { useState, useEffect } from "react";
import { useParams, useHistory } from "react-router-dom";
import "./post-id.css";
import { Requisicao } from "../../services/requisicao";
import { toast } from "react-toastify"

export default function PostPorId() {
  const { id } = useParams();
  const idInt = parseInt(id);
  const [post, setPost] = useState([]);
  const [loading, setLoading] = useState(true);
  const history = useHistory();

  useEffect(() => {
    Requisicao.loadPost()
      .then((res) => res.find((find) => find.id === idInt))
      .then((data) => {
        if (!data) {
          history.replace("/");
          return;
        }

        setPost(data);
        setLoading(false);
      });
  }, [history, id, idInt]);

  function salvaPost() {
    const minhaListaPost = localStorage.getItem("posts");
    let PostSalvos = JSON.parse(minhaListaPost) || [];
    const temPost = PostSalvos.some((postSalvo) => postSalvo.id === post.id);

    if (temPost) {
      toast.info("Esse post já esta salvo ✔");
      return;
    }
    PostSalvos.push(post);
    localStorage.setItem("posts", JSON.stringify(PostSalvos));
    toast.success("Post salvo com sucesso ^_^");
  }

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
      <div className="info">
        <div className="corpo">
          <article key={post.id}>
              <strong>{post.titulo}</strong>
              <br />
              <img src={post.capa} alt={post.categoria} />
              <p>{post.subtitulo}</p>
              <button onClick={salvaPost}>Salvar</button>
          </article>
        </div>
      </div>
    </div>
  );
}
