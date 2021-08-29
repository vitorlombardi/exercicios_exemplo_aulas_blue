import "../header/header.css";
import { Link } from "react-router-dom";

export default function Header() {
  const dica = "Dicas"
  const dieta = "Deita"
  const emagrecimento = "Emagrecimento"
  return (
    <header className="header">
        <Link id="titulo" to="/">Blog do Jorginho</Link>
        <ul className="bloco-nav">
            <li><Link to={`/categoria/${dica}`}>Dicas</Link></li>
            <li><Link to={`/categoria/${dieta}`}>Dieta</Link></li>
            <li><Link to={`/categoria/${emagrecimento}`}>Emagrecimento</Link></li>
            <li><Link to="/favoritos">Favoritos</Link></li>
        </ul>
    </header>
  );
}
