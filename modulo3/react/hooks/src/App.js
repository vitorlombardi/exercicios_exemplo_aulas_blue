import React, {useState, useEffect} from "react";


function App (){

  // tarefas -> nome do state
  //setTarefas -> funçao que atualiza o valor do useState
  // const[tarefas, setTarefas] = useState([

  //   "pagar conta de Net",
  //   "Comprar ração para os gatos",
  //   "terminar de ler a saga harry potter",
  //   "terminar o abis 12",
  //   "upar o personagem no grand chase"

  // ]); 

  const[tarefas, setTarefas] = useState([]); 

  useEffect(()=>{
    const tarefasStorage= localStorage.getItem("Tarefas");
    if (tarefasStorage){
      setTarefas(JSON.parse(tarefasStorage))
    };
  }, []);

  const[nome, setNome] = useState("tarefas para o dia = 03/08/2021") 
  
  const[input, setInput] = useState("")

  function onClick(){
    setTarefas([...tarefas, input]);
    setInput("")
  }

  

  useEffect(() => {
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
  },[tarefas]
  );

  return(
    <div>
      <ul>
        <h2>{nome}</h2>
        {tarefas.map((t) => (
           <li key = {t}>{t}</li>
        ))}
      </ul>
      <input
      type="text"
      value={input}
      onChange={(e) => setInput(e.target.value)}
      />
      <button type="button" onClick={onClick}>Salvar tarefa</button>
    </div>
  );
  
};

export default App;