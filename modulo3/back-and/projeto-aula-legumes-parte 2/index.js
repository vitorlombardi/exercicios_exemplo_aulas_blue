const express = require('express');
const app = express();
const port = 4000;
app.use(express.json());

const legumes = [

    'Espinafre',
    'Rúcula',
    'Brócolis',
    'Cenoura',
    'Abobrinha',
    'Chuchu'

];


//[get] - /home 

app.get('/', (req, res) => {

    res.send('Ola blumer');

});

//[get] - /legumes - retorna alista de legumes

app.get('/legumes', (req, res) => {

    res.send(legumes);

});

//[get] - /legumes/{id} - retorna um unico legume da lista

app.get('/legumes/:id', (req, res) => {

    const id = req.params.id-1;
    const legume = legumes[id];
    
    
    if (!legume){
        res.send('Legume não encontrado');
        return;
    }

    res.send(legume);

});

// [post] - /legumes - cria um novo legume na lista 

app.post('/legumes', (req, res) => {

    const legume = req.body.legume;
    const id =legumes.length;
    legumes.push(legume);
    
    res.send(`legume adcionado com sucesso:${legume}. ID do legume ${id + 1}`)

});

// [put] - /legumes{id} - atualiza um legume por id

app.put('/legumes/:id', (req, res)=>{

    const id = req.params.id-1;
    const legume = req.body.legume;
    legumes[id] = legume;

    res.send(`legume atualizado com sucesso: "${legume}", ID: "${id + 1}"`);
    
});

// [delete] - /legume{id} - deleta um legume por id

app.delete('/legumes/:id', (req, res)=> {

    const id = req.params.id-1;
    delete legumes[id]; //da para usar legumes.splice(id,1) ou skyscrapers.pop(id)

    res.send(`legume excluido com sucesso, ID do legumes: "${id + 1}"`);

});

app.listen(port, () => {

    console.info(`App codando em: http://localhost:${port}`);

});


