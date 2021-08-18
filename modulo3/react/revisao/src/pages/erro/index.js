import "./erro.css"
import { Link } from "react-router-dom"
import imgErro from "../../Assets/img/404.gif"

export default function Erro(){
    return(
        <div className="erro">
            <img src={imgErro} alt="404"/>
            <h2>Página não encontrada</h2>
            <Link to="/">Voltar para a home</Link>
        </div>
    );
};