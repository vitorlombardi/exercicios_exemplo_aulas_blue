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

//3-) Explique com suas palavras qual a vantagem de utilizarmos o useMemo.
//R:o useMemo ele serve para deixar a aplicação “mais leve” para otimizar o código , salvando uma função na memória e sempre deixa em execução não precisando atualizar a página para renderizar . 

// 4-) Utilize na Lista de chamadas criada, o useMemo para exibirmos o total de alunos cadastrados na
// nossa lista de chamada.

// 5-) Qual a diferença entre o useMemo e o UseCallback?
//R:o useMemo serve para otimizar uma aplicação, já o useCallbback mandar uma função de um componente para outro

// 6-) Utilize na lista de chamadas criada o UseCallback no método handleAdd criado.

import React, {useState, useEffect, useMemo, useCallback} from "react";
import "./App.css";

function App() {
   const[lista, setLista] = useState([

     "Adriano Nascimento",
     "Carlos Eduardo",
     "Elias Santana",
     "Gustavo Cervera",

   ]); 

  //const[lista, setLista] = useState([])

  const[titulo, setTitulo] = useState("Lista de chamada da turma full-Stack") 
  
  const[input, setInput] = useState("")

  const onClick= useCallback(() => {
    setLista([...lista, input]);
    setInput("")
  },[input, lista])

  useEffect(() => {
    const listaStorage = localStorage.getItem("Alunos");
    if(listaStorage){
      setLista(JSON.parse(listaStorage))
    }
  },[]);

  useEffect(() => {
    localStorage.setItem("Alunos", JSON.stringify(lista));
  },[lista]);

  const totalAlunos = useMemo(() => lista.length,[lista])

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
          <span className="totalAlunos">Total de alunos {totalAlunos} cadastrados</span>
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
