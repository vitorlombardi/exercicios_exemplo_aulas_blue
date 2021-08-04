import React, {useState, useEffect, useMemo, useCallback} from "react";


function App (){

  // tarefas -> nome do state
  //setTarefas -> funçao que atualiza o valor do useState
   const[tarefas, setTarefas] = useState([

     "pagar conta de Net",
     "Comprar ração para os gatos",
     "terminar de ler a saga harry potter",
     "terminar o abis 12",
     "upar o personagem no grand chase"

   ]); 

  // const[tarefas, setTarefas] = useState([]); 

  const[nome, setNome] = useState("tarefas para o dia = 04/08/2021");
  
  const[input, setInput] = useState("");

  // function onClick(){
  //   setTarefas([...tarefas, input]);
  //   setInput("")
  // };

  const onClick = useCallback(() => {
       setTarefas([...tarefas, input]);
       setInput("");
  },[input, tarefas]);


  useEffect(()=>{
    const tarefasStorage= localStorage.getItem("tarefas");
    if (tarefasStorage){
      setTarefas(JSON.parse(tarefasStorage))
    };
  }, []);

  useEffect(() => {
    localStorage.setItem("tarefas", JSON.stringify(tarefas));
  },[tarefas]
  );

  const totalTarefas = useMemo(() => tarefas.length,[tarefas]);

  return(
    <div>
      <ul>
        <h2>{nome}</h2>
        {tarefas.map((t) => (
           <li key = {t}>{t}</li>
        ))}
      </ul>
      <br/>
      <strong>Você tem {totalTarefas} tarefas</strong>
      <br/>
      <br/>
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