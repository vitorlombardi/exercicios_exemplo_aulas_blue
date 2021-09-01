import { Link } from "react-router-dom";
import "./not-found.css"

export default function NotFound() {
    return(
        <div className="not-found">
            <h1>Página não encontrada</h1>
            <br/>
            <img src="https://i.pinimg.com/originals/0e/c0/db/0ec0dbf1e9a008acb9955d3246970e15.gif" alt="Not Found"/>
            <Link to="/">Voltar para home</Link>
        </div>
        

    );
}