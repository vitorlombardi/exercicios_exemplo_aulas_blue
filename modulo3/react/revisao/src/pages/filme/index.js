import { useState, useEffect } from "react";
import { useParams, useHistory } from "react-router-dom";
import "./filme.css";
import api from "../../services/api";
import { toast } from "react-toastify"

export default function Filme() {
  const { id } = useParams();
  //console.log({id})
  const [filme, setFilme] = useState([]);
  const [loading, setLoading] = useState(true);
  const history = useHistory();

  useEffect(() => {
    async function loadFilme() {
      const res = await api.get(`r-api/?api=filmes/${id}`);
      setFilme(res.data);
      setLoading(false);
      //console.log(res.data)

      if(res.data.length === 0){
        history.replace("/")
        return;
      }
    }
    loadFilme();
  }, [id, history]);

  function salvaFilme() {
    //alert("bao fio, isso e um teste");
    const minhaLista = localStorage.getItem("filmes");
    let filmesSalvos = JSON.parse(minhaLista) || [];
    const hasFilme = filmesSalvos.some(
      (filmeSalvo) => filmeSalvo.id === filme.id
    );

    if (hasFilme) {
    toast.info("Este filme já esta salvo");
      return;
    }
    filmesSalvos.push(filme);
    localStorage.setItem("filmes", JSON.stringify(filmesSalvos));
    toast.success("Filme salvo com sucesso")
  }

  if (loading) {
    return (
      <div className="filme_carregando">
        <h1>Carregando...</h1>
        <img
          src="https://fellipe.com/slides/performance-javascript/i/loading.gif"
          alt="gif"
        />
      </div>
    );
  }

  return (
    <div className="filme-info">
      <h1>{filme.nome}</h1>
      <img src={filme.foto} alt={filme.nome} />
      <h3>sinopse</h3>
      {filme.sinopse}

      <div className="botao">
        <button onClick={salvaFilme}>Salvar</button>
        <button>
          <a
            target="blank"
            href={`http://youtube.com//results?search_query=${filme.nome} Trailer`}
          >
            Trailer
          </a>
        </button>
      </div>
    </div>
  );
}
