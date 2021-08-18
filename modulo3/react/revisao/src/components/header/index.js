import React from "react";
import {Link} from "react-router-dom" 
import "./header.css"

export default function Header() {
  return (
    <header>
      <Link className="logo" to="/">Jorginho Filmes</Link>
      <Link className="favoritos" to="/favoritos">Favoritos</Link>
    </header>
  );
}
