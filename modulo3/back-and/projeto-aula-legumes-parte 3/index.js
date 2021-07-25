const express = require('express');
const app = express();
const port = 3000;
app.use(express.json());

//tranformando em uma lista de objetos
const legumes = [

    {id:1,
    nome:'Espinafre',
    url:'https://static.tuasaude.com/media/article/ad/da/beneficios-do-espinafre_18895_l.jpg'
    },

    {id:2,
    nome:'Batata',
    url:'http://www.cabanamontefusco.com.br/wp-content/uploads/2019/04/Surpreenda-se-com-curiosidades-sobre-a-batata-Cabana-Montefuscoe.jpg'
    },

    {id:3,
    nome:'Rúcula',
    url:'https://s3.static.brasilescola.uol.com.br/be/2021/02/rucula.jpg'
    },

    {id:4,
    nome:'Brócolis',
    url:'https://conteudo.imguol.com.br/c/entretenimento/53/2020/05/04/brocolis-1588626077191_v2_450x337.jpg.webp'
    },

    {id:5,
    nome:'Abobrinha',
    url:'https://conteudo.imguol.com.br/c/entretenimento/5c/2019/04/25/abobrinha-1556223714538_v2_450x337.jpg.webp'
    },

    {id:6,
    nome:'Chuchu',
    url:'https://gooutside-static-cdn.akamaized.net/wp-content/uploads/sites/6/2019/04/beneficios-do-chuchu-656x420.jpg'
    }

];

const get_legumes_validos = () => legumes.filter(Boolean);
const get_legume_id = id => get_legumes_validos().find(legume=>legume.id===id)
const get_legume_index_id = id => get_legumes_validos().findIndex(legume=>legume.id===id)

//[get] - /home 

app.get('/', (req, res) => {

    res.send('Ola blumer');

});

//[get] - /legumes - retorna alista de legumes

app.get('/legumes', (req, res) => {

    res.send(get_legumes_validos());

});

//[get] - /legumes/{id} - retorna um unico legume da lista

app.get('/legumes/:id', (req, res) => {

    const id = +req.params.id;
    const legume = get_legume_id(id);
    
    if (!legume){
        res.send('Legume não encontrado');
        return;
    }

    res.send(legume);
    //JSON.stringify(legume)passa so os valores(srings)

});

// [post] - /legumes - cria um novo legume na lista 

app.post('/legumes', (req, res) => {

    let legume = req.body;

    //validação
    if(!legume || !legume.nome || !legume.url){

        res.status(400).send({message:"Deu ruim legume invalido. certifique-se de que o body da requisiçao possui 'nome' e 'url'."});

        return;
    }

    legume.id = legumes.length+1;
    let data = legumes
    legume ={id: data.id, ...legume}
    legumes.push(legume);
    
    res.send(legume)

});

// [put] - /legumes{id} - atualiza um legume por id

app.put('/legumes/:id', (req, res)=>{

    const id = +req.params.id;
    const legume_index = get_legume_index_id(id);

    //validação
    if(legume_index < 0){
        res.status(404).send({message: 'legume que você esta tentando editar não foi encontrado' });

        return;
    }

    const novo_legume = req.body;
    if(!Object.keys(novo_legume).length){//object = filmes
        
        res.status(400).send({message: 'o body da requisição não pode estar vasio.'});
        
        return;
    } 

    if(!novo_legume || !novo_legume.nome || !novo_legume.url){

        res.status(400).send({message:"Deu ruim legume invalido. certifique-se de que o body da requisiçao possui 'nome' e 'url'."});

        return;
    }

    const legume = get_legume_id(id);
    legumes[legume_index]={
        ...legume,
        ...novo_legume
    };

    res.send(legumes[legume_index]);

    
});

// [delete] - /legume{id} - deleta um legume por id

app.delete('/legumes/:id', (req, res)=> {

    const id = +req.params.id;
    const legume_index = get_legume_index_id(id);
    

    //validação
    if(legume_index < 0){
        res.status(404).send({message: 'legume que você esta tentando excluir não foi encontrado' });

        return;
    }

    legumes.splice(legume_index,1); //da para usar legumes.splice(id,1) ou skyscrapers.pop(id)


    res.send(`legume excluido com sucesso, ID do legumes: "${id}".`);

});

app.listen(port, () => {

    console.info(`App codando em: http://localhost:${port}`);

});


