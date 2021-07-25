//<Link>: componente que pertence ao pacote react-router-dom e vai substitui a tag <a> do HTML para acessar as páginas do próprio projeto. Além disso, recebe o parâmetro to. Ele representa o nome da rota que será acessada pela URL.

//O componente Link possui duas tags: uma de abertura e uma de fechamento. Entre as duas tags (abertura e fechamento) será inserido o conteúdo que ficará disponível para ser clicado.

import React from 'react';
import { Link } from 'react-router-dom';

const Home = () =>{
  return (
    <div>
      <h1>Página Inicial</h1>
      <nav>
        <ul>
          <li>
            <Link to="/sobre">Sobre</Link>
          </li>
          <li>
            <Link to="/usuario">Usuario</Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Home;