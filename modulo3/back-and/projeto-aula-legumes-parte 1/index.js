const express = require('express');
const app = express();
const port = 3000;

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

    res.send(legume)

});

app.listen(port, () => {

    console.info(`App codando em: http://localhost:${port}`);

});