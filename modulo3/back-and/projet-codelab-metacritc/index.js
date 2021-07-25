const express = require('express');
const app = express();
const port = 4000;
app.use(express.json());


const jogos = [

    {
    id:1,
    nome:"The Legend of Zelda: Ocarina of Time",
    url:"https://upload.wikimedia.org/wikipedia/pt/thumb/1/17/The_Legend_of_Zelda_Ocarina_of_Time_capa.png/280px-The_Legend_of_Zelda_Ocarina_of_Time_capa.png",
    ano:"1998",
    plataforma:'Nintendo',
    nota:"99",
    critica:"bla bla bla bla"
    },

    {
    id:2,
    nome:"God of War",
    url:"https://meups.com.br/wp-content/uploads/2018/01/God-of-War-4-900x503.jpg",
    ano:"2018",
    plataforma:'PlayStation',
    nota:"94",
    critica:"bla bla bla bla"
    },

    {
    id:3,
    nome:"Forza Horizon 4",
    url:"https://dropsdejogos.uai.com.br/wp-content/uploads/sites/10/2020/08/forza-950x634.jpg",
    ano:"2018",
    plataforma:'Xbox',
    nota:"92",
    criica:"bla bla bla"
    },
    

    {
    id:4,
    nome:"Control",
    url:"https://1.bp.blogspot.com/-jP2JYlJwCpw/XXcCzx4AycI/AAAAAAAAD8s/SYlhyRnuk8Iol8-WKtZJMCTiDCWKgcmswCLcBGAs/s640/082793%2B%25281%2529.png",
    ano:"2019",
    plataforma:'Multiplataforma',
    nota:"85",
    critica:"bla bla bla"
    },

    {
    id:5,
    nome:"The Witcher 3: Wild Hunt",
    url:"https://dropsdejogos.uai.com.br/wp-content/uploads/sites/10/2019/12/witcher-1-950x584.jpg",
    ano:"2015",
    plataforma:'Multiplataforma',
    nota:"93",
    critica:"bla bla bla"
    },

    {
    id:6,
    nome:"Grand Chase",
    url:"https://1.bp.blogspot.com/-AgNfcJpQ6wI/YNxf6LYE3hI/AAAAAAAA9mA/3IK3JWoMs7ICF761PpkY2KFNqm9Hok6jwCLcBGAsYHQ/w640-h416/GrandChaseClassic.jpg",
    ano:"2003",
    plataforma:'PC',
    nota:"98",
    critica:"bla bla bla"
    },

]

const get_jogos_validos = () => jogos.filter(Boolean);
const get_jogo_id = id => get_jogos_validos().find(jogo=>jogo.id===id)
const get_jogo_index_id = id => get_jogos_validos().findIndex(jogo=>jogo.id===id)



app.get('/', (req, res) => {

    res.send('Ola blumer');

});



app.get('/bluecritc', (req, res) => {

    res.send(get_jogos_validos());

});



app.get('/bluecritc/:id', (req, res) => {

    const id = +req.params.id;
    const jogo = get_jogo_id(id);
    
    if (!jogo){
        res.send('jogo não encontrado');
        return;
    }

    res.send(jogo);


});


app.post('/bluecritc', (req, res) => {

    let jogo = req.body;

    
    if(!jogo || !jogo.nome || !jogo.ano || !jogo.plataforma || !jogo.nota || !jogo.critica){

        res.status(400).send({message:"Deu ruim jogo invalido. certifique-se de que o body da requisiçao possui todos os dados."});

        return;
    }

    jogo.id = jogos.length+1;
    let data = jogos
    jogo = {id: data.id, ...jogo}
    jogos.push(jogo);
    
    res.send(jogo)

});


app.put('/bluecritc/:id', (req, res)=>{

    const id = +req.params.id;
    const jogo_index = get_jogo_index_id(id);


    if(jogo_index < 0){
        res.status(404).send({message: 'jogo que você esta tentando editar não foi encontrado' });

        return;
    }

    const novo_jogo = req.body;
    if(!Object.keys(novo_jogo).length){
        
        res.status(400).send({message: 'o body da requisição não pode estar nulo.'});
        
        return;
    } 

    if(!novo_jogo || !novo_jogo.nome || !novo_jogo.ano || !novo_jogo.plataforma || !novo_jogo.nota || !novo_jogo.critica){

        res.status(400).send({message:"Deu ruim jogo invalido. certifique-se de que o body da requisiçao possui todos os dados."});

        return;
    }

    const jogo = get_jogo_id(id);
    jogos[jogo_index]={
        ...jogo,
        ...novo_jogo
    };

    res.send(jogos[jogo_index]);

    
});


app.delete('/bluecritc/:id', (req, res)=> {

    const id = +req.params.id;
    const jogo_index = get_jogo_index_id(id);
    

    //validação
    if(jogo_index < 0){
        res.status(404).send({message: 'jogo que você esta tentando excluir não foi encontrado' });

        return;
    }

    jogos.splice(jogo_index,1); 

    res.send(`jogo excluido com sucesso, ID do jogo: "${id}".`);

});

app.listen(port, () => {

    console.info(`App codando em: http://localhost:${port}`);

});

