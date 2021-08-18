import { useState, useEffect } from "react";
import { Link } from "react-router-dom"
import "./favoritos.css";
import { toast } from "react-toastify"


export default function Favoritos(){

    const[filmes, setFilmes] = useState([]);

    useEffect(() => {
        const minhaLista = localStorage.getItem("filmes");
        setFilmes(JSON.parse(minhaLista) || []);
    }, [])

    function handleDelete(id) {
        let filtroFilmes = filmes.filter((f) => {
            return f.id !== id;
        });
        setFilmes(filtroFilmes)
        localStorage.setItem("filmes", JSON.stringify(filtroFilmes));
        toast.success("Filme excluido com sucesso")
    };

    return(
        <div id="meusFilmes">
            <h1>Filmes favoritos</h1>
            <ul>
                {filmes.map((f) => {
                    return(
                        <li key={f.id}>
                            <div className="itens">
                                <span>{f.nome}</span>
                                <div>
                                    <Link to={`/filme/${f.id}`}>Ver mais</Link>
                                
                                    <button onClick={() => handleDelete(f.id)}>Excluir</button>
                                </div>
                            </div>
                        </li>
                    )
                })}
            </ul>
        </div>
    );
}