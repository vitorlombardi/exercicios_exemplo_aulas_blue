/*componentes x props

props > são as propriedades dos componentes (similares aos atributos de um objeto)

componentes > são pedaços de codigo (header, footer, slider)
sao divididos em 2 grupos : class componets

stateless componentes: componentes "burros", não tem ciclo de vida, so exibe algumas coisas que vc passa para ele.*/


import Heact from 'react';
import "./App.css"

const Equipe = (props) => {

    return(

        <div className="adm">
            <Sobre_equipe nome = {props.nome} cargo = {props.cargo} idade = {props.idade} rede_Social = {props.rede_Social}/>
            

        </div>

    );

};

const Alunos = (props) => {

    return(

        <div>
            <Sobre_aluno nome = {props.nome} idade = {props.idade} rede_Social = {props.rede_Social}  />
            <hr/>

        </div>

    );

};

const Sobre_equipe = (props) => {

    return(

        <div className="pr_bloco" >
            
            <p><b>Nome:</b> {props.nome}</p>
            <p><b>cargo:</b> {props.cargo}</p>
            <p><b>idade:</b> {props.idade}</p>
            <a href={props.rede_Social}><b>Meu Github</b></a>

        </div>

    );

};

const Sobre_aluno = (props) => {

    return(

        <div className="al_bloco">

            <p><b>Nome:</b> {props.nome}</p>
            <p><b>Idade:</b> {props.idade}</p>
            <a href={props.rede_Social}><b>Github</b></a>

            
        </div>

    );

};


function App(){

    return(

        <div>
             <div className="pr">
                <h2 className="titolo">conheça nosso professor</h2>
                <br></br>
                <Equipe img="" nome="Gustavo agiota" cargo ="Coordenedor" idade ="30" rede_Social = "https://www.linkedin.com/in/gustavo-molina-a2798418/"/>
            </div>
            
            <div className="al">
                <h2 className="titolo">conheça os alunos</h2>
                <br></br>

                <Alunos nome="Adriano" idade ="?" rede_Social = "https://www.linkedin.com/in/adriano-guimaraes-978b3a80/"/>
                <Alunos nome="Carlos" idade ="?" rede_Social = "https://www.linkedin.com/in/carlos-eduardo-lima-galvão-a92707174"/>
                <Alunos nome="David" idade ="?" rede_Social = "https://www.linkedin.com/in/sotto-mayor"/>
                <Alunos nome="Diego" idade ="?" rede_Social = "https://www.linkedin.com/in/diego-moraes-6445aa4a/"/>
                <Alunos nome="Elias" idade ="?" rede_Social = "https://www.linkedin.com/in/elias-santana-225310208"/>
                <Alunos nome="gabriel " idade ="?" rede_Social = "https://www.linkedin.com/in/gabriel-duarte-69691a125" />
                <Alunos nome="Gustavo" idade ="?" rede_Social = "https://www.linkedin.com/in/gustavo-carvera"/>
                <Alunos nome="Jorginho" idade ="18" rede_Social = "https://www.linkedin.com/in/vitor-lombardi-23b447211"/>
                <Alunos nome="Matheus" idade ="?" rede_Social = "https://www.linkedin.com/in/theusmaoliver/"/>
                <Alunos nome="Marcos" idade ="200" rede_Social = "https://www.linkedin.com/in/marcos-domingues"/>
                <Alunos nome="Paulo" idade ="?" rede_Social = "https://www.linkedin.com/in/paulohenriquegama/"/>

            </div>

        </div>

    );

   
    

}

export default App;