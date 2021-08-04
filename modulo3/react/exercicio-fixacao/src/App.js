// 1 -) Utilizando o useState do hooks, criar a lista de chamada da nossa classe seguindo as orientações
// abaixo:
//  A lista deve conter um título (esse título deverá ser passado como valor padrão de uma useState).
//  Inicialmente a lista deve conter 4 alunos cadastrados.
//  O nome dos alunos deverá ser mapeado.
//  O restante dos alunos deverá ser cadastrado por meio de um input e a cada cadastro a tela deve
// ser limpa antes da adição de um novo aluno.
//  Deverá ser feita a estilização dessa lista (a critério do aluno).
// 2-) Adicionar a nossa lista de chamada o useEffect simulando o comportamento do componentDidMount
// e o useEffect simulando o comportamento do componentDidUpdate.

import React, {useState, useEffect} from "react";
import "./App.css";

function App() {
   const[lista, setLista] = useState([

    "Adriano Nascimento",
    "Carlos Eduardo",
    "Elias Santana",
    "Gustavo Cervera",

   ]); 

  const[titulo, setTitulo] = useState("Lista de chamada da turma full-Stack") 
  
  const[input, setInput] = useState("")

  function onClick(){
    setLista([...lista, input]);
    setInput("")
  }


  useEffect(() => {
    localStorage.setItem("Alunos", JSON.stringify(lista));
  },[lista]);
  
  

  return(
    <>
      <div className="header">
        <img src="https://blueedtech.com.br/wp-content/themes/blue/dist/images/logo-blue-croped.gif" alt="blue"/>
        <div className="titulo">
          <h2>Turma da tarde Full-Stack </h2>
        </div>
      </div>
      <hr/>
      <div className="conteiner">
        <div className="lista">
          <ul>
            <h2>{titulo}</h2>
            <br/>
            {lista.map((l) => (
              <li key = {l}>{l}</li>
            ))}
          </ul>
        </div>
        <div className="adiciona-aluno">
          <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="digite o nome do aluno"
          className="input"
          />
          <button type="button" onClick={onClick} className="botao">Salvar aluno</button>
        </div>
      </div>
    </>
  );
  
};
  

export default App;
